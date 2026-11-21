#!/usr/bin/env python3
"""/doc-to-md engine — convert common document types to Markdown without losing content.

Machine extracts, Claude only fills gaps: this script does ALL extraction deterministically.
Pages/images with no text layer are rendered to PNG and left as `<!-- vision-pending -->`
blocks for Claude to transcribe verbatim (SKILL.md Phase D). Fidelity is then proven by
verify.py (independent second extraction), not asserted.

Usage (from repo root):
  PYTHONUTF8=1 .tools/convert/Scripts/python.exe .claude/skills/doc-to-md/engine/convert.py \
      <file|folder|zip> [...] --out docs/_sources/{YYYY-MM-DD}-{slug} [--plan]

  --plan   dry run: print file -> engine table, write nothing (feeds the L1 approval gate)

Output per input `{stem}.md` + `assets/{stem}/...`, plus `_manifest.json` (local paths, gitignored
folder) used by verify.py. Frontmatter carries the source FILENAME only, never its local path.
"""
from __future__ import annotations

import argparse
import email
import email.policy
import glob
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from datetime import date
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[4]
ENGINE_VERSION = "1.1.0"

# ------------------------------------------------------------------ tool discovery
def find_tool(name: str, candidates: list[str]) -> str | None:
    hit = shutil.which(name)
    if hit:
        return hit
    for pattern in candidates:
        for p in glob.glob(pattern):
            if Path(p).is_file():
                return p
    return None


PANDOC = os.environ.get("PANDOC") or find_tool("pandoc", [str(ROOT / ".tools/export/pandoc-*/pandoc.exe"), str(ROOT / ".tools/export/pandoc-*/bin/pandoc"),
                                                        str(ROOT / ".tools/convert/Lib/site-packages/pypandoc/files/pandoc*"), str(ROOT / ".tools/convert/lib/python3*/site-packages/pypandoc/files/pandoc")])
SOFFICE = find_tool("soffice", [r"C:\Program Files\LibreOffice\program\soffice.exe", r"C:\Program Files (x86)\LibreOffice\program\soffice.exe", "/Applications/LibreOffice.app/Contents/MacOS/soffice"])
EBOOK_CONVERT = find_tool("ebook-convert", [r"C:\Program Files\Calibre2\ebook-convert.exe", "/Applications/calibre.app/Contents/MacOS/ebook-convert"])

# ------------------------------------------------------------------ type routing
ROUTES = {
    ".docx": "pandoc+python-docx", ".docm": "pandoc+python-docx",
    ".xlsx": "openpyxl", ".xlsm": "openpyxl",
    ".pptx": "python-pptx", ".pptm": "python-pptx",
    ".pdf": "pymupdf",
    ".doc": "libreoffice->docx", ".rtf": "libreoffice->docx", ".odt": "libreoffice->docx",
    ".xls": "libreoffice->xlsx", ".ods": "libreoffice->xlsx",
    ".ppt": "libreoffice->pptx", ".odp": "libreoffice->pptx",
    ".epub": "pandoc", ".mobi": "calibre->epub", ".azw3": "calibre->epub", ".azw": "calibre->epub", ".fb2": "pandoc",
    ".html": "markitdown", ".htm": "markitdown", ".csv": "markitdown", ".tsv": "markitdown",
    ".ipynb": "markitdown", ".msg": "markitdown", ".eml": "email",
    ".json": "verbatim-code", ".xml": "verbatim-code", ".yaml": "verbatim-code", ".yml": "verbatim-code",
    ".md": "verbatim", ".markdown": "verbatim", ".txt": "verbatim",
    ".png": "image->vision", ".jpg": "image->vision", ".jpeg": "image->vision", ".webp": "image->vision",
    ".gif": "image->vision", ".bmp": "image->vision", ".tif": "image->vision", ".tiff": "image->vision",
    ".zip": "unzip->recurse",
}
LIBREOFFICE_TARGET = {".doc": "docx", ".rtf": "docx", ".odt": "docx", ".xls": "xlsx", ".ods": "xlsx", ".ppt": "pptx", ".odp": "pptx"}
IMAGE_EXT = {k for k, v in ROUTES.items() if v == "image->vision"}


def route_for(path: Path) -> str:
    return ROUTES.get(path.suffix.lower(), "markitdown(fallback)")


# ------------------------------------------------------------------ result container
class Result:
    def __init__(self, engine: str):
        self.engine = engine
        self.parts: list[str] = []
        self.vision: list[dict] = []   # {"id","kind","image","required"}
        self.warnings: list[str] = []
        self.stats: dict = {}

    def add(self, text: str):
        if text is not None:
            self.parts.append(text.rstrip() + "\n")

    def vision_block(self, vid: str, image_rel: str, label: str, required: bool):
        self.vision.append({"id": vid, "kind": label, "image": image_rel, "required": required})
        return (f"<!-- vision-pending: {vid} | {label} | {'required' if required else 'if-text-visible'} -->\n"
                f"![{label}]({image_rel})\n<!-- /vision-pending: {vid} -->\n")


# ------------------------------------------------------------------ helpers
def esc_cell(v) -> str:
    s = "" if v is None else str(v)
    return s.replace("|", "\\|").replace("\r\n", "<br>").replace("\n", "<br>")


def md_table(rows: list[list]) -> str:
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [list(r) + [""] * (width - len(r)) for r in rows]
    out = ["| " + " | ".join(esc_cell(c) for c in rows[0]) + " |", "|" + "---|" * width]
    out += ["| " + " | ".join(esc_cell(c) for c in r) + " |" for r in rows[1:]]
    return "\n".join(out) + "\n"


def html_table(grid: list[list[dict]]) -> str:
    """grid cells: {"text","colspan","rowspan"} or None for covered cells."""
    out = ["<table>"]
    for r in grid:
        out.append("<tr>")
        for c in r:
            if c is None:
                continue
            attrs = ""
            if c.get("colspan", 1) > 1:
                attrs += f' colspan="{c["colspan"]}"'
            if c.get("rowspan", 1) > 1:
                attrs += f' rowspan="{c["rowspan"]}"'
            out.append(f"<td{attrs}>{html.escape(str(c.get('text') or '')).replace(chr(10), '<br>')}</td>")
        out.append("</tr>")
    out.append("</table>")
    return "\n".join(out) + "\n"


TCVN_CHARS = set("¸µ¶·¹¨©ª«¬®¯°±²³´½¾ÆÇÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß")


