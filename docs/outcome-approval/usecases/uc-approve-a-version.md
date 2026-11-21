# Use Case: UC-outcome-approval-01 Approve a version

> Scope: Leap Up Client Project Portal — outcome-approval · Level: sea (user goal)

## Primary Actor

Client

## Trigger

A round shows "Awaiting client approval" (board L192).

## Preconditions

- The client is signed in and is a member of the project.
- A version exists in Video Review.

## Guarantees

- **Minimal Guarantee:** No approval is recorded for a user who may not approve.
- **Success Guarantee:** The approval of the version is recorded with who and when and appears in the Approval Log.

## Main Success Scenario

1. Client reviews the version in Video Review.
2. Client approves the version (control location TBD).
3. Portal checks the user may approve (rule TBD, OPEN C4).
4. Portal records the approval: version, approver, date.
5. Approval Log shows the entry with its date.

## Extensions

**3a. The user may not approve:**
- 3a1. Portal records nothing and shows E-outcome-approval-001.
- 3a2. Use case ends.

## Related Requirements

- FR: [FR-outcome-approval-002](../srs/outcome-approval-spec.md#3-functional-requirements-fr), [FR-outcome-approval-005](../srs/outcome-approval-spec.md#3-functional-requirements-fr), [FR-outcome-approval-010](../srs/outcome-approval-spec.md#3-functional-requirements-fr), [FR-outcome-approval-011](../srs/outcome-approval-spec.md#3-functional-requirements-fr)
- BR: —
- Errors: E-outcome-approval-001 (wording in the spec Error Matrix — TBD)
- Stories: US-001 · Diagram: [Approve a version (Activity)](../srs/outcome-approval-flows.md)
