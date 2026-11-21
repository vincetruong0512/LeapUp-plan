---
type: brainstorm
feature: project-files
scope: MVP
status: draft
updated: 2026-11-22
links:
  - docs/_sources/2026-11-21-leapup-references/bao-gia-leapup-mvp.md
  - docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md
  - docs/_sources/2026-11-21-leapup-references/_comparison.md
---

# Project Files — Brainstorm

## 0. Scope

**Tag:** MVP — "3 thư mục Proposal / Material / Outcome, upload file và video, trạng thái file, tìm kiếm, tải về" (quote p.1, P1 #2). Board 03 "Project Status" — project detail, Project Files tab (L9–L179).

**Open decisions touching this feature:** Project Info tab content (C7, L34); who uploads where (portal OQ-9); file limits (portal OQ-10); file status rules (portal OQ-11). Task List tab (L33) is Phase 2 (`dashboard-tasks`).

## 1. Idea Seed

> "3 thư mục Proposal / Material / Outcome, upload file và video, trạng thái file, tìm kiếm, tải về" (quote P1 #2)

Inside a project, Leap Up and the client share files in three folders, see each file's status, search and download.

## 2. Context

- The project screen (board 03) has a sidebar (Dashboard L21, Projects L30, Files L46), breadcrumb "Projects / 711" (L9), project name (L16), status pill "In Progress" (L19), "Client: 7-Eleven | Due: 15 Dec 2026" (L24) and tabs Project Files / Task List / Project Info (L32–L34).
- Folder cards (L52–L72): **Proposal** — "Proposal deck, approved proposal", "Scope of work"; **Material** — "Client brief, brand assets", "References"; **Outcome Development** — "Creative WIP, final deliverables", "Versions and approval status". The quote calls the third folder "Outcome"; the board label "Outcome Development" is used.
- Files toolbar: "Files" (L81), "Search files..." (L84), "Upload Files" (L83).
- File table columns: Name, Folder, Last Modified, Uploaded By, Status (L98–L102). Sample rows show uploads by both Leap Up and Client (L112, L143, L153) and statuses Approved, Shared, In Review, Final (L113, L144, L164, L179).
- No download button is drawn; the quote requires download (P1 #2).
- Files are stored in Cloudflare R2 (quote §5); ~300 GB after year one.

## 3. User Types

| User Type | Pain Point | Primary Need |
|-----------|-----------|--------------|
| Leap Up member | Files scattered across channels | Share proposal, material and outcome files per project |
| Client | Needs the latest files and a place to send brand assets | Browse, search, download; upload (board shows client uploads) |

## 4. Capabilities Breakdown

### P0 — must have
- Project header and tabs as on board 03 (L9–L34).
- Three folder cards with their descriptions (L52–L72).
- File table with Name / Folder / Last Modified / Uploaded By / Status (L98–L102).
- Upload files and videos (L83; quote P1 #2).
- Search files (L84).
- Download a file (quote P1 #2; control not drawn — placement TBD).
- File status shown (L102; values Approved / Shared / In Review / Final).

### TBD
- Folder filter: clicking a folder card filters the table (inferred from the Proposal card highlight, board 03 visual) — OQ-1.
- Who sets the status, allowed transitions (OQ-4).
- Client upload rights and folders (OQ-3).
- Delete / rename / replace a file — not in the reference (OQ-6).
- Projects list (sidebar "Projects") and "Files" sidebar page — not drawn (OQ-7).

### P2 / other features
- Task List tab → `dashboard-tasks` (P2).
- Project Info tab → C7 OPEN.
- Videos in Outcome Development open in Video Review → `video-review`.

## 5. Core Flows (Happy Path)

### 5.1 Browse and download
1. User opens a project (from the projects list — TBD, OQ-7) → Project Files tab (L32).
2. User sees the three folder cards and the file table.
3. User selects a folder card (filter — OQ-1) or types in "Search files..." (L84).
4. User downloads a file (control TBD — OQ-5).

### 5.2 Upload
1. User presses "Upload Files" (L83).
2. User chooses one or more files and the target folder (folder choice UI TBD — OQ-2).
3. System checks type and size (limits TBD — OQ-8) and stores the files.
4. The file appears in the table with Name, Folder, Last Modified (date), Uploaded By (Leap Up / Client) and a status (initial status TBD — OQ-4).

```
┌──────────────┐ Upload Files ┌───────────────────┐  valid?  ┌──────────────────┐
│ Project Files│ ───────────▶ │ Choose files +    │ ──YES──▶ │ Store file;      │
│ tab (L32)    │              │ folder (TBD)      │          │ row in table     │
└──────┬───────┘              └─────────┬─────────┘          └──────────────────┘
       │ search / folder                │ NO (type/size TBD)
       ▼                                ▼
┌──────────────┐              ┌───────────────────┐
│ Filtered     │              │ Error, wording TBD│
│ table        │              └───────────────────┘
│ ─ no match → │ empty state (wording TBD)
└──────────────┘
```

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | When | YES | NO |
|---|---|---|---|
| D1 | User assigned to the project? | Show files | Refuse (auth-access FR-009) |
| D2 | File type/size allowed? | Store | Error, TBD (OQ-8) |
| D3 | Search matches any file? | Show matches | Empty state, wording TBD |
| D4 | Role allowed to upload to this folder? | Upload | TBD (OQ-3) |

### 6.2 Scenario Matrix

| Action | Leap Up member | Client |
|---|---|---|
| View / search / download | Yes | Yes (own projects) |
| Upload | Yes | Yes per board (L143, L153); folders TBD (OQ-3) |
| Change status | TBD (OQ-4) | TBD (OQ-4) |

### 6.3 State Transitions

```
File status values on the board: Shared · In Review · Approved · Final (L113, L144, L164, L179)
Order, trigger and who sets them: TBD (OQ-4)
```

### 6.4 Interrupted Transactions

| Situation | Keeps | Resume | Cleanup |
|---|---|---|---|
| Browser closed during a large upload | TBD (OQ-9) | TBD | TBD |
| Storage fails | File not listed (assumed) | Upload again | — |

## 7. Validation, Limits & Wording

| Parameter | Value |
|---|---|
| Allowed file types | TBD (OQ-8) — board samples: .pptx, .docx, .mp4, .pdf (L109–L175) |
| Max file size | TBD (OQ-8) |
| Search matches | file name (assumed); other fields TBD (OQ-1) |

| Label (board) | Line |
|---|---|
| "Project Files" · "Task List" · "Project Info" | L32–L34 |
| "Files" · "Search files..." · "Upload Files" | L81, L84, L83 |
| "Name" · "Folder" · "Last Modified" · "Uploaded By" · "Status" | L98–L102 |

Error/success/empty wording: TBD.

## 8. Assumptions

- Board file names, dates and statuses are sample data (L196).
- "Last Modified" shows a date in the board's format "19 Nov 2026" (L111).

## 9. Risks

| Risk | Likelihood | Consequence | Prevention |
|---|---|---|---|
| R1 Large video uploads fail on slow connections | sometimes | Missed review rounds | Decide limits and resume behaviour (OQ-8, OQ-9) |
| R2 Status meaning unclear | often | Clients misread "Approved" vs "Final" | Leap Up defines status rules (OQ-4) |

## 10. Success Criteria

- Leap Up shares a file and the client downloads it in the same project (MVP outcome, quote p.1).

## 11. Open Points

* [ ] OQ-1: Folder card click filters the table? Search covers which fields? TBD.
* [ ] OQ-2: How the folder is chosen on upload. TBD.
* [ ] OQ-3: Client upload rights — which folders? (portal OQ-9). TBD.
* [ ] OQ-4: File status — initial value, who changes it, allowed order (portal OQ-11). TBD.
* [ ] OQ-5: Download control placement; multiple-file download. TBD.
* [ ] OQ-6: Delete / rename / replace / version a file. TBD.
* [ ] OQ-7: Projects list page (sidebar "Projects", L30) and "Files" sidebar page (L46) — not drawn. TBD.
* [ ] OQ-8: Allowed types and max size (portal OQ-10). TBD.
* [ ] OQ-9: Interrupted upload behaviour (portal OQ-15). TBD.
* [ ] OQ-10 (C7): Project Info tab content. TBD.
* [ ] OQ-11: Phone layout of the file table (quote §7). TBD.

## 12. Next Steps

* `/srs project-files`
