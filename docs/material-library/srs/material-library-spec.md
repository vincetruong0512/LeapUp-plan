---
type: srs
feature: material-library
scope: OUT
status: draft
updated: 2026-11-22
links:
  - docs/material-library/brainstorms/material-library.md
  - docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md
---

# material-library — Software Requirements Specification

## 1. Scope

Material Library (board section "MARTERIAL ALIGNMENT", screen 05, L366–L424). **OUT — excluded by quote §7; change request per quote §6.** Specified so the board design is not lost.

## 2. Actors & Stakeholders

| Actor | Type | Goal | In scope? |
|-------|------|------|-----------|
| Client | person | Choose a visual direction per category with feedback | OUT (CR) |
| Leap Up member | person | Present options and revise them | OUT (CR) |

## 3. Functional Requirements (FR)

| ID | Title | Description | Scope | Priority | Verify by | Source |
|----|-------|-------------|-------|----------|-----------|--------|
| FR-material-library-001 | Header | Breadcrumb "Projects / {project} / Material", "{project} / Material Library", title "Material Library", button "Approval Summary {n}". | OUT | P0 | demo | L367–L370 |
| FR-material-library-002 | Categories with counts | "MATERIAL CATEGORIES" list: Pending Approval, Backgrounds, Characters, Props, Pending Generation, Scripts, each with a count; current category highlighted. | OUT | P0 | demo | L371, L374–L401 |
| FR-material-library-003 | Option review section | Heading "{CATEGORY} / OPTION REVIEW" and instruction, e.g. "Choose one preferred character direction. Leave feedback on each option." | OUT | P0 | demo | L372–L373 |
| FR-material-library-004 | Option cards | Each option shows type label, name, visual, status, "Feedback" note, select action and "Details / Feedback" link. | OUT | P0 | demo | L376–L422 |
| FR-material-library-005 | Option status | Option status is New, In Review or Selected. | OUT | P0 | demo | L382, L383, L406, L407 |
| FR-material-library-006 | Select preferred option | Client selects one option ("Select Option {X}"); it then reads "Selected Option {X}" and status "Selected". | OUT | P0 | demo | L373, L392–L393, L417–L418 |
| FR-material-library-007 | Feedback per option | Client leaves feedback on each option via "Details / Feedback". | OUT | P0 | demo | L373, L394, L415 |
| FR-material-library-008 | Uploaded visuals | Demo visuals are replaced with uploaded assets. Who uploads TBD (OQ-5). | OUT | P0 | demo | L398, L399, L421, L422 |
| FR-material-library-009 | Submit for approval | Client submits the selection for approval. Control TBD (OQ-6). | OUT | P0 | demo | L416 |
| FR-material-library-010 | Approval Summary | "Approval Summary {n}" opens a summary; content TBD (OQ-4). | OUT | P1 | demo | L370 |
| FR-material-library-011 | Approval workflow | Options follow Option submitted → Client feedback → Revision → Approved. | OUT | P0 | demo | L423–L424 |
| FR-material-library-012 | Review guide | Show "REVIEW GUIDE": Compare visual options · Select preferred direction · Add feedback per option · Submit for approval. | OUT | P2 | demo | L408, L411–L416 |
| FR-material-library-013 | Project-scoped | Only project members see the library. | OUT | P0 | test | auth-access FR-009 |
| FR-material-library-014 | Entry from Action Required | Action Required item (e.g. "Character Option A … Select visual direction and approve") opens the library with Review Now. | OUT | P1 | demo | L208–L215 |

## 4. Non-Functional Requirements (NFR)

| ID | Category | Requirement | Priority | Acceptance |
|----|----------|-------------|----------|------------|
| NFR-material-library-001 | storage | Visuals stored with project files (Cloudflare R2). | P0 | quote §5 |
| NFR-material-library-002 | usability | Usable in a phone browser. | P0 | quote §7 |

## 5. Business Rules

| ID | Rule | Trigger | Implements FR | Source |
|----|------|---------|---------------|--------|
| BR-material-library-001 | One preferred option per category. | Select option | FR-material-library-006 | L373 (inferred beyond Characters) |
| BR-material-library-002 | Option status ∈ {New, In Review, Selected}. | Status shown | FR-material-library-005 | L382–L407 |
| BR-material-library-003 | Workflow order: Option submitted → Client feedback → Revision → Approved. | Status change | FR-material-library-011 | L424 |

## 6. Error Matrix

| Error ID | Title | Trigger | Severity | Related FR | Wording (exact) | Screen state | Recovery |
|----------|-------|---------|----------|------------|-----------------|--------------|----------|
| E-material-library-001 | No options in category | Category has no options | minor | FR-material-library-004 | TBD | Empty grid | Choose another category |
| E-material-library-002 | Empty feedback | Feedback saved without text | minor | FR-material-library-007 | TBD | Form stays | Write feedback |
| E-material-library-003 | Visual upload failed | Upload fails | major | FR-material-library-008 | TBD | Demo visual stays | Retry |
| E-material-library-004 | Nothing selected | Submit with no selected option (rule TBD) | minor | FR-material-library-009 | TBD | Unchanged | Select an option |

## 7. Success Criteria

| ID | Business outcome | Measured by | Target |
|----|------------------|-------------|--------|
| SC-material-library-01 | Client picks a direction per category with feedback recorded | Demo | Works end to end |

## 8. Data Entities (summary)

- **MaterialCategory:** project, name, count.
- **MaterialOption:** category, type label, name, visual, status, feedback note, selected.
- **OptionFeedback:** option, author, text, date.

## 9. Flows (summary)

Open library → category → compare → feedback → select → submit → workflow to Approved.

## 10. Screens (summary)

| Screen | Board |
|---|---|
| Material Library | 05 (L366–L424) |
| Details / Feedback | link only (L394) — TBD |
| Approval Summary | button only (L370) — TBD |

## 11. Constraints, Dependencies & Assumptions

| Constraint | Source / Owner |
|------------|----------------|
| Not in the contract; needs a change request | quote §6, §7 |

| Dependency | Owner | Blocks if not ready |
|------------|-------|---------------------|
| Change request ordered | Leap Up | Everything |
| Approver rule (C4) | Leap Up | FR-009, FR-011 |

## 12. Open Questions

- [ ] OQ-1 (C1): Ordered as a change request?
- [ ] OQ-2: Fixed categories; meaning of "Pending Approval" and "Pending Generation".
- [ ] OQ-3: Card status vs workflow stage.
- [ ] OQ-4: Approval Summary content.
- [ ] OQ-5: Who uploads option visuals.
- [ ] OQ-6: Submit control, recipient, approver (C4).
- [ ] OQ-7: Change selection after submit.
- [ ] OQ-8: Relation to the Project Files Material folder.
- [ ] OQ-9: Wording E-material-library-001…004.
