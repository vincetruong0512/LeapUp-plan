---
type: srs
feature: project-files
scope: MVP
status: draft
updated: 2026-11-22
links:
  - docs/project-files/brainstorms/project-files.md
  - docs/_sources/2026-11-21-leapup-references/leapup-website-miro-board.md
---

# project-files — Software Requirements Specification

## 1. Scope

Project detail screen with the Project Files tab: three folders, file table with status, upload, search and download. MVP — quote P1 #2; board 03 (L9–L179).

## 2. Actors & Stakeholders

| Actor | Type | Goal | In scope? |
|-------|------|------|-----------|
| Leap Up member | person | Share files with the client | Yes |
| Client | person | Get files; send brand assets | Yes |
| Cloudflare R2 | external | Store files (quote §5) | Yes |

## 3. Functional Requirements (FR)

| ID | Title | Description | Scope | Priority | Verify by | Source |
|----|-------|-------------|-------|----------|-----------|--------|
| FR-project-files-001 | Project header | Show breadcrumb "Projects / {project}", project name, status pill, "Client: {client} \| Due: {date}". | MVP | P0 | demo | board L9, L16, L19, L24 |
| FR-project-files-002 | Project tabs | Show tabs Project Files, Task List, Project Info; Project Files is the MVP tab (Task List = P2, Project Info = OQ-1; what P2 tabs do in Phase 1 = OQ-14). | MVP | P0 | demo | board L32–L34 |
| FR-project-files-003 | Sidebar | Show sidebar Dashboard, Projects, Files with the current item active. Targets of Dashboard (P2) and Files TBD (OQ-2). | MVP | P1 | demo | board L21, L30, L46 |
| FR-project-files-004 | Folder cards | Show three folder cards Proposal, Material, Outcome Development with their two description lines. | MVP | P0 | demo | quote P1 #2; board L52–L72 |
| FR-project-files-005 | File table | Show files with columns Name, Folder, Last Modified, Uploaded By, Status. | MVP | P0 | demo | board L98–L102 |
| FR-project-files-006 | Upload | Members of the project can upload files and videos into a folder (folder choice TBD, OQ-3). | MVP | P0 | demo | quote P1 #2; board L83 |
| FR-project-files-007 | Upload validation | If the file type or size is not allowed, then the system shall reject it (E-project-files-001). Limits TBD (OQ-4). | MVP | P0 | test | brainstorm D2 |
| FR-project-files-008 | Uploaded By | The table shows who uploaded the file as "Leap Up" or "Client". | MVP | P0 | demo | board L101, L112, L143 |
| FR-project-files-009 | File status | Each file shows a status: Shared, In Review, Approved or Final. Rules TBD (OQ-5). Whether Approved / Final are manual labels in Phase 1 or belong to Outcome Approval (P2) is TBD (OQ-13). | MVP | P0 | demo | quote P1 #2; board L113, L144, L164, L179 |
| FR-project-files-010 | Search | User searches files with "Search files..."; the table shows matching files; none → empty state (E-project-files-002). | MVP | P0 | test | quote P1 #2; board L84 |
| FR-project-files-011 | Download | User downloads a file. Control placement TBD (OQ-6). | MVP | P0 | demo | quote P1 #2 |
| FR-project-files-012 | Folder filter | **Provisional — TBD pending OQ-7.** Selecting a folder card shows that folder's files (inferred, not stated in the reference). | MVP | P1 | demo | board 03 visual (Proposal card highlighted) |
| FR-project-files-013 | Project-scoped | Only members of the project see its files (Admin: TBD, auth-access OQ-10); others get E-auth-access-003. | MVP | P0 | test | auth-access FR-009 |
| FR-project-files-014 | Open video | **Provisional — TBD pending OQ-8.** A video in Outcome Development opens in Video Review (inferred from breadcrumb L10). | MVP | P1 | demo | board L10 |

## 4. Non-Functional Requirements (NFR)

| ID | Category | Requirement | Priority | Acceptance |
|----|----------|-------------|----------|------------|
| NFR-project-files-001 | storage | Files are stored in Cloudflare R2. | P0 | quote §5 |
| NFR-project-files-002 | capacity | ~300 GB of data after year one. | P1 | quote §5 |
| NFR-project-files-003 | usability | Usable in a phone browser. | P0 | quote §7; table layout on phone TBD (OQ-9) |
| NFR-project-files-004 | performance | Upload/download speed targets. | — | TBD — Leap Up |
| NFR-project-files-005 | reliability | Automatic backup. | P0 | quote P1 #4 (scope of backup for files TBD) |

## 5. Business Rules

