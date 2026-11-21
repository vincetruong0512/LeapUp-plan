# Use Case: UC-video-review-02 Resolve comments and log the round's changes

> Scope: Leap Up Client Project Portal — video-review · Level: sea (user goal)

## Primary Actor

Leap Up member

## Trigger

Leap Up works through the feedback of a round.

## Preconditions

- The round has Open comments.

## Guarantees

- **Minimal Guarantee:** Comment statuses and the change log stay as they were if nothing is saved.
- **Success Guarantee:** Handled comments show "Resolved" to all project members, and the Round Change Log shows what changed in the round and its status line.

## Main Success Scenario

1. Leap Up member opens Video Review of the round.
2. Member reads the Open comments.
3. An allowed user marks a handled comment Resolved (who may resolve TBD).
4. Portal shows the comment as "Resolved" to all project members.
5. Member records what changed in the round (editing method TBD).
6. Portal shows the change and the status line under the round in the Round Change Log.

## Extensions

None in the spec.

## Related Requirements

- FR: [FR-video-review-009](../srs/video-review-spec.md#3-functional-requirements-fr), [FR-video-review-012](../srs/video-review-spec.md#3-functional-requirements-fr)
- BR: BR-video-review-002
- Errors: —
- Stories: US-003, US-005 · Diagram: [Resolve comments and log the round's changes (Activity)](../srs/video-review-flows.md)
