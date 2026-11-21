---
type: srs-userflow
feature: material-library
updated: 2026-11-22
primary_device: desktop
stage: flow-approved
flow_approved_at: 2026-11-22
flow_hash: "0c50ac19"
---

# material-library — User Flow

## 1. User Flow (overall)

```mermaid
flowchart TD
    n0["Project Material area or Action Required Review Now"]
    n1["[1] Material Library - category option review (board 05)"]
    d1{"Category has options?"}
    n2["[2] Material Library - no options"]
    n3["[3] Details / Feedback (TBD)"]
    d2{"Feedback text entered?"}
    n4["Select Option X - becomes Selected"]
    n5["Submit for approval"]
    d3{"An option selected?"}
    n6["[4] Submit - error state"]
    n7["[5] Approval Summary (TBD)"]
    n0 -->|"Open"| n1
    n1 -->|"Choose category"| d1
    d1 -->|"Yes"| n1
    d1 -->|"No - E-material-library-001"| n2
    n2 -.->|"Choose another category"| n1
    n1 -->|"Details / Feedback"| n3
    n3 -->|"Save"| d2
    d2 -->|"Yes"| n1
    d2 -->|"No - E-material-library-002"| n3
    n1 -->|"Select Option X"| n4
    n4 -->|"Back to cards"| n1
    n1 -->|"Submit for approval"| d3
    d3 -->|"Yes"| n5
    d3 -->|"No - E-material-library-004"| n6
    n6 -.->|"Select an option"| n1
    n5 -->|"Workflow to Approved"| n1
    n1 -->|"Approval Summary"| n7
    n7 -.->|"Back"| n1
    class n0,n1,n3,n4,n5,n7 happy
    class n6 error
    class n2 edge
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
    classDef edge fill:#fff3cd,stroke:#ffc107
```

## 2. Screens

| [#] | Slug | Screen | Purpose | Flow | Board |
|-----|------|--------|---------|------|-------|
| 1 | material-library | Material Library | Categories, option cards, review guide, workflow | options | 05, L366–L424 |
| 2 | material-library-empty | No options | E-material-library-001 | options | not drawn |
| 3 | option-feedback | Details / Feedback | Feedback per option | options | link only (L394) |
| 4 | submit-error | Submit — error | E-material-library-004 | options | not drawn |
| 5 | approval-summary | Approval Summary | Summary (TBD) | options | button only (L370) |

## 3. Flows

| Flow-slug | Flow name | Screens | Cases covered |
|-----------|-----------|---------|---------------|
| options | Review material options and choose a direction | 1–5 | happy 1→3→1, select, submit · edge 2 · error 4 |

## 3.5. Transitions

| From [#] | To [#] | Trigger | Condition |
|----------|--------|---------|-----------|
| entry | 1 | Open | Member |
| 1 | 2 | Choose category | No options |
| 1 | 3 | Details / Feedback | — |
| 3 | 1 | Save | Text entered |
| 1 | 1 | Select Option X | — |
| 1 | 4 | Submit for approval | Nothing selected |
| 1 | 5 | Approval Summary | — |

## 4. Open Questions

- [ ] OQ-1: Details / Feedback and Approval Summary screens are not drawn (spec OQ-4, OQ-6).
