---
type: usecase-index
feature: dashboard-tasks
status: draft
updated: 2026-11-22
links:
  - docs/dashboard-tasks/srs/dashboard-tasks-spec.md
---

# Dashboard & Task List — Use Cases Index

Built from the draft SRS, user flow and user stories; nothing added beyond them. Open questions stay in the spec (§12).

## Use cases

| # | Use case | Level | Status | Primary actor | Covers FR | Stories | Screens | Errors (E-*) | OQ ref | Priority | Updated |
|---|----------|-------|--------|---------------|-----------|---------|---------|--------------|--------|----------|---------|
| 1 | [UC-dashboard-tasks-01 Check the overview and act on Action Required](uc-check-overview-and-act.md) | sea | draft | Leap Up member (Client — TBD) | FR-dashboard-tasks-001, FR-dashboard-tasks-002, FR-dashboard-tasks-003, FR-dashboard-tasks-004, FR-dashboard-tasks-009, FR-dashboard-tasks-010, FR-dashboard-tasks-011 | US-001, US-004 | [home](../html-wireframe/overview.html#s1), [home-empty](../html-wireframe/overview.html#s2) | E-dashboard-tasks-002 | spec.md#OQ-1, spec.md#OQ-3, spec.md#OQ-4 | P0 | 2026-11-22 |
| 2 | [UC-dashboard-tasks-02 Manage a project's tasks](uc-manage-project-tasks.md) | sea | draft | Leap Up member | FR-dashboard-tasks-004, FR-dashboard-tasks-005, FR-dashboard-tasks-006, FR-dashboard-tasks-007, FR-dashboard-tasks-008 | US-002, US-003 | [task-list](../html-wireframe/tasks.html#s1), [task-error](../html-wireframe/tasks.html#s2) | E-dashboard-tasks-001, E-dashboard-tasks-003 | spec.md#OQ-2, spec.md#OQ-5, spec.md#OQ-6, spec.md#OQ-7, spec.md#OQ-8 | P0 | 2026-11-22 |

**Coverage:** 11 FR in the spec — 11 covered. 3 error codes — 3 used in extensions.

## Actors

| Actor | Type | Description | Source |
|---|---|---|---|
| Leap Up member | primary | Tracks projects and tasks (Account, L199) | quote P2 #1 |
| Client | primary | Sees items awaiting their review (Home for clients TBD) | board L196, L199 |

## CRUD matrix

| UC \ Entity | Task | ActionItem | Project |
|---|---|---|---|
| [UC-01](uc-check-overview-and-act.md) | R | R | R |
| [UC-02](uc-manage-project-tasks.md) | CRU |  |  |

Entities from spec §8.

## Relationships

None stated in the spec.

## Sources

- [SRS spec](../srs/dashboard-tasks-spec.md) · [User flow](../srs/dashboard-tasks-userflow.md) · [Stories](../userstories/dashboard-tasks-story-index.md) · [Diagrams](../srs/dashboard-tasks-flows.md)
