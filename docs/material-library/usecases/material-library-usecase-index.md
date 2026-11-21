---
type: usecase-index
feature: material-library
status: draft
updated: 2026-11-22
links:
  - docs/material-library/srs/material-library-spec.md
---

# Material Library — Use Cases Index

Built from the draft SRS, user flow and user stories; nothing added beyond them. Open questions stay in the spec (§12).

## Use cases

| # | Use case | Level | Status | Primary actor | Covers FR | Stories | Screens | Errors (E-*) | OQ ref | Priority | Updated |
|---|----------|-------|--------|---------------|-----------|---------|---------|--------------|--------|----------|---------|
| 1 | [UC-material-library-01 Choose a material direction (OUT)](uc-choose-a-material-direction.md) | sea | draft | Client | FR-material-library-001, FR-material-library-002, FR-material-library-003, FR-material-library-004, FR-material-library-005, FR-material-library-006, FR-material-library-007, FR-material-library-009, FR-material-library-010, FR-material-library-011, FR-material-library-012, FR-material-library-013, FR-material-library-014 | US-001, US-002, US-003 | [material-library](../html-wireframe/options.html#s1), [material-library-empty](../html-wireframe/options.html#s2), [option-feedback](../html-wireframe/options.html#s3), [submit-error](../html-wireframe/options.html#s4), [approval-summary](../html-wireframe/options.html#s5) | E-material-library-001, E-material-library-002, E-material-library-004 | spec.md#OQ-1, spec.md#OQ-2, spec.md#OQ-3, spec.md#OQ-4, spec.md#OQ-6 | P0 | 2026-11-22 |
| 2 | [UC-material-library-02 Provide option visuals (OUT)](uc-provide-option-visuals.md) | sea | draft | Leap Up member | FR-material-library-008 | US-004 | [material-library](../html-wireframe/options.html#s1) | E-material-library-003 | spec.md#OQ-5 | P0 | 2026-11-22 |

**Coverage:** 14 FR in the spec — 14 covered. 4 error codes — 4 used in extensions.

## Actors

| Actor | Type | Description | Source |
|---|---|---|---|
| Client | primary | Compares options, gives feedback, chooses a direction | board L372–L373 |
| Leap Up member | primary | Provides option visuals and revises | board L398, L424 |

## CRUD matrix

| UC \ Entity | MaterialCategory | MaterialOption | OptionFeedback |
|---|---|---|---|
| [UC-01](uc-choose-a-material-direction.md) | R | RU | C |
| [UC-02](uc-provide-option-visuals.md) |  | U |  |

Entities from spec §8.

## Relationships

None stated in the spec.

## Sources

- [SRS spec](../srs/material-library-spec.md) · [User flow](../srs/material-library-userflow.md) · [Stories](../userstories/material-library-story-index.md) · [Diagrams](../srs/material-library-flows.md)
