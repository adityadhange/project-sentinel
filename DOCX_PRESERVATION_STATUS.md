# DOCX preservation status

**Status:** No DOCX source-of-record is currently established in this repository.

## Evidence

- PR [#60](https://github.com/adityadhange/project-sentinel/pull/60) added the legacy DOCX archive under `99_Legacy_DOCX_Binaries/` without content changes. The merge commit was `ea7377a642ab1d7090426a654bba93c39d38d4b0`; its tree contained 129 tracked `.docx` files.
- Commit [`4b24eea`](https://github.com/adityadhange/project-sentinel/commit/4b24eea8f4d1c311ce2b3ef88e3b47d114fe629e), dated 2026-11-12, is titled `chore: remove downloaded legacy DOCX binaries from repository` and deletes the archive contents. It is directly present in the current `main` history.
- Current `main` at `2bc3ec563ebb5fc3370b027cbc51397288a8853b` contains no `99_Legacy_DOCX_Binaries/` directory and no tracked `.docx` files.

## Disposition

This repository records the DOCX binaries as intentionally absent from the current tracked tree based on the explicit removal commit. That commit does **not** establish whether copies exist elsewhere, so external preservation is **unverified**. This change does not restore, delete, relocate, or convert any DOCX file.

The DOCX verification workflow therefore checks the true current invariant: the retired archive root is absent, no `.docx` files are tracked, and the protective `.gitattributes` export-ignore rules remain present. If a future operator authorizes a DOCX source-of-record, that change must establish provenance, inventory, and reviewable hashes before changing this invariant.
