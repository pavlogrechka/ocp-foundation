---
Decision-ID: AD-012
Title: Evidence Freshness and Replay Boundary
Version: 0.3.0
Status: Accepted
Owner: Architecture Board
Depends-On: AD-011, OCP-001, OCP-004, OCP-006, OCP-010, OCP-011, OCP-012, OCP-013, OCP-015, P-001
Applies-To: AB-039, evidence freshness, evidence ambiguity, deterministic replay
Review-After: Accepted contract-local invocations demonstrate stable shared obligations, a concrete domain boundary requires profiles, or a consumer needs an independently referenced usability record
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

Revision `0.1.0` moved AB-039 from `Open` to `Discovery` and supplied the first explicit candidate space for freshness, ambiguity and replay ownership.

Revision `0.1.0` does not change any Concept or document status, OCP version, P-001 invocation, Foundation map, Concept dependency, schema, checker rule or fixture. Existing OCP-011 and OCP-012 fail-safe matrices remain authoritative: declared `stale` or `ambiguous` cannot support a permissive conclusion, but the checker does not yet claim general proof of those states.

AD-011 remains closed at S0/R0. AD-012 does not reopen Readiness; a future R1 proposal would still need a concrete consumer, exact preparedness criterion, target contract and evaluator/rule authority in addition to any accepted freshness/replay semantics.

Revision `0.1.0` was exact-head reviewed, adjudicated, owner-authorized and squash-merged through PR #62. Revision `0.2.0` adds comparison only. Any Board selection and any downstream normative contract require separate exact-head Fable review, Codex adjudication, green CI and explicit Pavlo or Architecture Board authorization before squash merge.

## 17. Comparison method and verdict vocabulary

This revision compares the freshness axis, ambiguity axis and representation variants for external review. It does not select an owner model, a threshold, an ambiguity vocabulary, a representation or a downstream artifact.

The comparison follows five rules:

1. F0 and A0 are complete no-new-authority controls, not unfinished implementations.
2. Freshness ownership, ambiguity ownership and representation are evaluated separately.
3. A machine-derived outcome must name every normative owner, exact input and fail-safe branch it adds.
4. Every candidate is tested against the same human examples and all twenty counterexamples in §10, using evidence expressible for that candidate.
5. Similar fields or labels are not evidence of shared semantics, and implementation convenience is not decision-separating evidence.

The working verdicts below mean:

- **admissible control** — safe and complete while no shared derivation authority is justified;
- **leading hypothesis** — the smallest currently plausible positive direction, still subject to explicit evidence gates;
- **conditional alternative** — admissible only when a concrete consumer demonstrates the additional owner or representation it needs; and
- **not supported by current evidence** — review may falsify or revive the candidate, but the present repository cannot justify selecting it.

These are comparison verdicts, not Architecture Board selections.

## 18. Freshness-axis comparison

The freshness axis asks who may decide that exact evidence is temporally usable for one exact use.

| Outcome | Plain-language effect | Added authority | Main benefit | Main risk | Separate working verdict |
|---|---|---|---|---|---|
| F0 — attributable classification only | Core preserves an exact recorder or evaluator statement and enforces non-permissive downstream behavior without claiming to derive freshness. | None beyond the existing record authority. | Honest when no governed temporal rule exists. | Different evaluators may use incompatible unstated thresholds and the statement may not be portable. | **Admissible control and current default.** |
| F1 — contract-local versioned rule | Each consumer owns or exact-references the temporal rule for its own decision. | The consuming contract owns only its exact rule, temporal fact, cutoff and result. | Fits the use-relative nature of freshness and existing exact-binding contracts. | Rule shapes may drift or duplicate across OCPs. | **Leading hypothesis.** Selection still needs at least one complete concrete rule shape and evidence that local variation is intentional. |
| F2 — reusable Pattern obligations | A Pattern standardizes the form of freshness evaluation while each invoker owns meaning and permitted evidence. | Shared record or evaluation obligations, but no shared duration or domain meaning. | Could reduce repeated governance and replay defects across consumers. | A generic Pattern may silently become the rule owner or a universal time policy. | **Conditional alternative.** Repeated accepted invocations must first demonstrate a stable common form. |
| F3 — domain profiles with Core envelope | A domain defines the rule; Core exact-binds the profile and rejects unknown or incompatible meanings. | Each named domain profile owns its exact meaning; Core owns only envelope validation. | Preserves irreducibly domain-specific timing. | Opaque profiles may be transportable but not safely comparable. | **Conditional alternative.** It needs a concrete domain boundary and an interoperability need that F1 cannot express. |

