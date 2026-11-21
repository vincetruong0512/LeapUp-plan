---
type: brainstorm
feature: portal
scope: MVP
status: draft
updated: 2026-11-21
links:
  - docs/_sources/2026-11-21-leapup-references/bao-gia-leapup-mvp.md
  - docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md
  - docs/_sources/2026-11-21-leapup-references/_project-fit.md
  - docs/_sources/2026-11-21-leapup-references/_comparison.md
---

# Leap Up Client Project Portal — Project Overview

## 0. Scope

**Tag:** MVP — the overview frames Phase 1 and shows Phase 2 and excluded items for context (quote p.1–2, §7).

**Open decisions touching the whole portal:** C3 admin design, C4 roles, C7 Project Info tab block the MVP; C1, C2, C5, C6, C9 affect Phase 2. All are listed in §11 Open Points — none decided yet.

## 1. Idea Seed

> "Xây dựng web app giúp Leap Up và khách hàng cùng theo dõi một dự án sản xuất video ở một nơi: gửi file, review video theo từng giây, theo dõi công việc, ghi nhận yêu cầu chỉnh sửa và ký duyệt bản cuối." (quote §1)

In short: one place where Leap Up and its clients run a video production project together — share files, review video to the second, track tasks, record change requests and sign off the final cut.

## 2. Context

- **Who:** Leap Up, a video production agency, and its clients (brand-side stakeholders). About 50 users in total (quote §1).
- **What exists today:** the project is in the planning phase — no system, no prior work or material. Leap Up's current way of exchanging drafts and feedback has not been documented yet (OQ-1).
- **Agreed design:** a Miro wireframe board with 8 screens (quote §1: "giao diện dựa trên wireframe đã thống nhất trên Miro"). Only 3 of them are MVP (Login, Project Files, Video Review); 2 are excluded (Material Library, Storyboard Review).
- **Delivery:** 2 months in 2 phases, a demo every 2 weeks; the client gives feedback on each demo within 2 working days (quote §3, §7).
- **Platform:** web app in the browser, usable on phones; no native mobile app; one UI language (quote §7).
- **Stakeholders:** the clients are stakeholders of the portal, not only users (session note 2026-11-21).

## 3. User Types (preliminary)

