---
type: srs
feature: video-review
scope: MVP
status: draft
updated: 2026-11-22
links:
  - docs/video-review/brainstorms/video-review.md
  - docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md
---

# video-review — Software Requirements Specification

## 1. Scope

Online video review: player with timeline markers, timecoded comments with Open/Resolved status, rounds with version history and a round change log. MVP — quote P1 #3; board 07 (L10–L193). Approval is Phase 2.

## 2. Actors & Stakeholders

| Actor | Type | Goal | In scope? |
|-------|------|------|-----------|
| Client | person | Give feedback at exact timecodes | Yes |
| Leap Up member | person | Collect and resolve feedback per round | Yes |
| Cloudflare R2 | external | Store and serve video (quote §5) | Yes |

## 3. Functional Requirements (FR)

| ID | Title | Description | Scope | Priority | Verify by | Source |
|----|-------|-------------|-------|----------|-----------|--------|
| FR-video-review-001 | Header | Show breadcrumb "Projects / {project} / Outcome Development / Video Review", title "Video Review", current round pill, "{project} \| {description}", subtitle "Review video, pin feedback to exact timecodes, and track revisions". | MVP | P0 | demo | board L10, L12, L17, L22, L26 |
| FR-video-review-002 | Sidebar | Sidebar Dashboard, Projects, Files, Outcome Review; Outcome Review active. | MVP | P1 | demo | board L23, L31, L47, L51 |
| FR-video-review-003 | Version history | List rounds with status (Reviewed / In Review / Upcoming) and date or "Pending"; the current round is highlighted. | MVP | P0 | demo | board L38–L45 |
| FR-video-review-004 | Video player | Play the round's video online with play/pause, current/total time, volume and fullscreen; show the file name above the player. | MVP | P0 | demo | quote P1 #3; board L56, L85, L91, L145 |
| FR-video-review-005 | Add timecoded comment | User adds a comment; it is pinned to the player's current timecode (moment taken — start or submit — and rounding TBD, OQ-12); input shows "Add comment at {mm:ss}...". Submit control not on the board (OQ-15). | MVP | P0 | demo | quote P1 #3; board L147 |
| FR-video-review-006 | Empty comment | If the comment text is empty, then the system shall not save it (E-video-review-001). | MVP | P0 | test | brainstorm D1 |
| FR-video-review-007 | Timeline markers | Each comment of the round shows as a marker on the timeline at its timecode, with the time label. | MVP | P0 | demo | quote P1 #3; board L57–L59, L136–L138 |
| FR-video-review-008 | Comment list | List the round's comments with timecode chip, author side (Client / Leap Up), text, status; header "{n} comments \| Round {n}". | MVP | P0 | demo | board L55, L66, L75–L131 |
| FR-video-review-009 | Comment status | A comment is Open when created and can be marked Resolved. Who and re-open TBD (OQ-2). | MVP | P0 | demo | board L80, L131 |
| FR-video-review-010 | Rounds and versions | Leap Up provides a new version for a round / starts the next round. Mechanism TBD (OQ-3). | MVP | P0 | demo | quote P1 #3 |
| FR-video-review-011 | Round status | Round status moves Upcoming → In Review → Reviewed. Triggers TBD (OQ-4). | MVP | P0 | demo | board L43–L45 |
| FR-video-review-012 | Round change log | Show per round what changed and its status line. Who edits TBD (OQ-5). | MVP | P0 | demo | board L169–L193 |
| FR-video-review-013 | View another round | **Provisional — TBD pending OQ-6.** Selecting a round in Version History shows that round's video and comments (inferred, not stated in the reference). A round with no video shows E-video-review-004. | MVP | P1 | demo | board L38–L45 |
| FR-video-review-014 | Project-scoped | Only project members can open the review, play its video or add/resolve comments (Admin: TBD, auth-access OQ-10); others get E-auth-access-003. | MVP | P0 | test | auth-access FR-009 |
| FR-video-review-015 | Playback failure | If the video cannot be played, then the system shall show E-video-review-002. | MVP | P1 | test | brainstorm D3 |

## 4. Non-Functional Requirements (NFR)

| ID | Category | Requirement | Priority | Acceptance |
|----|----------|-------------|----------|------------|
| NFR-video-review-001 | storage | Video stored in Cloudflare R2. | P0 | quote §5 |
| NFR-video-review-002 | usability | Review works in a phone browser. | P0 | quote §7; layout TBD (OQ-8) |
| NFR-video-review-003 | performance | Time until playback starts. | — | TBD — Leap Up |
| NFR-video-review-004 | accuracy | Comment timecode equals the player position, to the second. Whether the position is taken when the comment is started or submitted, and how fractions of a second round, is TBD (OQ-12). | P0 | quote §1 "review video theo từng giây" |

