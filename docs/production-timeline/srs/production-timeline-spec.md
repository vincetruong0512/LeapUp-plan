---
type: srs
feature: production-timeline
scope: P2
status: draft
updated: 2026-11-22
links:
  - docs/production-timeline/brainstorms/production-timeline.md
  - docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md
---

# production-timeline — Software Requirements Specification

## 1. Scope

Project timeline with five production stages and milestones. P2 — quote P2 #2; board 04 (L197–L350). Client Inputs and Feedback Rule (C6) are specified as shown on the board but marked OPEN.

## 2. Actors & Stakeholders

| Actor | Type | Goal | In scope? |
|-------|------|------|-----------|
| Leap Up member | person | Maintain the timeline | Yes |
| Client | person | Follow progress; provide inputs (C6) | Yes |

## 3. Functional Requirements (FR)

| ID | Title | Description | Scope | Priority | Verify by | Source |
|----|-------|-------------|-------|----------|-----------|--------|
| FR-production-timeline-001 | Header | Breadcrumb "Projects / {project} / Proposal / Timeline", title "Proposal / Production Timeline", "{project} \| {description} \| Due {date}"; sidebar with "{project} · PROJECT". | P2 | P0 | demo | board L197, L205, L207, L209–L239 |
| FR-production-timeline-002 | Five stages | Show PRODUCTION STAGES: five cards with number, status label, stage name, date range. | P2 | P0 | demo | quote P2 #2; board L216–L244 |
| FR-production-timeline-003 | Stage status | Stage status ∈ DONE, CLIENT REVIEW, UP NEXT, NOT STARTED. Who changes it TBD (OQ-2). | P2 | P0 | demo | board L225–L229 |
| FR-production-timeline-004 | Milestones table | Show Milestones with MILESTONE, OWNER, DUE, STATUS. | P2 | P0 | demo | quote P2 #2; board L256–L268 |
| FR-production-timeline-005 | Milestone status | Milestone status ∈ Done, Waiting, Pending, Not started. | P2 | P0 | demo | board L278–L350 |
| FR-production-timeline-006 | Maintain timeline | Leap Up edits stage dates/status and milestones. Controls not drawn (OQ-2). | P2 | P0 | demo | quote P2 #2 |
| FR-production-timeline-007 | Client Inputs (OPEN C6) | Show Client Inputs with Received / Missing per item and "Upload inputs". | P2 | P1 | demo | board L255–L299 |
| FR-production-timeline-008 | Feedback Rule (OPEN C6) | Show the FEEDBACK RULE box text. | P2 | P2 | demo | board L318–L346 |
| FR-production-timeline-009 | Project-scoped | Only project members see the timeline. | P2 | P0 | test | auth-access FR-009 |

## 4. Non-Functional Requirements (NFR)

| ID | Category | Requirement | Priority | Acceptance |
|----|----------|-------------|----------|------------|
| NFR-production-timeline-001 | usability | Usable in a phone browser. | P0 | quote §7 |

## 5. Business Rules

| ID | Rule | Trigger | Implements FR | Source |
|----|------|---------|---------------|--------|
| BR-production-timeline-001 | A project has five production stages. | Timeline shown | FR-production-timeline-002 | quote P2 #2 |
| BR-production-timeline-002 | Milestone owner is Client or Leap Up. | Milestone saved | FR-production-timeline-004 | board L276, L301 |

## 6. Error Matrix

| Error ID | Title | Trigger | Severity | Related FR | Wording (exact) | Screen state | Recovery |
|----------|-------|---------|----------|------------|-----------------|--------------|----------|
| E-production-timeline-001 | No milestones | Project has none | minor | FR-production-timeline-004 | TBD | Empty table | Add milestone |
| E-production-timeline-002 | Input upload failed | Upload fails (C6) | major | FR-production-timeline-007 | TBD | Item stays Missing | Retry |

## 7. Success Criteria

| ID | Business outcome | Measured by | Target |
|----|------------------|-------------|--------|
| SC-production-timeline-01 | Client sees current stage and next milestones | Demo | Works |

## 8. Data Entities (summary)

- **Stage:** project, number, name, status, start/end date.
- **Milestone:** project, name, owner, due date, status.
- **Client input (C6):** project, name, Received/Missing, file.

## 9. Flows (summary)

Open timeline → view → (Leap Up) edit · (Client) upload input (C6).

## 10. Screens (summary)

| Screen | Board |
|---|---|
| Proposal / Production Timeline | 04 (L197–L350) |

## 11. Constraints, Dependencies & Assumptions

| Dependency | Owner | Blocks if not ready |
|------------|-------|---------------------|
| C6 decision | Leap Up | FR-007, FR-008 |

## 12. Open Questions

- [ ] OQ-1: Fixed stage names?
- [ ] OQ-2: Edit rights and controls.
- [ ] OQ-3: Status transitions.
- [ ] OQ-4: Entry point.
- [ ] OQ-5 (C6): Client Inputs in scope; upload target folder.
- [ ] OQ-6 (C6): Feedback Rule static or per project.
- [ ] OQ-7: Wording E-production-timeline-001…002.
