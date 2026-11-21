---
type: srs-userflow
feature: admin
updated: 2026-11-22
primary_device: desktop
stage: flow-approved
flow_approved_at: 2026-11-22
flow_hash: "9278efe7"
---

# admin — User Flow

Screens are not on the board (C3); names below are placeholders for flow tracing only, not designs.

## 1. User Flow (overall)

```mermaid
flowchart TD
    n1["[1] Admin page (TBD design)"]
    n2["[2] Create project form"]
    d1{"Required fields filled?"}
    n3["[3] Create client account form"]
    d2{"User ID unique?"}
    n4["[4] Assign members"]
    n5["[5] Form error state"]
    n1 -->|"Create project"| n2
    n2 -->|"Save"| d1
    d1 -->|"Yes"| n4
    d1 -->|"No - E-admin-001"| n5
    n1 -->|"Create client account"| n3
    n3 -->|"Save"| d2
    d2 -->|"Yes"| n4
    d2 -->|"No - E-admin-002"| n5
    n5 -.->|"Fix and retry"| n1
    n4 -->|"Done"| n1
    class n1,n2,n3,n4 happy
    class n5 error
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
    classDef edge fill:#fff3cd,stroke:#ffc107
```

## 2. Screens

| [#] | Slug | Screen | Purpose | Flow | Board |
|-----|------|--------|---------|------|-------|
| 1 | admin-home | Admin page | Entry to admin tasks | setup | none (C3) |
| 2 | project-form | Create project | Project details | setup | none |
| 3 | account-form | Create client account | User ID + password | setup | none |
| 4 | members | Assign members | Add users with role Leap Up / Client | setup | none |
| 5 | form-error | Form error state | E-admin-001 / 002 | setup | none |

## 3. Flows

| Flow-slug | Flow name | Screens | Cases covered |
|-----------|-----------|---------|---------------|
| setup | Set up a project and its access | 1–5 | happy 1→2→4, 1→3→4 · error 5 |

## 3.5. Transitions

| From [#] | To [#] | Trigger | Condition |
|----------|--------|---------|-----------|
| 1 | 2 | Create project | Admin |
| 2 | 4 | Save | Required fields filled |
| 1 | 3 | Create client account | Admin |
| 3 | 4 | Save | User ID unique |
| 2, 3 | 5 | Save | Validation fails |
| 4 | 1 | Done | — |

## 4. Open Questions

- [ ] OQ-1 (C3): All admin screens need a design before `/wireframe-html` can draw them.
