---
type: brainstorm
feature: dashboard-tasks
scope: P2
status: draft
updated: 2026-11-22
links:
  - docs/_sources/2026-11-21-leapup-references/bao-gia-leapup-mvp.md
  - docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md
  - docs/_sources/2026-11-21-leapup-references/_comparison.md
---

# Dashboard & Task List — Brainstorm

## 0. Scope

**Tag:** P2 — "Số liệu tổng quan, tiến độ project, danh sách việc cần review (Action Required); tạo, giao, theo dõi task theo project" (quote p.1, P2 #1). Board 02 Home page (L8–L231) and the Task List tab of board 03 (L33).

**Open decisions:** C2 — board note "Cần được update realtime task list mỗi ngày để Account update và client review to do" (L199) vs quote §7 excluding realtime. Treated as OPEN; no realtime behaviour is specified.

## 1. Idea Seed

> "Số liệu tổng quan, tiến độ project, danh sách việc cần review (Action Required); tạo, giao, theo dõi task theo project" (quote P2 #1)

## 2. Context

- Home header "LEAP UP / CLIENT PROJECT PORTAL" (L8) with tabs Dashboard / Project Management / Update Task List (L13–L15).
- **01 Dashboard** stat cards: Active Projects, Total Tasks, Completed Tasks (L20–L37).
- **02 Project Management** project cards: name, "Deadline: {date}", "Progress: {n}%" with a progress bar (L49–L74).
- **03 Update Task List / By Project** (L82): one table per project, columns TASK, OWNER, DUE, STATUS (L94–L97); owners Leap Up / Client; statuses In Progress, Completed, Pending Review, To Do (L107–L186).
- **ACTION REQUIRED** (L194): "{n} Pending Reviews" (L195), note "Items awaiting client review. Dates and tasks below are sample data." (L196); items with title, project, area, description, "Due: {date}, {time}" and "Review Now" (L200–L231). One sample item points to Material Library (L211), which is OUT.
- Board values are sample data (L196).

## 3. User Types

| User Type | Need |
|---|---|
| Leap Up member (Account) | See all projects at a glance; create, assign and update tasks (L199 "Account update") |
| Client | See what is waiting for their review ("client review to do", L199; Action Required L196) |

## 4. Capabilities Breakdown

### P0 (Phase 2)
- Stat cards: Active Projects, Total Tasks, Completed Tasks.
- Project cards with deadline and progress %.
- Task list per project: create, assign (owner), track status (quote P2 #1).
- Action Required list with Review Now.

### TBD
- How progress % is calculated (OQ-1).
- Owner values: only "Leap Up" / "Client" or named people (OQ-2).
- What creates an Action Required item and where Review Now leads (OQ-3).
- Who sees the Home page — Leap Up only, or also clients (OQ-4).
- C2 realtime vs daily update (OQ-5).

## 5. Core Flows

### 5.1 Overview
1. User opens Dashboard (sidebar "Dashboard").
2. Sees stat cards, project cards and Action Required.
3. Presses Review Now → the item's review screen (e.g. Video Review for "Video Round 2", L200–L203).

### 5.2 Manage tasks
1. Leap Up opens "Update Task List" (Home tab L15) or the project's Task List tab (L33).
2. Creates a task: task name, owner, due date, status (columns L94–L97).
3. Updates the status: To Do → In Progress → Pending Review → Completed (values from the board; order TBD — OQ-6).

```
┌──────────────┐  tab  ┌─────────────────────┐  Add task (control TBD)  ┌──────────────────┐
│ Home         │ ────▶ │ Update Task List    │ ───────────────────────▶ │ Task row: TASK,  │
│ (Dashboard)  │       │ by project (L82)    │                           │ OWNER, DUE,      │
└──────┬───────┘       └─────────────────────┘                           │ STATUS           │
       │ Review Now                                                      └──────────────────┘
       ▼
┌──────────────────────┐
│ Target review screen │  (Video Review / Project Detail — TBD per item type)
└──────────────────────┘
```

## 6. System Behavior Deep Dive

| ID | When | YES | NO |
|---|---|---|---|
| D1 | User is Leap Up? | Can create/assign tasks | Client: TBD (OQ-7) |
| D2 | Action Required items exist? | List them | Empty state, wording TBD |

```
Task status values (board): To Do · In Progress · Pending Review · Completed — transitions TBD (OQ-6)
```

## 7. Validation & Wording

| Field | Rule |
|---|---|
| Task name | Required (assumed) |
| Owner | Leap Up / Client (L105, L122) — TBD (OQ-2) |
| Due | Date "18 Nov" format (L106) |
| Status | One of the four board values |

Board wording kept as is; empty/error wording TBD.

## 8. Assumptions

- "Total Tasks" and "Completed Tasks" count tasks of the user's visible projects (assumed — OQ-1).

## 9. Risks

| Risk | Likelihood | Consequence | Prevention |
|---|---|---|---|
| R1 Realtime expectation (L199) vs quote | often | Dispute at acceptance | Resolve C2 in writing |
| R2 Action Required depends on Phase 2 approvals | sometimes | Items unclear until approval exists | Define item sources (OQ-3) |

## 10. Success Criteria

- Leap Up sees every project's progress and pending client reviews on one page.

## 11. Open Points

* [ ] OQ-1: Progress % and stat card counting rules. TBD.
* [ ] OQ-2: Task owner — side (Leap Up/Client) or person. TBD.
* [ ] OQ-3: Action Required item sources and Review Now targets. TBD.
* [ ] OQ-4: Home page for clients too? TBD.
* [ ] OQ-5 (C2): Realtime vs manual daily update (L199). TBD.
* [ ] OQ-6: Task status transitions. TBD.
* [ ] OQ-7: Can clients create/update tasks? TBD.
* [ ] OQ-8: Add/edit/delete task controls — not drawn. TBD.
* [ ] OQ-9: Material Library item in Action Required (L211) — OUT; remove from real data. TBD.
