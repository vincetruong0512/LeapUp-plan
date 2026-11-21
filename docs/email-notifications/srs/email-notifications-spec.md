---
type: srs
feature: email-notifications
scope: P2
status: draft
updated: 2026-11-22
links:
  - docs/email-notifications/brainstorms/email-notifications.md
  - docs/_sources/2026-11-21-leapup-references/bao-gia-leapup-mvp.md
---

# email-notifications — Software Requirements Specification

## 1. Scope

E-mail on new video, new comment and approval. P2 — quote P2 #4. No UI on the board.

## 2. Actors & Stakeholders

| Actor | Type | Goal | In scope? |
|-------|------|------|-----------|
| Client | person | Be told about new videos (and approvals — OQ-2) | Yes |
| Leap Up member | person | Be told about comments and approvals | Yes |
| E-mail service (free tier) | external | Deliver mail (quote §5) | Yes |

## 3. Functional Requirements (FR)

| ID | Title | Description | Scope | Priority | Verify by | Source |
|----|-------|-------------|-------|----------|-----------|--------|
| FR-email-notifications-001 | New video e-mail | When a new video version is added to a project, the system shall e-mail the recipients (TBD, OQ-2). | P2 | P0 | test | quote P2 #4 |
| FR-email-notifications-002 | New comment e-mail | When a comment is added in Video Review, the system shall e-mail the recipients (TBD). | P2 | P0 | test | quote P2 #4 |
| FR-email-notifications-003 | Approval e-mail | When an approval is recorded (version / final — OQ-7), the system shall e-mail the recipients (TBD). | P2 | P0 | test | quote P2 #4 |
| FR-email-notifications-004 | Project-scoped recipients | Only members of the project receive its e-mails. | P2 | P0 | test | board L146 |
| FR-email-notifications-005 | E-mail address on account | User accounts hold an e-mail address for notifications (OQ-1). | P2 | P0 | inspection | inferred from quote P1 #1 (login by User ID) |

## 4. Non-Functional Requirements (NFR)

| ID | Category | Requirement | Priority | Acceptance |
|----|----------|-------------|----------|------------|
| NFR-email-notifications-001 | cost | Sending stays within the free tier for ~50 users. | P1 | quote §5 |
| NFR-email-notifications-002 | language | E-mails in English. | P1 | quote §7 |
| NFR-email-notifications-003 | timeliness | Delay from event to e-mail. | — | TBD — Leap Up |

## 5. Business Rules

| ID | Rule | Trigger | Implements FR | Source |
|----|------|---------|---------------|--------|
| BR-email-notifications-001 | Only the three triggers send e-mail. | Any event | FR-001…003 | quote P2 #4 |
| BR-email-notifications-002 | No in-app notifications. | — | — | quote §7 |

## 6. Error Matrix

| Error ID | Title | Trigger | Severity | Related FR | Wording (exact) | Screen state | Recovery |
|----------|-------|---------|----------|------------|-----------------|--------------|----------|
| E-email-notifications-001 | Send failed | E-mail service error | major | FR-001…003 | n/a (no UI) | — | TBD (OQ-6) |
| E-email-notifications-002 | No address | Recipient without e-mail | minor | FR-005 | n/a | — | Skip; admin adds address |

## 7. Success Criteria

| ID | Business outcome | Measured by | Target |
|----|------------------|-------------|--------|
| SC-email-notifications-01 | Clients hear about new videos without checking the portal | Test e-mail per trigger | 3 of 3 triggers send |

## 8. Data Entities (summary)

- **Notification log (assumed):** event, recipient, sent at, result.

## 9. Flows (summary)

Event → recipients → send → (fail → TBD).

## 10. Screens (summary)

None on the board. E-mail templates TBD.

## 11. Constraints, Dependencies & Assumptions

| Dependency | Owner | Blocks if not ready |
|------------|-------|---------------------|
| Video versions, comments, approvals exist | `video-review`, `outcome-approval` | Triggers |
| E-mail field on accounts | `admin` | Recipients |

## 12. Open Questions

- [ ] OQ-1: E-mail address on accounts.
- [ ] OQ-2: Recipients per trigger.
- [ ] OQ-3: Content and link target.
- [ ] OQ-4: Batching.
- [ ] OQ-5: Opt-out.
- [ ] OQ-6: Failure handling.
- [ ] OQ-7: Which approvals.