### 18.1 Freshness decision-separating evidence

External review should ask:

- Which exact consumer needs a machine-derived freshness conclusion now?
- Which temporal fact does that consumer legitimately measure for each evidence kind?
- Can OCP-006, OCP-011 and OCP-012 use one stable obligation form without sharing thresholds or evidence meaning?
- Which real domain rule cannot be represented as a contract-local exact reference?
- Does a claimed reusable form reduce normative duplication, or merely move it behind generic names?
- Can cutoff equality, late arrival, missing time and incomparable time fail closed without inventing a universal time ontology?

F1 is the smallest positive hypothesis because the accepted contracts already bind exact criteria, contexts, snapshots and evaluation times. It is not selected merely because those fields exist. F0 remains correct wherever the concrete rule owner or inputs are absent.

### 18.2 Accepted-consumer fit

The accepted contracts expose repeated replay form, but not one demonstrated freshness meaning:

| Contract | Exact decision already owned | Freshness boundary exposed | Comparison consequence |
|---|---|---|---|
| OCP-004 | whether explicit intent is valid for one exact Operation revision and validation binding | a substantive binding change makes prior validation evidence stale | Strong F1 evidence: the Operation contract owns what changed. It does not define age for ObservationRecord or claim support. |
| OCP-006 | whether one exact Constraint is satisfied for one context, snapshot and model time | dynamic inputs may cease to be usable for a later evaluation | Strong F1 evidence and shared replay form; the predicate and context still own input meaning. |
| OCP-010 | occurrence and attributable observation facts with distinct times | it provides possible temporal facts but no usability threshold | It is an evidence provider, not a general F owner. A consumer must name which fact it measures. |
| OCP-011 | Objective outcome under one criterion, evidence/input snapshots and evaluation time | `stale` remains attributable and non-permissive until AB-039 | Strong F1 target and possible F2 form evidence; criterion-specific evidence meaning must remain local. |
| OCP-012 | holder-specific Capability claim with exact support, conditions and effectivity | stale support cannot project positive, but Core does not derive staleness | Strong F1 target with semantics distinct from Objective assessment; freshness never verifies possession. |
| OCP-013 | directional eligibility for one exact consumer requirement and context | current eligibility may depend on exact current claim projections and Constraint inputs | It may own freshness for its consumer inputs, but cannot rewrite the source claim or assessment. |
| OCP-015 | one exact proposal/response evidence projection | snapshots preserve replay, but response age does not grant authorization or agreement | It demonstrates replay obligations without yet demonstrating a shared freshness rule. |

This spread supports F1 as the least-authority positive direction. It also supplies material for testing F2, but repeated fields alone do not yet prove a Pattern: temporal facts, positive criteria and evidence kinds differ materially.

## 19. Ambiguity-axis comparison

The ambiguity axis asks which uncertainty Core can detect structurally and who may interpret unresolved meaning.

| Outcome | Plain-language effect | Added authority | Main benefit | Main risk | Separate working verdict |
|---|---|---|---|---|---|
| A0 — structural detection plus attributable semantic state | Core rejects finite structural defects; semantic ambiguity remains an exact attributable statement. | None beyond accepted structural contracts and the recorder or evaluator. | Avoids pretending that generic code understands domain meaning. | A bare label may be too opaque to replay why an evaluator was uncertain. | **Admissible control and current default.** |
| A1 — contract-local ambiguity rules | Each consumer names the ambiguity dimensions it can detect and exact-binds their rules. | The consuming contract owns only its named reference, lineage, criterion, temporal or semantic dimensions. | Makes relevant cases auditable without a universal semantic engine. | Reason vocabularies and comparison rules may drift between contracts. | **Leading hypothesis.** Selection needs a bounded dimension set and examples separating ambiguity, conflict and legitimate divergence. |
| A2 — reusable ambiguity obligations | A Pattern standardizes reason, candidate-interpretation, input and fail-safe obligations while invokers own semantic comparison. | Shared structural obligations, not shared interpretation. | Could make attributed and derived uncertainty consistently auditable. | Common reason codes may be mistaken for common domain meaning. | **Conditional alternative.** Stable repeated obligations must be demonstrated first. |
| A3 — domain profiles with Core envelope | Domains own semantic detection while Core validates exact profile binding and incompatibility. | Each domain profile owns its dimensions and rules; Core owns envelope rejection. | Preserves meanings that cannot be interpreted in Core. | Callers may compare identical labels from incompatible profiles. | **Conditional alternative.** It needs concrete domain semantics and safe transport requirements. |

