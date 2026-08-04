---
Document-ID: OCP-011
Title: Outcome Assessment Record Contract
Version: 0.2.0
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-004, OCP-006, OCP-008, OCP-010, AD-006, P-001
Uses-Patterns: P-001@0.1.0
Used-By: Objective Achievement, Operation Outcome Views, Capability Claim Evidence, Coordination, Audit
Last-Review: 2026-08-04
---

# OCP-011 — Outcome Assessment Record Contract

## 1. Authority and incorporated contract body

Architecture Board accepts OCP-011 revision `0.2.0` as the governed implementation of outcome `R3` from AD-006C.

The complete externally reviewed contract body is preserved verbatim in [`reviewed-contract-v0.1.1.md`](reviewed-contract-v0.1.1.md). The following parts of that immutable review artifact are incorporated into this Accepted specification without semantic alteration:

- §§1–18 — definition, purpose, ontological boundary, target contract, structure, field semantics, evidence matrix, authority, derivations, P-001 conformance, boundaries, semantic rules, invariants, executable evidence and integrated scenario;
- §§20–22 — explicit exclusions, open questions and external falsification evidence.

The annex frontmatter and its §§19 and 23 preserve the pre-acceptance migration/status state and are historical review evidence only. Where they differ from this README, the Result resolution and Architecture Board decision below are authoritative.

This split is publication mechanics only: it preserves the exact reviewed text while making document lifecycle and the acceptance act unambiguous.

## 2. Accepted normative baseline

**OutcomeAssessmentRecord** is an identified attributable record under `P-001@0.1.0`, Module C. It is not a fundamental Concept `Result`, not a lifecycle field of Operation and not mutable authoritative state of Objective.

The initial endpoint and evidence envelope remains:

```text
target_kind_ref: objective@1

evidence_kind_ref:
- event@1
- observation-record@1
```

Every record exact-binds:

```text
assessment_id
assessment_kind_ref
target_kind_ref
target_ref
criterion_ref
evidence_bindings[]
evidence_snapshot_ref
input_snapshot_ref
evidence_state
evaluator_ref
evaluated_at
recorded_at
conclusion
provenance_ref
supersedes_assessment_ref [optional]
```

The accepted evidence/conclusion baseline is:

| Evidence state | Allowed authoritative conclusion |
|---|---|
| `sufficient` | `achieved`, `not_achieved`, `partially_achieved` or `indeterminate` according to the exact criterion |
| `missing` | only `indeterminate` |
| `stale` | only `indeterminate` |
| `ambiguous` | only `indeterminate` |
| `conflicting` | only `indeterminate` |

Operation completion, absence of negative evidence, newest timestamp, evaluator count, source count or list order cannot manufacture a definitive conclusion.

## 3. P-001 Module C and derivations

Accepted supersession semantics preserve prior records, allow branching, reject self-reference/unresolved targets/cycles and prohibit one edge from changing assessment kind, target or criterion binding identity. No newest/current/truth winner is selected automatically.

Accepted reference derivations are:

```text
resolve_outcome_assessment
outcome_assessment_heads
effective_outcome_conclusion
```

Multiple unsuperseded exact-bound heads that disagree or use different evidence/input snapshots project only `indeterminate`. Historical records remain exact-resolvable.

## 4. Evidence-state trust boundary

The reference checker mechanically derives and cross-checks `missing` and its finite `conflicting` probe from governed bindings.

Until AB-039 accepts freshness and deterministic replay semantics, truth of self-declared `stale` and `ambiguous` remains attributable evaluator responsibility. A declared `sufficient` state is not proof that evidence is actually current or unambiguous.

This limitation is explicit and fail-safe: any declared non-sufficient state still permits only `indeterminate` under the baseline contract.

## 5. Integrated scenario

The accepted non-sensitive scenario composes Objective, Completed Operation, Resource, Assignment, Constraint, Event, conflicting ObservationRecords and OutcomeAssessmentRecord.

Its cross-Concept joints remain executable through:

```text
derived_participates_in
constraint_applicable_to
effective_constraint_result
exact Event resolution
exact ObservationRecord resolution
```

The scenario continues to prove:

```text
Completed Operation + conflicting evidence = indeterminate, not achieved
```

## 6. Result registry resolution

AD-006C gave a negative independent-identity verdict for a fundamental Result Concept. Acceptance of OCP-011 completes the temporary migration accounting:

1. `OutcomeAssessmentRecord` is Accepted as a governed non-Concept record contract;
2. `AB-056` is `Resolved`;
3. `Result: Proposed` is removed from the active OCP-000 Concept registry;
4. Result is removed from the generated Foundation map;
5. OCP-000 and OCP-002 preserve the negative identity decision in prose;
6. no `Result: Accepted`, `Result: Deprecated`, `Result: Archived` or defining Result Concept document is introduced.

This is deregistration after a negative identity verdict, not a Concept lifecycle promotion, deprecation or archival. Descriptive or local uses of the word `result`, including Constraint evaluation result, do not create a fundamental Result Concept.

## 7. External review evidence

External adversarial review tested hidden Result identity, implicit bindings, permissive evidence handling, history loss, order-dependent heads, lifecycle coupling and integrated-scenario regression.

One Minor finding identified the previously implicit trust boundary for `stale` and `ambiguous`. Revision `0.1.1` made that boundary explicit and named AB-039 as the future freshness/replay owner.

Repeated external review verified the resolution and approved head `46d24ac460e5e36e8911918105e54342e7c03d4d` for Architecture Board acceptance. The semantic implementation was squash-merged in PR #37 as `6519d9a257abb5c97bf51cacbfe4ba770a166dfc` before this separate atomic status/registry act.

## 8. Architecture Board decision

On 2026-08-04, Architecture Board accepts OCP-011 revision `0.2.0` and decides:

1. accept OutcomeAssessmentRecord as the governed R3 contract under P-001 Module C;
2. retain exact target, criterion, evidence snapshot, input snapshot, evaluator, time and provenance bindings;
3. retain fail-safe evidence/conclusion semantics and history-preserving branching supersession;
4. retain the explicit `stale`/`ambiguous` trust boundary until AB-039;
5. resolve AB-056;
6. deregister the fundamental Result candidate after AD-006C's negative identity verdict;
7. preserve eight Accepted fundamental Concepts—OutcomeAssessmentRecord remains a non-Concept record contract;
8. close the complete AD-006 axis: Event occurrence, ObservationRecord and OutcomeAssessmentRecord.
