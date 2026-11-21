---
type: technical-solution-design
feature: portal
status: proposal
updated: 2026-11-22
links:
  - docs/portal/delivery-plan.md
  - docs/_sources/2026-11-21-leapup-references/bao-gia-leapup-mvp.md
---

# Leap Up Client Project Portal — Technical Solution Design (proposal)

**How to read this:** 🟢 **Fixed** = stated in the quote. 🔵 **Proposal** = a suggestion for the developer to accept or replace; it is not a requirement and not agreed with Leap Up. The developer owns the final technical choices.

## 1. Fixed constraints (from the quote)

| # | Constraint | Source |
|---|---|---|
| 🟢 F1 | Web app in the browser, responsive, usable on phones; no native app | quote §7, P1 #1 |
| 🟢 F2 | ~50 users; ~300 GB of data after year one | quote §1, §5 |
| 🟢 F3 | VPS server for the application and database | quote §5 |
| 🟢 F4 | Video, image and document storage on Cloudflare R2 | quote §5 |
| 🟢 F5 | E-mail through a free-tier sending service (Phase 2) | quote §5, P2 #4 |
| 🟢 F6 | Domain, SSL, automatic backup, automatic deploy | quote P1 #4 |
| 🟢 F7 | Sign-in with User ID; permissions per project (Leap Up / Client) | quote P1 #1 |
| 🟢 F8 | No realtime updates, no in-app notifications, no multi-company | quote §7 |
| 🟢 F9 | Leap Up owns the infrastructure accounts (server, storage, domain) | quote §7 |
| 🟢 F10 | Full source code, installation guide and user guide handed over | quote §6 |

## 2. Architecture overview (🔵 proposal)

```
 Browser (desktop / phone)
   │  HTTPS (F6)
   ▼
┌───────────────────────────── VPS (F3) ─────────────────────────────┐
│  Reverse proxy (TLS)  ──▶  Web application (one deployable)         │
│                             • pages (server-rendered or SPA)        │
│                             • API + access check per project        │
│                             • background job runner (e-mail, P2)    │
│                           ──▶  Relational database                  │
└──────────────────────────────┬──────────────────────────────────────┘
                               │ signed upload / download URLs
                               ▼
                      Cloudflare R2 bucket (F4)   ◀── browser uploads / plays video directly
                               ▲
                      nightly DB backup copied here (F6)
   E-mail service (F5, Phase 2) ◀── job runner
```

- 🔵 **One application, one database.** ~50 users do not need services or queues beyond a simple job table.
- 🔵 **Files never pass through the VPS.** The app issues short-lived signed URLs; the browser uploads to and downloads/streams from R2 directly. This keeps VPS bandwidth and disk small for ~300 GB.
- 🔵 **Video playback** with the browser's built-in player over HTTP range requests from R2. Requires an MP4 (H.264/AAC) upload format — **TBD with Leap Up** (project-files OQ-4). No transcoding is quoted; adding it would be a change request.

## 3. Stack options (🔵 proposal — developer chooses)

| Layer | Option A | Option B | Notes |
|---|---|---|---|
| Web app | Next.js (TypeScript) | Laravel (PHP) | Both handle server pages + API in one deployable |
| Database | PostgreSQL | PostgreSQL / MySQL | Relational fits projects, members, files, rounds, comments |
| ORM / migrations | Prisma | Eloquent | Migrations kept in the repo for handover (F10) |
| Storage SDK | S3-compatible client for R2 | same | R2 is S3-compatible |
| E-mail (P2) | Free tier of a transactional service (e.g. Resend, Brevo) | same | Pick one whose free tier covers ~50 users (F5) |
| Deploy | Docker Compose on the VPS, GitHub Actions on push to `main` | same | "Tự động deploy" (F6) |

## 4. Data model (🔵 proposal, derived from the specs)

