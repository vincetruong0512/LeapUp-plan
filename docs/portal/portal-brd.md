---
type: brd
feature: portal
status: draft
updated: 2026-11-22
links:
  - docs/portal/brainstorms/project-overview.md
  - docs/_sources/2026-11-21-leapup-references/bao-gia-leapup-mvp.md
  - docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md
  - docs/_sources/2026-11-21-leapup-references/_project-fit.md
  - docs/_sources/2026-11-21-leapup-references/_comparison.md
  - docs/portal/review-2026-11-22-mvp.md
  - docs/portal/delivery-plan.md
---

# Leap Up Client Project Portal — Business Requirements Document

Business layer only: why Leap Up needs the portal, what it must achieve, how far the scope goes and which rules and
risks apply. System behaviour is in the feature specs (`docs/{feature}/srs/`); schedule and sprint deadlines are in
[delivery-plan.md](delivery-plan.md). Anything the quote or Miro board does not state is marked **TBD** or
**Assumption**. Prices and contacts from the quote are not repeated here.

**Terms used here:** *Leap Up* — the video-production agency that commissions the portal. *Client* — Leap Up's
customer company and its reviewers. *Development vendor* — the developer who builds and hands over the portal.

## 1. Executive Summary

Leap Up needs one place where it and each client follow a production project together: share files, review video
to the exact second, track work, record change requests and sign off the final cut (quote §1). How this happens
today is not documented (OQ-portal-1).

The portal serves about 50 users — Leap Up staff and client reviewers — in a web browser, including on phones, in one
UI language: English, as on the agreed design (quote §1, §7; auth-access brainstorm OQ-23). It is delivered in two
phases over two months, with a demo every two weeks (quote §3):

- **Phase 1 — MVP (month 1):** sign-in with a User ID issued by Leap Up and access per project; an admin page to
  create projects and client accounts and assign members; Project Files (Proposal / Material / Outcome folders,
  upload, status, search, download); Video Review (online player, timecoded comments, timeline markers, rounds and
  versions); deployment and handover. **Outcome:** Leap Up can create a project, invite the client, share files and
  review video with the client, end to end (quote p.1).
- **Phase 2 (month 2):** dashboard and task list, production timeline, outcome approval with change requests and
  final sign-off, e-mail notifications, testing and acceptance (quote §2).

Material Library, Storyboard Review, in-app notifications, realtime updates and a multi-company version are excluded
(quote §7), although two of them appear on the Miro board.

