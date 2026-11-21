---
type: brainstorm
feature: outcome-approval
scope: P2
status: draft
updated: 2026-11-22
links:
  - docs/_sources/2026-11-21-leapup-references/bao-gia-leapup-mvp.md
  - docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md
  - docs/_sources/2026-11-21-leapup-references/_comparison.md
---

# Outcome Approval — Revision & Sign-off — Brainstorm

## 0. Scope

**Tag:** P2 — "Duyệt từng version, change request, lịch sử phê duyệt, ký duyệt bản cuối" (quote p.1, P2 #3). Board 08 "Outcome Development / Revision & Sign-off" (L214–L365).

**OPEN items on this screen:** C4 approvers list (L246–L271; MVP roles decided as Admin / Leap Up member / Client — named approvers are not roles), C5 revision quota + change-request cost (L245–L274, L294–L333), C9 final sign-off checklist (L354–L360). Kept as on the board, marked OPEN.

## 1. Idea Seed

> "Duyệt từng version, change request, lịch sử phê duyệt, ký duyệt bản cuối" (quote P2 #3)

## 2. Context

- Sidebar with "711 · PROJECT" (L232–L257); breadcrumb "Projects / 711 / Outcome Development / Revision" (L214); title "Outcome Development / Revision & Sign-off" (L218); "711 | Social Campaign Film 30s" (L230).
- **Revision Rounds** (L245): Included 2, Used 1, Remaining 1 (L250–L260); note "Round 3 onwards: additional scope & cost" / "Client confirms before work starts." (L270, L274). OPEN C5.
- **Approvers** (L246): CLIENT Brand Manager · Final approver; CLIENT Marketing Exec · Reviewer; LEAP UP Account · Consolidates feedback; LEAP UP Producer · Internal QC (L248–L271). OPEN C4.
- **Change Requests** (L287): REQUEST, ROUND, SCOPE, COST, STATUS (L294–L298); scope In scope / Out of scope; cost "—" or "TBD"; status Done, Quote sent, Client approved (L304–L333). Cost OPEN C5.
- **FINAL SIGN-OFF** (L345): file name (L351), three checkboxes "Visuals, VO & music approved", "Mandatory copy & legal checked", "Delivery formats confirmed" (L354–L360, OPEN C9), button "Approve final version" (L365).
- **Approval Log** (L344): event + date; "Final sign-off — Pending" (L352–L364).
- Video Review round log shows "Awaiting client approval" (L192): the per-version approval point is not drawn on board 08.

## 3. User Types

| User Type | Need |
|---|---|
| Client (final approver — L346 "Final approver: Client") | Approve versions and sign off the final cut |
| Leap Up member | Log change requests, track rounds, see approval history |

## 4. Capabilities Breakdown

### P0 (Phase 2, quote)
- Approve each version (control not drawn — OQ-1).
- Change requests list.
- Approval log (history).
- Final sign-off with "Approve final version".

### OPEN
- Revision round quota (C5), CR cost (C5), approvers list (C4), sign-off checklist (C9).

### TBD
- Who may approve (only Client? a named final approver? — C4) (OQ-2).
- Change request lifecycle and who sets scope/status (OQ-3).
- What final sign-off changes (file status "Final"? project status?) (OQ-4).

## 5. Core Flows

### 5.1 Approve a version
1. Client reviews a version in Video Review (round "Awaiting client approval", L192).
2. Client approves the version (control/location TBD — OQ-1).
3. The approval is added to the Approval Log with date (L352–L362).

### 5.2 Change requests
1. Leap Up (or client — OQ-3) records a change request with round and scope (L304–L321).
2. Out-of-scope requests carry a cost (TBD) and status Quote sent → Client approved (L323, L333) — C5.
3. In-scope requests become Done when delivered (L308).

### 5.3 Final sign-off
1. Client opens Revision & Sign-off; FINAL SIGN-OFF shows the final file (L351).
2. Client ticks the three checks (C9) and presses "Approve final version" (L365).
3. Approval Log shows "Final sign-off" with the date (L363–L364).

```
┌────────────────┐ approve version (TBD) ┌────────────────┐
│ Video Review   │ ────────────────────▶ │ Approval Log   │
│ round awaiting │                       │ entry + date   │
└────────────────┘                       └───────▲────────┘
┌────────────────────┐  all 3 checks? (C9)       │
│ FINAL SIGN-OFF     │ ──YES──▶ Approve final ───┘
│ file + checkboxes  │ ──NO───▶ button disabled? (TBD)
└────────────────────┘
```

## 6. System Behavior Deep Dive

```
Change request:  (new) ──▶ Done                       — in scope (L306–L308)
                 (new) ──▶ Quote sent ──▶ Client approved — out of scope (L321–L333, C5)
Final sign-off:  Pending ──▶ Approved                 (L364)
Revision rounds: Included / Used / Remaining counts   (L250–L260, C5)
```

| ID | When | YES | NO |
|---|---|---|---|
| D1 | All sign-off checks ticked (C9)? | Approve allowed | TBD |
| D2 | Change request in scope? | No cost | Cost + quote (C5) |
| D3 | Rounds remaining > 0? | Next round included | "additional scope & cost" (L270, C5) |

## 7. Validation & Wording

Board wording kept as is. Error/confirmation wording TBD.

## 8. Assumptions

- Board content is sample data; the board file-name mismatch (L56 vs L351) is noted in `_comparison.md` §3.

## 9. Risks

| Risk | Likelihood | Consequence | Prevention |
|---|---|---|---|
| R1 C4/C5/C9 unresolved | often | Approval rules disputed | Resolve with Leap Up before build |
| R2 Sign-off has legal weight | sometimes | Need for a reliable record | Approval Log keeps who and when |

## 10. Success Criteria

- The client signs off the final version and the log records who and when.

## 11. Open Points

* [ ] OQ-1: Where and how a single version is approved (not drawn on board 08). TBD.
* [ ] OQ-2 (C4): Who can approve — any client member or a named final approver; approvers list. TBD.
* [ ] OQ-3: Change request — who creates, edits scope/cost/status; lifecycle. TBD.
* [ ] OQ-4: Effects of final sign-off (file status, project status, lock). TBD.
* [ ] OQ-5 (C5): Revision quota and paid change requests. TBD.
* [ ] OQ-6 (C9): Sign-off checklist items — fixed or per project. TBD.
* [ ] OQ-7: Reject / request changes on a version. TBD.
