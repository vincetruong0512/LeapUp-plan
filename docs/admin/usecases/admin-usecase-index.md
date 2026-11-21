---
type: usecase-index
feature: admin
status: draft
updated: 2026-11-22
links:
  - docs/admin/srs/admin-spec.md
---

# Admin — Use Cases Index

Built from the draft SRS, user flow and user stories; nothing added beyond them. Open questions stay in the spec (§12).

## Use cases

| # | Use case | Level | Status | Primary actor | Covers FR | Stories | Screens | Errors (E-*) | OQ ref | Priority | Updated |
|---|----------|-------|--------|---------------|-----------|---------|---------|--------------|--------|----------|---------|
| 1 | [UC-admin-01 Create a project](uc-create-project.md) | sea | draft | Admin | FR-admin-001, FR-admin-002, FR-admin-003, FR-admin-004, FR-admin-008 | US-001 | TBD (C3) | E-admin-001, E-admin-003 | spec.md#OQ-1, spec.md#OQ-3 | P0 | 2026-11-22 |
| 2 | [UC-admin-02 Create a client account](uc-create-client-account.md) | sea | draft | Admin | FR-admin-005, FR-admin-006, FR-admin-008 | US-002 | TBD (C3) | E-admin-001, E-admin-002 | spec.md#OQ-2, spec.md#OQ-4 | P0 | 2026-11-22 |
| 3 | [UC-admin-03 Assign members to a project](uc-assign-members.md) | sea | draft | Admin | FR-admin-007 | US-003 | TBD (C3) | — | spec.md#OQ-6 | P0 | 2026-11-22 |

**Coverage:** 8 FR in the spec — 8 covered. 3 error codes — 3 used in extensions.

## Actors

| Actor | Type | Description | Source |
|---|---|---|---|
| Admin | primary | Leap Up admin who sets up projects and access | quote P1 #1 |
| Client | secondary | Receives the account details outside the portal | board L159 |

## CRUD matrix

| UC \ Entity | Project | Folder | UserAccount | ProjectMembership |
|---|---|---|---|---|
| [UC-01](uc-create-project.md) | C | C |  |  |
| [UC-02](uc-create-client-account.md) |  |  | C |  |
| [UC-03](uc-assign-members.md) | R |  | R | C |

Entities from spec §8.

## Relationships

None stated in the spec.

## Sources

- [SRS spec](../srs/admin-spec.md) · [User flow](../srs/admin-userflow.md) · [Stories](../userstories/admin-story-index.md) · [Diagrams](../srs/admin-flows.md)
