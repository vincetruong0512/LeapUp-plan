---
name: doc-to-md
description: Use when any source document for Leap Up (Word, Excel, PowerPoint, PDF, scans, screenshots, Miro/FigJam/Figma board exports, e-mail, ebooks, legacy Office, images) must become Markdown that Claude can read and reason over. Converts losslessly into docs/_sources/, maps boards and diagrams (groups, colours, arrows) via a tiled vision pass, and proves nothing was dropped.
argument-hint: "<file | folder | .zip> [...] [--slug <name>]"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, AskUserQuestion, Agent
user-invocable: true
---

# /doc-to-md — lossless source → Markdown (text + visuals)

Engine (deterministic, no LLM): [engine/convert.py](engine/convert.py) extracts ·
[engine/verify.py](engine/verify.py) proves coverage · [engine/setup.ps1](engine/setup.ps1) one-time install ·
[engine/make_fixtures.py](engine/make_fixtures.py) regression fixtures.
Which export to ask for, per source (Miro, Figma, Google Docs…): [references/source-playbook.md](references/source-playbook.md).

## Goal

Every input becomes a `.md` that keeps **all** of its content: body, headers/footers, comments, tracked
changes, footnotes, every sheet (hidden too), formulas, speaker notes, hidden slides, charts, SmartArt,
images, links, annotations, metadata. **For visual material** (boards, flows, wireframes, design screens)
it also keeps the *meaning carried by layout*: which items are grouped, what colour they are, what
points to what. Downstream work (Leap Up overview, feature specs, user flows) then reads the real
source, not a paraphrase.

## Context (dynamic)

Engine: !`cd "${CLAUDE_PROJECT_DIR:-.}" && (test -x .tools/convert/Scripts/python.exe && .tools/convert/Scripts/python.exe -c "from markitdown import MarkItDown; import docx, openpyxl, pptx, pymupdf; print('OK')" 2>/dev/null || echo "MISSING — run setup.ps1 (Phase A.1)")`
Existing conversions: !`cd "${CLAUDE_PROJECT_DIR:-.}" && ls -d docs/_sources/*/ 2>/dev/null | tail -5 | tr '\n' ' '`
Today: !`date +%Y-%m-%d`

## Constraints — hard rules

1. **Machine extracts, Claude never retypes.** All text that has a text layer comes from `convert.py`.
   Claude must not rewrite, summarise, translate, reorder or "clean up" it. Claude adds only what the
   vision pass sees (Phase D): verbatim text that exists only as pixels, and the structure of visual pages.
2. **Never claim done without `verify.py`.** Report each file's status exactly as printed
   (PASS / INCOMPLETE / FAIL / UNVERIFIED-TEXT). Never round a FAIL up to "converted".
3. **No silent drops.** A file that fails stays in the report as FAIL with its error. Zero files
   converted → stop and say so.
4. **Privacy.** `docs/_sources/` is gitignored: inputs may be private. Frontmatter carries the
   filename only, never a local path. Don't suggest committing conversions unless the user says the
   source is public. Never send source content to an outside service.
