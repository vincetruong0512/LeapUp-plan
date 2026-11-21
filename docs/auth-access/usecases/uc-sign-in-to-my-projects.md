# Use Case: UC-auth-access-01 Sign in to my projects

> Scope: Leap Up Client Project Portal — auth-access · Level: sea (user goal)

## Primary Actor

Client (same for Leap Up member and Admin)

## Stakeholders & Interests

| Stakeholder | Interest |
|-------------|----------|
| Leap Up | Client content stays private per project (board L139–L146) |

## Trigger

The user opens the portal to reach their project workspace.

## Preconditions

- The account was created by Leap Up (BR-auth-access-001).
- The User ID and password were handed over outside the portal.

## Guarantees

- **Minimal Guarantee:** No session is created when sign-in fails; no content of a project the user is not assigned to is shown (BR-auth-access-002).
- **Success Guarantee:** The user is signed in and sees only the projects assigned to them (Admin: all projects) on the landing page (landing page TBD).

## Main Success Scenario

1. User enters the User ID and password; may press "Show" to read the typed password.
2. User presses "Sign In".
3. Portal checks that both fields are filled.
4. Portal matches the User ID (not case-sensitive) and password to an account.
5. Portal finds the projects the user is assigned to.
6. Portal shows the landing page with only those projects.

## Extensions

**3a. User ID or Password is empty:**
- 3a1. Portal shows E-auth-access-002 and checks nothing.
- 3a2. Resume at step 1.

**4a. User ID and password do not match an account:**
- 4a1. Portal keeps the user on Login and shows E-auth-access-001.
- 4a2. Resume at step 1.

**5a. The user has no assigned project:**
- 5a1. Portal shows the "no projects" state (E-auth-access-004).
- 5a2. Use case ends: signed in, no project shown.

***a. At any time the user requests a project, file, video or comment of a project they are not assigned to:**
- *a1. Portal refuses it (E-auth-access-003).
- *a2. The user continues with their own projects.

## Related Requirements

- FR: [FR-auth-access-001](../srs/auth-access-spec.md#3-functional-requirements-fr), [FR-auth-access-002](../srs/auth-access-spec.md#3-functional-requirements-fr), [FR-auth-access-003](../srs/auth-access-spec.md#3-functional-requirements-fr), [FR-auth-access-004](../srs/auth-access-spec.md#3-functional-requirements-fr), [FR-auth-access-005](../srs/auth-access-spec.md#3-functional-requirements-fr), [FR-auth-access-006](../srs/auth-access-spec.md#3-functional-requirements-fr), [FR-auth-access-007](../srs/auth-access-spec.md#3-functional-requirements-fr), [FR-auth-access-008](../srs/auth-access-spec.md#3-functional-requirements-fr), [FR-auth-access-009](../srs/auth-access-spec.md#3-functional-requirements-fr), [FR-auth-access-010](../srs/auth-access-spec.md#3-functional-requirements-fr)
- BR: BR-auth-access-001, BR-auth-access-002, BR-auth-access-003
- Errors: E-auth-access-001, E-auth-access-002, E-auth-access-003, E-auth-access-004 (wording in the spec Error Matrix — TBD)
- Stories: US-001, US-002 · Diagram: [Sign in to my projects (Activity)](../srs/auth-access-flows.md)
