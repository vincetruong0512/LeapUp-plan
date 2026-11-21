# Use Case: UC-storyboard-review-01 Review storyboard shots (OUT)

> Scope: Leap Up Client Project Portal — storyboard-review · Level: sea (user goal)

## Primary Actor

Client

## Trigger

A storyboard version is in Client Review ("Version 2 · Client Review | Feedback due 21 Nov, 17:00", L429).

## Preconditions

- The client is signed in and is a member of the project.
- OUT: change request needed.

## Guarantees

- **Minimal Guarantee:** A comment without text is not saved.
- **Success Guarantee:** Each reviewed frame shows Approved, or has the client's comment recorded; the counts reflect the frame statuses.

## Main Success Scenario

1. Client opens Material / Storyboard Review.
2. Portal shows the version, status and feedback due, the tabs (Script / Storyboard / Voice & Music), the count tiles and the frames.
3. Client presses Approve on a frame.
4. Portal shows the frame as Approved and updates the counts.
5. Client presses Comment on another frame and saves a comment.
6. Portal records the comment on the frame (status effect TBD).

## Extensions

**5a. The comment text is empty:**
- 5a1. Portal saves nothing and shows E-storyboard-review-002.
- 5a2. Resume at step 5.

## Related Requirements

- FR: [FR-storyboard-review-001](../srs/storyboard-review-spec.md#3-functional-requirements-fr), [FR-storyboard-review-002](../srs/storyboard-review-spec.md#3-functional-requirements-fr), [FR-storyboard-review-003](../srs/storyboard-review-spec.md#3-functional-requirements-fr), [FR-storyboard-review-004](../srs/storyboard-review-spec.md#3-functional-requirements-fr), [FR-storyboard-review-005](../srs/storyboard-review-spec.md#3-functional-requirements-fr), [FR-storyboard-review-006](../srs/storyboard-review-spec.md#3-functional-requirements-fr), [FR-storyboard-review-007](../srs/storyboard-review-spec.md#3-functional-requirements-fr), [FR-storyboard-review-008](../srs/storyboard-review-spec.md#3-functional-requirements-fr), [FR-storyboard-review-011](../srs/storyboard-review-spec.md#3-functional-requirements-fr), [FR-storyboard-review-012](../srs/storyboard-review-spec.md#3-functional-requirements-fr)
- BR: BR-storyboard-review-003
- Errors: E-storyboard-review-002 (wording in the spec Error Matrix — TBD)
- Stories: US-001, US-002 · Diagram: [Review storyboard shots (OUT) (Activity)](../srs/storyboard-review-flows.md)
