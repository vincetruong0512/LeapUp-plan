---
type: brainstorm
feature: storyboard-review
scope: OUT
status: draft
updated: 2026-11-22
links:
  - docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md
  - docs/_sources/2026-11-21-leapup-references/bao-gia-leapup-mvp.md
  - docs/_sources/2026-11-21-leapup-references/_comparison.md
---

# Storyboard Review (board section "MATERIAL | DETAIL SCRIPT & STORY BOARD") — Brainstorm

## 0. Scope

**Tag:** OUT — excluded by the quote: "Chưa bao gồm: Material Library, Storyboard Review…" (quote §7). Change request, estimated and quoted separately (quote §6). Documented in full at the BA's request (2026-11-22). Open item C1.

**Board:** column "PROJECT DEMO" (L4), section bar "MATERIAL | DETAIL SCRIPT & STORY BOARD" (L425), screen 06 (L426–L479).

## 1. Idea Seed

> "Approving the storyboard locks script, shots and VO. Further changes start a new revision." (L479)

The client reviews a storyboard version frame by frame, approves or comments on each shot, then approves the whole storyboard, which locks script, shots and voice-over.

## 2. Context (everything on board 06)

- **Sidebar:** Dashboard (L430) · Projects (L432) · Files (L433) · "711 · PROJECT" (L442).
- **Header:** breadcrumb "Projects / 711 / Material / Storyboard" (L426); title "Material / Storyboard Review" (L427); "Version 2 · Client Review | Feedback due 21 Nov, 17:00" (L429); green button "Approve storyboard" (L428).
- **Tabs:** "Script Storyboard Voice & Music" (L431) — one board text line; read as three tabs Script / Storyboard / Voice & Music (inferred). Only the Storyboard content is drawn.
- **Count tiles:** 6 "Shots · 30s" (L434, L438) · 2 "Approved" (L435, L439) · 1 "Needs change" (L436, L440) · 3 "Waiting review" (L437, L441).
- **Frames** (2×3 dark frame placeholders, each with Approve / Comment buttons):

| Frame | Shot | Description | Status | Buttons |
|---|---|---|---|---|
| FRAME 01 (L443) | Shot 01 · 0:00–0:04 (L446) | Wide shot: young man enters a 7-Eleven (L449) | Approved (L452) | Approve (L455) · Comment (L456) |
| FRAME 02 (L444) | Shot 02 · 0:04–0:09 (L447) | Close-up: picks up coffee, smiles (L450) | Approved (L453) | Approve (L457) · Comment (L458) |
| FRAME 03 (L445) | Shot 03 · 0:09–0:14 (L448) | Store aisle with snacks and drinks (L451) | Needs change (L454) | Approve (L459) · Comment (L460) |
| FRAME 04 (L461) | Shot 04 · 0:14–0:20 (L464) | Posing with product at counter (L467) | In review (L470) | Approve (L473) · Comment (L474) |
| FRAME 05 (L462) | Shot 05 · 0:20–0:26 (L465) | Packshot: coffee and snack pack (L468) | In review (L471) | Approve (L475) · Comment (L476) |
| FRAME 06 (L463) | Shot 06 · 0:26–0:30 (L466) | End card: logo and tagline (L469) | In review (L472) | Approve (L477) · Comment (L478) |

- **Lock notice** (light-blue box): "Approving the storyboard locks script, shots and VO. Further changes start a new revision." (L479).
- **Elsewhere on the board:** timeline stage "02 CLIENT REVIEW · Script & Storyboard · 10–21 Nov" (L226, L234, L241); milestones "Script V2 approval · Client · 19 Nov · Waiting" and "Storyboard approval · Client · 21 Nov · Pending" (L281–L291); approval log "Script V2 approved 19 Nov", "Storyboard V2 approved 21 Nov" (L355–L359); Feedback Rule "Consolidated feedback within 2 working days per round" (L328–L334).
- Board values are sample data (L196).

## 3. User Types

| User Type | Need |
|---|---|
| Client | Approve or comment per shot; approve the storyboard before production |
| Leap Up member | Share a storyboard version; revise frames that need change |

## 4. Capabilities (all OUT)

- Storyboard version header with status and feedback deadline; tabs Script / Storyboard / Voice & Music; count tiles; frame cards with shot timing, description and status; approve a frame; comment on a frame; approve the storyboard (lock); new revision for later changes.

## 5. Core Flow

1. Client opens Storyboard Review (Material area, breadcrumb L426).
2. Portal shows version, status and feedback due date (L429), counts and frames.
3. For each frame the client presses Approve (→ Approved) or Comment (→ Needs change — inferred).
4. When all frames are settled, the client presses "Approve storyboard" (L428).
5. Script, shots and VO are locked (L479); further changes start a new revision (Version 3).

```
┌───────────────────┐ per frame ┌──────────────┐ Approve ┌──────────┐
│ Storyboard Review │ ────────▶ │ Frame (shot) │ ──────▶ │ Approved │
│ Version 2 · due…  │           │ In review    │ Comment │ Needs    │
└────────┬──────────┘           └──────────────┘ ──────▶ │ change?  │
         │ Approve storyboard                            └──────────┘
         ▼
┌───────────────────────────────────────┐  later change  ┌──────────────────────┐
│ Locked: script, shots, VO (L479)      │ ─────────────▶ │ New revision (V+1)   │
└───────────────────────────────────────┘                └──────────────────────┘
```

## 6. System Behavior

```
Frame status:      In review · Approved · Needs change          (L452–L472)
Storyboard:        Version n · Client Review → approved → locked (L429, L428, L479)
After lock:        change → new revision                          (L479)
```

| ID | When | YES | NO |
|---|---|---|---|
| D1 | Approve storyboard while frames are not all Approved? | TBD (OQ-3) | — |
| D2 | Comment text entered? | Save | Error, TBD |
| D3 | Storyboard locked? | Change starts a new revision | Edit allowed |

## 7. Validation & Wording

All labels as on the board (§2). Error, empty and confirmation wording: TBD.

## 8. Assumptions

- "Comment" on a frame marks it "Needs change" (inferred from the counts) — to confirm (OQ-4).

## 9. Risks

| Risk | Consequence | Prevention |
|---|---|---|
| R1 Expected in the 2-month delivery (C1) | Dispute | Leap Up confirms exclusion or orders a change request |
| R2 Lock has contractual weight | Disputes over later changes | Record who approved and when |

## 10. Success Criteria

- The client approves the storyboard in the portal and later changes start a new revision.

## 11. Open Points

* [ ] OQ-1 (C1): Ordered as a change request?
* [ ] OQ-2: Content of the Script and Voice & Music tabs (only Storyboard is drawn).
* [ ] OQ-3: Can the storyboard be approved while frames are Needs change / In review?
* [ ] OQ-4: Does Comment set "Needs change"? Where are frame comments shown?
* [ ] OQ-5: Who uploads frames and how a new version is created.
* [ ] OQ-6: Who may approve (C4).
* [ ] OQ-7: What happens after the feedback due time (Feedback Rule, C6).
* [ ] OQ-8: Wording for errors and empty states.
