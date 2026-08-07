# Foundation Roadmap

## Progress Estimate

Оцінка є не-нормативною управлінською метрикою. Вона показує готовність foundation-репозиторію до переходу від онтологічного каркаса до машинозчитуваних правил і реалізації.

| Напрям | Орієнтовна готовність | Коментар |
|---|---:|---|
| Engineering and governance foundation | 100% | Репозиторій, taxonomy, decision/review process, versioning, Ruleset, required checker і post-factum history audit діють |
| Core domain ontology | 87% | Capability, Objective, Resource та Organization є Canonical; чотири інші Concepts і governed OCP-012–OCP-015 contracts лишаються Accepted, а їхні candidate-local blockers/gates не змінюються за implication |
| Operational rules and workflows | 19% | Є participation, admissibility, lifecycle projection, explicit-intent validation, assessment, interchangeability, Coordination consumer profile та proposal-response evidence workflow; AD-010 зберігає visibility та agreement як no-new-authority controls, а authorization, reservation і conflict models не завершені |
| Machine-readable schemas and enforcement | 72% | Local spatial profile/snapshot resolution і immutable transition evidence додані до checker; production contracts, geometry evaluator і semantic duplicate analysis відсутні |
| **Загальна foundation-готовність** | **≈71%** | Четвертий T4 micro-wave встановлює OCP-007/Organization `1.0.0 / Canonical` exact nine-file O9C unit; наступний remaining-T4 reassessment і будь-який downstream act мають окремі gates |

Відсоток не означає готовність production-системи. Репозиторій формує специфікаційний фундамент і reference validation layer, а не програмну реалізацію платформи.

## Milestone 0 — Engineering Foundation

- [x] Repository initialized
- [x] Branch and PR governance adopted
- [x] Operational Ontology draft
- [x] Ontology Governance draft
- [x] Concept Taxonomy draft
- [x] ADR registry and ADR-000…ADR-006
- [x] ADR-DRAFT-007
- [x] Active AD discovery/decision registry
- [x] Architecture Board review process established
- [x] Initial foundation merged after approval
- [x] GitHub Ruleset mechanically enforces PR-only, required checker and linear/squash history
- [x] Post-factum Git history audit with governed legacy baseline

## Milestone 1 — Core Domain Foundation

