---
type: backlog
feature: portal
status: open
updated: 2026-11-22
---

# Plan review backlog (2026-11-22)

Gaps found when the whole plan was reviewed against the pipeline rule (`.claude/rules/requirements-pipeline.md`),
the quote (`bao-gia-leapup-mvp.md`) and the Miro board. To revise later. MVP items first.

## What was checked and passed

| Check | Result |
|---|---|
| Every FR has a source (quote / board line / user decision) | 110 / 110 FR (84 quoted + 26 OUT) |
| Every FR is covered by ≥ 1 user story | 10 / 10 features, no gaps, no unknown FR IDs |
| Every story has Given/When/Then AC | 37 / 37 stories |
| Every FR is covered by a use case | 109 / 110 — see B-09 |
| Quote line items mapped to a feature or work package | P1 #1–#4, P2 #1–#5 all present in `delivery-plan.md` §1, §3 |
| Delivery-plan totals match the files | 84 FR · 30 stories · 19 use cases (quoted scope) |
| OUT features kept out of the prototype and sprint plan | Yes (prototype legend; delivery plan §1) |

## Backlog

| # | Tag | Gap | Rule / source | Suggested fix |
|---|---|---|---|---|
| B-01 | MVP | **No review gate passed.** Every step of every feature is `draft`; no story is `approved` (0 / 37). Pipeline rule 1 says a step starts only after the previous one is approved. | requirements-pipeline.md rule 1, rule 6 | Walk Leap Up through MVP features in order (auth-access → admin → project-files → video-review); record approval date per step in each `README.md` |
| B-02 | MVP | **Reviewer agents run 2026-11-22 on the 4 MVP features** (84 findings → 13 Leap Up decisions D-01…D-13, 17 doc fixes R-01…R-17): [review-2026-11-22-mvp.md](review-2026-11-22-mvp.md). Still to do: apply R-fixes; take D-items to Leap Up; `tech-reviewer` not run; P2 features not reviewed. | requirements-pipeline.md (skill availability) | Apply R-01…R-17, then re-run reviewers; P2 features after MVP |
| B-03 | MVP | **No BRD.** `/brd portal` is recommended once before `/srs`; it is the stakeholder-facing summary (objectives, success measures, scope, risks). | CLAUDE.md (Project skills) | Run `/brd portal` before the stakeholder presentation |
| B-04 | MVP | **Admin wireframe blocked** (C3: no board screen). PR3 (admin wizard) exists only as a Figma proposal. | _comparison.md C3; screen-design.md PR3 | Get Leap Up to provide or approve an admin design; then run `/wireframe-html admin` |
| B-05 | MVP | **Sprint 1 blockers still open:** landing page, upload rules, file status rules, C7 Project Info tab, login security, all error wording. | delivery-plan.md §6 | Settle in Sprint 0 with Leap Up |
| B-06 | MVP | **Error wording TBD** for 32 of 33 error codes across specs. | each spec's Error Matrix | Agree wording with Leap Up (one language, quote §7) |
| B-07 | MVP | **Proposals PR1–PR5 undecided.** They answer open questions (auth-access OQ-1, project-files OQ-3/OQ-8, video-review OQ-6, admin C3) but specs still show those as TBD. | screen-design.md L71–L79 | Present PR1–PR5 as options; if accepted, update spec → flow → wireframe → stories (mark downstream stale) |
| B-08 | MVP | **User guide (hướng dẫn sử dụng) not planned as a document.** It is a Phase 1 deliverable; `/userguide` is not installed. | quote P1 #4, §6 | Port `/userguide` (Tier 2) or plan it in the deployment & handover package |
| B-09 | MVP | **Fixed 2026-11-22** (extension 5a in uc-find-and-download-a-file, provisional). Was: `FR-project-files-014` (open video in Video Review) has no use case. Its trigger is inferred (OQ-8). | project-files-spec.md | Add to `uc-find-and-download-a-file` or a new UC after OQ-8 / PR2 is decided |
| B-10 | MVP | **No test checklist** for "Done = all AC pass" (delivery-plan §4). `/test-checklist` + `/test-cases` not installed. | delivery-plan.md §4; quote P2 #5 | Port on request; Phase 2 testing package needs it most |
| B-11 | MVP | **Jira not pushed**: import files only (no Atlassian connection, no approved stories). | requirements-pipeline.md rule 6 | After B-01, push with explicit yes per push |
| B-12 | OPEN | C2, C4, C5, C6, C9 unresolved (realtime tasks, approver roles, revision quota/CR cost, client inputs, sign-off checklist). C4 provisionally resolved for MVP roles only. | _comparison.md §2 | Ask Leap Up before Sprint 3 / 4 (delivery-plan §6) |
| B-13 | OUT | C1: Leap Up has not yet confirmed Material Library and Storyboard Review are outside this contract. | _comparison.md C1; quote §7 | Confirm in the stakeholder session |
| B-14 | P2 | Deployment & handover and testing & acceptance are work packages with no requirements doc (backup, auto-deploy, SSL are only listed). | quote P1 #4, P2 #5 | Enough for now; detail in `technical-solution-design.md` when Phase 1 build starts |
| B-15 | MVP | **Stale after the 2026-11-22 review fixes:** use cases, sequence/activity diagrams and Jira import files of the 4 MVP features; Figma screens (screen-design.md), Figma user-flow page and the portal prototype. | requirements-pipeline.md rule 1 | Re-run `/usecase`, `/sequence`, `/activity`, `/jira` after re-approval; redraw Figma; re-run `/prototype-html portal` |
| B-16 | MVP | `tech-reviewer` not run; P2 features not reviewed; MVP-only portal journey not drawn (R-15). | review-2026-11-22-mvp.md §3 | Run `tech-reviewer` on the 4 MVP specs; P2 reviews after MVP sign-off |
| B-17 | MVP | **Re-approval needed:** specs, flows, wireframes and stories of the 4 MVP features were revised; take decisions D-01…D-13 to Leap Up. | review-2026-11-22-mvp.md §1 | Walk Leap Up through D-items (Sprint 1 ones first), then approve each step |