### 19.1 Ambiguity decision-separating evidence

External review should ask:

- Which ambiguities are fully expressible from accepted exact-reference, snapshot and lineage structures?
- Which consumer needs more than an attributable `ambiguous` state to audit or replay the decision?
- Can named dimensions distinguish unresolved interpretation from ordinary evaluator disagreement and context-specific conclusions?
- Which obligations repeat across contracts without moving their comparison rules into Core?
- Can an unknown reason or profile remain non-permissive without being normalized by label?

A1 is the smallest positive hypothesis for named machine-verifiable dimensions. A0 remains binding wherever semantic comparison lacks a governed owner. A1 does not authorize Core to infer semantic equivalence from text, counts or timestamps.

### 19.2 Structural and semantic boundary

The current repository supports a narrower structural baseline than a generic `ambiguous` label may suggest:

| Core can detect when the owning accepted structure defines it | Core cannot infer without a new exact owner |
|---|---|
| zero or multiple exact-reference targets | whether two resolved records mean the same thing |
| duplicate identity | whether two statements are substantively equivalent |
| wrong or incompatible exact version binding | which domain version should win |
| evidence/input snapshot mismatch | whether different snapshots are equally sufficient |
| invalid, cyclic or unresolved supersession lineage | whether one legitimate branch is semantically preferable |
| multiple unsuperseded heads where the owning contract defines non-permissive projection | whether evaluator disagreement is ambiguity, conflict or valid contextual divergence |
| malformed or missing structurally required fields | which temporal fact, criterion or interpretation the caller intended |

A1 may name and test some right-column dimensions inside a specific consuming contract. A2 or A3 would still need separate proof that a shared obligation or domain profile adds value without claiming a universal semantic engine.

## 20. Representation comparison

Representation cannot supply missing freshness or ambiguity authority. It records or projects a conclusion whose owner must already be selected.

| Variant | Plain-language effect | Main benefit | Main risk | Separate working verdict |
|---|---|---|---|---|
| inline consuming result | The consuming assessment or evaluation records its exact rule/profile, inputs, time and classification in the same immutable snapshot-bound artifact. | Smallest historical form; keeps classification attached to the decision it protects. | Repeated bindings and vocabulary may drift across consuming contracts. | **Leading historical representation** if F1/A1 or another governed owner is selected. Existing F0/A0 attributable states may also remain inline. |
| separate identified record | A usability assessment has independent identity, attribution, endpoints and correction or supersession history. | Supports a governed reference to the same exact use-specific conclusion when that conclusion needs history of its own. | Overlaps OCP-011, creates another assessment family and can turn use-relative freshness into a standing property. | **Not supported by current evidence; conditional alternative only.** It needs a concrete independent-reference or correction-history consumer and, if selected, a full P-001 invocation or explicit reason not to invoke it. |
| derived-only view | A deterministic rule evaluates exact immutable inputs for an explicit query time without storing a standing current flag. | Avoids mutable `fresh: true` state and cleanly separates historical replay from a new current query. | Historical replay fails if old rule versions or inputs disappear; implementations may consult current state. | **Leading projection alternative**, but only under a selected rule-owning outcome with durable exact inputs and fail-closed unavailability. It cannot turn F0/A0 into machine proof. |
| domain-local record or derivation | A domain owns storage or derivation and Core validates only the selected envelope. | Keeps irreducible domain representation outside Core. | Core may transport but cannot compare opaque results safely. | **Conditional alternative** coupled to a justified F3 and/or A3 envelope. |

A global freshness field on an evidence identity is not admissible: the same evidence may be usable for one exact use and stale for another. A later Board act may select different representations for historical conclusions and current projections, but each role and authority must be explicit rather than treated as an implementation choice.

