# Source playbook — which export catches the most

Rule of thumb: **structured data > vector PDF > high-res image > screenshot.** Each step down loses
something the engine can no longer extract by machine, so the vision pass has to recover it, and vision
output is not machine-verified.

| Source | Best (most complete) | Good | Avoid |
|---|---|---|---|
| **Miro board** | Board → *Export* → **PDF, vector** (keeps sticky text as a text layer, plus shapes and colours, so you get a machine-extracted item table and a vision pass only for structure). For full structure, export via the **Miro REST API v2** (`/v2/boards/{id}/items` + `/connectors`): exact item text, colours, frames, connector start→end IDs. Save the JSON and convert it as verbatim | Export a **frame-by-frame PDF** (one frame per page) when the board is huge, so each page stays readable | Screenshots / "Save as image" of a whole board, where small text is lost before any tool sees it |
| **FigJam** | Export **PDF** (per section) | PNG at 2× | Screenshots |
| **Figma designs** | Read the file through the Figma MCP (`reqwise-figma` is installed): exact text, components, auto-layout, tokens. Use doc-to-md only for exported specs/PDF handoffs | Export frames as **PDF** (vector text) | PNG of a full page (text becomes pixels) |
| **Google Docs / Sheets / Slides** | Download as **.docx / .xlsx / .pptx** (keeps comments, suggestions, notes, hidden sheets) | PDF | Copy-paste |
| **Word / PowerPoint with diagrams** | Original **.docx / .pptx** (SmartArt, charts, notes are extracted as data) | PDF | Scans |
| **Confluence / Notion** | Export **Word (.docx)** or HTML | PDF | Screenshots |
| **Whiteboard photos / scans** | Photo straight-on, ≥ 12 MP, no glare. Images are tiled at native resolution | PDF scan at 300 dpi | Low-res chat-app forwards (compressed) |
| **Mixed PDF (text + screenshots)** | As is. Text pages are machine-extracted, pages dominated by images become visual pages, embedded screenshots are kept as assets | — | Printing to PDF from a browser (often rasterises) |

## Lesson from the Leap Up board (2026-11-21)

Miro's PDF export can be a **single raster image** (producer `jsPDF`, ~1000 px for the whole board). The
engine flags it as "no text layer". Wireframe text at that size is illegible even at 4× zoom. **Always also
export the board's text as CSV** (Miro: select all → *Export* → CSV), and convert both. Then map each CSV
line to its screen by line number (`Lnnn`) in the vision pass. Text stays machine-sourced, the image supplies
only placement and visual cues, and a script asserts every CSV line is used exactly once. Worked example:
`docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md`.

## Why a vector PDF beats an image for boards

A Miro PDF export keeps three things the engine reads directly:

1. **Text layer:** every sticky/shape label extracted exactly, verified by an independent extractor.
2. **Filled shapes:** each text item gets the colour of the sticky/card it sits on (`light yellow #fff9b1`).
3. **Geometry:** position of every item, so vision only has to say *how items relate* (groups,
   arrows) by ID, and never retypes text.

An image export keeps none of this: all text must be read from pixels, and small text on a large board
is often unreadable even with tiling.

## Checklist to send whoever shares the files

- Miro/FigJam: "Export → PDF (vector), and if the board is large, one frame per page."
- Figma: "Share the Figma link" (read via MCP), or "Export frames as PDF".
- Google/Office: "Send the original file format, not a PDF or screenshot."
- Any board where colour carries meaning: "Keep the legend on the board."
