---
type: srs-userflow
feature: admin
updated: 2026-11-22
primary_device: desktop
stage: revised-after-review
flow_approved_at: 2026-11-22
flow_hash: "9278efe7"
---

# admin — User Flow

Screens are not on the board (C3); names below are placeholders for flow tracing only, not designs.

Revised 2026-11-22 after the MVP review ([review-2026-11-22-mvp.md](../../portal/review-2026-11-22-mvp.md), R-01, R-05):
not-an-admin gate, Cancel on every form, errors return to the failing form, the three actions are independent (order TBD,
OQ-11), folders created on save, off-system hand-over of login details. Needs re-approval.

## 1. User Flow (overall)

```mermaid
flowchart TD
    e0["From auth-access: Landing - Admin pages"]
    d0{"Admin?"}
    n0["Not an Admin - E-admin-003"]
    n1["[1] Admin page (TBD design)"]
    n2["[2] Create project form"]
    d1{"Required fields filled?"}
    s1["Project created: Proposal, Material, Outcome Development folders; initial status TBD"]
    n3["[3] Create client account form"]
    d2{"User ID unique?"}
    s2["Account created"]
    n4["[4] Assign members"]
    d3{"Assignment valid?"}
    n5a["[5] Project form - error E-admin-001"]
    n5b["[6] Account form - error E-admin-001 or E-admin-002"]
    n6["Assignment error - TBD (OQ-10)"]
    h1["Hand over User ID and password outside the portal"]
    x1["Go to auth-access: Login - client signs in"]
    e0 --> d0
    d0 -->|"Yes"| n1
    d0 -->|"No"| n0
    n0 -->|"Back to my projects"| e0
    n1 -->|"Create project"| n2
    n2 -->|"Save"| d1
    n2 -->|"Cancel"| n1
    d1 -->|"Yes"| s1
    d1 -->|"No"| n5a
    n5a -.->|"Fix and save"| n2
    s1 -->|"Back"| n1
    n1 -->|"Create client account"| n3
    n3 -->|"Save"| d2
    n3 -->|"Cancel"| n1
    d2 -->|"Yes"| s2
    d2 -->|"No"| n5b
    n5b -.->|"Fix and save"| n3
    s2 -->|"Back"| n1
    n1 -->|"Assign members - choose project"| n4
    n4 -->|"Save"| d3
    n4 -->|"Cancel"| n1
    d3 -->|"Yes"| h1
    d3 -->|"No - TBD"| n6
    n6 -.->|"Fix"| n4
    h1 -.->|"Off-system"| x1
    h1 --> n1
    class n1,n2,n3,n4,s1,s2,h1,x1 happy
    class n0,n5a,n5b,n6 error
    class e0 edge
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
    classDef edge fill:#fff3cd,stroke:#ffc107
```

Order of the three actions: not set by the quote or board; drawn as independent actions from the admin page
(OQ-11). Proposal PR3 (one wizard) is undecided. Password reset (BR-auth-access-004) and remove member / deactivate
(OQ-5, OQ-6) have no flow until Leap Up answers.

## 2. Screens

| [#] | Slug | Screen | Purpose | Flow | Board |
|-----|------|--------|---------|------|-------|
| 1 | admin-home | Admin page | Entry to admin tasks | setup | none (C3) |
| 2 | project-form | Create project | Project details (fields TBD, OQ-3) | setup | none |
| 3 | account-form | Create client account | User ID + password | setup | none |
| 4 | members | Assign members | Choose project, add users with role Leap Up / Client | setup | none |
| 5 | project-form-error | Project form — error | E-admin-001 | setup | none |
| 6 | account-form-error | Account form — error | E-admin-001 / 002 | setup | none |
| — | not-admin | Not an Admin | E-admin-003 (shares the auth-access refusal state) | setup | none |

## 3. Flows

| Flow-slug | Flow name | Screens | Cases covered |
|-----------|-----------|---------|---------------|
| setup | Set up a project and its access | 1–6 | happy 1→2→1, 1→3→1, 1→4→hand-over · error 5, 6, not-admin, assignment error (TBD) · cancel on 2, 3, 4 |

## 3.5. Transitions

| From [#] | To [#] | Trigger | Condition |
|----------|--------|---------|-----------|
| auth-access landing | 1 | Admin pages | Admin; otherwise E-admin-003 |
| 1 | 2 | Create project | — |
| 2 | 1 | Save | Required fields filled; folders created; initial status TBD |
| 2 | 5 | Save | Required field empty (E-admin-001) |
| 5 | 2 | Fix and save | Input kept (TBD) |
| 1 | 3 | Create client account | — |
| 3 | 1 | Save | User ID unique |
| 3 | 6 | Save | Field empty (E-admin-001) or User ID taken (E-admin-002) |
| 6 | 3 | Fix and save | — |
| 1 | 4 | Assign members | Project chosen in the form |
| 4 | hand-over | Save | Assignment valid |
| 4 | assignment error | Save | TBD (OQ-10) |
| 2, 3, 4 | 1 | Cancel | Nothing saved |
| hand-over | auth-access [1] | Client signs in | Outside the portal |

## 4. Open Questions

- [ ] OQ-1 (C3): All admin screens need a design before `/wireframe-html` can draw them.
- [ ] OQ-2: Order of actions and admin entry point (spec OQ-11).
- [ ] OQ-3: Assignment error branch (spec OQ-10).
- [ ] OQ-4: Password reset, remove member, deactivate — no flow yet (spec OQ-5, OQ-6).
