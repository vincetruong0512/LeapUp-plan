---
type: wireframe-html-index
feature: project-files
status: draft
updated: 2026-11-22
links:
  - docs/project-files/srs/project-files-userflow.md
  - docs/project-files/srs/project-files-spec.md
---

# project-files — HTML Wireframes

Open [project-files-wireframe.html](project-files-wireframe.html) (entry page with contents). Device: desktop (board screens are desktop layouts; phone layout TBD).

| # | Flow | File | Screens (in order) | Status | Updated |
|---|------|------|--------------------|--------|---------|
| 1 | Share, find and download files | [files.html](files.html) | project-files → no-result → empty-folder → upload → upload-rejected → upload-failed | draft (revised after review 2026-11-22) | 2026-11-22 |

Screen description tables (5 columns) live inside each flow HTML file.

## Deviations from the Miro board

- None on screen 1: follows board 03 (L9–L179).
- Download control is required by the quote but not drawn: a "[Download — placement TBD]" marker sits next to the table.
- Screens 2–6 (no result, empty folder, upload, upload rejected, upload failed) are not on the board; they are state
  markers only. The upload screens drop the folder cards and table for brevity — the upload opens over screen 1
  (overlay or page TBD).
- Not on the board: upload progress, success feedback, download failure (spec OQ-15).
- Phone layout not provided by the board (quote §7 requires phone use; spec OQ-9, review D-06).
