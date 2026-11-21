---
type: brainstorm
feature: admin
scope: MVP
status: draft
updated: 2026-11-22
links:
  - docs/_sources/2026-11-21-leapup-references/bao-gia-leapup-mvp.md
  - docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md
  - docs/_sources/2026-11-21-leapup-references/_comparison.md
  - docs/auth-access/brainstorms/login-screen.md
---

# Admin — Projects, Client Accounts, Members — Brainstorm

## 0. Scope

**Tag:** MVP — "trang quản trị: tạo project, tài khoản client, gán thành viên" (quote p.1, P1 #1).

**Open decision:** the board has **no admin screen** (C3). Requirements only; screen design is TBD and is not invented here (strict-reference rule, 2026-11-22).

## 1. Idea Seed

> "trang quản trị: tạo project, tài khoản client, gán thành viên" (quote P1 #1)

A Leap Up admin creates a project, creates client accounts and assigns members to the project, so the client can sign in and see only that project.

## 2. Context

- Step 1–2 of the MVP outcome: "Leap Up đã có thể tạo project, mời khách…" (quote p.1, after Phase 1 table).
- No e-mail in Phase 1: "inviting" a client means creating the account and handing over the User ID and password outside the portal (quote P2 #4; board L159).
- Project information shown elsewhere on the board: project name "711" (L16), client "7-Eleven" and due date (L24), status "In Progress" (L19), project description "Social Campaign Film 30s" (L22). Board values are sample data (L196).
- Roles decided for now: Admin, Leap Up member, Client (auth-access OQ-2, C4).

## 3. User Types

| User Type | Pain Point | Primary Need |
|-----------|-----------|--------------|
| Admin (Leap Up) | Must give each client access to their own project only | Create projects and client accounts; assign members |
| Leap Up member | Needs to reach the projects they work on | Be assigned to projects |
| Client | Needs a login from Leap Up | Receive a User ID and password; be assigned to their project |

## 4. Capabilities Breakdown

### P0 — must have (quote P1 #1)
- Create a project.
- Create a client account (User ID + password).
- Assign members to a project (Leap Up / Client role in the project).

### TBD — implied but not stated in the reference
- Edit a project; project status changes (only "In Progress" is shown, L19) — OQ-3.
- Create Leap Up member accounts (quote names only "tài khoản client") — OQ-2.
- Reset a user's password (needed because users cannot reset it themselves — auth-access OQ-7/8) — OQ-5.
- Remove a member from a project; deactivate an account — OQ-6.
- Lists of projects and users for the admin — OQ-7.

### Post-MVP
- Multi-company (SaaS) administration (quote §7, excluded).

## 5. Core Flows (Happy Path)

### 5.1 Create a project
1. Admin opens the admin page (entry point TBD — OQ-1).
2. Admin enters the project details: name, client, due date, description (fields as displayed on the board L16, L22, L24; exact field list TBD — OQ-3).
3. System saves the project; it starts with status "In Progress" (L19 — initial status TBD, OQ-3).
4. The project has three folders Proposal / Material / Outcome Development (quote P1 #2; board L52–L54) — created automatically (assumed).

### 5.2 Create a client account
1. Admin enters the client person's name, User ID and initial password (OQ-4).
2. System checks the User ID is unique; saves the account.
3. Admin hands over User ID and password outside the portal.

### 5.3 Assign members
1. Admin opens a project and adds users as members with role Leap Up or Client (quote P1 #1 "phân quyền theo project (Leap Up / Client)").
2. The client now sees this project after sign-in (auth-access FR-006).

```
┌───────────────┐    ┌────────────────────┐    ┌────────────────────┐    ┌─────────────────┐
│ Create project│ ─▶ │ Create client      │ ─▶ │ Assign members     │ ─▶ │ Hand over User  │
│ (name, client,│    │ account (User ID,  │    │ (Leap Up / Client) │    │ ID + password   │
│  due, desc.)  │    │  password)         │    │                    │    │ outside portal  │
└───────────────┘    └─────────┬──────────┘    └────────────────────┘    └─────────────────┘
                               │ User ID already used?
                               ▼ YES
                     ┌────────────────────┐
                     │ Error, wording TBD │
                     └────────────────────┘
```

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | When | YES | NO |
|---|---|---|---|
| D1 | Required project fields filled? | Save project | Error, wording TBD |
| D2 | User ID unique? | Save account | Error, wording TBD |
| D3 | User already a member of the project? | No change (assumed) | Add member |

### 6.2 Scenario Matrix

| Action | Admin | Leap Up member | Client |
|---|---|---|---|
| Create project | Yes | TBD (OQ-2) | No |
| Create client account | Yes | TBD (OQ-2) | No |
| Assign members | Yes | TBD (OQ-2) | No |

### 6.3 State Transitions

| Entity | From | To | Trigger | Reversible? |
|---|---|---|---|---|
| Project | — | In Progress | Created (L19) | — |
| Project | In Progress | other states | TBD (OQ-3; portal OQ-14) | TBD |

## 7. Validation, Limits & Wording

| Field | Rule |
|---|---|
| Project name | Required (assumed); length TBD |
| Client (company) name | TBD |
| Due date | TBD whether required |
| User ID | Required, unique, short username, not case-sensitive (auth-access OQ-4) |
| Password | Rules TBD (auth-access OQ-5) |

All admin screen labels, messages and wording: **TBD** — no board design.

## 8. Assumptions

- The three folders exist in every project (quote P1 #2).
- The admin is a Leap Up person (role decision OQ-2 in auth-access).

## 9. Risks

| Risk | Likelihood | Consequence | Prevention |
|---|---|---|---|
| R1 Scope: admin UI has no agreed design | often | Rework at demo; possible change request (quote §6) | Leap Up approves admin screens before build (C3) |
| R2 Data: client assigned to the wrong project | rare | Confidential content exposed | Admin sees the member list per project before saving (TBD design) |

## 10. Success Criteria

- Admin can create a project, a client account and assign the client in one session (MVP outcome, quote p.1).

## 11. Open Points

* [ ] OQ-1 (C3): Admin screen design and entry point — no board screen. TBD.
* [ ] OQ-2: Who administers — only Admin, or also Leap Up members? Can admin create Leap Up member accounts? TBD.
* [ ] OQ-3: Project fields (name, client, due date, description?) and project statuses beyond "In Progress". TBD.
* [ ] OQ-4: Who sets the initial password, and how it is handed over. TBD.
* [ ] OQ-5: Password reset by admin — needed (users cannot reset)? TBD.
* [ ] OQ-6: Remove member / deactivate account — needed? TBD.
* [ ] OQ-7: Lists and search for projects and users in admin. TBD.
* [ ] OQ-8: Project Info tab content (C7, board L34) — filled from project details? TBD.

## 12. Next Steps

* `/srs admin`