| User Type | Pain Point | Primary Need |
|-----------|-----------|--------------|
| Leap Up account / project staff | Feedback scattered across channels; unclear which version a comment refers to (assumed — OQ-1) | One place per project to share files, collect timecoded feedback and track rounds |
| Leap Up admin | Must give each client access only to their own project (board L159, L170) | Create projects and client accounts, assign members (quote P1 #1) |
| Client reviewer | Hard to point at the exact moment in a video that needs changing (assumed — OQ-1) | Review a video and pin comments to exact timecodes (board L26) |
| Client final approver | Needs a clear record of what was approved (Phase 2) | Approve versions and sign off the final cut (quote P2 #3) |

Role details (single client role vs named approvers) are open — OQ-3.

## 4. Capabilities Breakdown

### P0 — must have (MVP, Phase 1)
- **Foundation & admin:** design-based responsive UI; sign in with User ID + password; per-project roles Leap Up / Client; admin page to create projects, create client accounts and assign members (quote P1 #1; board L18–L170).
- **Project Files:** three folders Proposal / Material / Outcome Development; upload files and videos; file status; search; download (quote P1 #2; board L52–L179).
- **Video Review:** online player; comments pinned to timecodes; markers on the timeline; rounds and versions (quote P1 #3; board L42–L193).
- **Deployment & handover:** server, domain, SSL, automatic backups, automatic deployment, user guide (quote P1 #4).

### P1 — should have (Phase 2)
- Home dashboard: stat cards, project progress, Action Required list (quote P2 #1; board L20–L74, L194–L231).
- Task list per project: create, assign, track (quote P2 #1; board L82–L186).
- Production timeline: 5 stages + milestones (quote P2 #2; board L216–L350).
- Outcome approval: approve each version, change requests, approval log, final sign-off (quote P2 #3; board L214–L365).
- E-mail notifications for new video, new comment, approval (quote P2 #4).

### P2 — nice to have / excluded for now
- **Excluded by the quote (post-MVP):** Material Library, Storyboard Review, in-app notifications, realtime updates, multi-company (SaaS) version (quote §7; board L366–L479).

## 5. Core Flows (Happy Path)

### 5.1 End-to-end MVP: create project → invite client → share files → review video

1. A Leap Up admin creates a project: name, client, due date (quote P1 #1; board L16, L24).
2. The admin creates client accounts and assigns members to the project (quote P1 #1).
3. The admin gives the client their User ID and password outside the portal — invite e-mails are Phase 2 (board L159; quote P2 #4).
4. The client signs in and sees only the projects assigned to them (board L18–L120, L146).
5. Leap Up uploads files into Proposal / Material / Outcome Development; each file shows a status (board L52–L72, L98–L179). Whether clients upload too, and where, is open (OQ-9).
6. The client browses, searches and downloads files (quote P1 #2).
7. Leap Up uploads a video as a version within a review round (board L42–L45).
8. The client plays it and pins comments to timecodes; each comment appears as a marker on the timeline (board L55–L147).
9. Leap Up works through the comments (Open → Resolved) and uploads the next version or round (board L80, L131, L187–L193).
10. The loop repeats. Formal approval and final sign-off come in Phase 2; how a round ends in the MVP is open (OQ-13).

```
 LEAP UP ADMIN                      CLIENT                         LEAP UP STAFF
┌──────────────────────┐
│ 1 Create project     │
│ 2 Create client acct │
│   + assign members   │
│ 3 Hand over User ID  │──────────▶┌──────────────────────┐
└──────────────────────┘           │ 4 Sign in            │
                                   │   User ID valid?     │──NO──▶ error, stay on Sign in
                                   │        │ YES         │
                                   │        ▼            │
                                   │  sees ONLY assigned  │
                                   │  projects            │
                                   └──────────┬───────────┘
                                              │            ┌──────────────────────────┐
                                              │◀───────────│ 5 Upload files to folder  │
                                              ▼            │   (Proposal/Material/     │
                                   ┌──────────────────────┐│    Outcome) + status      │
                                   │ 6 Browse / search /  ││ 7 Upload video version   │
                                   │   download files     ││   in round N             │
                                   │ 8 Play video, pin    │└────────────┬─────────────┘
                                   │   comments at time-  │             │
                                   │   codes (markers)    │────────────▶│ 9 Resolve comments,
                                   └──────────────────────┘             │   upload next version
                                              ▲                         │   or round
                                              └─────────────────────────┘
                                     10 repeat · approval / sign-off = Phase 2
```

### 5.2 Phase 2 extension (context only — not designed here)

Dashboard and Action Required → task list → production timeline with 5 stages → outcome approval with change requests and final sign-off (quote P2 #1–#3).

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | When | YES | NO |
|---|---|---|---|---|
| D1 | Sign in | User ID + password match? | Show the user's assigned projects | Error message, stay on Sign in (wording: OQ-16) |
| D2 | Project access | Is the user a member of this project? | Open the project | Not shown / access refused (board L146) |
| D3 | Upload | File type and size allowed? | Store the file in the chosen folder | Reject with a message (limits: OQ-10) |
| D4 | Video review | Comment has a timecode? | Pin as a marker at that time | — (every comment is pinned, board L147) |
| D5 | Round | Are all comments of the round handled? | Leap Up uploads the next version/round | Round stays In Review (rule: OQ-13) |

### 6.2 Scenario Matrix (roles × actions)

| Action | Leap Up admin | Leap Up staff | Client |
|---|---|---|---|
| Create project / client account / assign members | Yes (quote P1 #1) | OQ-4 | No |
| See a project | All | Assigned (assumed) | Assigned only (board L146) |
| Upload files | Yes | Yes | OQ-9 (board shows client uploads, L140–L154) |
| Set file status | OQ-11 | OQ-11 | OQ-11 |
| Comment on video | Yes | Yes (board L118) | Yes (board L75) |
| Mark comment resolved | OQ-12 | OQ-12 | OQ-12 |
| Approve / sign off | Phase 2 | Phase 2 | Phase 2 (final approver: OQ-3) |

### 6.3 State Transitions

```
File:     Shared ──▶ In Review ──▶ Approved ──▶ Final          (board L113, L144, L164, L179)
Comment:  Open ──▶ Resolved                                     (board L80, L131)
Round:    Upcoming ──▶ In Review ──▶ Reviewed                   (board L43–L45)
Project:  In Progress ──▶ (completed — not shown on the board)  (board L19)
```

| Entity | From | To | Trigger | Reversible? |
|--------|------|----|---------|-------------|
| File | Shared | In Review / Approved / Final | Set by whom and when: OQ-11 | OQ-11 |
| Comment | Open | Resolved | Leap Up handles the feedback (who exactly: OQ-12) | OQ-12 (re-open?) |
| Round | Upcoming | In Review | Leap Up uploads a version for the round | No (assumed) |
| Round | In Review | Reviewed | Round ends — rule open (OQ-13) | No (assumed) |
| Project | In Progress | Completed | Not defined on the board (OQ-14) | OQ-14 |

Approval-related statuses (version approved, change request Done / Quote sent / Client approved, board L294–L333) are Phase 2.

### 6.4 Interrupted Transactions

| Situation | What the system keeps | Resume | Cleanup |
|---|---|---|---|
| Browser closed during a large video upload | Open (OQ-15) | Open (OQ-15) | Open (OQ-15) |
| Storage service fails or times out | Nothing new is shown as uploaded (assumed) | User retries | — |
| Session expires while commenting | Unsaved comment text — open (OQ-15) | Sign in again | — |
| Two people act on the same file or comment | Last change wins (assumed) — open (OQ-15) | — | — |
| New version uploaded while the previous round is still in review | Open (OQ-13) | — | — |

### 6.5 Other Edge Cases

- A client assigned to several projects (one login or one per project: OQ-5).
- A client forgets the password — no reset e-mail in the MVP (e-mail is Phase 2; OQ-5).
- A project with no files yet, or a round with no comments (empty states — to design in `/wireframe-html`).
- A comment on a version that is later replaced (stays in the round's history — assumed, OQ-13).
- Board sample file names differ (`711_FILM_R2_V02.mp4` L56 vs `711_FILM_R2_V2.mp4` L351) — sample data, but version naming needs a rule (OQ-11).

## 7. Validation, Limits & Wording

### 7.1 Validation rules

| Field | Rule |
|---|---|
| User ID | Required; issued by Leap Up (board L50, L69, L159) — format: OQ-16 |
| Password | Required; masked with Show toggle (board L79, L89, L90) — policy: OQ-16 |
| Uploaded file | Allowed types and max size: OQ-10 |
| Comment | Pinned to the current timecode (board L147) — max length: OQ-16 |

### 7.2 Limits & Quotas (exact values)

| Parameter | Value | Window | Behaviour when exceeded |
|---|---|---|---|
| Users | ~50 | whole system | Planning figure (quote §1, §5) |
| Stored data | ~300 GB | after year one | Planning figure (quote §5) |
| Max file / video size | TBD (OQ-10) | per file | TBD |
| Failed sign-ins before lock | TBD (OQ-16) | — | TBD |
| Client feedback on demos | 2 working days | per demo | Delays the schedule (quote §7) |

### 7.3 Wording samples (exact strings)

#### Error messages

| Situation | Wording | Code |
|---|---|---|
| Wrong User ID or password | TBD (OQ-16) | E-? |
| File too large / wrong type | TBD (OQ-10) | E-? |

#### Success messages

| Situation | Wording |
|---|---|
| File uploaded | TBD (OQ-16) |

#### Info / neutral messages

| Situation | Wording |
|---|---|
| Sign-in page subtitle | "Sign in to access your project workspace." (board L41) |
| Sign-in brand panel | "Secure project-specific collaboration" (board L108) |
| Access note | "Only assigned project content is visible." (board L146) |
| Account note | "Each client receives a unique User ID and Password for each assigned project. Access is project-specific." (board L159, L170) |
| Video review subtitle | "Review video, pin feedback to exact timecodes, and track revisions" (board L26) |
| Comment box placeholder | "Add comment at 00:15..." (board L147) |

## 8. Assumptions

- Leap Up runs several client projects at the same time; each client sees only its own projects (board L146).
- One Leap Up team serves all clients; no multi-company use (quote §7).
- Video files are large; storage is Cloudflare R2 (quote §5) — upload time matters for users.
- Clients will give feedback inside the portal instead of e-mail/chat (to be validated — see risk R1).
- Board figures (projects, tasks, dates, names) are sample data, not real values (board L11, L196).

## 9. Risks

| Risk | Likelihood | Business consequence | Prevention |
|--------|----------|-------------------|-----------|
| R1 Adoption: clients keep sending feedback by e-mail or chat | sometimes | Feedback stays scattered; the portal loses its purpose | Leap Up asks clients to comment only in the portal; simple onboarding for clients |
| R2 Timeline: slow feedback on demos | sometimes | 2-month plan slips (quote §7 makes 2 working days a condition) | Agree a feedback owner on the client side at kickoff |
| R3 Expectation: clients see 8 designed screens but only 3 are MVP | often | Disappointment or disputes at acceptance | Confirm the excluded scope with Leap Up in writing (C1) |
| R4 Requirement gap: current process unknown | sometimes | The portal may solve the wrong problem | Interview Leap Up about today's workflow before /srs (OQ-1) |
| R5 Data: large video uploads fail on slow connections | sometimes | Missed review rounds, frustrated users | Define limits and resume behaviour early (OQ-10, OQ-15) |
| R6 Vendor: running costs billed in USD change with the exchange rate | rare | Monthly cost above Leap Up's expectation | Leap Up owns the infrastructure accounts and sees the bills (quote §5, §7) |

## 10. Success Criteria (preliminary)

- **MVP outcome reached:** Leap Up can create a project, invite a client, share files and review a video with the client end to end (quote p.1 note after Phase 1).
- **Feedback in one place:** share of client feedback given in the portal instead of other channels — target TBD (OQ-18).
- **Review speed:** time from a new version to the client's comments — baseline unknown (OQ-1), target TBD (OQ-18).
- **Adoption:** number of active projects and client users in the first month — TBD (OQ-2, OQ-18).

## 11. Open Points

Questions to take to Leap Up. Tick each one when answered and note the answer next to it.

### A. Today's way of working & why now
* [ ] OQ-1: How does Leap Up share drafts and collect client feedback today (e-mail, Drive, chat, a review tool)? What goes wrong most often?
* [ ] OQ-2: Why now, and is there a launch date? Which pilot clients and how many projects in the first month?

### B. Roles & access
* [ ] OQ-3 (C4, blocks MVP): Roles in the MVP — (a) Leap Up / Client only, (b) plus a Leap Up admin, or (c) the board's named roles (Brand Manager final approver, Marketing Exec reviewer, Account, Producer)?
* [ ] OQ-4 (C3, blocks MVP): Who administers — one Leap Up admin or any Leap Up staff? What does the admin page need (no wireframe exists)?
* [ ] OQ-5: One login per client person for all their projects, or one per project (board L159)? Who resets a forgotten password in the MVP?
* [ ] OQ-6: Roughly how many of the ~50 users are Leap Up staff vs client users?
* [ ] OQ-7 (C7, blocks MVP): What goes in the "Project Info" tab of the project screen (board L34)?

### C. Files & uploads
* [ ] OQ-8: Is the 10-step MVP flow in §5.1 right — anything missing or in the wrong order?
* [ ] OQ-9: Can clients upload files, and into which folders (board shows client uploads in Proposal and Material, L140–L154)?
* [ ] OQ-10: Allowed file types and maximum file/video size?
* [ ] OQ-11: Who sets file status (Shared / In Review / Approved / Final), when, and can it go back? How are versions named?

### D. Video review
* [ ] OQ-12: Who can comment, and who can mark a comment resolved (or re-open it)?
* [ ] OQ-13: In the MVP (no formal approval yet), how does a round end — Leap Up uploads the next version, or the client marks "done reviewing"? What happens to comments on replaced versions?
* [ ] OQ-14: When is a project "completed", and who closes it?
* [ ] OQ-15: Large uploads and conflicts — what happens if the browser closes mid-upload, the session expires while commenting, or two people change the same item?

### E. Wording & limits
* [ ] OQ-16: Exact messages and rules for sign-in (wrong credentials, lock after N failed attempts, password policy), upload success/failure, and comment length.

### F. Decisions from the quote–board comparison
* [ ] OQ-17 (C1): Does Leap Up accept that Material Library and Storyboard Review are not in the quote (board L366–L479)?
* [ ] OQ-19 (C2): The board note asks for the task list to be updated daily (L199) while the quote excludes realtime — is a daily manual update by the account team enough? (Phase 2)
* [ ] OQ-20 (C5, C6, C9): Revision quota and paid change requests, client inputs checklist, final sign-off checklist — needed in Phase 2 as drawn on the board?

### G. Goals & success
* [ ] OQ-18: Targets for success — e.g. % of feedback given in the portal, days from new version to client comments, number of active projects after the first month.

## 12. Next Steps

* `/brainstorm auth-access` — first MVP feature (sign-in and project access)
* `/brainstorm admin` · `/brainstorm project-files` · `/brainstorm video-review`
* `/brd portal` — optional business case before `/srs`
