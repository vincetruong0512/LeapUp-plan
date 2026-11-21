---
type: srs-flows
feature: material-library
updated: 2026-11-22
---

# Material Library — Flows

## Flow: Choose a material direction (OUT) (Activity)

**Trigger**: Client opens Material Library.
**Related UC**: [UC-material-library-01](../usecases/uc-choose-a-material-direction.md)
**Related FR**: FR-material-library-001, FR-material-library-002, FR-material-library-003, FR-material-library-004, FR-material-library-005, FR-material-library-006, FR-material-library-007, FR-material-library-009, FR-material-library-010, FR-material-library-011, FR-material-library-012, FR-material-library-013, FR-material-library-014
**Related E**: E-material-library-001, E-material-library-002, E-material-library-004

```mermaid
flowchart TB
    s(["Start"]) --> a1["Open Material Library"]
    a1 --> a2["Show MATERIAL CATEGORIES with counts"]
    a2 --> a3["Select a category"]
    a3 --> d1{"Category has options?"}
    d1 -->|"No"| e1["Show E-material-library-001"]
    e1 --> a3
    d1 -->|"Yes"| a4["Show OPTION REVIEW cards, REVIEW GUIDE, APPROVAL WORKFLOW"]
    a4 --> a5["Details / Feedback on an option"]
    a5 --> d2{"Feedback text entered?"}
    d2 -->|"No"| e2["Show E-material-library-002"]
    e2 --> a5
    d2 -->|"Yes"| a6["Select Option X - Selected"]
    a6 --> a7["Submit for approval (control TBD)"]
    a7 --> d3{"An option selected?"}
    d3 -->|"No"| e3["Show E-material-library-004"]
    e3 --> a6
    d3 -->|"Yes"| ok["Option submitted, Client feedback, Revision, Approved"]
    ok --> Stop(["End"])
    class ok happy
    class e1,e2,e3 error
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
```

## Flow: Provide option visuals (OUT) (Sequence)

**Trigger**: Leap Up uploads an asset for an option.
**Related UC**: [UC-material-library-02](../usecases/uc-provide-option-visuals.md)
**Related FR**: FR-material-library-008
**Related E**: E-material-library-003

```mermaid
sequenceDiagram
    actor Member as Leap Up member
    participant Portal
    participant R2 as Cloudflare R2
    Member->>Portal: Upload asset for the option (who and how TBD)
    Portal->>R2: Store the asset
    alt Stored
        R2-->>Portal: Stored
        Portal-->>Member: Card shows the uploaded visual
    else Upload fails
        R2-->>Portal: Failure
        Portal-->>Member: Demo visual stays - E-material-library-003
    end
```
