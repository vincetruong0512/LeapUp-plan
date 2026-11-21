---
type: brainstorm
feature: email-notifications
scope: P2
status: draft
updated: 2026-11-22
links:
  - docs/_sources/2026-11-21-leapup-references/bao-gia-leapup-mvp.md
  - docs/_sources/2026-11-21-leapup-references/_comparison.md
---

# E-mail Notifications — Brainstorm

## 0. Scope

**Tag:** P2 — "Email khi có video mới, có comment, có phê duyệt" (quote p.1, P2 #4). No board screen (C8). In-app notifications are OUT (quote §7).

## 1. Idea Seed

> "Email khi có video mới, có comment, có phê duyệt" (quote P2 #4)

## 2. Context

- Three triggers only: new video, new comment, new approval.
- E-mail is sent through a free-tier e-mail service (quote §5, free tier).
- Users sign in with a User ID, not an e-mail (quote P1 #1) — so users need an e-mail address on their account to receive mail (OQ-1).

## 3. User Types

| User Type | Need |
|---|---|
| Client | Know when a new video is ready to review |
| Leap Up member | Know when the client comments or approves |

## 4. Capabilities Breakdown

### P0 (Phase 2, quote)
- E-mail on new video.
- E-mail on new comment.
- E-mail on approval.

### TBD
- Recipients per trigger (OQ-2); e-mail address on the account (OQ-1).
- Content, subject, link into the portal (OQ-3).
- Batching (one mail per comment vs summary) (OQ-4).
- Opt-out (OQ-5).

### OUT
- In-app notifications, realtime (quote §7).

## 5. Core Flows

```
┌──────────────┐ event  ┌──────────────────────┐ recipients ┌──────────────────┐
│ New video /  │ ─────▶ │ System picks project │ ─────────▶ │ E-mail sent via  │
│ comment /    │        │ members to notify    │  (TBD)     │ e-mail service   │
│ approval     │        └──────────────────────┘            └────────┬─────────┘
└──────────────┘                                                     │ fails?
                                                                     ▼
                                                          ┌──────────────────────┐
                                                          │ TBD (retry / log)    │
                                                          └──────────────────────┘
```

## 6. System Behavior Deep Dive

| ID | When | YES | NO |
|---|---|---|---|
| D1 | Recipient has an e-mail address? | Send | Skip (assumed) — OQ-1 |
| D2 | E-mail service accepted the message? | Done | TBD (OQ-6) |

## 7. Validation & Wording

Subjects and bodies: TBD (OQ-3). Language: English (quote §7 one language).

## 8. Assumptions

- Only members of the project receive its notifications (project-scoped access, board L146).

## 9. Risks

| Risk | Likelihood | Consequence | Prevention |
|---|---|---|---|
| R1 Too many comment e-mails | often | Users ignore mail | Decide batching (OQ-4) |
| R2 Free-tier sending limit | sometimes | Mails dropped | Check limits for ~50 users (NFR) |

## 10. Success Criteria

- A client receives an e-mail when a new video is available in their project.

## 11. Open Points

* [ ] OQ-1: E-mail address field on user accounts (admin). TBD.
* [ ] OQ-2: Recipients per trigger. TBD.
* [ ] OQ-3: Subject, body, link target. TBD.
* [ ] OQ-4: One e-mail per event or batched. TBD.
* [ ] OQ-5: Opt-out. TBD.
* [ ] OQ-6: Failure handling. TBD.
* [ ] OQ-7: "Approval" — version approval, final sign-off, or both. TBD.
