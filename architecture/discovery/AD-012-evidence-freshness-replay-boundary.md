---
Decision-ID: AD-012
Title: Evidence Freshness and Replay Boundary
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: AD-011, OCP-001, OCP-004, OCP-006, OCP-010, OCP-011, OCP-012, OCP-013, OCP-015, P-001
Applies-To: AB-039, evidence freshness, evidence ambiguity, deterministic replay
Review-After: External adversarial review of the freshness, ambiguity and representation candidates
---

# AD-012 — Evidence Freshness and Replay Boundary

## 1. Trigger and scope

AB-039 was opened to decide how a dynamic Constraint evaluation remains usable over time and how the same exact evaluation can be replayed deterministically. The accepted foundation has since exposed the same unresolved boundary in several places:

- OCP-004 rejects stale validation evidence for non-Draft explicit intent, but does not define a general freshness rule;
- OCP-006 exact-binds a Constraint version, context and input snapshot, but leaves the currentness of dynamic inputs open;
- OCP-010 records occurrence, observation and recording times without declaring observations fresh, true or reliable;
- OCP-011 and OCP-012 fail safe for `stale` and `ambiguous`, while explicitly leaving those classifications attributable until AB-039;
- OCP-013 and OCP-015 consume exact inputs and preserve replay, but cannot manufacture missing freshness authority.

This discovery opens AB-039. It asks who may classify exact evidence as usable for one exact decision, which ambiguity states can be detected mechanically, and what bindings make that classification replayable.

Revision `0.1.0` does not add a freshness rule, duration, timestamp format, Concept, Pattern, record family, schema, checker derivation, fixture, result vocabulary or graph edge. It does not amend any accepted OCP contract. Its purpose is to make the competing semantic owners and representations reviewable in human-readable form.

## 2. Decision questions

The freshness question is:

> For one exact use, which governed rule decides whether an exact input remains usable at an explicit evaluation time, and which temporal fact does that rule measure?

The ambiguity question is:

> Which kinds of ambiguity can Core detect from exact structure, and which require a criterion, domain rule or attributable evaluator to interpret meaning?

The replay question is:

> Which immutable bindings must be preserved so the same rule, evidence, inputs and evaluation time produce the same classification without consulting current repository state or wall-clock time?

These questions are related but not interchangeable. A deterministic replay contract does not itself choose a freshness threshold. An exact timestamp does not prove that evidence is usable. Structural ambiguity detection does not prove semantic ambiguity or resolve disagreement.

## 3. Terms that must remain distinct

| Term | Meaning in this discovery | Not implied |
|---|---|---|
| temporal effectivity | whether a governed record applies at time `t` under its own contract | evidence freshness, truth or sufficiency |
| age | deterministic difference between two comparable time values | acceptable maximum age or authority |
| freshness | use-specific classification that exact evidence is temporally usable under an exact governed rule | truth, reliability, availability or positive conclusion |
| stale | evidence fails the exact freshness rule for that exact use | false evidence, negative claim or invalid historical record |
| expiry | an explicit rule-owned boundary after which a particular use is non-positive | universal lifetime of the evidence identity |
| ambiguity | more than one unresolved structural or semantic interpretation is admissible for the exact use | ordinary disagreement or conflict automatically |
| conflict | governed inputs or heads assert incompatible values under a defined comparison | ambiguity resolved by majority, recency or count |
| replay | re-evaluation from the same exact versioned rule, evidence, inputs, context and evaluation time | re-running against current data |
| current view | a projection for a newly stated query time and rule context | mutation of a prior historical conclusion |
| recorded time | when a record was created | when the represented occurrence happened or when evidence became usable |

Freshness is relational. The same ObservationRecord may be fresh for a thirty-minute monitoring rule and stale for a five-minute launch check. An old Event may remain valid evidence that something occurred, while being unusable as evidence of a subject's current condition. Therefore no record kind receives one universal `fresh` property merely from this discovery.

## 4. Accepted baseline and known gaps

### 4.1 What is already governed