| ID | Rule | Trigger | Implements FR | Source |
|----|------|---------|---------------|--------|
| BR-project-files-001 | Every project has exactly three folders: Proposal, Material, Outcome Development. | Project created | FR-project-files-004 | quote P1 #2; board L52–L54 |
| BR-project-files-002 | Files are visible only to members of their project. | Any view | FR-project-files-013 | board L146 |
| BR-project-files-003 | File status is one of Shared, In Review, Approved, Final. | Status shown/changed | FR-project-files-009 | board L113–L179 |
| BR-project-files-004 | Uploaded By records the uploader's side (Leap Up or Client). | Upload | FR-project-files-008 | board L112, L143 |

## 6. Error Matrix

| Error ID | Title | Trigger | Severity | Related FR | Wording (exact) | Screen state | Recovery |
|----------|-------|---------|----------|------------|-----------------|--------------|----------|
| E-project-files-001 | File not allowed | Type or size outside limits | major | FR-project-files-007 | TBD | Upload rejected | Choose another file |
| E-project-files-002 | No search result | Search matches nothing | minor | FR-project-files-010 | TBD | Empty table | Change the search |
| E-project-files-003 | Upload failed | Upload did not complete: storage or network failure (interrupted upload: OQ-11) | major | FR-project-files-006 | TBD | File not listed | Upload again |
| E-project-files-004 | Empty folder | Folder has no files | minor | FR-project-files-012 | TBD | Empty table | Upload (if allowed, OQ-3) |
| — (gap) | Download failed | Storage unavailable or file removed | — | FR-project-files-011 | TBD | TBD | TBD (OQ-15) |

## 7. Success Criteria

| ID | Business outcome | Measured by | Target |
|----|------------------|-------------|--------|
| SC-project-files-01 | Leap Up shares a file and the client downloads it | Demo with two accounts | Works end to end |
| SC-project-files-02 | Clients never see files of other projects | Access test | 0 leaks |

## 8. Data Entities (summary)

- **File:** name, folder, last modified date, uploaded by (user + side), status, size, type.

## 9. Flows (summary)

Open project → Project Files tab → filter / search → download · Upload → validate → listed.

## 10. Screens (summary)

| Screen | Board |
|---|---|
| Project detail — Project Files tab | 03 (L9–L179) |
| Upload (file + folder choice) | not drawn — TBD |
| Empty / no-result states | not drawn — TBD |

## 11. Constraints, Dependencies & Assumptions

| Constraint | Source / Owner |
|------------|----------------|
| Storage on Cloudflare R2; Leap Up creates the account | quote §5, §7 |

| Dependency | Owner | Blocks if not ready |
|------------|-------|---------------------|
| Project + members exist | `admin` | No project to show |
| Sign-in and access check | `auth-access` | Access control |

| Assumption | Invalidates if wrong |
|------------|----------------------|
| Folder card click filters the table | FR-project-files-012 |

## 12. Open Questions

- [ ] OQ-1 (C7): Project Info tab content.
- [ ] OQ-2: Targets of sidebar "Dashboard" in Phase 1 and "Files"; projects list page (sidebar "Projects").
- [ ] OQ-3: Folder choice on upload; client upload rights per folder; several files at once where one is rejected.
- [ ] OQ-4: Allowed types and max size.
- [ ] OQ-5: File status — initial value, who changes it, transitions.
- [ ] OQ-6: Download control placement.
- [ ] OQ-7: Folder card filter behaviour.
- [ ] OQ-8: How a video opens Video Review; which round opens; what "open" does for a video outside Outcome Development (e.g. `711_Brand Assets_V1.mp4` in Material, L149) or a non-video file.
- [ ] OQ-9: Phone layout of the table.
- [ ] OQ-10: Delete / rename / replace a file.
- [ ] OQ-11: Interrupted upload behaviour.
- [ ] OQ-12: All wording E-project-files-001…004.
- [ ] OQ-13: Are file statuses Approved / Final manual labels in Phase 1, or reserved for Outcome Approval (P2 #3: "Duyệt từng version… ký duyệt bản cuối")? (review SBA-11; scope-creep risk).
- [ ] OQ-14: What the P2 tab "Task List" and sidebar "Dashboard" do in Phase 1 — hidden, disabled or placeholder (review SBA-17).
- [ ] OQ-15: Download failure — trigger, error code, wording (review QA-2).
- [ ] OQ-16: Which fields search covers (file name assumed), case sensitivity, and how search combines with the folder filter (brainstorm OQ-1; restored by review SBA-15).
- [ ] OQ-17: File ↔ review link — is a Video Review version the same record as the Outcome Development file; is file status "In Review" (L164) synced with the round status; what happens to comments when a file is replaced or deleted? Shared with video-review OQ-10 (review SBA-12). Before Sprint 1.
- [ ] OQ-18: Third folder label — quote P1 #2 says "Outcome", the board says "Outcome Development" (L54). The board label is used because the UI follows the Miro design (quote §1); confirm (review SBA-22).
