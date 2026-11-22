---
type: portal-userflow
feature: portal
updated: 2026-11-22
status: draft
figma: file "Untitled", page "User Flows" (3 frames, Reqwise userflow, layout audit clean)
---

# Leap Up portal: end-to-end user journeys per role

Cross-feature view: one journey per user type, stitched from the approved per-feature user flows.
It adds no new screens or rules; every step traces to a feature flow below. Scope: **MVP + P2**
(P2 steps prefixed `P2 ·`). `OUT` (Material Library, Storyboard Review) is not drawn.

Roles: Admin, Leap Up member, Client. These are provisional (auth-access FR-010; C4 still OPEN for approver roles).
Decisions marked **TBD** are open questions drawn with both branches, not decisions.

| Source flow | Used for |
|---|---|
| [auth-access userflow](../auth-access/srs/auth-access-userflow.md) | Sign in, errors, landing, sign out (all roles) |
| [admin userflow](../admin/srs/admin-userflow.md) | Admin set-up |
| [project-files userflow](../project-files/srs/project-files-userflow.md) | Files: search, upload, download, open video |
| [video-review userflow](../video-review/srs/video-review-userflow.md) | Review rounds, comments, resolve |
| [dashboard-tasks userflow](../dashboard-tasks/srs/dashboard-tasks-userflow.md) | P2 Home, Action Required, tasks |
| [production-timeline userflow](../production-timeline/srs/production-timeline-userflow.md) | P2 timeline, Upload inputs |
| [outcome-approval userflow](../outcome-approval/srs/outcome-approval-userflow.md) | P2 version approval, change requests, sign-off |
| [email-notifications userflow](../email-notifications/srs/email-notifications-userflow.md) | P2 e-mail triggers |

## 1. Admin

```mermaid
flowchart TD
  login["Login (board 01)"]
  filled{"User ID and Password filled?"}
  match{"Credentials match?"}
  loginErr("Login error state")
  landing["Landing · all projects (design TBD, OQ-1)"]
  admin["Admin page (no board design, C3)"]
  projForm["Create project form"]
  projOk{"Required fields filled?"}
  acctForm["Create client account form"]
  acctOk{"User ID unique?"}
  formErr("Form error state")
  members["Assign members · role Leap Up / Client"]
  work(["Open a project · continues as Leap Up member journey"])
  signout(["Signed out · back to Login"])
  login -->|"Sign In"| filled
  filled -->|"Yes"| match
  filled -->|"No · E-auth-access-002"| loginErr
  match -->|"Yes"| landing
  match -->|"No · E-auth-access-001"| loginErr
  loginErr -.->|"Re-enter"| login
  landing -->|"Admin pages"| admin
  admin -->|"Create project"| projForm
  projForm -->|"Save"| projOk
  projOk -->|"Yes"| members
  projOk -->|"No · E-admin-001"| formErr
  admin -->|"Create client account"| acctForm
  acctForm -->|"Save"| acctOk
  acctOk -->|"Yes"| members
  acctOk -->|"No · E-admin-002"| formErr
  formErr -.->|"Fix and retry"| admin
  members -.->|"Done"| admin
  landing -->|"Open project"| work
  landing -->|"Sign out"| signout
  admin -->|"Sign out · placement TBD"| signout
  classDef happy fill:#d4edda,stroke:#28a745
  classDef error fill:#f8d7da,stroke:#dc3545
  classDef edge fill:#fff3cd,stroke:#ffc107
  class login,filled,match,landing,admin,projForm,projOk,acctForm,acctOk,members,work,signout happy
  class loginErr,formErr error
```

## 2. Leap Up member

