---
type: srs-flows
feature: project-files
updated: 2026-11-22
---

# Project Files — Flows

## Flow: Find and download a file (Activity)

**Trigger**: User opens a project to get a file.
**Related UC**: [UC-project-files-01](../usecases/uc-find-and-download-a-file.md)
**Related FR**: FR-project-files-001, FR-project-files-002, FR-project-files-003, FR-project-files-004, FR-project-files-005, FR-project-files-008, FR-project-files-009, FR-project-files-010, FR-project-files-011, FR-project-files-012, FR-project-files-013
**Related E**: E-project-files-002, E-project-files-004

```mermaid
flowchart TB
    s(["Start"]) --> a1["User opens the project"]
    a1 --> d0{"Member of the project?"}
    d0 -->|"No"| e0["Refuse access E-auth-access-003"]
    d0 -->|"Yes"| a2["Show header, tabs, 3 folder cards, file table"]
    a2 --> a3["User searches or selects a folder card"]
    a3 --> d1{"Any matching file?"}
    d1 -->|"No"| e1["Empty table E-project-files-002 or 004"]
    e1 --> a3
    d1 -->|"Yes"| a4["Show matching files"]
    a4 --> a5["User downloads a file (control TBD)"]
    a5 --> ok["User has a copy of the file"]
    ok --> Stop(["End"])
    e0 --> Stop
    class ok happy
    class e0,e1 error
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
```

## Flow: Upload files into a folder (Sequence)

**Trigger**: User presses "Upload Files" on the Project Files tab.
**Related UC**: [UC-project-files-02](../usecases/uc-upload-files.md)
**Related FR**: FR-project-files-006, FR-project-files-007, FR-project-files-008, FR-project-files-009
**Related E**: E-project-files-001, E-project-files-003

```mermaid
sequenceDiagram
    actor User
    participant Portal
    participant R2 as Cloudflare R2
    User->>Portal: Upload Files - choose files and folder (folder choice TBD)
    Portal->>Portal: Check type and size (limits TBD)
    alt Type or size not allowed
        Portal-->>User: Reject the file - E-project-files-001
    else Allowed
        Portal->>R2: Store the files
        alt Stored
            R2-->>Portal: Files stored
            Portal-->>User: List each file with Name, Folder, Last Modified, Uploaded By, Status
        else Storage or network failure
            R2-->>Portal: Failure
            Portal-->>User: No row added - E-project-files-003
        end
    end
```
