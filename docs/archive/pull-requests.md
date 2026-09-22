# Pull request and issue archive - RichardvZyl.github.io

Exported from GitHub before the repository was deleted and recreated to remove
stale `refs/pull/*` objects left behind by a history rewrite. GitHub owns those
refs and no git client can remove them, so the repository itself had to go.

Commit history survived the rewrite and is unaffected. What is preserved below is
the per-change rationale that lived in PR descriptions and review threads, since
that is not recoverable from commits alone.

**25 pull requests, 0 issues.** PR numbering restarts in the new repository,
so the numbers here do not map to anything live.


> **Redaction notice.** This archive was passed through the repository's own content
> guard before being committed. Passages matching its patterns - personal identifiers,
> figures, third-party identity, and claims previously withdrawn as inaccurate - are
> replaced with `[REDACTED]`. The surrounding rationale is preserved. If a redaction
> removes the point of a sentence, that sentence was describing something the guard
> exists to keep out of this repository.


---

## PR #1 - Align site with CV PR #3: correct multi-tenancy, restore deployment substance

`CLOSED` - opened 2026-09-02 - `cursor/cv-site-accuracy-patches-d947` into `master`

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Why

The live site still sold a **false** multi-tenancy claim (“a database per legal entity, a schema per brand … behind load-balanced instances”). CV [PR #3](https://github.com/RichardvZyl/curriculum-vitae/pull/3) (`cursor/cv-site-accuracy-patches-9957`) is the source of truth. This PR brings `RichardvZyl.github.io` into lockstep with that draft and does **not** touch `curriculum-vitae`.

## What changed

- **Replaced only the false multi-tenancy answer** with the shipped constraint: production was one SQL Server, schema-per-brand, because separate databases were priced out; 2 tenants / 25 brands / 150+ payment methods. Sit now says operators/brands, not legal entities.
- **Restored true deployment substance** as its own Problems card: four health-checked Docker instances behind a round-robin load balancer, spike warming, payment-method shedding. Did **not** drop the other Problems cards (7 original kept; 14 total).
- **Added** MeterMo as field metering / usage integrity (electricity, water, gas). No wallbox, charging, or target-sector adjacency.
- **Added** CombinatorialOptimiser as a dependency-free .NET optimiser library (20+ solvers, registry by instance size). No “intelligent charging” contrast.
- **Languages / Azure:** Node.js + SSR where that was the production problem; Azure production depth framed as request path, event-driven work, reliable delivery, and settlement. No AWS comparison. No industry-fit pitch.
- **Yuno Technologies:** [REDACTED] / solutions architect, Apr 2026–present (Now section). Existing technical claims kept and aligned with the CV (microVM isolation marked as under evaluation, not production).
- **Raging River:** Dec 2022 – Mar 2026; ended via voluntary severance during a post-acquisition restructure. The site no longer implies current employment there.

## Verification

- HTML parses. Forbidden phrases (database-per-legal-entity as shipped, wallbox/charging, AWS, Event Sourcing) are absent.
- Local browser pass at `http://127.0.0.1:8765/`: 14 Problems cards, nav (including Now), intro employment dates, Yuno/Orchestration, contact links.

## Out of scope (correctly not restored)

Hash-partitioned work queues and Event Sourcing remain out — they were already removed as unowned / inaccurate on the CV.

**This PR is a draft.** Do not mark ready for review until copy is checked against CV PR #3.
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-d1a7cd4d-e19e-4fb2-a5b1-81f3efa8d947?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-d1a7cd4d-e19e-4fb2-a5b1-81f3efa8d947&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>

> **Comment** - RichardvZyl, 2026-09-05
>
> Closing unmerged in favour of a replacement PR.
> 
> The useful commits here are **not lost** — both were merged into the replacement branch:
> - `Now` nav link and section aria-label matching the visible heading
> - "two operators and twenty-five brands" in the multi-tenancy card
> 
> The reason for replacing rather than updating is this PR's stated purpose: *"restore **true** deployment substance"* — four health-checked Docker instances behind a round-robin load balancer, spike warming, payment-method shedding.
> 
> That description may well be accurate about the platform. It is not attributable to Richard: he was in the design discussions, but building and maintaining the deployment topology was not his area, and he asked for those claims removed. **Truth about the system is not the test — ownership is.** Merging under a title that says "restore deployment substance" would leave a record saying the opposite of what was decided.
> 
> Same principle already applied to the hash-partitioned work queues, which this PR correctly left out.
> 
> 🤖 Generated with [Claude Code](https://claude.com/claude-code)

---

## PR #2 - Add GitHub Actions CI for the static site

`CLOSED` - opened 2026-09-08 - `cursor/add-github-actions-ci-5be8` into `master`

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
Adds a minimal GitHub Actions workflow so pushes and pull requests to `master` get a basic sanity check on this GitHub Pages site.

## What it does

New file: `.github/workflows/ci.yml`

- Runs on **push** and **pull_request** targeting `master`
- Checks out the repo
- Confirms `index.html` exists, is non-empty, has a `<!DOCTYPE html>` declaration, and includes opening/closing `html`, `head`, and `body` tags (stdlib `html.parser`, no extra packages)

No site content, layout, or Pages config changes.

## Verification

Ran the same check locally against the current `index.html` (pass). Confirmed empty and missing files fail the same script.
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-936054b9-7975-45c4-817f-03670f3e5be8?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-936054b9-7975-45c4-817f-03670f3e5be8&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>

> **Comment** - RichardvZyl, 2026-09-09
>
> Superseded by #3, which **includes this workflow unchanged** and adds a content guard beside it.
> 
> The structure check is carried over verbatim. It is kept as a floor, not removed — but the risk on this site is what the words say, not whether the tags balance. This file was adapted from a friend's site and carried his identity and two credentials Richard does not hold; an agent has twice restored a claim Richard disowned.
> 
> 🤖 Generated with [Claude Code](https://claude.com/claude-code)

---

## PR #3 - ci: add a content guard alongside the structure check

`MERGED` - merged 2026-09-09 - `ci/content-guard` into `master`

Builds on #2 rather than replacing it — that workflow is included unchanged, with a second job added.

## Why

#2 confirms `index.html` exists, is non-empty, and has `html`/`head`/`body` tags. Those can only fail if the file is deleted or truncated.

The real risk on this site is **content**. This file was adapted from a friend's personal site and carried his name, his domain, his city, and **two security credentials Richard does not hold**. An agent has twice restored a deployment-topology claim Richard had explicitly disowned — the second time by *refining* it rather than removing it.

## What this adds

`scripts/content-guard.py` — the same guard proposed for `curriculum-vitae`. 23 patterns, each mapped to a real incident, each recording why it exists: the template author's identity, unheld credentials, disowned claims, PII, compensation, client/product names, and unresolved conflict markers.

## Verification

Clean today. 12 injected violations, all caught — after fixing a compensation regex that initially missed `R[REDACTED]`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

---

## PR #4 - Publish the CV for download; add a .gitignore this repo never had

`CLOSED` - opened 2026-09-09 - `site/downloadable-cv` into `ci/content-guard`

Stacked on #3.

## Downloadable CV

`Richard-van-Zyl-CV.pdf` and `.docx`, served by Pages, linked from two places a reader would look: beside the availability pill in the hero for someone skimming, and among the contact links for someone who has decided to act. PDF primary, Word alongside because recruiters reformat.

Published from **this** repo rather than `curriculum-vitae`, which ignores PDFs by design — it holds payslips and reference letters, and publishing from there would have meant weakening that guard.

## A .gitignore

This repo had none, and **every tracked file here is served publicly**. Payslips, reference letters and the severance application are now blocked by name, with the two published CV files explicitly allowed.

Verified: the CV files are committable; a file named `Payslip_*.pdf` is refused.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

---

## PR #5 - Publish CV and skills overview PDF downloads on Pages

`MERGED` - merged 2026-09-14 - `cursor/publish-cv-pdf-downloads-9957` into `master`

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

Companion to [curriculum-vitae PR #9](https://github.com/RichardvZyl/curriculum-vitae/pull/9).

- Host `Richard-van-Zyl-CV.pdf` and `Richard-van-Zyl-Skills-Overview.pdf` at the site root (GitHub Pages).
- Hero + contact download rows: both PDFs only — no Word/DOCX.
- Relative hrefs so they resolve on https://richardvzyl.github.io/.
- PDFs refreshed after CV-pack spelling/grammar fixes (QnA Maker, monetisation, Skills Overview phrasing).

## Verification

- `python3 scripts/content-guard.py` — clean
- No `.docx` linked in `index.html`
- After merge + Pages publish: `/Richard-van-Zyl-CV.pdf` and `/Richard-van-Zyl-Skills-Overview.pdf` should return 200

Kept as draft.
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-badc6a68-1f6f-46e7-9a1e-a1aac2171f0c?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-badc6a68-1f6f-46e7-9a1e-a1aac2171f0c&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>

---

## PR #6 - Update Open to copy for hands-on senior roles

`MERGED` - merged 2026-09-14 - `cursor/update-open-to-copy-12e5` into `master`

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary
Updates the site’s availability messaging so “Open to” clearly signals Solutions Architect, Technical Lead, and senior hands-on backend roles — still building, mentoring, and influencing architecture/tech/design.

## Changes
- Hero pill copy updated to the new Open to wording
- Contact availability row updated to match (location retained)
- Availability row styling adjusted so the longer line wraps cleanly

## Verification
[Hero Open to pill](https://cursor.com/agents/bc-01a0a195-6c06-7e21-babf-d2d7a4af12e5/artifacts?path=%2Fopt%2Fcursor%2Fartifacts%2Fhero_open_to_pill.webp)
[Contact Open to row](https://cursor.com/agents/bc-01a0a195-6c06-7e21-babf-d2d7a4af12e5/artifacts?path=%2Fopt%2Fcursor%2Fartifacts%2Fcontact_open_to_row.webp)

## Test plan
- [x] Hero Open to pill shows the new sentence
- [x] Contact availability row matches
- [x] Mobile width: longer copy wraps without clipping


<sub>To show artifacts inline, <a href="https://cursor.com/dashboard/cloud-agents#my-pull-requests">enable</a> in settings.</sub>
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-01a0a195-6c06-7e21-babf-d2d7a4af12e5?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-01a0a195-6c06-7e21-babf-d2d7a4af12e5&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>

---

## PR #7 - Sync site and CV PDF with reviewer wording updates

`MERGED` - merged 2026-09-15 - `cursor/cv-reviewer-wording-12e5` into `master`

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary
Syncs the personal site and downloadable CV PDF with the CV reviewer wording updates.

## Changes
- Intro: removed voluntary-severance sentence
- Multi-tenancy problem card: operator DB + schema-per-brand; 2 operators
- Yuno card: Current production / Phase 2 planned / Under evaluation
- Regenerated `Richard-van-Zyl-CV.pdf` from updated CV source

## Verification
[Intro without severance](https://cursor.com/agents/bc-01a0a195-6c06-7e21-babf-d2d7a4af12e5/artifacts?path=%2Fopt%2Fcursor%2Fartifacts%2Fsite_intro_no_severance.webp)
[Multi-tenancy operators copy](https://cursor.com/agents/bc-01a0a195-6c06-7e21-babf-d2d7a4af12e5/artifacts?path=%2Fopt%2Fcursor%2Fartifacts%2Fsite_multitenancy_operators.webp)
[Yuno phased architecture copy](https://cursor.com/agents/bc-01a0a195-6c06-7e21-babf-d2d7a4af12e5/artifacts?path=%2Fopt%2Fcursor%2Fartifacts%2Fsite_yuno_phased.webp)
[CV PDF page 1 summary](https://cursor.com/agents/bc-01a0a195-6c06-7e21-babf-d2d7a4af12e5/artifacts?path=%2Fopt%2Fcursor%2Fartifacts%2Fcv_pdf_page1_summary.png)

## Test plan
- [x] content-guard clean
- [x] Intro no longer mentions voluntary severance
- [x] Yuno section labels production vs planned vs evaluation
- [x] PDF regenerated and spot-checked


<sub>To show artifacts inline, <a href="https://cursor.com/dashboard/cloud-agents#my-pull-requests">enable</a> in settings.</sub>
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-01a0a195-6c06-7e21-babf-d2d7a4af12e5?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-01a0a195-6c06-7e21-babf-d2d7a4af12e5&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>

---

## PR #8 - Correct multi-tenancy topology and refresh CV PDF

`MERGED` - merged 2026-09-15 - `cursor/cv-topology-segregation-12e5` into `master`

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary
Follow-up to #7: correct the multi-tenancy topology overclaim and refresh the downloadable CV PDF to match the CV-source recommendation.

## Changes
- Multi-tenancy problem card: restore **one SQL Server, schema-per-brand** (keep “2 operators” terminology)
- Regenerated `Richard-van-Zyl-CV.pdf` with shared-SQL-Server topology and restored segregation insight (app boundary can satisfy an auditor; isolation belongs in the engine)

Companion CV source PR: https://github.com/RichardvZyl/curriculum-vitae/pull/10

## Test plan
- [x] content-guard clean
- [x] Site no longer claims each operator had its own database
- [x] PDF includes shared SQL Server + engine-level segregation note

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-01a0a195-6c06-7e21-babf-d2d7a4af12e5?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-01a0a195-6c06-7e21-babf-d2d7a4af12e5&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>

---

## PR #9 - Make download links easier to click on desktop

`MERGED` - merged 2026-09-15 - `cursor/download-link-hit-targets-96d1` into `master`

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

Desktop download targets were hard to hit: hero CV/skills links were 12px underlined text with no padding.

## Changes
- Hero downloads: padded button-sized hit targets (`min-height: 44px`) on their own row, clearer borders
- Contact download pills: larger padding / `min-height: 48px`, clearer borders
- WebGL `#bg` canvas and scroll cue: `pointer-events: none` so decorative layers cannot intercept clicks

## Test plan
- [x] Desktop: hero CV + Skills overview links are easy to click
- [x] Desktop: contact section download pills clickable / hover correctly
- [x] PDFs download successfully
- [ ] Mobile: links remain usable

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-01a0a545-7719-7dac-99fd-6ad7ceb796d1?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-01a0a545-7719-7dac-99fd-6ad7ceb796d1&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>

---

## PR #10 - Refresh Skills Overview PDF formatting

`MERGED` - merged 2026-09-15 - `cursor/skills-overview-pdf-format-5761` into `master`

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary
Replaces the site’s Skills Overview download with a regenerated PDF that keeps readable table structure.

## Changes
- `Richard-van-Zyl-Skills-Overview.pdf` — bordered tables, visible headers, right-aligned years column, denser layout (4 pages)

## Source
Regenerated from `curriculum-vitae` `SKILLS-OVERVIEW.md` (companion PR on `cursor/skills-matrix-format-fix-5761`).

## Test plan
- [x] content-guard clean
- [x] PDF page previews show intact Skill/Years tables without letter-spacing glitches
- [ ] After merge, download from https://richardvzyl.github.io/ and confirm layout

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-01a0a597-b338-745d-bed9-a79c722b5761?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-01a0a597-b338-745d-bed9-a79c722b5761&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>

---

## PR #11 - Improve secondary text contrast on the dark backdrop

`MERGED` - merged 2026-09-17 - `cursor/text-contrast-color-theory-ebe0` into `master`

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
Cool mid-greys (`--muted` / `--slate`) sat near the WebGL particle slate and washed out against additive brass/teal glow — domain, location, and other secondary copy were hard to read.

**Approach (color theory, not random picks):**
- Keep surfaces in the green-black void family and accents as warm brass + cool living teal.
- Move readable secondary text onto the warm **paper→void** axis instead of cool mid-grey.
- Keep tertiary chrome quieter but still warm and lifted.
- Lift section numerals (`--slate`).
- Hero meta sits on the particle field with no sheet: **values use `--paper`**, **labels use brass chroma** for hierarchy (hue, not lowered value).

**Tokens:** `--soft: #D4CFC2` (sheet body), `--muted: #C4BFB2` (chrome), `--slate: #8B9A94`.

**Mapped to soft:** leads, problem answers, principles, ventures, availability, statement quieter words.
**Hero meta:** paper values + brass-hi labels.
**Stays muted:** nav idle, scroll cue, footer, PDF hints.

Contrast vs `--void`: paper ~15:1, soft ~12:1, muted ~10:1, slate ~6:1.
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-01a0aaf1-24ef-7415-bd71-2e278fe7ebe0?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-01a0aaf1-24ef-7415-bd71-2e278fe7ebe0&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>

---

## PR #12 - Give the AI work its own section; drop the equity share

`MERGED` - merged 2026-09-17 - `site/ai-section` into `master`

Gives the AI work its own section, and drops the equity share from the Yuno line.

This commit has existed only on one disk since 9 September. It was written on
`site/downloadable-cv`, that branch was rebased locally, PR #4 was closed rather than merged,
and the commit was never pushed anywhere. Cherry-picked onto current master here (clean, no
conflicts) so it stops being one `git gc` away from gone.

## What it does

AI was a single capability row — "agent orchestration with budget governance, multi-model
routing, MCP integration, analyzer-enforced quality gates" — for a body of work the CV gives a
full section to. It now has eight cards: the comparison harness, DAG orchestration with model
routing, budget governance, the analyzer-enforced gate, two-axis review, ADR capture while
planning, the content guard, and the standing evaluation of agent infrastructure.

It also removes "50%" from the Yuno role line. The share is accurate, but a reader needs to know
he is a [REDACTED] who leads technical delivery, not the size of the stake — that invites questions
about the business rather than the work.

## Checked

- Section numbering runs 01–08 unbroken: AI lands at 06, Now moves to 07, Contact to 08.
- Every nav anchor resolves to a real section id, `#ai` included.
- The download buttons added in #5 survived the cherry-pick untouched.

---

## PR #13 - One canonical copy of the PDFs, plus the hygiene this repo never had

`MERGED` - merged 2026-09-17 - `site/hygiene` into `master`

Stacked on #12 — review that one first; this targets its branch, not master.

Four hygiene items, none of them cosmetic.

## One canonical copy of each PDF

Both PDFs are removed from this repo. The buttons now link to `downloads/` in
[`curriculum-vitae`](https://github.com/RichardvZyl/curriculum-vitae), which is where the
`CV.md` and `SKILLS-OVERVIEW.md` that generate them live.

Keeping a second copy here is what caused the drift this fixes: the release tag and this repo
disagreed about which build was current, and the README's download link served the formatting
that two later PRs were opened to correct. One file, in the repo that owns its source, cannot
fall behind itself.

Measured before committing to it: `raw.githubusercontent.com` returns `application/octet-stream`
with `X-Content-Type-Options: nosniff`, so the buttons still download directly even though the
link is now cross-origin and the `download` attribute no longer applies.

**Breaking:** `https://richardvzyl.github.io/Richard-van-Zyl-CV.pdf` will 404 after this merges.
Nothing in either repo points there any more, but anything external that does will break.

## A `.gitignore`, which this repo has never had

Every tracked file here is served publicly by Pages. Until now nothing stopped a private
document, a payslip or a reference letter from being committed into a public web root by
accident. Added, with the career artefacts excluded by extension so a stray copy cannot
reappear.

## The content guard can read PDFs

`.pdf` was in `SKIP_SUFFIXES`, so the one file a reader actually downloads was the one file
nothing checked. It now extracts text with `pdftotext` and scans it against the same forbidden
list as everything else, and fails loudly if the extractor is missing. CI installs
`poppler-utils`. No PDFs are tracked here after this PR, so it costs nothing today and catches
the case where one lands tomorrow.

## `actions/checkout@v4` → `v5`

The curriculum-vitae repo moved to v5 already; this one was still on v4 and the Node 20
deprecation applies.

## Checked

- `scripts/content-guard.py` runs clean locally.
- No `href="Richard-van-Zyl-*.pdf"` references remain in `index.html`.
- CI's structure check does not require the PDFs to be present, so removing them does not
  break it.

---

## PR #14 - Sync CV PDF with tightened layout

`CLOSED` - opened 2026-09-17 - `cursor/cv-layout-spacing-8358` into `master`

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary
Updates the site-root `Richard-van-Zyl-CV.pdf` to match the curriculum-vitae WeasyPrint regeneration (tighter post-subheading spacing, left-aligned lists, page-break heading margins).

**Skills Overview PDF left unchanged.**

## Companion
Source pipeline: `curriculum-vitae` branch `cursor/cv-layout-spacing-8358`

## Test plan
- [x] Site content-guard clean
- [x] Skills Overview PDF unchanged
- [x] CV download opens and matches the curriculum-vitae artifact
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-01a0aed6-951b-7888-b317-29714ed58358?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-01a0aed6-951b-7888-b317-29714ed58358&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>

> **Comment** - cursor, 2026-09-17
>
> Closing as absorbed into #15 (`cursor/skills-overview-equal-margins-5761`), which already includes this CV PDF sync plus the Skills Overview update.
> 
> Prefer landing #12 → #13 next: #13 removes local PDF copies and points at curriculum-vitae `downloads/`, which is the cleaner end state once curriculum-vitae #16 is on master.

---

## PR #15 - Sync Skills Overview PDF with equal margins

`CLOSED` - opened 2026-09-17 - `cursor/skills-overview-equal-margins-5761` into `master`

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary
Site copies of both PDFs after merging the CV layout-spacing session into the equal-margins Skills Overview branch.

- `Richard-van-Zyl-CV.pdf` — WeasyPrint with tightened heading/list layout (`pdf/cv-print.css` upstream)
- `Richard-van-Zyl-Skills-Overview.pdf` — equal 14mm margins
- Content-guard ENTP false-positive fix

## Source
https://github.com/RichardvZyl/curriculum-vitae/pull/16

## Test plan
- [x] PDFs synced from curriculum-vitae regenerate
- [ ] Visual sign-off

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-01a0a597-b338-745d-bed9-a79c722b5761?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-01a0a597-b338-745d-bed9-a79c722b5761&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>

> **Comment** - cursor, 2026-09-17
>
> Closing without merging — superseded by the better end state in #13 (remove local PDFs; link to curriculum-vitae `downloads/`). This PR only refreshed the local copies; #13 deletes the drift source entirely. Wait for curriculum-vitae #16 on master first so those raw links serve the current builds.

---

## PR #16 - Note DOCX unpublished; PDFs owned by curriculum-vitae

`MERGED` - merged 2026-09-17 - `cursor/download-canonical-notes-5761` into `master`

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary
Notes in README that Word/DOCX is unpublished and that PDF buttons already point at `curriculum-vitae` `downloads/`.

## Companion
https://github.com/RichardvZyl/curriculum-vitae/pull/… (download-canonical-notes)

## Test plan
- [x] README states DOCX not linked

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-01a0a597-b338-745d-bed9-a79c722b5761?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-01a0a597-b338-745d-bed9-a79c722b5761&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>

---

## PR #17 - Recognition in credentials; the tool layer gets its own card

`MERGED` - merged 2026-09-17 - `feat/recognition-and-ai-tooling` into `master`

Site-side companion to `RichardvZyl/curriculum-vitae#18` — keeps the two in step per this repo's README.

Three changes, all in `index.html`:

1. **A `Recognition` row in `#credentials`.** Uses the existing `credrow` / `ck` / `cv` / `sub`
   pattern, so no new section and no CSS. Leads on Banking Developer of the Year (first place,
   twice) with the rest in the `sub` span.
2. **A·01 retitled and extended.** "Five assistants, not one bet" → "Five assistants, plus one
   that runs offline". Adds the CLI-and-GUI split as a workflow choice and locally hosted
   open-weight inference as the outage/no-network path.
3. **New A·09 — "Tools, not just conversation".** The MCP-and-plugins layer with the ~30
   purpose-built skills. This is the card that separates "I use assistants" from "I built the tool
   surface they act through", and nothing on the page said it.

Deliberately unchanged: A·08 names no routing products, so the Omniroute correction that `CV.md`
needed does not apply here.

Prize details and the bonuses attached to the awards are omitted on purpose — see the
`curriculum-vitae` PR for the reasoning.

## Notes

- Branched from `origin/master` in a separate worktree; the `site/hygiene` checkout was untouched.
  That branch is stale — its content is on master as squash-merged #13 / #16.
- `python scripts/content-guard.py` — clean.
- Not visually verified in a browser. Worth a look at `#credentials` and the A·09 card at phone
  width before merge, since the recognition row's `sub` span is longer than its neighbours.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_015N5DijjLi7Vhsx14bHN9eQ

---

## PR #18 - Drop AKS; keep Docker; list the third public repo

`MERGED` - merged 2026-09-18 - `cursor/drop-aks-keep-docker-8fc3` into `master`

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
Yuno is a **stakeholder side project**, partner-operated — not [REDACTED] / [REDACTED]. Orchestration platform stays, labelled side project. Intro says available for hire.

The recruitment venture was removed in site commit `e0e30c2` (never launched). The 50% figure came out in [PR #12](https://github.com/RichardvZyl/RichardvZyl.github.io/pull/12); “I hold [REDACTED]” lingered and is gone here.

Companion CV PR (PDFs regenerated, both ventures, page-break keep): https://github.com/RichardvZyl/curriculum-vitae/pull/21

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-35bf1f7c-b117-4522-9a02-a410c31a8fc3?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-35bf1f7c-b117-4522-9a02-a410c31a8fc3&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>

---

## PR #19 - Chooser: condensed Skills Overview vs full Skills Matrix

`MERGED` - merged 2026-09-18 - `cursor/skills-download-chooser-0ef5` into `master`

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

Hero and contact downloads now let a reader choose between the two published skills PDFs from [curriculum-vitae#22](https://github.com/RichardvZyl/curriculum-vitae/pull/22):

- **Skills overview** (condensed PDF)
- **Skills matrix** (full PDF)

CV remains a single download (no condensed/full CV pair). Still raw GitHub `master` `downloads/` URLs — no PDF copies in this repo.

## Companion

Depends on curriculum-vitae#22 for `Richard-van-Zyl-Skills-Matrix.pdf` on `master`.

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-6770c238-066c-535d-b27f-230e12cd0ef5?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-6770c238-066c-535d-b27f-230e12cd0ef5&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>

---

## PR #20 - Restore the A01 argument; reword local inference; stop A09 repeating its neighbours

`MERGED` - merged 2026-09-18 - `feat/sixth-link-and-copy-fixes` into `master`

Site-side companion to `RichardvZyl/curriculum-vitae#22`.

**A·01 headline restored to an argument.** "Five assistants, plus one that runs offline" counted
things; "Five assistants, no single bet" says why the five exist. The offline point stays in the
body, where it belongs — and a locally run model is not an "assistant" in the same sense as Cursor
anyway, so the old headline was also loose.

**Local inference reworded** to match `CV.md`: needs no provider, no subscription and no network,
rather than surviving an outage.

**A·09 no longer repeats its neighbours.** It was listing "orchestration", "the enforcement gate"
and "two-axis review" — which are A·02, A·04 and A·05, sitting directly above it. Read top to
bottom, the last card restated a third of the section. Now lists only what has no card of its own:
domain modelling, .NET design-guideline review, per-engine concurrency probes, merge-conflict
resolution, session continuity and repository auditing.

Its closing line also loosened from "Untooled, a model produces an opinion; tooled, it produces a
change you can review" to "A model without tools gives you an opinion; with tools it gives you a
change you can review."

Sixth is named and linked in `CV.md` only. The site's AI section demotes tool names by design, so
adding an outbound product link there is a separate decision — say the word if you want it.

`python scripts/content-guard.py` — clean.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_015N5DijjLi7Vhsx14bHN9eQ

---

## PR #21 - Link Sixth in A01

`MERGED` - merged 2026-09-18 - `content/link-sixth` into `feat/sixth-link-and-copy-fixes`

Stacked on #20 — branched from and targeting `feat/sixth-link-and-copy-fixes`, because both
changes land on the same single line of A·01 and two PRs against `master` would collide.

Adds the Sixth link to the site, matching `curriculum-vitae#23`:

> A sixth, [Sixth](https://trysixth.com), ran alongside them as a fallback while the routing layer
> was being settled.

Worth knowing what this trades: the AI section's copy deliberately leads on capability and keeps
product names out — it is the only outbound product link in the section, and A·08 talks about
routing layers and memory systems without naming any of them. The argument for making Sixth the
exception is that it is the one a reader can go and look at, and an unnamed "sixth subscription"
tells them nothing. The argument against is that A·01 is about not betting on one vendor, and a
link is a soft bet.

Close this and the link lives in `CV.md` only, which is also a defensible place to leave it.

`python scripts/content-guard.py` — clean.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_015N5DijjLi7Vhsx14bHN9eQ

---

## PR #22 - Expand the AI capability row and link it to Building with AI

`MERGED` - merged 2026-09-19 - `ai-capabilities-row` into `master`

The Capabilities **AI** row still had the one-line summary from the initial site, so on mobile it read as if the AI work had been trimmed. The detail lives in **Building with AI**, several screens further down.

- Row now lists all nine areas that section covers
- Ends with a brass `See Building with AI →` link to `#ai` (new `.cmore` style using existing tokens)

Checks: structure check and content guard pass; rendered at 390px width.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_0176HJ7wVHMLKAy5ckM5Bc2X

---

## PR #23 - Add a Temporary files section to AGENTS.md; ignore .temp/

`OPEN` - opened 2026-09-21 - `chore/agents-and-temp-folder` into `master`

This extends the existing AGENTS.md (tracked in #24); it does not create one. The earlier version of this PR added a competing AGENTS.md; that file has been discarded in favour of the one already on master.

Two changes only:
- Append a **Temporary files** section to AGENTS.md: scratch goes in an ignored .temp/ at the repo root and is removed when the task ends; anything that regenerates a tracked artefact is kept in its proper place.
- Add .temp/ to .gitignore.

Branch rebased onto master and reduced to a single commit.

---

## PR #24 - Normalise line endings; track agent conventions

`MERGED` - merged 2026-09-21 - `chore/normalise-line-endings` into `master`

Adds .gitattributes (line endings/file modes) and tracks AGENTS.md, CLAUDE.md and .perseus/.

Rebased onto current master. The older 'One canonical copy of the PDFs' commit was dropped: master already removed the local PDFs, added .gitignore, the PDF-reading content guard and the hosted-download links (with the condensed/full split), so it would only have reintroduced conflicts and the older single-overview wording.

---

## PR #25 - Stop the content guard from carrying what it guards against

`MERGED` - merged 2026-09-22 - `sec/content-guard-patterns` into `master`

Splits the content guard so it no longer carries the values it checks for.

## Why

Both repos are public; the site repo additionally serves every tracked file. The guard listed its patterns as literals, so it published more than it prevented. The pattern set also grows every time the guard improves, so the design leaked by construction.

## What changed

- Ten editorial patterns stay in `scripts/content-guard.py` where they can be reviewed.
- Sixteen that name a person, an identifier, a figure or a client move to `.content-guard-patterns.json` - git-ignored, written in CI from the `CONTENT_GUARD_PATTERNS` secret, removed again in an `if: always()` step.
- **Fail closed:** a missing private set exits 1. Scanning with fewer patterns and printing `clean` reports success it has not earned. `CONTENT_GUARD_ALLOW_PARTIAL=1` overrides knowingly.
- **Redacted findings:** private hits report path, line and label, never the matched text. Actions logs on a public repo are public, so echoing the line would publish the value just caught.
- The rule is written into `AGENTS.md` in both repos, with the procedure in `docs/security/secret-hygiene.md`.
- Per-session worktrees ignored under `.worktrees/`.

## Verified

Guard clean on both repos. Fail-closed, allow-partial and redaction paths each tested. The two copies of the script had drifted in formatting and are byte-identical again.

## Not covered here

This does not remove the values from history - they remain reachable by SHA on every ref and must be treated as disclosed regardless.

---

