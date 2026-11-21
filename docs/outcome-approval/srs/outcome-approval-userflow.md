---
type: srs-userflow
feature: outcome-approval
updated: 2026-11-22
primary_device: desktop
stage: flow-approved
flow_approved_at: 2026-11-22
flow_hash: "9a6255d5"
---

# outcome-approval — User Flow

## 1. User Flow (overall)

```mermaid
flowchart TD
    n0["Video Review - round awaiting approval"]
    n1["[1] Revision and Sign-off (board 08)"]
    d0{"User may approve?"}
    n2["Version approved - log entry"]
    n3["[2] Not allowed state"]
    d1{"All sign-off checks ticked?"}
    n4["Final sign-off approved - log entry"]
    n5["[3] Checklist incomplete state"]
    n6["Record or update change request"]
    n0 -->|"Approve version (control TBD)"| d0
    d0 -->|"Yes"| n2
    d0 -->|"No - E-outcome-approval-001"| n3
    n2 -->|"Open Revision and Sign-off"| n1
    n3 -.->|"Back"| n0
    n1 -->|"Approve final version"| d1
    d1 -->|"Yes"| n4
    d1 -->|"No - E-outcome-approval-002"| n5
    n5 -.->|"Tick items"| n1
    n4 -->|"Log updated"| n1
    n1 -->|"Change request"| n6
    n6 -->|"Save"| n1
    class n0,n1,n2,n4,n6 happy
    class n3,n5 error
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
    classDef edge fill:#fff3cd,stroke:#ffc107
```

## 2. Screens

| [#] | Slug | Screen | Purpose | Flow | Board |
|-----|------|--------|---------|------|-------|
| 1 | revision-signoff | Revision & Sign-off | Rounds, approvers, CRs, sign-off, log | approval | 08, L214–L365 |
| 2 | approval-not-allowed | Not allowed state | E-outcome-approval-001 | approval | not drawn |
| 3 | signoff-incomplete | Checklist incomplete state | E-outcome-approval-002 | approval | not drawn |

## 3. Flows

| Flow-slug | Flow name | Screens | Cases covered |
|-----------|-----------|---------|---------------|
| approval | Approve versions, track change requests, sign off | 1, 2, 3 | happy 1 · error 2, 3 |

## 3.5. Transitions

| From [#] | To [#] | Trigger | Condition |
|----------|--------|---------|-----------|
| video-review | log | Approve version | Allowed approver (OQ-2) |
| 1 | 1 | Approve final version | All checks ticked (C9) |
| 1 | 3 | Approve final version | Checks missing |
| 1 | 1 | Save change request | Rights TBD (OQ-3) |

## 4. Open Questions

- [ ] OQ-1: Version-approval control not drawn (spec OQ-1).
