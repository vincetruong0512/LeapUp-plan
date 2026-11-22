---
type: review
feature: portal
status: doc fixes applied 2026-11-22; decisions open
updated: 2026-11-22
---

# MVP review — 2026-11-22

First run of the reviewer agents on the four MVP features (auth-access, admin, project-files, video-review).
Raw findings: `senior-ba` 25 (SBA), `qa-reviewer` 25 (QA), `flow-reviewer` 17 (FLOW), `uxui-reviewer` 17 (UX) = 84.
Merged below by root cause: **D-** items need a Leap Up decision; **R-** items are doc fixes that need no decision
(strict-reference rule: unknowns become TBD/OQ, never filled in). Status: `open` / `fixed {date}`.

Verdicts: senior-ba **REVISE** · wireframes match the Miro board on all three drawn screens · no feature flow treats
PR1–PR5 as decided · FR/error totals in `delivery-plan.md` §1 match the specs.

## 1. Decisions for Leap Up (D)

| # | Decision needed | Features | From | Blocks |
|---|---|---|---|---|
| D-01 | Password reset: already decided that the Leap Up admin resets it (auth-access brainstorm OQ-8, user decision 2026-11-21 — so SBA-1 is not a source gap). Still open: how (screen, steps); admin now cites the decision (admin OQ-5) | auth-access, admin | SBA-1, FLOW-10 | Sprint 1 |
| D-02 | How are Leap Up member accounts and the first Admin account created? Who administers? (admin OQ-2) | admin | SBA-2, SBA-5, FLOW-10 | Sprint 1 |
| D-03 | Account type vs project role: can one person be Leap Up on one project and Client on another? Does Admin see all projects? What label do Admin uploads/comments show? | auth-access, admin, project-files, video-review | SBA-3, SBA-4, SBA-18 | Sprint 1 |
| D-04 | Are file statuses Approved / Final manual labels in Phase 1, or reserved for Outcome Approval (P2)? Who sets status? | project-files | SBA-11, QA-25 | Sprint 1 (scope creep risk) |
| D-05 | File ↔ review link: is a Video Review version the same record as the Outcome Development file? Status sync? Comments when a file is replaced? Can Material videos be reviewed? Which round opens? | project-files, video-review | SBA-12, FLOW-14, FLOW-16, QA-25 | Sprint 1 (moved from Sprint 2, SBA-20) |
| D-06 | Phone browser: separate phone frames from Leap Up, or a stacking rule? Which test devices/browsers? | all MVP | UX-4, QA-3, FLOW-17 | Sprint 1 acceptance |
| D-07 | Sign-in error: where shown, User ID kept after failure, and must the message hide whether the User ID exists? | auth-access | UX-12, FLOW-12, QA-18 | Sprint 1 |
| D-08 | Who may resolve / re-open comments; may users comment on a past round or a round with no video? | video-review | QA-7, FLOW-6, FLOW-7, SBA-13 | Sprint 2 |
| D-09 | Timecode capture: moment the comment is started or submitted; rounding of fractional seconds | video-review | SBA-23, QA-6 | Sprint 2 |
| D-10 | Who records the round change log, and which status lines it may show in Phase 1 | video-review | QA-4, SBA-10 | Sprint 2 |
| D-11 | Client upload rights per folder; upload type/size limits; multi-file partial failure | project-files | FLOW-8, QA-8, QA-9 | Sprint 1 |
| D-12 | Admin set-up order and admin page entry (C3, PR3) | admin | FLOW-11 | Sprint 1 |
| D-13 | Required project fields; duplicate-assignment and unknown-user errors; remove member / deactivate account | admin | QA-12, QA-15, SBA-7 | Sprint 1 |

## 2. Doc fixes (R)

