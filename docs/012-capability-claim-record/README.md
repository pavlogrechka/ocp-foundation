---
Document-ID: OCP-012
Title: Capability Claim Record Contract
Version: 0.3.0
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-003, OCP-009, AD-007, AD-013, P-001
Uses-Patterns: P-001@0.1.0
Used-By: AB-011, Resource Matching, Coordination, Audit
Last-Review: 2026-08-05
Review-After: First implementation-facing holder-capability@2 consumer or AD-013 reopening evidence
---

# OCP-012 — Capability Claim Record Contract

## 1. Authority and incorporated contract body

Revision `0.2.0` established the governed implementation of Outcome B from AD-007C. Revision `0.3.0` preserves that record contract and activates the OCP-012-local F1/A1 boundary selected by AD-013B for exact claim kind `holder-capability@2`.

The complete externally reviewed contract body is preserved verbatim in [`reviewed-contract-v0.1.0.md`](reviewed-contract-v0.1.0.md). Sections 1–15 of that immutable review artifact are incorporated into this Accepted specification without semantic alteration as the baseline for `holder-capability@1`. Its frontmatter and §16 preserve the pre-acceptance Draft state as historical review evidence only.

Revision `0.3.0` §§7–14 are a later normative amendment. They are authoritative for `holder-capability@2`, while the annex's attributable F0/A0 trust boundary remains authoritative for `holder-capability@1`. Where the annex differs from this README on lifecycle, the activated claim kind, evidence expectation, F1/A1 rules or forward mode transition, this README is authoritative.

This publication split does not change the reviewed claim semantics, checker contract or ontology boundary. CapabilityClaimRecord remains a governed identified-record contract, not a fundamental Concept.

## 2. Accepted normative baseline

The accepted contract defines one narrowly attributable claim by one claimant about one exact Resource and one exact OCP-009 Capability version under an exact condition set and stated temporal applicability.

The record is authoritative only for the attribution that the claimant made the claim under the recorded authority and provenance. It does not establish objective truth, independent verification, Readiness, availability, authorization, admissibility, Assignment eligibility, Operation success or Resource interchangeability.

The baseline retains:

- exact Resource, Capability-version, claimant, claim-kind, condition-set, authority and provenance bindings;
- `P-001@0.1.0` Modules A and C for half-open temporal applicability and history-preserving supersession;
- immutable evidence snapshots and fail-safe support handling;
- withdrawal distinct from negative polarity;
- visible branching without newest, storage-order, claimant-count or source-count precedence;
- a fail-safe attributable claim-head projection;
- Resource-only initial holders and explicit rejection of Organization holders;
- separate Resource identities even when their applicable claims match.

## 3. Executable conformance

The normative checker manifest, derivations and fixtures introduced with revision `0.1.0` remain executable evidence for the accepted baseline. Revision `0.3.0` adds the explicit `@1/@2` boundary, disjoint support modes, forward-only mode transition, exact local rules, historical replay and fail-safe current-query evidence described in §§7–13.

The checker remains a reference validator. Acceptance does not create a production wire schema, persistence API, trust engine, assessment contract or condition-expression language.

## 4. Boundary with assessment and AB-011

CapabilityClaimRecord records an attributable declaration. It does not become a Capability assessment or silently extend OCP-011. A future independently assessed Capability path still requires its own reviewed decision under AD-007C §24.3.

AB-011 may consume only the accepted fail-safe projection of applicable claim heads. Missing, stale, ambiguous, conflicting, unresolved or otherwise invalid inputs cannot yield an authoritative positive input by default. AB-011 must decide contextual Resource interchangeability separately and may not collapse Resource identity.

## 5. External review evidence

External adversarial review examined the semantic contract and executable evidence on exact head `7eb7dd60e5bb4991478694559b8a5511239b100f`. Fable approved that head at iteration 2 of 5, CI was green on the same head, and the reviewed Draft was squash-merged in PR #44 as `ec285c4c0393914717781952a5929c94e9a84a7d`.

The revision `0.2.0` acceptance act changed lifecycle and governance projections only; it did not alter the reviewed body or executable contract. Revision `0.3.0` is the separate activation required by AD-013B and therefore changes checker rules, derivations, manifest and fixtures. Its new exact head requires its own external review and authorization gates under §14.

## 6. Initial Architecture Board decision

On 2026-08-04, Architecture Board accepts OCP-012 revision `0.2.0` and decides:

