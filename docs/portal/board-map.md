---
type: board-map
feature: portal
status: draft
updated: 2026-11-22
links:
  - docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md
  - docs/_sources/2026-11-21-leapup-references/bao-gia-leapup-mvp.md
---

# Miro Board → Feature Map

Where every part of the agreed Miro board ("LEAP UP / CLIENT PROJECT PORTAL", Frame 1, L1) is documented. `Lnnn` = line of the board text export.

## 1. Board columns and section bars

| Board column (header bar) | Section bar | Screen | Feature (docs) | Scope | Quote |
|---|---|---|---|---|---|
| LOGIN (L2) | — | 01 Login | [auth-access](../auth-access/README.md) | MVP | P1 #1 |
| HOME PAGE (L3) | — | 02 Home: Dashboard, Project Management, Update Task List, Action Required | [dashboard-tasks](../dashboard-tasks/README.md) | P2 | P2 #1 |
| PROJECT DEMO (L4) | PROJECT STATUS (L6) | 03 Project detail — Project Files tab | [project-files](../project-files/README.md) | MVP | P1 #2 |
| PROJECT DEMO (L4) | PROPOSAL \| PROJECT TIMELINE (L190) | 04 Proposal / Production Timeline | [production-timeline](../production-timeline/README.md) | P2 | P2 #2 |
| PROJECT DEMO (L4) | MARTERIAL ALIGNMENT (L366, board typo) | 05 Material Library | [material-library](../material-library/README.md) | **OUT** | excluded §7 |
| PROJECT DEMO (L4) | MATERIAL \| DETAIL SCRIPT & STORY BOARD (L425) | 06 Material / Storyboard Review | [storyboard-review](../storyboard-review/README.md) | **OUT** | excluded §7 |
| OUTCOME REVIEW (L5) | OUTCOME REVIEW (L7) | 07 Outcome Development / Video Review | [video-review](../video-review/README.md) | MVP | P1 #3 |
| OUTCOME REVIEW (L5) | OUTCOME APPROVAL (L198) | 08 Outcome Development / Revision & Sign-off | [outcome-approval](../outcome-approval/README.md) | P2 | P2 #3 |
| — (no screen) | — | Admin pages | [admin](../admin/README.md) | MVP | P1 #1 (C3) |
| — (no screen) | — | E-mail notifications | [email-notifications](../email-notifications/README.md) | P2 | P2 #4 |

Header line "Full-page editable wireframe | Sample project data" (L11) and "Items awaiting client review. Dates and tasks below are sample data." (L196): all board values are sample data.

## 2. Screen parts → documents

| Screen | Board parts (lines) | Spec FRs | Wireframe |
|---|---|---|---|
| 01 Login | brand panel L48–L146 · form L18–L120 · access note L150–L170 | FR-auth-access-001…011 | [sign-in](../auth-access/html-wireframe/sign-in.html) |
| 02 Home | header + tabs L8–L15 · stat cards L20–L37 · project cards L49–L74 · task tables L82–L186 · annotation L199 · Action Required L194–L231 | FR-dashboard-tasks-001…011 | [overview](../dashboard-tasks/html-wireframe/overview.html), [tasks](../dashboard-tasks/html-wireframe/tasks.html) |
| 03 Project Status | sidebar L21–L46 · header L9–L24 · tabs L32–L34 · folder cards L52–L72 · toolbar L81–L84 · file table L98–L179 | FR-project-files-001…014 | [files](../project-files/html-wireframe/files.html) |
| 04 Proposal / Timeline | sidebar L209–L239 · header L197–L207 · stages L216–L244 · milestones L256–L350 · client inputs L255–L299 · feedback rule L318–L346 | FR-production-timeline-001…009 | [timeline](../production-timeline/html-wireframe/timeline.html) |
| 05 Material Library | header L367–L370 · categories L371–L401 · option review L372–L373 · option cards L376–L422 · review guide L408–L416 · approval workflow L423–L424 | FR-material-library-001…014 | [options](../material-library/html-wireframe/options.html) |
| 06 Storyboard Review | sidebar L430–L442 · header L426–L429 · tabs L431 · counts L434–L441 · frames L443–L478 · lock notice L479 | FR-storyboard-review-001…012 | [storyboard](../storyboard-review/html-wireframe/storyboard.html) |
| 07 Video Review | sidebar L23–L51 · header L10–L26 · version history L38–L45 · player L56–L145 · comments L55–L147 · round change log L169–L193 | FR-video-review-001…015 | [review](../video-review/html-wireframe/review.html) |
| 08 Revision & Sign-off | sidebar L232–L257 · header L214–L230 · revision rounds L245–L274 · approvers L246–L271 · change requests L287–L333 · final sign-off L345–L365 · approval log L344–L364 | FR-outcome-approval-001…011 | [approval](../outcome-approval/html-wireframe/approval.html) |

## 3. Coverage check (2026-11-22)

Each of the 479 board lines was checked against the published documents (cited by line, or its exact text present). Result: **479 / 479 covered.** Re-run the audit after any board change.
