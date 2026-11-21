---
type: srs-flows
feature: auth-access
updated: 2026-11-22
---

# Login & Project Access — Flows

## Flow: Sign in to my projects (Activity)

**Trigger**: User presses "Sign In" on the Login screen.
**Related UC**: [UC-auth-access-01](../usecases/uc-sign-in-to-my-projects.md)
**Related FR**: FR-auth-access-001, FR-auth-access-002, FR-auth-access-003, FR-auth-access-004, FR-auth-access-005, FR-auth-access-006, FR-auth-access-007, FR-auth-access-008, FR-auth-access-009, FR-auth-access-010
**Related E**: E-auth-access-001, E-auth-access-002, E-auth-access-003, E-auth-access-004

```mermaid
flowchart TB
    subgraph U["User"]
        s(["Start"]) --> a1["Enter User ID and password"]
        a1 --> a2["Press Sign In"]
    end
    subgraph P["Portal"]
        d1{"Both fields filled?"}
        d2{"User ID and password match? (User ID not case-sensitive)"}
        a3["Find assigned projects (Admin: all)"]
        d3{"At least 1 assigned project?"}
        e1["Show E-auth-access-002"]
        e2["Show E-auth-access-001, stay on Login"]
        e3["Show no-projects state E-auth-access-004"]
        ok["Show landing page with assigned projects only (landing TBD)"]
    end
    a2 --> d1
    d1 -->|"No"| e1
    d1 -->|"Yes"| d2
    d2 -->|"No"| e2
    d2 -->|"Yes"| a3
    a3 --> d3
    d3 -->|"No"| e3
    d3 -->|"Yes"| ok
    e1 --> a1
    e2 --> a1
    e3 --> Stop(["End"])
    ok --> Stop
    class ok happy
    class e1,e2,e3 error
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
```

## Flow: Sign out (Sequence)

**Trigger**: User chooses Sign out.
**Related UC**: [UC-auth-access-02](../usecases/uc-sign-out.md)
**Related FR**: FR-auth-access-011
**Related E**: —

```mermaid
sequenceDiagram
    actor User
    participant Portal
    User->>Portal: Choose Sign out (placement TBD)
    Portal->>Portal: End the session
    Portal-->>User: Show the Login screen
    Note over User,Portal: Opening a project page afterwards requires signing in again (FR-auth-access-011)
```