```mermaid
flowchart TD
  login["Login (board 01)"]
  filled{"User ID and Password filled?"}
  match{"Credentials match?"}
  loginErr("Login error state")
  assigned{"Assigned projects?"}
  noProj("Landing · no projects")
  landing["Landing · assigned projects (design TBD, OQ-1)"]
  files["Project Files tab (board 03)"]
  found{"Search or folder has files?"}
  listed("Matching files shown")
  filesEmpty("Empty or no-result state")
  upload["Upload · choose files and folder (design TBD)"]
  uploadOk{"Type and size allowed?"}
  uploaded("Row added to file table")
  uploadErr("Upload error state")
  download(["File downloaded"])
  hasVideo{"Round has a video?"}
  noVideo("No video yet state")
  review["Video Review · current round (board 07)"]
  plays{"Video plays?"}
  playing("Playing with timeline markers")
  playErr("Playback error state")
  commentOk{"Comment text entered?"}
  commentSaved("Comment saved as Open + marker")
  commentErr("Empty comment state")
  mayResolve{"May resolve? (TBD, OQ-2)"}
  resolved("Comment marked Resolved")
  noResolve("Resolve not available (TBD)")
  otherRound("Selected round shown")
  email[["P2 · E-mail to project members"]]
  home["P2 · Home dashboard (board 02)"]
  actions{"P2 · Action Required items?"}
  homeEmpty("P2 · No action required state")
  tasks["P2 · Update Task List / By Project"]
  taskOk{"P2 · Task name entered?"}
  taskSaved("P2 · Task saved")
  taskErr("P2 · Task form error state")
  timeline["P2 · Production Timeline (board 04)"]
  editStage("P2 · Stage or milestone edited (controls TBD)")
  signoff["P2 · Revision & Sign-off (board 08)"]
  cr("P2 · Change request recorded")
  signout(["Signed out · back to Login"])
  login -->|"Sign In"| filled
  filled -->|"Yes"| match
  filled -->|"No · E-auth-access-002"| loginErr
  match -->|"Yes"| assigned
  match -->|"No · E-auth-access-001"| loginErr
  loginErr -.->|"Re-enter"| login
  assigned -->|"1 or more"| landing
  assigned -->|"None · E-auth-access-004"| noProj
  noProj -->|"Sign out"| signout
  landing -->|"Open project"| files
  files -->|"Search or select folder"| found
  found -->|"Yes"| listed
  found -->|"No match · E-project-files-002"| filesEmpty
  found -->|"Empty folder · E-project-files-004"| filesEmpty
  listed -.->|"Back"| files
  filesEmpty -.->|"Clear search"| files
  files -->|"Upload Files"| upload
  upload -->|"Upload"| uploadOk
  uploadOk -->|"Yes"| uploaded
  uploadOk -->|"Wrong type · E-project-files-001"| uploadErr
  uploadOk -->|"Too large · E-project-files-003"| uploadErr
  uploadErr -.->|"Try again"| upload
  uploaded -.->|"Back"| files
  files -->|"Download"| download
  files -->|"Open video (OQ-8)"| hasVideo
  hasVideo -->|"Yes"| review
  hasVideo -->|"No · E-video-review-004"| noVideo
  noVideo -.->|"Select another round"| otherRound
  review -->|"Play"| plays
  plays -->|"Yes"| playing
  plays -->|"No · E-video-review-002"| playErr
  playing -.->|"Pause"| review
  playErr -.->|"Retry"| review
  review -->|"Add comment at time"| commentOk
  commentOk -->|"Yes"| commentSaved
  commentOk -->|"No · E-video-review-001"| commentErr
  commentErr -.->|"Type comment"| review
  commentSaved -.->|"Back to list"| review
  commentSaved -->|"P2 · notify"| email
  review -->|"Resolve comment"| mayResolve
  mayResolve -->|"Yes"| resolved
  mayResolve -->|"No"| noResolve
  resolved -.->|"Status updated"| review
  noResolve -.->|"Back"| review
  review -->|"Version History"| otherRound
  otherRound -.->|"Show that round"| review
  review -->|"P2 · Open Revision & Sign-off"| signoff
  signoff -->|"Change request · Save"| cr
  cr -.->|"Back"| signoff
  landing -->|"P2 · Home"| home
  home -->|"Load"| actions
  actions -->|"Yes · Review Now (target OQ-3)"| hasVideo
  actions -->|"No · E-dashboard-tasks-002"| homeEmpty
  home -->|"Update Task List tab"| tasks
  homeEmpty -->|"Update Task List tab"| tasks
  tasks -->|"Add task · Save"| taskOk
  taskOk -->|"Yes"| taskSaved
  taskOk -->|"No · E-dashboard-tasks-001"| taskErr
  taskSaved -.->|"Back to list"| tasks
  taskErr -.->|"Fix"| tasks
  landing -->|"P2 · Open timeline (entry TBD)"| timeline
  timeline -->|"Edit stage or milestone"| editStage
  editStage -.->|"Save"| timeline
  landing -->|"Sign out"| signout
  classDef happy fill:#d4edda,stroke:#28a745
  classDef error fill:#f8d7da,stroke:#dc3545
  classDef edge fill:#fff3cd,stroke:#ffc107
  class login,filled,match,assigned,landing,files,found,listed,upload,uploadOk,uploaded,download,hasVideo,review,plays,playing,commentOk,commentSaved,resolved,otherRound,email,home,actions,tasks,taskOk,taskSaved,timeline,editStage,signoff,cr,signout happy
  class loginErr,uploadErr,playErr,commentErr,taskErr error
  class noProj,filesEmpty,noVideo,mayResolve,noResolve,homeEmpty edge
```