- OCP-004 binds explicit-intent validation to an exact intent version, validation rule and input snapshot; a substantive binding change invalidates prior evidence.
- OCP-006 requires deterministic Constraint evaluation for the same predicate version, parameters, input snapshot and evaluation time, or an explicit `indeterminate` result.
- OCP-010 separates `occurred_at`, `observed_at` and `recorded_at` and forbids newest timestamp, source count and list order as truth rules.
- OCP-011 binds one assessment to exact target, criterion, evidence snapshot, input snapshot, evaluator and evaluation time. Non-sufficient evidence cannot yield a definitive conclusion.
- OCP-012 binds one Capability claim to exact holder, Capability version, conditions, support snapshot, effectivity, claimant and authority. Stale or ambiguous support projects to `indeterminate`.
- OCP-013 binds one eligibility result to an exact consumer requirement, claim projections, Constraint decision, rule version, context and time.
- OCP-015 preserves immutable proposal revisions, response lineages and exact evidence snapshots without using timestamp or response count as authority.
- P-001 Module A defines record effectivity when invoked. It does not define whether external evidence is fresh for a consumer.

### 4.2 What is not yet governed

The foundation does not yet define:

- a universal reference time for every evidence kind;
- a default maximum age or expiry interval;
- a general rule for late-arriving evidence;
- clock precision, uncertainty or synchronization semantics;
- a general semantic-equivalence or contradiction engine;
- whether freshness rules belong to each criterion, each consuming contract, a reusable Pattern or a domain profile;
- whether a freshness or ambiguity conclusion needs separate identified-record history;
- a machine-verifiable basis for changing declared `sufficient` into `stale` or `ambiguous` across arbitrary accepted contracts.

The current checker can detect finite structural cases such as missing exact references, snapshot mismatch, duplicate identity and some explicit conflicting values. It cannot infer a missing semantic owner from a timestamp.

## 5. Authority boundary

Any positive freshness classification needs all of the following authorities to be explicit:

1. the consumer and exact use being protected;
2. the evidence kind and exact evidence reference;
3. the temporal fact measured for that evidence kind;
4. the exact evaluation time;
5. the exact versioned freshness rule or profile;
6. every rule input and immutable input snapshot;
7. boundary semantics, including equality at a cutoff;
8. the evaluator or deterministic rule authority;
9. provenance for a stored conclusion, if one is retained.

A duration alone is not a rule. `10 minutes` is meaningless until a legitimate owner states what is measured, for which use, relative to which evaluation time, under which inclusive or exclusive boundary and with which behavior for missing or incomparable time values.

Newest timestamp, record order, source count, evaluator count, claimant count, caller identity and current wall-clock time do not supply any missing authority.

## 6. Freshness-axis candidates

### F0 — attributable classification only

Accepted records may continue to carry attributable `stale`, `ambiguous` or equivalent non-permissive states, while Core checks only structure and the fail-safe result matrix. The checker does not claim to prove temporal usability.

F0 is the current control. It is honest where no governed freshness rule exists, but it leaves different evaluators free to apply incompatible unstated thresholds.

### F1 — contract-local versioned freshness rule

Each consuming normative contract defines or exact-references its own freshness rule. The rule names the protected use, applicable evidence kinds, temporal facts, evaluation time, inputs, cutoff semantics and non-permissive behavior.

OCP-006, OCP-011 or OCP-012 could adopt different local rules because Constraint admissibility, Objective achievement and Capability-claim support are different decisions. Shared field names would not create shared semantics.

F1 is admissible only if every consumer exact-binds its rule and replay context and if local variation does not create silent contradiction or duplicated normative formulas.

### F2 — reusable freshness-evaluation Pattern

A future Pattern defines stable cross-contract obligations for freshness evaluation: exact rule identity, evidence and input snapshots, evaluation time, reference-time selection, boundary behavior, provenance and fail-safe classification. Each invoker still owns the domain meaning and allowed evidence kinds.

F2 does not create a universal duration or a `Freshness` Concept. It is justified only if repeated accepted contracts demonstrate the same form and the Pattern reduces drift without absorbing domain semantics. AD-012 does not define or invoke such a Pattern.

### F3 — domain-owned profiles with a Core interoperability envelope

Each domain owns its freshness profiles. Core defines only exact domain/profile/version binding, immutable replay inputs and rejection of unknown or incompatible profiles.

F3 is useful when acceptable age depends irreducibly on domain operations. It is admissible only if an unknown profile cannot be treated as fresh and two profile results cannot be compared merely because both use `fresh` or `stale` labels.

## 7. Ambiguity-axis candidates

### A0 — structural detection plus attributable semantic state

Core detects only ambiguity expressible from accepted structure: zero or multiple exact-reference targets, duplicate identity, snapshot mismatch, incompatible exact versions, invalid lineage and unresolved branching where the owning contract defines those cases. Semantic ambiguity remains an attributable evaluator statement.

