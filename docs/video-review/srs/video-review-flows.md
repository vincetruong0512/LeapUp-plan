---
type: srs-flows
feature: video-review
updated: 2026-11-22
---

# Video Review — Flows

## Flow: Review a round with timecoded comments (Sequence)

**Trigger**: Client opens Video Review for the current round.
**Related UC**: [UC-video-review-01](../usecases/uc-review-a-round-with-timecoded-comments.md)
**Related FR**: FR-video-review-001, FR-video-review-002, FR-video-review-003, FR-video-review-004, FR-video-review-005, FR-video-review-006, FR-video-review-007, FR-video-review-008, FR-video-review-013, FR-video-review-014, FR-video-review-015
**Related E**: E-video-review-001, E-video-review-002, E-video-review-003, E-video-review-004

```mermaid
sequenceDiagram
    actor Client
    participant Portal
    participant R2 as Cloudflare R2
    Client->>Portal: Open Video Review (entry TBD)
    alt Not a member of the project
        Portal-->>Client: Refuse access - E-auth-access-003
    else Member
        Portal-->>Client: Header, Version History, video, timecode comments, Round Change Log
        opt Round has no video yet
            Portal-->>Client: E-video-review-004
        end
        Client->>Portal: Play the video
        Portal->>R2: Get the round's video
        alt Video plays
            R2-->>Portal: Video
            Portal-->>Client: Video plays with time, volume, fullscreen
            Client->>Portal: Pause at mm:ss and submit comment text
            alt Text entered
                Portal->>Portal: Save comment as Open with timecode, round, author side
                Portal-->>Client: Comment listed, marker at mm:ss, count updated
            else Empty text
                Portal-->>Client: Nothing saved - E-video-review-001
            end
        else Playback fails
            R2-->>Portal: Failure
            Portal-->>Client: E-video-review-002
        end
    end
```

## Flow: Resolve comments and log the round's changes (Activity)

**Trigger**: Leap Up member opens the round to handle feedback.
**Related UC**: [UC-video-review-02](../usecases/uc-resolve-comments-and-log-changes.md)
**Related FR**: FR-video-review-009, FR-video-review-012
**Related E**: —

```mermaid
flowchart TB
    s(["Start"]) --> a1["Open Video Review of the round"]
    a1 --> a2["Read the Open comments"]
    a2 --> d1{"Comment handled?"}
    d1 -->|"Yes"| a3["Allowed user marks it Resolved (who TBD)"]
    a3 --> a4["Resolved shown to all project members"]
    d1 -->|"No"| a5["Comment stays Open"]
    a4 --> d2{"More Open comments to handle?"}
    a5 --> d2
    d2 -->|"Yes"| a2
    d2 -->|"No"| a6["Record what changed in the Round Change Log (method TBD)"]
    a6 --> ok["Change and status line shown under the round"]
    ok --> Stop(["End"])
    class ok happy
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
```

## Flow: Add a new version and start the next round (Activity)

**Trigger**: Leap Up has a new version after feedback.
**Related UC**: [UC-video-review-03](../usecases/uc-start-the-next-round.md)
**Related FR**: FR-video-review-003, FR-video-review-010, FR-video-review-011, FR-video-review-013
**Related E**: E-video-review-004

```mermaid
flowchart TB
    s(["Start"]) --> a1["Leap Up provides the new version or starts the next round (mechanism TBD)"]
    a1 --> a2["Record the version in the round"]
    a2 --> a3["Move round statuses Upcoming, In Review, Reviewed (triggers TBD)"]
    a3 --> ok["Version History shows rounds with status and date"]
    ok --> Stop(["End"])
    class ok happy
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
```
