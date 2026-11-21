# LeapUp-plan

Planning and overview workspace for the **Leap Up Client Project Portal**: a web app where Leap Up
(a video-production agency) and its clients follow one production project in one place. They exchange
files, review video at exact timecodes, track tasks, log change requests and sign off the final cut.
This repo holds the sources, analysis and plans. It is not the app's codebase.

## Project goal and MVP

- **Users:** about 50 (Leap Up staff and client reviewers). Responsive web app, usable on mobile; no
  native app. One UI language.
- **Access:** sign in with a User ID issued per client. Permissions are per project (Leap Up / Client).

| Phase | Scope | Priority |
|---|---|---|
| **Phase 1 = MVP** (month 1) | Foundation and admin (login, per-project roles, create projects and client accounts, assign members) · **Project Files** (Proposal / Material / Outcome folders, upload, status, search, download) · **Video Review** (online player, timecoded comments, timeline markers, rounds and versions) · deployment and handover | **Focus here first** |
| Phase 2 (month 2) | Dashboard and task list (Action Required) · Production Timeline (5 stages, milestones) · Outcome Approval (per-version approval, change requests, approval log, final sign-off) · email notifications · testing and acceptance | Plan, don't build ahead |
| Out of scope (quoted) | Material Library · Storyboard Review · in-app notifications · realtime updates · multi-company SaaS | Log as post-MVP; don't design for them. Exception (BA, 2026-11-22): Material Library and Storyboard Review are documented in full, tagged OUT, as change-request candidates — never scheduled without a CR |

**MVP outcome:** Leap Up can create a project, invite the client, share files and review video with the
client, end to end.

Open scope questions (quote vs Miro wireframe, e.g. realtime task list, approver roles, revision quota):
`docs/_sources/2026-11-21-leapup-references/_comparison.md`. Resolve them; don't silently pick a side.

## Where things are

- `references/`: original source files (gitignored; may hold contacts and pricing).
- `docs/_sources/`: Markdown conversions made by `/doc-to-md` (gitignored). Read these, not the PDFs.
- `.claude/skills/`: project skills. `.claude/rules/`: rules every skill and task follows.

## Project skills

- `/doc-to-md`: turns any source (PDF, Office, Miro/Figma exports, images, CSV) into verified Markdown
  in `docs/_sources/`, tagging what it finds by MVP scope. Supports all phases; run it before analysing a new source.
- `/brainstorm`: pipeline step 1. Adaptive interview for one feature, grounded in the quote and board, resolves
  OPEN items, output `docs/{feature}/brainstorms/`. MVP. (English adaptation of a licensed AI4BA BA-Kit skill;
  gitignored, do not commit or share.)
- `/brd`: optional, outside the pipeline. Business requirements (problem, objectives + success measures,
  current/future/gap, scope MVP/P2/OUT, business rules, risks); recommended once as `/brd portal` before `/srs`.
  Never copies quote prices or contacts. MVP. (Licensed AI4BA BA-Kit adaptation; gitignored.)
- Pipeline steps 2–6 (licensed AI4BA BA-Kit adaptations, English, gitignored), all MVP:
  `/srs` core spec (FR/NFR/BR/error matrix) · `/user-flow` Mermaid flow + flow split · `/wireframe-html`
  B&W wireframes following the Miro board · `/userstory` + `/ac` stories with acceptance criteria ·
  `/jira` two-way sync (inspect by default; push needs a yes each time; no Atlassian MCP yet → import file).
  Shared rules for them: `.claude/skills/_ba-kit/conventions.md`; reviewer agents in `.claude/agents/`.
- Supporting (after `/srs`, licensed BA-Kit adaptations, gitignored), MVP + P2: `/usecase` fully-dressed use cases
  with UC ↔ FR ↔ story ↔ error trace · `/sequence` and `/activity` Mermaid diagrams per use case in
  `docs/{feature}/srs/{feature}-flows.md`.
- `/prototype-html` (after `/wireframe-html`, licensed BA-Kit adaptation, gitignored), MVP + P2: one clickable,
  state-driven HTML prototype per feature or `portal` (all quoted flows in one app), neutral greyscale; never OUT.
  Comment layer (syncs to jsonbin.io) off by default; warn and get a yes before embedding it.

## Rules

@.claude/rules/mvp-focus.md
@.claude/rules/skill-authoring.md
@.claude/rules/requirements-pipeline.md

Requirements flow: `/doc-to-md` (sources) → `/brainstorm → /srs → /user-flow → /wireframe-html → /userstory → /jira`, per MVP feature.

## Conventions

- Source text stays in its language (Vietnamese stays Vietnamese). Write analysis in English unless asked.
- Cite sources by file and line (`L199`, `p. 2`). Mark anything inferred as inferred.
- Never copy pricing, phone numbers or e-mail addresses from `references/` into tracked files.
