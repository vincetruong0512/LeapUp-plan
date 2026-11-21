---
type: srs-userflow
feature: storyboard-review
updated: 2026-11-22
primary_device: desktop
stage: flow-approved
flow_approved_at: 2026-11-22
flow_hash: "76ce8052"
---

# storyboard-review — User Flow

## 1. User Flow (overall)

```mermaid
flowchart TD
    n0["Project Material area"]
    n1["[1] Storyboard Review - Storyboard tab (board 06)"]
    n2["Approve frame - status Approved"]
    n3["[2] Comment on frame (TBD)"]
    d1{"Comment text entered?"}
    d2{"Frames settled? (rule TBD)"}
    d3{"User may approve? (C4)"}
    n4["[3] Storyboard approved - locked"]
    n5["[4] Approve storyboard - error state"]
    n6["New revision (version + 1)"]
    n0 -->|"Open"| n1
    n1 -->|"Approve on a frame"| n2
    n2 -->|"Counts updated"| n1
    n1 -->|"Comment on a frame"| n3
    n3 -->|"Save"| d1
    d1 -->|"Yes"| n1
    d1 -->|"No - E-storyboard-review-002"| n3
    n1 -->|"Approve storyboard"| d3
    d3 -->|"No - E-storyboard-review-004"| n5
    d3 -->|"Yes"| d2
    d2 -->|"No - E-storyboard-review-001"| n5
    d2 -->|"Yes"| n4
    n5 -.->|"Back"| n1
    n4 -->|"Later change - E-storyboard-review-003"| n6
    n6 -->|"New version to review"| n1
    class n0,n1,n2,n3,n4,n6 happy
    class n5 error
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
    classDef edge fill:#fff3cd,stroke:#ffc107
```

## 2. Screens

| [#] | Slug | Screen | Purpose | Flow | Board |
|-----|------|--------|---------|------|-------|
| 1 | storyboard | Storyboard Review — Storyboard tab | Version, counts, frames, lock notice | storyboard | 06, L425–L479 |
| 2 | frame-comment | Comment on a frame | Frame feedback | storyboard | button only (L456) |
| 3 | storyboard-approved | Storyboard approved (locked) | After Approve storyboard | storyboard | not drawn |
| 4 | storyboard-approve-error | Approve storyboard — error | E-storyboard-review-001 / 004 | storyboard | not drawn |

## 3. Flows

| Flow-slug | Flow name | Screens | Cases covered |
|-----------|-----------|---------|---------------|
| storyboard | Review and approve a storyboard version | 1–4 | happy 1→3 · error 4 · new revision |

## 3.5. Transitions

| From [#] | To [#] | Trigger | Condition |
|----------|--------|---------|-----------|
| entry | 1 | Open | Member |
| 1 | 1 | Approve frame | — |
| 1 | 2 | Comment | — |
| 1 | 3 | Approve storyboard | Allowed, frames settled (rule TBD) |
| 1 | 4 | Approve storyboard | Not allowed or frames not settled |
| 3 | 1 | Later change | New revision |

## 4. Open Questions

- [ ] OQ-1: Script and Voice & Music tabs not drawn (spec OQ-2).
