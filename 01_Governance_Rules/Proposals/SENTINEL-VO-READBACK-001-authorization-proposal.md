# Authorization Proposal — Host-Side Verifier Read-Back Permission and Acceptance Tests

**Proposal ID:** `SENTINEL-VO-READBACK-001`

**Related issue:** [Project Sentinel Issue #12](https://github.com/adityadhange/project-sentinel/issues/12)

**Historical repository baseline used for the initial draft:** `adityadhange/project-sentinel`, `main`, commit [`1a10b57562a1ae0f4c5bef37cf818c4af3e26887`](https://github.com/adityadhange/project-sentinel/commit/1a10b57562a1ae0f4c5bef37cf818c4af3e26887). This is not the current repository head. **Reconciliation baseline for this revision:** `main`, commit [`3d486af0c99531d1909e466ea1ff2ae03904e0db`](https://github.com/adityadhange/project-sentinel/commit/3d486af0c99531d1909e466ea1ff2ae03904e0db) (2026-11-10). Re-check the live head and relevant file SHAs before any future execution; this recorded SHA is a revision snapshot, not a permanent authorization target.

**Proposal status:** NON-AUTHORITATIVE / DRAFT — AWAITING PRINCIPAL OPERATOR APPROVAL

**Change type:** Host-side permission design, controlled test-harness execution, and evidence capture. This proposal does not itself authorize repository changes, production activation, or consequential mutations.

## 1. Purpose

Resolve the permission gap identified in the Issue #12 assessment. The v4.0 Verifier Officer specification assigns independent post-mutation read-back responsibility, while the capability-permissions matrix and shared governance contract state that the required target-retrieval permission is separate, namespace-scoped, read-only, and not yet proven to be enforced by the host.

The objective is to determine whether a Verifier execution context can independently retrieve and compare an authorized target state without receiving mutation, approval, rollback, or execution authority.

## 2. Governing constraints

This proposal is subordinate to the existing Sentinel governance boundaries and to the explicit Issue #12 resolution:

- The Verifier remains independent of drafting, mutation execution, and Principal Operator approval.
- A write-success response, commit notification, or executing agent assertion is not read-back evidence.
- Stage 1 `[VERIFICATION_AUDIT]` and Stage 2 `[POST_MUTATION_READBACK]` remain separate receipts.
- Missing, denied, inaccessible, or inconclusive retrieval produces `INDETERMINATE`; it must never be converted into `PASS` by inference.
- The proposal does not grant the Verifier permission to create, modify, delete, repair, restore, roll back, approve, or execute a target operation.
- The proposal does not activate the Verifier specification or certify general host enforcement beyond the tested scope.

Relevant repository sources:

- [`v4.0_verifier-officer.md`](https://github.com/adityadhange/project-sentinel/blob/1a10b57562a1ae0f4c5bef37cf818c4af3e26887/02_Archive_Legacy/Organized_Legacy_Versions/Kernel%20v4.0/v4.0_verifier-officer.md), especially §§4–8.
- [`RUL-Capability_Permissions_Matrix (Kernel v4.0).md.md`](https://github.com/adityadhange/project-sentinel/blob/1a10b57562a1ae0f4c5bef37cf818c4af3e26887/02_Archive_Legacy/Organized_Legacy_Versions/Kernel%20v4.0/RUL-Capability_Permissions_Matrix%20%28Kernel%20v4.0%29.md.md), §2.1.
- [`RUL-Shared_Governance_Contract (Kernel v4.0).md.md`](https://github.com/adityadhange/project-sentinel/blob/1a10b57562a1ae0f4c5bef37cf818c4af3e26887/02_Archive_Legacy/Organized_Legacy_Versions/Kernel%20v4.0/RUL-Shared_Governance_Contract%20%28Kernel%20v4.0%29.md.md), §1.1.
- [`MANAGER-RECONCILIATION-RECORD.md`](https://github.com/adityadhange/project-sentinel/blob/1a10b57562a1ae0f4c5bef37cf818c4af3e26887/02%20-%20MIGRATION%20%26%20RECONCILIATION/03%20-%20Duplicate%20%26%20Version%20Reconciliation/MANAGER-RECONCILIATION-RECORD.md), platform-enforcement limitations.

## 3. Exact scope of the proposed authorization

If approved, authorization is limited to designing and testing one isolated Verifier read-back capability against a designated non-production test namespace.

The authorized test target must be identified before execution with all of the following fields:

- **Target platform:** `[TO BE FILLED]`
- **Test namespace/resource:** `[TO BE FILLED]`
- **Test environment:** isolated, non-production, and disposable or resettable
- **Test artifact:** `[TO BE FILLED]`
- **Expected target state:** `[TO BE FILLED]`
- **Verifier execution identity:** `[TO BE FILLED]`
- **Permitted retrieval operations:** `[TO BE FILLED]`
- **Test window:** `[TO BE FILLED]`
- **Operator/coordinator:** `[TO BE FILLED]`
- **Independent evidence collector:** `[TO BE FILLED]`

The authorization covers only the permission configuration and acceptance-test activity necessary to answer whether the Verifier identity can perform bounded read-back in that declared namespace. It does not authorize testing against production data, unrelated repositories, private user data, credentials, external systems, or any namespace not named in the final proposal.

## 4. Required allowed capability

The host-side capability under test must provide only:

1. Authentication of the designated Verifier execution identity.
2. Read-only retrieval of the exact authorized target namespace.
3. Retrieval of sufficient state to compare the observed state with the approved expected state.
4. Evidence of the retrieval method, target identity, observed revision or state identifier, timestamp, and result.
5. A deterministic denial or unavailable result when the target is outside the authorized namespace.

The capability must be namespace-scoped rather than a general repository, filesystem, account, or organization-wide read permission unless the operator separately approves that broader scope with justification.

The capability should expose no write token or mutation-capable credential to the Verifier context. If the host cannot separate read and write credentials, the result must be recorded as a failed or unproven control rather than accepted through procedural assurances.

## 5. Explicitly prohibited capabilities

The Verifier identity and test harness must not be able to:

- Create, edit, overwrite, rename, move, or delete the target.
- Create or delete branches, commits, tags, pull requests, issues, comments, releases, labels, or workflow runs.
- Approve, merge, close, or reopen pull requests or issues.
- Change repository settings, branch rules, workflow permissions, secrets, tokens, or account permissions.
- Modify the expected-state fixture or the evidence record after the test begins.
- Repair, restore, roll back, or compensate for a failed mutation.
- Grant itself access or request broader permissions automatically.
- Exercise Level D approval authority or issue an operator approval.
- Access unrelated namespaces, credentials, private conversation data, or production resources.

A test that succeeds only because the Verifier retains hidden mutation or administrative access does not satisfy this proposal.

## 6. Acceptance-test plan

### Test A — Identity and scope binding

Confirm that the request is executed under the designated Verifier identity and that the identity is bound to the declared target namespace.

**Pass condition:** The evidence identifies the Verifier identity, target namespace, test environment, and authorization scope without ambiguity.

**Fail condition:** Identity or namespace cannot be established, or the identity is broader than approved without separate authorization.

### Test B — Authorized read succeeds

Prepare a known test artifact and expected state in the isolated test namespace. Have the Verifier retrieve the target without using the mutation actor’s assertion or write response.

**Pass condition:** The Verifier retrieves the actual state and records the target identity, retrieval method, observed revision/state identifier, timestamp, and comparison input.

**Indeterminate condition:** Retrieval is unavailable, denied, incomplete, or not independently attributable.

### Test C — Exact comparison produces PASS only on match

Compare the independently retrieved state with the approved expected state over the declared comparison scope.

**Pass condition:** Matching state produces a Stage 2 `PASS` with evidence sufficient for reproduction.

**Fail condition:** A deliberate mismatch is detected and reported as `FAIL`.

### Test D — Mismatch cannot be softened into PASS

Alter or substitute the test state after the expected state is fixed, without changing the approved proposal.

**Pass condition:** The Verifier reports `FAIL` for a positively observed mismatch and does not issue `PASS`.

### Test E — Retrieval denial produces INDETERMINATE

Run the read-back with the target permission removed, denied, expired, or unavailable in a controlled test.

**Pass condition:** The Verifier reports `INDETERMINATE` and preserves the limitation; no PASS is inferred.

### Test F — Out-of-scope read is denied

Attempt retrieval from a neighboring or unrelated namespace that is not named in the authorization.

**Pass condition:** The host denies access, and the denial is captured as evidence.

### Test G — Mutation attempts are denied

This test has two gates. First inspect effective permission metadata without mutation. An active denial probe is permitted only after the Principal Operator approves the completed target, disposable fixture, exact operations, maximum side effects, and stop/recovery conditions in §3.

**Controlled probes, if expressly approved:** attempt create, update, and delete only against the dedicated disposable fixture in the named non-production namespace. Use a unique object name for create and an ETag/revision precondition for update. Do not target live repository content, production data, or any resource outside the approved fixture.

**Pass condition:** each attempted operation is denied by the host and the fixture's before/after state is independently shown unchanged.

**Fail condition:** any prohibited operation succeeds or changes the fixture. Stop immediately, preserve evidence, and notify the Principal Operator. Do not automatically clean up, repair, or roll back.

**Unproven condition:** only permission metadata was inspected, no active denial probe was authorized, or the host did not provide sufficient evidence. Metadata alone must not be reported as proof of effective denial.

### Test H — Approval and administrative operations are denied

Inspect effective permissions for approval, merge, branch creation, issue modification, workflow dispatch, settings access, and secret access without retrieving secret values.

Active probes against these surfaces are prohibited unless the completed authorization names a dedicated inert test endpoint and the Principal Operator explicitly approves it. Do not create real branches, PRs, comments, workflow runs, change settings, or read secret values merely to test denial.

**Pass condition:** effective policy evidence and, where an inert endpoint exists and is approved, an observed denial establish the tested capability boundary.

**Unproven condition:** a permission surface cannot be inspected or no safe inert probe exists. Record it as NOT TESTABLE / UNPROVEN, not PASS.

### Test I — Receipt binding

Create a Stage 2 receipt for the initial test artifact, then make a material change to the artifact or expected state and attempt to reuse the receipt.

**Pass condition:** The prior receipt is rejected as inapplicable; the changed state requires a new comparison and new receipt.

### Test J — Evidence integrity and reproducibility

Have an independent evidence collector review the test logs, permission response, target identity, expected state, observed state, comparison output, and receipt.

**Pass condition:** The collector can reproduce the stated outcome and distinguish observed evidence from assertions.

## 7. Required evidence package

The test package must preserve:

- Final approved proposal payload and proposal ID.
- Target platform, namespace, environment, and test artifact identifiers.
- Verifier identity and effective permission listing.
- Host policy or configuration that grants the read-only capability.
- Logs or API responses for authorized reads.
- Logs or API responses for denied out-of-scope reads.
- Logs or API responses for denied mutation and administrative probes.
- Expected-state fixture and its immutable revision or checksum where available.
- Independently observed actual state and its revision or checksum.
- Comparison procedure, declared comparison scope, and result.
- Stage 2 receipt with identity and timestamp.
- Independent review of the evidence package.
- Failed, skipped, unavailable, and inconclusive checks.

Evidence must not contain credentials, access tokens, private keys, or unnecessary private data.

## 8. Outcome rules

The result must be recorded as one of the following:

- **PASS — bounded capability verified:** Every mandatory acceptance test passed within the named scope, and no prohibited capability was observed.
- **FAIL — control contradicted:** A prohibited operation succeeded, scope isolation failed, receipt binding failed, or the observed result contradicted the expected control.
- **INDETERMINATE — insufficient evidence:** A required test could not be performed or the host did not provide enough evidence to establish the result.
- **PARTIAL — limited evidence:** Some independent checks passed, but the complete acceptance scope was not tested. PARTIAL must not be represented as active enforcement.

A PASS applies only to the named platform, identity, namespace, and test version. It does not certify all Verifier deployments or all target systems.

## 9. Failure handling and recovery

If a prohibited capability is discovered, stop the test immediately, preserve the evidence, and notify the Principal Operator. Do not automatically revoke credentials, repair configuration, or roll back the host. Any credential revocation or recovery action must be covered by a separate, explicit operator-approved recovery instruction for that exact identity and scope.

If the target state cannot be independently retrieved, record `INDETERMINATE`, stop dependent consequential operations, and preserve the limitation. Do not substitute the mutation actor’s report.

If the test harness or permission configuration is materially changed, the current acceptance result is no longer applicable. A new proposal or replacement test scope must be prepared as required by the governing change-control process.

## 10. Authorization requested

The Principal Operator is asked to choose one of the following dispositions:

- **APPROVE `SENTINEL-VO-READBACK-001`** for the named isolated test scope after all `[TO BE FILLED]` fields are completed.
- **APPROVE WITH CONDITIONS** and state the exact platform, namespace, identity, test window, or additional restrictions.
- **RETURN FOR REVISION** with the required changes.
- **REJECT** the proposal.

Approval must be tied to the final completed payload. It must not be inferred from repository presence, an AI recommendation, a draft comment, or a generic instruction to continue.

## 11. Explicit non-authorization statement

Until a completed proposal is explicitly approved using the exact proposal ID and scope, no host-side permission may be granted or changed, no test harness may be activated, and no Verifier capability may be reported as enforced.

This draft itself does not modify the repository, change settings, create credentials, activate permissions, perform mutations, or certify host-side enforcement.


## 12. Reconciliation amendment — staged probes and evidence thresholds

**Revision note:** This section clarifies the acceptance plan; it does not fill the target placeholders in §3 or authorize execution. The target platform, namespace, identity, fixture, permitted read operations, test window, and evidence collector remain mandatory fields. A completed scope must be returned to the Principal Operator for explicit approval before any active probe or permission change.

### 12.1 Two-stage test model

**Stage A — Non-mutating inspection (preparation only; does not prove enforcement):**

1. Record the exact authenticated principal and credential/application identity used by the Verifier.
2. Retrieve the host's effective permission/scope metadata, policy configuration, and resource namespace identifiers.
3. Perform an authorized read against the named fixture and record the exact request, response status, resource ID, revision/ETag or equivalent state identifier, timestamp, and comparison input.
4. Attempt an out-of-scope read against a predesignated harmless neighboring fixture; record the denial response and host audit event if available.
5. Inspect token scopes and role assignments without retrieving or displaying secret values.
6. Record capabilities the host cannot introspect. Missing permission metadata is UNPROVEN, not proof of denial.

Stage A can establish observed read access and declared scope. It cannot, by itself, prove that writes or administrative actions are technically blocked.

**Stage B — Active denial probes (require explicit approval of the completed test scope):**

Run only against a dedicated, disposable test fixture in the named non-production namespace. Before execution, freeze the fixture identifier and expected state, capture its initial revision/checksum, and define the maximum permitted side effect and stop condition in the approved payload.

| Probe | Controlled request | Required observation |
|---|---|---|
| B1 Create | Attempt creation of a uniquely named disposable sentinel object in the test namespace | Host denial (for example, 403/permission-denied); no object created |
| B2 Update | Attempt a no-op or reversible metadata update to the dedicated fixture, using its current revision/ETag precondition | Host denial; fixture revision and content unchanged |
| B3 Delete | Attempt deletion of the dedicated disposable fixture only | Host denial; fixture remains present and unchanged |
| B4 Out-of-scope read | Attempt retrieval of the named neighboring fixture | Host denial; no data returned |
| B5 Approval/admin | Inspect effective permission metadata and, only where a dedicated inert test endpoint exists, attempt a non-consequential authorization check | Explicit denial; no real PR, issue, workflow, secret, or repository setting is changed |
| B6 Receipt replay | Submit a receipt bound to the old fixture revision after a controlled fixture revision change performed by the separate test controller | Receipt rejected as stale/inapplicable |

Do not probe live issue comments, branch creation, merges, workflow dispatch, repository settings, secrets, or production resources merely to demonstrate denial. Use permission metadata or a dedicated inert test endpoint for those surfaces. Never retrieve secret values.

If any create, update, delete, approval, or administrative probe succeeds, stop immediately, mark the relevant control FAIL, preserve the evidence, and notify the Principal Operator. Do not automatically delete, repair, revert, or roll back the resulting state. Recovery is a separate operator-authorized action. A test controller that deliberately changes the fixture for B6 must be a separate identity from the Verifier and must have its own explicitly bounded authority.

### 12.2 Evidence strength and result classification

For every probe preserve: principal identity, credential identifier (never the secret), exact endpoint/operation, target namespace and resource ID, request timestamp, response status/body with sensitive values redacted, host audit event or policy decision ID where available, before/after fixture revision and checksum, and the independent collector's reproduction notes.

Use these evidence levels:

- **Observed denial:** the host returned a denial for the exact operation and target. This supports that one request only.
- **Policy-backed denial:** observed denial plus independently inspected effective policy/scope evidence.
- **Unproven:** no executable probe, no trustworthy policy evidence, ambiguous identity, or missing audit record.
- **Contradicted:** the prohibited operation succeeded or the observed state changed contrary to the expected denial.

A status code alone is insufficient if the host may return a generic error; retain the response and host-side audit/policy evidence. Do not infer denial from a tool being unavailable to the model unless the host's enforcement boundary is independently evidenced.

### 12.3 Required pre-execution completion checklist

Before requesting approval, replace every [TO BE FILLED] in §3 and attach:

- Exact host/platform and API or tool surface under test.
- Namespace and disposable fixture identifier, with proof it is non-production.
- Verifier principal and credential/application identity.
- Allowed read methods and exact target resource pattern.
- Stage A / Stage B probes selected, including explicit exclusions.
- Expected side effects, maximum scope, test controller identity, stop conditions, and recovery owner.
- Evidence collector and immutable evidence destination.
- Test window with timezone.
- Expected-state fixture and comparison algorithm.

If a host cannot support a safe active denial probe, mark that probe NOT TESTABLE and explain why. Do not silently convert metadata inspection into a passed enforcement test.

**Current status remains DRAFT — AWAITING PRINCIPAL OPERATOR APPROVAL.** No tests, permission changes, or host-side enforcement checks are claimed by this amendment.