def mojibake_warnings(text: str) -> list[str]:
    w = []
    if not text:
        return w
    fffd = text.count("\ufffd")
    if fffd > 3:
        w.append(f"{fffd} replacement characters (U+FFFD) — source encoding/font not decodable")
    if "(cid:" in text:
        w.append("'(cid:N)' glyph codes found — PDF font has no Unicode map (Identity-H); affected text needs vision")
    letters = [ch for ch in text if ch.isalpha()]
    if letters:
        ratio = sum(ch in TCVN_CHARS for ch in letters) / len(letters)
        if ratio > 0.03:
            w.append(f"possible TCVN3/VNI legacy Vietnamese encoding ({ratio:.0%} suspicious letters) — verify text against the original")
    return w


def ooxml_extras(zpath: Path, prefix: str) -> tuple[str, dict]:
    """Charts + SmartArt text embedded in any OOXML package (pandoc/python-pptx drop or flatten these)."""
    ns = {"c": "http://schemas.openxmlformats.org/drawingml/2006/chart",
          "a": "http://schemas.openxmlformats.org/drawingml/2006/main"}
    parts, n_charts, n_smart = [], 0, 0
    with zipfile.ZipFile(zpath) as z:
        names = z.namelist()
        for name in sorted(n for n in names if re.match(rf"{prefix}/charts/chart\d+\.xml$", n)):
            n_charts += 1
            root = ET.fromstring(z.read(name))
            title = " ".join(t.text or "" for t in root.findall(".//c:title//a:t", ns)).strip()
            parts.append(f"### Chart {n_charts}{(' — ' + title) if title else ''} (`{name}`)\n")
            for ser in root.iter("{%s}ser" % ns["c"]):
                sname = " ".join(v.text or "" for v in ser.findall("./c:tx//c:v", ns)) or "(unnamed series)"
                cats = [v.text for v in ser.findall("./c:cat//c:pt/c:v", ns)]
                vals = [v.text for v in ser.findall("./c:val//c:pt/c:v", ns)] or [v.text for v in ser.findall("./c:yVal//c:pt/c:v", ns)]
                rows = [["Category", sname]] + [[cats[i] if i < len(cats) else i + 1, vals[i]] for i in range(len(vals))]
                parts.append(md_table(rows))
        for name in sorted(n for n in names if re.match(rf"{prefix}/diagrams/data\d+\.xml$", n)):
            n_smart += 1
            root = ET.fromstring(z.read(name))
            texts = [t.text for t in root.iter("{%s}t" % ns["a"]) if t.text and t.text.strip()]
            parts.append(f"### SmartArt {n_smart} (`{name}`)\n" + "".join(f"- {t}\n" for t in texts))
    body = ("## Embedded charts and diagrams\n\n" + "\n".join(parts)) if parts else ""
    return body, {"charts": n_charts, "smartart": n_smart}


def run(cmd: list[str], cwd: Path | None = None, timeout: int = 300) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout)


# ------------------------------------------------------------------ converters
def conv_docx(src: Path, out: Path, stem: str) -> Result:
    import docx

    res = Result("pandoc+python-docx")
    if not PANDOC:
        raise RuntimeError("pandoc not found (expected under .tools/export/pandoc-*/)")
    with zipfile.ZipFile(src) as z:
        body_xml = z.read("word/document.xml").decode("utf-8", "replace")
        n_media = len([n for n in z.namelist() if n.startswith("word/media/")])
    has_merges = "w:gridSpan" in body_xml or "w:vMerge" in body_xml
    fmt = "gfm-pipe_tables" if has_merges else "gfm"
    # shift headings so the document's own H1s sit under the file-name H1 written by convert_file
    cp = run([PANDOC, str(src.resolve()), "-t", fmt, "--track-changes=all", "--wrap=none", "--shift-heading-level-by=1",
              f"--extract-media=assets/{stem}"], cwd=out)
    if cp.returncode != 0:
        raise RuntimeError(f"pandoc failed: {cp.stderr.strip()[:400]}")
    if cp.stderr.strip():
        res.warnings.append("pandoc: " + cp.stderr.strip().replace("\n", " ")[:300])

    d = docx.Document(str(src))
    cpp = d.core_properties
    props = {k: getattr(cpp, k) for k in ("title", "subject", "author", "last_modified_by", "created", "modified", "revision", "keywords", "comments") if getattr(cpp, k, None)}
    if props:
        res.add("## Document properties\n\n" + md_table([["Property", "Value"]] + [[k, v] for k, v in props.items()]))

    hf, seen = [], set()
    for i, sec in enumerate(d.sections, start=1):
        for label, part in (("Header", sec.header), ("First-page header", sec.first_page_header), ("Even-page header", sec.even_page_header),
                            ("Footer", sec.footer), ("First-page footer", sec.first_page_footer), ("Even-page footer", sec.even_page_footer)):
            if part.is_linked_to_previous and i > 1:
                continue
            texts = [p.text for p in part.paragraphs if p.text.strip()]
            for t in part.tables:
                texts += [" | ".join(c.text for c in row.cells) for row in t.rows]
            key = (label, tuple(texts))
            if texts and key not in seen:
                seen.add(key)
                hf.append(f"- **Section {i} — {label}:** " + " / ".join(texts))
    if hf:
        res.add("## Page headers and footers\n\n" + "\n".join(hf) + "\n")

    res.add(cp.stdout)
    extras, xs = ooxml_extras(src, "word")
    res.add(extras)
    extracted = len([p for p in (out / "assets" / stem).rglob("*") if p.is_file()]) if (out / "assets" / stem).exists() else 0
    res.stats = {"images_in_source": n_media, "images_extracted": extracted, "tables": body_xml.count("<w:tbl>"),
                 "sections": len(d.sections), "merged_tables_as_html": has_merges, **xs}
    return res


