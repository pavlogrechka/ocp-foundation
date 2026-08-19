# Foundation Roadmap

## Progress Estimate

Оцінка є не-нормативною управлінською метрикою. Вона показує готовність foundation-репозиторію до переходу від онтологічного каркаса до машинозчитуваних правил і реалізації.

| Напрям | Орієнтовна готовність | Коментар |
|---|---:|---|
| Engineering and governance foundation | 100% | Репозиторій, taxonomy, decision/review process, versioning, Ruleset, required checker і post-factum history audit діють |
| Core domain ontology | 93% | Capability, Objective, Resource, Organization, Operation та Event є Canonical; Assignment і Constraint лишаються Accepted, Event є Canonical, OCP-017 є Route C Accepted non-Concept, а candidate-local blockers/gates не змінюються за implication |
| Operational rules and workflows | 33% | Є participation, admissibility, explicit-intent validation, Accepted Q3I Operation lifecycle contract, assessment, interchangeability, Coordination workflow, Accepted OCP-018–OCP-024 positive/negative/partial bounded contracts, Route D OCP-023 occupancy та synthetic-only OCP-024 completeness-evidence recognition; AD-044 знаходить binding-level pressure на всі три semantic Assignment blockers, AD-045 не знаходить нормативного виключення серед шести survivors, AD-046 закриває лише Q3 prospective-effectivity boundary, а AD-047/AD-048 окремо доводять недостатність наявної підстави для закриття Q9/Q2; Q9 утримує temporal, Q2 — amendment whole-freeze blocker, real evaluator, production activation і positive models не завершені |
| Machine-readable schemas and enforcement | 77% | Checker додатково перевіряє exact quantitative inputs, exact-unit aggregation, separate E/Q Reservation/Allocation boundaries, three-question Order-authorization negative boundary, separate Constraint application-order/override/contextual-waiver boundaries, Accepted snapshot-bounded occupancy та synthetic-only completeness recognition; production occupancy completeness/activation, real evaluators, geometry evaluator і semantic duplicate analysis відсутні |
| **Загальна foundation-готовність** | **≈72%** | Event T6 завершено окремими discovery, reassessment, selection, promotion і Concept-canonicalization gates; T7–T10, known reference debt і кожен відкритий Operation backlog item зберігають окремі gates |

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
- [x] Operation `1.0.0 / Canonical` bounded identity/Q3I contract with Accepted Route C OCP-017 lifecycle owner
- [x] Assignment Accepted working description
- [x] Constraint Accepted working description
- [x] Constraint interaction boundaries — AD-027 separately selects AN, ON and WN; OCP-006 `0.3.1 / Draft` preserves complete-set permutation invariance and denies implicit override/contextual waiver without introducing a Concept or positive authority
- [x] Constraint bounded stable-surface discovery — AD-050 enumerates all twelve OCP-006 questions, keeps four resolved entries historical, isolates five bounded candidates/eight moving surfaces and identifies only Q6 evaluation-currentness as a whole-document blocker without editing OCP-006, selecting Constraint or opening T7
- [x] Constraint Q6 sufficiency check — AD-051 derives the full current OCP-006 dependency/Accepted-consumer neighborhood, separates direct norms from non-exhaustive lists and silence, proves local freshness rules do not establish a general lifetime, and keeps Q6 plus its sole whole-freeze blocker open without editing OCP-006 or opening T7
- [x] Constraint document-status norm discovery — AD-052 derives the actual Accepted/Canonical criteria from current OCP-001/OCP-016, separates AD-050 discovery vocabulary from norm, scans all 23 promoted OCP documents and shows that open questions are not a status bar; OCP-006 still needs a separate complete Accepted act and fails Canonical L2 on Draft OCP-005
- [x] Resolved-AB/open-question hygiene — AD-028 synchronizes twelve exact current mirrors for AB-025/036/037/056/059, preserves forty-six lawfully open prompts and mechanically rejects loss of any declared strikeout, Resolved status or exact disposition reference
- [x] Accepted-document evidence hygiene — AD-029 enforces one exact named and hashed reviewed-contract snapshot for every current Accepted OCP, retains OCP-016 acceptance evidence explicitly after Canonical promotion and inventories the wider eight-primary presentation debt without rewriting Canonical or incorporated bodies
- [x] Organization `1.1.1 / Canonical` bounded Q2 identity and local relationship-record contract with explicit continuity/classification/mapping exclusions, document-local post-`1.0.0` SemVer rules and resolvable current governance navigation
- [x] Objective Accepted working description
- [x] State/Readiness mandate and final axis decision — `AD-002 / AD-011`; S0/R0 accepted, candidates deregistered, R1 remains a separately gated reopening path
- [x] Capability boundary and registry direction accepted in `AD-005C`
- [x] Capability Concept and governed registry contract accepted in `PR-0010 / OCP-009`
- [x] Event and Result boundary accepted in `AD-006C`: E3 occurrence + observation records, R3 governed assessment records
- [x] Event occurrence Concept and governed ObservationRecord contract — `AB-055 / OCP-010 / PR-0012`
- [x] Event Concept canonicalization — `AD-032` proves stable live dependencies and machine-readable semantic coverage, preserves immutable prior-step witnesses and synchronously advances Event `Accepted → Canonical` without changing the OCP-010 semantic body or graph
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
- [x] OCP-007 post-canonical versioning correction — `1.1.0 / Canonical` adds local PATCH/MINOR/MAJOR boundaries for the unchanged §33.2 promise; Organization status, data, checker semantics, readiness and remaining-T4 authority do not change
- [x] AD-016U post-Organization remaining-frontier reassessment — a fresh rule-based sweep derives exactly Operation, Assignment, Constraint and Event, preserves strict T5/T6/T7 L2 order, audits exact P-001 and OCP-007 bridge obligations, and records U4D only as a recommendation before separate AD-016V selection
- [x] AD-016V remaining-frontier Board comparison — a fresh all-seventeen-OCP replay and independent adjudication of all twenty targets select U4D only for preparation of one separate outcome-fair AD-020 Operation stable-surface discovery; no OCP edit, semantic outcome or downstream merge is authorized
- [x] AD-020 Operation stable-surface discovery — H0–H4 layouts, ten semantic/authority axes and separate form verdicts for ExplicitIntentRecord, validation evidence, lifecycle transitions and inter-operation assertions are compared; Q3 is recommendation-only and H0 remains fail-safe before AD-020A
- [x] AD-020A Operation stable-surface Board selection — all thirty targets are re-attempted; target 22 defeats provisional Q3's unowned IO3/H3–H4 blend, and revised Q3I selects one OCP-004 kernel plus one downstream Route C lifecycle owner and inline IO2 only as remediation preparation
- [x] P-001 evidence-accounting correction — §§11/13 are time-anchored to the exact T3 acceptance baseline, the recurring live invoker count is removed without a Pattern version/form change, §16 stays historical, and structured `Uses-Patterns` remains the sole current invoker-set source
- [x] Bounded Q3I remediation — OCP-004 `0.9.0 / Draft` retains the stable Operation kernel, F1/V1 and inline IO2; new Route C OCP-017 `0.1.0 / Draft` owns G2/A1/T1 lifecycle and LT2 Module B in one atomic tree, with unchanged P-001 and no Concept/edge/backlog-status change
- [x] AD-016W post-Operation-remediation blocker/stability audit — OCP-004 and OCP-017 are classified independently; six-consumer D2/E1 topology, L2/Accepted-Pattern/Route C floors, eight metadata-derived P-001 invokers, all reopening gates, 30 scenarios, 32 rejection classes and 191/125 executable evidence replay without a current semantic B; WJ is recommendation-only before AD-016X
- [x] AD-016X Operation lifecycle-scope Board comparison — all twenty targets are independently re-adjudicated and W0/W4C/W17A/WJ/WR receive outcome-fair treatment; WJ is selected only as preparation of one exact joint proposal whose two artifacts retain separate readiness proof and fresh merge gates
- [x] Post-AD-016X governance hygiene PATCH — correct the two OCP-011 `0.3.0` anchor cells, the real foundation-map path and completed AD-002/018/019/020 review triggers; preserve AD-011 S0/R0 and change no semantic contract, lifecycle status, backlog status or readiness authority
- [x] T5 WJ joint lifecycle act — OCP-004/Operation `1.0.0 / Canonical` and Route C OCP-017 `0.2.0 / Accepted` in one exact twelve-file unit with separate compatibility/readiness/migration/rollback evidence, immutable OCP-017 Draft snapshot and unchanged P-001/rules/checker/tests/fixtures
- [x] Coordination workflow source-metadata PATCH — rederive all nine manifest owners from the incorporated OCP-015 snapshot, remove the two structurally dangling labels, synchronize the Accepted checker-guide view and defer repository-wide semantic-source enforcement without executable or normative change
- [x] Bare-integer section-reference hygiene PATCH — repair the sole current OCP-007 occurrence with a named-heading link, preserve and permanently register eight historical occurrences, record the honest `9 → 8` metric and prohibit new occurrences without machine enforcement or history rewriting
- [x] AD-016Y post-T5 frontier reassessment — rederive all eighteen current OCPs, replay L2/Pattern/route/consumer floors, register every `Review-After` value as 17 fulfilled / 12 open without repair and retain Y10D Event discovery only as a recommendation before a separately mandated Board comparison
- [x] AD-016Z post-T5 Board comparison — independently replay the two-candidate frontier and all twenty targets, resolve positive target 14 by correcting the repository-wide `Review-After` area/form inventory to 30 fields, and select Y10D only as a future separately mandated Event dependency/stable-surface discovery scope
- [x] AD-016AA T6/T7 promotion prerequisite gate — prove T0–T5 and AD-016C/D complete but candidate-scoped authority exhausted, rederive Assignment/Event L2 pass and Constraint L2 failure on Draft OCP-005, record absent Y10D/reassessment/selection gates and enforce the hold without an OCP or Concept status change
- [x] AD-031 Y10D Event dependency/stable-surface discovery — derive seven current inputs and two primary consumers from structured metadata, separate exact Pattern/record-kind bindings from unversioned document dependencies, classify five stable candidates and five moving surfaces, and pin four blockers without an OCP, Concept, edge, reassessment, Board selection or T6 change
- [x] AD-016AB post-Y10D reassessment — independently derive live L2 from current OCP metadata, compare hold/Assignment/Event/the justified Assignment+Constraint unit/Constraint remediation under one criterion, recommend current hold plus Event-YK remediation continuation without selection authority, and make reassessed/unselected versus fully gated states executable
- [x] AD-016AC candidate-specific Board selection — record exact OCP-010/Event as selected-but-Draft, bind compatibility/migration/rollback across both Accepted consumers and all three live blockers, repair historical witnesses to immutable baselines, and retain a separate Event lifecycle promotion act
- [x] AD-016AD Event lifecycle remediation and document promotion — prove all three selection preconditions independently, preserve AD-031/AD-016AC as baseline-bound history, complete the final gate and promote OCP-010 to `1.0.0 / Canonical` while Event remains `Accepted`
- [x] AD-032 Event Concept canonicalization — apply the separate OCP-001 lifecycle decision, prove empty Concept dependencies plus Canonical direct OCP floors and four executable semantic surfaces, preserve historical baseline witnesses and synchronize all current Event status carriers to `Canonical`
- [x] AD-033 multicycle promotion-gate infrastructure — replace the one-cycle schema with an append-only generic cycle journal, prove an entire later selection/document/Concept cycle reachable without code changes, retain skipped-step/L2 failure and leave no active next cycle
- [x] AD-035 Assignment bounded stable-surface discovery — derive two Concept dependencies and all six structured consumers from live metadata, classify all eleven OCP-005 questions, and pin six bounded candidates, seven moving surfaces and four blockers without selecting Assignment or starting a cycle
- [x] AD-036 positive consumer-need discovery — enumerate all 19 current Accepted/Canonical lifecycle artifacts plus 30 Accepted governance acts, apply one predeclared own-obligation test, distinguish established positive outputs from negative/deferred mentions, and mechanically preserve the empty unmet-positive-need result without activation or a new cycle
- [x] AD-037 negative-boundary acceptance — independently prove OCP-019/OCP-021/OCP-022 ready for Accepted status, preserve each `0.1.0` reviewed body byte-for-byte, move each primary to `0.2.0 / Accepted`, and extend the AD-029 snapshot guard without changing negative semantics or activating a positive model
- [x] AD-038 Assignment Q2 negative-closure attempt — falsify the supersession-only hypothesis against current OCP-005, all five live Accepted consumers and two executable field-change probes; keep Q2/AB-026 open because closure requires new positive immutability, successor-binding and provenance rules under G4
- [x] AD-039 Assignment temporal/partial-scope negative-closure attempts — isolate the existing pre-establishment effectivity boundary, reproduce accepted backdated-establishment, extra-interval and partial-scope probes, and keep Q3/Q9/Q5 plus both freeze blockers open because closure requires new positive rules under G4
- [x] AD-040 Assignment Accepted-consumer compatibility evidence — rederive five live Accepted consumers, replay four negative exclusions and OCP-017 positive terminal alignment on unchanged fixtures, remove only the compatibility-evidence blocker and retain all three semantic blockers without selecting Assignment or starting a cycle
- [x] AD-041 / OCP-023 Route D Resource occupancy — select one domain-local snapshot-bounded `occupied` derivation with complete Assignment witnesses, six synthetic executable cases and an explicit G4/non-activation stop; the missing Resource-wide Assignment-set completeness result is stated as a concrete need, while OCP-023 remains Draft and no promotion cycle starts
- [x] AD-042 / OCP-023 acceptance — independently prove the exact partial Route D contract ready for `0.2.0 / Accepted`, preserve its reviewed Draft body byte-for-byte, register its snapshot, and make the current unmet completeness need plus sixth Accepted Assignment consumer executable without activation or a promotion cycle
- [x] AD-043 / OCP-024 completeness-evaluator recognition — derive producer-independent subject/scope/time/provenance/authority/consistency properties as an executable Route D Draft envelope, while proving that repository-internal references cannot establish a real evaluator and activate nothing
- [x] AD-044 Assignment consumer-pressure discovery — exhaust all three whole-freeze blockers and ten resolution classes against the current OCP-023 need; classify all three `pressured` by missing observation-cut or part–whole closure bindings, without selecting or removing anything
- [x] AD-045 Assignment survivor norm-compatibility discovery — exhaust all six pressure survivors through a bounded 25-current-primary/64-hit lexical sweep plus three exact-guarded known out-of-vocabulary temporal deferrals; admit OCP-005's direct provisional boundaries without lifecycle promotion, exclude none, classify one `compatible` and five `underdetermined`, without semantic-completeness or lifecycle authority
- [x] AD-046 Assignment Q3 lifecycle resolution — finalize only the existing negative `established_at` effectivity lower bound, advance OCP-005 `0.2.8 → 0.3.0 / Draft`, strike only Q3 and keep Q9 plus `TEMPORAL_MODEL_UNRESOLVED` current without changing the pressure/survivor inventories or opening a promotion cycle
- [x] AD-047 Assignment Q9 sufficiency check — apply a predeclared Q3-level threshold, prove the singular minimum record shape is not a closed-world cardinality rule, accept a causal synthetic two-interval extension while rejecting a real scalar interval violation, and keep OCP-005 byte-identical with Q9 and its temporal blocker unchanged
- [x] AD-048 Assignment Q2 sufficiency check — classify direct norm, enumeration inference and silence separately; calibrate against Q3-pass/Q9-fail; prove executable behavior and all six Accepted consumers select neither surviving supersession/immutability class; keep OCP-005 byte-identical with Q2 and its amendment blocker unchanged
- [x] AD-049 / OCP-024 lifecycle acceptance — accept the exact synthetic-only recognition body as `0.2.0 / Accepted`, preserve its `0.1.0` reviewed snapshot, and mechanically prove that no real evaluator, completeness supply, G4 binding, activation or OCP-023 negative result follows

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
- [x] Operation Lifecycle foundation contract — OCP-017 `0.2.0 / Accepted`, with source-side evidence delegated to OCP-018 and broader stage/profile expansion and production implementation separately gated
- [ ] Assignment / Operation lifecycle coordination
- [x] Coordination proposal-response evidence workflow — `OCP-015`
- [x] Cross-vertical visibility/agreement boundary — `AD-010` selects independent V0/A0 no-new-authority controls
- [x] Operation authorization source model — AD-021 selects AC and OCP-018 `0.2.1 / Accepted` governs the Route C source/Organization/Capability/level/effectivity evidence contract with material negative fixtures, without resolving Order, legitimizing a production source or introducing Authority/Approval/Policy Concepts
- [x] Order authorization establishment boundary — AD-030 selects ON and OCP-022 `0.1.0 / Draft` makes mandatory, sufficient and admissible-source non-results separately executable while Order remains Proposed and every positive profile/Concept route requires fresh G4 and registry gates
- [x] Conflict derivation boundary — AD-022 selects H0-B and OCP-019 `0.1.0 / Draft` makes the negative Route C establishment boundary executable: exact ConstraintEvaluationRecord references are preserved, while one/many violations and incomplete, conflicting, stale or indeterminate inputs never permissively derive Conflict; positive activation remains separately gated by OCP-016 G4
- [x] Positive Conflict activation-gate audit — AD-023 inventories every Accepted-or-higher contract and finds no complete OCP-019 §9 / OCP-016 G4 consumer; seven synthetic gate probes make each missing group and a complete self-declared attempt derive only `indeterminate`, while OCP-019 remains byte-identical `0.1.0 / Draft`
- [x] Operation consumer-independence audit — AD-024 applies a reproducible seven-surface inventory before route selection and finds no concrete current consumer, protected handling decision or legitimate non-Board owner/evaluator; three synthetic self-supply probes preserve `indeterminate`, so no OCP-004 profile is prepared and the three-act minimum remains future work
- [x] Quantitative Constraint input direction and acceptance — AD-025 selects QC and OCP-020 `0.2.0 / Accepted` preserves the byte-identical reviewed Draft while governing exact profile/unit/snapshot bindings and exact-unit demand/consumed aggregation without capacity-sufficiency, availability, reservation or allocation authority; AB-037 is Resolved and only the input-status prerequisite for partial/quantitative reservation is removed
- [ ] Production source profiles and any broader approval semantics
- [x] Reservation and Allocation establishment boundary — AD-026 separately selects EN for whole-Resource exclusivity and QN for partial/quantitative use; OCP-021 `0.1.0 / Draft` makes both negative composition results executable without a Concept or positive authority, while any positive reopening remains branch-local and requires new Accepted-consumer, rule, owner/evaluator, object-form and OCP-016 G4 evidence
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

