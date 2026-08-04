# Executable Ontology Checker

This directory contains the executable reference slice for OCP Foundation.

The checker is **not** a production validator, persistence schema, policy engine, or independent normative source. OCP documents, accepted architecture decisions, governed Patterns and artifact taxonomy remain authoritative. Code here implements a deliberately limited subset so that reviewed invariants and counterexamples become repeatable tests.

## Current scope

Implemented validators:

- Resource identity and classification;
- Operation identity, Objective resolution and explicit-intent exact-binding evidence;
- Assignment transition history, projections, applicability and participation derivation;
- Constraint structure, lifecycle, effectivity, applicability and exact-version evaluation;
- Organization and OrganizationRelationshipRecord module validation;
- Capability definition identity, namespace, supersession and exact resolution;
- Event occurrence identity and exact resolution;
- ObservationRecord attribution, optional Event linkage and Module C supersession;
- OutcomeAssessmentRecord exact target/criterion/evidence/input/evaluator binding, fail-safe evidence states and Module C supersession;
- CapabilityClaimRecord exact Resource/Capability/claimant/condition binding, temporal effectivity, Module C supersession and fail-safe attributable projection;
- the integrated non-sensitive foundation scenario;
- Concept status synchronization and dependency graph;
- artifact governance and complete-history process audit.

Implemented reference derivations include:

- `assignment_effective_at`;
- `derived_participates_in`;
- `constraint_effective_at`;
- `constraint_applicable_to`;
- `effective_constraint_result`;
- `constraint_blocks`;
- `constraint_set_decision`;
- `resolve_capability_definition`;
- `resolve_event`;
- `observations_for_event`;
- `resolve_outcome_assessment`;
- `outcome_assessment_heads`;
- `effective_outcome_conclusion`;
- `resolve_capability_claim`;
- `capability_claim_effective_at`;
- `capability_claim_heads`;
- `effective_capability_claim`.

## Manifest discipline

The checker uses exact module manifests:

- `rules.yaml` — core, governance, Objective, Capability and Event/Observation codes and derivations;
- `organization-rules.yaml` — Organization module;
- `assessment-rules.yaml` — OCP-011 OutcomeAssessmentRecord module;
- `capability-claim-rules.yaml` — OCP-012 CapabilityClaimRecord module.

Each manifest is checked for exact equality against its exported code and derivation sets. Adding an emitted code or derivation without a cited defining source fails unit tests.

Module manifests do not create independent normative authority. Their `source` fields point back to OCP specifications, decisions or governance contracts.

## Pattern invocation policy

A `Uses-Patterns` invocation uses `P-NNN@x.y.z` checker syntax and must resolve to an existing Pattern whose current `Version` exactly equals the invoked version.

The repository policy is **track-current**, not historical pinning. A Pattern version change must update all invokers atomically and pass the applicable review lane.

ObservationRecord and OutcomeAssessmentRecord invoke `P-001@0.1.0` with selected Module C supersession. CapabilityClaimRecord selects Modules A and C for time-bounded applicability plus history-preserving correction/withdrawal. Their domain semantics remain in OCP-010, OCP-011 and OCP-012 respectively.

## Authority and exact references

Checker fixtures serialize some opaque governed references as `identity@version`. The delimiter is harness syntax unless the owning OCP document explicitly makes it normative.

Resolvers use exact normalized identities. They do not select by:

- label;
- newest timestamp;
- list order;
- source count;
- evaluator count;
- superseding record recency;
- fuzzy similarity.

Zero or multiple exact candidates fail closed.

## Event and ObservationRecord envelope

OCP-010 defines Event as reusable occurrence identity and ObservationRecord as a separate attributable record.

`resolve_event(events, event_ref)` compares exact `event_id` only. Equal kind or time does not collapse identity.

`observations_for_event(observations, event_ref)` returns all structurally valid exact-linked observations. The deterministic output sort has no truth or priority meaning.

ObservationRecord without `event_ref` remains a valid unresolved assertion. Supersession preserves prior records, allows branching and defines no newest/current/truth winner.

## OutcomeAssessmentRecord envelope

OCP-011 defines the assessment fixture contract:

```yaml
assessment:
  assessment_id: ASM-001
  assessment_kind_ref: objective-achievement@1
  target_kind_ref: objective@1
  target_ref: OBJ-001
  criterion_ref: neutral.asset-condition-assessment@1
  evidence_bindings:
    - evidence_kind_ref: observation-record@1
      evidence_ref: OBS-001
  evidence_snapshot_ref: SNAP-EVIDENCE-001
  input_snapshot_ref: SNAP-INPUT-001
  evidence_state: sufficient
  evaluator_ref: EVALUATOR-001
  evaluated_at: 2026-08-04T01:00:00Z
  recorded_at: 2026-08-04T01:01:00Z
  conclusion: achieved
  provenance_ref: ACT-ASM-001
  supersedes_assessment_ref: ASM-000 # optional
```

The initial reference subset supports:

- target kind `objective@1`;
- evidence kinds `event@1` and `observation-record@1`;
- conclusions `achieved`, `not_achieved`, `partially_achieved`, `indeterminate`;
- evidence states `sufficient`, `missing`, `stale`, `ambiguous`, `conflicting`.

Definitive conclusions require `evidence_state: sufficient`. Missing, stale, ambiguous or conflicting evidence permits only `indeterminate` in the baseline contract.

Evidence bindings must exact-resolve and exactly equal the immutable set stored under `evidence_snapshot_ref`. `input_snapshot_ref` must resolve independently. Current repository state is never substituted during replay.

The finite conflict probe detects disagreement among normalized bound ObservationRecord statements. It is a regression guard, not a production truth, semantic-equivalence or source-reliability engine.

