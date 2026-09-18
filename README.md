# richardvzyl.github.io

Personal site for **Richard van Zyl** — Solutions Architect / Technical Lead, backend and
data-intensive financial systems.

Served by GitHub Pages from the default branch at <https://richardvzyl.github.io/>.

## Structure

Single self-contained page. `index.html` holds the markup, styles and the WebGL background
inline — no build step, no bundler, nothing to install.

The CV and skills PDFs are **not** kept here. They live in
[`curriculum-vitae`](https://github.com/RichardvZyl/curriculum-vitae) under `downloads/`, and the
hero and contact buttons link straight there:

| Download | Artefact |
|---|---|
| CV | Single narrative PDF |
| Skills overview | **Condensed** skills PDF |
| Skills matrix | **Full** skills PDF |

GitHub serves those raw URLs as `application/octet-stream`, so the buttons still download rather
than opening in the browser. One copy, in the repo that owns the source — a second copy here would
silently fall behind the next regeneration. Word/DOCX may exist for local editing in the CV repo
but is gitignored and **not** linked from this site.

| Dependency | Source | Purpose |
|---|---|---|
| Bricolage Grotesque, Geist, Geist Mono | Google Fonts | Typography |
| three.js r128 | cdnjs | Animated background canvas (`#bg`) |

Both degrade gracefully: the page is fully readable with the canvas blank and system fonts
substituted.

## Editing

Edit `index.html` directly and push. Content is kept in step with
[`curriculum-vitae`](https://github.com/RichardvZyl/curriculum-vitae) — when a date, title or
years figure changes there, change it here too.

## Credit

Visual design adapted with permission from a template shared by a friend. All content, copy and
structured data are original.

## Licence

© 2026 Richard van Zyl. All rights reserved.
