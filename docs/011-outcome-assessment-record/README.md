---
Document-ID: OCP-011
Title: Outcome Assessment Record Contract
Version: 0.3.0
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-004, OCP-006, OCP-008, OCP-010, AD-006, AD-012, P-001
Uses-Patterns: P-001@0.1.0
Used-By: Objective Achievement, Operation Outcome Views, Capability Claim Evidence, Coordination, Audit
Last-Review: 2026-08-05
---

# OCP-011 — Outcome Assessment Record Contract

## 1. Authority and incorporated contract body

Revision `0.2.0` established the governed implementation of outcome `R3` from AD-006C. Revision `0.3.0` preserves that record contract and activates the contract-local F1/A1 semantics selected by AD-012B for the new exact assessment kind `objective-achievement@2`.

The complete externally reviewed contract body is preserved verbatim in [`reviewed-contract-v0.1.1.md`](reviewed-contract-v0.1.1.md). The following parts of that immutable review artifact are incorporated into this Accepted specification without semantic alteration:

- §§1–18 — definition, purpose, ontological boundary, target contract, structure, field semantics, evidence matrix, authority, derivations, P-001 conformance, boundaries, semantic rules, invariants, executable evidence and integrated scenario;
- §§20–22 — explicit exclusions, open questions and external falsification evidence.

The annex frontmatter and its §§19 and 23 preserve the pre-acceptance migration/status state and are historical review evidence only. Revision `0.3.0` §§9–15 are a later normative amendment: their F1/A1 rules are authoritative for `objective-achievement@2`, while the annex's attributable trust boundary continues for `objective-achievement@1`. Where the annex differs from this README on lifecycle, Result resolution or the activated kind, this README is authoritative.

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
derive_outcome_evidence_usability
```

Multiple unsuperseded exact-bound heads that disagree or use different evidence/input snapshots project only `indeterminate`. Historical records remain exact-resolvable.

## 4. Evidence-state trust boundary

The reference checker mechanically derives and cross-checks `missing` and its finite `conflicting` probe from governed bindings for both supported assessment kinds.

For `objective-achievement@1`, `stale` and `ambiguous` remain attributable evaluator statements under F0/A0. The activation fields defined below are forbidden, so an implementation cannot present that legacy kind as machine-derived.

For `objective-achievement@2`, the checker exact-resolves the local F1/A1 rules, derives freshness plus the governed ambiguity dimensions, and cross-checks the inline states and findings. Missing authority or an unresolved, future-dated or incomparable input is non-permissive.

For both kinds, any non-sufficient `evidence_state` permits only `indeterminate`. A declared or derived `fresh` state does not prove that evidence is true, reliable, sufficient, available, authorizing or indicative of Readiness.

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

## 8. Initial Architecture Board decision

On 2026-08-04, Architecture Board accepts OCP-011 revision `0.2.0` and decides:

1. accept OutcomeAssessmentRecord as the governed R3 contract under P-001 Module C;
2. retain exact target, criterion, evidence snapshot, input snapshot, evaluator, time and provenance bindings;
3. retain fail-safe evidence/conclusion semantics and history-preserving branching supersession;
4. retain the explicit `stale`/`ambiguous` trust boundary until AB-039;
5. resolve AB-056;
6. deregister the fundamental Result candidate after AD-006C's negative identity verdict;
7. preserve eight Accepted fundamental Concepts—OutcomeAssessmentRecord remains a non-Concept record contract;
8. close the complete AD-006 axis: Event occurrence, ObservationRecord and OutcomeAssessmentRecord.

## 9. AD-012B activation boundary

Revision `0.3.0` adds one explicit semantic boundary without changing record family, target kinds, evidence kinds or P-001 invocation:

| `assessment_kind_ref` | Freshness and ambiguity authority | Required behavior |
|---|---|---|
| `objective-achievement@1` | F0/A0 attributable baseline | Existing fields and fail-safe matrix remain valid; activation fields are forbidden. |
| `objective-achievement@2` | Activated contract-local F1/A1 | Exact local rules, immutable rule-input bindings and inline derived states are mandatory. |
| any other version | no authority | Reject; an unknown version cannot bypass either boundary. |

`objective-achievement@2` adds these mandatory fields to the structure in §2:

```text
freshness_rule_ref
freshness_state
ambiguity_rule_ref
ambiguity_state
ambiguity_findings[]
  - dimension_ref
  - reason_ref
  - basis: rule-derived | attributable
