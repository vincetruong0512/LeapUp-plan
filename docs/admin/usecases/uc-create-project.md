# Use Case: UC-admin-01 Create a project

> Scope: Leap Up Client Project Portal — admin · Level: sea (user goal)

## Primary Actor

Admin

## Trigger

Leap Up starts a production for a client.

## Preconditions

- The Admin is signed in.

## Guarantees

- **Minimal Guarantee:** No partially created project exists after a failed save.
- **Success Guarantee:** The project exists with status "In Progress" and the folders Proposal, Material and Outcome Development.

## Main Success Scenario

1. Admin opens the admin page (design TBD, C3).
2. Portal confirms the user is an Admin.
3. Admin enters the project details (field list TBD).
4. Admin saves.
5. Portal checks the required fields.
6. Portal creates the project with status "In Progress" and its three folders.

## Extensions

**2a. The user is not an Admin:**
- 2a1. Portal refuses access (E-admin-003).
- 2a2. Use case ends; nothing created.

**5a. A required field is empty:**
- 5a1. Portal does not save and shows E-admin-001.
- 5a2. Resume at step 3.

## Related Requirements

- FR: [FR-admin-001](../srs/admin-spec.md#3-functional-requirements-fr), [FR-admin-002](../srs/admin-spec.md#3-functional-requirements-fr), [FR-admin-003](../srs/admin-spec.md#3-functional-requirements-fr), [FR-admin-004](../srs/admin-spec.md#3-functional-requirements-fr), [FR-admin-008](../srs/admin-spec.md#3-functional-requirements-fr)
- BR: BR-admin-001
- Errors: E-admin-001, E-admin-003 (wording in the spec Error Matrix — TBD)
- Stories: US-001 · Diagram: [Create a project (Activity)](../srs/admin-flows.md)