1. accept CapabilityClaimRecord as the governed holder-specific claim contract selected by AD-007C Outcome B;
2. retain its authority as a narrow attributable declaration, not objective truth or independent assessment;
3. retain exact bindings, P-001 Modules A/C, withdrawal semantics, visible branching and fail-safe projection;
4. preserve Resource-only initial holders and every accepted non-equivalence boundary;
5. resolve AB-057;
6. keep AB-011 Planned as the next normative cycle and prohibit claim equality from implying Resource equality or automatic substitution;
7. preserve eight Accepted fundamental Concepts because CapabilityClaimRecord remains a non-Concept record contract.

## 7. AD-013B activation boundary

Revision `0.3.0` adds one bounded authority without rewriting the accepted `holder-capability@1` history:

| `claim_kind_ref` | Support authority | Required behavior |
|---|---|---|
| `holder-capability@1` | F0/A0 attributable baseline | Existing shape and support vocabulary remain valid; every activation field is forbidden. |
| `holder-capability@2` + `declaration-only` | narrow claimant declaration | External evidence and every evidence-rule field are forbidden; a non-withdrawn record uses `support_state: declared`. |
| `holder-capability@2` + `evidence-backed` | OCP-012-local F1/A1 for its source projection | Exact rules, immutable evidence/rule-input snapshots, explicit evaluation time and inline classifications are mandatory. |
| any other kind or mode | no authority | Reject; an unknown version, missing mode or mixed shape cannot bypass the boundary. |

The protected use is exactly `capability-claim-source-projection@1`: whether the bound external evidence is usable for OCP-012's own attributable projection under one exact local rule. The classification is not Capability truth, independent verification, Readiness, availability, authorization, admissibility, selection or Resource interchangeability. A downstream consumer cannot reuse it as that consumer's own freshness conclusion merely because the labels match.

The two `@2` modes are explicit and mutually exclusive. Mode is never inferred from evidence count, support-state label, field presence, timestamp or record order. Evidence-backed mode with an empty evidence snapshot is `missing`; it is not silently converted to declaration-only. Declaration-only freshness is semantically not applicable and is therefore not stored as a freshness classification.

Withdrawal remains assertion semantics. An `@2` withdrawal preserves its predecessor's support mode, carries no external evidence or activation classification, uses `support_state: declared`, and cannot mean negative, stale or mode downgrade.

## 8. Forward-only mode transition

Within one `holder-capability@2` P-001 Module C lineage, an explicit successor may change mode only from `declaration-only` to `evidence-backed`. That edge must preserve:

```text
claim_kind_ref
holder_kind_ref and holder_ref
exact OCP-009 Capability namespace, id and version
claimant_ref
condition_set_ref
assertion
```

The evidence-backed successor supplies the complete rule, snapshot, evaluation, authority and provenance contract. The predecessor remains exact-resolvable and historically declaration-only; the successor never upgrades or rewrites it. Combining the mode transition with an assertion-polarity correction is rejected.

`evidence-backed → declaration-only` is rejected because dropping evidence could bypass `missing`, `stale`, `ambiguous` or `conflicting` handling. Same-mode correction and explicit same-mode withdrawal remain ordinary Module C successors. Branches stay visible, and no newest timestamp, list order, claimant count, source count or issuer count selects a winner.

Crossing `holder-capability@1 → @2` is not a correction edge. Claim kind remains part of binding identity, so historical `@1` records retain their original F0/A0 authority.

## 9. Contract-local freshness rule

An activated freshness rule has this governed shape:

