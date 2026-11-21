# Use Case: UC-outcome-approval-02 Track change requests and revision rounds

> Scope: Leap Up Client Project Portal — outcome-approval · Level: sea (user goal)

## Primary Actor

Leap Up member

## Trigger

Feedback leads to a change request.

## Preconditions

- The member is signed in and is a member of the project.

## Guarantees

- **Minimal Guarantee:** Existing change requests stay as they were if the change is not saved.
- **Success Guarantee:** The change request is in the table with request, round, scope, cost and status.

## Main Success Scenario

1. Member opens Outcome Development / Revision & Sign-off.
2. Portal shows Revision Rounds (Included, Used, Remaining and the note "Round 3 onwards: additional scope & cost" — OPEN C5), Approvers (OPEN C4) and the Change Requests table.
3. Member records or updates a change request: request, round, scope (In scope / Out of scope), cost (OPEN C5), status (Done, Quote sent, Client approved) (rights TBD).
4. Portal shows the change request in the table.

## Extensions

**2a. No change request exists:**
- 2a1. Portal shows E-outcome-approval-003.
- 2a2. Continue at step 3.

## Related Requirements

- FR: [FR-outcome-approval-001](../srs/outcome-approval-spec.md#3-functional-requirements-fr), [FR-outcome-approval-003](../srs/outcome-approval-spec.md#3-functional-requirements-fr), [FR-outcome-approval-004](../srs/outcome-approval-spec.md#3-functional-requirements-fr), [FR-outcome-approval-008](../srs/outcome-approval-spec.md#3-functional-requirements-fr), [FR-outcome-approval-009](../srs/outcome-approval-spec.md#3-functional-requirements-fr)
- BR: BR-outcome-approval-002, BR-outcome-approval-003, BR-outcome-approval-004
- Errors: E-outcome-approval-003 (wording in the spec Error Matrix — TBD)
- Stories: US-002, US-004 · Diagram: [Track change requests and revision rounds (Activity)](../srs/outcome-approval-flows.md)
