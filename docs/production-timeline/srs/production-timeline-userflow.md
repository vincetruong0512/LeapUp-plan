---
type: srs-userflow
feature: production-timeline
updated: 2026-11-22
primary_device: desktop
stage: flow-approved
flow_approved_at: 2026-11-22
flow_hash: "d0bda710"
---

# production-timeline — User Flow

## 1. User Flow (overall)

```mermaid
flowchart TD
    n0["Project (entry TBD)"]
    n1["[1] Proposal / Production Timeline (board 04)"]
    n2["Edit stage or milestone (control TBD)"]
    n3["Upload inputs (OPEN C6)"]
    d1{"Upload OK?"}
    n4["[2] Upload inputs - error"]
    n0 -->|"Open timeline"| n1
    n1 -->|"Leap Up edits"| n2
    n2 -->|"Save"| n1
    n1 -->|"Upload inputs"| n3
    n3 -->|"Upload"| d1
    d1 -->|"Yes - item Received"| n1
    d1 -->|"No - E-production-timeline-002"| n4
    n4 -.->|"Retry"| n3
    class n0,n1,n2,n3 happy
    class n4 error
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
    classDef edge fill:#fff3cd,stroke:#ffc107
```

## 2. Screens

| [#] | Slug | Screen | Purpose | Flow | Board |
|-----|------|--------|---------|------|-------|
| 1 | timeline | Proposal / Production Timeline | Stages, milestones, inputs, rule | timeline | 04, L197–L350 |
| 2 | timeline-upload-error | Upload inputs error | E-production-timeline-002 | timeline | not drawn |

## 3. Flows

| Flow-slug | Flow name | Screens | Cases covered |
|-----------|-----------|---------|---------------|
| timeline | Follow and maintain the production timeline | 1, 2 | happy 1 · error 2 |

## 3.5. Transitions

| From [#] | To [#] | Trigger | Condition |
|----------|--------|---------|-----------|
| project | 1 | Open timeline | Member |
| 1 | 1 | Edit + save | Leap Up (OQ-2) |
| 1 | 1 | Upload inputs | Success (C6) |
| 1 | 2 | Upload inputs | Failure |

## 4. Open Questions

- [ ] OQ-1: Edit controls not drawn (spec OQ-2).