User IDs: the quote says accounts are per client ("tài khoản client", P1 #1); the board says "a unique User ID and
Password for each assigned project" (L159). Leap Up decided on 2026-11-21 that **one User ID per person** covers all of
that person's projects (BR-portal-003); aligning the board wording is still open (auth-access OQ-9).

## 2. Business Problem & Context

### 2.1 Problem Statement

| ID | Business Condition | Baseline | Business Impact | Evidence |
|----|--------------------|----------|-----------------|----------|
| BP-portal-01 | Files and feedback for one production are not held in one place shared by Leap Up and the client. | Not available — establish by interviewing Leap Up (OQ-portal-1) | Assumption: feedback is scattered across channels and it is unclear which version a comment refers to. | Quote §1 (goal "ở một nơi"); portal brainstorm §3 (assumed) |
| BP-portal-02 | Clients cannot point to the exact moment in a video that needs changing. | Not available (OQ-portal-1) | Assumption: revision rounds take longer and changes are misread. | Quote §1 "review video theo từng giây"; board L26 (target design) |
| BP-portal-03 | Assumption: there is no controlled, per-project access for clients today. | Not available (OQ-portal-1) | Assumption: a client could see another client's material, or Leap Up manages access by hand. | Inferred from the future-state board text L146, L159, L170 |

### 2.2 Opportunity & Why Now

Leap Up has commissioned the portal in a two-month, two-phase plan with an agreed Miro design (quote §1, §3). The
start date follows contract signature; a launch date and pilot clients/projects are not stated — **TBD (OQ-portal-2)**.

### 2.3 Strategic Alignment

Quote §1 states the goal: one place for Leap Up and the client to follow a video production project. Assumption: a
single client-facing workspace supports Leap Up's client service (to confirm with Leap Up, OQ-portal-1). One Leap Up
team serves all clients — no multi-company use is intended (quote §7).

## 3. Current State, Future State & Gap

### 3.1 Current State (AS-IS)

Not documented in the sources. How Leap Up shares drafts, collects client feedback, tracks rounds and records
approval today is **Not available — establish by interviewing Leap Up (OQ-portal-1)**. No system exists for the portal
yet (portal brainstorm §2).

### 3.2 Future State (TO-BE)

- Leap Up creates each project, creates client accounts and assigns members; each client reviewer signs in with a
  User ID issued by Leap Up and sees only the projects assigned to them (quote P1 #1; board L146, L159).
- Each project holds its files in three folders — Proposal, Material, Outcome — with a status, search and download
  (quote P1 #2).
- Clients watch each video version online and pin comments to exact timecodes; Leap Up works through the comments
  round by round (quote P1 #3).
- In Phase 2: an overview of work and actions required, a five-stage production timeline, approval of each version
  with change requests and an approval history, final sign-off, and e-mail when there is a new video, comment or
  approval — recipients TBD (C8) (quote P2 #1–#4).

### 3.3 Gap

All gaps are assumed until the current state is known (OQ-portal-1).

| Gap | Description | Priority |
|-----|-------------|----------|
| G1 Shared project space | Assumed gap: no single place per project for files and feedback | MVP |
| G2 Precise video feedback | Assumed gap: no way to tie feedback to an exact second of a version | MVP |
| G3 Client access control | Assumed gap: no per-project, Leap Up-issued client access | MVP |
| G4 Visibility of progress and actions | Assumed gap: no shared overview of tasks, stages and what needs the client | P2 |
| G5 Formal approval record | Assumed gap: no recorded approval per version, change requests or final sign-off | P2 |
| G6 Notification | Assumed gap: no message when something needs attention | P2 (e-mail only) |

## 4. Stakeholders

Roles only; no named people.

| Stakeholder Role | Interest | Influence | Stakeholder Requirement / Expectation |
|------------------|----------|-----------|----------------------------------------|
| Leap Up management (sponsor) | Client service, delivery on time and cost | High | Delivery in two phases within two months; changes only by agreed change request (quote §3, §6) |
| Leap Up Admin | Set up projects and access | High | Create projects and client accounts, assign members, reset passwords (quote P1 #1; decision 2026-11-21) |
| Leap Up member (account, producer) | Run production with the client | High | One place per project for files, timecoded feedback and rounds (quote §1); the board shows the Leap Up Account consolidating feedback (L261, P2 section) |
| Client reviewer | Give feedback quickly and precisely | Medium | Sign in simply; see only own project; comment at exact timecodes; use a phone browser (board L26, L146; quote §7) |
| Client final approver | Control what is approved | Medium (P2) | Clear record of approved versions and final sign-off (quote P2 #3); who approves is open (C4, P2 part) |
| Development vendor — delivery lead | Build, deploy and hand over on time | Medium | Demo feedback within 2 working days; logo, content and infrastructure accounts provided by Leap Up (quote §7) |

## 5. Business Objectives & Success Measures

BO-portal-01 and BO-portal-05 are delivery and acceptance objectives. The post-launch business-value measures
(BO-portal-02, BO-portal-04a, BO-portal-04b) have no agreed measure or target yet — TBD pending OQ-portal-1 and OQ-portal-3.

| ID | Objective | Baseline | Target | Timeframe | Success Measure |
|----|-----------|----------|--------|-----------|-----------------|
| BO-portal-01 | *(Delivery)* Leap Up runs a client project end to end in the portal. `MVP` | No portal | All four steps pass: (1) create a project, (2) invite the client, (3) share files, (4) review a video with the client (quote p.1) | Phase 1 handover, end of month 1 (quote §3) | Checklist of the four steps at the Phase 1 handover demo with a Leap Up and a client account; who signs it off: TBD (OQ-portal-9) |
| BO-portal-02 | *(Value)* Client feedback on video is collected in one place and pinned to timecodes. `MVP` | Not available (OQ-portal-1) | TBD (OQ-portal-3) | TBD (OQ-portal-3) | TBD (OQ-portal-3) — candidate measures listed there |
| BO-portal-03 | Each client sees only their own projects. `MVP` | Not available | No client can see another client's project | Phase 1 handover | Access check with two client accounts on every project page and file (auth-access SC-auth-access-01) |
| BO-portal-04a | *(Value)* Final cuts are signed off in the portal with a record. `P2` | Not available | TBD (OQ-portal-3) | TBD (OQ-portal-3) | TBD (OQ-portal-3) — candidate: sign-offs recorded per project |
| BO-portal-04b | *(Value)* Review is faster. `P2` | Not available (OQ-portal-1) | TBD (OQ-portal-3) | TBD (OQ-portal-3) | TBD (OQ-portal-3) — candidate: days from new version to client comments |
| BO-portal-05 | *(Acceptance)* The portal is delivered and accepted within two months. | — | Phase 2 accepted | End of month 2 (quote §3) | Phase 2 acceptance (quote §2 P2 #5); acceptance criteria and signatory TBD (OQ-portal-9) |

## 6. Business Scope

### 6.1 In Scope

- Sign-in with a User ID issued by Leap Up (one per person, decision 2026-11-21); access per project; roles Admin, Leap Up member, Client — provisional (C4) — `MVP` (quote P1 #1)
- Admin: create projects and client accounts, assign members — `MVP` (quote P1 #1)
- Project Files: three folders, upload files and videos, status (status values OPEN — D-04), search, download — `MVP` (quote P1 #2)
- Video Review: online playback, timecoded comments, timeline markers, rounds and versions — `MVP` (quote P1 #3)
- Deployment and Phase 1 handover: hosted on Leap Up-owned services with automatic backup and deployment, user guide — `MVP` (quote P1 #4)
- Dashboard and task list, Action Required — `P2` (quote P2 #1)
- Production timeline: five stages and milestones — `P2` (quote P2 #2)
- Outcome approval: approve each version, change requests, approval history, final sign-off — `P2` (quote P2 #3)
- E-mail on new video, new comment, approval; recipients TBD (C8) — `P2` (quote P2 #4)
- System testing, fixes, acceptance support — `P2` (quote P2 #5)
- Final handover: full source code, installation documents and user guide — `P2` (quote §6)

### 6.2 Out of Scope

- Material Library (board 05, L366–L424) — `OUT` (quote §7); a change-request candidate
- Storyboard Review (board 06, L425–L479) — `OUT` (quote §7); a change-request candidate
- In-app notifications — `OUT` (quote §7)
- Realtime updates — `OUT` (quote §7); see C2 for the daily task-list note on the board
- Multi-company (SaaS) version — `OUT` (quote §7)
- Native mobile app — `OUT` (quote §7)

### 6.3 Assumptions

- Assumption: clients are willing to give feedback in the portal instead of e-mail or chat (portal brainstorm §8; RISK-portal-01).
- Board figures — projects, dates, tasks, names — are sample data, not baselines (board L11, L196).
- About 50 users and about 300 GB of data after year one are planning figures (quote §1, §5); nothing checks them yet.
- How client login details are handed over in Phase 1 (no e-mail until Phase 2, quote P2 #4) is TBD (D-02, OQ-portal-8).

### 6.4 Constraints

- Two months, two phases, a demo every two weeks (quote §3). The 8 weeks start at contract signature (TBD) and
  assume Leap Up's inputs (§6.5) are ready; the length of the preparation period before week 1 is TBD.
- Web app in the browser, usable on phones; one UI language, English, following the agreed design (quote §7, §1).
- Scope as quoted. Changes to design, features or flows are change requests, estimated and done only with Leap Up's
  agreement (quote §6, §7).
- Warranty: defects against accepted scope are fixed free for 3 months "sau nghiệm thu" (quote §6). The quote uses
  "nghiệm thu" (acceptance) only for Phase 2; Phase 1 ends with a handover ("bàn giao"). How Phase 1 defects found in
  month 2 are handled is TBD (OQ-portal-10).
- Files are stored on a storage service in Leap Up's own account (quote §5, §7); the provider choice is in the
  technical design.

### 6.5 Dependencies

| Dependency (Leap Up provides) | Needed by | Source |
|---|---|---|
| Logo | Sprint 1 (app frame) — per delivery-plan §2 | Quote §7 |
| Content — what this covers is TBD (OQ-portal-11) | TBD | Quote §7 |
| Infrastructure accounts: server, storage, domain | Before Sprint 1 (Sprint 0) — per delivery-plan §2 | Quote §7 |
| Feedback on each demo within 2 working days | Every demo | Quote §7 |
| Approved admin design (the board has none) | Before Sprint 1 | C3 |
| Procedure for handing over login details and resetting passwords | Before Sprint 1 | D-01, D-02 |
| Answers to the open points, by sprint | See delivery-plan §6 | [delivery-plan.md](delivery-plan.md) §6 |

## 7. High-level Business Requirements

Every quoted module is contracted at a fixed price per module (quote §2), so all are **Must (contracted)**. Ranking
the Phase 2 modules is not decided here.

| ID | Business Requirement | Business Objective | Scope | Priority |
|----|----------------------|--------------------|-------|----------|
| BREQ-portal-01 | Leap Up can set up a project and decide who takes part in it. | BO-portal-01, BO-portal-03 | MVP | Must (contracted) |
| BREQ-portal-02 | Each client reviewer reaches only the projects Leap Up assigned to them, with login details issued by Leap Up. | BO-portal-03 | MVP | Must (contracted) |
| BREQ-portal-03 | Leap Up and the client exchange project files in agreed folders and can find and download them; status values OPEN (D-04). | BO-portal-01 | MVP | Must (contracted) |
| BREQ-portal-04 | Clients review each video version online and tie every comment to an exact moment; Leap Up follows feedback round by round. | BO-portal-01, BO-portal-02 | MVP | Must (contracted) |
| BREQ-portal-05 | The portal works in a browser on computers and phones, in one language, following the agreed design. | BO-portal-01 | MVP | Must (contracted) |
| BREQ-portal-06 | The portal runs on Leap Up-owned services with backup, and Leap Up receives a user guide at the Phase 1 handover. | BO-portal-01, BO-portal-05 | MVP | Must (contracted) |
| BREQ-portal-07 | Leap Up and clients see an overview of progress, tasks and actions waiting for them. | BO-portal-04a, BO-portal-04b | P2 | Must (contracted) |
| BREQ-portal-08 | Everyone sees where the production stands across five stages and milestones. | BO-portal-04b | P2 | Must (contracted) |
| BREQ-portal-09 | Versions are approved, change requests recorded and the final cut signed off, with a history. | BO-portal-04a | P2 | Must (contracted) |
| BREQ-portal-10 | Project members are told by e-mail about a new video, comment or approval; recipients TBD (C8). | BO-portal-04b | P2 | Must (contracted) |
| BREQ-portal-11 | The whole portal is tested and accepted before final handover. | BO-portal-05 | P2 | Must (contracted) |
| BREQ-portal-12 | Leap Up receives the full source code, installation documents and user guide at final handover. | BO-portal-05 | P2 | Must (contracted, quote §6) |

## 8. Business Rules

Rules about how the portal is used. Contract terms (change requests, warranty, demo feedback) are in §6.4 and §6.5.

| ID | Business Rule | Rationale | Source |
|----|---------------|-----------|--------|
| BR-portal-001 | A client sees only the content of projects they are assigned to. | Client confidentiality | Board L146, L170 |
| BR-portal-002 | Only Leap Up creates accounts and projects; there is no self sign-up. | Leap Up controls access | Board L159; quote P1 #1 |
| BR-portal-003 | One User ID per person covers all of that person's projects. | Simple access for clients | Decision 2026-11-21 (auth-access brainstorm OQ-3); board L159 says per project — wording open (auth-access OQ-9) |
| BR-portal-004 | Users cannot recover their own password in the MVP; the Leap Up admin resets it. How: TBD (D-01). | No e-mail in Phase 1 | Decision 2026-11-21 (auth-access brainstorm OQ-7, OQ-8) |
| BR-portal-005 | Every project has the folders Proposal, Material and Outcome. | Agreed structure | Quote P1 #2; board L52–L54 ("Outcome Development") |
| BR-portal-006 | Every video comment is tied to a timecode of a specific video version. How versions relate to rounds: TBD (D-05). | Precise feedback | Quote §1, P1 #3; board L147 |
| BR-portal-007 | **TBD:** each client login is used by one named person, and how login details are handed over safely (OQ-portal-8). | Access by person; clear comment authors | Not in the sources |
| BR-portal-008 | **TBD:** who may upload into each folder (D-11). | Folder ownership | Board shows client uploads (L140–L154) |
| BR-portal-009 | **TBD:** who may set a file status (D-04). | Status authority | Not in the sources |
| BR-portal-010 | **TBD:** who resolves a video comment (D-08). | Feedback ownership | Not in the sources |
| BR-portal-011 | **TBD:** how conflicting feedback from two client reviewers is handled; the board shows the Leap Up Account "consolidates feedback" (L261, P2 section). | One clear instruction per round | Board L261 |
| BR-portal-012 | **TBD:** when a project is closed, what happens to its files and accounts, and how long material is kept (OQ-portal-5, OQ-portal-6). | Data retention | Not in the sources |
| BR-portal-013 | **OPEN (C5, P2):** from round 3 onwards, revisions are additional scope and cost. | Revision quota | Board L270; not in the quote |
| BR-portal-014 | **OPEN (C4, P2 part):** the client's Brand Manager gives final approval. MVP roles are provisionally decided (Admin, Leap Up member, Client). | Approval authority | Board L246–L254; quote names only Leap Up / Client |

## 9. Cost-Benefit (qualitative)

### 9.1 Cost Drivers

- Development of Phase 1 and Phase 2 (figures: see quote §2, private reference).
- Monthly running costs paid by Leap Up directly to providers: server, file storage, e-mail sending, domain; billed
  in USD, so they move with the exchange rate (figures: see quote §5, private reference).
- Leap Up time: demo feedback within 2 working days, setting up accounts, onboarding clients (quote §7).
- Change requests for anything outside the quote, e.g. Material Library or Storyboard Review (quote §6).

### 9.2 Expected Benefits

All assumed until OQ-portal-1 and OQ-portal-3 are answered:

- Assumption: one place per project for files and feedback, so less searching across channels (BO-portal-01, -02).
- Assumption: feedback tied to exact seconds and versions, so fewer misunderstandings per round (BO-portal-02).
- Controlled client access per project (BO-portal-03).
- In Phase 2, a recorded approval trail and final sign-off that support acceptance and change-request discussions
  (BO-portal-04a).

### 9.3 Priority / Rough ROI

Not available as a figure: no current-cost or time baseline exists (OQ-portal-1) and benefit targets are TBD
(OQ-portal-3). Every module is contracted (quote §2). Investment analysis, if needed, is a separate business case
owned by the sponsor.

## 10. Risks

Likelihood and impact are **Assumption — BA estimate, to confirm with Leap Up**. Mitigations are **proposed — to
confirm with Leap Up**. One owner per risk.

| ID | Risk | Likelihood | Impact | Mitigation (proposed) | Owner Role |
|----|------|------------|--------|------------|------------|
| RISK-portal-01 | Clients keep sending feedback by e-mail or chat. | Medium | High — the portal loses its purpose | Leap Up asks clients to comment only in the portal; simple onboarding | Leap Up management |
| RISK-portal-02 | Demo feedback is slower than 2 working days (§6.5). | Medium | High — the plan slips | Name a feedback owner at kick-off. Effect of late feedback on the schedule: TBD (not in the quote) | Leap Up management |
| RISK-portal-03 | Leap Up expects all 8 designed board screens, but only some are quoted. | High | Medium — disputes at acceptance | Confirm the excluded scope in writing (C1) | Development vendor — delivery lead |
| RISK-portal-04 | Open points are not answered before the sprint that needs them. | Medium | High — sprint scope slips | Track the full list with deadlines in delivery-plan §6 (includes D-01…D-13 and other open points) | Development vendor — delivery lead |
| RISK-portal-05 | Current way of working is unknown, so the portal may solve the wrong problem. | Medium | Medium | Interview Leap Up about today's workflow (OQ-portal-1) | Leap Up management |
| RISK-portal-06 | Large video uploads fail on slow connections. | Medium | Medium — missed review rounds | Agree file limits and retry behaviour early (D-11; project-files OQ-4, OQ-11) | Development vendor — delivery lead |
| RISK-portal-07 | Running costs rise with storage use or the exchange rate. | Low | Low | Leap Up owns the infrastructure accounts and sees the bills (quote §5, §7) | Leap Up management |
| RISK-portal-08 | File statuses "Approved" / "Final" in Phase 1 are read as formal approval, which is Phase 2. | Medium | Medium — scope creep or disputes | Decide whether they are manual labels in Phase 1 (D-04) | Leap Up management |
| RISK-portal-09 | Leap Up inputs arrive late: logo, content, infrastructure accounts (§6.5). | Medium | High — design and deployment slip | Request at kick-off; needed before Sprint 1 | Leap Up management |
| RISK-portal-10 | No time to act on demo feedback before handover: the Phase 1 handover falls in the same week as demo D2, and feedback may arrive up to 2 working days later (quote §3, §7). The same applies to Phase 2 acceptance. | Medium | Medium — handover with known issues | TBD — agree with Leap Up; no schedule change proposed here | Development vendor — delivery lead |
| RISK-portal-11 | Stored video grows beyond the ~300 GB first-year planning figure (quote §5). | TBD | Medium — running cost | TBD — who decides on clean-up or a larger plan (OQ-portal-5) | Leap Up management |

## 11. Open Questions

The full list of open points with sprint deadlines is [delivery-plan.md](delivery-plan.md) §6. This section lists the
business questions. IDs follow the portal brainstorm where one exists.

**Business questions for this BRD**

- [ ] OQ-portal-1 (brainstorm OQ-1): How does Leap Up share drafts and collect client feedback today, and what goes wrong most often?
- [ ] OQ-portal-2 (brainstorm OQ-2): Launch date, pilot clients and number of projects in the first month.
- [ ] OQ-portal-3 (brainstorm OQ-18): Success measures and targets for BO-portal-02 and BO-portal-04a/b. Candidates to choose from: share of client video feedback given in the portal; sign-offs recorded per project; days from new version to client comments.
- [ ] OQ-portal-4 (brainstorm OQ-6): How many of the ~50 users are Leap Up staff vs client users?
- [ ] OQ-portal-5: Project closure — archive, read-only or delete; how long files and videos are kept; who decides when storage grows.
- [ ] OQ-portal-6: Who owns client material after handover, and after the warranty ends.
- [ ] OQ-portal-7: Offboarding — a client reviewer leaves the client company, or a Leap Up member leaves.
- [ ] OQ-portal-8: May one client login be shared by several people; how login details are handed over safely (with D-01, D-02).
- [ ] OQ-portal-9: Acceptance criteria and who signs the Phase 1 handover and Phase 2 acceptance.
- [ ] OQ-portal-10: How Phase 1 is checked at handover, and how Phase 1 defects found in month 2 are handled.
- [ ] OQ-portal-11: What "content" Leap Up provides (quote §7), and by when.

**Quote ↔ board items** (`_comparison.md`)

- [ ] C1 `OUT` — Leap Up confirms Material Library and Storyboard Review are not in this contract (expectation; at kick-off).
- [ ] C2 `P2` — Daily task-list update by the account team vs realtime (board L199). Before Sprint 3.
- [ ] C3 `MVP` — Admin design; the board has none. Before Sprint 1.
- [x] C4 `MVP` part — roles Admin, Leap Up member, Client, provisionally decided 2026-11-21. [ ] `P2` part — final approver (BR-portal-014). Before Sprint 4.
- [ ] C5 `P2` — revision quota and change-request cost. Before Sprint 4.
- [ ] C6 `P2` — client inputs checklist and feedback rule. Before Sprint 3.
- [ ] C7 `MVP` — Project Info tab content. Before Sprint 1.
- [ ] C8 `P2` — e-mail triggers and recipients. Before Sprint 4.
- [ ] C9 `P2` — final sign-off checklist. Before Sprint 4.

**Business decisions from the 2026-11-22 MVP review** ([review-2026-11-22-mvp.md](review-2026-11-22-mvp.md) §1;
the system-behaviour decisions D-06, D-07, D-09, D-10, D-12 are tracked there)

- [ ] D-01 / D-02 — password reset procedure; how Leap Up member and first Admin accounts are created
- [ ] D-03 — account role vs project role; does Admin see all projects
- [ ] D-04 — are file statuses Approved / Final Phase 1 labels or Phase 2 approval; who sets them
- [ ] D-05 — how a project file becomes a review version and round
- [ ] D-08 — who resolves comments
- [ ] D-11 — upload rights per folder and limits
- [ ] D-13 — required project fields, assignment errors, deactivation
