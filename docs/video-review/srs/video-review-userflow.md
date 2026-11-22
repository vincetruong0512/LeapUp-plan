---
type: srs-userflow
feature: video-review
updated: 2026-11-22
primary_device: desktop
stage: revised-after-review
flow_approved_at: 2026-11-22
flow_hash: "f1978c00"
---

# video-review — User Flow

Revised 2026-11-22 after the MVP review ([review-2026-11-22-mvp.md](../../portal/review-2026-11-22-mvp.md), R-01, R-03,
R-06): access gate, exit via breadcrumb / sidebar, a selected round goes through the "has a video?" check, empty-comment
and no-comments states, resolve permission kept TBD, change-log and marker-click nodes. Needs re-approval.

## 1. User Flow (overall)

```mermaid
flowchart TD
    n0["From project-files: Open video, or sidebar Outcome Review"]
    d0{"Assigned to project?"}
    x0["auth-access: Not assigned - E-auth-access-003"]
    d1{"Round has a video?"}
    n1["[1] Video Review - current round (board 07)"]
    n2["[2] No video yet - E-video-review-004"]
    d2{"Video plays?"}
    n3["[3] Playback error - E-video-review-002"]
    d4{"Round has comments?"}
    n7["[4] No comments yet - E-video-review-003"]
    d3{"Comment text entered?"}
    n8["[5] Empty comment - E-video-review-001"]
    n4["Comment saved as Open + marker"]
    d5{"May resolve? TBD OQ-2"}
    n5["Comment marked Resolved"]
    n9["Resolve not available"]
    n6["Select another round - provisional OQ-6"]
    n10["Click marker or time chip - seek, inferred OQ-6"]
    n11["Read round change log"]
    x1["Go to project-files: Project Files"]
    n0 --> d0
    d0 -->|"Yes"| d1
    d0 -->|"No"| x0
    d1 -->|"Yes"| n1
    d1 -->|"No"| n2
    n1 -->|"Play"| d2
    d2 -->|"Yes"| n1
    d2 -->|"No"| n3
    n3 -.->|"Retry"| d2
    n1 -->|"Show comments"| d4
    d4 -->|"Yes"| n1
    d4 -->|"No"| n7
    n7 -->|"Add a comment"| d3
    n1 -->|"Add comment at time"| d3
    d3 -->|"Yes"| n4
    d3 -->|"No"| n8
    n8 -.->|"Type text"| d3
    n4 -->|"Back to list"| n1
    n1 -->|"Resolve comment"| d5
    d5 -->|"Yes"| n5
    d5 -->|"No"| n9
    n5 -->|"Status updated"| n1
    n9 --> n1
    n1 -->|"Version History"| n6
    n2 -.->|"Select another round"| n6
    n6 -->|"Show that round"| d1
    n1 -.->|"Marker"| n10
    n10 --> n1
    n1 -.->|"Change log"| n11
    n11 --> n1
    n1 -->|"Breadcrumb or sidebar"| x1
    n2 -->|"Breadcrumb or sidebar"| x1
    class n1,n4,n5,n6,n10,n11,x1 happy
    class n3,n8,x0 error
    class n0,n2,n7,n9 edge
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
    classDef edge fill:#fff3cd,stroke:#ffc107
```

No flow yet (TBD, not silently dropped): FR-video-review-010 new version / next round (OQ-3 — no control on board 07),
FR-video-review-011 round status triggers (OQ-4), FR-video-review-012 who records the change log (OQ-5). Commenting on a
past round, an Upcoming round or a replaced version: TBD (OQ-11). Others' changes without realtime: TBD (OQ-14).

## 2. Screens

| [#] | Slug | Screen | Purpose | Flow | Board |
|-----|------|--------|---------|------|-------|
| 1 | video-review | Video Review | Player, markers, comments, rounds, log | review | 07, L10–L193 |
| 2 | video-review-no-video | No video in round | E-video-review-004; Upcoming round, no player | review | not drawn |
| 3 | video-review-error | Playback error | E-video-review-002; Retry | review | not drawn |
| 4 | video-review-no-comments | No comments yet | E-video-review-003; Add a comment | review | not drawn |
| 5 | video-review-empty-comment | Empty comment | E-video-review-001; input stays | review | not drawn |

## 3. Flows

| Flow-slug | Flow name | Screens | Cases covered |
|-----------|-----------|---------|---------------|
| review | Review a round with timecoded comments | 1–5 | happy 1 (comment, resolve, switch round, marker, change log, exit) · edge 2, 4, resolve not available · error 3, 5, not assigned |

## 3.5. Transitions

| From [#] | To [#] | Trigger | Condition |
|----------|--------|---------|-----------|
| entry | 1 | Open review | Member of project, round has a video |
| entry | auth-access [5] | Open review / link | Not a member (E-auth-access-003) |
| entry | 2 | Open review | No video yet |
| 1 | 3 | Play | Video fails |
| 3 | 1 | Retry | Plays |
| 1 | 4 | Show comments | Round has no comments |
| 1, 4 | 1 | Add comment | Text entered → Open comment + marker |
| 1, 4 | 5 | Add comment | Empty text |
| 1 | 1 | Resolve | Allowed role (OQ-2); otherwise "not available" |
| 1, 2 | 1 or 2 | Select round | Version History (provisional, OQ-6) → has a video? |
| 1, 2 | project-files [1] | Breadcrumb / sidebar | — (board L10, L23–L51) |

## 4. Open Questions

- [ ] OQ-1: Upload of a new version/round — no control on board 07 (spec OQ-3).
- [ ] OQ-2: Who may resolve (spec OQ-2).
- [ ] OQ-3: Comments on past / no-video rounds (spec OQ-11).
- [ ] OQ-4: Phone layout (spec OQ-8).
