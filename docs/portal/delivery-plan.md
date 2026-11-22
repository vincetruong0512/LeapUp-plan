---
type: delivery-plan
feature: portal
status: draft
updated: 2026-11-22
links:
  - docs/_sources/2026-11-21-leapup-references/bao-gia-leapup-mvp.md
  - docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md
  - docs/_sources/2026-11-21-leapup-references/_comparison.md
---

# Leap Up Client Project Portal — Delivery Plan

Plan for the development team, built from the quote and the Miro board only. Anything the reference does not state is **TBD** and listed in §6.

## 1. What is delivered

| Phase | Feature (slug) | Quote | Board | Stories | Status of docs |
|---|---|---|---|---|---|
| **Phase 1 — MVP** | Login & project access (`auth-access`) | P1 #1 | 01 | 3 | brainstorm → stories done (draft) |
| | Admin (`admin`) | P1 #1 | — (C3) | 3 | wireframe blocked: no design |
| | Project Files (`project-files`) | P1 #2 | 03 | 5 | done (draft) |
| | Video Review (`video-review`) | P1 #3 | 07 | 5 | done (draft) |
| | Deployment & handover | P1 #4 | — | work package (§3) | — |
| **Phase 2** | Dashboard & Task list (`dashboard-tasks`) | P2 #1 | 02 | 4 | done (draft) |
| | Production Timeline (`production-timeline`) | P2 #2 | 04 | 3 | done (draft); C6 OPEN |
| | Outcome Approval (`outcome-approval`) | P2 #3 | 08 | 4 | done (draft); C4/C5/C9 OPEN |
| | E-mail notifications (`email-notifications`) | P2 #4 | — | 3 | no UI |
| | Testing & acceptance | P2 #5 | — | work package (§3) | — |
| **Not quoted — change request (OUT)** | Material Library (`material-library`, board section "MARTERIAL ALIGNMENT") | §7 | 05 | 4 | fully documented (draft); not scheduled |
| | Storyboard Review (`storyboard-review`, board section "MATERIAL \| DETAIL SCRIPT & STORY BOARD") | §7 | 06 | 3 | fully documented (draft); not scheduled |
| | In-app notifications, realtime updates, multi-company SaaS | §7 | — | — | not planned |

Totals (quoted scope): 8 features · 84 functional requirements · 25 error codes (wording TBD) · 30 user stories · 97 acceptance criteria (drafts; 22 marked blocked by an open question, after the 2026-11-22 review) · 20 wireframe screens on 6 features. OUT add-ons: 2 features · 26 FR · 8 error codes · 7 stories · 17 AC · 9 screens. Board → feature map: [board-map.md](board-map.md).

**Change-request add-ons (not in the 8 weeks):** Material Library and Storyboard Review are ready to estimate if Leap Up orders them (quote §6). They depend on Project Files (upload, R2) and on the approver rule (C4); they are not in the sprint plan below.

**Phase 1 outcome (quote p.1):** "Sau phase 1, Leap Up đã có thể tạo project, mời khách, gửi file và review video với khách."

## 2. Timeline

The quote fixes 2 months in 2 phases, a demo every 2 weeks, and client feedback on each demo within 2 working days (quote §3, §7). **Start date: TBD** (contract signature).

```
Week        1        2        3        4    │    5        6        7        8
            ├─ Sprint 1 ──────┤├─ Sprint 2 ──────┤├─ Sprint 3 ──────┤├─ Sprint 4 ──────┤
Phase 1     Foundation, login,  Video Review,     │
            admin, Files        deploy, handover  │
Phase 2                                           │ Dashboard, Tasks,  Outcome Approval,
                                                  │ Timeline           e-mail, testing
Demos                 ▲ D1               ▲ D2 + Phase 1 handover    ▲ D3              ▲ D4 + acceptance
Client feedback        └ ≤ 2 working days └ ≤ 2 working days         └ ≤ 2 wd          └ ≤ 2 wd
```

| Sprint | Weeks | Quote content (§3) | Stories | Demo / milestone |
|---|---|---|---|---|
| 0 (before week 1) | — | — | Settle blocking open points (§6); Leap Up creates server, storage and domain accounts (quote §7) | Kick-off |
| 1 | 1–2 | Nền tảng, đăng nhập, phân quyền, trang quản trị, Project Files | auth-access US-001…003 · admin US-001…003 · project-files US-001…005 | **D1** — sign in, admin set-up, files |
| 2 | 3–4 | Video Review, triển khai server, bàn giao phase 1 | video-review US-001…005 · deployment & handover work package | **D2 + Phase 1 handover** (MVP outcome end to end) |
| 3 | 5–6 | Dashboard, Task list, Production Timeline | dashboard-tasks US-001…004 · production-timeline US-001…003 | **D3** |
| 4 | 7–8 | Outcome Approval, thông báo email, kiểm thử, nghiệm thu | outcome-approval US-001…004 · email-notifications US-001…003 · testing & acceptance | **D4 + Phase 2 acceptance** |
| Warranty | 3 months after acceptance | Free fixes for defects against accepted scope; changes are separate change requests (quote §6) | — | — |