The checker mechanically derives and cross-checks `missing` and the finite `conflicting` probe from current governed bindings; until AB-039 defines freshness and replay semantics, `stale` and `ambiguous` remain evaluator-attributed declarations, so the checker cannot detect `sufficient` asserted over actually stale or ambiguous evidence.

OutcomeAssessmentRecord supersession:

- preserves prior exact resolution;
- rejects self-reference, unresolved targets and cycles;
- allows branching;
- requires assessment kind, target and criterion binding identity to remain unchanged across an edge;
- does not select a newest or preferred record.

`outcome_assessment_heads` returns unsuperseded exact-bound records. `effective_outcome_conclusion` returns `indeterminate` when heads disagree or use different evidence/input snapshots. List order does not affect the projection.

The validator rejects embedded Result, Operation lifecycle-success, Objective mutable status, Capability, Readiness, authorization, Conflict, Risk and State convenience fields.

## CapabilityClaimRecord envelope

OCP-012 defines a separate identified record for one claimant's proposition about one exact Resource and one exact OCP-009 Capability version under one condition set. The checker keeps declaration authority narrow: `support_state: declared` records what the claimant said and never marks it independently verified.

The checker mechanically cross-checks `declared`/`missing` against evidence-set composition and verifies snapshot consistency. Until AB-039 defines freshness and replay semantics, the truth of `sufficient`, `stale`, `ambiguous` and `conflicting` remains an attributable recorder responsibility.

The reference slice supports Resource-only holders, exact Capability resolution, half-open effectivity intervals, evidence snapshots and branching supersession. Withdrawal is a successor assertion distinct from negative polarity. `capability_claim_heads` performs as-of replay; `effective_capability_claim` returns `indeterminate` for missing, stale, ambiguous or conflicting support and for disagreeing heads. It never uses newest timestamp, list order, claimant count or source count as authority.

Matching claim projections for two Resources preserve two Resource identities and do not decide AB-011 interchangeability.

## Integrated non-sensitive scenario

`IntegratedEventScenario` composes:

```text
Objective
→ Completed Operation
→ Resource + Established Assignment participation
→ applicable Constraint
→ Event
→ conflicting ObservationRecords
→ OutcomeAssessmentRecord
```

The cross-Concept joints are executable:

- `derived_participates_in` verifies Assignment participation;
- `constraint_applicable_to` verifies the Constraint target/context joint;
- `effective_constraint_result` verifies exact evaluation selection;
- Event and Observation references resolve exactly;
- OutcomeAssessmentRecord binds the exact Objective, evidence and input snapshots.

The accepted PR-0012 scenario now uses the proposed OCP-011 record contract rather than the former checker-local assessment probe. Conflicting evidence produces `evidence_state: conflicting` and `conclusion: indeterminate`.

The scenario proves that `Completed ≠ achieved`. Assessment conclusion does not mutate Operation lifecycle or create Capability, Readiness, authorization, admissibility, Conflict, Risk or State.

## Process-audit boundary

GitHub Rulesets remain the preventive authority for pull-request-only, squash-only and linear-history enforcement. The checker is a post-factum audit.

In `pr` context the audit skips the synthetic GitHub merge ref. In explicit `main` context it requires complete non-shallow history, validates the governed baseline and rejects any later merge commit.

PR CI also checks out the actual proposed head and runs the repository checker in `main` context. This is the mechanical Board-gate used for atomic Concept or registry transitions.

## Fixture contract

Each YAML fixture includes:

```yaml
case_id: stable-test-id
concept: governed fixture class
expected:
  valid: true | false
  error_codes: []
```

Depending on the fixture class it may also include:

```yaml
entity: {}
entries: []
events: []
observations: []
objectives: []
assessments: []
evidence_snapshots: []
input_snapshots: []
scenario: {}
contexts: []
reference: {}
```

For invalid fixtures, `error_codes` must equal the complete emitted set. Unexpected additional or missing errors fail CI.

The fixture format is a test harness, not an implementation-facing API schema.

## Regression evidence

The suite includes, among other cases:

- silent Assignment termination and invalid projections;
- contradictory or stale Constraint evaluations;
- exact Capability references and supersession;
- zero-observation Event and distinct equal-time Events;
- unresolved, duplicate and conflicting observations;
- missing/conflicting assessment evidence with `indeterminate`;
- stale evidence attempting a definitive conclusion;
- unresolved assessment target/evidence/snapshots;
- late evidence producing a successor without rewriting history;
- branching assessment heads and order-independent `indeterminate` projection;
- assessment supersession cycle and binding-identity change;
- forbidden Result/lifecycle coupling;
- valid and invalid integrated scenarios;
- artifact, Pattern, Concept-status, graph and Git-history governance probes.

## Time handling

ISO-8601 timestamps with offsets are normalized to UTC. A naive timestamp is interpreted as UTC by this reference checker. Canonical time, interval uncertainty and clock-source policy remain separate decisions.

## Run locally

```bash
python -m pip install -r tools/ontology_checker/requirements.txt
python -m unittest discover -s tools/ontology_checker/tests -v
python tools/ontology_checker/check.py tools/ontology_checker/fixtures
python tools/ontology_checker/check.py tools/ontology_checker/fixtures --context main
```

## Explicitly deferred

This slice does not provide:

- production persistence, API, UI or transport contracts;
- a production Event registry, correlation or truth-selection engine;
- universal source reliability, confidence or causal inference;
- criterion expression language or evaluator authorization;
- quantitative partial-achievement semantics;
- automatic multi-Objective or multi-Operation aggregation;
- holder-specific Capability Claims;
- Constraint-result assessment evidence kind;
- authorization, Conflict, Risk, Readiness or State semantics;
- full cross-file identity uniqueness or complete normative duplicate linter.
