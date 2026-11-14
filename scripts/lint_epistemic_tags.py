#!/usr/bin/env python3
"""Static epistemic tag and locator syntax linter; not a truth verifier."""
import argparse
import re
import subprocess
import sys
from pathlib import Path

TAGS = {"[FACT: PRIMARY_VERIFIED]", "[INFERENCE: DEDUCTIVE_VALID]", "[GAP: UNVERIFIED_ABSTENTION]", "[REFUTED]"}
EXCLUDED_PATH_PREFIXES = ("02_Archive_Legacy/",)
TAG_RE = re.compile(r"\[(?:FACT|INFERENCE|GAP)\s*:[^\]]*\]|\[REFUTED\]", re.I)
LOCATOR_RE = re.compile(r"\[(?:Q|E|SRC|REF)-?\d+[A-Za-z0-9._-]*\]|https?://[^\s<>)]+|\[[^\]]+\]\((?:https?://|/|\.\.?/)[^)]+\)|\b[\w.-]+(?:/[\w.-]+)+\.(?:md|markdown|py|yml|yaml|json|txt)(?::L?\d+(?:-L?\d+)?)?\b|\blocator\s*:\s*\S+", re.I)
ASSERTION_RE = re.compile(r"\b(?:is|are|was|were|has|have|had|does|do|did|will|would|must|should|can|cannot|could|may|might|contains|supports|requires|provides|prevents|ensures|allows|blocks|validates|implements|demonstrates|proves|shows|indicates|means|results|causes|increases|decreases|includes|excludes|uses|depends|remains|becomes|represents|records|states|establishes|creates|maintains|fails|passes|confirms|contradicts|identifies|defines|specifies|applies|precedes|follows|matches|differs|equals)\b", re.I)

def is_excluded_path(filename):
    return any(filename.startswith(prefix) for prefix in EXCLUDED_PATH_PREFIXES)

def clean(line):
    line = re.sub(r"^(?:>\s*)+", "", line.strip())
    return re.sub(r"^(?:[-*+]|\d+[.)])\s+", "", line).strip()

def check_block(path, line_no, lines):
    raw = "\n".join(lines).strip()
    normalized = " ".join(clean(line) for line in lines).replace("|", " ").strip()
    if not normalized or normalized.endswith("?"):
        return []
    if not (ASSERTION_RE.search(normalized) or re.search(r"[.!](?:[)\]\"']*)$", normalized)):
        return []
    tags = TAG_RE.findall(raw)
    if not tags:
        return [f"{path}:{line_no}: untagged assertion; add one exact canonical epistemic tag: {', '.join(sorted(TAGS))}"]
    invalid = [tag for tag in tags if tag not in TAGS]
    if invalid:
        return [f"{path}:{line_no}: invalid/manufactured epistemic tag {invalid[0]!r}; use an exact canonical tag"]
    if len({tag.upper() for tag in tags}) != 1:
        return [f"{path}:{line_no}: mixed epistemic tags; split claims into separately tagged blocks"]
    if not raw.lstrip().startswith("|") and not normalized.upper().startswith(tags[0].upper()):
        return [f"{path}:{line_no}: epistemic tag must prefix the assertion block"]
    if tags[0].upper() != "[GAP: UNVERIFIED_ABSTENTION]" and not LOCATOR_RE.search(raw):
        return [f"{path}:{line_no}: {tags[0]} assertion lacks a concrete citation locator (e.g. [Q1], source URL, or repository path:line)"]
    return []

def lint_text(text, path="<memory>"):
    errors, block = [], []
    block_start, in_fence, fence_char = 1, False, ""
    lines = text.splitlines()
    in_front = bool(lines and lines[0].strip() == "---")
    def flush():
        nonlocal block
        if block:
            errors.extend(check_block(path, block_start, block))
            block = []
    for number, line in enumerate(lines, 1):
        if in_front:
            if number > 1 and line.strip() == "---":
                in_front = False
            continue
        fence = re.match(r"^\s*(~{3,}|" + re.escape(chr(96))*3 + r"+)", line)
        if fence:
            flush()
            marker = fence.group(1)[0]
            if not in_fence:
                in_fence, fence_char = True, marker
            elif marker == fence_char:
                in_fence = False
            continue
        if in_fence:
            continue
        if not line.strip() or re.match(r"^\s{0,3}#{1,6}\s", line) or re.match(r"^\s*(?:[-*_]\s*){3,}$", line) or re.match(r"^\s*\|?(?:\s*:?-{3,}:?\s*\|)+\s*$", line):
            flush()
            continue
        if line.lstrip().startswith("<!--"):
            flush()
            continue
        if line.lstrip().startswith("|") or re.match(r"^\s*(?:[-*+]|\d+[.)])\s+", line):
            flush()
            block, block_start = [line], number
            flush()
            continue
        if not block:
            block_start = number
        block.append(line)
    flush()
    return errors

def main():
    parser = argparse.ArgumentParser(description="Lint changed Markdown for epistemic tags and citation locators.")
    parser.add_argument("--base-ref", required=True)
    parser.add_argument("--head-ref", required=True)
    args = parser.parse_args()
    try:
        result = subprocess.run(["git", "diff", "--name-only", "--diff-filter=ACMR", f"{args.base_ref}...{args.head_ref}", "--", "*.md", "*.markdown"], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as exc:
        print(f"ERROR: cannot determine changed Markdown files: {exc}", file=sys.stderr)
        return 2
    changed_files = [name for name in result.stdout.splitlines() if name]
    files = [name for name in changed_files if not is_excluded_path(name)]
    excluded_files = [name for name in changed_files if is_excluded_path(name)]
    failures = []
    for filename in files:
        path = Path(filename)
        if not path.is_file():
            failures.append(f"{filename}: changed Markdown file is unavailable")
            continue
        try:
            failures.extend(lint_text(path.read_text(encoding="utf-8"), filename))
        except UnicodeDecodeError:
            failures.append(f"{filename}: Markdown is not valid UTF-8")
    if failures:
        print(f"Epistemic Markdown lint failed: {len(failures)} violation(s).", file=sys.stderr)
        for failure in failures:
            print(f"::error::{failure}", file=sys.stderr)
        return 1
    print(
        f"Epistemic Markdown lint passed: {len(files)} changed Markdown file(s) checked; "
        f"{len(excluded_files)} archived file(s) excluded."
    )
    print("Static tag/locator validation only; factual truth and deductive validity remain human/Verifier responsibilities.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
