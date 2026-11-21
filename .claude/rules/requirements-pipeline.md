# Rule: requirements pipeline

Every Leap Up requirement goes through this pipeline, one feature at a time, in this order:

```
/brainstorm → /srs → /user-flow → /wireframe-html → /userstory → /jira
```

Step 0 is always [`/doc-to-md`](../skills/doc-to-md/SKILL.md): any new source document is converted
and verified before it feeds step 1. Steps read the Markdown in `docs/_sources/`, never raw PDFs.

## Steps and handoffs

| # | Step | Reads | Produces | Gate before next step |
|---|---|---|---|---|
| 1 | `/brainstorm <feature>` | `docs/_sources/…` (quote, board), `CLAUDE.md` scope | `docs/{feature}/brainstorms/{idea}.md` | Scope and open questions agreed with the user |
| 2 | `/srs {feature}` | brainstorm | `docs/{feature}/srs/{feature}-spec.md`: FR / NFR / business rules / errors / success criteria | Every FR traced to a source line or a user decision |
| 3 | `/user-flow {feature}` | spec | `docs/{feature}/srs/{feature}-userflow.md` (mermaid, happy / error / edge) | Every screen and button mapped. This file is the only source of flow splits |
| 4 | `/wireframe-html {feature}` | userflow + Miro board (`leapup-website-miro-board.md`) | HTML wireframes per flow + `{feature}-wireframe.html` entry page | Matches the agreed Miro design; deviations listed |
| 5 | `/userstory {feature}` | spec FR + flows + screens | `docs/{feature}/userstories/{feature}-story-index.md` + `us-{NNN}.md` with AC | Every FR covered by ≥ 1 story; every story has AC |
| 6 | `/jira {feature}` | story index | Jira Epic (feature) → Stories → AC sub-tasks | **Explicit user approval of each push** |

## Rules

1. **No skipping, no reordering.** A step starts only when the previous step's output exists and the user
   has approved it. If an upstream file changes, re-run the downstream steps that depend on it, or
   mark them stale.
2. **MVP first** (per [mvp-focus.md](mvp-focus.md)). Run the pipeline for `MVP` features before any `P2`
   feature. Never run it for `OUT` features. An `OPEN` question that touches the feature is resolved in
   step 1, not guessed later. Suggested MVP order: `auth-access` → `admin` → `project-files` → `video-review`.
3. **One feature slug end to end.** The same kebab-case slug is used in every step and path so the chain
   stays traceable (brainstorm → FR → flow → screen → story → Jira key).
4. **Traceability is the check.** Each step cites its upstream IDs: FR → brainstorm/source line;
   flow/screen → FR; story → FR + screen; Jira issue → story. Each step reports any upstream item it left
   uncovered, as a gap rather than a silent drop.
5. **Wireframes follow the agreed design.** The Miro board is the agreed design (quote p.1). Step 4 adapts
   it to the spec and must not invent a new layout. Admin (no wireframe yet, OPEN C3) is the exception,
   designed here and confirmed with the user.
6. **`/jira` is outward-facing.** Show what will be created or updated (issue type, summary, parent) and
   wait for a yes every time. Never push stories whose status is not approved.
7. **Status per feature.** Keep `docs/{feature}/README.md` with one line per step:
   `done / in progress / stale / not started` + date.

## Skill availability (2026-11-21)

**All six steps are installed** (English, adapted for Leap Up, from the licensed AI4BA BA-Kit):
`/brainstorm` · `/srs` · `/user-flow` · `/wireframe-html` · `/userstory` + `/ac` · `/jira`. Shared rules:
`.claude/skills/_ba-kit/conventions.md`; reviewer agents `senior-ba`, `qa-reviewer`, `tech-reviewer`,
`uxui-reviewer`, `flow-reviewer`; Mermaid checker `.claude/scripts/mermaid-verify.mjs` (patched for Windows).
None has been run on a real Leap Up feature yet — the first run of each counts as its test.

Optional, outside the pipeline: `/brd` (installed), after `/brainstorm` and before `/srs` when a business
case is needed; never a required step.

Licence: keep copyright notices and watermarks; keep all BA-Kit files gitignored.

**Tier 2 installed 2026-11-22 (supporting, outside the six steps; run after `/srs`):** `/usecase` (Cockburn use
cases + trace index), `/sequence` and `/activity` (Mermaid diagrams in `srs/{feature}-flows.md`).

**Installed 2026-11-22 at the user's request (moved off the deferred list):** `/prototype-html` — interactive
prototype after `/wireframe-html`; `portal` mode covers all quoted MVP + P2 flows. Its comment layer sends data
to jsonbin.io: off by default, warn and get a yes before embedding.

**Tier 2 (not installed yet, port on request per [skill-authoring.md](skill-authoring.md)):** `/erd`, `/state`, `/wireframe-ascii`, `/cr`, `/gap`, `/ask`, `/preview`, `/export`,
`/userguide` (the user guide is a Phase 1 deliverable, quote P1 #4), `/test-checklist` + `/test-cases`, `/kg`,
`/update-overview`, `/dashboard`. Decided 2026-11-21: `/usecase-diagram` and `/activity-swimlane` will be
installed but must **warn and get a yes before every render**, because they send diagram text to the public
plantuml.com server. **Deferred (don't fit the MVP now):** `/api-*`, `/discover`, `/roadmap`, `/doc-drift`,
`/prototype-next`, `/dbdiagram`.

Don't run a step whose skill isn't installed; say which one is missing.
