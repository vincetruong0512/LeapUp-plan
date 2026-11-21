---
type: usecase-index
feature: video-review
status: draft
updated: 2026-11-22
links:
  - docs/video-review/srs/video-review-spec.md
---

# Video Review — Use Cases Index

Built from the draft SRS, user flow and user stories; nothing added beyond them. Open questions stay in the spec (§12).

## Use cases

| # | Use case | Level | Status | Primary actor | Covers FR | Stories | Screens | Errors (E-*) | OQ ref | Priority | Updated |
|---|----------|-------|--------|---------------|-----------|---------|---------|--------------|--------|----------|---------|
| 1 | [UC-video-review-01 Review a round with timecoded comments](uc-review-a-round-with-timecoded-comments.md) | sea | draft | Client | FR-video-review-001, FR-video-review-002, FR-video-review-003, FR-video-review-004, FR-video-review-005, FR-video-review-006, FR-video-review-007, FR-video-review-008, FR-video-review-013, FR-video-review-014, FR-video-review-015 | US-001, US-002 (and project-files US-005) | [video-review](../html-wireframe/review.html#s1), [video-review-no-video](../html-wireframe/review.html#s2), [video-review-error](../html-wireframe/review.html#s3) | E-video-review-001, E-video-review-002, E-video-review-003, E-video-review-004 | spec.md#OQ-1, spec.md#OQ-6, spec.md#OQ-7 | P0 | 2026-11-22 |
| 2 | [UC-video-review-02 Resolve comments and log the round's changes](uc-resolve-comments-and-log-changes.md) | sea | draft | Leap Up member | FR-video-review-009, FR-video-review-012 | US-003, US-005 | [video-review](../html-wireframe/review.html#s1) | — | spec.md#OQ-2, spec.md#OQ-5, spec.md#OQ-7 | P0 | 2026-11-22 |
| 3 | [UC-video-review-03 Add a new version and start the next round](uc-start-the-next-round.md) | sea | draft | Leap Up member | FR-video-review-003, FR-video-review-010, FR-video-review-011, FR-video-review-013 | US-004 | [video-review](../html-wireframe/review.html#s1) | E-video-review-004 | spec.md#OQ-3, spec.md#OQ-4 | P0 | 2026-11-22 |

**Coverage:** 15 FR in the spec — 15 covered. 4 error codes — 4 used in extensions.

## Actors

| Actor | Type | Description | Source |
|---|---|---|---|
| Client | primary | Gives timecoded feedback | board L75 |
| Leap Up member | primary | Resolves feedback, manages rounds | board L118 |
| Cloudflare R2 | system | Stores and serves video | quote §5 |

## CRUD matrix

| UC \ Entity | Round | Version | Comment |
|---|---|---|---|
| [UC-01](uc-review-a-round-with-timecoded-comments.md) | R | R | CR |
| [UC-02](uc-resolve-comments-and-log-changes.md) | U |  | RU |
| [UC-03](uc-start-the-next-round.md) | CU | C |  |

Entities from spec §8.

## Relationships

None stated in the spec.

## Sources

- [SRS spec](../srs/video-review-spec.md) · [User flow](../srs/video-review-userflow.md) · [Stories](../userstories/video-review-story-index.md) · [Diagrams](../srs/video-review-flows.md)
