# Use Case: UC-admin-02 Create a client account

> Scope: Leap Up Client Project Portal — admin · Level: sea (user goal)

## Primary Actor

Admin

## Stakeholders & Interests

| Stakeholder | Interest |
|-------------|----------|
| Client | Receives a unique User ID and Password (board L159) |

## Trigger

A client person needs access to the portal.

## Preconditions

- The Admin is signed in on the admin page.

## Guarantees

- **Minimal Guarantee:** No second account with the same User ID exists (case-insensitive).
- **Success Guarantee:** The client account exists and the client can sign in with its User ID and password.

## Main Success Scenario

1. Admin enters the User ID and initial password for the client.
2. Admin saves.
3. Portal checks the required fields.
4. Portal checks that the User ID is unique, ignoring case.
5. Portal creates the account.
6. Admin hands over the User ID and password outside the portal.

## Extensions

**3a. A required field is empty:**
- 3a1. Portal shows E-admin-001; nothing saved.
- 3a2. Resume at step 1.

**4a. The User ID already exists:**
- 4a1. Portal shows E-admin-002; nothing saved.
- 4a2. Resume at step 1.

## Related Requirements

- FR: [FR-admin-005](../srs/admin-spec.md#3-functional-requirements-fr), [FR-admin-006](../srs/admin-spec.md#3-functional-requirements-fr), [FR-admin-008](../srs/admin-spec.md#3-functional-requirements-fr)
- BR: BR-admin-001
- Errors: E-admin-001, E-admin-002 (wording in the spec Error Matrix — TBD)
- Stories: US-002 · Diagram: [Create a client account (Activity)](../srs/admin-flows.md)
