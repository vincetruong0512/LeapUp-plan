---
type: srs-userflow
feature: email-notifications
updated: 2026-11-22
primary_device: desktop
stage: flow-approved
flow_approved_at: 2026-11-22
flow_hash: "28f039c7"
---

# email-notifications — User Flow

No portal screens: the flow shows the event-to-mail path. No wireframes (step 4 not applicable).

## 1. User Flow (overall)

```mermaid
flowchart TD
    e1["New video, comment or approval"]
    d1{"Recipient has an e-mail address?"}
    s1["Send e-mail"]
    d2{"Service accepted?"}
    ok["E-mail delivered"]
    skip["Skip recipient"]
    fail["Failure handling (TBD)"]
    e1 -->|"Project members"| d1
    d1 -->|"Yes"| s1
    d1 -->|"No - E-email-notifications-002"| skip
    s1 --> d2
    d2 -->|"Yes"| ok
    d2 -->|"No - E-email-notifications-001"| fail
    endN["End"]
    ok --> endN
    skip --> endN
    fail --> endN
    class e1,s1,ok happy
    class fail error
    class skip edge
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
    classDef edge fill:#fff3cd,stroke:#ffc107
```

## 2. Screens

None (e-mail only).

## 3. Flows

| Flow-slug | Flow name | Screens | Cases covered |
|-----------|-----------|---------|---------------|
| notify | Send notification e-mails | — | happy send · edge no address · error send failed |

## 3.5. Transitions

| From | To | Trigger | Condition |
|------|----|---------|-----------|
| event | send | Event | Recipient has address |
| send | failure | Service error | — |

## 4. Open Questions

- [ ] OQ-1: Link in the e-mail and where it lands (spec OQ-3).
