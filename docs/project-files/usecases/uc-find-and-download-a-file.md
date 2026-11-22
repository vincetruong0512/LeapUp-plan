# Use Case: UC-project-files-01 Find and download a file

> Scope: Leap Up Client Project Portal — project-files · Level: sea (user goal)

## Primary Actor

Client (same for Leap Up member)

## Trigger

The user needs a file of their project.

## Preconditions

- The user is signed in and is a member of the project.

## Guarantees

- **Minimal Guarantee:** No file of another project is shown or downloaded (BR-project-files-002).
- **Success Guarantee:** The user has a copy of the file they chose.

## Main Success Scenario

1. User opens the project.
2. Portal shows the header, the tabs, the three folder cards and the file table (Name, Folder, Last Modified, Uploaded By, Status).
3. User searches with "Search files..." or selects a folder card.
4. Portal shows the matching files.
5. User downloads a file (control placement TBD).
6. Portal delivers the file.

## Extensions

**1a. The user is not a member of the project:**
- 1a1. Portal refuses access (E-auth-access-003).
- 1a2. Use case ends.

**4a. No file matches the search:**
- 4a1. Portal shows an empty table (E-project-files-002).
- 4a2. Resume at step 3.

**4b. The selected folder has no files:**
- 4b1. Portal shows an empty table (E-project-files-004).
- 4b2. Resume at step 3.

**5a. The file is a video in Outcome Development (provisional — FR-project-files-014, spec OQ-8):**
- 5a1. User opens the video instead of downloading it.
- 5a2. Portal opens Video Review on that video; which round opens is TBD (spec OQ-8, OQ-17).
- 5a3. Use case continues in video-review UC-video-review-01.

**5b. Download fails (spec OQ-15):**
- 5b1. Behaviour, error code and wording TBD.

## Related Requirements

- FR: [FR-project-files-001](../srs/project-files-spec.md#3-functional-requirements-fr), [FR-project-files-002](../srs/project-files-spec.md#3-functional-requirements-fr), [FR-project-files-003](../srs/project-files-spec.md#3-functional-requirements-fr), [FR-project-files-004](../srs/project-files-spec.md#3-functional-requirements-fr), [FR-project-files-005](../srs/project-files-spec.md#3-functional-requirements-fr), [FR-project-files-008](../srs/project-files-spec.md#3-functional-requirements-fr), [FR-project-files-009](../srs/project-files-spec.md#3-functional-requirements-fr), [FR-project-files-010](../srs/project-files-spec.md#3-functional-requirements-fr), [FR-project-files-011](../srs/project-files-spec.md#3-functional-requirements-fr), [FR-project-files-012](../srs/project-files-spec.md#3-functional-requirements-fr), [FR-project-files-013](../srs/project-files-spec.md#3-functional-requirements-fr), [FR-project-files-014](../srs/project-files-spec.md#3-functional-requirements-fr) (provisional)
- BR: BR-project-files-001, BR-project-files-002, BR-project-files-003
- Errors: E-project-files-002, E-project-files-004 (wording in the spec Error Matrix — TBD)
- Stories: US-001, US-003, US-004, US-005 · Diagram: [Find and download a file (Activity)](../srs/project-files-flows.md)
