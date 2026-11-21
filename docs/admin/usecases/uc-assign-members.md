# Use Case: UC-admin-03 Assign members to a project

> Scope: Leap Up Client Project Portal — admin · Level: sea (user goal)

## Primary Actor

Admin

## Trigger

A person must start working on, or reviewing, a project.

## Preconditions

- The project and the user account exist.

## Guarantees

- **Minimal Guarantee:** A user who is not assigned does not see the project (BR-admin-002).
- **Success Guarantee:** The user is a member of the project with role Leap Up or Client and sees it after signing in.

## Main Success Scenario

1. Admin opens the project in the admin page.
2. Admin selects a user and the role Leap Up or Client.
3. Admin saves.
4. Portal records the membership.

## Extensions

**2a. The user is already a member of the project:**
- 2a1. No change (brainstorm D3, assumed).
- 2a2. Use case ends.

## Related Requirements

- FR: [FR-admin-007](../srs/admin-spec.md#3-functional-requirements-fr)
- BR: BR-admin-002, BR-admin-003
- Errors: —
- Stories: US-003 · Diagram: [Assign members to a project (Activity)](../srs/admin-flows.md)
