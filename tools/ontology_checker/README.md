# Executable Ontology Checker

This directory contains the first executable reference slice for OCP Foundation.

The checker is **not** a production validator, persistence schema, policy engine, or independent normative source. OCP documents, accepted architecture decisions and the machine-readable artifact taxonomy remain authoritative. Code in this directory implements a deliberately limited subset of those contracts so that accepted counterexamples can become repeatable tests.

## Current scope

Implemented validators:

- Resource: identity and classification presence;
- Operation: identity, plural Objective resolution, and the accepted non-Draft explicit-intent exact-binding evidence contract;
- Assignment: authoritative linear transition history, optional materialized lifecycle projections, required Established-lineage fields, applicability interval, and supersession self-reference;
- Constraint: authoritative linear transition history, optional materialized lifecycle projections, target/predicate/enforcement completeness, validity interval, exact-version evaluation selection, evaluation uniqueness, and contradictory `not_applicable` detection;
- Capability: definition structure, exact identity uniqueness, namespace-owner consistency, supersession validation, holder-coupling rejection and exact reference resolution;
- repository status synchronization: OCP-000 registry, OCP-002 machine-readable projection, and defining-document `Concept-Status`;
- artifact governance: path-derived OCP, Pattern and AD identifiers; taxonomy-allowed statuses; duplicate AB identifiers; accepted AD↔AB synchronization; and exact Pattern invocation resolution;
- process audit: main-context verification that complete post-baseline Git history contains no merge commit.

Implemented reference derivations:

- `assignment_effective_at`;
- `derived_participates_in`;
- `constraint_effective_at`;
- `constraint_applicable_to`;
- `effective_constraint_result`;
- `constraint_blocks`;
- `constraint_set_decision`;
- `resolve_capability_definition`.

## Artifact-governance authority

`architecture/artifact-taxonomy.yaml` is the machine-readable source for artifact classes and the policies implemented by the governance checker.

The checker reads, rather than hardcodes:

- `AB.active_states`, currently `Open`, `Proposed`, `Discovery`, and `Under Review`;
- `Pattern.version_format`, currently `semver`;
- `Pattern.invocation_version_policy`, currently `track-current`;
- the obligation to atomically update all Pattern invokers when a Pattern version changes;
- the complete-history, post-baseline process-audit scope and governed baseline SHA.

Legacy AD-001 metadata is read from its historical heading and bullet format when YAML frontmatter is absent. This compatibility parser does not authorize new legacy-format AD files.

## Pattern invocation policy

A `Uses-Patterns` invocation uses `P-NNN@x.y.z` checker syntax and must resolve to an existing Pattern whose current `Version` exactly equals the invoked version.

The policy is **track-current**, not historical pinning. A Pattern version change must be accompanied in the same PR by atomic updates to every invoker, with the applicable review lane for affected normative artifacts. Historical versions are not treated as separately resolvable repository artifacts.

Malformed invocation syntax, missing Pattern identity, invalid Pattern semver, and current-version mismatch are distinct validation failures.

## Process-audit boundary

GitHub Rulesets remain the preventive authority for pull-request-only, squash-only and linear-history enforcement. The checker is a post-factum audit.

In `pr` context the process audit is intentionally skipped because GitHub's synthetic pull-request merge ref has two parents and is not repository merge history.

In `main` context the audit:

1. requires a non-shallow repository;
2. reads the full-SHA `history_audit_baseline` from taxonomy;
3. requires that baseline to be an ancestor of `HEAD`;
4. searches `<baseline>..HEAD` for commits with two or more parents;
5. fails closed when the baseline or Git history cannot be inspected.

Taxonomy `0.4.0` sets the baseline to `fc15d2dfc6d0529735347d8c78dd0e3e5225721d`, the last accepted legacy merge before squash-only enforcement. The baseline and earlier merge commits are historical evidence and are not reclassified as current violations. Any merge commit after that baseline emits `PROCESS_HISTORY_NON_LINEAR`.

The workflow checks out with `fetch-depth: 0`. A shallow clone emits `PROCESS_HISTORY_SHALLOW`; an absent, malformed, unreachable baseline or Git infrastructure failure emits `PROCESS_HISTORY_AUDIT_FAILED`. Neither condition can report PASS. PR CI also checks out the actual proposed head and runs the repository checker explicitly in `main` context, avoiding false evidence from GitHub's synthetic merge ref.

## Authority and version envelope

OCP-006 requires an evaluation result for the exact Constraint version and input snapshot. The current version token is supplied by the checker fixture/evaluation envelope:

```yaml
reference:
  constraint_version_ref: C-001@2
```

This is checker harness metadata, not a new field in the OCP-006 Constraint structural contract. Historical evaluation records for older versions may remain in `evaluation_records`, but they are excluded from the effective result for the current version.

If the current version has no authoritative result, has contradictory results, or the version token is absent, derivation returns `indeterminate`. YAML list order never decides admissibility.

## Operation explicit-intent evidence envelope

OCP-004 treats `intent_version_ref` and `validation_rule_ref` as opaque references that distinguish identity and immutable version. The reference fixture harness serializes those references as `identity@version`; the `@` delimiter is checker-envelope syntax, not a normative OCP-004 wire format.

The checker selects explicit-intent evidence by exact string equality across `intent_version_ref`, `validation_rule_ref`, and `input_snapshot_ref`. Multiple exact-binding immutable records are permitted when all results agree. List order and `evaluated_at` never break a tie or select an authoritative record; divergent exact-binding results are conflicting.