```text
rule_ref
protected_use_ref: capability-claim-source-projection@1
protected_claim_kind_ref: holder-capability@2
protected_support_mode: evidence-backed
condition_set_ref
evaluation_time_source: support_evaluated_at
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

The initial evidence envelope admits only these exact temporal facts when the selected rule names them:

| Evidence kind | Exact temporal fact | Record field read |
|---|---|---|
| `event@1` | `event-occurred-at@1` | `occurred_at` |
| `observation-record@1` | `observation-observed-at@1` | `observed_at` |
| `outcome-assessment-record@1` | `assessment-evaluated-at@1` | `evaluated_at` |

For one exact expectation, the freshness rule must define exactly one policy for every admitted evidence kind. A partial rule is invalid even when the current snapshot happens not to contain the omitted kind.

The rule never substitutes evidence recording time, claim `recorded_at`, claim effectivity, arrival order, current wall clock or OCP-011's own freshness result. `support_evaluated_at` and claim `recorded_at` must be offset-aware and comparable, with support evaluation no later than recording. A current query supplies a separate explicit offset-aware time.

Age is `support evaluation time - selected temporal fact`. Inclusive equality is fresh; exclusive equality is stale. The checker preserves parsed microseconds and accepts only finite non-negative integer durations. Missing, future-dated, timezone-less, unresolved or otherwise incomparable required input derives `indeterminate` and a non-permissive ambiguity finding. An empty evidence set derives `not_applicable` freshness while the composed support state remains `missing`.

The non-sensitive reference rule `holder-capability-freshness.field-context@1` protects exact `field-context@1` and uses inclusive cutoffs of 3600 seconds for Event occurrence, 600 seconds for Observation time and 1800 seconds for OutcomeAssessment evaluation. These are inputs of that exact reference contract only—not platform defaults, recommended production lifetimes or inherited consumer rules.

## 10. Contract-local ambiguity rule

The initial A1 rule `holder-capability-ambiguity.field-context@1` protects the same exact source use, claim kind, mode and condition set. It names two machine-verifiable dimensions:

- `reference@1` — an exact rule, snapshot, evidence item or activation input has zero or multiple resolutions;
- `temporal@1` — the explicit evaluation/query time or selected evidence time is missing, future-dated, timezone-less or incomparable.

The finite rule-derived reasons are:

| Dimension | Reason |
|---|---|
| `reference@1` | `activation-input-unresolved@1` |
| `temporal@1` | `evaluation-time-incomparable@1` |
| `temporal@1` | `temporal-fact-missing@1` |
| `temporal@1` | `temporal-fact-future@1` |
| `temporal@1` | `temporal-fact-incomparable@1` |

Every machine finding uses `basis: rule-derived`. `semantic-classification@1` remains attributable: relevance, source reliability, condition equivalence and whether evidence substantively supports the Capability proposition are not inferred by this rule. Any attributable semantic finding is non-permissive.

`ambiguity_state` is `clear` only when the exact rule derives no finding and no admissible attributable finding is recorded. Otherwise it is `ambiguous`. The finite ObservationRecord disagreement probe composes as `conflicting`; it is not a general semantic-equivalence engine or a vote.

## 11. Immutable activation inputs and support composition

Evidence-backed mode exact-binds a governed expectation before it classifies the resolved evidence. The initial non-sensitive expectation has this form:

```text
expectation_ref: holder-capability-evidence.field-context@1
protected_use_ref: capability-claim-source-projection@1
protected_claim_kind_ref: holder-capability@2
protected_support_mode: evidence-backed
condition_set_ref: field-context@1
admitted_evidence_kinds:
  - event@1
  - observation-record@1
  - outcome-assessment-record@1
