---
type: usecase-index
feature: auth-access
status: draft
updated: 2026-11-22
links:
  - docs/auth-access/srs/auth-access-spec.md
---

# Login & Project Access — Use Cases Index

Built from the draft SRS, user flow and user stories; nothing added beyond them. Open questions stay in the spec (§12).

## Use cases

| # | Use case | Level | Status | Primary actor | Covers FR | Stories | Screens | Errors (E-*) | OQ ref | Priority | Updated |
|---|----------|-------|--------|---------------|-----------|---------|---------|--------------|--------|----------|---------|
| 1 | [UC-auth-access-01 Sign in to my projects](uc-sign-in-to-my-projects.md) | sea | draft | Client (same for Leap Up member and Admin) | FR-auth-access-001, FR-auth-access-002, FR-auth-access-003, FR-auth-access-004, FR-auth-access-005, FR-auth-access-006, FR-auth-access-007, FR-auth-access-008, FR-auth-access-009, FR-auth-access-010 | US-001, US-002 | [login](../html-wireframe/sign-in.html#s1), [login-error](../html-wireframe/sign-in.html#s2), [landing-empty](../html-wireframe/sign-in.html#s3), [landing](../html-wireframe/sign-in.html#s4) | E-auth-access-001, E-auth-access-002, E-auth-access-003, E-auth-access-004 | spec.md#OQ-1, spec.md#OQ-3, spec.md#OQ-6 | P0 | 2026-11-22 |
| 2 | [UC-auth-access-02 Sign out](uc-sign-out.md) | sea | draft | Leap Up member (same for Client and Admin) | FR-auth-access-011 | US-003 | [landing](../html-wireframe/sign-in.html#s4) | — | spec.md#OQ-2 | P0 | 2026-11-22 |

**Coverage:** 11 FR in the spec — 11 covered. 4 error codes — 4 used in extensions.

## Actors

| Actor | Type | Description | Source |
|---|---|---|---|
| Client | primary | Client reviewer assigned to projects | quote P1 #1; board L159 |
| Leap Up member | primary | Leap Up staff assigned to projects | spec §2 |
| Admin | primary | Leap Up admin; sees all projects | spec §2; FR-auth-access-010 |

## CRUD matrix

| UC \ Entity | UserAccount | ProjectMembership |
|---|---|---|
| [UC-01](uc-sign-in-to-my-projects.md) | R | R |
| [UC-02](uc-sign-out.md) | R |  |

Entities from spec §8.

## Relationships

None stated in the spec.

## Sources

- [SRS spec](../srs/auth-access-spec.md) · [User flow](../srs/auth-access-userflow.md) · [Stories](../userstories/auth-access-story-index.md) · [Diagrams](../srs/auth-access-flows.md)
