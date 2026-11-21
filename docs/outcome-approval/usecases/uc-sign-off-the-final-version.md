# Use Case: UC-outcome-approval-03 Sign off the final version

> Scope: Leap Up Client Project Portal — outcome-approval · Level: sea (user goal)

## Primary Actor

Client

## Stakeholders & Interests

| Stakeholder | Interest |
|-------------|----------|
| Leap Up | A reliable record of who approved and when (brainstorm R2) |

## Trigger

The final version is ready for sign-off.

## Preconditions

- The client is signed in and is a member of the project.
- FINAL SIGN-OFF shows the final file.

## Guarantees

- **Minimal Guarantee:** Nothing is recorded when the user may not approve or the checklist is incomplete.
- **Success Guarantee:** The Approval Log shows "Final sign-off" with the date instead of "Pending".

## Main Success Scenario

1. Client opens Revision & Sign-off.
2. Portal shows FINAL SIGN-OFF with the final file name and the three checks (OPEN C9).
3. Client ticks "Visuals, VO & music approved", "Mandatory copy & legal checked" and "Delivery formats confirmed".
4. Client presses "Approve final version".
5. Portal checks the user may approve (Final approver: Client).
6. Portal checks all three checks are ticked.
7. Portal records the final sign-off; the Approval Log shows it with the date.

## Extensions

**5a. The user may not approve:**
- 5a1. Portal records nothing and shows E-outcome-approval-001.
- 5a2. Use case ends.

**6a. A check is not ticked:**
- 6a1. Portal records nothing and shows E-outcome-approval-002.
- 6a2. Resume at step 3.

## Related Requirements

- FR: [FR-outcome-approval-005](../srs/outcome-approval-spec.md#3-functional-requirements-fr), [FR-outcome-approval-006](../srs/outcome-approval-spec.md#3-functional-requirements-fr), [FR-outcome-approval-007](../srs/outcome-approval-spec.md#3-functional-requirements-fr), [FR-outcome-approval-010](../srs/outcome-approval-spec.md#3-functional-requirements-fr)
- BR: BR-outcome-approval-001
- Errors: E-outcome-approval-001, E-outcome-approval-002 (wording in the spec Error Matrix — TBD)
- Stories: US-003 · Diagram: [Sign off the final version (Activity)](../srs/outcome-approval-flows.md)
