---
type: usecase-index
feature: email-notifications
status: draft
updated: 2026-11-22
links:
  - docs/email-notifications/srs/email-notifications-spec.md
---

# E-mail Notifications — Use Cases Index

Built from the draft SRS, user flow and user stories; nothing added beyond them. Open questions stay in the spec (§12).

## Use cases

| # | Use case | Level | Status | Primary actor | Covers FR | Stories | Screens | Errors (E-*) | OQ ref | Priority | Updated |
|---|----------|-------|--------|---------------|-----------|---------|---------|--------------|--------|----------|---------|
| 1 | [UC-email-notifications-01 Notify project members by e-mail](uc-notify-project-members-by-email.md) | sea | draft | Client or Leap Up member (recipient) | FR-email-notifications-001, FR-email-notifications-002, FR-email-notifications-003, FR-email-notifications-004, FR-email-notifications-005 | US-001, US-002, US-003 | — | E-email-notifications-001, E-email-notifications-002 | spec.md#OQ-1, spec.md#OQ-2, spec.md#OQ-3, spec.md#OQ-6, spec.md#OQ-7 | P0 | 2026-11-22 |

**Coverage:** 5 FR in the spec — 5 covered. 2 error codes — 2 used in extensions.

## Actors

| Actor | Type | Description | Source |
|---|---|---|---|
| Client | primary | Recipient — told about new videos (other triggers TBD) | quote P2 #4 |
| Leap Up member | primary | Recipient — told about comments and approvals | quote P2 #4 |
| E-mail service | system | Free-tier sending service | quote §5 |

## CRUD matrix

| UC \ Entity | NotificationLog |
|---|---|
| [UC-01](uc-notify-project-members-by-email.md) | C |

Entities from spec §8.

## Relationships

None stated in the spec.

## Sources

- [SRS spec](../srs/email-notifications-spec.md) · [User flow](../srs/email-notifications-userflow.md) · [Stories](../userstories/email-notifications-story-index.md) · [Diagrams](../srs/email-notifications-flows.md)
