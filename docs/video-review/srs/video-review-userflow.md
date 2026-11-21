---
type: srs-userflow
feature: video-review
updated: 2026-11-22
primary_device: desktop
stage: flow-approved
flow_approved_at: 2026-11-22
flow_hash: "f1978c00"
---

# video-review — User Flow

## 1. User Flow (overall)

```mermaid
flowchart TD
    n0["Project Files or sidebar Outcome Review"]
    n1["[1] Video Review - current round (board 07)"]
    d1{"Round has a video?"}
    n2["[2] Video Review - no video yet"]
    d2{"Video plays?"}
    n3["[3] Video Review - playback error"]
    d3{"Comment text entered?"}
    n4["Comment saved as Open + marker"]
    n5["Mark Resolved (who TBD)"]
    n6["Select another round"]
    n0 -->|"Open review"| d1
    d1 -->|"Yes"| n1
    d1 -->|"No - E-video-review-004"| n2
    n1 -->|"Play"| d2
    d2 -->|"Yes"| n1
    d2 -->|"No - E-video-review-002"| n3
    n3 -.->|"Retry"| n1
    n1 -->|"Add comment at time"| d3
    d3 -->|"Yes"| n4
    d3 -->|"No - E-video-review-001"| n1
    n4 -->|"Back to list"| n1
    n1 -->|"Resolve comment"| n5
    n5 -->|"Status updated"| n1
    n1 -->|"Version History"| n6
    n6 -->|"Show that round"| n1
    n2 -.->|"Select another round"| n6
    class n0,n1,n4,n5,n6 happy
    class n3 error
    class n2 edge
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
    classDef edge fill:#fff3cd,stroke:#ffc107
```

## 2. Screens

| [#] | Slug | Screen | Purpose | Flow | Board |
|-----|------|--------|---------|------|-------|
| 1 | video-review | Video Review | Player, markers, comments, rounds, log | review | 07, L10–L193 |
| 2 | video-review-no-video | No video in round | E-video-review-004 | review | not drawn |
| 3 | video-review-error | Playback error | E-video-review-002 | review | not drawn |

## 3. Flows

| Flow-slug | Flow name | Screens | Cases covered |
|-----------|-----------|---------|---------------|
| review | Review a round with timecoded comments | 1, 2, 3 | happy 1 (comment, resolve, switch round) · edge 2 · error 3 |

## 3.5. Transitions

| From [#] | To [#] | Trigger | Condition |
|----------|--------|---------|-----------|
| entry | 1 | Open review | Round has a video |
| entry | 2 | Open review | No video yet |
| 1 | 3 | Play | Video fails |
| 1 | 1 | Add comment | Text entered → Open comment + marker |
| 1 | 1 | Resolve | Allowed role (OQ-2) |
| 1 | 1 | Select round | Version History |

## 4. Open Questions

- [ ] OQ-1: Upload of a new version/round — no control on board 07 (spec OQ-3).
