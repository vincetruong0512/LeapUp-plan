# Use Case: UC-project-files-02 Upload files into a folder

> Scope: Leap Up Client Project Portal — project-files · Level: sea (user goal)

## Primary Actor

Leap Up member (Client per board; rights TBD)

## Trigger

The user has files or videos to share in the project.

## Preconditions

- The user is signed in and is a member of the project.

## Guarantees

- **Minimal Guarantee:** A rejected or failed file is not listed.
- **Success Guarantee:** The file is stored in Cloudflare R2 and listed with its folder, today's date, Uploaded By (Leap Up or Client) and a status.

## Main Success Scenario

1. User presses "Upload Files".
2. User chooses the files and the target folder (folder choice TBD).
3. Portal checks file type and size (limits TBD).
4. Portal stores the files in Cloudflare R2.
5. Portal lists each file with Name, Folder, Last Modified, Uploaded By and Status (initial status TBD).

## Extensions

**3a. Type or size not allowed:**
- 3a1. Portal rejects the file (E-project-files-001).
- 3a2. Resume at step 2.

**4a. Storage or network failure:**
- 4a1. Portal adds no row and shows E-project-files-003.
- 4a2. Resume at step 1.

## Related Requirements

- FR: [FR-project-files-006](../srs/project-files-spec.md#3-functional-requirements-fr), [FR-project-files-007](../srs/project-files-spec.md#3-functional-requirements-fr), [FR-project-files-008](../srs/project-files-spec.md#3-functional-requirements-fr), [FR-project-files-009](../srs/project-files-spec.md#3-functional-requirements-fr)
- BR: BR-project-files-003, BR-project-files-004
- Errors: E-project-files-001, E-project-files-003 (wording in the spec Error Matrix — TBD)
- Stories: US-002 · Diagram: [Upload files into a folder (Sequence)](../srs/project-files-flows.md)
