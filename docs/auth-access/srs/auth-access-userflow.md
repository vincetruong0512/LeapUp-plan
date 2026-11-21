---
type: srs-userflow
feature: auth-access
updated: 2026-11-22
primary_device: desktop
stage: flow-approved
flow_approved_at: 2026-11-22
flow_hash: "1cb9f2ae"
---

# auth-access — User Flow

## 1. User Flow (overall)

```mermaid
flowchart TD
    n1["[1] Login (board 01)"]
    d1{"User ID and Password filled?"}
    d2{"Credentials match?"}
    d3{"Assigned projects?"}
    n2["[2] Login - error state"]
    n3["[3] Landing - no projects"]
    n4["[4] Landing - project list (TBD)"]
    n5["Sign out"]
    n1 -->|"Sign In"| d1
    d1 -->|"Yes"| d2
    d1 -->|"No - E-auth-access-002"| n2
    d2 -->|"Yes"| d3
    d2 -->|"No - E-auth-access-001"| n2
    n2 -.->|"Re-enter"| n1
    d3 -->|"1 or more"| n4
    d3 -->|"None - E-auth-access-004"| n3
    n4 -->|"Sign out"| n5
    n3 -->|"Sign out"| n5
    n5 -.->|"Back to Login"| n1
    class n1,n4,n5 happy
    class n2 error
    class n3 edge
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
    classDef edge fill:#fff3cd,stroke:#ffc107
```

## 2. Screens

| [#] | Slug | Screen | Purpose | Flow | Board |
|-----|------|--------|---------|------|-------|
| 1 | login | Login | Enter User ID + password | sign-in | 01, L18–L170 |
| 2 | login-error | Login — error state | Show E-auth-access-001/002 (wording TBD) | sign-in | not drawn |
| 3 | landing-empty | Landing — no projects | Signed in, no assigned project (E-auth-access-004) | sign-in | not drawn |
| 4 | landing | Landing — project list | Assigned projects; page TBD (spec OQ-1) | sign-in | not drawn |

## 3. Flows

| Flow-slug | Flow name | Screens | Cases covered |
|-----------|-----------|---------|---------------|
| sign-in | Sign in and sign out | 1, 2, 3, 4 | happy: 1→4 · error: 2 · edge: 3 · sign out → 1 |

## 3.5. Transitions

| From [#] | To [#] | Trigger | Condition |
|----------|--------|---------|-----------|
| 1 | 4 | Sign In | Fields filled, credentials match, ≥ 1 assigned project |
| 1 | 2 | Sign In | Empty field (E-auth-access-002) or wrong credentials (E-auth-access-001) |
| 2 | 1 | Edit fields | — |
| 1 | 3 | Sign In | Credentials match, no assigned project |
| 3, 4 | 1 | Sign out | Placement TBD |

## 4. Open Questions

- [ ] OQ-1: Landing page content (spec OQ-1).
- [ ] OQ-2: Sign-out placement (spec OQ-2).
- [ ] OQ-3: Lockout branch — add only if Leap Up decides one (spec OQ-3).
- [ ] OQ-4: Session-expired branch (spec OQ-4).