def conv_xlsx(src: Path, out: Path, stem: str) -> Result:
    import openpyxl
    from openpyxl.utils import get_column_letter

    res = Result("openpyxl")
    wb_f = openpyxl.load_workbook(src, data_only=False)
    wb_v = openpyxl.load_workbook(src, data_only=True)
    n_formulas = 0
    for ws in wb_f.worksheets:
        wv = wb_v[ws.title]
        state = "" if ws.sheet_state == "visible" else f" ({ws.sheet_state})"
        res.add(f"## Sheet: {ws.title}{state}\n")
        cells = [c for row in ws.iter_rows() for c in row if c.value is not None]
        if not cells:
            res.add("_(empty sheet)_\n")
        else:
            min_r, max_r = min(c.row for c in cells), max(c.row for c in cells)
            min_c, max_c = min(c.column for c in cells), max(c.column for c in cells)
            for mr in ws.merged_cells.ranges:
                min_r, min_c = min(min_r, mr.min_row), min(min_c, mr.min_col)
                max_r, max_c = max(max_r, mr.max_row), max(max_c, mr.max_col)
            res.add(f"Range `{get_column_letter(min_c)}{min_r}:{get_column_letter(max_c)}{max_r}`\n")

            def show(r, c):
                f = ws.cell(r, c).value
                v = wv.cell(r, c).value
                if isinstance(f, str) and f.startswith("="):
                    nonlocal n_formulas
                    n_formulas += 1
                    return f"{v if v is not None else '(no cached value)'} ⟨{f}⟩"
                return "" if f is None else f

            merges = {(m.min_row, m.min_col): m for m in ws.merged_cells.ranges}
            covered = {(r, c) for m in ws.merged_cells.ranges for r in range(m.min_row, m.max_row + 1)
                       for c in range(m.min_col, m.max_col + 1) if (r, c) != (m.min_row, m.min_col)}
            header = [""] + [get_column_letter(c) for c in range(min_c, max_c + 1)]
            if merges:
                grid = [[{"text": h} for h in header]]
                for r in range(min_r, max_r + 1):
                    row = [{"text": str(r)}]
                    for c in range(min_c, max_c + 1):
                        if (r, c) in covered:
                            row.append(None)
                        else:
                            m = merges.get((r, c))
                            row.append({"text": show(r, c), "colspan": (m.max_col - m.min_col + 1) if m else 1,
                                        "rowspan": (m.max_row - m.min_row + 1) if m else 1})
                    grid.append(row)
                res.add(html_table(grid))
            else:
                rows = [header] + [[r] + [show(r, c) for c in range(min_c, max_c + 1)] for r in range(min_r, max_r + 1)]
                res.add(md_table(rows))

        comments = [[c.coordinate, c.comment.author or "", c.comment.text] for row in ws.iter_rows() for c in row if c.comment]
        if comments:
            res.add("### Cell comments\n\n" + md_table([["Cell", "Author", "Comment"]] + comments))
        links = [[c.coordinate, c.hyperlink.target or c.hyperlink.location] for row in ws.iter_rows() for c in row if c.hyperlink]
        if links:
            res.add("### Hyperlinks\n\n" + md_table([["Cell", "Target"]] + links))
        dvs = [[str(dv.sqref), dv.type or "", dv.formula1 or "", dv.formula2 or ""] for dv in ws.data_validations.dataValidation]
        if dvs:
            res.add("### Data validation\n\n" + md_table([["Cells", "Type", "Rule / list", "Rule 2"]] + dvs))

    names = [[n, dn.attr_text] for n, dn in wb_f.defined_names.items()]
    for ws in wb_f.worksheets:
        names += [[f"{ws.title}!{n}", dn.attr_text] for n, dn in ws.defined_names.items()]
    if names:
        res.add("## Defined names\n\n" + md_table([["Name", "Refers to"]] + names))

    img_dir = out / "assets" / stem
    with zipfile.ZipFile(src) as z:
        media = [n for n in z.namelist() if n.startswith("xl/media/")]
        if media:
            img_dir.mkdir(parents=True, exist_ok=True)
            lines = []
            for i, n in enumerate(media, 1):
                dest = img_dir / Path(n).name
                dest.write_bytes(z.read(n))
                rel = f"assets/{stem}/{dest.name}"
                lines.append(res.vision_block(f"{stem}-img{i}", rel, f"Embedded image {i}", required=False))
            res.add("## Embedded images\n\n" + "\n".join(lines))
    extras, xs = ooxml_extras(src, "xl")
    res.add(extras)
    res.stats = {"sheets": len(wb_f.worksheets), "hidden_sheets": sum(ws.sheet_state != "visible" for ws in wb_f.worksheets),
                 "formulas": n_formulas, "images_in_source": len(media), "images_extracted": len(media), **xs}
    return res


def conv_pptx(src: Path, out: Path, stem: str) -> Result:
    from pptx import Presentation
    from pptx.enum.shapes import MSO_SHAPE_TYPE

    res = Result("python-pptx")
    prs = Presentation(str(src))
    img_dir = out / "assets" / stem
    n_img = 0

    def table_md(tbl) -> str:
        cells = [[tbl.cell(r, c) for c in range(len(tbl.columns))] for r in range(len(tbl.rows))]
        if any(c.is_merge_origin for row in cells for c in row):
            grid = [[None if c.is_spanned else {"text": c.text, "colspan": c.span_width if c.is_merge_origin else 1,
                                                 "rowspan": c.span_height if c.is_merge_origin else 1} for c in row] for row in cells]
            return html_table(grid)
        return md_table([[c.text for c in row] for row in cells])

    def walk(shapes, slide_no, depth=0) -> list[str]:
        nonlocal n_img
        out_parts = []
        for sh in sorted(shapes, key=lambda s: ((s.top or 0), (s.left or 0))):
            if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
                out_parts += walk(sh.shapes, slide_no, depth + 1)
                continue
            if sh.has_text_frame and sh.text_frame.text.strip():
                if sh.is_placeholder and sh.placeholder_format.type is not None and "TITLE" in str(sh.placeholder_format.type):
                    continue  # already used as the slide heading
                lines = []
                for p in sh.text_frame.paragraphs:
                    t = "".join(r.text for r in p.runs) or p.text
                    if t.strip():
                        lines.append("  " * p.level + "- " + t)
                out_parts.append("\n".join(lines) + "\n")
            if getattr(sh, "has_table", False) and sh.has_table:
                out_parts.append(table_md(sh.table))
            if getattr(sh, "has_chart", False) and sh.has_chart:
                ch = sh.chart
                title = ch.chart_title.text_frame.text if ch.has_title else sh.name
                rows = [["Category"] + [s.name for s in ch.plots[0].series]] if ch.plots else []
                if ch.plots:
                    cats = list(ch.plots[0].categories)
                    series = [list(s.values) for s in ch.plots[0].series]
                    rows += [[cats[i]] + [s[i] if i < len(s) else "" for s in series] for i in range(len(cats))]
                out_parts.append(f"**Chart — {title}**\n\n" + md_table(rows))
            if sh.shape_type == MSO_SHAPE_TYPE.PICTURE:
                n_img += 1
                img_dir.mkdir(parents=True, exist_ok=True)
                dest = img_dir / f"slide{slide_no}-img{n_img}.{sh.image.ext}"
                dest.write_bytes(sh.image.blob)
                alt = (sh._element.xpath("./p:nvPicPr/p:cNvPr/@descr") or [""])[0] or sh.name
                out_parts.append(res.vision_block(f"{stem}-s{slide_no}-img{n_img}", f"assets/{stem}/{dest.name}",
                                                  f"Slide {slide_no} image: {alt}", required=False))
        return out_parts

    hidden = 0
    for i, slide in enumerate(prs.slides, start=1):
        is_hidden = slide._element.get("show") == "0"
        hidden += is_hidden
        title = slide.shapes.title.text if slide.shapes.title is not None and slide.shapes.title.text.strip() else "(untitled)"
        res.add(f"## Slide {i} — {title}{' (hidden slide)' if is_hidden else ''}\n")
        res.add("\n".join(walk(slide.shapes, i)))
        if slide.has_notes_slide and slide.notes_slide.notes_text_frame.text.strip():
            res.add("### Speaker notes\n\n" + slide.notes_slide.notes_text_frame.text + "\n")

    with zipfile.ZipFile(src) as z:
        comments = []
        for n in sorted(x for x in z.namelist() if re.match(r"ppt/comments/.*\.xml$", x)):
            root = ET.fromstring(z.read(n))
            comments += [t.text for t in root.iter() if t.tag.endswith("}text") and t.text]
        n_media = len([n for n in z.namelist() if n.startswith("ppt/media/")])
    if comments:
        res.add("## Slide comments\n\n" + "".join(f"- {c}\n" for c in comments))
    extras, xs = ooxml_extras(src, "ppt")
    res.add(extras)
    res.stats = {"slides": len(prs.slides), "hidden_slides": hidden, "images_in_source": n_media, "images_extracted": n_img, **xs}
    if n_img < n_media:
        res.warnings.append(f"{n_media - n_img} media file(s) in package not placed on a slide (layouts/masters/backgrounds)")
    return res