minimum_evidence_count: 1
```

This means that one or more exact records from the admitted envelope are expected as the external support basis. It does not say that any such record is relevant, reliable or true. An empty exact snapshot therefore composes as `missing`; a bound kind outside the expectation is invalid rather than silently ignored.

Every evidence-backed non-withdrawn record exact-binds:

```text
evidence_expectation_ref
evidence_snapshot_ref
input_snapshot_ref
freshness_rule_ref
freshness_state
ambiguity_rule_ref
ambiguity_state
ambiguity_findings[]
support_evaluated_at
```

The evidence snapshot exact-matches the normalized evidence bindings, including an explicitly empty set. Every bound Event, ObservationRecord or OutcomeAssessmentRecord has exactly one valid resolution under its own governed contract; a malformed or duplicated record is unresolved for activation purposes. The immutable input snapshot exact-binds `capability-claim-source-projection@1`, `holder-capability@2`, `evidence-backed`, the same evidence expectation, `condition_set_ref` and exact freshness and ambiguity rule versions. Missing, duplicated or mismatched historical inputs never fall back to a latest rule, repository state or caller default.

The checker replays the inline classification and enforces this precedence:

| Condition | Required `support_state` |
|---|---|
| no evidence bindings | `missing` |
| finite actual ObservationRecord disagreement | `conflicting` |
| one or more ambiguity findings | `ambiguous` |
| clear but beyond a governed cutoff | `stale` |
| clear and within every governed cutoff | `sufficient` |

`sufficient` means only that the exact temporal and ambiguity guards did not force a narrower state. It does not verify Capability possession or make the claimant, evidence or assertion true. `effective_capability_claim` may project an activated evidence-backed assertion only when the complete exact Resource, Capability, evidence, snapshot and rule context validates. Record shape alone returns `indeterminate`.

## 12. Historical replay and explicit current query

The historical and current-query roles remain separate:

- an evidence-backed record stores its exact inline result for its `support_evaluated_at`, snapshots and rule versions;
- `derive_capability_claim_support_usability` reproduces that historical result without consulting wall clock or current repository state;
- the same derivation accepts a later explicit query time and returns a new view without mutating the record, support state, assertion or effectivity.

Unavailable historical evidence, duplicate identities, unknown rule versions or missing snapshots fail closed as `freshness_state: indeterminate` with an ambiguity finding. A later stale view does not rewrite a historically fresh record. It also does not automatically expire the claim or authorize a downstream decision.

## 13. Executable evidence and AD-013 coverage

The reference implementation maps every applicable AD-013 §13 pressure without borrowing authority from a downstream layer:

| Pressure | Executable evidence or governed disposition |
|---|---|
| 1–3 | Explicit `support_evaluated_at` stays separate from `recorded_at`, effectivity and later query time; replay never recomputes history implicitly. |
| 4, 6 | The result is exact-bound to OCP-012's source use, remains attributable and is not portable as truth or a consumer-local conclusion. |
| 5 | Declaration-only records forbid evidence-rule fields; evidence-backed empty sets remain `missing`. |
| 7 | OutcomeAssessment `evaluated_at` is a separately measured input fact; OCP-011 freshness is not inherited. |
| 8, 21 | Exact OCP-009 Capability version and historical `condition_set_ref` remain binding across lineage and query. |
| 9, 10, 19 | Exact old rules, evidence, snapshots and input snapshots replay deterministically; unavailable or duplicate inputs fail closed. |
| 11 | Future-dated evidence derives temporal ambiguity; timezone-less activated record time is rejected. |
| 12 | Inclusive equality is fresh at microsecond precision; a different exact rule may classify the same evidence differently. |
| 13, 15 | Branches remain visible in either list order; recency and counts never choose authority. |
| 14 | Only explicit same-assertion `declaration-only → evidence-backed` is accepted; reverse or polarity-changing transitions reject. |
| 16 | Matching or sufficient claims do not establish Resource equality, availability, authorization, selection or interchangeability. |
| 17 | `holder-capability@2` remains Resource-only; Organization holders still reject. |
| 18 | Withdrawal preserves mode and remains distinct from negative, stale or missing. |
| 20 | `holder-capability@1` with activation fields and unknown claim-kind versions reject. |

The suite includes 100 non-sensitive fixtures and 129 unit tests across the complete checker. Capability-claim-specific tests cover disjoint modes, missing evidence, exact cutoff equality, later-query staleness, every admitted temporal-fact kind, snapshot/rule mismatch, unavailable historical inputs, forward/reverse transition, polarity changes, withdrawal, branching and finite disagreement.

## 14. OCP-012A amendment and accepted effect

Revision `0.3.0` implements the separate activation required by AD-013B. Its accepted effect:

1. activates F1/A1 only for exact `holder-capability@2` evidence-backed mode and the exact OCP-012 source use;
2. preserves F0/A0 for `holder-capability@1` and narrow attribution for `@2` declaration-only mode;
3. accepts the reviewed same-kind `declaration-only → evidence-backed` transition while forbidding reverse and polarity-changing transitions;
4. preserves historical inline and explicit-time derived roles without creating a standing freshness property on Capability, Resource or evidence records;
5. resolves AB-060 after the complete activation is reviewed, approved, owner-authorized and squash-merged; and
6. retains OCP-012 as a non-Concept P-001 Modules A/C record contract with no new Pattern invocation or Concept graph edge.

This amendment does not create a Concept, Pattern, record family, universal duration, source trust score, semantic-equivalence engine or Organization claim. It does not change OCP-009 Capability definitions, OCP-011 assessment authority, OCP-013 eligibility authority, Resource identity, Assignment identity or the eight Accepted Concepts. `Capability ≠ Readiness` remains binding.

Newest timestamp, record order, claimant/source/issuer count, majority, caller identity and current wall clock remain forbidden authority rules. The amendment takes effect only through squash merge after exact-head external approval, Codex adjudication, green CI and explicit Architecture Board authorization.
