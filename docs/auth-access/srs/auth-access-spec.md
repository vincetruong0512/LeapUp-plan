---
type: srs
feature: auth-access
scope: MVP
status: draft
updated: 2026-11-22
links:
  - docs/auth-access/brainstorms/login-screen.md
  - docs/_sources/2026-11-21-leapup-references/bao-gia-leapup-mvp.md
  - docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md
---

# auth-access — Software Requirements Specification

## 1. Scope

Sign in with a User ID and password issued by Leap Up, project-scoped access for three roles, and sign out. MVP — quote P1 #1 "đăng nhập bằng User ID, phân quyền theo project (Leap Up / Client)"; board 01 Login (L18–L170). Account creation and password reset belong to `admin`.

## 2. Actors & Stakeholders

| Actor | Type | Goal | In scope? |
|-------|------|------|-----------|
| Client | person | Sign in and reach only the projects assigned to them | Yes |
| Leap Up member | person | Sign in and reach the projects assigned to them | Yes |
| Admin (Leap Up) | person | Sign in and reach all projects and the admin pages | Yes |
| Leap Up (business owner) | stakeholder | Client content stays private per project (board L139–L146) | Yes |

## 3. Functional Requirements (FR)

| ID | Title | Description | Scope | Priority | Verify by | Source |
|----|-------|-------------|-------|----------|-----------|--------|
| FR-auth-access-001 | Sign in | The system shall let a user sign in with a User ID and a password issued by Leap Up. | MVP | P0 | demo | quote P1 #1; board L50–L120 |
| FR-auth-access-002 | Masked password with Show | The password field shall be masked; pressing "Show" reveals the typed password. | MVP | P0 | demo | board L79, L89, L90 |
| FR-auth-access-003 | Required fields | If User ID or Password is empty when Sign In is pressed, then the system shall not check the credentials and shall show E-auth-access-002. | MVP | P0 | test | brainstorm D1 |
| FR-auth-access-004 | Wrong credentials | If the User ID and password do not match an account, then the system shall keep the user on Login and show E-auth-access-001. | MVP | P0 | test | brainstorm D2 |
| FR-auth-access-005 | User ID not case-sensitive | The system shall match the User ID regardless of upper/lower case. | MVP | P1 | test | brainstorm OQ-4 (user decision) |
| FR-auth-access-006 | Assigned projects only | After sign-in, the system shall show a user only the projects they are assigned to; an Admin sees all projects. | MVP | P0 | test | quote P1 #1; board L146, L170 |
| FR-auth-access-007 | Landing page | After sign-in the user lands on a landing page — which page is TBD (OQ-1). | MVP | P0 | demo | brainstorm OQ-17 |
| FR-auth-access-008 | No assigned projects | If a signed-in user has no assigned project, then the system shall show a "no projects" state (wording TBD, E-auth-access-004). | MVP | P1 | test | brainstorm D4 |
| FR-auth-access-009 | Access check on every request | If a user requests a project, file, video or comment of a project they are not assigned to, then the system shall refuse it (E-auth-access-003). | MVP | P0 | test | board L146, L170; brainstorm R1 |
| FR-auth-access-010 | Three roles per project | The system shall support the roles Admin, Leap Up member and Client; Leap Up member and Client are assigned per project. | MVP | P0 | inspection | quote P1 #1; brainstorm OQ-2 (C4) |
| FR-auth-access-011 | Sign out | The system shall let a signed-in user sign out and return to Login. Placement and wording TBD (OQ-2). | MVP | P0 | demo | brainstorm 5.2, OQ-16 |

## 4. Non-Functional Requirements (NFR)