# ------------------------------------------------------------------ visual pages (boards, diagrams, designs)
# Claude's vision reads an image at most ~1568 px on its long side; anything bigger is downscaled and small
# text on a Miro/FigJam board becomes unreadable. So visual content is rendered as one overview (layout)
# plus overlapping tiles at a zoom where the smallest text is still legible.
VISION_MAX_PX = 1568
MIN_TEXT_PX = 14          # rendered glyph height (px) that stays legible
TILE_OVERLAP = 0.10
MAX_TILES = int(os.environ.get("DOC_TO_MD_MAX_TILES", "24"))


def colour_name(rgb) -> str:
    """Coarse human name for a fill colour — Miro/FigJam encode meaning in sticky colours."""
    import colorsys
    r, g, b = (float(x) for x in rgb[:3])
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    if v < 0.2:
        return "black"
    if s < 0.15:
        return "white" if v > 0.9 else "gray"
    deg = h * 360
    for limit, name in ((15, "red"), (40, "orange"), (70, "yellow"), (165, "green"), (200, "cyan"),
                        (255, "blue"), (290, "violet"), (335, "pink"), (361, "red")):
        if deg < limit:
            return ("light " if v > 0.85 and s < 0.45 else "") + name
    return "?"


def hex_of(rgb) -> str:
    return "#" + "".join(f"{round(max(0, min(1, c)) * 255):02x}" for c in rgb[:3])


def visual_profile(page) -> dict:
    """Decide whether a page carries meaning in its *layout* (board, flow, wireframe, design) rather
    than only in its text. Table borders and rules are thin h/v lines and do not count."""
    import pymupdf
    pr = page.rect
    parea = max(pr.get_area(), 1)
    try:
        drawings = page.get_drawings()
    except Exception:
        drawings = []
    shapes, connectors = [], 0
    for d in drawings:
        r = pymupdf.Rect(d.get("rect") or (0, 0, 0, 0))
        items = d.get("items") or []
        if any(it[0] in ("c", "qu") for it in items) or any(
                it[0] == "l" and abs(it[1].x - it[2].x) > 2 and abs(it[1].y - it[2].y) > 2 for it in items):
            connectors += 1                       # curves / diagonal lines: arrows, connectors, icons
        fill = d.get("fill")
        if fill and min(r.width, r.height) >= 3 and r.get_area() < 0.5 * parea and colour_name(fill) not in ("white",):
            shapes.append((r, fill))              # filled shape: sticky note, card, button, swimlane
    img_area = 0.0
    for info in page.get_images(full=True):
        try:
            for ir in page.get_image_rects(info[0]):
                img_area += (ir & pr).get_area()
        except Exception:
            pass
    oversized = max(pr.width, pr.height) > 1700   # larger than A2 — typical of Miro/FigJam/Figma exports
    visual = oversized or len(shapes) >= 12 or connectors >= 15 or img_area / parea >= 0.35
    return {"visual": visual, "shapes": shapes, "connectors": connectors, "image_ratio": round(img_area / parea, 2),
            "oversized": oversized}


def render_for_vision(page, dest_dir: Path, prefix: str, zoom: float, warnings: list[str], label: str) -> tuple[str, list[str]]:
    """Render `page` (a PDF page, or an image opened via pymupdf) as overview + legible tiles.
    Returns (overview file name, [tile file names]). All names end in -render.png (verify.py ignores them
    when counting extracted source images)."""
    import math
    import pymupdf
    dest_dir.mkdir(parents=True, exist_ok=True)
    pr = page.rect
    long_side = max(pr.width, pr.height)
    ov_zoom = min(VISION_MAX_PX / long_side, max(zoom, 1.0))
    overview = f"{prefix}-overview-render.png"
    page.get_pixmap(matrix=pymupdf.Matrix(ov_zoom, ov_zoom)).save(str(dest_dir / overview))
    if long_side * zoom <= VISION_MAX_PX * 1.05:
        return overview, []                       # the overview is already full-detail

    def grid(z):
        tile = VISION_MAX_PX / z
        step = tile * (1 - TILE_OVERLAP)
        cols = max(1, math.ceil((pr.width - tile) / step) + 1) if pr.width > tile else 1
        rows = max(1, math.ceil((pr.height - tile) / step) + 1) if pr.height > tile else 1
        return tile, step, cols, rows

    want = zoom
    tile, step, cols, rows = grid(zoom)
    while cols * rows > MAX_TILES and zoom > ov_zoom:
        zoom *= 0.9
        tile, step, cols, rows = grid(zoom)
    if zoom < want * 0.95:
        warnings.append(f"{label}: tiled at {zoom / want:.0%} of the legibility zoom (cap {MAX_TILES} tiles; "
                        f"raise DOC_TO_MD_MAX_TILES for more detail)")
    names = []
    for r in range(rows):
        for c in range(cols):
            x0, y0 = pr.x0 + c * step, pr.y0 + r * step
            clip = pymupdf.Rect(x0, y0, min(x0 + tile, pr.x1), min(y0 + tile, pr.y1))
            name = f"{prefix}-tile-r{r + 1}c{c + 1}-render.png"
            page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom), clip=clip).save(str(dest_dir / name))
            names.append(name)
    return overview, names


