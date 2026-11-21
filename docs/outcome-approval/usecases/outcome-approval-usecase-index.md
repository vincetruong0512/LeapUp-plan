---
type: usecase-index
feature: outcome-approval
status: draft
updated: 2026-11-22
links:
  - docs/outcome-approval/srs/outcome-approval-spec.md
---

# Outcome Approval — Use Cases Index

Built from the draft SRS, user flow and user stories; nothing added beyond them. Open questions stay in the spec (§12).

## Use cases

| # | Use case | Level | Status | Primary actor | Covers FR | Stories | Screens | Errors (E-*) | OQ ref | Priority | Updated |
|---|----------|-------|--------|---------------|-----------|---------|---------|--------------|--------|----------|---------|
| 1 | [UC-outcome-approval-01 Approve a version](uc-approve-a-version.md) | sea | draft | Client | FR-outcome-approval-002, FR-outcome-approval-005, FR-outcome-approval-010, FR-outcome-approval-011 | US-001 | [revision-signoff](../html-wireframe/approval.html#s1), [approval-not-allowed](../html-wireframe/approval.html#s2) | E-outcome-approval-001 | spec.md#OQ-1, spec.md#OQ-2 | P0 | 2026-11-22 |
| 2 | [UC-outcome-approval-02 Track change requests and revision rounds](uc-track-change-requests.md) | sea | draft | Leap Up member | FR-outcome-approval-001, FR-outcome-approval-003, FR-outcome-approval-004, FR-outcome-approval-008, FR-outcome-approval-009 | US-002, US-004 | [revision-signoff](../html-wireframe/approval.html#s1) | E-outcome-approval-003 | spec.md#OQ-2, spec.md#OQ-3, spec.md#OQ-5 | P0 | 2026-11-22 |
| 3 | [UC-outcome-approval-03 Sign off the final version](uc-sign-off-the-final-version.md) | sea | draft | Client | FR-outcome-approval-005, FR-outcome-approval-006, FR-outcome-approval-007, FR-outcome-approval-010 | US-003 | [revision-signoff](../html-wireframe/approval.html#s1), [signoff-incomplete](../html-wireframe/approval.html#s3) | E-outcome-approval-001, E-outcome-approval-002 | spec.md#OQ-4, spec.md#OQ-6 | P0 | 2026-11-22 |

**Coverage:** 11 FR in the spec — 11 covered. 3 error codes — 3 used in extensions.

## Actors

| Actor | Type | Description | Source |
|---|---|---|---|
| Client | primary | Approves versions; final approver (board L346) | quote P2 #3 |
| Leap Up member | primary | Tracks change requests and approvals | quote P2 #3 |

## CRUD matrix

| UC \ Entity | Approval | ChangeRequest | RevisionQuota |
|---|---|---|---|
| [UC-01](uc-approve-a-version.md) | C |  |  |
| [UC-02](uc-track-change-requests.md) |  | CRU | R |
| [UC-03](uc-sign-off-the-final-version.md) | C |  |  |

Entities from spec §8.

## Relationships

None stated in the spec.

## Sources

- [SRS spec](../srs/outcome-approval-spec.md) · [User flow](../srs/outcome-approval-userflow.md) · [Stories](../userstories/outcome-approval-story-index.md) · [Diagrams](../srs/outcome-approval-flows.md)
