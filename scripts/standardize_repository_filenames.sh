#!/usr/bin/env bash
set -Eeuo pipefail

# Project Sentinel SNT-TO-17 filename repair
# Default: dry-run. Apply only with --apply.
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "ERROR: run inside a Git repository." >&2; exit 2; }
cd "$ROOT"
MANIFEST="${1:-docs/filename-repair-manifest.tsv}"
MODE="${2:---dry-run}"
if [[ "$MODE" != "--dry-run" && "$MODE" != "--apply" ]]; then
  echo "Usage: $0 [manifest.tsv] [--dry-run|--apply]" >&2; exit 2
fi
[[ -f "$MANIFEST" ]] || { echo "ERROR: manifest not found: $MANIFEST" >&2; exit 2; }
if [[ "$MODE" == "--apply" ]]; then
  if [[ "$(git branch --show-current)" == "main" ]]; then
    echo "ERROR: refusing to rename directly on main. Use a dedicated branch." >&2; exit 2
  fi
  if [[ -n "$(git status --porcelain)" ]]; then
    echo "ERROR: working tree must be clean before applying." >&2; exit 2
  fi
fi

declare -a SOURCES=() TARGETS=() SHAS=()
declare -A SEEN_TARGETS=()
while IFS=$'\t' read -r status sha mode source target; do
  [[ "$status" == "status" ]] && continue
  [[ -n "${status:-}" ]] || continue
  if [[ "$status" != "SAFE_CANDIDATE" ]]; then
    printf 'REVIEW ONLY (not moved): %s -> %s [%s]\n' "$source" "$target" "$status"
    continue
  fi
  [[ -n "$source" && -n "$target" && -n "$sha" ]] || { echo "ERROR: malformed manifest row." >&2; exit 2; }
  [[ -z "${SEEN_TARGETS[$target]+x}" ]] || { echo "ERROR: duplicate destination in manifest: $target" >&2; exit 2; }
  SEEN_TARGETS["$target"]=1
  [[ -f "$source" ]] || { echo "ERROR: source missing: $source" >&2; exit 2; }
  actual="$(git hash-object -- "$source")"
  [[ "$actual" == "$sha" ]] || { echo "ERROR: source hash mismatch: $source (expected $sha, got $actual)" >&2; exit 2; }
  if [[ -e "$target" ]]; then
    echo "ERROR: destination already exists: $target" >&2; exit 2
  fi
  SOURCES+=("$source"); TARGETS+=("$target"); SHAS+=("$sha")
done < "$MANIFEST"

printf 'Validated %d safe rename(s); collision/manual-review rows were not scheduled.\n' "${#SOURCES[@]}"
for i in "${!SOURCES[@]}"; do
  printf '%s -> %s\n' "${SOURCES[$i]}" "${TARGETS[$i]}"
done

if [[ "$MODE" == "--dry-run" ]]; then
  echo "DRY RUN ONLY. Re-run with --apply on a clean dedicated branch to execute."
  exit 0
fi

for i in "${!SOURCES[@]}"; do
  git mv -- "${SOURCES[$i]}" "${TARGETS[$i]}"
done
for i in "${!SOURCES[@]}"; do
  actual="$(git hash-object -- "${TARGETS[$i]}")"
  [[ "$actual" == "${SHAS[$i]}" ]] || { echo "ERROR: post-rename hash mismatch: ${TARGETS[$i]}" >&2; exit 1; }
done

mkdir -p reports
{
  printf 'source\ttarget\texpected_blob_sha\tactual_blob_sha\tstatus\n'
  for i in "${!SOURCES[@]}"; do
    actual="$(git hash-object -- "${TARGETS[$i]}")"
    printf '%s\t%s\t%s\t%s\t%s\n' "${SOURCES[$i]}" "${TARGETS[$i]}" "${SHAS[$i]}" "$actual" "PASS"
  done
} > reports/filename-repair-verification.tsv

echo "PASS: all applied rename targets match their original Git blob hashes."
echo "Next: inspect git status, review references, run repository checks, then commit and push."
