# WARNING — read before you commit or push

Both repositories in this pair are **public**. `RichardvZyl.github.io` additionally
serves every tracked file over HTTP because of `.nojekyll`, so in that repo
*tracked* means *published at a URL*, not merely *readable by someone who clones*.

Everything below is a mistake that has already been made here, or a trap that was
caught on the way to being made. None of it is hypothetical.

This file is mirrored byte-for-byte in both repositories. The two copies of
`scripts/content-guard.py` silently drifted once; keep these identical.

---

## 1. Never put a literal secret in a tracked file

Not in config, not in a pattern, not in a test fixture, not in example data, not in
a comment explaining what to avoid.

**This catches people in detectors.** A guard that greps for an account number has
to contain the account number. Writing a value down in order to catch it publishes
it exactly as surely as pasting it into the README — and the better the detector
gets, the more it carries.

So: `scripts/content-guard.py` holds editorial patterns only. Anything naming a
person, an identifier, a figure or a client lives in `.content-guard-patterns.json`,
which is git-ignored and injected in CI from the `CONTENT_GUARD_PATTERNS` secret.

Two properties are load-bearing. Do not "simplify" them away:

- **Fail closed.** A missing private set exits 1. Scanning with fewer patterns and
  printing `clean` reports a success it has not earned.
- **Redacted findings.** Private hits print path, line and label — never the matched
  text. Actions logs on a public repo are public, so echoing the line publishes the
  value the guard just caught.

## 2. The private pattern set exists in five places and drifts silently

Both repo roots, the offline backup, and the `CONTENT_GUARD_PATTERNS` secret on each
repository. **Change one, change all five.** GitHub secrets are write-only, so the
two secrets can never serve as your backup.

## 3. Local ignore rules do not travel

`.git/info/exclude` is per-clone and is never cloned. A `.gitignore` rule that only
exists on an unmerged branch does not protect the default branch. Before placing an
ignored file into a fresh clone, confirm the tracked rule is on the branch in hand —
otherwise the next `git add -A` commits it.

Currently relying on a local exclude: `docs/archive/`.

## 4. `downloads/` must not move

Its raw URLs are linked from the live site, from the README, and possibly from
applications already sent. `.gitignore` ignores `*.pdf` globally and un-ignores those
two files **by exact path** — relocate the folder and they silently drop out of the
index while the links 404.

## 5. Deleting from the tip is not removal

A value committed once stays reachable by SHA. If one lands:

- Find **every affected path** by walking `git rev-list --all --objects`, not the one
  you happened to notice.
- Check **every ref**. A value on a feature branch is one click from a value on the
  default branch, so a default-branch-only rewrite accomplishes nothing.
- `git filter-repo --replace-text` **does not touch commit messages.** Pass
  `--replace-message` as well.
- filter-repo's `regex:` rules are **case-sensitive**; the guard matches
  case-insensitively. Prefix rules with `(?i)` or case variants survive and your
  verification lies to you.
- Rehearse on a `git clone --mirror`, verify zero matches across all refs, and only
  then push.
- Verification must parse a single `git cat-file --batch-all-objects` stream. One
  subprocess per blob is too slow and will time out.

## 6. `refs/pull/*` survives a history rewrite

GitHub creates a ref per pull request pointing at the original commits. **No git
client can rewrite or delete them.** A normal clone does not fetch them; a
`--mirror` clone does. After a rewrite the branches can be clean while a mirror
still finds everything.

Only two things remove them: a GitHub Support purge, or deleting and recreating the
repository. Check the fork count first — with forks, deleting the parent promotes a
fork to root of the network and the objects survive anyway.

## 7. A rewrite stops exposure; it does not retract disclosure

Forks, caches and archive services may hold what was public. Anything exposed is
rotated **at the source** — bank, tax authority, mobile operator, credential issuer —
independently of anything done to git. That is the step that limits harm, and it is
the one the git work makes people feel they can skip.

## 8. Exports and archives reintroduce what they were meant to outlive

A PR export built to preserve history contained a compensation figure, a third
party's identity, and phrasing the guard exists to block. **Run the guard against
any generated document before committing it.**

Note the inverse trap: a document *about* withdrawn claims necessarily quotes them,
so editorial patterns fire on it forever. That is a reason to keep such a document
untracked, not a reason to weaken the guard.

## 9. Line endings and the Linux mount

- `core.autocrlf=true` against a Windows tree produced whole-file rewrites of every
  tracked file — symmetric insertions and deletions, zero content change. Fixed by
  `.gitattributes` (`* text=auto eol=lf`, binaries marked) and `core.filemode=false`.
  If diffs ever look like that again, this is why.
- Worktree `gitdir` files hold **Windows** paths, so worktree administration fails
  from the Linux VM. Do it natively.
- `sed -i` anchored with `$` does not match a CRLF working tree. Use `(\r?)$`.
- Git cannot always remove its own `.git/index.lock` from the mount. A stale
  zero-byte lock blocks the next command.

## 10. Other agents may be working in these repos

Before any force-push, check for in-flight work. **Normalise timestamps to one
timezone before concluding a session is active** — comparing `+02:00` against
`+00:00` made a five-hour-old session look current.

## 11. Overstated claims are the expensive kind

An inflated years figure that a reader can check against the role history costs more
than the claim gains: the hole found in one row discredits the rows that were true.
Correcting downward protects the strong claims. That is what the guard's editorial
patterns are for.

---

# Pre-push checklist

The `.githooks/pre-push` hook runs the mechanical checks automatically. These are
the ones only a human can answer.

- [ ] `.content-guard-patterns.json` is **not** staged, tracked, or newly added
- [ ] No new literal identifier, figure, client name or third-party name in any
      tracked file — including patterns, fixtures and comments
- [ ] If the private set changed: **all five copies** updated, backup included
- [ ] If a generated or exported document is being added: guard run against it first
- [ ] If `downloads/` or its `.gitignore` exception was touched: raw URLs still resolve
- [ ] If anything in `docs/` changed that feeds a PDF: artefacts rebuilt, or
      deliberately deferred and said so
- [ ] Claims changed in `CV.md` / `PROFILE.md` / `SKILLSMATRIX.md` are ones you can
      defend against the role dates in a screening call
- [ ] No other agent session has in-flight work on these branches
- [ ] Pushing to `master`: this publishes. For the site repo it goes live immediately

To install the hook:

```
git config core.hooksPath .githooks
```