## 21. Axis independence and combination behavior

No F/A/representation combination is selected by this comparison. The following combinations expose the independent gates:

- **F0 + A0 + inline attributable states** is the current safe behavior. Core preserves the statement and enforces the accepted fail-safe matrix without claiming semantic derivation.
- **F1 + A1 + inline result** is the smallest currently plausible positive combination. Each consuming contract owns its exact freshness and ambiguity rules in the historical decision.
- **F1 + A0** may derive temporal usability while leaving semantic ambiguity attributable; machine-verifiable freshness does not create a semantic comparison engine.
- **F0 + A1** may detect governed ambiguity dimensions while leaving temporal usability attributable; ambiguity rules do not create a freshness threshold.
- **F2 and/or A2** require separate proof that repeated obligations are stable. Choosing one reusable axis does not justify the other.
- **F3 and/or A3** require exact domain/profile/version binding. A domain freshness profile does not automatically own ambiguity, and identical labels remain incomparable without an accepted mapping.
- **derived-only** may serve a new query under F1–F3 or A1–A3 only when the exact historical rule and inputs are resolvable. It does not replace the immutable historical consuming result.
- **a separate record** may be combined with any selected semantic owner only after independent identity and consumer evidence is demonstrated. Its existence never makes the classification authoritative.

A combination fails if representation changes semantic ownership, if one global value is attached to the evidence identity, or if missing authority is filled by newest timestamp, record order, count, caller identity or current wall clock.

## 22. Normative authority accounting

“Unselected” below is an explicit evidence gap, not permission for an implementation to choose an owner.

| Binding or conclusion | Current or candidate owner | Fail-safe obligation |
|---|---|---|
| protected consumer and exact use | accepted consuming contract; exact positive owner unselected | A classification from another use is not portable by label. |
| evidence kind and exact reference | accepted evidence and consuming contracts | Missing, unresolved or wrong-kind evidence is non-permissive. |
| temporal fact measured | unselected under F0; exact consuming rule, Pattern invocation or domain profile under F1–F3 | Code cannot silently choose occurrence, observation, recording, effectivity or receipt time. |
| evaluation time | exact consuming record or derived query contract | Current wall clock cannot replace the recorded time during replay. |
| cutoff and boundary behavior | unselected under F0; exact versioned F1–F3 owner if selected | Missing equality, precision or incomparable-time behavior cannot yield positive usability. |
| freshness rule/profile version | unselected under F0; exact F1–F3 owner if selected | Latest available rule cannot replace the exact historical version. |
| ambiguity dimensions and comparison rules | finite accepted structure plus attributable evaluator under A0; exact A1–A3 owner if selected | Structural, semantic and conflict states cannot be collapsed or resolved by count or recency. |
| evidence and input snapshots | accepted consuming contract and any selected Pattern/profile invocation | Current evidence cannot replace the exact historical snapshot. |
| evaluator or deterministic rule authority | accepted consuming contract; otherwise unselected | Caller identity and number of evaluators do not create authority. |
| historical stored conclusion | its accepted record contract | The record remains immutable; correction preserves explicit history. |
| current projection | selected exact rule plus explicit query time and inputs | It is a new evaluation, not mutation or automatic invalidation of history. |
| record effectivity | invoking contract under P-001 Module A | Effectivity does not become evidence freshness. |
| source reliability, truth, sufficiency, availability, Readiness and authorization | their own governed owners, outside this decision | `fresh` cannot be promoted into any of these conclusions. |

## 23. Mandatory counterexample mapping

Every row maps the complete §10 pressure to all three comparison dimensions. A range means every candidate in that range must preserve the stated behavior.