def visual_block(res: Result, vid: str, rel_dir: str, overview: str, tiles: list[str], label: str, hint: str) -> str:
    res.vision.append({"id": vid, "kind": label, "image": f"{rel_dir}/{overview}", "tiles": [f"{rel_dir}/{t}" for t in tiles],
                       "required": True, "visual": True})
    body = f"<!-- vision-pending: {vid} | {label} | required -->\n![{label} — overview]({rel_dir}/{overview})\n\n"
    if hint:
        body += f"_{hint}_\n\n"
    if tiles:
        pos = [re.search(r"tile-(r\d+c\d+)", t).group(1) for t in tiles]
        body += (f"Detail tiles ({len(tiles)}, row-major, {int(TILE_OVERLAP * 100)}% overlap): "
                 + " · ".join(f"[{p}]({rel_dir}/{t})" for p, t in zip(pos, tiles)) + "\n")
    return body + f"<!-- /vision-pending: {vid} -->\n"


def small_font_size(page, default: float = 10.0) -> float:
    """20th-percentile span size: the text the tiles must keep legible."""
    sizes = sorted(s["size"] for b in page.get_text("dict").get("blocks", []) if b.get("type") == 0
                   for l in b["lines"] for s in l["spans"] if s["text"].strip() and s["size"] > 0)
    return sizes[len(sizes) // 5] if sizes else default


def conv_pdf(src: Path, out: Path, stem: str) -> Result:
    import pymupdf

    res = Result("pymupdf")
    doc = pymupdf.open(str(src))
    img_dir = out / "assets" / stem
    meta = {k: v for k, v in (doc.metadata or {}).items() if v}
    if meta:
        res.add("## Document properties\n\n" + md_table([["Property", "Value"]] + [[k, v] for k, v in meta.items()]))
    toc = doc.get_toc()
    if toc:
        res.add("## Outline (bookmarks)\n\n" + "".join(f"{'  ' * (lvl - 1)}- {t} (p. {pg})\n" for lvl, t, pg in toc))

    seen_xref, n_img, n_tables, vision_pages, all_text = set(), 0, 0, 0, []
    visual_pages = 0
    for pno, page in enumerate(doc, start=1):
        res.add(f"## Page {pno}\n")
        text = page.get_text("text")
        all_text.append(text)
        prof = visual_profile(page)
        scanned = len(text.strip()) < 25 and bool(page.get_images() or page.get_drawings())
        visual = prof["visual"] and not scanned
        try:
            # boards and designs produce phantom grids; their text goes into the positioned item table instead
            tables = [] if visual else list(page.find_tables().tables)
        except Exception:  # find_tables can fail on odd pages; text is still kept below
            tables = []
        # Table finder drops ligature glyphs and treats decorative frames as grids: re-read each cell with
        # ligatures expanded, and keep a table only if it preserves the text the plain blocks hold there.
        no_lig = pymupdf.TEXTFLAGS_TEXT & ~pymupdf.TEXT_PRESERVE_LIGATURES
        block_flags = pymupdf.TEXTFLAGS_BLOCKS & ~pymupdf.TEXT_PRESERVE_LIGATURES
        kept = []
        for t in tables:
            grid = [[" ".join(page.get_text("text", clip=pymupdf.Rect(c), flags=no_lig).split()) if c else "" for c in row.cells] for row in t.rows]
            flat = re.sub(r"\W+", "", "".join("".join(r) for r in grid)).casefold()
            box = pymupdf.Rect(t.bbox)
            lines = [l for bl in page.get_text("blocks", flags=block_flags) if bl[6] == 0 and box.intersects(pymupdf.Rect(bl[:4])) for l in bl[4].splitlines()]
            if flat and all(re.sub(r"\W+", "", l).casefold() in flat for l in lines):
                kept.append((t, grid))
        tboxes = [pymupdf.Rect(t.bbox) for t, _ in kept]
        # Light structure only (never changes words): a block whose spans are all bold and clearly larger
        # than body text becomes a heading; an all-bold short block becomes **bold**; a bullet glyph on its
        # own line is joined to its text as a Markdown list item.
        spans = [s for bl in page.get_text("dict", flags=block_flags).get("blocks", []) if bl.get("type") == 0
                 for ln in bl["lines"] for s in ln["spans"] if s["text"].strip()]
        sizes = sorted(s["size"] for s in spans)
        body = sizes[len(sizes) // 2] if sizes else 0

        def styled(r: "pymupdf.Rect", txt: str) -> str:
            txt = re.sub(r"(?m)^[•●▪◦‣■]\s*(?:\n|$)", "- ", txt)
            inside = [s for s in spans if r.contains(pymupdf.Rect(s["bbox"]).tl + (pymupdf.Rect(s["bbox"]).br - pymupdf.Rect(s["bbox"]).tl) * 0.5)]
            if inside and len(txt) < 160 and not txt.startswith("- ") and all(s["flags"] & 16 for s in inside):
                txt = " ".join(txt.split())            # a heading wrapped over two lines is still one heading
                big = max(s["size"] for s in inside)
                if body and big >= body * 1.4:
                    return "### " + txt.strip()          # "## Page N" is the engine's own level
                return ("#### " if body and big >= body * 1.15 else "**") + txt.strip() + ("" if body and big >= body * 1.15 else "**")
            return txt

        items = []
        for b in page.get_text("blocks", flags=block_flags):
            if b[6] != 0 or not b[4].strip():
                continue
            r = pymupdf.Rect(b[:4])
            if any(tb.contains(r) or tb.intersects(r) and (tb & r).get_area() > 0.6 * r.get_area() for tb in tboxes):
                continue
            items.append((b[1], b[0], (b[4].strip() if visual else styled(r, b[4].strip())) + "\n", r))
        for t, grid in kept:
            n_tables += 1
            items.append((t.bbox[1], t.bbox[0], md_table(grid), pymupdf.Rect(t.bbox)))
        if visual:
            # Positioned item table: every text block keeps an ID, the colour of the shape it sits on
            # (sticky / card / lane) and its place on the page, so the vision pass can describe groups and
            # arrows by ID ("p3.4 → p3.9") instead of retyping text. Text stays machine-extracted.
            # PyMuPDF blocks merge stickies that share a row, so work per LINE: lines on the same shape form
            # one item; free lines group only with lines of their block that overlap them horizontally.
            pr = page.rect
            groups: list[dict] = []
            by_shape: dict[int, dict] = {}
            for bno, b in enumerate(page.get_text("dict", flags=block_flags).get("blocks", [])):
                if b.get("type") != 0:
                    continue
                for ln in b["lines"]:
                    t = "".join(s["text"] for s in ln["spans"]).strip()
                    if not t:
                        continue
                    lr = pymupdf.Rect(ln["bbox"])
                    c = pymupdf.Point((lr.x0 + lr.x1) / 2, (lr.y0 + lr.y1) / 2)
                    under = [(s.get_area(), k, f) for k, (s, f) in enumerate(prof["shapes"]) if c in s]
                    if under:
                        _, k, f = min(under, key=lambda u: u[0])
                        g = by_shape.get(k)
                        if g is None:
                            g = by_shape[k] = {"rect": pymupdf.Rect(lr), "lines": [], "fill": f"{colour_name(f)} {hex_of(f)}"}
                            groups.append(g)
                    else:
                        g = next((g for g in groups if g.get("block") == bno and min(g["rect"].x1, lr.x1) > max(g["rect"].x0, lr.x0)), None)
                        if g is None:
                            g = {"rect": pymupdf.Rect(lr), "lines": [], "fill": "", "block": bno}
                            groups.append(g)
                    g["rect"] |= lr
                    g["lines"].append(t)
            rows = [["ID", "Text", "Sits on (fill)", "Position x%, y%"]]
            for i, g in enumerate(sorted(groups, key=lambda g: (round(g["rect"].y0 / 8), g["rect"].x0)), start=1):
                r = g["rect"]
                rows.append([f"p{pno}.{i}", "\n".join(g["lines"]), g["fill"],
                             f"{100 * (r.x0 - pr.x0) / pr.width:.0f}, {100 * (r.y0 - pr.y0) / pr.height:.0f}"])
            res.add(f"_Visual page — {len(rows) - 1} text items, {len(prof['shapes'])} filled shapes, "
                    f"{prof['connectors']} connector-like paths, images cover {prof['image_ratio']:.0%}._\n")
            res.add(md_table(rows))
        else:
            for _, _, chunk, _ in sorted(items, key=lambda x: (round(x[0], 1), x[1])):
                res.add(chunk)

        # A page with (almost) no text layer is a scan, and a visual page is covered by its own render: the
        # page render is the one required vision item; embedded images are still extracted (kept as assets)
        # but not queued a second time.
        for info in page.get_images(full=True):
            xref = info[0]
            if xref in seen_xref:
                continue
            seen_xref.add(xref)
            try:
                img = doc.extract_image(xref)
            except Exception:
                continue
            n_img += 1
            img_dir.mkdir(parents=True, exist_ok=True)
            dest = img_dir / f"page{pno}-img{n_img}.{img['ext']}"
            dest.write_bytes(img["image"])
            if scanned or visual:
                res.add(f"_Embedded image (covered by the page render below): [assets/{stem}/{dest.name}](assets/{stem}/{dest.name})_\n")
            else:
                res.add(res.vision_block(f"{stem}-p{pno}-img{n_img}", f"assets/{stem}/{dest.name}", f"Page {pno} image {n_img}", required=False))

        if scanned or visual:
            vision_pages += 1
            visual_pages += visual
            zoom = max(1.0, min(8.0, MIN_TEXT_PX / small_font_size(page)))
            label = f"Page {pno} has no text layer (scan)" if scanned else f"Page {pno} is visual (board / diagram / design)"
            ov, tiles = render_for_vision(page, img_dir, f"page{pno}", zoom, res.warnings, label)
            hint = ("" if scanned else
                    f"Text is already extracted above as p{pno}.N items — map structure by ID; transcribe only text "
                    f"that is visible here but missing from the table. Expect ~{prof['connectors']} connector-like paths.")
            res.add(visual_block(res, f"{stem}-p{pno}", f"assets/{stem}", ov, tiles, label, hint))

        links = [l.get("uri") for l in page.get_links() if l.get("uri")]
        if links:
            res.add("**Links on this page:** " + ", ".join(f"<{u}>" for u in dict.fromkeys(links)) + "\n")
        annots = [(a.type[1], (a.info.get("title") or ""), a.info.get("content") or "") for a in page.annots() or []]
        annots = [a for a in annots if a[2].strip()]
        if annots:
            res.add("**Annotations:**\n\n" + md_table([["Type", "Author", "Content"]] + [list(a) for a in annots]))

    res.warnings += mojibake_warnings("".join(all_text))
    res.stats = {"pages": len(doc), "pages_needing_vision": vision_pages, "visual_pages": visual_pages, "images_extracted": n_img,
                 "images_in_source": len(seen_xref), "tables": n_tables, "encrypted": doc.needs_pass}
    return res


def pandoc_meta_text(node) -> str:
    """Flatten a pandoc JSON metadata value (MetaInlines/MetaList/MetaMap/...) to plain text."""
    if isinstance(node, list):
        return " ".join(filter(None, (pandoc_meta_text(n) for n in node)))
    if isinstance(node, dict):
        t, c = node.get("t"), node.get("c")
        if t == "Str":
            return c
        if t in ("Space", "SoftBreak", "LineBreak"):
            return " "
        if t == "MetaMap":
            return "; ".join(f"{k}: {pandoc_meta_text(v)}" for k, v in c.items())
        if c is not None:
            return pandoc_meta_text(c)
        return ""
    return str(node) if isinstance(node, (str, int, float, bool)) else ""


def conv_pandoc_generic(src: Path, out: Path, stem: str, fmt_in: str | None = None) -> Result:
    res = Result("pandoc")
    if not PANDOC:
        raise RuntimeError("pandoc not found")
    cmd = [PANDOC, str(src.resolve()), "-t", "gfm", "--wrap=none", f"--extract-media=assets/{stem}"]
    if fmt_in:
        cmd[2:2] = ["-f", fmt_in]
    cp = run(cmd, cwd=out)
    if cp.returncode != 0:
        raise RuntimeError(f"pandoc failed: {cp.stderr.strip()[:400]}")
    # gfm output drops document metadata (title/author/date/...) — pull it from the JSON AST instead
    jp = run([PANDOC, str(src.resolve()), "-t", "json"] + (["-f", fmt_in] if fmt_in else []), cwd=out)
    if jp.returncode == 0:
        meta = {k: pandoc_meta_text(v) for k, v in json.loads(jp.stdout).get("meta", {}).items()}
        meta = {k: v for k, v in meta.items() if v.strip()}
        if meta:
            res.add("## Document properties\n\n" + md_table([["Property", "Value"]] + [[k, v] for k, v in meta.items()]))
    res.add(cp.stdout)
    res.stats = {"images_extracted": len(list((out / "assets" / stem).rglob("*.*"))) if (out / "assets" / stem).exists() else 0}
    return res


def conv_markitdown(src: Path, out: Path, stem: str) -> Result:
    from markitdown import MarkItDown

    res = Result("markitdown")
    r = MarkItDown(enable_plugins=False).convert(str(src))
    res.add(r.text_content)
    res.warnings += mojibake_warnings(r.text_content)
    return res


def conv_email(src: Path, out: Path, stem: str, sub_convert) -> Result:
    res = Result("email")
    msg = email.message_from_bytes(src.read_bytes(), policy=email.policy.default)
    hdr = [[h, str(msg[h])] for h in ("From", "To", "Cc", "Bcc", "Date", "Subject", "Message-ID") if msg[h]]
    res.add("## Headers\n\n" + md_table([["Header", "Value"]] + hdr))
    body = msg.get_body(preferencelist=("plain", "html"))
    if body is not None:
        content = body.get_content()
        if body.get_content_type() == "text/html":
            from markitdown import MarkItDown
            import io
            content = MarkItDown().convert_stream(io.BytesIO(content.encode("utf-8")), file_extension=".html").text_content
        res.add("## Body\n\n" + content)
    att_dir = out / "assets" / stem
    atts = list(msg.iter_attachments())
    for i, part in enumerate(atts, 1):
        name = part.get_filename() or f"attachment-{i}"
        att_dir.mkdir(parents=True, exist_ok=True)
        dest = att_dir / name
        dest.write_bytes(part.get_payload(decode=True) or b"")
        res.add(f"## Attachment {i}: {name}\n\n" + sub_convert(dest))
    res.stats = {"attachments": len(atts)}
    return res


# ------------------------------------------------------------------ orchestration
class Converter:
    def __init__(self, out: Path):
        self.out = out
        self.manifest: list[dict] = []
        self.used_stems: set[str] = set()
        self.tmp = Path(tempfile.mkdtemp(prefix="doc-to-md-"))

    def stem_for(self, src: Path) -> str:
        base = re.sub(r"[^\w.-]+", "-", src.stem, flags=re.UNICODE).strip("-") or "file"
        stem = base if base not in self.used_stems else f"{base}-{src.suffix.lower().lstrip('.')}"
        n = 2
        while stem in self.used_stems:
            stem, n = f"{base}-{n}", n + 1
        self.used_stems.add(stem)
        return stem

    def libreoffice(self, src: Path, stem: str) -> Path:
        """Legacy/ODF -> OOXML. The intermediate is KEPT under assets/_intermediate/ so verify.py can
        check the .md against it (and a human can open it) — not thrown away with the temp dir."""
        if not SOFFICE:
            raise RuntimeError("LibreOffice (soffice) not found — needed for legacy/ODF formats")
        target = LIBREOFFICE_TARGET[src.suffix.lower()]
        work = self.tmp / f"lo-{stem}"
        work.mkdir(parents=True, exist_ok=True)
        cp = run([SOFFICE, "--headless", "--norestore", "--convert-to", target, "--outdir", str(work), str(src.resolve())])
        hits = list(work.glob(f"*.{target}"))
        if cp.returncode != 0 or not hits:
            raise RuntimeError(f"LibreOffice conversion failed: {(cp.stderr or cp.stdout).strip()[:300]}")
        keep = self.out / "assets" / "_intermediate" / f"{stem}.{target}"
        keep.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(hits[0], keep)
        return keep

    def dispatch(self, src: Path, stem: str) -> Result:
        ext = src.suffix.lower()
        route = route_for(src)
        if ext in (".docx", ".docm"):
            return conv_docx(src, self.out, stem)
        if ext in (".xlsx", ".xlsm"):
            return conv_xlsx(src, self.out, stem)
        if ext in (".pptx", ".pptm"):
            return conv_pptx(src, self.out, stem)
        if ext == ".pdf":
            return conv_pdf(src, self.out, stem)
        if ext in LIBREOFFICE_TARGET:
            modern = self.libreoffice(src, stem)
            res = self.dispatch(modern, stem)
            res.engine = f"libreoffice->{res.engine}"
            res.verify_path = str(modern.resolve())
            res.stats["intermediate"] = f"assets/_intermediate/{modern.name}"
            return res
        if ext in (".epub", ".fb2"):
            return conv_pandoc_generic(src, self.out, stem)
        if ext in (".mobi", ".azw", ".azw3"):
            if not EBOOK_CONVERT:
                raise RuntimeError("Calibre ebook-convert not found")
            epub = self.tmp / f"{stem}.epub"
            cp = run([EBOOK_CONVERT, str(src.resolve()), str(epub)], timeout=600)
            if cp.returncode != 0 or not epub.exists():
                raise RuntimeError(f"ebook-convert failed: {cp.stderr.strip()[:300]}")
            res = conv_pandoc_generic(epub, self.out, stem)
            res.engine = "calibre->pandoc"
            return res
        if ext == ".eml":
            return conv_email(src, self.out, stem, self.inline_attachment)
        if route == "verbatim":
            res = Result("verbatim")
            text = src.read_text(encoding="utf-8", errors="replace")
            if text.startswith("---"):
                end = text.find("\n---", 3)
                if end > 0:
                    res.add("```yaml original-frontmatter\n" + text[3:end].strip("\n") + "\n```\n")
                    text = text[end + 4:]
            res.add(text)
            res.warnings += mojibake_warnings(text)
            return res
        if route == "verbatim-code":
            res = Result("verbatim-code")
            lang = ext.lstrip(".").replace("yml", "yaml")
            res.add(f"```{lang}\n" + src.read_text(encoding="utf-8", errors="replace").rstrip("\n") + "\n```\n")
            return res
        if ext in IMAGE_EXT:
            res = Result("image->vision")
            d = self.out / "assets" / stem
            d.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, d / src.name)
            # Board / screen exports are often far larger than vision reads at once: tile them at native size.
            import pymupdf
            try:
                with pymupdf.open(str(src)) as idoc:
                    ipage = idoc[0]
                    native = pymupdf.Pixmap(str(src)).width / max(ipage.rect.width, 1)
                    ov, tiles = render_for_vision(ipage, d, "image", native, res.warnings, f"Image {src.name}")
            except Exception as e:  # unreadable by pymupdf (e.g. animated gif): fall back to the original
                res.warnings.append(f"could not tile image ({type(e).__name__}); vision reads the original")
                ov, tiles = src.name, []
            res.add(f"Original: [assets/{stem}/{src.name}](assets/{stem}/{src.name})\n")
            res.add(visual_block(res, stem, f"assets/{stem}", ov, tiles, f"Image {src.name}",
                                 "Image only — transcribe all visible text verbatim and map its structure."))
            res.stats = {"images_extracted": 1}
            return res
        return conv_markitdown(src, self.out, stem)

    def inline_attachment(self, path: Path) -> str:
        """Convert an e-mail attachment as its own file, then reference it."""
        stem = self.convert_file(path, parent="attachment")
        return f"Converted separately → [{stem}.md]({stem}.md)\n" if stem else "_(attachment could not be converted — see report)_\n"

    def convert_file(self, src: Path, parent: str | None = None) -> str | None:
        stem = self.stem_for(src)
        entry = {"source_name": src.name, "source_path": str(src.resolve()), "stem": stem, "route": route_for(src), "parent": parent}
        try:
            data = src.read_bytes()
            entry.update(sha256=hashlib.sha256(data).hexdigest(), size_bytes=len(data))
            res = self.dispatch(src, stem)
            fm = {
                "type": "source-conversion", "source": src.name, "source_type": src.suffix.lower().lstrip("."),
                "sha256": entry["sha256"], "size_bytes": entry["size_bytes"], "engine": res.engine,
                "engine_version": ENGINE_VERSION, "converted": date.today().isoformat(),
                "status": "needs-vision" if any(v["required"] for v in res.vision) else "converted",
            }
            head = "---\n" + "".join(f"{k}: {json.dumps(v, ensure_ascii=False) if isinstance(v, str) else v}\n" for k, v in fm.items()) + "---\n\n"
            title = f"# {src.name}\n\n"
            (self.out / f"{stem}.md").write_text(head + title + "\n".join(res.parts), encoding="utf-8")
            entry.update(status=fm["status"], engine=res.engine, stats=res.stats, vision=res.vision, warnings=res.warnings)
            if getattr(res, "verify_path", None):
                entry["verify_path"] = res.verify_path
        except Exception as e:  # never drop a file silently: record the failure
            entry.update(status="failed", error=f"{type(e).__name__}: {e}")
            stem = None
        self.manifest.append(entry)
        return stem

    def expand(self, inputs: list[str], keep_archives: bool = True) -> list[Path]:
        """Folders -> files; .zip -> extracted and recursed. Extracted contents are KEPT under
        assets/_archives/ (originals stay verifiable and nothing exists only in a temp dir)."""
        files = []
        for raw in inputs:
            p = Path(raw)
            if p.is_dir():
                files += sorted(f for f in p.rglob("*") if f.is_file() and not f.name.startswith(("~$", ".")))
            elif p.is_file():
                files.append(p)
            else:
                self.manifest.append({"source_name": p.name, "status": "failed", "error": "not found"})
        expanded = []
        for f in files:
            if f.suffix.lower() == ".zip":
                base = (self.out / "assets" / "_archives") if keep_archives else (self.tmp / "zip")
                dest = base / re.sub(r"[^\w.-]+", "-", f.stem)
                with zipfile.ZipFile(f) as z:
                    z.extractall(dest)
                expanded += self.expand([str(dest)], keep_archives)
            else:
                expanded.append(f)
        return expanded


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("inputs", nargs="+")
    ap.add_argument("--out", required=True)
    ap.add_argument("--plan", action="store_true", help="dry run: list file -> engine, write nothing")
    a = ap.parse_args()
    out = Path(a.out)

    conv = Converter(out)
    files = conv.expand(a.inputs, keep_archives=not a.plan)
    if a.plan:
        print(f"Tools: pandoc={'OK' if PANDOC else 'MISSING'} libreoffice={'OK' if SOFFICE else 'MISSING'} calibre={'OK' if EBOOK_CONVERT else 'MISSING'}")
        print(f"{len(files)} file(s) -> {out}")
        for f in files:
            print(f"  {f.name}\t{route_for(f)}\t{f.stat().st_size} bytes")
        for m in conv.manifest:
            print(f"  {m['source_name']}\tNOT FOUND")
        shutil.rmtree(conv.tmp, ignore_errors=True)
        return 0

    out.mkdir(parents=True, exist_ok=True)
    mf = out / "_manifest.json"
    # Re-running into an existing folder (e.g. a resume library) must not forget earlier files:
    # keep previous entries, but don't reuse their stems, and replace any entry for the same source name.
    previous = json.loads(mf.read_text(encoding="utf-8")).get("files", []) if mf.exists() else []
    conv.used_stems |= {p["stem"] for p in previous if p.get("stem")}
    names_now = {f.name for f in files}
    for p in previous:
        if p.get("source_name") in names_now and p.get("stem"):
            conv.used_stems.discard(p["stem"])  # same file re-converted: reuse its stem, overwrite its .md
    for f in files:
        conv.convert_file(f)
    kept = [p for p in previous if p.get("source_name") not in names_now]
    mf.write_text(json.dumps({"engine_version": ENGINE_VERSION, "converted": date.today().isoformat(),
                              "files": kept + conv.manifest}, ensure_ascii=False, indent=2), encoding="utf-8")
    shutil.rmtree(conv.tmp, ignore_errors=True)
    ok = [m for m in conv.manifest if m["status"] != "failed"]
    print(f"converted {len(ok)}/{len(conv.manifest)} file(s) -> {out}")
    for m in conv.manifest:
        vis = sum(1 for v in m.get("vision", []) if v["required"])
        print(f"  [{m['status']}] {m['source_name']} -> {m.get('stem')}.md  engine={m.get('engine', '-')}"
              + (f"  vision-required={vis}" if vis else "") + (f"  ERROR {m['error']}" if m.get("error") else ""))
        for w in m.get("warnings", []):
            print(f"      ! {w}")
    if not ok:
        print("GATE-A: zero sources converted — abort", file=sys.stderr)
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
