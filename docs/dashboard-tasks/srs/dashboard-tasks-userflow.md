---
type: srs-userflow
feature: dashboard-tasks
updated: 2026-11-22
primary_device: desktop
stage: flow-approved
flow_approved_at: 2026-11-22
flow_hash: "cd614d80"
---

# dashboard-tasks — User Flow

## 1. User Flow (overall)

```mermaid
flowchart TD
    n1["[1] Home - Dashboard (board 02)"]
    d1{"Action Required items?"}
    n2["[2] Home - no action required"]
    n3["Review screen (Video Review etc.)"]
    n4["[3] Update Task List by project"]
    n5["Add or update task (control TBD)"]
    d2{"Task name entered?"}
    n6["[4] Task form error"]
    n1 -->|"Load"| d1
    d1 -->|"Yes"| n1
    d1 -->|"No - E-dashboard-tasks-002"| n2
    n1 -->|"Review Now"| n3
    n1 -->|"Update Task List tab"| n4
    n2 -->|"Update Task List tab"| n4
    n4 -->|"Add task"| n5
    n5 -->|"Save"| d2
    d2 -->|"Yes"| n4
    d2 -->|"No - E-dashboard-tasks-001"| n6
    n6 -.->|"Fix"| n5
    n4 -.->|"Dashboard tab"| n1
    n3 -.->|"Back to Home"| n1
    class n1,n3,n4,n5 happy
    class n6 error
    class n2 edge
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
    classDef edge fill:#fff3cd,stroke:#ffc107
```

## 2. Screens

| [#] | Slug | Screen | Purpose | Flow | Board |
|-----|------|--------|---------|------|-------|
| 1 | home | Home — Dashboard, Project Management, Action Required | Overview | overview | 02, L8–L74, L194–L231 |
| 2 | home-empty | No action required | E-dashboard-tasks-002 | overview | not drawn |
| 3 | task-list | Update Task List / By Project | Task tables | tasks | 02, L82–L186 |
| 4 | task-error | Task form error | E-dashboard-tasks-001 | tasks | not drawn |

## 3. Flows

| Flow-slug | Flow name | Screens | Cases covered |
|-----------|-----------|---------|---------------|
| overview | Project overview and Action Required | 1, 2 | happy 1 · edge 2 |
| tasks | Manage tasks by project | 3, 4 | happy 3 · error 4 |

## 3.5. Transitions

| From [#] | To [#] | Trigger | Condition |
|----------|--------|---------|-----------|
| 1 | review | Review Now | Item target (OQ-3) |
| 1 | 3 | Update Task List tab | — |
| 3 | 3 | Save task | Name entered |
| 3 | 4 | Save task | Name empty |

## 4. Open Questions

- [ ] OQ-1: Task create/edit controls not drawn (spec OQ-8).