| # | Pressure | Freshness-axis required behavior | Ambiguity-axis required behavior | Representation required behavior | Future executable-evidence owner |
|---|---|---|---|---|---|
| 1 | Same evidence is fresh for one criterion and stale for another | **F0:** preserve separate attributable uses. **F1–F3:** exact-bind each use and rule. | **A0–A3:** legitimate rule-specific divergence is not ambiguity by itself. | No global evidence flag; every stored or derived result binds its exact use. | Selected F owner plus each consuming contract. |
| 2 | Old Event remains historically relevant but not current-condition evidence | **F0–F3:** historical validity and new temporal usability remain separate. | **A0–A3:** the two questions are not conflicting interpretations. | Historical result stays immutable; current reuse is a new stored or derived evaluation. | OCP-010 plus selected consumer/F owner. |
| 3 | Code silently chooses among occurrence, observation and recording time | **F0:** no machine-derived positive claim. **F1–F3:** name the exact temporal fact per evidence kind. | **A0:** leave unresolved meaning attributable. **A1–A3:** classify named temporal ambiguity only under an exact rule/profile. | Preserve the selected binding; storage location cannot choose it. | Selected F/A owner. |
| 4 | Late arrival looks recent by recording time | **F0–F3:** never substitute newest time; the rule states whether age, delay, both or neither matters. | **A0–A3:** missing temporal interpretation remains unresolved, not silently normalized. | Record or derivation preserves every exact time input used. | Selected F owner and evidence contract. |
| 5 | Future-dated, timezone-less or incomparable time is treated as fresh | **F0:** no Core derivation. **F1–F3:** explicit comparability and non-permissive failure. | **A0:** reject structural invalidity where expressible. **A1–A3:** exact-bind any temporal-ambiguity rule. | No representation normalizes or guesses missing semantics. | Selected F/A owner plus schema only after selection. |
| 6 | Cutoff equality differs between implementations | **F0:** no implicit cutoff. **F1–F3:** bind inclusive/exclusive equality and precision behavior. | **A0–A3:** missing boundary semantics stays unresolved and non-permissive. | Rule version and boundary inputs remain replayable. | Selected F owner. |
| 7 | Wall clock replaces evaluation time during replay | **F0–F3:** replay uses the recorded exact time. | **A0–A3:** no ambiguity path licenses time substitution. | Derived queries require explicit time; stored history never recomputes silently. | Every selected consuming/derivation contract. |
| 8 | Current evidence or latest rule replaces historical bindings | **F0:** replay the exact attributable record. **F1–F3:** replay exact rule and snapshots. | **A0–A3:** mismatch or unresolved binding is non-permissive. | Inline/separate history retains exact references; derived-only fails if they are unavailable. | Every selected owner. |
| 9 | Historical assessment changes merely because time passed | **F0–F3:** historical conclusion remains valid for its recorded use and time. | **A0–A3:** age alone does not make its meaning ambiguous. | Never mutate history; create a new evaluation or query. | Existing record contract plus selected consumer. |
| 10 | Missing rule, version, time or snapshot yields positive usability | **F0:** cannot claim machine-proven positive freshness. **F1–F3:** fail closed. | **A0–A3:** missing interpretation authority cannot become resolved. | No fallback to defaults, current state or standing flags. | Every selected owner. |
| 11 | `stale` becomes false evidence or a negative domain conclusion | **F0–F3:** stale means unusable for the exact temporal use only. | **A0–A3:** no ambiguity rule changes that meaning. | Preserve freshness state separately from evidence truth and domain conclusion. | Every consuming contract. |
| 12 | `fresh` becomes truth, reliability, availability, Readiness or authorization | **F0–F3:** freshness supplies none of those authorities. | **A0–A3:** absence of ambiguity supplies none either. | No stored or derived projection upgrades the conclusion. | Downstream domain owners and compatibility fixtures. |
| 13 | Two exact references resolve but their semantic meaning cannot be distinguished | **F0–F3:** temporal usability cannot resolve semantic equivalence. | **A0:** preserve attributable semantic uncertainty. **A1–A3:** use only an exact governed semantic dimension/profile. | Preserve candidate references or the exact attributable statement; do not choose by order. | Selected A owner. |
| 14 | Legitimate context-specific conclusions are mislabeled ambiguous or conflicting | **F0–F3:** retain each exact use and rule. | **A0–A3:** distinguish different contexts from unresolved interpretation and conflict. | Separate exact contexts remain independently replayable. | Selected A owner plus consuming contracts. |
| 15 | Conflict is resolved by recency, majority or count | **F0–F3:** those signals add no freshness authority. | **A0–A3:** no winner without an explicit governed comparison or lineage rule. | Representation preserves conflicting candidates and provenance. | Selected A owner and lineage contract. |
| 16 | Branching supersession is collapsed into one newest head | **F0–F3:** freshness cannot choose a head. | **A0:** accepted structure detects unresolved branching where defined. **A1–A3:** named lineage rule/profile must fail closed. | Separate records preserve branches; inline/derived consumers exact-bind the chosen governed head or remain non-permissive. | P-001 invoker or exact owning contract. |
| 17 | Unknown domain profile is treated as compatible | **F3:** reject unknown/mismatched profile versions. **F0–F2:** do not reinterpret a domain label as local authority. | **A3:** reject unknown/mismatched profiles. **A0–A2:** do not normalize them by label. | Domain-local representation carries exact envelope bindings. | Core envelope plus each named domain profile. |
| 18 | Derived-only history cannot reproduce because old inputs disappeared | **F0–F3:** missing historical inputs is non-permissive. | **A0–A3:** unavailability is not resolved by current interpretations. | Derived-only fails closed; inline or separate history must retain resolvable exact snapshots. | Selected derivation and retention contract. |
| 19 | Separate usability record changes bindings under one identity | **F0–F3:** rule, evidence and use bindings remain immutable for that identity. | **A0–A3:** changed meaning requires explicit correction/supersession, never silent reinterpretation. | A selected separate record needs full identity and branching-history evidence; otherwise it is inadmissible. | P-001 invocation or explicitly justified record contract. |
| 20 | Evidence assumes a layer rejected by the candidate | **F0–F3:** each candidate proves only its own owner model. | **A0–A3:** structural, contract, Pattern and domain blocks remain separate. | Inline, separate, derived and domain fixtures are conditional on the selected representation. | OCP-001 outcome-fair review plus each selected owner. |

