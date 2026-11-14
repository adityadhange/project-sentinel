# SNT-TO-18 Duplicate Candidate Verification Report

## Scope and safety boundary

This is a verification-only report for issue #90. It does not delete, rename, overwrite, consolidate, or edit any candidate artifact. The original cleanup manifest is preserved unchanged. No row in this report authorizes cleanup.

## Evidence snapshot

- Existing manifest: `.github/audits/exact-duplicate-cleanup-manifest-2026-11-11.csv`
- Source manifest commit: `00c01e8e594e27862313e9b70d63767d681c894f`
- Verification snapshot commit: `35dfe80844edb4d4672ad588b23bffdd7b368d1d`
- Manifest rows: **170**
- Unique manifest Git blob SHA values: **86**
- Current tracked paths matching manifest blobs: **131**
- Current active-scope matches: **0** (expected zero; all matched copies remain under `02_Archive_Legacy/`)

## Classification result

| Classification | Rows | Meaning |
|---|---:|---|
| `EXACT_BYTE_DUPLICATE` | 165 | Current-tree blob match with independently recomputed byte size and SHA-256 agreement. |
| `UNVERIFIED` | 5 | No current checked-out file permits the required independent recomputation. |
| `CONTENT_DIFFERENT` | 0 | No new content-difference candidate was introduced by this exact-duplicate manifest verification. |
| `NEAR_DUPLICATE` | 0 | Filename/title similarity was not treated as proof and no similarity classification was performed. |
| `HISTORICAL_VERSION` | 0 | Exact-byte candidates were not relabeled as distinct historical versions; provenance signals are recorded separately. |
| `COLLISION` | 0 | No destination/name collision analysis was part of this existing exact-duplicate manifest. |

## Unresolved rows

Five rows are `UNVERIFIED`. They are historical DOCX candidates whose Git objects are still present in repository history, but whose files are absent from the current checked-out tree. Their documented provenance is that the DOCX files were downloaded, converted to Markdown, re-uploaded, and then intentionally removed. The ledger now records each historical object byte count, independently computed historical-object SHA-256, and status `HISTORICAL_OBJECT_CONFIRMED_CURRENT_FILE_UNVERIFIED`. Because issue #90 requires recomputation from current repository files, historical object availability alone is not elevated to an exact-duplicate classification.

- Row 24: `01 - SOURCE ARCHIVE/Organized_Legacy_Versions/Kernel v3.5/Copy of 01_sentinel-master-task-register (Kernel v3.5.0 Ratified).md.docx` vs `01 - SOURCE ARCHIVE/Organized_Legacy_Versions/Kernel v3.5/01_sentinel-master-task-register (Kernel v3.5.0 Ratified).md(1).docx`; blob `3bd8eb09a7e153140448285aaaebf16d3eeb11b6`; 223660 bytes.
- Row 56: `01 - SOURCE ARCHIVE/Organized_Legacy_Versions/Kernel v3.5/Copy of [SUPERSEDED] 02_Sentinel_Master_Roadmap (Kernel v3.5.0 Ratified).docx` vs `01 - SOURCE ARCHIVE/Organized_Legacy_Versions/Kernel v3.5/[SUPERSEDED] 02_Sentinel_Master_Roadmap (Kernel v3.5.0 Ratified).docx`; blob `f8d838006db6e8a7aa6d1eb71dbec23b96eff7a9`; 220035 bytes.
- Row 57: `01 - SOURCE ARCHIVE/Organized_Legacy_Versions/Kernel v3.5/Copy of [SUPERSEDED] 02_sentinel-decisions-approval-ledger (Kernel v3.5.0 Ratified).docx` vs `01 - SOURCE ARCHIVE/Organized_Legacy_Versions/Kernel v3.5/[SUPERSEDED] 02_sentinel-decisions-approval-ledger (Kernel v3.5.0 Ratified).docx`; blob `a65cace7d8f23770f65154116a6decfaa8617616`; 221012 bytes.
- Row 58: `01 - SOURCE ARCHIVE/Organized_Legacy_Versions/Kernel v3.5/Copy of [SUPERSEDED] 03_sentinel-capability-permissions-register (Kernel v3.5.0 Ratified).docx` vs `01 - SOURCE ARCHIVE/Organized_Legacy_Versions/Kernel v3.5/[SUPERSEDED] 03_sentinel-capability-permissions-register (Kernel v3.5.0 Ratified).docx`; blob `38a91713c6313235ccecc399e982f028d3e52e47`; 221160 bytes.
- Row 59: `01 - SOURCE ARCHIVE/Organized_Legacy_Versions/Kernel v3.5/Copy of v3.5.0 04_sentinel-shared-operating-contract (Kernel v3.5.0 Ratified).docx` vs `01 - SOURCE ARCHIVE/Organized_Legacy_Versions/Kernel v3.5/v3.5.0 04_sentinel-shared-operating-contract (Kernel v3.5.0 Ratified).docx`; blob `3c0a194c35e412bd33f8db3e3cbba8a6d4f9d01c`; 222808 bytes.

