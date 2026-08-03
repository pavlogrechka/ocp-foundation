# AB-043 External Review Findings

- Review target: `PR #25 — AB-043 — Expand Foundation Artifact Governance Checks`
- Initial reviewed head: `15c373eaeab594c8faedc67bc82d1bf2fe768b40`
- F1–F6 resolution head: `d08aab1916c3826180a6fe5631561b6aac48d830`
- F7 resolution head: `f5862af65536cb94db15efd235ba7e338bb4a619`
- Resolution PR: `PR #25`
- Merge commit: `93c04f6b2205b97459ccdd795624acf3118cbad5`
- Decision date: 2026-08-03
- External review verdict: `Approved`
- Architecture Board decision comments: `5171790618`, `5172258235`
- Transient materialization PR: `PR #26`, closed without merge

## Finding 1 — Governance codes were absent from the provenance manifest

**Severity:** Blocking.

**Status:** Accepted — resolved and externally verified.

The initial artifact-governance module emitted validation codes that did not participate in the exact `rules.yaml` manifest equality check. CI could therefore remain green while provenance coverage regressed.

**Resolution:**

- all 14 governance and process-audit codes are exported through `GOVERNANCE_ERROR_CODES`;
- every code has a source entry in `rules.yaml`;
- the existing exact-equality meta-test includes the governance code set;
- `manifest_version` advanced to `0.4.0`.

## Finding 2 — Process history audit failed open

**Severity:** Blocking.

**Status:** Accepted — resolved and externally verified.

The initial workflow used shallow checkout and inspected only `HEAD`. A real merge could therefore be hidden by the shallow boundary, and a merge below `HEAD` was not inspected.

**Resolution:**

- workflow checkout uses `fetch-depth: 0`;
- shallow history emits `PROCESS_HISTORY_SHALLOW` rather than PASS;
- unavailable Git inspection emits `PROCESS_HISTORY_AUDIT_FAILED`;
- the audit inspects governed history rather than only the latest commit;
- integration tests use real temporary Git repositories and real merge commits.

## Finding 3 — Checker-owned policies lacked a normative source

**Severity:** Moderate.

**Status:** Accepted — resolved by explicit Architecture Board decision and externally verified.

The initial checker hardcoded which AB states were active and required `Uses-Patterns` to match the current Pattern version without a governed policy source.

**Resolution:**

- taxonomy `0.4.0` owns `AB.active_states: [Open, Proposed, Discovery, Under Review]`;
- taxonomy owns Pattern `semver` and `track-current` invocation policy;
- a Pattern version change requires atomic update of every invoker and the applicable review lane;
- checker reads these policies from taxonomy rather than defining them independently.

## Finding 4 — Diagnostics conflated infrastructure and version defects

**Severity:** Minor.

**Status:** Accepted — resolved and externally verified.

Git inspection failures previously reused an artifact metadata code, and a non-semver Pattern version could surface as a misleading missing reference.

**Resolution:**

- process infrastructure failures have dedicated fail-closed codes;
- invalid Pattern semver emits `PATTERN_VERSION_INVALID`;
- malformed, missing and current-version-mismatch references remain distinct failures.

## Finding 5 — Checker documentation omitted the new governance boundary

**Severity:** Minor.

**Status:** Accepted — resolved and externally verified.

**Resolution:** the checker README and human-readable taxonomy now document artifact authority, legacy AD parsing, AB active states, Pattern `track-current`, complete-history requirements, baseline scope, PR synthetic merge-ref handling and every fail-closed mode.

## Finding 6 — Declared counterexamples lacked executable tests

**Severity:** Minor.

**Status:** Accepted — resolved and externally verified.

**Resolution:** tests now cover duplicate AB identifiers, malformed and missing Pattern references, stale Pattern versions, invalid Pattern semver, taxonomy-owned active states, merge history, shallow clones and Git infrastructure failure.

## Finding 7 — Full-history audit rejected accepted legacy history

**Severity:** Blocking.

**Status:** Accepted — resolved by explicit Architecture Board decision and externally verified.

The first F1–F6 resolution correctly audited all reachable history, but the real `main` branch contains three merge commits created before squash-only enforcement. A real-repository `--context main` run therefore failed permanently even though no new violation existed.

**Resolution:**

- taxonomy `0.4.0` defines `history_audit_baseline: fc15d2dfc6d0529735347d8c78dd0e3e5225721d`;
- the baseline is the last accepted legacy merge before squash-only enforcement;
- the checker requires a full SHA and verifies that the baseline is an ancestor of `HEAD`;
- audit scope is exactly `<baseline>..HEAD`, excluding the baseline and earlier historical evidence;
- missing, malformed or unreachable baseline evidence fails closed with `PROCESS_HISTORY_AUDIT_FAILED`;
- executable regression tests prove merge at baseline → PASS and merge after baseline → FAIL;
- CI checks out the actual proposed PR head and executes the repository checker in explicit `main` context, avoiding false evidence from GitHub's synthetic merge ref.

## Final executable evidence

At final reviewed head `f5862af65536cb94db15efd235ba7e338bb4a619`:

- 50/50 unit tests passed;
- 25/25 fixtures matched exact expected results;
- artifact governance, status synchronization, Concept graph and generated-map checks passed;
- PR-context validation passed;
- actual proposed-head `main`-context validation passed against the real repository history;
- shallow, unreachable-baseline, merge-at-baseline and merge-after-baseline probes passed.

After squash merge `93c04f6b2205b97459ccdd795624acf3118cbad5`, the first `main`-context checker run also succeeded according to the post-merge monitor evidence.

## External reviewer verdict

> Findings F1–F7 are resolved and verified. The real-history audit passes, all required fail-closed cases and counterexamples are executable, and the final PR tree contains no builder artifacts. From the external reviewer position, head `f5862af` is approved. Merge remains an explicit Architecture Board decision.

## Architecture Board decisions

The Architecture Board:

1. selected taxonomy-owned AB active states and Pattern `track-current` policy before the F1–F6 resolution commit;
2. selected the full-SHA post-baseline history contract before the F7 resolution commit;
3. approved and squash-merged PR #25 after repeated external review;
4. retained the checker as a reference implementation subordinate to OCP documents, accepted decisions and machine-readable taxonomy.
