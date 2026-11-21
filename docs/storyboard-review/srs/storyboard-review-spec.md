---
type: srs
feature: storyboard-review
scope: OUT
status: draft
updated: 2026-11-22
links:
  - docs/storyboard-review/brainstorms/storyboard-review.md
  - docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md
---

# storyboard-review — Software Requirements Specification

## 1. Scope

Storyboard Review (board section "MATERIAL | DETAIL SCRIPT & STORY BOARD", screen 06, L425–L479). **OUT — excluded by quote §7; change request per quote §6.** Specified so the board design is not lost.

## 2. Actors & Stakeholders

| Actor | Type | Goal | In scope? |
|-------|------|------|-----------|
| Client | person | Approve or comment on shots; approve the storyboard | OUT (CR) |
| Leap Up member | person | Share and revise storyboard versions | OUT (CR) |

## 3. Functional Requirements (FR)

| ID | Title | Description | Scope | Priority | Verify by | Source |
|----|-------|-------------|-------|----------|-----------|--------|
| FR-storyboard-review-001 | Header | Breadcrumb "Projects / {project} / Material / Storyboard", title "Material / Storyboard Review", "Version {n} · {status} \| Feedback due {date}, {time}", button "Approve storyboard". | OUT | P0 | demo | L426–L429 |
| FR-storyboard-review-002 | Sidebar | Dashboard, Projects, Files, "{project} · PROJECT". | OUT | P1 | demo | L430–L433, L442 |
| FR-storyboard-review-003 | Tabs | Tabs Script, Storyboard, Voice & Music (inferred from L431); Script and Voice & Music content TBD (OQ-2). | OUT | P1 | demo | L431 |
| FR-storyboard-review-004 | Count tiles | Show number of shots with total length ("Shots · 30s"), Approved, Needs change, Waiting review. | OUT | P0 | demo | L434–L441 |
| FR-storyboard-review-005 | Frame cards | Each frame: "FRAME {nn}", "Shot {nn} · {start}–{end}", description, frame image, status, Approve and Comment buttons. | OUT | P0 | demo | L443–L478 |
| FR-storyboard-review-006 | Frame status | Frame status is In review, Approved or Needs change. | OUT | P0 | demo | L452–L454, L470–L472 |
| FR-storyboard-review-007 | Approve a frame | Client approves a frame; its status becomes Approved and the counts update. | OUT | P0 | demo | L455, L435 |
| FR-storyboard-review-008 | Comment on a frame | Client comments on a frame. Effect on status (Needs change?) TBD (OQ-4). | OUT | P0 | demo | L456, L436 |
| FR-storyboard-review-009 | Approve storyboard | "Approve storyboard" approves the version and locks script, shots and VO. Pre-conditions TBD (OQ-3). | OUT | P0 | demo | L428, L479 |
| FR-storyboard-review-010 | New revision after lock | After approval, further changes start a new revision (version number increases). | OUT | P0 | demo | L479, L429 |
| FR-storyboard-review-011 | Feedback due | Show the feedback due date and time of the version. | OUT | P1 | demo | L429 |
| FR-storyboard-review-012 | Project-scoped | Only project members see the storyboard. | OUT | P0 | test | auth-access FR-009 |

## 4. Non-Functional Requirements (NFR)

| ID | Category | Requirement | Priority | Acceptance |
|----|----------|-------------|----------|------------|
| NFR-storyboard-review-001 | audit | Storyboard approval records who and when. | P0 | Approval visible in the approval log (cf. L358) |
| NFR-storyboard-review-002 | usability | Usable in a phone browser. | P0 | quote §7 |

## 5. Business Rules

| ID | Rule | Trigger | Implements FR | Source |
|----|------|---------|---------------|--------|
| BR-storyboard-review-001 | Approving the storyboard locks script, shots and VO. | Approve storyboard | FR-storyboard-review-009 | L479 |
| BR-storyboard-review-002 | Changes after the lock start a new revision. | Change after approval | FR-storyboard-review-010 | L479 |
| BR-storyboard-review-003 | Frame status ∈ {In review, Approved, Needs change}. | Status change | FR-storyboard-review-006 | L452–L472 |

## 6. Error Matrix

| Error ID | Title | Trigger | Severity | Related FR | Wording (exact) | Screen state | Recovery |
|----------|-------|---------|----------|------------|-----------------|--------------|----------|
| E-storyboard-review-001 | Frames not settled | Approve storyboard while frames are not approved (rule TBD) | major | FR-storyboard-review-009 | TBD | Unchanged | Settle frames |
| E-storyboard-review-002 | Empty comment | Comment saved without text | minor | FR-storyboard-review-008 | TBD | Form stays | Write comment |
| E-storyboard-review-003 | Locked | Edit after the storyboard is approved | major | FR-storyboard-review-010 | TBD | Unchanged | Start a new revision |
| E-storyboard-review-004 | Not allowed to approve | Non-approver approves (C4) | major | FR-storyboard-review-009 | TBD | Unchanged | — |

## 7. Success Criteria

| ID | Business outcome | Measured by | Target |
|----|------------------|-------------|--------|
| SC-storyboard-review-01 | Storyboard approved in the portal with a lock and record | Demo | Works end to end |

## 8. Data Entities (summary)

- **StoryboardVersion:** project, version number, status, feedback due, approved by/at, locked.
- **Frame:** version, number, shot start/end, description, image, status.
- **FrameComment:** frame, author, text, date.

## 9. Flows (summary)

Open version → approve / comment per frame → approve storyboard → locked → later change → new revision.

## 10. Screens (summary)

| Screen | Board |
|---|---|
| Material / Storyboard Review (Storyboard tab) | 06 (L425–L479) |
| Script tab, Voice & Music tab | tab labels only (L431) — TBD |

## 11. Constraints, Dependencies & Assumptions

| Constraint | Source / Owner |
|------------|----------------|
| Not in the contract; needs a change request | quote §6, §7 |

| Dependency | Owner | Blocks if not ready |
|------------|-------|---------------------|
| Change request ordered | Leap Up | Everything |
| Approver rule (C4) | Leap Up | FR-009 |

## 12. Open Questions

- [ ] OQ-1 (C1): Ordered as a change request?
- [ ] OQ-2: Script and Voice & Music tab content.
- [ ] OQ-3: Approve storyboard with unsettled frames?
- [ ] OQ-4: Effect of Comment on frame status; where comments show.
- [ ] OQ-5: Who uploads frames; how a new version starts.
- [ ] OQ-6 (C4): Who may approve.
- [ ] OQ-7 (C6): After the feedback due time.
- [ ] OQ-8: Wording E-storyboard-review-001…004.