- [x] Resource `1.0.0 / Canonical` bounded identity contract with explicit exclusions and non-governed classification catalog
- [x] Operation Accepted working description
- [x] Assignment Accepted working description
- [x] Constraint Accepted working description
- [x] Organization `1.0.0 / Canonical` bounded Q2 identity and local relationship-record contract with explicit continuity/classification/mapping exclusions
- [x] Objective Accepted working description
- [x] State/Readiness mandate and final axis decision — `AD-002 / AD-011`; S0/R0 accepted, candidates deregistered, R1 remains a separately gated reopening path
- [x] Capability boundary and registry direction accepted in `AD-005C`
- [x] Capability Concept and governed registry contract accepted in `PR-0010 / OCP-009`
- [x] Event and Result boundary accepted in `AD-006C`: E3 occurrence + observation records, R3 governed assessment records
- [x] Event occurrence Concept and governed ObservationRecord contract — `AB-055 / OCP-010 / PR-0012`
- [x] OutcomeAssessmentRecord contract and Result registry resolution — `AB-056 / OCP-011 / PR-0013`
- [x] Holder-specific Capability Claim boundary accepted in `AD-007C`: Outcome B, a single narrowly attributable CapabilityClaimRecord direction
- [x] Normative CapabilityClaimRecord contract with fail-safe claim-head projection — `AB-057 / OCP-012 / PR-0014A`
- [x] Resource interchangeability boundary and Model A direction accepted — `AB-011 / AD-008C`
- [x] Normative deterministic Resource interchangeability contract and executable evidence — `AB-011 / OCP-013 / PR #49`
- [x] Governed Coordination consumer profile — `AB-003 / OCP-014`
- [x] Operational Coordination workflow-evidence boundary — `AB-058 / AD-009 / OCP-015`
- [x] Evidence-based State/Readiness selection — `AB-007 / AD-011`; S0 and R0 no-new-authority controls
- [x] Operational Area and environment boundary — `OCP-004 0.8.0` implements AD-014B Outcome A, resolves `AB-008` and removes the temporary Operational Area registry marker without a new Concept or graph edge
- [x] Core Boundary specification — `OCP-001 1.0.0 / Canonical + OCP-016 1.0.0 / Canonical` implement AD-015B C3 with Routes F/C/E/D/I, an orthogonal Pattern form verdict and no machine admission authority
- [x] Objective editorial-correction boundary — `OCP-008 0.3.0` implements AD-017B A+D with immutable stored statements, display exclusion and exact historical consumer replay; `AB-063` Resolved without promotion
- [ ] Promote stable core descriptions to Canonical — `AB-062 / AD-016B 0.3.0` selects R4 (`F → C`) with L2, limits current preparation to T0–T3 and requires AD-016C reassessment plus AD-016D Board selection before T4; no promotion occurs in this act
- [x] T0 OCP-000 registry contract — `1.0.0 / Canonical` with independent Proposed rows, explicit authority boundaries and no implicit Concept/graph promotion
- [x] T1 OCP-016 routing contract — `1.0.0 / Canonical` with exact accepted-content anchors, stable F/C/E/D/I routes, orthogonal Pattern verdict and no machine admission layer
- [x] T2 OCP-001 governance contract — `1.0.0 / Canonical` with L2, R4/atomicity/non-transfer rules, human counterexamples and a structural direct-dependency witness
- [x] T3 OCP-002 Concept-status projection — `1.0.0 / Canonical` with exact defined-Concept set/value synchronization and explicitly non-normative category views
- [x] T3 P-001 identified-record Pattern — `0.1.0 / Accepted` at the unchanged §§1–10 surface, with six exact primary invokers, explicit reviewed-snapshot treatment and no transfer to T4
- [x] AD-016C post-enabling reassessment — exact T4–T10 inventory and B/S/C recompute, with G2/OCP-009-first as a recommendation only and AD-016D still mandatory
- [x] AD-016D post-enabling Board selection — G2 inside C/L2, with preparation scope limited to one separately reviewed OCP-009 T4 draft and no merge-authorization transfer
- [x] First T4 micro-wave — OCP-009/Capability `1.0.0 / Canonical`, atomic OCP-000/OCP-002 `1.1.0` projections, exact definition-version independence and non-redirecting supersession
- [x] AD-016F Objective readiness reassessment — fresh B/S/C audit on exact post-OCP-008A evidence finds no current B item, bounds S/C and records K8 only as the leading hypothesis before mandatory AD-016G
- [x] AD-016G Objective scope selection — K8 selected for preparation of one separately reviewed OCP-008/Objective lifecycle draft with atomic projections, bounded OCP-004 cleanup and no merge-authorization transfer
- [x] AD-016H K8 preflight repair selection — lifecycle authoring stopped on two stale Capability status views; Q1 selects a separate OCP-003/OCP-004 correction before recomputed K8 work
- [x] AD-016H Q1 preflight correction — OCP-003 `0.6.1` and OCP-004 `0.8.1` correct only the two stale Capability status views; Resource/Operation semantics, dependencies and Concept statuses remain unchanged
- [x] Second T4 micro-wave — OCP-008/Objective `1.0.0 / Canonical`, atomic OCP-000/OCP-002 `1.2.0` projections and bounded OCP-004 `0.8.2` status rendering, with exact historical consumer replay and no achievement authority
- [x] AD-016I post-Objective reassessment — OCP-003/OCP-007 remain blocked; M0 stays fail-safe and M3 Resource stable-surface discovery is only a leading hypothesis before mandatory AD-016J selection
- [x] AD-016J remaining-T4 scope selection — M3 authorizes preparation of one separate AD-018 Resource stable-surface discovery; it selects no semantic outcome and changes no OCP, Concept status or backlog resolution
- [x] AD-018 Resource stable-surface discovery — exact consumer/fixture audit and outcome-fair R0/RI/RE/RS/RX comparison; RS is a leading hypothesis only and R0 remains fail-safe
- [x] AD-018A Resource stable-surface selection — RS authorizes preparation of one OCP-003 `0.7.0 / Draft` remediation; no OCP edit, Concept status change, mapping decision or lifecycle authority occurs in the selection act
- [x] OCP-003 `0.7.0 / Draft` Resource stable-kernel remediation — one normative kernel, explicit deferred boundary, non-governed opaque classification catalog and two bounded fixtures; Resource remains Accepted and consumers/checker stay unchanged
- [x] AD-016K post-Resource-remediation audit — no current semantic B-item is demonstrated inside the bounded kernel; N3 ten-file lifecycle preparation leads only as a recommendation before separate AD-016L selection
- [x] AD-016L Resource lifecycle scope selection — N3 authorizes preparation of one exact ten-file proposal with OCP-002 prose sync and three PATCH-only consumer views; selection itself changes no lifecycle state
- [x] Third T4 micro-wave — OCP-003/Resource `1.0.0 / Canonical`, atomic OCP-000/OCP-002 `1.3.0` projections and PATCH-only OCP-004/005/006 Resource status views, with no semantic consumer change, migration or excluded-surface authority
- [x] AD-016M post-Resource reassessment — OCP-007 is the sole remaining-T4 candidate; continuity, classification, class/type and scheme/exception authority remain blocked, O7D leads only as a discovery hypothesis before separate AD-016N selection
- [x] AD-016N Organization discovery scope selection — O7D authorizes preparation of one outcome-fair AD-019 discovery across independent identity, classification, relationship-kind, scheme/exception, composition and mapping axes; no semantic outcome, OCP edit or topology change is selected
- [x] AD-019 Organization stable-surface discovery — H0–H4 authority layouts and independent C/K/T/S/E/Y/R/U/M treatments are compared; Q2 is a leading hypothesis only and H0 remains fail-safe before separate AD-019A selection
- [x] AD-019A Organization stable-surface selection — Q2 authorizes preparation of one bounded OCP-007 `0.4.0 / Draft` remediation with one owner, two readable surfaces and exact C2/K3/T2/S1/E1/Y1/R1/U0/M0 boundaries; no OCP/checker/fixture or lifecycle change occurs in the selection act
- [x] OCP-007 Q2 remediation — `0.4.0 / Draft` separates readable identity/lifecycle and local relationship-record surfaces, adds exact external kind-profile/dataset resolution and finite seventeen-group evidence; lifecycle remains separately gated
- [x] AD-016O post-Organization-remediation audit — no current semantic B-item is demonstrated inside the bounded Q2 promise; O7C seven-file lifecycle preparation leads only as a recommendation before mandatory AD-016P selection
- [x] AD-016P Organization lifecycle scope selection — fifteen commissioned targets close negatively but target 12 finds a live eighth checker-guide projection; O0 hold is selected, exact seven-file O7C is not expanded by implication, and no lifecycle, backlog-status or topology proposal is authorized
- [x] AD-016Q complete Organization lifecycle-projection audit — a rule-based exact-baseline sweep classifies eight projection-bearing/current-roadmap files plus AB-062 accounting as evidence-only candidate U9, records stale OCP-005 §4 `Organization: Proposed` for a separate repair act, and leaves O0 binding with no outcome or proposal authorized
- [x] AD-016R peer status synchronization selection — rule-based audit finds six stale registered-Concept views across OCP-005/OCP-006; O7V authorizes preparation only of one separate synchronization-and-guardrail PATCH, O0 remains binding for Organization lifecycle, and implementation plus post-repair comparison require fresh exact-head gates
- [x] O7V peer status synchronization implementation — OCP-005/OCP-006 `0.2.4 / Draft` synchronize all six demonstrated rows; bounded repository validation rejects mismatched or duplicate registered-Concept rows without becoming lifecycle authority; O0 remains binding
- [x] AD-016S post-O7V Organization audit — 172 tests and 120 fixtures replay green, all governed peer rows are synchronized, a fresh rule-based sweep derives exact nine-file O9C without a demonstrated tenth projection, and O9C remains recommendation-only before AD-016T
- [x] AD-016T Organization lifecycle scope selection — independent projection/consumer/non-Markdown sweep and all sixteen targets support O9C only as preparation of one exact nine-file proposal with explicit SemVer/status atomicity; no lifecycle state changes in the selection act
- [x] Fourth T4 micro-wave — OCP-007/Organization `1.0.0 / Canonical`, atomic OCP-000/OCP-002 `1.4.0`, OCP-005 `0.2.5`, current map/checker-guide/accounting synchronization and no semantic, migration, mapping or T5 authority
- [x] AD-016U post-O9C frontier reassessment — T4 is complete; OCP-004 retains lifecycle/composition blockers, bounded OCP-012 has no demonstrated B item, and P12 is recommendation-only before a separate AD-016V Board selection

