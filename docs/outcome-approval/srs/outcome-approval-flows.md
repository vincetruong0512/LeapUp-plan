---
type: srs-flows
feature: outcome-approval
updated: 2026-11-22
---

# Outcome Approval — Flows

## Flow: Approve a version (Activity)

**Trigger**: Round awaits client approval.
**Related UC**: [UC-outcome-approval-01](../usecases/uc-approve-a-version.md)
**Related FR**: FR-outcome-approval-002, FR-outcome-approval-005, FR-outcome-approval-010, FR-outcome-approval-011
**Related E**: E-outcome-approval-001

```mermaid
flowchart TB
    subgraph C["Client"]
        s(["Start"]) --> a1["Review the version in Video Review"]
        a1 --> a2["Approve the version (control TBD)"]
    end
    subgraph P["Portal"]
        d1{"User may approve? (rule TBD, C4)"}
        e1["Record nothing, show E-outcome-approval-001"]
        ok["Record approval: version, approver, date"]
        a3["Approval Log shows the entry"]
    end
    a2 --> d1
    d1 -->|"No"| e1
    d1 -->|"Yes"| ok
    ok --> a3
    a3 --> Stop(["End"])
    e1 --> Stop
    class ok happy
    class e1 error
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
```

## Flow: Track change requests and revision rounds (Activity)

**Trigger**: Member opens Revision & Sign-off.
**Related UC**: [UC-outcome-approval-02](../usecases/uc-track-change-requests.md)
**Related FR**: FR-outcome-approval-001, FR-outcome-approval-003, FR-outcome-approval-004, FR-outcome-approval-008, FR-outcome-approval-009
**Related E**: E-outcome-approval-003

```mermaid
flowchart TB
    s(["Start"]) --> a1["Open Revision and Sign-off"]
    a1 --> a2["Show Revision Rounds (OPEN C5) and Approvers (OPEN C4)"]
    a2 --> d1{"Change requests exist?"}
    d1 -->|"No"| e1["Show E-outcome-approval-003"]
    d1 -->|"Yes"| a3["Show REQUEST, ROUND, SCOPE, COST, STATUS"]
    e1 --> a4
    a3 --> a4["Record or update a change request (rights TBD)"]
    a4 --> d2{"Scope?"}
    d2 -->|"In scope"| a5["Cost -, status Done when delivered"]
    d2 -->|"Out of scope"| a6["Cost TBD (C5), status Quote sent then Client approved"]
    a5 --> ok["Change request shown in the table"]
    a6 --> ok
    ok --> Stop(["End"])
    class ok happy
    class e1 error
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
```

## Flow: Sign off the final version (Activity)

**Trigger**: Client presses "Approve final version".
**Related UC**: [UC-outcome-approval-03](../usecases/uc-sign-off-the-final-version.md)
**Related FR**: FR-outcome-approval-005, FR-outcome-approval-006, FR-outcome-approval-007, FR-outcome-approval-010
**Related E**: E-outcome-approval-001, E-outcome-approval-002

```mermaid
flowchart TB
    subgraph C["Client"]
        s(["Start"]) --> a1["Open Revision and Sign-off"]
        a1 --> a2["Tick the three checks (OPEN C9)"]
        a2 --> a3["Press Approve final version"]
    end
    subgraph P["Portal"]
        d1{"User may approve? (Final approver: Client)"}
        d2{"All three checks ticked?"}
        e1["Record nothing, show E-outcome-approval-001"]
        e2["Record nothing, show E-outcome-approval-002"]
        ok["Record final sign-off, Approval Log shows date instead of Pending"]
    end
    a3 --> d1
    d1 -->|"No"| e1
    d1 -->|"Yes"| d2
    d2 -->|"No"| e2
    e2 --> a2
    d2 -->|"Yes"| ok
    ok --> Stop(["End"])
    e1 --> Stop
    class ok happy
    class e1,e2 error
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
```
