---
type: srs-flows
feature: dashboard-tasks
updated: 2026-11-22
---

# Dashboard & Task List — Flows

## Flow: Check the overview and act on Action Required (Activity)

**Trigger**: User opens Dashboard.
**Related UC**: [UC-dashboard-tasks-01](../usecases/uc-check-overview-and-act.md)
**Related FR**: FR-dashboard-tasks-001, FR-dashboard-tasks-002, FR-dashboard-tasks-003, FR-dashboard-tasks-004, FR-dashboard-tasks-009, FR-dashboard-tasks-010, FR-dashboard-tasks-011
**Related E**: E-dashboard-tasks-002

```mermaid
flowchart TB
    s(["Start"]) --> a1["User opens Dashboard"]
    a1 --> a2["Show stat cards, project cards, task tables (assigned projects only)"]
    a2 --> d1{"Items awaiting review?"}
    d1 -->|"No"| e1["Action Required empty E-dashboard-tasks-002"]
    d1 -->|"Yes"| a3["Show Action Required with n Pending Reviews"]
    a3 --> a4["User presses Review Now"]
    a4 --> ok["Open the item's review screen (targets TBD)"]
    ok --> Stop(["End"])
    e1 --> Stop
    class ok happy
    class e1 error
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
```

## Flow: Manage a project's tasks (Activity)

**Trigger**: Member opens Update Task List.
**Related UC**: [UC-dashboard-tasks-02](../usecases/uc-manage-project-tasks.md)
**Related FR**: FR-dashboard-tasks-004, FR-dashboard-tasks-005, FR-dashboard-tasks-006, FR-dashboard-tasks-007, FR-dashboard-tasks-008
**Related E**: E-dashboard-tasks-001, E-dashboard-tasks-003

```mermaid
flowchart TB
    s(["Start"]) --> a1["Open Update Task List or project Task List tab"]
    a1 --> d0{"Project has tasks?"}
    d0 -->|"No"| e0["Empty table E-dashboard-tasks-003"]
    d0 -->|"Yes"| a2["Show TASK, OWNER, DUE, STATUS"]
    e0 --> a3
    a2 --> a3["Create task: name, owner, due date, status (controls TBD)"]
    a3 --> d1{"Task name entered?"}
    d1 -->|"No"| e1["Show E-dashboard-tasks-001"]
    e1 --> a3
    d1 -->|"Yes"| a4["Add the task to the project table"]
    a4 --> a5["Update status: To Do, In Progress, Pending Review, Completed"]
    a5 --> ok["New status shown on next page load (no realtime)"]
    ok --> Stop(["End"])
    class ok happy
    class e0,e1 error
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
```
