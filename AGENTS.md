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

