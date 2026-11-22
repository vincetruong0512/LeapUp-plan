---
type: srs-userflow
feature: auth-access
updated: 2026-11-22
primary_device: desktop
stage: revised-after-review
flow_approved_at: 2026-11-22
flow_hash: "1cb9f2ae"
---

# auth-access — User Flow

Revised 2026-11-22 after the MVP review ([review-2026-11-22-mvp.md](../../portal/review-2026-11-22-mvp.md), R-01, R-03, R-17):
not-assigned branch, hand-offs to project-files and admin, TBD stubs for lockout and session expiry. Needs re-approval.

## 1. User Flow (overall)

```mermaid
flowchart TD
    n1["[1] Login (board 01)"]
    d1{"User ID and Password filled?"}
    d2{"Credentials match?"}
    d3{"Assigned projects?"}
    d4{"Assigned to this project?"}
    n2["[2] Login - error state"]
    n3["[3] Landing - no projects"]
    n4["[4] Landing - project list (TBD)"]
    n6["[5] Not assigned - E-auth-access-003 (not on board, TBD)"]
    n5["Sign out"]
    x1["Go to project-files: Project Files"]
    x2["Go to admin: Admin page - Admin only, entry TBD C3"]
    t1["Lockout - TBD (OQ-3)"]
    t2["Session expired - TBD (OQ-4)"]
    n1 -->|"Sign In"| d1
    d1 -->|"Yes"| d2
    d1 -->|"No - E-auth-access-002"| n2
    d2 -->|"Yes"| d3
    d2 -->|"No - E-auth-access-001"| n2
    d2 -.->|"Too many failures? TBD"| t1
    n2 -.->|"Re-enter"| n1
    d3 -->|"1 or more"| n4
    d3 -->|"None - E-auth-access-004"| n3
    n4 -->|"Open a project"| d4
    d4 -->|"Yes"| x1
    d4 -->|"No, or link to another project"| n6
    n6 -->|"Back to my projects"| n4
    n4 -.->|"Admin pages (Admin only)"| x2
    n4 -->|"Sign out"| n5
    n3 -->|"Sign out"| n5
    t1 -.->|"Contact Leap Up"| n1
    n4 -.->|"Inactive too long? TBD"| t2
    t2 -.->|"Sign in again"| n1
    n5 -.->|"Back to Login"| n1
    class n1,n4,n5,x1,x2 happy
    class n2,n6 error
    class n3,t1,t2 edge
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
    classDef edge fill:#fff3cd,stroke:#ffc107
```

The access check d4 runs on every request, not only from the landing page: a copied link, a file download, a video
or a comment of a project the user isn't assigned to all end in [5] (FR-auth-access-009). project-files, video-review
and admin show the same branch and point here. A signed-out request goes to [1] Login.

Not drawn as flow (display only): masked password with Show (FR-auth-access-002, board L79, L89–L90), the access
note box (board L150–L170).

## 2. Screens

| [#] | Slug | Screen | Purpose | Flow | Board |
|-----|------|--------|---------|------|-------|
| 1 | login | Login | Enter User ID + password | sign-in | 01, L18–L170 |
| 2 | login-error | Login — error state | Show E-auth-access-001/002 (wording, position TBD — spec OQ-13) | sign-in | not drawn |
| 3 | landing-empty | Landing — no projects | Signed in, no assigned project (E-auth-access-004) | sign-in | not drawn |
| 4 | landing | Landing — project list | Assigned projects; page TBD (spec OQ-1) | sign-in | not drawn |
| 5 | not-assigned | Not assigned | Refusal, no project content (E-auth-access-003, wording TBD) | sign-in | not drawn |

## 3. Flows

| Flow-slug | Flow name | Screens | Cases covered |
|-----------|-----------|---------|---------------|
| sign-in | Sign in, open a project, sign out | 1, 2, 3, 4, 5 | happy: 1→4→project-files · error: 2, 5 · edge: 3, lockout/expiry TBD · sign out → 1 |

## 3.5. Transitions

| From [#] | To [#] | Trigger | Condition |
|----------|--------|---------|-----------|
| 1 | 4 | Sign In | Fields filled, credentials match, ≥ 1 assigned project |
| 1 | 2 | Sign In | Empty field (E-auth-access-002) or wrong credentials (E-auth-access-001) |
| 2 | 1 | Edit fields | — |
| 1 | 3 | Sign In | Credentials match, no assigned project |
| 4 | project-files [1] | Open a project | User is assigned to the project |
| 4 or any link | 5 | Open a project / file / video / comment | User is not assigned (E-auth-access-003) |
| 5 | 4 | Back to my projects | — |
| 4 | admin [1] | Admin pages | Admin only; entry placement TBD (C3, admin OQ-1) |
| 3, 4 | 1 | Sign out | Placement TBD |

## 4. Open Questions

- [ ] OQ-1: Landing page content (spec OQ-1).
- [ ] OQ-2: Sign-out placement (spec OQ-2).
- [ ] OQ-3: Lockout branch — drawn as a TBD stub; keep only if Leap Up decides one (spec OQ-3).
- [ ] OQ-4: Session-expired branch — drawn as a TBD stub (spec OQ-4).
- [ ] OQ-5: Phone layout of the flow's screens (spec OQ-5).
- [ ] OQ-6: Access note says one User ID per project (board L159) vs one per person (spec BR-auth-access-003, OQ-9).
- [ ] OQ-7: Already signed-in user opening Login (spec OQ-14).
