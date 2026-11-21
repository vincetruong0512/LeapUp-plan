---
type: brainstorm
feature: material-library
scope: OUT
status: draft
updated: 2026-11-22
links:
  - docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md
  - docs/_sources/2026-11-21-leapup-references/bao-gia-leapup-mvp.md
  - docs/_sources/2026-11-21-leapup-references/_comparison.md
---

# Material Library (board section "MARTERIAL ALIGNMENT") — Brainstorm

## 0. Scope

**Tag:** OUT — the quote excludes it: "Chưa bao gồm: Material Library, Storyboard Review…" (quote §7). Building it is a change request, estimated and quoted separately (quote §6). Documented in full at the BA's request (2026-11-22) so no board information is lost.

**Board:** column "PROJECT DEMO" (L4), section bar "MARTERIAL ALIGNMENT" (L366, typo on the board), screen 05 (L367–L424). Open item C1 (client aware it is not quoted).

## 1. Idea Seed

> "CHARACTERS / OPTION REVIEW — Choose one preferred character direction. Leave feedback on each option." (L372–L373)

The client compares visual options per material category (characters, backgrounds, props…), gives feedback on each option, picks a preferred direction and submits it for approval.

## 2. Context (everything on board 05)

- **Header:** breadcrumb "Projects / 711 / Material" (L367); "711 / Material Library" (L368); title "Material Library" (L369); dark button "Approval Summary 04" (L370).
- **MATERIAL CATEGORIES** (L371), category list with counts — "Characters" highlighted (board visual): Pending Approval 04 (L374–L375) · Backgrounds 13 (L378–L379) · Characters 17 (L384–L385) · Props 60 (L390–L391) · Pending Generation 06 (L396–L397) · Scripts 10 (L400–L401).
- **Section:** "CHARACTERS / OPTION REVIEW" (L372) · "Choose one preferred character direction. Leave feedback on each option." (L373).
- **Four option cards** (2×2, photos in the image only):

| Card | Type label | Name | Status | "Feedback" note | Action | Link | Visual |
|---|---|---|---|---|---|---|---|
| A | CHARACTER (L376) | Character - lifestyle pose (L380) | Selected (L382) | Use as main direction (L386, L388) | Selected Option A (L392) | Details / Feedback (L394) | Demo visual \| Replace with uploaded assets (L398) |
| B | POSING WITH PRODUCT (L377) | Character - product pose (L381) | In Review (L383) | Adjust expression (L387, L389) | Select Option B (L393) | Details / Feedback (L395) | same (L399) |
| C | BACKGROUND (L402) | Convenience store scene (L404) | New (L406) | Background direction (L409, L413) | Select Option C (L417) | Details / Feedback (L419) | same (L421) |
| D | PACKSHOT (L403) | Product and prop kit (L405) | New (L407) | Props direction (L410, L414) | Select Option D (L418) | Details / Feedback (L420) | same (L422) |

- **REVIEW GUIDE** (L408): Compare visual options (L411) · Select preferred direction (L412) · Add feedback per option (L415) · Submit for approval (L416).
- **APPROVAL WORKFLOW** (L423): "Option submitted → Client feedback → Revision → Approved" (L424).
- **Elsewhere on the board:** Action Required item "Character Option A · 711 · Material Library · Select visual direction and approve · Due: 21 Nov 2026, 17:00 · Review Now" (L208–L215); Project Files folder "Material — Client brief, brand assets / References" (L53, L64, L71) is a different thing (files, MVP).
- Board values are sample data (L196).

## 3. User Types

| User Type | Need |
|---|---|
| Client | Compare options, give feedback, choose a direction, submit for approval |
| Leap Up member | Put options (with uploaded visuals) in front of the client; revise after feedback |

## 4. Capabilities (all OUT)

- Category list with counts; option review per category; option cards with status; feedback per option; select preferred option; submit for approval; approval summary; replace demo visuals with uploaded assets; approval workflow states.

## 5. Core Flow

1. Client opens Material Library (from the project's Material area, L367, or Action Required "Review Now", L212).
2. Client picks a category (e.g. Characters, L384).
3. Portal shows "{CATEGORY} / OPTION REVIEW", the instruction and the option cards.
4. Client compares options, opens "Details / Feedback" and leaves feedback per option.
5. Client selects the preferred option ("Select Option B" → "Selected Option B").
6. Client submits for approval (L416).
7. Leap Up revises; option moves Option submitted → Client feedback → Revision → Approved (L424).

```
┌──────────────┐ category ┌─────────────────────┐ feedback ┌──────────────────┐ select ┌──────────────┐
│ Material     │ ───────▶ │ OPTION REVIEW cards │ ───────▶ │ Details/Feedback │ ─────▶ │ Selected     │
│ Library      │          │ status New/In Review│          │ per option       │        │ Option X     │
└──────────────┘          └─────────────────────┘          └──────────────────┘        └──────┬───────┘
                                                                                              │ Submit for approval
                                                                                              ▼
                                       Option submitted → Client feedback → Revision → Approved (L424)
```

## 6. System Behavior

```
Option status on cards: New · In Review · Selected            (L382, L383, L406, L407)
Approval workflow:      Option submitted → Client feedback → Revision → Approved   (L424)
How card status maps to workflow stage: TBD (OQ-3)
```

## 7. Validation & Wording

All labels as on the board (§2). Error, empty and confirmation wording: TBD.

## 8. Assumptions

- One preferred option per category ("Choose one preferred character direction", L373) — inferred for categories other than Characters.

## 9. Risks

| Risk | Consequence | Prevention |
|---|---|---|
| R1 Client expects this screen in the 2-month delivery (C1) | Dispute at acceptance | Leap Up confirms exclusion or orders a change request |
| R2 Overlap with the Material folder in Project Files | Two places for "material" | Decide the relationship (OQ-8) |

## 10. Success Criteria

- The client chooses a direction per category with feedback recorded, without leaving the portal.

## 11. Open Points

* [ ] OQ-1: Ordered as a change request? (quote §6, §7; C1)
* [ ] OQ-2: Are the six categories fixed? What are "Pending Approval" and "Pending Generation" (categories or filters)?
* [ ] OQ-3: Card status (New / In Review / Selected) vs workflow stages (L424).
* [ ] OQ-4: What "Approval Summary 04" shows.
* [ ] OQ-5: Who uploads option visuals ("Replace with uploaded assets", L398) and how.
* [ ] OQ-6: What "Submit for approval" sends, and who approves (C4).
* [ ] OQ-7: Can a selection be changed after submitting?
* [ ] OQ-8: Relationship with the Project Files "Material" folder.
* [ ] OQ-9: Wording for errors and empty states.
