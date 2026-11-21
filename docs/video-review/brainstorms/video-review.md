---
type: brainstorm
feature: video-review
scope: MVP
status: draft
updated: 2026-11-22
links:
  - docs/_sources/2026-11-21-leapup-references/bao-gia-leapup-mvp.md
  - docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md
  - docs/_sources/2026-11-21-leapup-references/_comparison.md
---

# Video Review — Brainstorm

## 0. Scope

**Tag:** MVP — "Xem video trực tuyến, comment gắn timecode, marker trên thanh thời gian, quản lý round và version" (quote p.1, P1 #3). Board 07 "Outcome Review — Video Review" (L10–L193).

**Open decisions:** who resolves comments (portal OQ-12); how a round ends without Phase 2 approval (portal OQ-13); round vs version model. Approval of a version and final sign-off are Phase 2 (`outcome-approval`).

## 1. Idea Seed

> "Xem video trực tuyến, comment gắn timecode, marker trên thanh thời gian, quản lý round và version" (quote P1 #3)

The client plays a video in the browser and pins feedback to exact timecodes; Leap Up tracks the feedback round by round.

## 2. Context

- Screen layout (board 07): sidebar Dashboard / Projects / Files / **Outcome Review** (L23, L31, L47, L51); breadcrumb "Projects / 711 / Outcome Development / Video Review" (L10); title "Video Review" (L12); pill "Round 2" (L17); "711 | Social Campaign Film 30s" (L22); subtitle "Review video, pin feedback to exact timecodes, and track revisions" (L26).
- **VERSION HISTORY** (L42): Round 1 "Reviewed | 15 Nov", Round 2 "In Review | 20 Nov", Round 3 "Upcoming | Pending" (L38–L45).
- **Player:** "VIDEO PREVIEW / 711_FILM_R2_V02.mp4" (L56), "VIDEO FRAME" (L85), "30-second campaign film" (L91), three markers (L57–L59) at 00:08, 00:15, 00:23 (L136–L138), controls "▶ 00:15 / 00:30 Volume Fullscreen" (L145).
- **TIMECODE COMMENTS** (L55): "3 comments | Round 2" (L66); each comment = timecode chip, author side (Client / Leap Up), text, status Open / Resolved (L75–L131); input "Add comment at 00:15..." (L147).
- **ROUND CHANGE LOG** (L169): per round a "what changed" line and a status line (L180–L193).
- The file name includes round and version: "R2_V02" (L56). The video file appears in the Outcome Development folder with status "In Review" (L160–L164).

## 3. User Types

| User Type | Pain Point | Primary Need |
|-----------|-----------|--------------|
| Client | Hard to point to the exact moment to change | Pin a comment to a timecode |
| Leap Up member | Feedback per round gets lost | See all comments per round, resolve them, log changes |

## 4. Capabilities Breakdown

### P0 — must have
- Play the video online with play, time, volume, fullscreen (L145).
- Add a comment at the current timecode (L147).
- Show each comment as a marker on the timeline at its timecode (L57–L59, L136–L138).
- Comment list with timecode, author side, text, status Open / Resolved (L75–L131).
- Rounds with status Reviewed / In Review / Upcoming and date (L38–L45).
- Round change log (L169–L193).
- Version of the video per round (quote "version"; file name L56).

### TBD
- Who marks a comment Resolved; can it be re-opened (OQ-2).
- How a new round / version is created and who uploads it (OQ-3).
- How a round moves to "Reviewed" in the MVP (OQ-4).
- Who writes the round change log text (OQ-5).
- Click a marker or a timecode chip → jump the player (inferred — OQ-6).
- Edit / delete a comment; replies (OQ-7).

### Phase 2
- "Awaiting client approval" (L192) and approval → `outcome-approval`.

## 5. Core Flows (Happy Path)

### 5.1 Review a round
1. User opens Video Review for the project (entry: sidebar "Outcome Review" L51 or a video in Outcome Development — OQ-1).
2. The current round is shown (pill "Round 2", L17) with its video in the player (L56).
3. User plays the video and pauses at a moment; the comment box shows "Add comment at {time}..." (L147).
4. User types and submits; the comment appears in the list with timecode, author side and status "Open" (L75–L80), and a marker appears on the timeline (L57).
5. Comment count updates ("3 comments | Round 2", L66).

### 5.2 Handle feedback
1. Leap Up reads Open comments; marks handled comments "Resolved" (L131) — who exactly TBD (OQ-2).
2. Leap Up records what changed for the round in the change log (L188) — how TBD (OQ-5).
3. Leap Up provides the next version / round (OQ-3); the previous round becomes "Reviewed" (L43).

```
┌────────────────┐  play / pause  ┌──────────────────────┐ submit ┌──────────────────────┐
│ Video Review   │ ─────────────▶ │ "Add comment at      │ ─────▶ │ Comment (Open) in    │
│ round N (L17)  │                │  {time}..." (L147)   │        │ list + marker on bar │
└──────┬─────────┘                └──────────┬───────────┘        └──────────┬───────────┘
       │                                     │ empty → no submit (wording TBD)│
       │ select another round (L38–L40)                                       ▼
       ▼                                                          ┌──────────────────────┐
┌────────────────┐                                                │ Leap Up: Resolved    │
│ Older round,   │                                                │ (who — TBD); log     │
│ read-only? TBD │                                                │ change; next round   │
└────────────────┘                                                └──────────────────────┘
```

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | When | YES | NO |
|---|---|---|---|
| D1 | Comment text entered? | Save at current timecode | No submit, wording TBD |
| D2 | Round is the current one? | Comments allowed | Older round: comments allowed? TBD (OQ-8) |
| D3 | Video playable? | Play | Error, wording TBD (E) |

### 6.2 Scenario Matrix

| Action | Leap Up member | Client |
|---|---|---|
| Play video | Yes | Yes |
| Add comment | Yes (L118) | Yes (L75) |
| Mark Resolved | TBD (OQ-2) | TBD (OQ-2) |
| Add version / round | TBD (OQ-3) | No (assumed) |

### 6.3 State Transitions

```
Comment:  Open ──▶ Resolved                          (L80, L131) — who/reversible TBD
Round:    Upcoming ──▶ In Review ──▶ Reviewed        (L43–L45) — triggers TBD
```

### 6.4 Interrupted Transactions

| Situation | Keeps | Resume |
|---|---|---|
| Comment typed, session expires | TBD (auth-access OQ-15) | — |
| Network drops while playing | Player stops; TBD | Play again |

## 7. Validation, Limits & Wording

| Item | Rule |
|---|---|
| Comment text | Required; max length TBD |
| Timecode | Taken from the player position, format mm:ss (L76) |
| Video formats / size | TBD (project-files OQ-8); sample .mp4 (L56) |

Board wording used: "Video Review", "Round 2", "VERSION HISTORY", "VIDEO PREVIEW", "TIMECODE COMMENTS", "Add comment at 00:15...", "ROUND CHANGE LOG", "Open", "Resolved", "Reviewed", "In Review", "Upcoming", "Pending". Error/empty wording: TBD.

## 8. Assumptions

- One video per round is shown in the player (board shows one).
- Board content (round dates, comments, file name) is sample data.

## 9. Risks

| Risk | Likelihood | Consequence | Prevention |
|---|---|---|---|
| R1 Round vs version model unclear | often | Rework of the data model; P2 approval depends on it | Leap Up confirms OQ-3 before build |
| R2 Large video playback slow on phones | sometimes | Reviews delayed | Playback target TBD (NFR) |

## 10. Success Criteria

- The client pins a comment at a timecode and Leap Up sees it as a marker in the same round (MVP outcome).

## 11. Open Points

* [ ] OQ-1: Entry to Video Review — sidebar "Outcome Review" (L51), from a file, or both? TBD.
* [ ] OQ-2: Who marks Resolved; re-open? (portal OQ-12). TBD.
* [ ] OQ-3: Round vs version — how a new version/round is added, by whom (no control drawn). TBD.
* [ ] OQ-4: When a round becomes "Reviewed" in Phase 1 (portal OQ-13). TBD.
* [ ] OQ-5: Who writes the round change log, and is it free text? TBD.
* [ ] OQ-6: Clicking a marker/timecode jumps the player? TBD.
* [ ] OQ-7: Edit/delete comments; replies. TBD.
* [ ] OQ-8: Comments on older rounds allowed? TBD.
* [ ] OQ-9: Phone layout of player + comments (quote §7). TBD.
* [ ] OQ-10: Wording for empty comment, playback error, no comments yet. TBD.

## 12. Next Steps

* `/srs video-review`
