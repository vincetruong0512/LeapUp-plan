---
type: srs
feature: dashboard-tasks
scope: P2
status: draft
updated: 2026-11-22
links:
  - docs/dashboard-tasks/brainstorms/dashboard-tasks.md
  - docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md
---

# dashboard-tasks — Software Requirements Specification

## 1. Scope

Home page with stat cards, project cards, task list by project and Action Required; task list tab in the project. P2 — quote P2 #1; board 02 (L8–L231), board 03 tab L33.

## 2. Actors & Stakeholders

| Actor | Type | Goal | In scope? |
|-------|------|------|-----------|
| Leap Up member | person | Track projects and tasks | Yes |
| Client | person | See items awaiting their review (TBD, OQ-4) | Yes |

## 3. Functional Requirements (FR)

| ID | Title | Description | Scope | Priority | Verify by | Source |
|----|-------|-------------|-------|----------|-----------|--------|
| FR-dashboard-tasks-001 | Home header and tabs | Header "LEAP UP / CLIENT PROJECT PORTAL"; tabs Dashboard, Project Management, Update Task List. | P2 | P0 | demo | board L8, L13–L15 |
| FR-dashboard-tasks-002 | Stat cards | Show Active Projects, Total Tasks, Completed Tasks counts. Counting rules TBD (OQ-1). | P2 | P0 | demo | board L20–L37 |
| FR-dashboard-tasks-003 | Project cards | One card per visible project: name, "Deadline: {date}", "Progress: {n}%", progress bar. Progress rule TBD (OQ-1). | P2 | P0 | demo | quote P2 #1; board L49–L74 |
| FR-dashboard-tasks-004 | Task list by project | Per project a table TASK, OWNER, DUE, STATUS. | P2 | P0 | demo | board L82–L186 |
| FR-dashboard-tasks-005 | Create task | Leap Up creates a task in a project with name, owner, due date, status. Control not drawn (OQ-8). | P2 | P0 | demo | quote P2 #1 "tạo" |
| FR-dashboard-tasks-006 | Assign task | Set the task owner (Leap Up / Client — OQ-2). | P2 | P0 | demo | quote P2 #1 "giao"; board L95 |
| FR-dashboard-tasks-007 | Track task status | Update status: To Do, In Progress, Pending Review, Completed. | P2 | P0 | demo | quote P2 #1 "theo dõi"; board L107, L117, L124, L135 |
| FR-dashboard-tasks-008 | Project Task List tab | The project's Task List tab shows that project's tasks. | P2 | P1 | demo | board L33 |
| FR-dashboard-tasks-009 | Action Required | List items awaiting client review: count "{n} Pending Reviews", title, project, area, description, "Due: {date}, {time}", Review Now. Sources TBD (OQ-3). | P2 | P0 | demo | quote P2 #1; board L194–L231 |
| FR-dashboard-tasks-010 | Review Now | Review Now opens the item's review screen. Targets TBD (OQ-3). | P2 | P0 | demo | board L203, L212, L223 |
| FR-dashboard-tasks-011 | Project-scoped | Only projects the user is assigned to are counted and shown. | P2 | P0 | test | auth-access FR-009 |

## 4. Non-Functional Requirements (NFR)

| ID | Category | Requirement | Priority | Acceptance |
|----|----------|-------------|----------|------------|
| NFR-dashboard-tasks-001 | freshness | Data shown on page load; no realtime push (quote §7). | P0 | Refresh shows changes; realtime is OUT (C2 OPEN) |
| NFR-dashboard-tasks-002 | usability | Usable in a phone browser. | P0 | quote §7 |

## 5. Business Rules

| ID | Rule | Trigger | Implements FR | Source |
|----|------|---------|---------------|--------|
| BR-dashboard-tasks-001 | Task status ∈ {To Do, In Progress, Pending Review, Completed}. | Status change | FR-dashboard-tasks-007 | board L107–L186 |
| BR-dashboard-tasks-002 | A task belongs to one project. | Create task | FR-dashboard-tasks-004 | quote "task theo project"; board L82 |
| BR-dashboard-tasks-003 | Realtime updates are not provided. | Any change | NFR-dashboard-tasks-001 | quote §7 |

## 6. Error Matrix

| Error ID | Title | Trigger | Severity | Related FR | Wording (exact) | Screen state | Recovery |
|----------|-------|---------|----------|------------|-----------------|--------------|----------|
| E-dashboard-tasks-001 | Task name empty | Save without name | minor | FR-dashboard-tasks-005 | TBD | Form stays | Enter name |
| E-dashboard-tasks-002 | No action required | No pending items | minor | FR-dashboard-tasks-009 | TBD | Empty list | — |
| E-dashboard-tasks-003 | No tasks | Project has no tasks | minor | FR-dashboard-tasks-004 | TBD | Empty table | Add task |

## 7. Success Criteria

| ID | Business outcome | Measured by | Target |
|----|------------------|-------------|--------|
| SC-dashboard-tasks-01 | Leap Up sees all project progress in one place | Demo at Phase 2 | All active projects shown |

## 8. Data Entities (summary)

- **Task:** project, name, owner, due date, status.
- **Action item:** title, project, area, description, due date-time, target screen (source TBD).

## 9. Flows (summary)

Dashboard → Review Now → target · Update Task List → add/update task.

## 10. Screens (summary)

| Screen | Board |
|---|---|
| Home (Dashboard / Project Management / Update Task List / Action Required) | 02 (L8–L231) |
| Project — Task List tab | 03 tab L33 (content not drawn; same table assumed) |

## 11. Constraints, Dependencies & Assumptions

| Dependency | Owner | Blocks if not ready |
|------------|-------|---------------------|
| Video rounds / approvals produce review items | `video-review`, `outcome-approval` | Action Required content |

## 12. Open Questions

- [ ] OQ-1: Stat and progress calculation.
- [ ] OQ-2: Owner values.
- [ ] OQ-3: Action Required sources and Review Now targets.
- [ ] OQ-4: Home for clients.
- [ ] OQ-5 (C2): Realtime vs daily update.
- [ ] OQ-6: Status transitions.
- [ ] OQ-7: Client task rights.
- [ ] OQ-8: Add/edit/delete task controls.
- [ ] OQ-9: Wording E-dashboard-tasks-001…003.