A0 is the current control. It avoids pretending that generic code understands domain meaning, but a bare `ambiguous` label may be too opaque for audit and replay.

### A1 — contract-local ambiguity rules

Each consuming contract defines named ambiguity dimensions and exact detection rules. Examples include reference ambiguity, lineage ambiguity, criterion ambiguity, temporal ambiguity and semantic classification ambiguity.

A1 may make the relevant cases machine-verifiable without claiming one universal ambiguity engine. It must distinguish legitimate context-specific disagreement from unresolved ambiguity and must not select a winner by newest timestamp, majority or source count.

### A2 — reusable ambiguity obligations

A future Pattern defines shared structural obligations such as an exact ambiguity reason, the candidate interpretations considered, rule/profile version, immutable inputs and a non-permissive result. Invokers own the semantic dimensions and comparison rules.

A2 is admissible only if a stable shared form exists across accepted contracts. It must not convert implementation helpers or a common word into shared domain semantics.

### A3 — domain-owned ambiguity profiles with a Core envelope

Domains define semantic ambiguity detection, while Core validates exact profile binding and rejects unknown, mismatched or unresolvable meanings.

A3 preserves domain ownership but can weaken interoperability. A Core consumer may transport an opaque domain result; it may not reinterpret or compare that result without an accepted mapping.

## 8. Representation variants

Freshness and ambiguity ownership do not by themselves decide storage. Any non-control outcome must justify one of these representations:

1. **inline consuming result** — the consuming evaluation records the exact rule/profile and classification in its own immutable snapshot-bound record;
2. **separate identified record** — a distinct evidence-usability assessment has stable identity, provenance, endpoints and correction or supersession history;
3. **derived-only view** — a deterministic rule derives the classification from exact immutable inputs for an explicit evaluation time without storing a standing current value;
4. **domain-local record or derivation** — a domain owns the representation and Core only validates an interoperability envelope.

Storage location is not semantic authority. A derived-only view is admissible only when historical inputs and rule versions remain resolvable. A stored `expires_at` or `fresh: true` field is only a projection unless its rule owner and derivation are exact. A separate record is justified only if the conclusion needs independent reference, attribution or history that the consuming record cannot preserve.

## 9. Required examples

### 9.1 Same evidence, different legitimate uses

One ObservationRecord was observed at `10:00`. At evaluation time `10:08`, a five-minute launch criterion rejects it as stale while a thirty-minute monitoring criterion accepts it as fresh.

The conclusions are not contradictory because they bind different exact rules and uses. Any candidate that stores one global freshness value on the ObservationRecord fails this example.

### 9.2 Historical truth versus current reuse

An OutcomeAssessmentRecord evaluated at `10:08` used evidence that was sufficient under its exact rule at that time. At `11:00`, a consumer asks whether the same evidence is usable for a new decision.

The historical record does not mutate to stale. The new use requires a new explicit evaluation time and governed rule. Historical replay at `10:08` must reproduce the original classification; current reuse at `11:00` may fail safe.

### 9.3 Late arrival

An ObservationRecord says the observation occurred at `10:00` but was recorded at `10:20`. A rule may care about age since observation, delivery delay, both, or neither. Selecting `recorded_at` because it is newest is not a valid default.

### 9.4 Constraint replay and current admissibility

A ConstraintEvaluationRecord exact-bound to a predicate version, context, input snapshot and evaluation time remains replayable. It does not remain automatically usable for a later candidate context with dynamic inputs. Replaying the old decision and making a new current decision are separate operations.

## 10. Mandatory counterexamples

External review must test every applicable candidate against at least these cases:

1. The same evidence is fresh for one exact criterion and stale for another.
2. An old Event remains relevant to historical Objective achievement but not to current condition.
3. A record has `observed_at`, `recorded_at` and an Event `occurred_at`; code silently chooses one.
4. Late-arriving evidence has a recent recording time and an old observation time.
5. A future-dated, timezone-less or incomparable timestamp is treated as fresh.
6. A cutoff equality case changes between implementations because interval boundaries are implicit.
7. Current wall-clock time replaces the recorded evaluation time during historical replay.
8. Current evidence or a latest rule version replaces the exact historical snapshot or rule.
9. A historical assessment is mutated or invalidated merely because time passed.
10. Missing freshness rule, rule version, evaluation time or input snapshot yields positive usability.
11. `stale` is translated into false evidence, a negative Capability claim or a negative Objective conclusion.
12. `fresh` is translated into truth, source reliability, availability, Readiness or authorization.
13. Two exact references resolve, but the criterion cannot distinguish their semantic meaning.
14. Two legitimate context-specific conclusions are mislabeled as ambiguous or conflicting.
15. Conflicting evidence is resolved by newest timestamp, majority, evaluator count or source count.
16. Branching supersession is collapsed into one newest head.
17. An unknown domain freshness or ambiguity profile is treated as compatible.
18. A derived-only outcome cannot reproduce the historical result because its old inputs are unavailable.
19. A separate usability record changes its evidence, criterion or rule binding under one identity.
20. Evidence obligations assume a stored record, Pattern or domain layer rejected by the candidate itself.

