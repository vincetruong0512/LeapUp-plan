---
type: brainstorm
feature: production-timeline
scope: P2
status: draft
updated: 2026-11-22
links:
  - docs/_sources/2026-11-21-leapup-references/bao-gia-leapup-mvp.md
  - docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md
  - docs/_sources/2026-11-21-leapup-references/_comparison.md
---

# Production Timeline — Brainstorm

## 0. Scope

**Tag:** P2 — "5 giai đoạn sản xuất và milestone của project" (quote p.1, P2 #2). Board 04 "Proposal / Production Timeline" (L197–L350).

**OPEN (C6):** the board also shows **Client Inputs** (Received / Missing + "Upload inputs", L255–L299) and a **Feedback Rule** box (L318–L346), not listed in the quote. They are kept as on the board and marked OPEN — not decided here.

## 1. Idea Seed

> "5 giai đoạn sản xuất và milestone của project" (quote P2 #2)

## 2. Context

- Sidebar Dashboard / Projects / Files / "711 · PROJECT" (L209–L239); breadcrumb "Projects / 711 / Proposal / Timeline" (L197); title "Proposal / Production Timeline" (L205); "711 | Social Campaign Film 30s | Due 15 Dec 2026" (L207).
- **PRODUCTION STAGES** (L216): five cards — number + status (01 DONE, 02 CLIENT REVIEW, 03 UP NEXT, 04/05 NOT STARTED), stage name (Brief & Inputs, Script & Storyboard, AI Generation, Edit & Post, Delivery), date range (L225–L244).
- **Milestones** (L256): MILESTONE, OWNER, DUE, STATUS (L265–L268); 9 sample rows, statuses Done, Waiting, Pending, Not started (L275–L350).
- **Client Inputs** (L255): items with Received / Missing; "Upload inputs" (L263–L299). OPEN C6.
- **FEEDBACK RULE** (L318): "Consolidated feedback within 2 working days per round. Late feedback shifts delivery. Final approver: Client" (L328–L346). OPEN C6.

## 3. User Types

| User Type | Need |
|---|---|
| Leap Up member | Plan and update stages and milestones |
| Client | See where the project is and what is due from them |

## 4. Capabilities Breakdown

### P0 (Phase 2, quote)
- Five production stages with status and date range.
- Milestones table with owner, due date, status.

### OPEN (C6 — on board, not in quote)
- Client Inputs checklist and "Upload inputs".
- Feedback Rule box.

### TBD
- Are the five stage names fixed for every project? (OQ-1)
- Who edits stages and milestones; controls not drawn (OQ-2).
- Stage and milestone status transitions (OQ-3).

## 5. Core Flows

1. User opens the project's Timeline (entry: Proposal area / breadcrumb L197 — OQ-4).
2. Sees the five stages, milestones, client inputs (C6) and feedback rule (C6).
3. Leap Up updates a stage status or a milestone (control TBD — OQ-2).
4. Client uploads a missing input with "Upload inputs" (C6 — OQ-5).

```
┌──────────────┐ open ┌──────────────────────────────┐ edit (TBD) ┌─────────────────────┐
│ Project      │ ───▶ │ Production Timeline          │ ─────────▶ │ Stage / milestone   │
│              │      │ 5 stages · milestones ·      │            │ status updated      │
└──────────────┘      │ client inputs (C6) · rule(C6)│            └─────────────────────┘
                      └──────────────┬───────────────┘
                                     │ Upload inputs (C6)
                                     ▼
                      ┌──────────────────────────────┐
                      │ Input Missing → Received     │
                      └──────────────────────────────┘
```

## 6. System Behavior Deep Dive

```
Stage:      NOT STARTED ──▶ UP NEXT ──▶ CLIENT REVIEW ──▶ DONE   (values L225–L229; order inferred — OQ-3)
Milestone:  Not started · Pending · Waiting · Done               (L278–L350; meaning/order TBD — OQ-3)
Input:      Missing ──▶ Received                                 (L264, L286; C6)
```

## 7. Validation & Wording

Board wording kept as is (stage labels, column headers, statuses, Feedback Rule text). Date formats as on the board ("03–07 Nov", "07 Nov"). Error/empty wording TBD.

## 8. Assumptions

- Board dates and items are sample data (L196).

## 9. Risks

| Risk | Likelihood | Consequence | Prevention |
|---|---|---|---|
| R1 C6 items treated as in scope without agreement | often | Change request dispute | Resolve C6 with Leap Up |

## 10. Success Criteria

- The client can see the current production stage and next milestones of their project.

## 11. Open Points

* [ ] OQ-1: Fixed five stage names for every project? TBD.
* [ ] OQ-2: Who edits stages/milestones; edit controls (not drawn). TBD.
* [ ] OQ-3: Stage and milestone status transitions and meanings. TBD.
* [ ] OQ-4: Entry point (Proposal area vs project tab). TBD.
* [ ] OQ-5 (C6): Client Inputs + Upload inputs — in scope? where do uploads go? TBD.
* [ ] OQ-6 (C6): Feedback Rule box — static text or configurable? TBD.
* [ ] OQ-7: Phone layout. TBD.
