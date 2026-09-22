#!/usr/bin/env python3
"""Content guard for Richard's public career repos.

Every pattern corresponds to something that actually went wrong in these
repositories, not a generic template. Structure checks are a floor; the real
risk in a public repo written by multiple agents is what the words say.

The pattern set is split deliberately.

  * The patterns below are editorial: withdrawn claims, unfalsifiable phrasing,
    credentials not held, conflict markers. They are safe to read.

  * Everything that identifies a person, a real account or reference number, a
    figure, or a client is loaded at runtime from a private file. This repo is
    public and every tracked file is served, so a guard that carried those
    values would leak more than it prevents.

The private set lives in .content-guard-patterns.json (git-ignored). CI writes
it from the CONTENT_GUARD_PATTERNS repository secret. If it is missing the
guard fails rather than passing quietly, because a silent half-run is worse
than a broken build. Set CONTENT_GUARD_ALLOW_PARTIAL=1 to override knowingly.

Private findings report path, line and label only - never the matched text.
Actions logs on a public repo are public, so echoing the line would publish
the very value that was caught. Reproduce locally to see the text.

Exit 1 on any hit. Scans only files git tracks.
"""
import json
import os
import re
import subprocess
import sys

PUBLIC_PATTERNS = [
    ('unheld credential', 'ISO[\\s/]*(IEC[\\s/]*)?27001|OWASP',
     'certifications and board candidacy Richard does not hold'),
    ('unowned: work queues', 'hash-partitioned',
     "wallet team's work, not his"),
    ('unowned: deploy shape', 'deployed shape|health-checked Docker|warmed ahead of known spikes|sheds the hot payment',
     'deployment topology he did not design'),
    ('inflated: MeterMo', 'double-counted|device telemetry|usage integrity',
     'exactly-once telemetry ingestion was not the work'),
    ('dropped: Event Sourcing', 'Event Sourcing',
     'mechanism is attempt records + rowversion'),
    ('unfalsifiable', 'exceed\\w*\\s+(those\\s+of\\s+)?conventional banking|millions of (users|transactions)',
     'cannot be substantiated'),
    ('personality test', 'DISC\\s*&|Values Index|\\bENTP\\b',
     'public-CV noise'),
    ('unowned: cluster orch', '\\bAKS\\b|\\bKubernetes\\b|\\bK8s\\b',
     'no cluster-orchestration skill; Docker and containerisation stay'),
    ('self-deprecating', 'unglamorous',
     'a reader decides that, not the author'),
    ('merge conflict', '^<{7} |^={7}$|^>{7} ',
     'unresolved conflict markers'),
]

PRIVATE_PATTERNS_FILE = os.environ.get(
    "CONTENT_GUARD_PATTERNS", ".content-guard-patterns.json"
)


def load_private_patterns():
    """Load the patterns that must not live in a public file."""
    if not os.path.exists(PRIVATE_PATTERNS_FILE):
        if os.environ.get("CONTENT_GUARD_ALLOW_PARTIAL") == "1":
            print(
                "::warning::content-guard: private pattern set not found at "
                f"{PRIVATE_PATTERNS_FILE} - running with editorial patterns only"
            )
            return []
        print(
            f"::error::content-guard: private pattern set not found at "
            f"{PRIVATE_PATTERNS_FILE}. In CI, write it from the "
            f"CONTENT_GUARD_PATTERNS secret. Locally, restore your copy. "
            f"Set CONTENT_GUARD_ALLOW_PARTIAL=1 only if you accept a partial scan."
        )
        sys.exit(1)
    try:
        with open(PRIVATE_PATTERNS_FILE, encoding="utf-8") as fh:
            data = json.load(fh)
        return [
            (entry["label"], entry["pattern"], entry.get("why", ""))
            for entry in data["patterns"]
        ]
    except (ValueError, KeyError, TypeError) as exc:
        print(f"::error::content-guard: private pattern set is malformed - {exc}")
        sys.exit(1)


SKIP_SUFFIXES = (".png", ".jpg", ".jpeg", ".gif", ".ico", ".docx", ".woff", ".woff2")
# The guard describes what it forbids, so it would always match itself.
SKIP_PATHS = (".github/workflows/", "scripts/content-guard.py")


def tracked_files():
    out = subprocess.run(["git", "ls-files"], capture_output=True, text=True, check=True)
    for f in out.stdout.splitlines():
        if f.lower().endswith(SKIP_SUFFIXES):
            continue
        if any(f.startswith(p) or f == p for p in SKIP_PATHS):
            continue
        yield f


def read_text(path):
    """A published PDF is what a reader actually downloads, so it gets scanned too.

    Diff tools show it as `(binary)` and the eye never lands on it, which makes it
    the easiest place for something already removed from the markdown to survive.
    A missing extractor fails loudly rather than quietly waving the file through.
    """
    if path.lower().endswith(".pdf"):
        try:
            out = subprocess.run(
                ["pdftotext", "-layout", path, "-"],
                capture_output=True,
                text=True,
                check=True,
            )
            return out.stdout
        except (OSError, subprocess.CalledProcessError):
            print(
                f"::error file={path}::cannot extract text - install poppler-utils "
                f"so the guard can read published PDFs"
            )
            sys.exit(1)
    return open(path, encoding="utf-8", errors="replace").read()


def main():
    private = load_private_patterns()
    rules = [(l, p, w, False) for l, p, w in PUBLIC_PATTERNS]
    rules += [(l, p, w, True) for l, p, w in private]
    print(
        f"content-guard: {len(PUBLIC_PATTERNS)} editorial + {len(private)} private "
        f"patterns"
    )

    failures = []
    scanned = 0
    for path in tracked_files():
        try:
            text = read_text(path)
        except OSError:
            continue
        scanned += 1
        for lineno, line in enumerate(text.splitlines(), 1):
            for label, pattern, why, is_private in rules:
                if re.search(pattern, line, re.IGNORECASE | re.MULTILINE):
                    failures.append(
                        (path, lineno, label, why, line.strip()[:110], is_private)
                    )

    print(f"content-guard: scanned {scanned} tracked files")
    if not failures:
        print("content-guard: clean")
        return 0

    for path, lineno, label, why, snippet, is_private in failures:
        if is_private:
            # Never echo the matched text: these logs are public.
            print(
                f"::error file={path},line={lineno}::[{label}] matched a private "
                f"pattern - reproduce locally to see the line"
            )
        else:
            print(f"::error file={path},line={lineno}::[{label}] {why} -- {snippet}")

    print(f"\ncontent-guard: {len(failures)} finding(s).")
    print("Each pattern marks something previously removed on purpose. If a hit is")
    print("legitimate, remove the pattern in the same commit and say why.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
