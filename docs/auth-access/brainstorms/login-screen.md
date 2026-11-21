---
type: brainstorm
feature: auth-access
scope: MVP
status: draft
updated: 2026-11-22
links:
  - docs/_sources/2026-11-21-leapup-references/bao-gia-leapup-mvp.md
  - docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md
  - docs/_sources/2026-11-21-leapup-references/_comparison.md
  - docs/portal/brainstorms/project-overview.md
---

# Login & Project Access — Brainstorm

## 0. Scope

**Tag:** MVP — "đăng nhập bằng User ID, phân quyền theo project (Leap Up / Client)" (quote p.1, P1 #1); Login screen on the board (board L18–L170).

**Open decisions touching this feature:** landing page after sign-in (OQ-17). Roles (C4 → OQ-2), one login page (OQ-1) and one User ID per person (OQ-3) are decided for now. Everything the reference does not state is TBD — see §11.

**Not in this feature:** creating accounts, assigning members, resetting passwords from the admin side → feature `admin`. E-mail (invites, reset links) → Phase 2 (quote P2 #4).

## 1. Idea Seed

> "đăng nhập bằng User ID, phân quyền theo project (Leap Up / Client)" (quote P1 #1)

Every user signs in with a User ID and password issued by Leap Up, and then sees only the projects they are assigned to.

## 2. Context

- The portal is private: there is no public sign-up; Leap Up issues every account (board L159).
- Access is project-specific: a client sees only the content of projects assigned to them (board L146, L170).
- No e-mail in the MVP, so accounts and passwords are handed over outside the portal (quote P2 #4 puts e-mail in Phase 2).
- Web app, usable on phones, one UI language following the current design (quote §7).
- The Login screen is the only drawn auth screen on the board: User ID, Password with Show, Sign In. There is no forgot-password, change-password, remember-me, lockout or sign-out element anywhere on the board or in the quote. Error, loading and signed-out states are not drawn.

## 3. User Types

| User Type | Role | Pain Point | Primary Need |
|-----------|------|-----------|--------------|
| Client reviewer | Client | Must reach only their own projects, simply | Sign in with the User ID Leap Up gave them and land on their projects |
| Leap Up staff | Leap Up member | Works across several client projects | Sign in once and reach all assigned projects |
| Leap Up admin | Admin | Responsible for who can see what | Confidence that clients never see another client's project |

All three use the same Login page — the board has one (OQ-1).

## 4. Capabilities Breakdown

### P0 — must have
- Sign in with User ID + password; password masked with a Show toggle (board L50–L120).
- Show only the projects the user is assigned to; refuse access to any other project (board L146; quote P1 #1).
- Error when the User ID or password is wrong — wording TBD (OQ-10).
- Sign out — not drawn; placement and wording TBD (OQ-16).
- A landing page after sign-in (OQ-17).

### TBD — not in the reference, needs Leap Up's decision
- Lockout after failed sign-ins (OQ-9).
- Session length / expiry (OQ-13).

### Post-MVP (not designed further)
- Users change their own password (OQ-8).
- Forced password change at first sign-in (OQ-6).
- Sign-in history for Leap Up (OQ-12).
- Reset by e-mail link → Phase 2 (quote P2 #4).

## 5. Core Flows (Happy Path)

### 5.1 Sign in

1. User opens the portal and sees the Login screen: brand panel + "Welcome — Sign in to access your project workspace." (board L25, L41).
2. User enters the User ID (placeholder "Enter your User ID", L69) and password (placeholder "Enter your password", L89); may press Show to check the password (L90).
3. User presses **Sign In** (L120). Loading state: TBD (OQ-21).
4. System checks the User ID (not case-sensitive — OQ-4) and password.
5. System checks the account is active.
6. System finds the projects the user is assigned to.
7. User lands on the landing page with only those projects (OQ-17).

```
┌──────────────────────────┐
│ Login screen (board 01)  │
│ User ID + Password       │
└────────────┬─────────────┘
             │ press Sign In
             ▼
┌──────────────────────────┐   NO   ┌───────────────────────────────┐
│ User ID + password match?│ ─────▶ │ Error, stay on Login           │
└────────────┬─────────────┘        │ wording TBD (OQ-10)            │
             │ YES                  │ lockout TBD (OQ-9)             │
             ▼                      └───────────────────────────────┘
┌──────────────────────────┐   NO   ┌───────────────────────────────┐
│ Account active?          │ ─────▶ │ Error, stay on Login           │
└────────────┬─────────────┘        │ wording TBD (OQ-11)            │
             │ YES                  └───────────────────────────────┘
             ▼
┌──────────────────────────┐   0    ┌───────────────────────────────┐
│ How many assigned        │ ─────▶ │ "No projects" state            │
│ projects?                │        │ wording TBD (OQ-18)            │
└────────────┬─────────────┘        └───────────────────────────────┘
             │ ≥ 1
             ▼
┌──────────────────────────┐
│ Landing page (OQ-17)     │
│ only assigned projects   │
└──────────────────────────┘
```

### 5.2 Sign out

1. User chooses Sign out (not drawn on the board — placement TBD, OQ-16).
2. System ends the session.
3. User returns to the Login screen (assumed; message TBD).

### 5.3 Password help (MVP, no e-mail)

1. User cannot sign in.
2. The Login screen has no "Forgot password?" link (OQ-7); the access note (board L150–L170) is the only guidance.
3. User contacts Leap Up outside the portal.
4. Leap Up admin sets a new password (feature `admin`) and hands it over outside the portal.
5. User signs in with the new password and keeps it (no forced change — OQ-6).

### 5.4 Session expired

1. Whether and when a session expires is TBD (OQ-13).
2. If it does, the user returns to the Login screen; message TBD (OQ-21); unsaved input behaviour TBD (OQ-15).

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | When | YES | NO |
|---|---|---|---|---|
| D1 | Sign in | Both fields filled? | Continue to D2 | Field message, wording TBD (OQ-21) |
| D2 | Sign in | User ID + password match? | Continue to D3 | Error, wording TBD (OQ-10); lockout TBD (OQ-9) |
| D3 | Sign in | Account active? | Continue to D4 | Error, wording TBD (OQ-11) |
| D4 | Sign in | ≥ 1 assigned project? | Landing page (OQ-17) | "No projects" state, wording TBD (OQ-18) |
| D5 | Any page | Session still valid? | Continue | Back to Login — rule TBD (OQ-13) |
| D6 | Open a project | User assigned to this project? | Open it | Refuse; project not listed (board L146) |

### 6.2 Scenario Matrix (role × access)

| User | Assigned projects | Opens own project | Opens another client's project | Admin pages |
|---|---|---|---|---|
| Client | 1 | Yes | Refused (board L146) | No |
| Client | several | Yes, all assigned, with one User ID (OQ-3) | Refused | No |
| Client | 0 | — "No projects" state (OQ-18) | Refused | No |
| Leap Up member | assigned ones | Yes | Refused unless assigned | No |
| Admin | all | Yes | Yes | Yes (feature `admin`) |
| Any, deactivated | — | Cannot sign in | — | — |

### 6.3 State Transitions

```
Account:  Active ──(admin deactivates)──▶ Deactivated ──(admin reactivates)──▶ Active
          Locked state — TBD (OQ-9)
Session:  Signed out ──(sign in)──▶ Signed in ──(sign out / expiry TBD)──▶ Signed out
```

| Entity | From | To | Trigger | Reversible? |
|--------|------|----|---------|-------------|
| Account | Active | Deactivated | Admin removes access (feature `admin`) | Yes — admin reactivates |
| Session | Signed in | Signed out | Sign out; expiry rule TBD (OQ-13) | Yes — sign in again |

### 6.4 Interrupted Transactions

| Situation | What the system keeps | Resume | Cleanup |
|---|---|---|---|
| Network drops after pressing Sign In | No session | Press Sign In again | — |
| Session expires while writing a comment | TBD (OQ-15) | Sign in again | — |
| User removed from a project while signed in | — | TBD (OQ-19) | — |
| Signed in on two devices | TBD (OQ-14) | — | — |

### 6.5 Other Edge Cases

- User ID typed with different upper/lower case → accepted (OQ-4).
- Browser autofill of User ID and password.
- Project closed or archived while users are assigned → TBD (OQ-19, feature `admin`).

## 7. Validation, Limits & Wording

### 7.1 Validation rules

| Field | Rule |
|---|---|
| User ID | Required; issued by Leap Up (board L159); short username, e.g. `nguyen.an`; not case-sensitive (OQ-4) |
| Password | Required; masked, Show toggle (board L89–L90); rules TBD (OQ-5) |

### 7.2 Limits & Quotas (exact values)

| Parameter | Value | Window | Behaviour when exceeded |
|---|---|---|---|
| Failed sign-in attempts | TBD (OQ-9) | TBD | TBD |
| Session length / inactivity | TBD (OQ-13) | — | TBD |
| Password minimum length | TBD (OQ-5) | — | TBD |

### 7.3 Wording samples (exact strings)

#### Error messages

| Situation | Wording | Code |
|---|---|---|
| Wrong User ID or password | TBD (OQ-10) | E-01 |
| Account deactivated | TBD (OQ-11) | E-02 |
| Field empty | TBD (OQ-21) | E-03 |

#### Success messages

| Situation | Wording |
|---|---|
| Signed in | TBD (OQ-21) |

#### Info / neutral messages

| Situation | Wording |
|---|---|
| Screen label | "00 / CLIENT LOGIN" (board L18) |
| Heading | "Welcome" (board L25) |
| Subtitle | "Sign in to access your project workspace." (board L41) |
| User ID label / placeholder | "User ID" / "Enter your User ID" (board L50, L69) |
| Password label / placeholder | "Password" / "Enter your password" (board L79, L89) |
| Password toggle | "Show" (board L90); hidden-state label TBD (OQ-24) |
| Button | "Sign In" (board L120) |
| Brand tagline | "One portal." / "Every project." / "One clear view." (board L48, L62, L77) |
| Brand subtitle | "Client Project Portal" / "Secure project-specific collaboration" (board L92, L108) |
| Private access badge | "PRIVATE CLIENT ACCESS" / "Only assigned project content is visible." (board L139, L146) |
| Access note | "PROJECT ACCESS NOTE" / "Each client receives a unique User ID and Password for each assigned project. Access is project-specific." (board L150, L159, L170) |
| Signing in · Session expired · Signed out · No projects | TBD (OQ-16, OQ-18, OQ-21) |

## 8. Assumptions

- Every account is created by Leap Up; there is no self sign-up (board L159).
- Passwords are handed over outside the portal (no e-mail in the MVP) and users keep them (OQ-6).
- The User ID is not case-sensitive (OQ-4).
- Signing out returns the user to the Login screen.
- The UI is in English, as on the board (quote §7 "một ngôn ngữ theo design hiện tại"; OQ-23).

## 9. Risks

| Risk | Likelihood | Business consequence | Prevention |
|--------|----------|-------------------|-----------|
| R1 Data: a client sees another client's project | rare | Breach of client confidentiality; loss of client trust | Access check on every project and file, not only on the list (D6); test with two clients |
| R2 Process: forgotten passwords flood Leap Up (no self-service in MVP) | sometimes | Leap Up staff time; clients blocked from reviewing | Admin reset in feature `admin`; guidance wording TBD |
| R4 Compliance: passwords shared by chat when handed over, and never changed | often | Accounts exposed | Accepted for the MVP (no forced change, OQ-6); Leap Up hands passwords over by a private channel |
| R5 Consistency: access-note text says one User ID "for each assigned project" (L159–L170) but the decision is one User ID per person (OQ-3) | sometimes | Clients misread how their login works | Leap Up confirms the note wording (OQ-3) |
| R6 Security: no lockout or session rule in the reference | sometimes | Password guessing; shared computers stay signed in | Leap Up decides OQ-9 and OQ-13 |

## 10. Success Criteria (preliminary)

- A client signs in on the first try with the details Leap Up gave them — target TBD.
- Zero cases of a user seeing a project they are not assigned to.

## 11. Open Points

Tick each one when answered and note the answer next to it. ⛔ = blocks `/srs`. `[x]` = decided for now (2026-11-22), the BA will follow up with Leap Up. Items the reference does not state stay open as TBD (strict-reference rule, 2026-11-22).

### A. Who signs in here
* [x] OQ-1: One shared Login page for staff and clients (the board has one). Label stays "00 / CLIENT LOGIN" as on the board (L18).
* [x] OQ-2 (C4): Three MVP roles — Admin, Leap Up member, Client. The board's named approvers are not MVP roles. (= portal OQ-3)
* [x] OQ-3: One User ID per person for all their projects. Access-note wording stays as on the board (L159–L170); whether Leap Up rewords it is TBD (risk R5). (= portal OQ-5)

### B. User ID & password
* [x] OQ-4: Short username, e.g. `nguyen.an`; not case-sensitive.
* [ ] OQ-5: Password rules — minimum length, character types, expiry. TBD.
* [x] OQ-6: No forced change at first sign-in (matches the reference). Admin sets the password and hands it over outside the portal.
* [x] OQ-7: No "Forgot password?" link (matches the reference); users contact Leap Up, as the access note implies (board L159).
* [x] OQ-8: No self-service password change (matches the reference); Leap Up admin resets it (feature `admin`).

### C. Failed sign-in & security
* [ ] OQ-9: Lockout after failed attempts — not in the reference. TBD.
* [ ] OQ-10: Wording for wrong User ID or password. TBD.
* [ ] OQ-11: Wording for a deactivated account. TBD.
* [x] OQ-12: No sign-in history (not in the reference); post-MVP.

### D. Session
* [ ] OQ-13: Session length / expiry — not in the reference. TBD.
* [ ] OQ-14: Signed in on two devices at once. TBD.
* [ ] OQ-15: Unsaved input when the session expires. TBD.
* [ ] OQ-16: Sign out — required, but not drawn; placement and wording TBD.

### E. After sign-in
* [ ] OQ-17 ⛔: Landing page in the MVP (the board's Home is the Phase 2 dashboard) — "My projects" list, or straight into the project when there is only one? TBD.
* [ ] OQ-18: Message for a user with no assigned projects. TBD.
* [ ] OQ-19: User removed from a project, or project closed, while signed in. TBD.
* [ ] OQ-20: Different landing for Leap Up staff and clients? TBD (depends on OQ-17).

### F. Screen & wording
* [ ] OQ-21: Wording for empty fields, signing in, session expired, success. TBD.
* [ ] OQ-22: Phone layout of the split Login screen (quote §7 requires phone use; board shows desktop only). TBD.
* [x] OQ-23: English, as on the board.
* [ ] OQ-24: Show toggle hidden-state label and accessibility. TBD.

## Work map — Login through the pipeline

| Step | Expected output |
|---|---|
| 1 /brainstorm | This document; 9 of 24 open points decided, 15 TBD |
| 2 /srs | ~7 requirements, 3 error codes with TBD wording, ~3 business rules |
| 3 /user-flow | 1 flow: sign in · error · no projects · landing · sign out |
| 4 /wireframe-html | Login screen as on board 01; states not drawn on the board are listed, not designed |
| 5 /userstory + /ac | ~4 stories |
| 6 /jira | 1 epic + ~4 stories (import file) |

## 12. Next Steps

* `/srs auth-access` — runs with OQ-17 as TBD
* `/brainstorm admin` — accounts, members and password reset (pairs with this feature)