1. The completed T5 WJ act establishes OCP-004/Operation `1.0.0 / Canonical` and OCP-017 `0.2.0 / Accepted` without transferring authority to T6–T10; any next frontier needs its own fresh inventory, Board selection and exact-head gates.
2. The completed coordination source-metadata PATCH rederives all nine OCP-015 manifest owners and corrects the Accepted checker-guide view without changing executable or normative behavior.
3. The separately gated bare-integer hygiene PATCH repairs only current OCP-007 navigation, permanently registers eight historical occurrences and adds no machine enforcement. Completion of the four-step sequence grants no authority to T6–T10 or another post-T5 frontier.
4. AD-016Y independently derives Assignment and Event as the exact post-T5 L2-admissible frontier and records Y10D only as a recommendation; AD-016Z independently replays that frontier and all twenty targets, resolves the area/form inventory positive without field repair and selects Y10D only as a next-question scope.
5. AD-016AA proves that no candidate-specific promotion selection exists: Assignment and Event pass L2, Constraint fails on Draft OCP-005, and all three remain Draft behind an executable no-self-supply gate.
6. AD-031 completes only the separately mandated Y10D Event dependency/stable-surface discovery: the bounded in-place kernel is a leading candidate, while relation/time/correlation/kind and legacy-assessment surfaces remain moving and no lifecycle outcome is selected.
7. AD-016AB completes only the fresh post-discovery reassessment: current hold is legal, Event-YK remediation is the leading continuation without selection authority, and a candidate-specific Board act remains mandatory before any lifecycle proposal.
8. AD-016AD completes the separately mandated Event lifecycle act after executable proof of all three preconditions; OCP-010 is `1.0.0 / Canonical` while Event remains `Accepted`, and no T7, Concept promotion, positive relation owner or next act is authorized.
9. AD-032 separately completes the OCP-001 Concept canonicalization cycle: Event becomes `Canonical` on stable live dependencies and machine-readable checks, while the Operation↔Event owner remains unresolved and Assignment/Constraint remain `Accepted`. Define `Review-After` through its separately mandated normative governance act before any YR repair.
10. AD-033 makes that governance sequence repeatable without beginning another cycle: schema 5 records the completed Event cycle, no active cycle, and mechanically preserves selection → document promotion → Concept canonicalization ordering for any separately authorized future candidate.
9. Preserve the time-anchored P-001 evidence rule: adding an invoker of unchanged `P-001@0.1.0` does not edit the T3 ledger. Stop for a separate Pattern-version act only if Pattern form/obligations change or exact `track-current` binding cannot be preserved.
10. Preserve AB-015/AB-016/AB-018/AB-019/AB-020/AB-023/AB-028 until a later exact owner/treatment and separate Board act resolve each status; AD-023 closes only the positive activation attempt on `main@f69e4b31`, while AD-024 finds that the proposed OCP-004 profile lacks an independent current consumer and legitimate owner/evaluator. AB-018 remains Open; any retry must first prove that independent basis, then prepare and separately accept a profile before another comparison.
11. Any selected-owner, history-migration, dependency, authorization-source, Assignment-alignment or IO2-boundary failure returns to Q0/Board rather than being repaired inside lifecycle promotion.
12. Preserve AB-006/AB-044–AB-047/AB-051/AB-052 and OCP-003 exclusions; Operation work creates no Organization mapping, Resource lifecycle, availability, Readiness or interchangeability authority.
13. Continue T5–T10 only through an explicit topology decision, OCP-016 routing, OCP-001 L2/atomicity and separate exact-head review/Board gates.
14. AD-034 repairs the stale current Concept distribution without changing status and makes one central current accounting claim derive OCP/Concept statuses, reviewed snapshots, P-001 invokers and executable-suite totals from live repository sources; historical act-local counts and non-formula readiness estimates remain explicitly separate.
