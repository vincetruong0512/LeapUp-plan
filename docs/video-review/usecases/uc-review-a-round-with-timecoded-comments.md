# Use Case: UC-video-review-01 Review a round with timecoded comments

> Scope: Leap Up Client Project Portal — video-review · Level: sea (user goal)

## Primary Actor

Client

## Trigger

A round's video is ready and the client opens Video Review (sidebar "Outcome Review" or a video in Outcome Development — entry TBD).

## Preconditions

- The client is signed in and is a member of the project.

## Guarantees

- **Minimal Guarantee:** No comment is saved without text; every saved comment has a timecode and a round (BR-video-review-001).
- **Success Guarantee:** Each submitted comment is saved as Open in the round, pinned to the second it was made, shown as a timeline marker, and the comment count is updated.

## Main Success Scenario

1. Client opens Video Review.
2. Portal shows the header, Version History with the current round highlighted, the round's video, the timecode comments and the Round Change Log.
3. Client plays the video.
4. Client pauses at a moment; the comment box reads "Add comment at {mm:ss}...".
5. Client writes and submits the comment.
6. Portal saves the comment as Open with the timecode, round and author side (Client).
7. Portal lists the comment, adds a marker at its timecode and updates "{n} comments | Round {n}".

## Extensions

**1a. The client is not a member of the project:**
- 1a1. Portal refuses access (E-auth-access-003).
- 1a2. Use case ends.

**2a. The round has no video yet:**
- 2a1. Portal shows E-video-review-004.
- 2a2. Client may select another round (extension *a).

**2b. The round has no comments yet:**
- 2b1. Portal shows E-video-review-003.
- 2b2. Continue at step 3.

**3a. The video cannot be played:**
- 3a1. Portal shows E-video-review-002.
- 3a2. Client retries at step 3.

**5a. The comment text is empty:**
- 5a1. Portal saves nothing and shows E-video-review-001.
- 5a2. Resume at step 5.

***a. Client selects another round in Version History:**
- *a1. Portal shows that round's video and comments (inferred, FR-video-review-013).
- *a2. Continue at step 3.

## Related Requirements

- FR: [FR-video-review-001](../srs/video-review-spec.md#3-functional-requirements-fr), [FR-video-review-002](../srs/video-review-spec.md#3-functional-requirements-fr), [FR-video-review-003](../srs/video-review-spec.md#3-functional-requirements-fr), [FR-video-review-004](../srs/video-review-spec.md#3-functional-requirements-fr), [FR-video-review-005](../srs/video-review-spec.md#3-functional-requirements-fr), [FR-video-review-006](../srs/video-review-spec.md#3-functional-requirements-fr), [FR-video-review-007](../srs/video-review-spec.md#3-functional-requirements-fr), [FR-video-review-008](../srs/video-review-spec.md#3-functional-requirements-fr), [FR-video-review-013](../srs/video-review-spec.md#3-functional-requirements-fr), [FR-video-review-014](../srs/video-review-spec.md#3-functional-requirements-fr), [FR-video-review-015](../srs/video-review-spec.md#3-functional-requirements-fr); FR-project-files-014 (open video from Outcome Development)
- BR: BR-video-review-001, BR-video-review-002, BR-video-review-004
- Errors: E-video-review-001, E-video-review-002, E-video-review-003, E-video-review-004 (wording in the spec Error Matrix — TBD)
- Stories: US-001, US-002 (and project-files US-005) · Diagram: [Review a round with timecoded comments (Sequence)](../srs/video-review-flows.md)