| # | Fix | Files | From | Status |
|---|---|---|---|---|
| R-01 | Add the "not assigned to this project" branch (E-auth-access-003) to every feature flow and the portal journeys; add a TBD wireframe state | auth-access, project-files, video-review, admin flows; sign-in.html; portal-userflow.md | UX-1, FLOW-2 | fixed 2026-11-22 |
| R-02 | Split the access-refusal AC per surface (page, download, video, comment create/resolve, change log) + signed-out + two-client leak check | auth-access us-002; project-files us-001/us-004; video-review us-001 | QA-1, QA-13 | fixed 2026-11-22 |
| R-03 | Connect the feature flows: landing → project → files → video review; landing → admin (entry TBD) | auth-access, project-files, admin, video-review flows | FLOW-1, FLOW-5 | fixed 2026-11-22 |
| R-04 | Fix upload error labels: size/type = E-project-files-001, upload failed = 003 with its own branch and retry | project-files flow; portal-userflow.md; us-002 | FLOW-3, QA-10, UX-6 | fixed 2026-11-22 |
| R-05 | Admin flow: Cancel on every form, errors return to the failing form, assign-members reachable directly, off-system credential hand-over node | admin-userflow.md | FLOW-4, FLOW-10, FLOW-11 | fixed 2026-11-22 |
| R-06 | Video review flow: exit via breadcrumb/sidebar, selected round without video goes to the no-video state, FR-010/011/012 marked "no flow, TBD", no-comments empty state | video-review-userflow.md | FLOW-5, FLOW-6 | fixed 2026-11-22 |
| R-07 | Video review wireframe: add empty-comment and no-comments states; no-video screen shows the Upcoming round with no player/comments | review.html | UX-2, UX-3 | fixed 2026-11-22 |
| R-08 | Downgrade guesses to TBD: FR-admin-004 status, FR-admin-001 member rights, BR-auth "Admin resets", "Admin sees all projects", BR-vr-003, inferred FR-pf-012/014 and FR-vr-013 marked provisional | admin, auth-access, project-files, video-review specs + affected AC | SBA-1, SBA-4–SBA-9 | fixed 2026-11-22 |
| R-09 | Restore dropped open questions (search fields; comments on older rounds/replaced versions; user removed while signed in; Show-toggle label; simultaneous edits without realtime; P2 tabs in Phase 1; Outcome vs Outcome Development label) | specs §12 | SBA-13–SBA-17, SBA-22 | fixed 2026-11-22 |
| R-10 | Fix story trace errors and placeholders (`FR-admin-BR-admin-002`, wrong BR cite, missing linked FRs, `{n}` / `{status}` placeholders, round 3 "Pending") | stories | SBA-24, QA-5, QA-16, QA-24 | fixed 2026-11-22 |
| R-11 | Add missing scenarios as AC (marked "blocked by OQ-n" where needed): client/video upload, empty folder, Leap Up member sign-in, multi-project user, wrong-case password, empty-field outline, duplicate assignment, playback retry, download failure | stories | QA-2, QA-8, QA-11, QA-14, QA-15, QA-18–QA-23 | fixed 2026-11-22 |
| R-12 | Mark untestable AC "blocked by OQ-n" (landing page, required fields, upload limits, resolve rights, wording) | stories | QA-12, QA-17, QA-25 | fixed 2026-11-22 |
| R-13 | Project files flow/wireframe: empty-folder → Upload edge, separate empty-search vs empty-folder states, Download placement marker, download return edge in portal, display-only FR note | project-files flow, files.html, portal-userflow.md | FLOW-8, FLOW-9, UX-5, UX-9 | fixed 2026-11-22 |
| R-14 | Wireframe tables: loading/success TBD rows, normalised control types, list deviations (sign out, landing, change log as table, submit control, phone layout not on board), a11y notes | 3 wireframes + index md | UX-7, UX-8, UX-10, UX-13–UX-16 | fixed 2026-11-22 |
| R-15 | Portal journeys: drop the "adds nothing new" claim or list added edges; separate MVP from P2 overlay; add upload → review hand-off (TBD) | portal-userflow.md | FLOW-14, FLOW-15 | partly fixed 2026-11-22 — claim reworded, hand-off listed as a gap; MVP-only diagram not drawn; Figma frames stale |
| R-16 | Delivery plan §6: add admin OQ-2/3/5/6, project-files OQ-2, auth OQ-8 to Sprint 1; move round/version and file↔review link to Sprint 1 | delivery-plan.md | SBA-19, SBA-20 | fixed 2026-11-22 |
| R-17 | Housekeeping: brainstorm deactivated state → TBD; brainstorm ↔ spec OQ/error crosswalk; portal brainstorm ticks OQ-3/OQ-5 and aligns role names; cite OQ-9 (User ID per project vs per person) in auth flow | brainstorms, auth flow | SBA-7, SBA-21, SBA-25, FLOW-13 | fixed 2026-11-22 |

## 3. After the fixes (2026-11-22)

- All flows re-verified with `.claude/scripts/mermaid-verify.mjs`: auth-access, admin, project-files, video-review and the
  three portal journeys pass (remaining warnings are hand-offs into other features). The committed portal journeys
  failed the strict-renderer check before this pass (0/3); they now pass 3/3.
- Quoted scope now has 97 acceptance criteria (was 65); 22 are marked "blocked by OQ-n" instead of asserting a guess.
- New open questions added to the specs: auth-access OQ-10…OQ-14, admin OQ-10…OQ-12, project-files OQ-13…OQ-18,
  video-review OQ-10…OQ-15. Two error gaps recorded without codes: admin assignment errors, project-files download failure.
- Marked stale, to re-run after re-approval: use cases, sequence/activity diagrams and Jira import files of the four
  MVP features; Figma screens, Figma user-flow page and the portal prototype.
- Not done: `tech-reviewer`; reviews of P2 features; an MVP-only portal journey diagram (R-15).
