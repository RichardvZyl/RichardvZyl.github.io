#!/usr/bin/env python3
"""Content guard for Richard's public career repos.

Every pattern here corresponds to something that actually went wrong in these
repositories, not a generic template. Structure checks are a floor; the real
risk in a public repo written by multiple agents is what the words say.

Exit 1 on any hit. Scans only files git tracks.
"""
import re
import subprocess
import sys

# (label, regex, why it is here)
FORBIDDEN = [
    # --- Personally identifying, from the payslips and severance application ---
    ("SA ID number",        r"\b9403175\d{6}\b",            "ID number appears on payslips"),
    ("bank account",        r"\b4086266157\b",              "account number on payslip"),
    ("branch code",         r"\b632005\b",                  "branch code on payslip"),
    ("tax reference",       r"\b1820092177\b",              "SARS reference on payslip"),
    ("employee number",     r"\bRRTVAN013\b",               "payroll employee number"),
    ("mobile number",       r"\b0?82[\s-]?775[\s-]?6655\b", "kept off public pages by decision"),
    ("home address",        r"Cura\s+ave|Equestria",        "street address on payslip"),
    ("date of birth",       r"\b17\s+Mar(ch)?\s+1994\b",    "DOB on payslip"),

    # --- Compensation: never public, in any repo ---
    # No leading \b: "R130,000" has no word boundary between R and 1.
    ("compensation figure", r"(?<!\d)1[,.]?56\d[,.]?\d{3}(?!\d)|(?<!\d)130[,.\s]?000(?!\d)|(?<!\d)97[,.\s]?187(?!\d)|(?<!\d)117[,.\s]?769(?!\d)|R\s?850\s*(/|per)\s*h",
                            "salary and rate figures"),
    ("payroll grade",       r"CU\s*-\s*Skilled Technical",  "EE occupational band; reads as 'junior'"),

    # --- Another person's identity and credentials (site template origin) ---
    ("template author",     r"\bXien\b|xiensingh|Xee Holdings|Bondis|iX Online",
                            "the friend whose design the site was adapted from"),
    ("unheld credential",   r"ISO[\s/]*(IEC[\s/]*)?27001|OWASP",
                            "certifications and board candidacy Richard does not hold"),
    ("wrong city",          r"\bDurban\b",                  "template author's city, not Richard's"),

    # --- Claims withdrawn as not Richard's to make ---
    ("unowned: work queues", r"hash-partitioned",           "wallet team's work, not his"),
    ("unowned: deploy shape", r"deployed shape|health-checked Docker|warmed ahead of known spikes|sheds the hot payment",
                            "deployment topology he did not design"),
    ("inflated: MeterMo",   r"double-counted|device telemetry|usage integrity",
                            "exactly-once telemetry ingestion was not the work"),

    # --- Claims withdrawn as inaccurate or unfalsifiable ---
    ("dropped: Event Sourcing", r"Event Sourcing",          "mechanism is attempt records + rowversion"),
    ("unfalsifiable",       r"exceed\w*\s+(those\s+of\s+)?conventional banking|millions of (users|transactions)",
                            "cannot be substantiated"),
    ("personality test",    r"DISC\s*&|Values Index|ENTP",  "public-CV noise"),

    # --- Security disclosure about a former employer ---
    ("security disclosure", r"operator proxy|hammer the ledger|watched that happen",
                            "described an exploitable path at a named employer"),

    # --- Client and product names under the disclosure limit ---
    ("client/product name", r"medimatters|CubeSandbox|ktk-play|KTK Play|AEZLedger|WhiteLabelBanking",
                            "architecture may be described; names may not"),

    # --- Superseded employment facts ---
    ("stale employment",    r"seeking new challenges|recruitment agency|technical screening",
                            "the venture was never launched; the reason was stale"),

    # --- Self-deprecation ---
    ("self-deprecating",    r"unglamorous",                 "a reader decides that, not the author"),

    # --- Mechanical ---
    ("merge conflict",      r"^<{7} |^={7}$|^>{7} ",        "unresolved conflict markers"),
]

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
    the easiest place for something already removed from the markup to survive.
    A missing extractor fails loudly rather than quietly waving the file through.
    """
    if path.lower().endswith(".pdf"):
        try:
            out = subprocess.run(["pdftotext", "-layout", path, "-"],
                                 capture_output=True, text=True, check=True)
            return out.stdout
        except (OSError, subprocess.CalledProcessError):
            print(f"::error file={path}::cannot extract text - install poppler-utils "
                  f"so the guard can read published PDFs")
            sys.exit(1)
    return open(path, encoding="utf-8", errors="replace").read()


def main():
    failures = []
    scanned = 0
    for path in tracked_files():
        try:
            text = read_text(path)
        except OSError:
            continue
        scanned += 1
        for lineno, line in enumerate(text.splitlines(), 1):
            for label, pattern, why in FORBIDDEN:
                if re.search(pattern, line, re.IGNORECASE | re.MULTILINE):
                    failures.append((path, lineno, label, why, line.strip()[:110]))

    print(f"content-guard: scanned {scanned} tracked files")
    if not failures:
        print("content-guard: clean")
        return 0

    for path, lineno, label, why, snippet in failures:
        print(f"::error file={path},line={lineno}::[{label}] {why} -- {snippet}")
    print(f"\ncontent-guard: {len(failures)} finding(s).")
    print("Each pattern marks something previously removed on purpose. If a hit is")
    print("legitimate, remove the pattern in the same commit and say why.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
