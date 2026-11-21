# Use Case: UC-auth-access-02 Sign out

> Scope: Leap Up Client Project Portal — auth-access · Level: sea (user goal)

## Primary Actor

Leap Up member (same for Client and Admin)

## Trigger

The user has finished working in the portal.

## Preconditions

- The user is signed in.

## Guarantees

- **Minimal Guarantee:** The session stays as it was if sign-out does not complete.
- **Success Guarantee:** The session has ended; the Login screen is shown and project pages require signing in again.

## Main Success Scenario

1. User chooses Sign out (placement TBD).
2. Portal ends the session.
3. Portal shows the Login screen.

## Extensions

None in the spec.

## Related Requirements

- FR: [FR-auth-access-011](../srs/auth-access-spec.md#3-functional-requirements-fr)
- BR: —
- Errors: —
- Stories: US-003 · Diagram: [Sign out (Sequence)](../srs/auth-access-flows.md)
