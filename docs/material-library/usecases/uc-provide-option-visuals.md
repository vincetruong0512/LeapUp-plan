# Use Case: UC-material-library-02 Provide option visuals (OUT)

> Scope: Leap Up Client Project Portal — material-library · Level: sea (user goal)

## Primary Actor

Leap Up member

## Trigger

Options still show "Demo visual | Replace with uploaded assets".

## Preconditions

- The member is signed in and is a member of the project.
- OUT: change request needed.

## Guarantees

- **Minimal Guarantee:** The demo visual stays when the upload fails.
- **Success Guarantee:** The option card shows the uploaded visual.

## Main Success Scenario

1. Leap Up member opens the option in Material Library.
2. Member uploads the asset for the option (who and how TBD).
3. Portal stores the asset.
4. Portal shows the uploaded visual on the card.

## Extensions

**3a. The upload fails:**
- 3a1. Portal keeps the demo visual and shows E-material-library-003.
- 3a2. Resume at step 2.

## Related Requirements

- FR: [FR-material-library-008](../srs/material-library-spec.md#3-functional-requirements-fr)
- BR: —
- Errors: E-material-library-003 (wording in the spec Error Matrix — TBD)
- Stories: US-004 · Diagram: [Provide option visuals (OUT) (Sequence)](../srs/material-library-flows.md)