No candidate may pass by making a more permissive result from missing, stale, ambiguous, conflicting, unresolved or structurally invalid inputs.

## 11. Evidence and authority matrix

| Input or conclusion | Current owner | Permitted use | Forbidden upgrade |
|---|---|---|---|
| explicit-intent validation binding | OCP-004 | exact intent/rule/input evidence | general freshness rule or authorization |
| Constraint context and evaluation | OCP-006 | exact predicate, context, snapshot and evaluation time | implicit currentness of dynamic inputs |
| Event occurrence | OCP-010 | exact occurrence identity and time | current condition or evidence truth |
| ObservationRecord | OCP-010 | attributable statement with observed/recorded times | universal freshness, reliability or truth |
| OutcomeAssessmentRecord | OCP-011 | attributable exact assessment and fail-safe matrix | checker-proven stale/ambiguous without AB-039 owner |
| CapabilityClaimRecord | OCP-012 | attributable claim, support state and effectivity | verified possession or universal support freshness |
| eligibility result | OCP-013 plus exact consumer requirement | directional result for one context and time | availability, selection, Readiness or freshness authority |
| Coordination evidence | OCP-015 | exact proposal/response evidence projection | authorization or general evidence-quality rule |
| record effectivity | invoking contract under P-001 Module A | whether that record applies at time `t` | freshness of evidence consumed by another decision |
| freshness/ambiguity semantics | AB-039 / AD-012, unresolved | comparison of candidate owners and representations | assumed threshold or generic semantic engine |

## 12. Unconditional semantic core

Every admissible outcome must preserve these guarantees, regardless of representation:

1. freshness and ambiguity are classified for an exact use, not assigned globally to an evidence identity;
2. the attributable recorder or evaluator is explicit, and any machine-derived or shared classification names its normative owner;
3. evidence and every input claimed by the classification are preserved through exact immutable bindings appropriate to the owning contract;
4. any candidate that derives temporal usability exact-binds its evaluation time, rule or profile version, temporal fact for each evidence kind and cutoff behavior;
5. the same exact authoritative bindings—or the same exact attributable record under F0/A0—replay to the same classification regardless of record order;
6. current repository data, current wall clock and latest rule versions never replace historical inputs;
7. missing, unresolved, incomparable or invalid inputs are non-permissive;
8. `stale` does not mean false or negative, and `fresh` does not mean true or sufficient by itself;
9. structural ambiguity, semantic ambiguity and conflict remain distinguishable;
10. no timestamp, count, order or caller identity becomes authority by convenience;
11. historical records remain immutable and exact-resolvable;
12. a positive downstream conclusion still requires its own accepted criterion and authority.

These are semantic obligations, not an accepted schema.

For F0/A0, the semantic equivalent of a governed classification rule is an explicit authority limit: Core replays the exact attributable statement, does not present it as machine-proven or portable across consumers, and keeps every non-permissive downstream guard. A rule-owning outcome must instead prove exact rule binding and deterministic derivation.

## 13. Outcome-conditional executable evidence

Executable evidence must remain outcome-fair under OCP-001.

| Candidate | Required evidence if selected |
|---|---|
| F0 | Fixtures prove attributed non-permissive states cannot yield positive results and checker output does not claim machine-proven freshness. |
| F1 | Each selected contract owns exact rule/version bindings, cutoff behavior, missing-input failure and same-snapshot replay fixtures. |
| F2 | Every Pattern invoker proves complete invocation, local semantic ownership and cross-invoker conformance without a universal duration. |
| F3 | Domain fixtures prove local semantics; Core fixtures reject unknown, mismatched and incomparable domain/profile versions. |
| A0 | Core fixtures cover only named structural ambiguities and preserve attributed semantic uncertainty without overclaiming. |
| A1 | Each contract names ambiguity dimensions and tests legitimate divergence, unresolved interpretation and conflict separately. |
| A2 | Pattern fixtures prove shared structural obligations while invokers retain semantic comparison rules. |
| A3 | Domain fixtures own semantic cases; Core detects unknown or incompatible profile bindings. |
| inline representation | The consuming record binds the exact classification rule and cannot detach it from its immutable snapshots. |
| separate record | Identity and supersession tests prevent binding changes, order-based heads and history loss. |
| derived-only representation | Identical exact inputs reproduce identical results; unavailable historical inputs fail closed rather than consulting current data. |

