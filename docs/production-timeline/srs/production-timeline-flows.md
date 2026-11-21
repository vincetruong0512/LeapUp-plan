---
type: srs-flows
feature: production-timeline
updated: 2026-11-22
---

# Production Timeline — Flows

## Flow: Follow the production timeline (Sequence)

**Trigger**: Client opens the project timeline.
**Related UC**: [UC-production-timeline-01](../usecases/uc-follow-the-production-timeline.md)
**Related FR**: FR-production-timeline-001, FR-production-timeline-002, FR-production-timeline-003, FR-production-timeline-004, FR-production-timeline-005, FR-production-timeline-009
**Related E**: E-production-timeline-001

```mermaid
sequenceDiagram
    actor Client
    participant Portal
    Client->>Portal: Open Proposal / Production Timeline (entry TBD)
    Portal-->>Client: Header and 5 stage cards - number, status, name, date range
    alt Project has milestones
        Portal-->>Client: Milestones - MILESTONE, OWNER, DUE, STATUS
    else No milestones
        Portal-->>Client: Empty table - E-production-timeline-001
    end
```

## Flow: Maintain stages and milestones (Activity)

**Trigger**: Leap Up member opens the timeline to update it.
**Related UC**: [UC-production-timeline-02](../usecases/uc-maintain-the-production-timeline.md)
**Related FR**: FR-production-timeline-003, FR-production-timeline-005, FR-production-timeline-006
**Related E**: —

```mermaid
flowchart TB
    s(["Start"]) --> a1["Open the timeline"]
    a1 --> d1{"What changes?"}
    d1 -->|"Stage"| a2["Change stage dates or status (controls TBD)"]
    d1 -->|"Milestone"| a3["Add or change milestone: name, owner, due, status"]
    a2 --> ok["Updated timeline shown to all project members"]
    a3 --> ok
    ok --> Stop(["End"])
    class ok happy
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
```

## Flow: Provide missing client inputs (OPEN C6) (Activity)

**Trigger**: Client sees a Missing input.
**Related UC**: [UC-production-timeline-03](../usecases/uc-provide-client-inputs.md)
**Related FR**: FR-production-timeline-007, FR-production-timeline-008
**Related E**: E-production-timeline-002

```mermaid
flowchart TB
    s(["Start"]) --> a1["Open the timeline"]
    a1 --> a2["Show Client Inputs Received or Missing and FEEDBACK RULE (OPEN C6)"]
    a2 --> a3["Upload inputs for a Missing item"]
    a3 --> d1{"Upload OK?"}
    d1 -->|"Yes"| ok["Item shows Received"]
    d1 -->|"No"| e1["Show E-production-timeline-002, item stays Missing"]
    e1 --> a3
    ok --> Stop(["End"])
    class ok happy
    class e1 error
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
```