## 3. Client

```mermaid
flowchart TD
  mail[["P2 · E-mail: new video"]]
  login["Login (board 01)"]
  filled{"User ID and Password filled?"}
  match{"Credentials match?"}
  loginErr("Login error state")
  assigned{"Assigned projects?"}
  noProj("Landing · no projects")
  landing["Landing · assigned projects only (design TBD, OQ-1)"]
  files["Project Files tab (board 03)"]
  found{"Search or folder has files?"}
  listed("Matching files shown")
  filesEmpty("Empty or no-result state")
  mayUpload{"Client may upload here? (TBD, OQ-3)"}
  noUpload("Upload not available (TBD)")
  upload["Upload brand assets · choose files and folder (design TBD)"]
  uploadOk{"Type and size allowed?"}
  uploaded("Row added to file table")
  uploadErr("Upload error state")
  download(["File downloaded"])
  hasVideo{"Round has a video?"}
  noVideo("No video yet state")
  review["Video Review · current round (board 07)"]
  plays{"Video plays?"}
  playing("Playing with timeline markers")
  playErr("Playback error state")
  commentOk{"Comment text entered?"}
  commentSaved("Comment saved as Open + marker")
  commentErr("Empty comment state")
  mayResolve{"May resolve? (TBD, OQ-2)"}
  resolved("Comment marked Resolved")
  noResolve("Resolve not available (TBD)")
  otherRound("Selected round shown")
  home["P2 · Home (client content TBD, OQ-4)"]
  actions{"P2 · Action Required items?"}
  homeEmpty("P2 · No action required state")
  timeline["P2 · Production Timeline (board 04)"]
  inputs["P2 · Upload inputs (C6 OPEN)"]
  inputOk{"P2 · Upload OK?"}
  received("P2 · Input marked Received")
  inputErr("P2 · Upload inputs error state")
  mayApprove{"P2 · May approve? (TBD, C4)"}
  approved("P2 · Version approved · log entry")
  notAllowed("P2 · Not allowed state")
  signoff["P2 · Revision & Sign-off (board 08)"]
  checks{"P2 · All sign-off checks ticked?"}
  incomplete("P2 · Checklist incomplete state")
  final(["P2 · Final version signed off"])
  signout(["Signed out · back to Login"])
  mail -->|"Open link (target TBD)"| login
  login -->|"Sign In"| filled
  filled -->|"Yes"| match
  filled -->|"No · E-auth-access-002"| loginErr
  match -->|"Yes"| assigned
  match -->|"No · E-auth-access-001"| loginErr
  loginErr -.->|"Re-enter"| login
  assigned -->|"1 or more"| landing
  assigned -->|"None · E-auth-access-004"| noProj
  noProj -->|"Sign out"| signout
  landing -->|"Open project"| files
  files -->|"Search or select folder"| found
  found -->|"Yes"| listed
  found -->|"No match · E-project-files-002"| filesEmpty
  found -->|"Empty folder · E-project-files-004"| filesEmpty
  listed -.->|"Back"| files
  filesEmpty -.->|"Clear search"| files
  files -->|"Upload Files"| mayUpload
  mayUpload -->|"Yes"| upload
  mayUpload -->|"No"| noUpload
  noUpload -.->|"Back"| files
  upload -->|"Upload"| uploadOk
  uploadOk -->|"Yes"| uploaded
  uploadOk -->|"Wrong type · E-project-files-001"| uploadErr
  uploadOk -->|"Too large · E-project-files-003"| uploadErr
  uploadErr -.->|"Try again"| upload
  uploaded -.->|"Back"| files
  files -->|"Download"| download
  files -->|"Open video (OQ-8)"| hasVideo
  hasVideo -->|"Yes"| review
  hasVideo -->|"No · E-video-review-004"| noVideo
  noVideo -.->|"Select another round"| otherRound
  review -->|"Play"| plays
  plays -->|"Yes"| playing
  plays -->|"No · E-video-review-002"| playErr
  playing -.->|"Pause"| review
  playErr -.->|"Retry"| review
  review -->|"Add comment at time"| commentOk
  commentOk -->|"Yes"| commentSaved
  commentOk -->|"No · E-video-review-001"| commentErr
  commentErr -.->|"Type comment"| review
  commentSaved -.->|"Back to list"| review
  review -->|"Resolve comment"| mayResolve
  mayResolve -->|"Yes"| resolved
  mayResolve -->|"No"| noResolve
  resolved -.->|"Status updated"| review
  noResolve -.->|"Back"| review
  review -->|"Version History"| otherRound
  otherRound -.->|"Show that round"| review
  review -->|"P2 · Approve version (control TBD)"| mayApprove
  mayApprove -->|"Yes"| approved
  mayApprove -->|"No · E-outcome-approval-001"| notAllowed
  notAllowed -.->|"Back"| review
  approved -->|"Open Revision & Sign-off"| signoff
  signoff -->|"Approve final version"| checks
  checks -->|"Yes"| final
  checks -->|"No · E-outcome-approval-002"| incomplete
  incomplete -.->|"Tick items"| signoff
  landing -->|"P2 · Home"| home
  home -->|"Load"| actions
  actions -->|"Yes · Review Now (target OQ-3)"| hasVideo
  actions -->|"No · E-dashboard-tasks-002"| homeEmpty
  homeEmpty -.->|"Back to projects"| landing
  landing -->|"P2 · Open timeline (entry TBD)"| timeline
  timeline -->|"Upload inputs"| inputs
  inputs -->|"Upload"| inputOk
  inputOk -->|"Yes"| received
  inputOk -->|"No · E-production-timeline-002"| inputErr
  received -.->|"Back"| timeline
  inputErr -.->|"Retry"| inputs
  landing -->|"Sign out"| signout
  classDef happy fill:#d4edda,stroke:#28a745
  classDef error fill:#f8d7da,stroke:#dc3545
  classDef edge fill:#fff3cd,stroke:#ffc107
  class mail,login,filled,match,assigned,landing,files,found,listed,upload,uploadOk,uploaded,download,hasVideo,review,plays,playing,commentOk,commentSaved,resolved,otherRound,home,actions,timeline,inputs,inputOk,received,approved,signoff,checks,final,signout happy
  class loginErr,uploadErr,playErr,commentErr,inputErr,notAllowed,incomplete error
  class noProj,filesEmpty,noVideo,mayUpload,noUpload,mayResolve,noResolve,homeEmpty,mayApprove edge
```

