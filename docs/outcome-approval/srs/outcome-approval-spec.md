---
type: srs
feature: outcome-approval
scope: P2
status: draft
updated: 2026-11-22
links:
  - docs/outcome-approval/brainstorms/outcome-approval.md
  - docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md
---

# outcome-approval — Software Requirements Specification

## 1. Scope

Per-version approval, change requests, approval log and final sign-off. P2 — quote P2 #3; board 08 (L214–L365). C4, C5, C9 parts specified as on the board and marked OPEN.

## 2. Actors & Stakeholders

| Actor | Type | Goal | In scope? |
|-------|------|------|-----------|
| Client | person | Approve versions; sign off final | Yes |
| Leap Up member | person | Track change requests and approvals | Yes |

## 3. Functional Requirements (FR)

| ID | Title | Description | Scope | Priority | Verify by | Source |
|----|-------|-------------|-------|----------|-----------|--------|
| FR-outcome-approval-001 | Header | Breadcrumb "Projects / {project} / Outcome Development / Revision", title "Outcome Development / Revision & Sign-off", "{project} \| {description}". | P2 | P0 | demo | board L214, L218, L230 |
| FR-outcome-approval-002 | Approve a version | Client approves a version; recorded in the Approval Log. Location of the control TBD (OQ-1). | P2 | P0 | demo | quote P2 #3 |
| FR-outcome-approval-003 | Change Requests table | Show REQUEST, ROUND, SCOPE, COST, STATUS. | P2 | P0 | demo | quote P2 #3; board L287–L333 |
| FR-outcome-approval-004 | Record change request | Create/update change requests. Who and which fields TBD (OQ-3). | P2 | P0 | demo | quote P2 #3 |
| FR-outcome-approval-005 | Approval Log | List approval events with date; pending items show "Pending". | P2 | P0 | demo | quote P2 #3 "lịch sử phê duyệt"; board L344–L364 |
| FR-outcome-approval-006 | Final sign-off | FINAL SIGN-OFF card with the final file name and "Approve final version". | P2 | P0 | demo | quote P2 #3; board L345, L351, L365 |
| FR-outcome-approval-007 | Sign-off checklist (OPEN C9) | Three checkboxes before approving the final version. | P2 | P1 | demo | board L354–L360 |
| FR-outcome-approval-008 | Revision Rounds (OPEN C5) | Show Included / Used / Remaining and the note "Round 3 onwards: additional scope & cost / Client confirms before work starts." | P2 | P1 | demo | board L245–L274 |
| FR-outcome-approval-009 | Approvers (OPEN C4) | Show approvers with side (CLIENT / LEAP UP), name/title and responsibility. | P2 | P2 | demo | board L246–L271 |
| FR-outcome-approval-010 | Approver rights | Only allowed client users can approve (rule TBD, OQ-2); others get E-outcome-approval-001. | P2 | P0 | test | board L346 "Final approver: Client" |
| FR-outcome-approval-011 | Project-scoped | Only project members see this screen. | P2 | P0 | test | auth-access FR-009 |

## 4. Non-Functional Requirements (NFR)

| ID | Category | Requirement | Priority | Acceptance |
|----|----------|-------------|----------|------------|
| NFR-outcome-approval-001 | audit | Every approval keeps who, what, when; not editable afterwards (assumed — OQ-4). | P0 | Log entry visible after approval |
| NFR-outcome-approval-002 | usability | Usable in a phone browser. | P0 | quote §7 |

## 5. Business Rules

| ID | Rule | Trigger | Implements FR | Source |
|----|------|---------|---------------|--------|
| BR-outcome-approval-001 | Final approver is the Client. | Final sign-off | FR-outcome-approval-006, 010 | board L346 |
| BR-outcome-approval-002 | Change request scope is In scope or Out of scope. | CR saved | FR-outcome-approval-003 | board L306, L321 |
| BR-outcome-approval-003 | CR status values: Done, Quote sent, Client approved. | CR status change | FR-outcome-approval-004 | board L308, L323, L333 |
| BR-outcome-approval-004 | Rounds beyond the included count are additional scope and cost (OPEN C5). | Next round | FR-outcome-approval-008 | board L270, L274 |

## 6. Error Matrix

| Error ID | Title | Trigger | Severity | Related FR | Wording (exact) | Screen state | Recovery |
|----------|-------|---------|----------|------------|-----------------|--------------|----------|
| E-outcome-approval-001 | Not allowed to approve | Non-approver tries to approve | major | FR-outcome-approval-010 | TBD | Unchanged | — |
| E-outcome-approval-002 | Checklist incomplete | Approve final with unticked items (C9) | minor | FR-outcome-approval-007 | TBD | Unchanged | Tick items |
| E-outcome-approval-003 | No change requests | None recorded | minor | FR-outcome-approval-003 | TBD | Empty table | — |

## 7. Success Criteria

| ID | Business outcome | Measured by | Target |
|----|------------------|-------------|--------|
| SC-outcome-approval-01 | Final cut signed off with a record | Demo | Log shows who and when |

## 8. Data Entities (summary)

- **Approval:** project, version, approver, date, type (version / final).
- **Change request:** project, request, round, scope, cost, status.
- **Revision quota (C5):** included, used, remaining.

## 9. Flows (summary)

Approve version → log · record CR → status · final sign-off → log.

## 10. Screens (summary)

| Screen | Board |
|---|---|
| Outcome Development / Revision & Sign-off | 08 (L214–L365) |
| Version approval control | not drawn (OQ-1) |

## 11. Constraints, Dependencies & Assumptions

| Dependency | Owner | Blocks if not ready |
|------------|-------|---------------------|
| Rounds/versions from Video Review | `video-review` | Versions to approve |
| C4, C5, C9 decisions | Leap Up | FR-007…010 |

## 12. Open Questions

- [ ] OQ-1: Version approval control location.
- [ ] OQ-2 (C4): Who can approve; approvers list.
- [ ] OQ-3: Change request lifecycle and rights.
- [ ] OQ-4: Effects of final sign-off; edit lock.
- [ ] OQ-5 (C5): Revision quota and CR cost.
- [ ] OQ-6 (C9): Checklist items.
- [ ] OQ-7: Reject/request changes on a version.
- [ ] OQ-8: Wording E-outcome-approval-001…003.