```
User(id, user_id UNIQUE case-insensitive, password_hash, display_name, role: ADMIN|MEMBER, email NULL [P2], active)
Project(id, name, client_name, description, due_date, status)            -- fields TBD (admin OQ-3)
ProjectMember(project_id, user_id, side: LEAP_UP|CLIENT)                  -- per-project permission (F7)
Folder(id, project_id, kind: PROPOSAL|MATERIAL|OUTCOME_DEVELOPMENT)       -- 3 per project
File(id, project_id, folder_id, name, r2_key, size, mime, uploaded_by, uploaded_side, status: SHARED|IN_REVIEW|APPROVED|FINAL, modified_at)
Round(id, project_id, number, status: UPCOMING|IN_REVIEW|REVIEWED, date, change_text, status_text)
Version(id, round_id, file_id, label)                                    -- round vs version model TBD (video-review OQ-3)
Comment(id, version_id, author_id, timecode_seconds, text, status: OPEN|RESOLVED, created_at)
-- Phase 2
Task(id, project_id, name, owner, due_date, status: TO_DO|IN_PROGRESS|PENDING_REVIEW|COMPLETED)
Stage(id, project_id, number, name, status, start_date, end_date); Milestone(id, project_id, name, owner, due_date, status)
Approval(id, project_id, version_id NULL, approver_id, type: VERSION|FINAL, approved_at)    -- append-only
ChangeRequest(id, project_id, request, round_no, scope: IN|OUT, cost NULL, status)
EmailLog(id, event, recipient_id, sent_at, result)
```

Phase 1 already includes `Round`, `Version` and `File.status` so Outcome Approval (P2) can attach approvals without migration pain (`_project-fit.md` design notes).

## 5. Access control (🔵 proposal for 🟢 F7)

- 🔵 One server-side check used by every project route and every signed-URL request: *user is Admin, or is a member of the project*. Covers FR-auth-access-009, BR-project-files-002 and the video and comment routes.
- 🔵 Signed R2 URLs are issued only after that check and expire after a short time (e.g. 15 minutes — value for the developer).
- 🔵 Automated test with two client accounts on every project route (SC-auth-access-01).

## 6. Security (🔵 proposal)

| Topic | Proposal | Requirement status |
|---|---|---|
| Passwords | Slow hash (argon2id or bcrypt); never stored or shown in clear | Password rules TBD (auth-access OQ-7) |
| Sessions | HTTP-only, Secure, SameSite cookies | Expiry TBD (auth-access OQ-4) |
| Brute force | Rate limiting on sign-in at the proxy/app | Lockout rule TBD (auth-access OQ-3) |
| Transport | TLS certificates with automatic renewal | 🟢 F6 |
| Uploads | Type/size check before issuing an upload URL; R2 bucket private | Limits TBD (project-files OQ-4) |
| Web | CSRF protection, output escaping, security headers | — |

## 7. Large uploads (🔵 proposal)

- R2 multipart upload from the browser for big videos (parts of e.g. 10–100 MB), with a progress bar; parts can be retried.
- A file row is created only when the upload completes (matches E-project-files-003: nothing listed on failure).
- Resume after the browser closes: possible with multipart, but behaviour is **TBD** (project-files OQ-11).

## 8. Backup and recovery (🔵 proposal for 🟢 F6)

| Item | Proposal |
|---|---|
| Database | Nightly dump, compressed, copied to a separate R2 bucket; keep e.g. 30 days |
| Files in R2 | Bucket kept private; whether to keep a second copy is a cost decision for Leap Up |
| Restore test | Once before Phase 1 handover, documented in the installation guide |

## 9. Environments and deploy (🔵 proposal)

- **Production** on the VPS; **staging** for demos every 2 weeks (on the same VPS, separate database and bucket prefix) — cost check with Leap Up.
- Push to `main` → tests → build → deploy (F6). Database migrations run in the deploy.
- Basic uptime check and error log; no paid monitoring.

## 10. Phase 2 hooks (🔵 proposal)

- **E-mail:** events (new version, new comment, approval) write a row to a job table; a worker sends through the e-mail service and records `EmailLog` (FR-email-notifications-001…003). No realtime (F8).
- **Dashboard counts:** computed on page load from tasks and projects; no caching needed at ~50 users.
- **Approvals:** append-only table so the Approval Log stays reliable (NFR-outcome-approval-001).

## 11. Sizing and running cost (🟢 from quote §5)

~50 users and ~300 GB after year one fit one small VPS plus R2; the quote's monthly estimate covers VPS, R2, free-tier e-mail and domain. Amounts are in the quote and not repeated here.

## 12. Technical open points

- Video format rule (MP4 H.264?) and max size — needed before Sprint 1.
- Staging environment cost.
- Second copy of R2 files for backup.
- Session/lockout values once Leap Up decides (auth-access OQ-3, OQ-4).