## Milestone 1A — Governed Executable Validation Loop

- [x] `PR-0006 — Add Executable Ontology Checker`
- [x] YAML fixtures for Resource, Operation, Assignment and Constraint
- [x] Valid and invalid lifecycle fixtures for the initial reference subset
- [x] Regression fixtures for silent Assignment termination, contradictory `not_applicable` and stale Constraint versions
- [x] Reference checks for optional materialized projections and authoritative transition histories
- [x] Exact Constraint version and input snapshot selection independent of YAML record order
- [x] Complete provenance manifest for emitted validation codes and derivations
- [x] Meta-test enforcing exact manifest completeness
- [x] Reference derivations:
  - `assignment_effective_at`
  - `derived_participates_in`
  - `constraint_effective_at`
  - `constraint_applicable_to`
  - `effective_constraint_result`
  - `constraint_blocks`
  - `constraint_set_decision`
- [x] Cross-document Concept status synchronization check
- [x] Defining-document Concept dependency graph, phantom-reference and cycle checks
- [x] Generated Foundation map and CI drift detection
- [x] OCP-004 exact-binding explicit-intent evidence and fail-safe projection fixtures
- [x] Artifact ID and taxonomy-status checks
- [x] Duplicate AB and accepted AD↔AB synchronization checks
- [x] Pattern semver and `Uses-Patterns` `track-current` checks
- [x] Full-history checkout and post-baseline non-linear-history audit
- [x] PR CI validates the actual proposed head in explicit `main` context
- [x] OCP-009 Capability exact-resolution, namespace, supersession and registry≠possession evidence
- [x] OCP-010 Event identity, ObservationRecord, exact references, supersession and zero-observation evidence
- [x] First integrated non-sensitive scenario with `derived_participates_in`, `constraint_applicable_to` and `effective_constraint_result`
- [x] OCP-011 normative OutcomeAssessmentRecord evidence with exact snapshots, fail-safe states and branching supersession
- [x] Atomic removal of temporary `Result: Proposed` registry marker without creating a Result Concept
- [x] Draft OCP-012 CapabilityClaimRecord exact binding, temporal/supersession history and fail-safe projection fixtures
- [x] OCP-014 exact governed owner binding and wrong-owner fail-safe fixture
- [x] OCP-015 proposal/response exact binding, history-preserving withdrawal, fail-safe projection and symmetric reference-normalization evidence
- [x] First machine-verifiable evidence freshness, ambiguity and deterministic replay activation — `OCP-011 0.3.0` activates F1+A1 for exact `objective-achievement@2`; `AB-039` is Resolved while unactivated consumers remain under F0/A0
- [x] Capability Claim support-usability activation — `OCP-012 0.3.0` implements the AD-013B unified `holder-capability@2` boundary, reviewed `declaration-only → evidence-backed` transition, exact source-use F1/A1 rules and replay evidence; `AB-060` is Resolved
- [x] Global primary-artifact identity uniqueness across OCP, Pattern, AD, ADR and AB registries
- [x] Structured normative-rule and reference-integrity linter for exact `Depends-On`, global manifest rule IDs and resolvable OCP sources
- [x] OCP-004 Operation-local spatial binding with exact profile/snapshot resolution, immutable transition evidence and fail-safe non-implication fixtures
- [x] OCP-008 strict statement immutability with duplicate-ID rejection, visible correction branching and prior Operation/assessment replay
- [ ] Production validator, persistence and implementation-facing contracts