The harness trusts `intent_version_ref` to identify an immutable version of all binding-relevant intent content, including `statement`. Detecting reuse of an old version token after substantive content changed is outside this reference checker's capability and must be prevented by the authoring/versioning authority.

When no unambiguous exact-binding effective result exists, the normative projection is `not_evaluated`. A materialized `validation_status: passed` or `failed` is therefore a mismatch and cannot create a more permissive Operation.

## Capability registry reference envelope

OCP-009 defines a structured exact reference:

```yaml
reference:
  namespace: mobility
  capability_id: navigate
  version: v1
```

The checker compares all three components by exact string equality. It does not define a delimiter, choose a latest version, use `published_at` as a tie-break, match by label, or redirect a superseded reference to a successor.

Fixture `entries` form the reference registry dataset. `resolve_capability_definition(entries, reference)` returns one valid exact record or `None`. Duplicate exact identities are ambiguous and therefore cannot create an authoritative positive result.

Supersession is validated as an exact same-identity version edge: the target must exist, use the same namespace and `capability_id`, differ by version, and remain acyclic. A superseded historical version remains resolvable by its own exact reference.

The registry validator rejects embedded holder, possession, readiness, availability, authorization and admissibility assertions. Resource context included in a fixture does not create a Capability claim.

Holder-coupling rejection is a finite key probe, not a semantically complete implementation of OCP-009 invariant 12. Review of normative artifacts remains responsible for detecting unlisted holder-specific semantics, and the probe list may be expanded in later cycles.

## Materialized projections

OCP-005 and OCP-006 allow lifecycle projections to be materialized but do not require them.

Accordingly:

- an omitted `lifecycle_stage`, lifecycle timestamp, or provenance projection is valid;
- if a projection field is present, it must exactly match authoritative transition history;
- derivations always use projections recomputed from transition history, not independently stored fields.

## Regression fixtures and governance probes

The suite includes:

- an Established Assignment with a materialized `terminal_at` but no terminal transition;
- an applicable Constraint with a stored `not_applicable` result;
- a stale permissive result for an older Constraint version below a current blocking result;
- advisory uncertainty producing `review_required`, not `inadmissible`;
- valid Established Assignment and Constraint fixtures without materialized projections;
- deterministic Capability exact-version resolution;
- equal Capability labels in different namespaces that remain distinct identities;
- superseded Capability exact references that do not redirect;
- unresolved and duplicate Capability references that fail closed;
- Capability supersession cycles, namespace-owner conflicts and holder-coupled registry entries;
- same-type Resource context that does not create a Capability claim;
- duplicate AB identifiers;
- malformed, missing and stale Pattern invocations;
- non-semver Pattern versions;
- a legacy merge at the configured baseline that remains valid;
- a merge commit after the baseline, including one below `HEAD`, that is rejected;
- an unreachable baseline and a shallow Git clone that must fail closed;
- a real-repository proposed-head run in explicit `main` context.

The `not_applicable` case intentionally tests two independent layers:

1. validation reports `CONSTRAINT_NOT_APPLICABLE_CONTRADICTION`;
2. derivation still normalizes the stored result to `indeterminate`.

This defense-in-depth is intentional.

## Fixture contract

Each YAML fixture contains:

```yaml
case_id: stable-test-id
concept: Resource | Operation | Assignment | Constraint | Capability | CapabilityRegistry | CapabilityReference
reference: {} # checker-only evaluation or exact-resolution metadata when required
entries: [] # Capability registry dataset when required
expected:
  valid: true | false
  error_codes: []
entity: {}
contexts: [] # optional; used by Constraint and boundary fixtures
```

For invalid fixtures, `error_codes` must equal the complete emitted error set. Unexpected additional errors fail CI.

The fixture format is a reference test contract, not an implementation-facing API schema.

## Time handling

ISO-8601 timestamps with offsets are normalized to UTC. A naive timestamp without an offset is interpreted as UTC by this reference checker. The ontology's canonical time and timezone model remains deferred.

## Run locally

```bash
python -m pip install -r tools/ontology_checker/requirements.txt
python -m unittest discover -s tools/ontology_checker/tests -v
python tools/ontology_checker/check.py tools/ontology_checker/fixtures
python tools/ontology_checker/check.py tools/ontology_checker/fixtures --context main
```

The CLI reports malformed YAML as a failure for that file and continues checking the remaining fixtures.

## Explicitly deferred

This slice does not yet provide:

- a production or cross-repository Capability registry; OCP-009 support is a local reference dataset and resolver only;
- holder-specific Capability claims or Resource/Organization possession semantics;
- duplicate normative-rule detection;
- cross-file identity uniqueness beyond the Capability fixture dataset and other currently governed artifact classes;
- full Operation lifecycle validation;
- a Constraint expression language or production evaluator interface;
- `relation_scope` evaluation semantics;
- `subject_selector` semantics beyond the test-only `match_all` placeholder;
- quantity, capacity, geometry, spectrum, authorization, Conflict, Risk, Readiness, or State semantics;
- database, API, or UI contracts.

Every emitted validation code and derivation must cite its defining source in `rules.yaml`. `GOVERNANCE_ERROR_CODES`, `CAPABILITY_ERROR_CODES` and the other checker code sets participate in the same exact-equality manifest meta-test, so adding an error or derivation without provenance fails CI.