```

The `input_snapshot_ref` for an activated record resolves an immutable input snapshot that exact-binds the same `criterion_ref`, `freshness_rule_ref` and `ambiguity_rule_ref`. The evidence snapshot continues to exact-bind the evidence set. A missing or mismatched binding never falls back to a current rule, a caller-selected default or repository state.

Changing `objective-achievement@1` to `@2` is not correction of the same assessment binding. Assessment kind is part of the Module C binding identity, so a supersession edge cannot cross this boundary. Historical `@1` records remain exact-resolvable and attributable.

## 10. Contract-local freshness rule

An activated freshness rule has this complete governed shape:

```text
rule_ref
protected_assessment_kind_ref: objective-achievement@2
criterion_ref
evaluation_time_source: evaluated_at
comparison_precision: microsecond
evidence_policies[]
  - evidence_kind_ref
  - temporal_fact_ref
  - max_age_seconds
  - cutoff: inclusive | exclusive
missing_temporal_fact: indeterminate
future_temporal_fact: indeterminate
incomparable_temporal_fact: indeterminate
```

For the initial evidence envelope, the only admitted temporal-fact bindings are:

| Evidence kind | Exact temporal fact | Record field read |
|---|---|---|
| `event@1` | `event-occurred-at@1` | `occurred_at` |
| `observation-record@1` | `observation-observed-at@1` | `observed_at` |

The rule never substitutes Event/Observation recording time, receipt time, newest timestamp or wall clock. `evaluated_at` and `recorded_at` on an activated record must be offset-aware and comparable. A current query supplies its own explicit offset-aware query time. Comparison preserves parsed microseconds; `max_age_seconds` is a finite non-negative integer, so no implementation may invent rounding or truncation.

For every bound evidence item, age is `evaluation time - selected temporal fact`. An inclusive cutoff classifies equality as `fresh`; an exclusive cutoff classifies equality as `stale`. If any usable item exceeds its own cutoff, the aggregate freshness state is `stale`. If a required fact, evidence item, rule, rule version or comparable time is unavailable, or if the selected fact is future-dated, the state is `indeterminate`. With no evidence bindings, the state is `not_applicable` and the existing evidence state is `missing`.

The executable non-sensitive activation uses exact criterion `neutral.condition@1`, freshness rule `objective-achievement-freshness.neutral-condition@1`, an inclusive 600-second `observed_at` policy and an inclusive 3600-second `occurred_at` policy. These numbers are inputs of that exact reference contract only. They are neither platform defaults nor claimed production lifetimes, and no other criterion or consumer may inherit them.

## 11. Contract-local ambiguity rule

The initial A1 rule names two machine-verifiable dimensions:

- `reference@1` — exact activation input, rule or evidence cannot be resolved;
- `temporal@1` — evaluation time or the selected evidence time is missing, future-dated or incomparable.

The exact non-sensitive rule `objective-achievement-ambiguity.neutral-condition@1` protects `objective-achievement@2` under criterion `neutral.condition@1`. It names `reference@1` and `temporal@1` as machine dimensions and `semantic-classification@1` as attributable. The governed machine-derived reasons are finite:

| Dimension | Reason | Meaning |
|---|---|---|
| `reference@1` | `activation-input-unresolved@1` | An exact rule, snapshot, evidence item or other activation input has zero or multiple resolutions. |
| `temporal@1` | `evaluation-time-incomparable@1` | The explicit evaluation/query time cannot be compared. |
| `temporal@1` | `temporal-fact-missing@1` | The exact selected temporal fact is absent. |
| `temporal@1` | `temporal-fact-future@1` | The selected fact occurs after the explicit evaluation/query time. |
| `temporal@1` | `temporal-fact-incomparable@1` | The selected fact is timezone-less or otherwise incomparable. |

Every machine finding uses `basis: rule-derived`. A semantic-classification finding uses `basis: attributable`, carries an exact versioned reason selected by the evaluator and remains non-permissive. OCP-011 does not infer semantic equivalence, contradiction or preference from prose, labels, timestamps, record order, evaluator count or source count.

`ambiguity_state` is `clear` only when the exact rule derives no finding and the evaluator records no attributable finding. Otherwise it is `ambiguous`. The finite ObservationRecord disagreement probe remains `conflicting`, not a semantic-ambiguity engine; legitimate conclusions under different exact criteria or query contexts are neither ambiguity nor conflict merely because they differ.

## 12. Inline evidence-state composition

The activated record stores the historical freshness and ambiguity result inline. The checker derives the same result from the exact rule, snapshots and `evaluated_at`, then enforces this precedence:

| Condition | Required `evidence_state` |
|---|---|
| no evidence bindings | `missing` |
| finite actual ObservationRecord disagreement | `conflicting` |
| one or more ambiguity findings | `ambiguous` |
| clear but outside a governed freshness cutoff | `stale` |
| clear and within every governed cutoff | `sufficient` |

This composition does not redefine sufficiency as truth. `sufficient` means only that the exact activated temporal and ambiguity guards did not force a narrower non-permissive state; the exact assessment criterion and attributable evaluator still own the conclusion. Any other state permits only `conclusion: indeterminate`.

`effective_outcome_conclusion` may project a definitive activated head only when the complete Objective, evidence, snapshot and exact-rule context validates. Calling it with an `objective-achievement@2` record alone returns `indeterminate`; record shape cannot substitute for activation authority.

## 13. Historical replay and explicit current query

The historical role and current-query role remain separate:

- an `objective-achievement@2` record stores its immutable inline result for its exact `evaluated_at`, evidence snapshot, input snapshot and rule versions;
- `derive_outcome_evidence_usability` reproduces that result when no query time is supplied;
- the same derivation may accept an explicit later query time and return a new view without mutating the historical record or its conclusion.

The derivation never consults current wall clock, latest rules or newly arrived evidence. Unavailable historical evidence or rule versions fail closed as `freshness_state: indeterminate` plus an ambiguity finding. A later query that classifies the evidence as stale does not invalidate or rewrite the historical assessment.

## 14. Executable evidence and AD-012 §23 coverage

The reference checker is evidence for the contract, not an independent normative authority. The activation maps every applicable AD-012 §23 pressure as follows:

| Pressure | Executable evidence or governed disposition |
|---|---|
| 1 | One test classifies the same exact evidence as stale or fresh under two exact criterion-local rules; no global evidence flag exists. |
| 2, 7, 9 | A later explicit query becomes stale while the stored historical result remains fresh and unchanged. |
| 3, 4 | A test proves that recent `recorded_at` cannot replace rule-selected `observed_at`. |
| 5 | Future-dated evidence derives temporal ambiguity; timezone-less activated record time is rejected. |
| 6 | The exact inclusive equality case is fresh and repeatable. |
| 8, 10 | Unknown rule versions, unavailable historical evidence and input-snapshot/rule mismatch fail closed. |
| 11 | A stale fixture remains historically present and can conclude only `indeterminate`; stale never means false. |
| 12 | The accepted forbidden-coupling checks and this authority boundary prevent freshness from becoming Result, lifecycle success, Capability, Readiness or authorization. |
| 13, 14 | Semantic uncertainty stays attributable, while different exact criterion contexts remain independently valid. |
| 15, 16 | Existing conflicting-evidence and branching-head fixtures preserve all candidates and never select by recency, count or order. |
| 17 | F3/A3 domain profiles were not selected; no domain label or compatibility fallback is accepted by this activation. |
| 18 | Removing an exact historical evidence input makes derived replay indeterminate and ambiguous. |
| 19 | AD-012B rejected a separate usability record; OCP-011 adds no record family or second P-001 invocation. |
| 20 | `objective-achievement@1` carrying activation fields and any unknown assessment-kind version are rejected. |

Fixtures also reject a declared inline state that disagrees with derivation, a rule bound to a different criterion, and a snapshot that names different rule inputs. The full fixture suite remains order-independent and contains no sensitive operational data.

## 15. OCP-011A amendment and accepted effect

Revision `0.3.0` defines the OCP-011 activation submitted through the separate review required by AD-012B §26.5. Its accepted effect:

1. activates F1/A1 only for exact `objective-achievement@2`;
2. preserves F0/A0 for `objective-achievement@1` and every other unactivated consumer;
3. preserves the inline historical and explicit derived-query roles without adding a standing property to Event or ObservationRecord;
4. resolves AB-039 after the first complete contract-local activation with executable evidence;
5. leaves OCP-012 and every other consumer unchanged until its own reviewed activation; and
6. retains OCP-011 as a non-Concept P-001 Module C record contract with no new Pattern invocation or Concept graph edge.

This amendment does not create a Concept, Pattern, record family, domain profile, universal duration, time ontology or semantic-comparison engine. It does not define source reliability, evidence truth, availability, Readiness, Capability possession, authorization, admissibility, Resource identity or interchangeability. Newest timestamp, record order, issuer/evaluator/source count and caller identity remain forbidden authority rules.

The amendment takes effect only through squash merge after exact-head external approval, Codex adjudication, green CI and explicit Architecture Board authorization.
