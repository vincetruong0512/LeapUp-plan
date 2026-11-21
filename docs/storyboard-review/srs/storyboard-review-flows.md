---
type: srs-flows
feature: storyboard-review
updated: 2026-11-22
---

# Storyboard Review — Flows

## Flow: Review storyboard shots (OUT) (Activity)

**Trigger**: Client opens a storyboard version in Client Review.
**Related UC**: [UC-storyboard-review-01](../usecases/uc-review-storyboard-shots.md)
**Related FR**: FR-storyboard-review-001, FR-storyboard-review-002, FR-storyboard-review-003, FR-storyboard-review-004, FR-storyboard-review-005, FR-storyboard-review-006, FR-storyboard-review-007, FR-storyboard-review-008, FR-storyboard-review-011, FR-storyboard-review-012
**Related E**: E-storyboard-review-002

```mermaid
flowchart TB
    s(["Start"]) --> a1["Open Material / Storyboard Review"]
    a1 --> a2["Show version, feedback due, tabs, counts, frames"]
    a2 --> d1{"Action on a frame?"}
    d1 -->|"Approve"| ok1["Frame Approved, counts updated"]
    d1 -->|"Comment"| a3["Write comment"]
    a3 --> d2{"Comment text entered?"}
    d2 -->|"No"| e1["Show E-storyboard-review-002"]
    e1 --> a3
    d2 -->|"Yes"| ok2["Comment recorded on the frame (status effect TBD)"]
    ok1 --> d3{"More frames to review?"}
    ok2 --> d3
    d3 -->|"Yes"| d1
    d3 -->|"No"| Stop(["End"])
    class ok1,ok2 happy
    class e1 error
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
```

## Flow: Approve and lock the storyboard (OUT) (Activity)

**Trigger**: Client presses "Approve storyboard".
**Related UC**: [UC-storyboard-review-02](../usecases/uc-approve-and-lock-the-storyboard.md)
**Related FR**: FR-storyboard-review-009, FR-storyboard-review-010
**Related E**: E-storyboard-review-001, E-storyboard-review-003, E-storyboard-review-004

```mermaid
flowchart TB
    subgraph C["Client"]
        s(["Start"]) --> a1["Press Approve storyboard"]
    end
    subgraph P["Portal"]
        d1{"User may approve? (C4)"}
        d2{"Frames settled? (rule TBD)"}
        e1["Approve nothing, show E-storyboard-review-004"]
        e2["Approve nothing, show E-storyboard-review-001"]
        ok["Approve version, record who and when, lock script, shots and VO"]
        d3{"Change needed later?"}
        a2["Locked version unchanged E-storyboard-review-003, start new revision"]
    end
    a1 --> d1
    d1 -->|"No"| e1
    d1 -->|"Yes"| d2
    d2 -->|"No"| e2
    d2 -->|"Yes"| ok
    ok --> d3
    d3 -->|"Yes"| a2
    d3 -->|"No"| Stop(["End"])
    a2 --> Stop
    e1 --> Stop
    e2 --> Stop
    class ok happy
    class e1,e2 error
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
```
