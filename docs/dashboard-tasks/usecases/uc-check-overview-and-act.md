# Use Case: UC-dashboard-tasks-01 Check the overview and act on Action Required

> Scope: Leap Up Client Project Portal — dashboard-tasks · Level: sea (user goal)

## Primary Actor

Leap Up member (Client — TBD)

## Trigger

The user opens Dashboard to see where projects stand.

## Preconditions

- The user is signed in.

## Guarantees

- **Minimal Guarantee:** Projects the user is not assigned to are neither counted nor shown (FR-dashboard-tasks-011).
- **Success Guarantee:** The user has seen the status of their assigned projects and reached the review screen of an item awaiting review.

## Main Success Scenario

1. User opens Dashboard.
2. Portal shows the stat cards (Active Projects, Total Tasks, Completed Tasks), project cards (Deadline, Progress), task tables by project and Action Required with "{n} Pending Reviews" — assigned projects only.
3. User presses "Review Now" on an item.
4. Portal opens the item's review screen (targets TBD).

## Extensions

**2a. No item awaits review:**
- 2a1. Portal shows E-dashboard-tasks-002 in Action Required.
- 2a2. Use case ends after step 2.

## Related Requirements

- FR: [FR-dashboard-tasks-001](../srs/dashboard-tasks-spec.md#3-functional-requirements-fr), [FR-dashboard-tasks-002](../srs/dashboard-tasks-spec.md#3-functional-requirements-fr), [FR-dashboard-tasks-003](../srs/dashboard-tasks-spec.md#3-functional-requirements-fr), [FR-dashboard-tasks-004](../srs/dashboard-tasks-spec.md#3-functional-requirements-fr), [FR-dashboard-tasks-009](../srs/dashboard-tasks-spec.md#3-functional-requirements-fr), [FR-dashboard-tasks-010](../srs/dashboard-tasks-spec.md#3-functional-requirements-fr), [FR-dashboard-tasks-011](../srs/dashboard-tasks-spec.md#3-functional-requirements-fr)
- BR: BR-dashboard-tasks-003
- Errors: E-dashboard-tasks-002 (wording in the spec Error Matrix — TBD)
- Stories: US-001, US-004 · Diagram: [Check the overview and act on Action Required (Activity)](../srs/dashboard-tasks-flows.md)