No row may pass by turning missing, stale, ambiguous, conflicting, unresolved, incomparable or structurally invalid inputs into a more permissive result.

## 24. Executable-evidence plan by candidate

This comparison adds no checker code or fixtures. It assigns future evidence only to the normative owner that would exist after selection.

| Candidate | Required downstream evidence |
|---|---|
| F0 | Compatibility fixtures show that attributable `stale` or equivalent states remain non-permissive and checker output never claims a machine-proven threshold. |
| F1 | Each selected consuming contract tests exact use, evidence kind, temporal fact, rule/version, evaluation time, snapshots, cutoff equality, incomparable inputs and historical replay. |
| F2 | A separately reviewed Pattern and every invocation prove complete bindings, stable shared obligations, local semantic ownership and absence of a universal duration. |
| F3 | Each domain owns semantic fixtures; the Core envelope rejects unknown, mismatched and incomparable domain/profile versions. |
| A0 | Core fixtures cover only named finite structural cases and preserve attributable semantic uncertainty without overclaiming. |
| A1 | Each selected contract tests every named dimension, legitimate contextual divergence, unresolved interpretation and conflict separately. |
| A2 | A separately reviewed Pattern proves shared reason/input/provenance obligations while every invoker owns semantic comparison. |
| A3 | Each domain owns semantic ambiguity fixtures; the Core envelope rejects unknown and incompatible profiles. |
| inline result | The consuming record cannot detach the classification from its exact rule, evidence, input snapshots, context and evaluation time. |
| separate record | A full identity, provenance, endpoint, correction, supersession and branching suite proves independent consumer need and prevents binding changes under one identity. |
| derived-only view | Same exact inputs reproduce the same result; missing historical rules or inputs fail closed and current data or wall clock is never consulted implicitly. |
| domain-local representation | Domain fixtures prove local storage/derivation; Core fixtures validate exact envelope bindings without comparing opaque meanings. |

If F0 or A0 is later selected, no placeholder rule, Pattern, profile, record family or checker module is created merely to make the control appear implemented.

## 25. Comparison status and next decision gate

Revision `0.1.0` opened `AB-039 / AD-012` in Discovery. Fable approved its exact head with zero findings, Codex accepted the verdict, Pavlo authorized merge, and PR #62 was squash-merged with green post-merge CI.

Revision `0.2.0` supplies separate F0–F3 and A0–A3 working verdicts, representation comparison, combination behavior, authority accounting, a complete map of all twenty counterexamples and outcome-conditional executable-evidence ownership. It remains `Discovery` and records no Architecture Board selection.