The unconditional test set covers §10 only where the behavior is expressible for every candidate. A fixture that requires a separate record, reusable Pattern or domain profile belongs only to that candidate's block. External review must reject any evidence plan that assumes a layer rejected by the selected outcome.

## 14. Candidate-separating questions for external review

Fable should attempt to determine:

1. whether F0/A0 remains sufficient as an honest fail-safe control while no consumer supplies a governed rule;
2. whether freshness is necessarily criterion-local, or whether OCP-006/OCP-011/OCP-012 demonstrate stable cross-contract form;
3. whether repeated form is mature enough for F2/A2 without moving domain semantics into a Pattern;
4. whether any demonstrated consumer needs to reference an evidence-usability conclusion independently of its consuming assessment or evaluation;
5. whether a separate identified usability record overlaps OCP-011 or creates a generic assessment container;
6. whether domain variability justifies F3/A3 and whether a Core envelope can reject unknown meanings safely;
7. which ambiguity dimensions are mechanically detectable from current accepted structures;
8. whether `ambiguous` needs exact reason codes or candidate interpretations for auditability;
9. how cutoff equality, late arrival, timestamp precision and incomparable times fail safe without defining a universal time ontology;
10. whether historical replay and new current evaluation remain visibly separate in every candidate;
11. whether all twenty counterexamples are fairly mapped to every applicable candidate; and
12. whether the document remains understandable without checker code.

If evidence cannot distinguish the owner model, ambiguity model or representation, AD-012 must remain in `Discovery`. Implementation convenience is not decision-separating evidence.

## 15. Working hypotheses, not selections

F1 is the leading positive candidate because freshness is use-specific and accepted contracts already bind exact criteria, contexts, snapshots and evaluation times. Its main risk is duplicated or drifting rule shape across contracts.

F2 is promising only if the comparison demonstrates a stable shared form across multiple accepted contracts. Its main risk is a generic Pattern that silently owns domain semantics.

A separate identified usability record is justified only if a concrete consumer needs independent reference, attribution or correction history for the usability conclusion. Its main risk is overlapping OCP-011 and multiplying record families; if selected later, it would require a full P-001 invocation or an explicit reason not to use P-001.

F3/A3 may be necessary for irreducibly domain-specific timing or semantic interpretation. Their main risk is opaque profiles that Core can transport but cannot compare safely.

F0/A0 remain the honest current controls. They preserve fail-safe behavior but do not satisfy the roadmap goal of machine-verifiable `stale` and `ambiguous` states. A later comparison may still conclude that only a narrow subset is mechanically derivable.

A1 is the leading ambiguity candidate because reference, lineage, temporal and semantic ambiguity have different owners. Its main risk is inconsistent reason vocabularies and insufficient cross-contract auditability.

These hypotheses do not pre-approve a Pattern, record family, OCP extension, duration, profile vocabulary or checker implementation.

## 16. Discovery status and accounting

AD-012 moves AB-039 from `Open` to `Discovery` and supplies the first explicit candidate space for freshness, ambiguity and replay ownership.

Revision `0.1.0` does not change any Concept or document status, OCP version, P-001 invocation, Foundation map, Concept dependency, schema, checker rule or fixture. Existing OCP-011 and OCP-012 fail-safe matrices remain authoritative: declared `stale` or `ambiguous` cannot support a permissive conclusion, but the checker does not yet claim general proof of those states.

AD-011 remains closed at S0/R0. AD-012 does not reopen Readiness; a future R1 proposal would still need a concrete consumer, exact preparedness criterion, target contract and evaluator/rule authority in addition to any accepted freshness/replay semantics.

The next revision may incorporate external findings and compare the candidates in greater detail. Any Board selection and any downstream normative contract require separate exact-head Fable review, Codex adjudication, green CI and explicit Pavlo or Architecture Board authorization before squash merge.
