---
type: usecase-index
feature: project-files
status: draft
updated: 2026-11-22
links:
  - docs/project-files/srs/project-files-spec.md
---

# Project Files — Use Cases Index

Built from the draft SRS, user flow and user stories; nothing added beyond them. Open questions stay in the spec (§12).

## Use cases

| # | Use case | Level | Status | Primary actor | Covers FR | Stories | Screens | Errors (E-*) | OQ ref | Priority | Updated |
|---|----------|-------|--------|---------------|-----------|---------|---------|--------------|--------|----------|---------|
| 1 | [UC-project-files-01 Find and download a file](uc-find-and-download-a-file.md) | sea | draft | Client (same for Leap Up member) | FR-project-files-001, FR-project-files-002, FR-project-files-003, FR-project-files-004, FR-project-files-005, FR-project-files-008, FR-project-files-009, FR-project-files-010, FR-project-files-011, FR-project-files-012, FR-project-files-013, FR-project-files-014 | US-001, US-003, US-004, US-005 | [project-files](../html-wireframe/files.html#s1), [no-result, empty-folder](../html-wireframe/files.html#s2) | E-project-files-002, E-project-files-004 | spec.md#OQ-1, spec.md#OQ-5, spec.md#OQ-6, spec.md#OQ-7 | P0 | 2026-11-22 |
| 2 | [UC-project-files-02 Upload files into a folder](uc-upload-files.md) | sea | draft | Leap Up member (Client per board; rights TBD) | FR-project-files-006, FR-project-files-007, FR-project-files-008, FR-project-files-009 | US-002 | [upload](../html-wireframe/files.html#s3), [upload-rejected, upload-failed](../html-wireframe/files.html#s4) | E-project-files-001, E-project-files-003 | spec.md#OQ-3, spec.md#OQ-4, spec.md#OQ-5, spec.md#OQ-11 | P0 | 2026-11-22 |

**Coverage:** 14 FR in the spec — 14 covered (FR-project-files-014 covered by video-review UC-01 (step 1 entry)). 4 error codes — 4 used in extensions.

## Actors

| Actor | Type | Description | Source |
|---|---|---|---|
| Client | primary | Gets files; uploads per board (rights TBD) | board L143, L153 |
| Leap Up member | primary | Shares files with the client | quote P1 #2 |
| Cloudflare R2 | system | Stores files | quote §5 |

## CRUD matrix

| UC \ Entity | File | Folder | Project |
|---|---|---|---|
| [UC-01](uc-find-and-download-a-file.md) | R | R | R |
| [UC-02](uc-upload-files.md) | C | R |  |

Entities from spec §8.

## Relationships

None stated in the spec.

## Sources

- [SRS spec](../srs/project-files-spec.md) · [User flow](../srs/project-files-userflow.md) · [Stories](../userstories/project-files-story-index.md) · [Diagrams](../srs/project-files-flows.md)
