---
type: usecase-index
feature: production-timeline
status: draft
updated: 2026-11-22
links:
  - docs/production-timeline/srs/production-timeline-spec.md
---

# Production Timeline — Use Cases Index

Built from the draft SRS, user flow and user stories; nothing added beyond them. Open questions stay in the spec (§12).

## Use cases

| # | Use case | Level | Status | Primary actor | Covers FR | Stories | Screens | Errors (E-*) | OQ ref | Priority | Updated |
|---|----------|-------|--------|---------------|-----------|---------|---------|--------------|--------|----------|---------|
| 1 | [UC-production-timeline-01 Follow the production timeline](uc-follow-the-production-timeline.md) | sea | draft | Client | FR-production-timeline-001, FR-production-timeline-002, FR-production-timeline-003, FR-production-timeline-004, FR-production-timeline-005, FR-production-timeline-009 | US-001 | [timeline](../html-wireframe/timeline.html#s1) | E-production-timeline-001 | spec.md#OQ-1, spec.md#OQ-3, spec.md#OQ-4 | P0 | 2026-11-22 |
| 2 | [UC-production-timeline-02 Maintain stages and milestones](uc-maintain-the-production-timeline.md) | sea | draft | Leap Up member | FR-production-timeline-003, FR-production-timeline-005, FR-production-timeline-006 | US-002 | [timeline](../html-wireframe/timeline.html#s1) | — | spec.md#OQ-2, spec.md#OQ-3 | P0 | 2026-11-22 |
| 3 | [UC-production-timeline-03 Provide missing client inputs (OPEN C6)](uc-provide-client-inputs.md) | sea | draft | Client | FR-production-timeline-007, FR-production-timeline-008 | US-003 | [timeline](../html-wireframe/timeline.html#s1), [timeline-upload-error](../html-wireframe/timeline.html#s2) | E-production-timeline-002 | spec.md#OQ-5, spec.md#OQ-6 | P1 | 2026-11-22 |

**Coverage:** 9 FR in the spec — 9 covered. 2 error codes — 2 used in extensions.

## Actors

| Actor | Type | Description | Source |
|---|---|---|---|
| Client | primary | Follows progress; provides inputs (C6) | board L255–L299 |
| Leap Up member | primary | Maintains the timeline | quote P2 #2 |

## CRUD matrix

| UC \ Entity | Stage | Milestone | ClientInput |
|---|---|---|---|
| [UC-01](uc-follow-the-production-timeline.md) | R | R |  |
| [UC-02](uc-maintain-the-production-timeline.md) | U | CU |  |
| [UC-03](uc-provide-client-inputs.md) |  |  | RU |

Entities from spec §8.

## Relationships

None stated in the spec.

## Sources

- [SRS spec](../srs/production-timeline-spec.md) · [User flow](../srs/production-timeline-userflow.md) · [Stories](../userstories/production-timeline-story-index.md) · [Diagrams](../srs/production-timeline-flows.md)
