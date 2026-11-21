# Use Case: UC-dashboard-tasks-02 Manage a project's tasks

> Scope: Leap Up Client Project Portal — dashboard-tasks · Level: sea (user goal)

## Primary Actor

Leap Up member

## Trigger

Work in a project must be planned or its progress updated.

## Preconditions

- The user is signed in and is a member of the project.

## Guarantees

- **Minimal Guarantee:** No task is created without a name.
- **Success Guarantee:** The task is in the project's table with name, owner, due date and status; status changes show after the page is loaded again (no realtime).

## Main Success Scenario

1. Member opens "Update Task List" (or the project's Task List tab).
2. Portal shows the task table per project (TASK, OWNER, DUE, STATUS).
3. Member creates a task with name, owner, due date and status (controls TBD).
4. Portal checks the task name.
5. Portal adds the task to the project's table.
6. Member updates a task status: To Do, In Progress, Pending Review or Completed.
7. Portal shows the new status when the page is loaded again.

## Extensions

**2a. The project has no tasks:**
- 2a1. Portal shows an empty table (E-dashboard-tasks-003).
- 2a2. Continue at step 3.

**4a. The task name is empty:**
- 4a1. Portal creates nothing and shows E-dashboard-tasks-001.
- 4a2. Resume at step 3.

## Related Requirements

- FR: [FR-dashboard-tasks-004](../srs/dashboard-tasks-spec.md#3-functional-requirements-fr), [FR-dashboard-tasks-005](../srs/dashboard-tasks-spec.md#3-functional-requirements-fr), [FR-dashboard-tasks-006](../srs/dashboard-tasks-spec.md#3-functional-requirements-fr), [FR-dashboard-tasks-007](../srs/dashboard-tasks-spec.md#3-functional-requirements-fr), [FR-dashboard-tasks-008](../srs/dashboard-tasks-spec.md#3-functional-requirements-fr)
- BR: BR-dashboard-tasks-001, BR-dashboard-tasks-002, BR-dashboard-tasks-003
- Errors: E-dashboard-tasks-001, E-dashboard-tasks-003 (wording in the spec Error Matrix — TBD)
- Stories: US-002, US-003 · Diagram: [Manage a project's tasks (Activity)](../srs/dashboard-tasks-flows.md)
