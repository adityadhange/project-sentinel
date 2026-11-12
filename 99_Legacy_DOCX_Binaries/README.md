# Legacy DOCX binary archive

This directory preserves the original Word documents that were previously stored throughout `02_Archive_Legacy/`.

## Preservation rules

- All 130 source DOCX files were moved here without modifying their Git blobs.
- Their original directory hierarchy is retained beneath this directory.
- The original Git blob SHA for each file is unchanged by the move.
- Do not delete, overwrite, convert in place, or treat these historical documents as current canonical instructions.
- `.gitattributes` marks this directory and all DOCX files as `export-ignore`, excluding them from Git archive/source ZIP exports.
- Embedded fonts and other package assets remain inside each original DOCX; no standalone font files were found in the repository at the time of segregation.

Markdown conversions, if later required, must be created as separate derived artifacts with source-to-output provenance and validation. The DOCX originals remain the preservation baseline.
