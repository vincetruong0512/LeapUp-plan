---
type: usecase-index
feature: storyboard-review
status: draft
updated: 2026-11-22
links:
  - docs/storyboard-review/srs/storyboard-review-spec.md
---

# Storyboard Review — Use Cases Index

Built from the draft SRS, user flow and user stories; nothing added beyond them. Open questions stay in the spec (§12).

## Use cases

| # | Use case | Level | Status | Primary actor | Covers FR | Stories | Screens | Errors (E-*) | OQ ref | Priority | Updated |
|---|----------|-------|--------|---------------|-----------|---------|---------|--------------|--------|----------|---------|
| 1 | [UC-storyboard-review-01 Review storyboard shots (OUT)](uc-review-storyboard-shots.md) | sea | draft | Client | FR-storyboard-review-001, FR-storyboard-review-002, FR-storyboard-review-003, FR-storyboard-review-004, FR-storyboard-review-005, FR-storyboard-review-006, FR-storyboard-review-007, FR-storyboard-review-008, FR-storyboard-review-011, FR-storyboard-review-012 | US-001, US-002 | [storyboard](../html-wireframe/storyboard.html#s1), [frame-comment](../html-wireframe/storyboard.html#s2) | E-storyboard-review-002 | spec.md#OQ-2, spec.md#OQ-4 | P0 | 2026-11-22 |
| 2 | [UC-storyboard-review-02 Approve and lock the storyboard (OUT)](uc-approve-and-lock-the-storyboard.md) | sea | draft | Client | FR-storyboard-review-009, FR-storyboard-review-010 | US-003 | [storyboard](../html-wireframe/storyboard.html#s1), [storyboard-approved](../html-wireframe/storyboard.html#s3), [storyboard-approve-error](../html-wireframe/storyboard.html#s4) | E-storyboard-review-001, E-storyboard-review-003, E-storyboard-review-004 | spec.md#OQ-3, spec.md#OQ-5, spec.md#OQ-6 | P0 | 2026-11-22 |

**Coverage:** 12 FR in the spec — 12 covered. 4 error codes — 4 used in extensions.

## Actors

| Actor | Type | Description | Source |
|---|---|---|---|
| Client | primary | Approves or comments per shot; approves the storyboard | board L428, L455–L456 |
| Leap Up member | primary | Shares and revises storyboard versions | board L429, L479 |

## CRUD matrix

| UC \ Entity | StoryboardVersion | Frame | FrameComment |
|---|---|---|---|
| [UC-01](uc-review-storyboard-shots.md) | R | RU | C |
| [UC-02](uc-approve-and-lock-the-storyboard.md) | U | R |  |

Entities from spec §8.

## Relationships

None stated in the spec.

## Sources

- [SRS spec](../srs/storyboard-review-spec.md) · [User flow](../srs/storyboard-review-userflow.md) · [Stories](../userstories/storyboard-review-story-index.md) · [Diagrams](../srs/storyboard-review-flows.md)