External adversarial review must now determine separately:

1. whether F1 is fairly identified as the smallest positive freshness hypothesis while F0 remains the full current control;
2. whether A1 is fairly identified as the smallest positive ambiguity hypothesis while A0 remains the full current control;
3. whether current evidence demonstrates a stable cross-contract form for F2 or A2;
4. whether any concrete domain boundary justifies F3 or A3;
5. whether inline history and derived-only current projection are distinguished without silently selecting both;
6. whether a separate identified record is correctly withheld absent an independent-reference or correction-history consumer;
7. whether every authority in §22 and all twenty counterexamples in §23 are mapped fairly; and
8. whether the comparison remains understandable without checker code.

A later `AD-012B` Board act may select one outcome per decidable semantic axis and an explicit representation by role, or keep any axis in `Discovery`. A selection act may not itself create a Pattern, record family, domain profile, schema, checker rule, fixture or graph edge. Each such normative artifact requires its own accepted contract and evidence cycle.

Exact-head Fable approval, Codex adjudication, green CI and explicit Pavlo or Architecture Board authorization remain mandatory before squash merge of this comparison and of any later selection act.

## 26. Architecture Board decision — AD-012B

The Architecture Board accepts this decision by act **AD-012B** on **2026-08-05**, after Fable reviewed the complete comparison on exact head `ef07392d2a3d9c4f0f2d0e474849cf10b2592ec7`, found no defects and recommended merge. Codex independently accepted that verdict, Pavlo authorized the merge, and PR #63 was squash-merged with green post-merge CI.

This act selects semantic owners and representation roles. It does not define a freshness duration, ambiguity vocabulary or executable rule.

### 26.1 Freshness axis — F1

AD-012 selects **F1 — contract-local versioned freshness rule** as the positive freshness direction.

Freshness is use-relative. Each consuming normative contract that needs machine-derived temporal usability must own or exact-reference the rule for its own decision. Its separately reviewed activation must bind:

1. the protected consumer and exact use;
2. each evidence kind and exact evidence reference;
3. the temporal fact measured for each kind;
4. the exact evaluation time;
5. the exact rule identity and version;
6. all rule inputs and immutable snapshots;
7. cutoff equality, precision and incomparable-time behavior; and
8. the evaluator or deterministic rule authority.

No global duration, default timestamp or universal evidence lifetime is selected. OCP-004, OCP-006, OCP-011, OCP-012, OCP-013 and OCP-015 may therefore own different rules where their decisions differ. Shared field names do not make those rules interchangeable.

F0 remains the mandatory behavior for any consuming semantics that are not already governed by a narrow accepted local rule and have not completed an explicit F1 activation. In that scope, Core may preserve an attributable `stale` or equivalent statement and enforce non-permissive downstream handling, but it must not present the statement as machine-derived. This is a governed activation boundary, not a caller-selectable fallback.

OCP-004's accepted binding-change rule is a narrow pre-existing contract-local rule: it may mechanically classify prior explicit-intent validation evidence as stale after a substantive binding change. AD-012B neither downgrades that rule nor extends it to age, ObservationRecord, assessment evidence or claim support.

### 26.2 Ambiguity axis — A1

AD-012 separately selects **A1 — contract-local ambiguity rules** as the positive ambiguity direction.

Each activated consuming contract must name the dimensions it can decide, the exact rule and inputs for each dimension, and the non-permissive behavior for unresolved meaning. Reference ambiguity, lineage ambiguity, criterion ambiguity, temporal ambiguity, semantic-classification ambiguity and conflict remain distinct unless that contract explicitly governs their relationship.

Accepted Core structure may continue to detect finite defects such as zero or multiple exact-reference targets, duplicate identity, version mismatch, snapshot mismatch and invalid or unresolved lineage where the owning contract defines them. A1 does not authorize Core to infer semantic equivalence, contradiction or preference from text, labels, timestamps, record order, majority or count.

A0 remains the mandatory behavior outside an accepted A1 activation. Structural defects may be detected mechanically; semantic ambiguity remains an exact attributable statement and cannot yield a permissive downstream result. As with F1, implementations cannot silently opt into A1 because a convenient heuristic exists.

### 26.3 Accepted representation roles

The Board selects two explicit, non-competing roles:

- **inline consuming result for historical classification** — an activated immutable assessment or evaluation records the exact rule/profile, inputs, evaluation time and classification needed by the decision it protects; correction or supersession preserves history under that consuming contract; and
- **derived-only view for a new current query** — a selected deterministic rule may project usability from exact immutable inputs and an explicit query time without storing one standing `fresh` or `ambiguous` property on the evidence identity.

The roles do not select two authorities. The consuming contract owns both the historical result and any derived query semantics. A derived view must fail closed when its exact historical rule or inputs are unavailable and must never consult current repository state, latest rule versions or wall clock implicitly. A historical record never mutates merely because a later query classifies the same evidence differently.

A separate identified usability record is not accepted by this act. No demonstrated consumer needs independent reference, attribution or correction history beyond the consuming result, and a generic record would overlap OCP-011. If new evidence later justifies that role, it requires a separate Board reopening plus a full P-001 invocation or an explicit reviewed reason not to invoke P-001.

Domain-local representation is not selected because no concrete F3/A3 profile boundary has been demonstrated.

### 26.4 Alternatives and reopening gates

F2 and A2 remain conditional future directions. They may be reconsidered only after multiple accepted contract-local activations demonstrate the same stable obligation form and show that a Pattern reduces real normative drift without owning domain meaning, durations or comparison rules.

F3 and A3 may be reconsidered only when a concrete domain profile cannot be represented safely through an F1/A1 exact reference and a Core interoperability envelope has a demonstrated consumer. Unknown or mismatched profiles must remain non-permissive.

A global freshness field on an evidence identity remains inadmissible. Implementation convenience, repeated field names, one domain example or a desire to share code is not reopening evidence.

### 26.5 Downstream activation plan

AB-039 moves from `Discovery` to `Planned` for the first contract-local activation. OCP-011 is the first target because it already exact-binds criterion, evidence/input snapshots, evaluator and evaluation time and explicitly identifies `stale` and `ambiguous` as attributable until AB-039 supplies an owner.

That downstream OCP-011 cycle must, in one separately reviewed normative revision:

- define or exact-reference one complete F1 rule contract for its protected use;
- name the A1 dimensions it can actually decide and preserve attributable handling for every other semantic dimension;
- keep `stale` distinct from false evidence or a negative Objective conclusion;
- keep `fresh` distinct from truth, reliability, sufficiency, availability, Readiness and authorization;
- preserve exact historical replay and the inline/derived role split; and
- add outcome-appropriate executable fixtures for all applicable §23 pressures.

OCP-011 and OCP-012 versions and Accepted statuses do not change through AD-012B. Their current `stale`/`ambiguous` trust boundaries remain binding until each contract completes its own reviewed activation. OCP-012, OCP-006 and other consumers may later activate F1/A1 independently; one contract's rule never becomes their default.

AB-039 may move from `Planned` to `Resolved` when the first complete OCP-011 activation is accepted with executable evidence. Unactivated consumers remain explicitly under F0/A0 after that accounting transition and require their own reviewed amendment before claiming machine-derived semantics.

### 26.6 Accepted effect and exclusions

AD-012B has the following narrow effects:

- AD-012 becomes `Accepted` at version `0.3.0`;
- F1 and A1 become the selected positive owner models;
- F0 and A0 remain mandatory per-contract behavior wherever no narrow accepted local rule or separately accepted activation exists;
- inline historical classification and derived-only current projection are selected as distinct representation roles;
- AB-039 moves `Discovery → Planned` for the first OCP-011 activation; and
- the comparison, authority accounting and twenty counterexample obligations in §§17–24 remain binding guidance for every activation.

This act does not create a Concept, Pattern, record family, P-001 invocation, domain profile, rule identifier, duration, time ontology, ambiguity code, schema, checker derivation, fixture or graph edge. It does not reopen AD-011 R0, define Readiness, verify Capability possession, change Resource identity, grant authorization or decide source reliability.

Newest timestamp, record order, source count, evaluator count, claimant count, caller identity and current wall clock remain forbidden substitutes for authority.

This selection takes effect only through squash merge after exact-head Fable approval, Codex adjudication, green CI and explicit Pavlo or Architecture Board authorization. Until that merge, the PR carrying §26 is a proposed Board act.