| ID | Category | Requirement | Priority | Acceptance |
|----|----------|-------------|----------|------------|
| NFR-auth-access-001 | security | All pages are served over SSL. | P0 | Portal reachable only via https (quote P1 #4 "SSL") |
| NFR-auth-access-002 | usability | Login works in a phone browser; no native app. | P0 | Sign in completed on a phone browser (quote §7); phone layout TBD (OQ-5) |
| NFR-auth-access-003 | localisation | One UI language: English, as on the board. | P0 | All Login text matches board wording (quote §7; board L18–L170) |
| NFR-auth-access-004 | capacity | About 50 users in total. | P1 | 50 accounts can sign in (quote §1) |
| NFR-auth-access-005 | security | Lockout after failed attempts and session expiry. | — | TBD — Leap Up — before build (OQ-3, OQ-4) |

## 5. Business Rules

| ID | Rule | Trigger | Implements FR | Source |
|----|------|---------|---------------|--------|
| BR-auth-access-001 | Only Leap Up creates accounts; there is no self sign-up. | Any new user | FR-auth-access-001 | board L159 |
| BR-auth-access-002 | Access is project-specific: a Client or Leap Up member sees only content of projects they are assigned to. | Every request | FR-auth-access-006, FR-auth-access-009 | board L146, L170 |
| BR-auth-access-003 | One User ID per person covers all of that person's projects. | Account creation | FR-auth-access-001 | brainstorm OQ-3 (user decision) |
| BR-auth-access-004 | Users cannot change or recover their own password in the MVP; Leap Up admin resets it. | Forgotten password | FR-auth-access-001 | brainstorm OQ-7, OQ-8 |

## 6. Error Matrix

| Error ID | Title | Trigger | Severity | Related FR | Wording (exact) | Screen state | Recovery |
|----------|-------|---------|----------|------------|-----------------|--------------|----------|
| E-auth-access-001 | Wrong credentials | User ID + password don't match | major | FR-auth-access-004 | TBD | Login, fields kept (User ID) — TBD | Re-enter; contact Leap Up |
| E-auth-access-002 | Empty field | Sign In with an empty field | minor | FR-auth-access-003 | TBD | Login | Fill the field |
| E-auth-access-003 | Not assigned | Request for a project the user isn't assigned to | critical | FR-auth-access-009 | TBD | TBD | Back to the user's projects |
| E-auth-access-004 | No projects | Signed-in user has no assigned project | minor | FR-auth-access-008 | TBD | Landing, empty | Contact Leap Up |

## 7. Success Criteria

| ID | Business outcome | Measured by | Target |
|----|------------------|-------------|--------|
| SC-auth-access-01 | No client sees another client's project | Access test with two clients on every project page and file | 0 leaks |
| SC-auth-access-02 | Clients can sign in with the details Leap Up gave them | First-try sign-in at demo / acceptance | TBD |

## 8. Data Entities (summary)

- **User account:** User ID, password (protected), display name, role (Admin / Leap Up member / Client), active or not.
- **Project membership:** user, project, role in the project (Leap Up / Client).

## 9. Flows (summary)

Sign in → (error | no projects | landing) · sign out → Login. Details in `auth-access-userflow.md`.

## 10. Screens (summary)

| Screen | Board | Notes |
|---|---|---|
| Login | 01 (L18–L170) | As drawn |
| Login — error state | not drawn | Message position and wording TBD |
| Landing | not drawn | TBD (OQ-1) |

## 11. Constraints, Dependencies & Assumptions

**Constraints:**

| Constraint | Source / Owner |
|------------|----------------|
| Sign-in uses a User ID (not e-mail) | quote P1 #1 |
| UI follows the agreed Miro design | quote §1 |
| No e-mail in Phase 1 | quote P2 #4 |

**Dependencies:**

| Dependency | Owner | Blocks if not ready |
|------------|-------|---------------------|
| Accounts and project memberships created | feature `admin` | Nobody can sign in |
| Landing page content | feature `project-files` (Projects) / OQ-1 | Post-sign-in screen |

**Assumptions:**

| Assumption | Invalidates if wrong |
|------------|----------------------|
| Passwords are handed over outside the portal | FR-auth-access-001 onboarding |
| Sign out returns to Login | FR-auth-access-011 |

## 12. Open Questions

- [ ] OQ-1: Landing page after sign-in (brainstorm OQ-17, OQ-20). Owner: Leap Up.
- [ ] OQ-2: Sign-out placement and wording (brainstorm OQ-16).
- [ ] OQ-3: Lockout after failed sign-ins (brainstorm OQ-9).
- [ ] OQ-4: Session length and expiry; behaviour of unsaved input; multiple devices (brainstorm OQ-13–OQ-15).
- [ ] OQ-5: Phone layout of the split Login screen (brainstorm OQ-22).
- [ ] OQ-6: All error/info wording E-auth-access-001…004 (brainstorm OQ-10, OQ-18, OQ-21).
- [ ] OQ-7: Password rules (brainstorm OQ-5).
- [ ] OQ-8: Account deactivation — not in the reference; needed? (brainstorm OQ-11; feature `admin`).
- [ ] OQ-9: Access-note wording vs one User ID per person (brainstorm OQ-3, R5).