## 4. Counts (check against Figma)

| Journey | Nodes | Edges | Return edges | Figma frame |
|---|---|---|---|---|
| Admin | 14 | 20 | 3 | `Userflow · Admin · end-to-end journey` |
| Leap Up member | 42 | 64 | 17 | `Userflow · Leap Up member · end-to-end journey` |
| Client | 48 | 71 | 19 | `Userflow · Client · end-to-end journey` |

## 5. Gaps shown in the journeys (open, not decided)

| Gap | Where | Source |
|---|---|---|
| Landing / projects list design | all roles | auth-access OQ-1, project-files OQ-2 |
| Sign-out placement | all roles | auth-access OQ-2 |
| Admin screens have no design | Admin | C3, admin OQ-1 |
| Client upload rights per folder; upload screen | Client, Leap Up | project-files OQ-3 |
| How a video opens Video Review | Leap Up, Client | project-files OQ-8 |
| Who may resolve comments | Leap Up, Client | video-review OQ-2 |
| How a new version / round is added (no control drawn; **not in the journeys**) | Leap Up | video-review OQ-3 |
| Action Required sources and Review Now target; client home | P2 | dashboard-tasks OQ-3, OQ-4 |
| Timeline entry and edit controls; Client Inputs in scope | P2 | production-timeline OQ-2, OQ-4, OQ-5 (C6) |
| Who may approve; approval control location | P2 Client | outcome-approval OQ-1, OQ-2 (C4) |
| E-mail link target; recipients per trigger | P2 | email-notifications OQ-2, OQ-3 |

Not checked by any tool: whether these journeys match how Leap Up and its clients actually work.
