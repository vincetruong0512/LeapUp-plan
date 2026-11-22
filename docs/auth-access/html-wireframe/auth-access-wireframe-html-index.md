---
type: wireframe-html-index
feature: auth-access
status: draft
updated: 2026-11-22
links:
  - docs/auth-access/srs/auth-access-userflow.md
  - docs/auth-access/srs/auth-access-spec.md
---

# auth-access — HTML Wireframes

Open [auth-access-wireframe.html](auth-access-wireframe.html) (entry page with contents). Device: desktop (board screens are desktop layouts; phone layout TBD).

| # | Flow | File | Screens (in order) | Status | Updated |
|---|------|------|--------------------|--------|---------|
| 1 | Sign in and sign out | [sign-in.html](sign-in.html) | login → login-error → landing-empty → landing → not-assigned | draft (revised after review 2026-11-22) | 2026-11-22 |

Screen description tables (5 columns) live inside each flow HTML file.

## Deviations from the Miro board

- None on the Login screen: layout, wording and controls follow board 01 (L18–L170).
- Screens 2–5 are states the board does not draw; they only mark where a TBD message/page is needed and do not define a layout.
- Not on the board: Sign out, the landing page, the not-assigned refusal (screen 5), loading states.
- Phone layout not provided by the board (quote §7 requires phone use; spec OQ-5, review D-06).
