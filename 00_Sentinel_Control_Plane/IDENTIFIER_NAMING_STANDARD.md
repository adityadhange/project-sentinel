# Specialist Identifier Naming Standard

**Status:** Operator-confirmed naming decision  
**Applies to:** Active Sentinel control-plane documents and future architecture specifications

## Canonical identity

The canonical identifier for the offline architecture-advisory role is:

`co-developer`

It is an **offline advisory role**, not a member of the five-person runtime specialist fleet. It does not receive runtime execution permissions, tool permissions, mutation authority, or Level D approval authority by virtue of its name or registry entry.

## Naming rules

1. Use `co-developer` when referring to this offline advisory role.
2. Reserve the `SKL-*` namespace for active specialist skill identifiers.
3. Do not introduce a runtime skill identifier formed by joining `SKL-` and `co-developer`.
4. Treat the historical spelling formed by joining `SKL-` and `co-developer` as a legacy alias only when quoting or documenting preserved historical source material.
5. Do not rewrite, rename, delete, or otherwise mutate files in the immutable source archive solely to normalize this identifier.
6. New active documents, control-plane references, workflow configuration, and generated records must use `co-developer`.

## Reconciliation disposition

The v4.0 Persona Registry's `co-developer` label is canonical. The alternate spelling in the historical v4.0 Capability Permissions Matrix is a legacy naming inconsistency, not evidence of a separately provisioned runtime skill.

This decision resolves the identifier question only. It does not resolve or expand the role's authority, permissions, activation status, or capabilities.

## Enforcement

The GitHub Actions workflow `audit_co_developer_naming.yml` checks tracked text files. It fails when the legacy alias appears outside `01 - SOURCE ARCHIVE/`, and reports preserved historical occurrences without modifying them.

Historical occurrences are intentionally visible in the audit report. Their presence is not a failure while they remain confined to the source archive.