Payment milestones follow signature, Phase 1 handover and Phase 2 acceptance (quote §4); amounts are not repeated here.

### 2.1 Story order inside each sprint

| Sprint | Order (dependencies first) |
|---|---|
| 1 | admin US-001 create project → admin US-002 client account → admin US-003 assign members → auth-access US-001 sign in → auth-access US-002 assigned projects only → auth-access US-003 sign out → project-files US-001 view → US-002 upload → US-003 search/filter → US-004 download |
| 2 | video-review US-001 play → US-002 timecoded comment → US-003 resolve → US-004 rounds/versions → US-005 change log → project-files US-005 open video → deployment & handover |
| 3 | dashboard-tasks US-002 create/assign tasks → US-003 track status → US-001 overview → US-004 Action Required → production-timeline US-001 view → US-002 maintain → US-003 client inputs (only if C6 is accepted) |
| 4 | outcome-approval US-001 approve version → US-002 change requests → US-003 final sign-off → US-004 rounds/approvers (only if C4/C5 are accepted) → email-notifications US-001…003 → testing & acceptance |

## 3. Work packages without user stories

| Package | Phase | Content (quote) | Output |
|---|---|---|---|
| Foundation | 1 | "Giao diện theo design, responsive" (P1 #1) | App shell: sidebar, breadcrumb, tabs, header patterns shared by boards 03, 04, 07, 08 |
| Deployment & handover | 1 | "Cài đặt server, domain, SSL, backup tự động, tự động deploy; hướng dẫn sử dụng" (P1 #4) | Production server, domain, SSL, automatic backups, automatic deploy, **user guide** |
| Testing & acceptance | 2 | "Kiểm thử toàn hệ thống, sửa lỗi, hỗ trợ nghiệm thu và bàn giao" (P2 #5) | Test pass on all stories' AC, defect fixes, acceptance support |
| Final handover | 2 | "Bàn giao toàn bộ mã nguồn, tài liệu cài đặt và hướng dẫn sử dụng" (§6) | Source code, installation guide, user guide |

## 4. Definition of Ready / Done (for the team)

- **Ready:** story status `approved`; its 🔴 open questions settled; error wording agreed; wireframe confirmed by Leap Up (admin: design provided).
- **Done:** all AC pass on the staging/demo environment; project-scoped access checked with two client accounts; works in a phone browser (quote §7); demoed to Leap Up.

## 5. Documents

| Feature | Brainstorm | SRS | User flow | Wireframes | Stories | Jira import |
|---|---|---|---|---|---|---|
| auth-access | [login-screen](../auth-access/brainstorms/login-screen.md) | [spec](../auth-access/srs/auth-access-spec.md) | [flow](../auth-access/srs/auth-access-userflow.md) | [open](../auth-access/html-wireframe/auth-access-wireframe.html) | [index](../auth-access/userstories/auth-access-story-index.md) | [file](../exports/jira-import-auth-access-2026-11-22.md) |
| admin | [admin-management](../admin/brainstorms/admin-management.md) | [spec](../admin/srs/admin-spec.md) | [flow](../admin/srs/admin-userflow.md) | blocked (C3) | [index](../admin/userstories/admin-story-index.md) | [file](../exports/jira-import-admin-2026-11-22.md) |
| project-files | [brainstorm](../project-files/brainstorms/project-files.md) | [spec](../project-files/srs/project-files-spec.md) | [flow](../project-files/srs/project-files-userflow.md) | [open](../project-files/html-wireframe/project-files-wireframe.html) | [index](../project-files/userstories/project-files-story-index.md) | [file](../exports/jira-import-project-files-2026-11-22.md) |
| video-review | [brainstorm](../video-review/brainstorms/video-review.md) | [spec](../video-review/srs/video-review-spec.md) | [flow](../video-review/srs/video-review-userflow.md) | [open](../video-review/html-wireframe/video-review-wireframe.html) | [index](../video-review/userstories/video-review-story-index.md) | [file](../exports/jira-import-video-review-2026-11-22.md) |
| dashboard-tasks | [brainstorm](../dashboard-tasks/brainstorms/dashboard-tasks.md) | [spec](../dashboard-tasks/srs/dashboard-tasks-spec.md) | [flow](../dashboard-tasks/srs/dashboard-tasks-userflow.md) | [open](../dashboard-tasks/html-wireframe/dashboard-tasks-wireframe.html) | [index](../dashboard-tasks/userstories/dashboard-tasks-story-index.md) | [file](../exports/jira-import-dashboard-tasks-2026-11-22.md) |
| production-timeline | [brainstorm](../production-timeline/brainstorms/production-timeline.md) | [spec](../production-timeline/srs/production-timeline-spec.md) | [flow](../production-timeline/srs/production-timeline-userflow.md) | [open](../production-timeline/html-wireframe/production-timeline-wireframe.html) | [index](../production-timeline/userstories/production-timeline-story-index.md) | [file](../exports/jira-import-production-timeline-2026-11-22.md) |
| outcome-approval | [brainstorm](../outcome-approval/brainstorms/outcome-approval.md) | [spec](../outcome-approval/srs/outcome-approval-spec.md) | [flow](../outcome-approval/srs/outcome-approval-userflow.md) | [open](../outcome-approval/html-wireframe/outcome-approval-wireframe.html) | [index](../outcome-approval/userstories/outcome-approval-story-index.md) | [file](../exports/jira-import-outcome-approval-2026-11-22.md) |
| email-notifications | [brainstorm](../email-notifications/brainstorms/email-notifications.md) | [spec](../email-notifications/srs/email-notifications-spec.md) | [flow](../email-notifications/srs/email-notifications-userflow.md) | n/a (no UI) | [index](../email-notifications/userstories/email-notifications-story-index.md) | [file](../exports/jira-import-email-notifications-2026-11-22.md) |

Use cases and diagrams (19 use cases, one sequence or activity diagram each): `docs/{feature}/usecases/{feature}-usecase-index.md` and `docs/{feature}/srs/{feature}-flows.md` for every feature above.

Critical error and edge-case scenarios (proposal, with one error flow diagram): [error-edge-cases.md](error-edge-cases.md).

Technical proposal: [technical-solution-design.md](technical-solution-design.md).

## 6. Open points to settle, by deadline

Details and numbering live in each feature's spec §12.

This is the full list of open points by deadline. Thirteen of them are cross-feature decisions D-01…D-13 from the 2026-11-22 MVP review ([review-2026-11-22-mvp.md](review-2026-11-22-mvp.md)); the rest are feature-level open questions. Business questions not tied to a sprint are in [portal-brd.md](portal-brd.md) §11.

### Before Sprint 1 (blocks Phase 1 build)
- **C3** Admin screen design, entry point and order of set-up steps (admin OQ-1, OQ-11) — no board screen.
- **Who administers; how Leap Up member accounts and the first Admin account are created** (admin OQ-2).
- **Project fields**, required fields and initial status (admin OQ-3).
- **Password reset** — decided that the admin resets it; how is TBD (admin OQ-5). Remove member / deactivate account (admin OQ-6, auth-access OQ-8). Assignment errors (admin OQ-10).
- **Roles:** does Admin see all projects; can one person hold different roles on different projects (auth-access OQ-10).
- **Landing page** after sign-in and the projects list (auth-access OQ-1, project-files OQ-2).
- Sign-in error behaviour (auth-access OQ-13).
- **Upload rules:** allowed types, max size, client upload rights, folder choice (project-files OQ-3, OQ-4).
- **File status rules**, and whether Approved / Final are Phase 1 labels or P2 approval (project-files OQ-5, OQ-13).
- **C7** Project Info tab content (project-files OQ-1); what P2 tabs and links do in Phase 1 (project-files OQ-14).
- **File ↔ review link and round vs version model** — moved here from Sprint 2 because Project Files (Sprint 1) stores the videos (project-files OQ-17, video-review OQ-3, OQ-10). Video Review entry (video-review OQ-1 = project-files OQ-8).
- Login security: lockout, session expiry, password rules (auth-access OQ-3, OQ-4, OQ-7).
- **Phone browser:** phone layouts or a stacking rule, and test devices (auth-access OQ-5, project-files OQ-9, video-review OQ-8).
- All error and empty-state wording (every spec's Error Matrix).

### Before Sprint 2
- Round status triggers (video-review OQ-4).
- Who resolves comments; change-log editing and its Phase 1 status lines (video-review OQ-2, OQ-5, OQ-13).
- Comments on past / no-video rounds; timecode capture moment; submit control (video-review OQ-11, OQ-12, OQ-15).

### Before Sprint 3
- **C2** realtime vs daily task update (dashboard-tasks OQ-5).
- Progress and stat rules; Action Required sources (dashboard-tasks OQ-1, OQ-3).
- **C6** Client Inputs and Feedback Rule in scope? (production-timeline OQ-5, OQ-6).

### Before Sprint 4
- **C4** who may approve; **C5** revision quota and change-request cost; **C9** sign-off checklist (outcome-approval OQ-2, OQ-5, OQ-6).
- E-mail recipients, content, e-mail address on accounts (email-notifications OQ-1…OQ-3).

### Expectation
- **C1** Leap Up confirms Material Library and Storyboard Review are not in this contract.

## 7. Risks to the plan

| Risk | Effect | Mitigation |
|---|---|---|
| Open points in §6 not answered before their sprint | Sprint scope slips; demo feedback loop breaks | Weekly open-point review with Leap Up; 2-working-day feedback rule (quote §7) |
| Admin design missing (C3) | Sprint 1 cannot finish admin UI | Leap Up provides/approves admin screens in Sprint 0 |
| OPEN items (C4, C5, C6, C9) treated as included | Change-request disputes (quote §6, §7) | Keep their stories `draft` until decided |
| Infrastructure accounts not created by Leap Up | Deployment blocked (quote §7) | Request in Sprint 0 |