5. **Source language stays.** Vietnamese stays Vietnamese — no translation.
6. **Seen ≠ inferred.** In Phase D, readable text goes in verbatim; unreadable → `[illegible]`. An
   arrow you can see is a connection; an arrow you *assume* is not. Anything interpretive (e.g. "this
   looks like a happy path") goes in an `_italic note_` so it can't be mistaken for source content.
7. **Ask before writing.** Show the plan (Phase B) and get a yes before the first write.

## Approach

### Phase A — Intake

1. **Engine probe.** If Context shows `MISSING`, say setup is needed (≈200 MB one-time download into
   `.tools/convert/`, gitignored; needs `uv`) and ask before running:
   `powershell -ExecutionPolicy Bypass -File .claude/skills/doc-to-md/engine/setup.ps1`.
2. **Resolve inputs:** files, folders (recursive; `~$` lock files and dotfiles skipped), `.zip`
   (extracted and recursed). No argument → ask which files/folder.
3. **Check the source format** against [references/source-playbook.md](references/source-playbook.md).
   If a better export exists (e.g. a Miro board supplied only as a screenshot, when a vector PDF would
   keep the text machine-readable), tell the user once, in one line, then continue with what was given.
4. **Output folder:** `docs/_sources/{YYYY-MM-DD}-{slug}/`. Slug = `--slug` or the main input name
   (kebab-case ASCII ≤ 50). Folder exists → ask: new dated folder (default) or overwrite (list files).

### Phase B — Plan (no write before Y)

5. Dry run — writes nothing:
   `PYTHONUTF8=1 .tools/convert/Scripts/python.exe .claude/skills/doc-to-md/engine/convert.py <inputs> --out <folder> --plan`
6. Tell the user in plain prose: how many files, which kinds, which go through LibreOffice/Calibre
   first, the output folder, that it stays out of git, any MISSING tool. Ask `Apply? (Y / change)`.

### Phase C — Convert

7. Run the same command without `--plan`. Output: `{stem}.md` per input, `assets/{stem}/` (images,
   page renders, tiles), `assets/_intermediate/`, `assets/_archives/`, `_manifest.json`.
8. Show the per-file lines verbatim, including `!` warnings (encoding, tiling below legibility zoom).

**How PDF pages are classified** (automatic):

| Page kind | Detected by | Output |
|---|---|---|
| Text | normal text layer, few shapes | text in reading order + tables |
| **Visual** | oversized page (> A2, typical of Miro/FigJam/Figma exports), ≥ 12 coloured shapes, ≥ 15 curves/diagonals (connectors), or images cover ≥ 35 % | **positioned item table** (`pN.M` ID · text · colour of the sticky/card it sits on · position) + overview render + legibility tiles → *required* vision item |
| Scan | < 25 chars of text, has images/drawings | overview + tiles → *required* verbatim transcription |

Standalone images (`.png/.jpg/…` — screenshots, board exports) are tiled the same way at native resolution.

### Phase D — Vision pass (only if `vision-pending` blocks exist)

9. Find them: `grep -n "vision-pending:" <folder>/*.md`. Three kinds:
   - **Visual page** (`is visual (board / diagram / design)`) — text already extracted as `pN.M` items.
   - **Scan / image only** (`no text layer` or `Image …`) — everything must be transcribed.
   - **Optional embedded image** (`| if-text-visible -->`) — transcribe if it holds text, else mark reviewed.
10. More than 20 required items → tell the user the count and ask first. For many items, spawn read-only
    `Agent` subagents in parallel (one batch each). They **return** results; only the main thread edits.
11. **Reading order:** `Read` the overview first (layout, groups, arrows, colours). Open a detail tile only
    where the overview is too small to resolve: raster text, connector labels, arrowheads, crowded
    areas. For scans/images, read every tile, since the text exists only as pixels. Tiles overlap 10 %, so
    text on a seam appears twice. Transcribe it once.
12. Replace **only that block** with:

    **Visual page:**
    ```
    <!-- vision-transcribed: {id} | {label} | structure by vision, not machine-verified -->
    ![overview]({overview path})

    #### Groups
    - {frame / lane / cluster title, verbatim if written on the board}: p3.2, p3.3, p3.7
    #### Connections
    - p3.2 → p3.3 — {arrow label verbatim, or "unlabelled"} {(dashed) / (bi-directional) if seen}
    #### Colour meaning
    - {only if a legend on the board states it, verbatim; otherwise "no legend on board"}
    #### Text visible only in the image
    - {verbatim text not present in the item table — e.g. text inside pasted screenshots}
    #### Flow (only if the page is a flow/journey)
    ```mermaid
    flowchart LR
      p3_2["Sign up"] --> p3_3["Verify email"]
    ```
    <!-- /vision-transcribed: {id} -->
    ```
    Every `pN.M` item must appear in at least one Group or Connection, or be listed under
    `- Ungrouped: …`. That is how you check nothing on the board was skipped. Mermaid node labels are
    copied from the item table, not retyped from the image.

    **Scan / image:** same wrapper (`| verbatim, not machine-verified`), the overview link, then the
    verbatim text with line breaks; lists and tables as Markdown. If it's a board or screen, add the
    Groups / Connections sections too, describing items by their visible text.

    **Optional image with no text:** `<!-- vision-reviewed: {id} | no text visible -->` + image link.
13. These are edits to gitignored files this skill just created: show a one-line summary per block, no
    per-block diff needed.

### Phase E — Fidelity gate

14. `PYTHONUTF8=1 .tools/convert/Scripts/python.exe .claude/skills/doc-to-md/engine/verify.py <folder>`
    re-extracts each source by an **independent** path (raw OOXML, pdfminer, raw bytes), checks token
    coverage (≥ 99.5 %) and structure counts (pages/slides/sheets/images), stamps `status` +
    `fidelity_coverage` into each `.md`, writes `_conversion-report.md`.
15. Any **FAIL** → read `## Gaps`, find the cause in the source, fix the *engine* (or report it); never
    hand-patch the `.md` to make the number pass. Vision output is labelled not-machine-verified.

### Phase F — Report

16. Reply with the report table (as printed), the folder link, anything still INCOMPLETE/FAIL, and, for
    boards, a one-line count per visual page (`items · groups · connections`).
17. **Project fit** (per [../../rules/mvp-focus.md](../../rules/mvp-focus.md)): for a source about Leap Up, add
    a short list of what it contributes, tagged `MVP` / `P2` / `OUT` / `OPEN` against the scope table in
    `CLAUDE.md`, with MVP items first and each item citing its line/page. Anything that contradicts the
    current scope (e.g. a screen for an excluded module) is `OPEN` and goes into that conversion folder's
    `_comparison.md`. Then suggest the next MVP step (e.g. feed into the Leap Up overview, or `/userflow`
    for an MVP flow).

## What each format keeps

| Input | Engine | Kept beyond body text |
|---|---|---|
| .docx/.docm | pandoc (bundled) + python-docx | headers/footers, comments, tracked changes, footnotes, merged cells, images, metadata, charts, SmartArt |
| .xlsx/.xlsm | openpyxl | every sheet incl. hidden, `value ⟨=formula⟩`, merged cells, comments, links, validation, names, images, charts |
| .pptx/.pptm | python-pptx | slide order, hidden slides, tables, charts as tables, images, notes, comments, SmartArt |
| .pdf | PyMuPDF | per-page text + tables, images, links, annotations, bookmarks, metadata; **visual pages → item table + tiles**; scans → tiles |
| .doc .rtf .odt / .xls .ods / .ppt .odp | LibreOffice → OOXML → above | same as the modern format |
| .epub .fb2 / .mobi .azw3 | pandoc / Calibre | metadata, images |
| .eml | Python email | headers, body, every attachment converted separately |
| .html .csv .tsv .ipynb .msg | markitdown | — |
| .json .xml .yaml / .md .txt | verbatim | original frontmatter kept as a fenced block |
| images | overview + tiles → vision | — |

## Pitfalls

- **One giant render is not enough.** Vision downsizes anything over ~1568 px; a 4000-pt Miro page at
  that size makes 7-pt sticky text unreadable. That's why tiles exist. If the engine warns it tiled
  below legibility zoom, raise `DOC_TO_MD_MAX_TILES` (default 24) and re-run that file.
- **Board text flattened to outlines.** Some exports turn text into vector paths, so there is no text
  layer and the page is classified as a scan. Everything must then be transcribed from tiles. Ask
  for a re-export with text kept (see playbook).
- **Colour names are coarse** (`light yellow #fff9b1`). The hex is exact. Meaning of colours comes only
  from a legend on the board, never assumed.
- **Arrow direction** is not machine-detected. Only claim a direction when the arrowhead is visible.
- **Encrypted PDFs / protected Office files** fail. Ask for an unlocked copy; never bypass protection.
- **PDF `(cid:N)` / TCVN warnings** mean the text layer is unreliable: treat those pages as vision items.
- **Formula cells without cached values** show `(no cached value) ⟨=…⟩`. That's honest, not a loss.

## Regression

After changing the engine:
`PYTHONUTF8=1 .tools/convert/Scripts/python.exe .claude/skills/doc-to-md/engine/make_fixtures.py`, convert
`fixtures/` into `tmp/fx`, run `verify.py`. Expect: docx/pptx/xlsx PASS; `sample.pdf` INCOMPLETE (page 2
scan); `sample-board.pdf` INCOMPLETE with 7 items, each sticky with its own fill colour, overview +
tiles; `sample-board.png` INCOMPLETE with tiles. Then delete a line from an output `.md` and confirm
`verify.py` reports FAIL with that text.
