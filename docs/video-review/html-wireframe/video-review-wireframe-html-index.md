---
type: wireframe-html-index
feature: video-review
status: draft
updated: 2026-11-22
links:
  - docs/video-review/srs/video-review-userflow.md
  - docs/video-review/srs/video-review-spec.md
---

# video-review — HTML Wireframes

Open [video-review-wireframe.html](video-review-wireframe.html) (entry page with contents). Device: desktop (board screens are desktop layouts; phone layout TBD).

| # | Flow | File | Screens (in order) | Status | Updated |
|---|------|------|--------------------|--------|---------|
| 1 | Review a round with timecoded comments | [review.html](review.html) | video-review → video-review-no-video → video-review-error → video-review-no-comments → video-review-empty-comment | draft (revised after review 2026-11-22) | 2026-11-22 |

Screen description tables (5 columns) live inside each flow HTML file.

## Deviations from the Miro board

- Screen 1 follows board 07 (L10–L193), with one deviation: the board lists the round change log as lines
  (L169–L193); it is drawn as a table of the same text for readability.
- No control for adding a new version/round is drawn on the board — listed as TBD only (spec OQ-3).
- The comment submit control (Enter or button) is not on the board (L147) — TBD (spec OQ-15).
- Screens 2–5 (no video, playback error, no comments, empty comment) are not on the board; they are state markers.
  Screen 2 shows the Upcoming round with no player; whether comments are allowed there is TBD (spec OQ-11).
- Timeline markers are yellow on the board; colour is not shown in the B&W wireframe.
- Phone layout not provided by the board (quote §7 requires phone use; spec OQ-8, review D-06).
