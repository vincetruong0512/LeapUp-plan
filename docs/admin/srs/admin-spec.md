---
type: srs
feature: admin
scope: MVP
status: draft
updated: 2026-11-22
links:
  - docs/admin/brainstorms/admin-management.md
  - docs/_sources/2026-11-21-leapup-references/bao-gia-leapup-mvp.md
---

# admin — Software Requirements Specification

## 1. Scope

Admin page to create projects, create client accounts and assign members per project (Leap Up / Client). MVP — quote P1 #1. No board design (C3): screens and wording are TBD.

## 2. Actors & Stakeholders

| Actor | Type | Goal | In scope? |
|-------|------|------|-----------|
| Admin (Leap Up) | person | Set up projects and access | Yes |
| Leap Up member | person | Be assigned to projects; admin rights TBD (OQ-2) | Yes |
| Client | person | Receive an account and project access | Yes |

## 3. Functional Requirements (FR)

| ID | Title | Description | Scope | Priority | Verify by | Source |
|----|-------|-------------|-------|----------|-----------|--------|
| FR-admin-001 | Admin page access | A Client cannot open the admin page or send an admin request (E-admin-003). Whether Leap Up members have admin rights is TBD (OQ-2). | MVP | P0 | test | quote P1 #1; auth-access FR-010 |
| FR-admin-002 | Create project | Admin creates a project with its details (field list TBD, OQ-3). | MVP | P0 | demo | quote P1 #1; board L16, L22, L24 |
| FR-admin-003 | Project folders | Every new project has the folders Proposal, Material, Outcome Development. | MVP | P0 | inspection | quote P1 #2; board L52–L54 |
| FR-admin-004 | Initial project status | A new project gets an initial status. Which status is TBD (OQ-3); the board's sample project shows "In Progress" (L19, sample data L11). | MVP | P1 | demo | board L19 (sample) |
| FR-admin-005 | Create client account | Admin creates a client account with a User ID and initial password. | MVP | P0 | demo | quote P1 #1; board L159 |
| FR-admin-006 | Unique User ID | If the User ID already exists (case-insensitive), then the system shall refuse it (E-admin-002). | MVP | P0 | test | auth-access BR-003, FR-005 |
| FR-admin-007 | Assign members | Admin assigns users to a project with role Leap Up or Client. | MVP | P0 | demo | quote P1 #1 |
| FR-admin-008 | Required fields | If a required field is empty, then the system shall not save and shall show E-admin-001. | MVP | P0 | test | brainstorm D1 |

## 4. Non-Functional Requirements (NFR)

| ID | Category | Requirement | Priority | Acceptance |
|----|----------|-------------|----------|------------|
| NFR-admin-001 | usability | UI follows the portal design language; admin screens to be approved by Leap Up. | P0 | Leap Up sign-off on admin screens (C3) |
| NFR-admin-002 | capacity | Supports ~50 users and their project memberships. | P1 | quote §1 |

## 5. Business Rules

| ID | Rule | Trigger | Implements FR | Source |
|----|------|---------|---------------|--------|
| BR-admin-001 | Only Leap Up creates accounts and projects. | Any creation | FR-admin-001, FR-admin-005 | board L159 |
| BR-admin-002 | A user sees a project only after being assigned to it. | Assignment | FR-admin-007 | board L146, L170 |
| BR-admin-003 | Role in a project is Leap Up or Client. | Assignment | FR-admin-007 | quote P1 #1 |

## 6. Error Matrix

| Error ID | Title | Trigger | Severity | Related FR | Wording (exact) | Screen state | Recovery |
|----------|-------|---------|----------|------------|-----------------|--------------|----------|
| E-admin-001 | Required field empty | Save with an empty required field | minor | FR-admin-008 | TBD | Form stays open | Fill the field |
| E-admin-002 | User ID taken | User ID already exists | major | FR-admin-006 | TBD | Form stays open | Choose another User ID |
| E-admin-003 | Not an Admin | Non-admin opens the admin page or sends an admin request directly | critical | FR-admin-001 | TBD | TBD | Back to user's projects |
| — (gap) | Assignment errors | User already a member, unknown user, assigning an Admin | — | FR-admin-007 | TBD | TBD | TBD (OQ-10) |

## 7. Success Criteria

| ID | Business outcome | Measured by | Target |
|----|------------------|-------------|--------|
| SC-admin-01 | Admin sets up a project with a client ready to sign in | Demo: create project → client account → assign → client signs in | Works end to end |

## 8. Data Entities (summary)

- **Project:** name, client name, due date, description, status (fields TBD, OQ-3).
- **Folder:** Proposal / Material / Outcome Development, per project.
- **User account:** see auth-access.
- **Project membership:** user, project, role (Leap Up / Client).

## 9. Flows (summary)

Create project · create client account · assign members — independent admin actions; the order is not set by the
reference (OQ-11; proposal PR3 suggests a wizard). Login details are handed over outside the portal.

## 10. Screens (summary)

No board design (C3). Screens TBD: admin home, project form, account form, member assignment.

## 11. Constraints, Dependencies & Assumptions

| Constraint | Source / Owner |
|------------|----------------|
| No e-mail invites in Phase 1 | quote P2 #4 |

| Dependency | Owner | Blocks if not ready |
|------------|-------|---------------------|
| Admin screen design approved | Leap Up (C3) | Build of FR-admin-002…008 UI |

| Assumption | Invalidates if wrong |
|------------|----------------------|
| Folders are created automatically per project | FR-admin-003 |

## 12. Open Questions

- [ ] OQ-1 (C3): Admin screen design and entry point.
- [ ] OQ-2: Admin rights for Leap Up members; how Leap Up member accounts and the first Admin account are created (quote names only "tài khoản client"; review SBA-2). Owner: Leap Up. Before Sprint 1.
- [ ] OQ-3: Project fields, which are required, and the initial status (board sample "In Progress", L19); statuses beyond it; edit/close project.
- [ ] OQ-4: Initial password handling and password rules (with auth-access OQ-7).
- [ ] OQ-5: Password reset — decided that the Leap Up admin resets it (auth-access brainstorm OQ-8, BR-auth-access-004). Still TBD: how (screen, steps). No FR yet; add one when answered.
- [ ] OQ-6: Remove member / deactivate account.
- [ ] OQ-7: Admin lists and search.
- [ ] OQ-8 (C7): Project Info tab content.
- [ ] OQ-9: All admin wording (E-admin-001…003).
- [ ] OQ-10: Assignment errors and limits — user already a member, unknown user, assigning an Admin; error codes and wording (review QA-15).
- [ ] OQ-11: Order of set-up actions and where the admin page is entered from (review FLOW-11; C3; proposal PR3).
- [ ] OQ-12: What an Admin's uploads and comments show as "Uploaded By" / author, since Admin is not a project role (review SBA-18; see auth-access OQ-10).