## Historical Kernel v3.5 DOCX evidence update

The five unresolved rows are not missing from Git history. Their historical Git objects are available, and the object sizes match the original manifest byte counts exactly. This is stronger historical evidence, but it does not change their current-checkout classification.

| Row | Historical object bytes | Historical SHA-256 | Current-checkout status | Ledger status |
|---:|---:|---|---|---|
| 24 | 223660 | `bad46ff768eaa233b1025348a50832a0ab6ad9bf46fe03d05ee7ce65c7ef0d36` | No current matching path | `HISTORICAL_OBJECT_CONFIRMED_CURRENT_FILE_UNVERIFIED` |
| 56 | 220035 | `a4f5b718ef2eaad4f8ea0db0b687f35d2b1b22ada0aea3f3c1c3d179d40ca582` | No current matching path | `HISTORICAL_OBJECT_CONFIRMED_CURRENT_FILE_UNVERIFIED` |
| 57 | 221012 | `4d6643487fb872ffd2dc9a8d6030f4502278b02b3c884b0168b94d03ad13d350` | No current matching path | `HISTORICAL_OBJECT_CONFIRMED_CURRENT_FILE_UNVERIFIED` |
| 58 | 221160 | `2671465f4b2884c14f0983414af7006fc5e59c1c9f3fc1129adcbc21b70d240c` | No current matching path | `HISTORICAL_OBJECT_CONFIRMED_CURRENT_FILE_UNVERIFIED` |
| 59 | 222808 | `03157580be184bfbcca0e993f5f0543169c38396994290a155a57b036e87fadc` | No current matching path | `HISTORICAL_OBJECT_CONFIRMED_CURRENT_FILE_UNVERIFIED` |

The status update documents historical provenance and marks these five rows `EXCLUDED_FROM_CLEANUP`; it does not authorize recovery, deletion, or any new cleanup action.

## DOCX conversion and cleanup disposition

The five historical Kernel v3.5 DOCX rows are retained as `UNVERIFIED` for evidence integrity because their current checked-out bytes cannot be recomputed. Their provenance is now explicitly recorded as downloaded DOCX sources that were converted to Markdown, re-uploaded, and then removed. They are therefore marked `EXCLUDED_FROM_CLEANUP`; they are not proposed removal candidates under SNT-TO-19.

The 165 current-tree exact-byte rows remain subject to separate retained-copy review and explicit per-file Principal Operator authorization.

## Reference and provenance assessment

The ledger performs a conservative literal-reference scan across current tracked, UTF-8, non-archive operational files, excluding audit records and filename inventory artifacts. It checks historical full paths and basenames. A basename match is only a review signal, not proof of an operational dependency.

- Rows with active literal full-path mentions: **0**
- Rows with active basename mentions: **0**
- Historical path signals such as `Copy of`, numeric suffixes, chained `.md` extensions, `_Recovered_Duplicate_Copies`, and `[SUPERSEDED]` are recorded in the ledger but are not used as proof of duplication.

## Disposition

All `EXACT_BYTE_DUPLICATE` rows remain candidates only. They require separate operator review, explicit retained-path confirmation, reference review, and authorization under issue #91. The `UNVERIFIED` rows must not be removed without recovering or independently inspecting the underlying artifacts.

The machine-readable ledger is [`reports/snt-to-18-duplicate-verification-2026-11-14.csv`](../reports/snt-to-18-duplicate-verification-2026-11-14.csv).
