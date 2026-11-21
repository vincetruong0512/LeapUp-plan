# Use Case: UC-video-review-03 Add a new version and start the next round

> Scope: Leap Up Client Project Portal — video-review · Level: sea (user goal)

## Primary Actor

Leap Up member

## Trigger

Leap Up has a new version of the video after feedback.

## Preconditions

- A round is In Review.

## Guarantees

- **Minimal Guarantee:** Round statuses stay as they were if the new version is not added.
- **Success Guarantee:** The new round is In Review with its video; the previous round is Reviewed; Version History shows each round with status and date.

## Main Success Scenario

1. Leap Up member provides the new version for the round or starts the next round (mechanism TBD).
2. Portal records the version in the round.
3. Portal moves the round statuses Upcoming → In Review → Reviewed (triggers TBD).
4. Portal shows Version History with each round's status and date and the current round highlighted.

## Extensions

**1a. An Upcoming round has no video yet:**
- 1a1. Viewers of that round see E-video-review-004.
- 1a2. Use case resumes at step 1 when the version is provided.

## Related Requirements

- FR: [FR-video-review-003](../srs/video-review-spec.md#3-functional-requirements-fr), [FR-video-review-010](../srs/video-review-spec.md#3-functional-requirements-fr), [FR-video-review-011](../srs/video-review-spec.md#3-functional-requirements-fr), [FR-video-review-013](../srs/video-review-spec.md#3-functional-requirements-fr)
- BR: BR-video-review-003
- Errors: E-video-review-004 (wording in the spec Error Matrix — TBD)
- Stories: US-004 · Diagram: [Add a new version and start the next round (Activity)](../srs/video-review-flows.md)
