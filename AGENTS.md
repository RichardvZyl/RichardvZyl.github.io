# AGENTS.md

> Agent entry for RichardvZyl.github.io. Keep project rules above; Perseus memory rules below.

## Memory and workspace context (Perseus)

### Shared Vault (all repos on this machine)
- Store: `../.perseus-vault` (the shared vault sits beside the repos) via **`perseus-vault`** MCP (`perseus_vault_*` tools).
- **Read when:** session start (`perseus_vault_context`); before re-deciding something that may already be settled; looking up cross-repo conventions/facts.
- **Write when:** durable facts, decisions, conventions (`perseus_vault_remember`); journal meaningful events. Prefer consolidate related memories over duplicates.
- **Never write:** secrets, credentials, API keys, or session/chat transcripts (use https://perseus.observer/ledger/ for session history if needed).

### Project Context Engine (this repo only)
- Files: `.perseus/context.md` (and `pack.yaml`) via **`perseus`** MCP; edit context then `perseus render` when the briefing changes.
- **Read when:** entering this repo; before planning or implementing work here.
- **Write when:** project-specific status, constraints, architecture notes, and handoff briefing — keep them here, not in the shared Vault, unless they are true cross-repo conventions.
- Do **not** reuse another project's `.perseus` briefing.


## Secrets in a public repo

This repository is public and every tracked file is readable; the site repo
also *serves* them. Never put a literal secret in a tracked file. That includes
patterns, tests, fixtures and example data - not just config. A value written
down in order to detect it is still a value written down, and a detector that
carries what it detects leaks more than it prevents.

The content guard is built this way: editorial patterns live in
`scripts/content-guard.py` where they can be reviewed, and anything naming a
person, an identifier, a figure or a client lives in
`.content-guard-patterns.json`, which is git-ignored and injected in CI from
the `CONTENT_GUARD_PATTERNS` repository secret. The guard fails the build if
that set is missing, and reports private matches as path and line only - never
the matched text, because Actions logs on a public repo are public.

Full procedure: `docs/security/secret-hygiene.md` in the curriculum-vitae repo.

## Temporary files

Scratch files an agent creates while working go in `.temp/` at the repository root, never loose in
the root, and are deleted when the task is done. Anything that regenerates a tracked artefact is
not scratch: keep it, in its proper place (`scripts/`). `.temp/` is git-ignored.