The checker is a reference validation layer, not production implementation. OCP documents, accepted decisions and machine-readable taxonomy remain authoritative. Semantic equivalence or duplication in natural-language normative text remains an external-review obligation; expression language, persistence model and production evaluator remain separate decisions.

## Milestone 2 — Operational Rules

- [ ] Constraint pattern library
- [ ] Assignment conflict, exclusivity and capacity rules
- [ ] Business Rules specification
- [ ] Operation Lifecycle completion
- [ ] Assignment / Operation lifecycle coordination
- [x] Coordination proposal-response evidence workflow — `OCP-015`
- [x] Cross-vertical visibility/agreement boundary — `AD-010` selects independent V0/A0 no-new-authority controls
- [ ] Visibility, authorization and approval model
- [ ] Reservation and Allocation decision
- [ ] Conflict and remediation model

## Milestone 3 — Machine-Readable Foundation Expansion

- [ ] Machine-readable Concept registry beyond the current status projection
- [ ] Machine-readable invariants and derivation rules beyond the current reference slice
- [x] Structured ontology identity/reference linter for primary artifacts, dependency metadata and rule manifests
- [ ] Semantic duplicate analysis across natural-language normative text (external review; no machine-completeness claim)
- [ ] Constraint expression and evaluator contracts
- [x] First integrated non-sensitive scenario spanning Operation, Objective, Assignment, Constraint, Event, observations and assessments — accepted in PR-0012
- [x] Replace its temporary assessment envelope with Accepted OCP-011 OutcomeAssessmentRecord — PR-0013
- [ ] Additional example datasets without sensitive information
- [ ] Expanded CI checks for schemas, lifecycle consistency and normative references
- [ ] Versioned implementation-facing contracts

## Planned Sequence

1. Prepare a separate AD-016V exact-head Board selection over P0/P12/P4D/P4/P45/PR; AD-016U recommends P12 but authorizes no OCP-012 or OCP-004 edit.
2. Keep OCP-004 lifecycle/composition questions explicit B items and do not couple them to an otherwise bounded OCP-012 candidate through a combined T5 wave.
3. Preserve Resource-only CapabilityClaimRecord holders, exact OCP-009 Capability version binding, claim/assessment separation, `Capability ≠ Readiness` and fail-safe consumer-local evidence semantics.
4. Continue T5–T10 only through OCP-016 routing, OCP-001 L2/atomicity and separate exact-head review/Board gates; no authorization transfers from T4.