## 5. Business Rules

| ID | Rule | Trigger | Implements FR | Source |
|----|------|---------|---------------|--------|
| BR-video-review-001 | Every comment has a timecode and belongs to one round. | Comment saved | FR-video-review-005, FR-video-review-008 | board L66, L147 |
| BR-video-review-002 | A new comment starts as Open. | Comment saved | FR-video-review-009 | board L80 |
| BR-video-review-003 | **Open — not a rule yet.** Whether only one round can be In Review at a time is TBD (OQ-4); the board sample shows one (L43–L45, sample data). | Round status change | FR-video-review-011 | board L43–L45 (sample) |
| BR-video-review-004 | Comment author shows as "Client" or "Leap Up". | Comment shown | FR-video-review-008 | board L75, L118 |

## 6. Error Matrix

| Error ID | Title | Trigger | Severity | Related FR | Wording (exact) | Screen state | Recovery |
|----------|-------|---------|----------|------------|-----------------|--------------|----------|
| E-video-review-001 | Empty comment | Submit without text | minor | FR-video-review-006 | TBD | Input stays | Type text |
| E-video-review-002 | Playback failed | Video can't load | major | FR-video-review-015 | TBD | Player shows error | Retry |
| E-video-review-003 | No comments yet | Round has no comments | minor | FR-video-review-008 | TBD | Empty list | Add a comment |
| E-video-review-004 | No video in round | Round has no video yet (Upcoming) | minor | FR-video-review-010 | TBD | Empty player | Wait for Leap Up |

## 7. Success Criteria

| ID | Business outcome | Measured by | Target |
|----|------------------|-------------|--------|
| SC-video-review-01 | Client feedback is pinned to exact seconds | Demo: comment at 00:15 shows marker at 00:15 | Exact to the second |
| SC-video-review-02 | Leap Up tracks feedback per round | Demo of rounds 1→2 with comments and log | Works end to end |

## 8. Data Entities (summary)

- **Round:** number, status, date, change-log text, status line.
- **Version (video):** file, round, version label (e.g. V02).
- **Comment:** round, version, timecode, author, side, text, status, date.

## 9. Flows (summary)

Open review → play → comment at timecode → marker → resolve → change log → next round.

## 10. Screens (summary)

| Screen | Board |
|---|---|
| Video Review | 07 (L10–L193) |
| Empty / error states | not drawn — TBD |

## 11. Constraints, Dependencies & Assumptions

| Constraint | Source / Owner |
|------------|----------------|
| Online playback, no download required to review | quote P1 #3 |

| Dependency | Owner | Blocks if not ready |
|------------|-------|---------------------|
| Video uploaded to the project | `project-files` | Nothing to review |
| Round/version model compatible with approval | `outcome-approval` (P2) | P2 rework |

| Assumption | Invalidates if wrong |
|------------|----------------------|
| One video per round in the player | FR-video-review-004 |

## 12. Open Questions

- [ ] OQ-1: Entry to Video Review.
- [ ] OQ-2: Who resolves comments; re-open.
- [ ] OQ-3: Round vs version; how a new version/round is added (no control drawn).
- [ ] OQ-4: Round status triggers in Phase 1.
- [ ] OQ-5: Change-log editing.
- [ ] OQ-6: Marker/timecode click and round selection behaviour.
- [ ] OQ-7: Edit/delete/reply to comments.
- [ ] OQ-8: Phone layout.
- [ ] OQ-9: Wording E-video-review-001…004.
- [ ] OQ-10: File ↔ review link — is a version the same record as the Outcome Development file; status sync; comments when the file is replaced; can Material videos be reviewed? Shared with project-files OQ-17 (review SBA-12). Before Sprint 1.
- [ ] OQ-11: May users comment on a past (Reviewed) round, an Upcoming round with no video, or a replaced version? (brainstorm OQ-8, portal OQ-13; restored by review SBA-13).
- [ ] OQ-12: Timecode capture — moment the comment is started or submitted while the video keeps playing; rounding of fractional seconds (review SBA-23, QA-6).
- [ ] OQ-13: Which status lines the round change log can show in Phase 1 — board text such as "Awaiting client approval" (L192) belongs to Outcome Approval (P2) (review SBA-10, QA-4).
- [ ] OQ-14: Without realtime updates (quote §7), how do users see comments or resolves made by others at the same time — on reload? Two people resolving the same comment? (portal OQ-15; review SBA-16).
- [ ] OQ-15: Comment submit control — Enter key or a button; not on the board (L147) (review UX-8).
