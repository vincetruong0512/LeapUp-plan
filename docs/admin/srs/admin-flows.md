---
type: srs-flows
feature: admin
updated: 2026-11-22
---

# Admin — Flows

## Flow: Create a project (Activity)

**Trigger**: Admin opens the admin page to create a project.
**Related UC**: [UC-admin-01](../usecases/uc-create-project.md)
**Related FR**: FR-admin-001, FR-admin-002, FR-admin-003, FR-admin-004, FR-admin-008
**Related E**: E-admin-001, E-admin-003

```mermaid
flowchart TB
    s(["Start"]) --> a1["Admin opens the admin page"]
    a1 --> d1{"User is an Admin?"}
    d1 -->|"No"| e1["Refuse access E-admin-003"]
    d1 -->|"Yes"| a2["Admin enters project details (fields TBD)"]
    a2 --> a3["Admin saves"]
    a3 --> d2{"Required fields filled?"}
    d2 -->|"No"| e2["Show E-admin-001, nothing saved"]
    e2 --> a2
    d2 -->|"Yes"| ok["Create project: status In Progress + folders Proposal, Material, Outcome Development"]
    ok --> Stop(["End"])
    e1 --> Stop
    class ok happy
    class e1,e2 error
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
```

## Flow: Create a client account (Activity)

**Trigger**: Admin saves a new client account.
**Related UC**: [UC-admin-02](../usecases/uc-create-client-account.md)
**Related FR**: FR-admin-005, FR-admin-006, FR-admin-008
**Related E**: E-admin-001, E-admin-002

```mermaid
flowchart TB
    s(["Start"]) --> a1["Admin enters User ID and initial password"]
    a1 --> a2["Admin saves"]
    a2 --> d1{"Required fields filled?"}
    d1 -->|"No"| e1["Show E-admin-001"]
    e1 --> a1
    d1 -->|"Yes"| d2{"User ID unique, ignoring case?"}
    d2 -->|"No"| e2["Show E-admin-002"]
    e2 --> a1
    d2 -->|"Yes"| ok["Create the account"]
    ok --> a3["Admin hands over User ID and password outside the portal"]
    a3 --> Stop(["End"])
    class ok happy
    class e1,e2 error
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
```

## Flow: Assign members to a project (Activity)

**Trigger**: Admin adds a user to a project.
**Related UC**: [UC-admin-03](../usecases/uc-assign-members.md)
**Related FR**: FR-admin-007
**Related E**: —

```mermaid
flowchart TB
    s(["Start"]) --> a1["Admin opens the project"]
    a1 --> a2["Admin selects a user and role Leap Up or Client"]
    a2 --> d1{"Already a member?"}
    d1 -->|"Yes"| n1["No change (assumed)"]
    d1 -->|"No"| a3["Admin saves"]
    a3 --> ok["Record membership: user sees the project after sign-in"]
    ok --> Stop(["End"])
    n1 --> Stop
    class ok happy
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
```
