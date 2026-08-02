# PR-0006 External Review Findings

- Review target: `PR-0006 — Add Executable Ontology Checker`
- Review source: external Fable 5 review provided to Architecture Board
- Decision date: 2026-08-02
- Resolution branch: `agent/pr-0006-executable-ontology-checker`
- Resolution PR: `PR #9`
- External review verdict: `Approved`
- Current Architecture Board state: ready for review; merge not approved

## Finding 1 — Effective evaluation ignored exact Constraint version

**Severity:** Blocking.

**Status:** Accepted — resolved and externally verified.

The initial `_matching_evaluation` implementation selected records by `context_ref + input_snapshot_ref` and returned the last YAML item. A stale permissive record for an older Constraint version could therefore override a current blocking result, making admissibility depend on list order.

**Resolution:**

- current `constraint_version_ref` is mandatory checker/evaluation-envelope metadata;
- it is not introduced as a new OCP-006 Constraint structural field;
- effective evaluation filters by exact Constraint version, context and snapshot;
- historical records for non-current versions remain valid history but cannot affect current derivation;
- zero matches, conflicting current-version matches, or a missing version token normalize to `indeterminate`;
- YAML record order cannot affect the result;
- regression fixture `stale-version-permissive.yaml` contains current `violated` and stale `satisfied` records;
- the unit test reverses record order and requires `violated` plus `inadmissible` in both orders.

## Finding 2 — Rule provenance manifest was incomplete

**Severity:** Moderate.

**Status:** Accepted — resolved and externally verified.

The initial manifest covered only part of the emitted validation codes and omitted the implemented `constraint_effective_at` derivation.

**Resolution:**

- `ERROR_CODES` and `DERIVATION_RULES` are explicit checker constants;
- `rules.yaml` contains every emitted validation code and every implemented derivation;
- each manifest entry cites its OCP source or clearly identified PR-0006 fixture contract;
- a meta-test requires exact equality between implementation sets and manifest sets;
- adding an emitted code or derivation without provenance now fails CI.

## Finding 3 — Checker required materialized projections

**Severity:** Moderate.

**Status:** Accepted — resolved and externally verified.

OCP-005 and OCP-006 state that lifecycle projections may be materialized. The initial checker treated absence as mismatch and therefore imposed a stronger rule than the specifications.

**Resolution:**

- absent materialized projection fields are valid;
- a present projection field must exactly equal authoritative transition history;
- derivations always recompute projections from transition history;
- positive fixtures cover Established Assignment and Constraint without materialized stage, timestamps or provenance.

## Finding 4 — Invalid fixtures tolerated unexpected extra errors

**Severity:** Minor.

**Status:** Accepted — resolved and externally verified.

Expected and actual error-code sets now require exact equality. Unexpected additional errors fail both unit tests and the fixture CLI.

## Finding 5 — One malformed YAML file stopped the entire fixture run

**Severity:** Minor.

**Status:** Accepted — resolved and externally verified.

The CLI now reports an individual malformed fixture as `FAIL`, increments the failure count and continues checking remaining files.

## Finding 6 — Concept status synchronization remained deferred

**Severity:** Minor / high-value governance automation.

**Status:** Accepted — resolved and externally verified.

The checker now compares:

- the OCP-000 Concept registry;
- the machine-readable `Concept-Statuses` projection in OCP-002 frontmatter;
- `Defines-Concepts` and `Concept-Status` in defining documents.

OCP-002 is updated to version `0.8.1` with the machine-readable projection. AB-024 is marked `Resolved`.

## Finding 7 — Time and target-scope assumptions were implicit

**Severity:** Minor.

**Status:** Accepted as clarification — resolved and externally verified.

The checker README now states:

- timezone-aware ISO-8601 values are normalized to UTC;
- naive timestamps are interpreted as UTC by this reference implementation;
- canonical time semantics remain deferred;
- `relation_scope` evaluation is deferred;
- `subject_selector` supports only the test placeholder `match_all` in this slice.

## External reviewer verdict

> All seven resolutions were verified at code and test level, including YAML order reversal and exact manifest equality. The three remaining observations are non-blocking follow-ups suitable for a later single-commit correction. From the external reviewer position, PR-0006 is approved.

## Architecture Board correction decision

> Accept the exact-version finding as blocking. Require current-version selection independent of YAML order, full rule-manifest traceability, optional materialized projections, exact fixture-error expectations, resilient malformed-YAML handling, and repository status synchronization. Preserve the checker as a reference validation layer rather than introducing new OCP-006 structural semantics. External review is complete; PR-0006 may proceed to Architecture Board review. Merge still requires an explicit Board decision and AB-040 resolution before merge.
