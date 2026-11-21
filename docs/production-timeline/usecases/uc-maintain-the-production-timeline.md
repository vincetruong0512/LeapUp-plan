# Use Case: UC-production-timeline-02 Maintain stages and milestones

> Scope: Leap Up Client Project Portal — production-timeline · Level: sea (user goal)

## Primary Actor

Leap Up member

## Trigger

The production moves on or dates change.

## Preconditions

- The member is signed in and is a member of the project.

## Guarantees

- **Minimal Guarantee:** The timeline stays as it was if the change is not saved.
- **Success Guarantee:** Stage dates and statuses and the milestones show the update to all project members.

## Main Success Scenario

1. Leap Up member opens the timeline.
2. Member changes a stage's dates or status (DONE, CLIENT REVIEW, UP NEXT, NOT STARTED) (controls TBD).
3. Member adds or changes a milestone: name, owner (Client or Leap Up), due date, status (Done, Waiting, Pending, Not started).
4. Portal shows the updated timeline to all project members.

## Extensions

None in the spec.

## Related Requirements

- FR: [FR-production-timeline-003](../srs/production-timeline-spec.md#3-functional-requirements-fr), [FR-production-timeline-005](../srs/production-timeline-spec.md#3-functional-requirements-fr), [FR-production-timeline-006](../srs/production-timeline-spec.md#3-functional-requirements-fr)
- BR: BR-production-timeline-002
- Errors: —
- Stories: US-002 · Diagram: [Maintain stages and milestones (Activity)](../srs/production-timeline-flows.md)
