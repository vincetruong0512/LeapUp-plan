---
type: srs-userflow
feature: project-files
updated: 2026-11-22
primary_device: desktop
stage: flow-approved
flow_approved_at: 2026-11-22
flow_hash: "71ec07ce"
---

# project-files — User Flow

## 1. User Flow (overall)

```mermaid
flowchart TD
    n0["Projects list (TBD - OQ-2)"]
    n1["[1] Project Files tab (board 03)"]
    d1{"Search or folder has files?"}
    n2["[2] Project Files - empty or no result"]
    n3["[3] Upload - choose files and folder (TBD)"]
    d2{"Type and size allowed?"}
    n4["[4] Upload - error state"]
    n5["Download file"]
    n6["Video Review"]
    n0 -->|"Open project"| n1
    n1 -->|"Search or select folder"| d1
    d1 -->|"Yes"| n1
    d1 -->|"No - E-project-files-002 or 004"| n2
    n2 -.->|"Clear search"| n1
    n1 -->|"Upload Files"| n3
    n3 -->|"Upload"| d2
    d2 -->|"Yes - row added"| n1
    d2 -->|"No - E-project-files-001 or 003"| n4
    n4 -.->|"Try again"| n3
    n1 -->|"Download"| n5
    n5 -.->|"Back"| n1
    n1 -->|"Open video"| n6
    n6 -.->|"Back to project"| n1
    class n0,n1,n3,n5,n6 happy
    class n4 error
    class n2 edge
    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
    classDef edge fill:#fff3cd,stroke:#ffc107
```

## 2. Screens

| [#] | Slug | Screen | Purpose | Flow | Board |
|-----|------|--------|---------|------|-------|
| 1 | project-files | Project detail — Project Files tab | Folders, file table, search, upload | files | 03, L9–L179 |
| 2 | project-files-empty | Empty / no-result state | E-project-files-002, 004 | files | not drawn |
| 3 | upload | Upload — choose files and folder | Upload input | files | not drawn (only "Upload Files" L83) |
| 4 | upload-error | Upload error state | E-project-files-001, 003 | files | not drawn |

## 3. Flows

| Flow-slug | Flow name | Screens | Cases covered |
|-----------|-----------|---------|---------------|
| files | Share, find and download files | 1, 2, 3, 4 | happy 1→3→1, download · edge 2 · error 4 |

## 3.5. Transitions

| From [#] | To [#] | Trigger | Condition |
|----------|--------|---------|-----------|
| list | 1 | Open project | Member of project |
| 1 | 2 | Search / folder | No match / empty |
| 1 | 3 | Upload Files | Upload allowed (OQ-3) |
| 3 | 1 | Upload | Valid → row added |
| 3 | 4 | Upload | Invalid or failed |
| 1 | download | Download | — |
| 1 | Video Review | Open video | Outcome video (OQ-8) |

## 4. Open Questions

- [ ] OQ-1: Projects list screen (spec OQ-2).
- [ ] OQ-2: Upload screen design — only the button is on the board (spec OQ-3).
