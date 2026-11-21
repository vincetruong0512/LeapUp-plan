# Rule: adding or adapting a skill

Applies whenever a skill is created, copied from another repo (e.g. `project-ai-ba`), or changed under
`.claude/skills/`. A skill must earn its place by serving the Leap Up project, not by being generally useful.

## Before writing

1. **Name the project need.** Write one sentence: which Leap Up goal or MVP module it serves (see the
   scope table in `CLAUDE.md`) and what work it saves. If it serves only `P2`/`OUT` items, defer it and say so.
2. **Reuse before building.** Check `.claude/skills/`, `~/.claude/skills/` and sibling repos for an existing
   skill. Prefer adapting one (as `doc-to-md` was adapted from `project-ai-ba`) to writing a new one.
3. **Strip foreign assumptions.** Ported skills often reference files that don't exist here (other repos'
   `rules/`, templates, folder names). Remove or replace every such reference; the skill must work
   self-contained in this repo.

## The skill must

4. **Read project context first:** `CLAUDE.md` and the relevant `docs/_sources/` conversions, not raw PDFs.
5. **Apply [mvp-focus.md](mvp-focus.md):** its output tags items `MVP` / `P2` / `OUT` / `OPEN` and puts
   MVP content first. Post-MVP content goes in a short closing section.
6. **Use project paths:** inputs from `docs/_sources/` or `references/`, outputs under `docs/` (tracked) or
   `docs/_sources/` (private, gitignored). No new top-level folders without asking.
7. **Keep privacy:** never write pricing, phone numbers, e-mails or local paths into tracked files.
8. **Ask before writing** files, showing the plan first. Make no outward-facing actions (publish, push, send)
   without explicit approval.
9. **Verify, don't assert:** if it produces derived content, it includes a check (counts, coverage,
   cross-reference to source lines) and reports failures as failures.

## Done means

10. **Tested on real Leap Up material**, at least one source in `references/`, not only synthetic samples.
11. **Frontmatter `description`** mentions Leap Up / the MVP use, so the skill triggers in the right context.
12. **Registered in `CLAUDE.md`:** add a line under "Project skills" with what it's for and its MVP tag.
