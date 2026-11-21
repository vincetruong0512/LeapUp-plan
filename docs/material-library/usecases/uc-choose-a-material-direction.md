# Use Case: UC-material-library-01 Choose a material direction (OUT)

> Scope: Leap Up Client Project Portal — material-library · Level: sea (user goal)

## Primary Actor

Client

## Trigger

Options for a material category are ready for the client (e.g. Action Required "Character Option A … Select visual direction and approve", L208–L215).

## Preconditions

- The client is signed in and is a member of the project.
- OUT: built only after a change request (quote §6, §7).

## Guarantees

- **Minimal Guarantee:** Nothing is submitted without a selected option (rule TBD); feedback without text is not saved.
- **Success Guarantee:** One preferred option per category is selected, feedback is recorded on the options, and the selection has entered the approval workflow (Option submitted → Client feedback → Revision → Approved).

## Main Success Scenario

1. Client opens Material Library (Material area or Review Now).
2. Portal shows MATERIAL CATEGORIES with counts and the "Approval Summary {n}" button.
3. Client selects a category.
4. Portal shows "{CATEGORY} / OPTION REVIEW", the instruction, the option cards (type, name, visual, status, Feedback note), the REVIEW GUIDE and the APPROVAL WORKFLOW.
5. Client opens "Details / Feedback" on an option and saves feedback.
6. Client presses "Select Option {X}"; the option reads "Selected Option {X}" with status Selected.
7. Client submits for approval (control TBD).
8. Portal moves the option into the approval workflow.

## Extensions

**4a. The category has no options:**
- 4a1. Portal shows E-material-library-001.
- 4a2. Resume at step 3.

**5a. Feedback text is empty:**
- 5a1. Portal saves nothing and shows E-material-library-002.
- 5a2. Resume at step 5.

**7a. No option is selected (rule TBD):**
- 7a1. Portal submits nothing and shows E-material-library-004.
- 7a2. Resume at step 6.

***a. Client presses "Approval Summary {n}":**
- *a1. Portal shows the approval summary (content TBD).
- *a2. Continue at step 3.

## Related Requirements

- FR: [FR-material-library-001](../srs/material-library-spec.md#3-functional-requirements-fr), [FR-material-library-002](../srs/material-library-spec.md#3-functional-requirements-fr), [FR-material-library-003](../srs/material-library-spec.md#3-functional-requirements-fr), [FR-material-library-004](../srs/material-library-spec.md#3-functional-requirements-fr), [FR-material-library-005](../srs/material-library-spec.md#3-functional-requirements-fr), [FR-material-library-006](../srs/material-library-spec.md#3-functional-requirements-fr), [FR-material-library-007](../srs/material-library-spec.md#3-functional-requirements-fr), [FR-material-library-009](../srs/material-library-spec.md#3-functional-requirements-fr), [FR-material-library-010](../srs/material-library-spec.md#3-functional-requirements-fr), [FR-material-library-011](../srs/material-library-spec.md#3-functional-requirements-fr), [FR-material-library-012](../srs/material-library-spec.md#3-functional-requirements-fr), [FR-material-library-013](../srs/material-library-spec.md#3-functional-requirements-fr), [FR-material-library-014](../srs/material-library-spec.md#3-functional-requirements-fr)
- BR: BR-material-library-001, BR-material-library-002, BR-material-library-003
- Errors: E-material-library-001, E-material-library-002, E-material-library-004 (wording in the spec Error Matrix — TBD)
- Stories: US-001, US-002, US-003 · Diagram: [Choose a material direction (OUT) (Activity)](../srs/material-library-flows.md)
