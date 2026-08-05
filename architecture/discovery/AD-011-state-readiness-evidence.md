---
Decision-ID: AD-011
Title: State and Readiness Evidence Boundary
Version: 0.3.0
Status: Accepted
Owner: Architecture Board
Depends-On: AD-002, ADR-DRAFT-007, OCP-003, OCP-004, OCP-005, OCP-006, OCP-007, OCP-010, OCP-011, OCP-012, OCP-013
Applies-To: AB-007, State, Readiness
Review-After: A separately accepted mandate supplies new State identity evidence or a concrete Readiness consumer with legitimate criterion, target and freshness owners
---

# AD-011 — State and Readiness Evidence Boundary

## 1. Trigger and accepted mandate

AD-002 accepted the evidence contract and guardrails for a later State and Readiness decision. The roadmap names that later decision as the first successor cycle after accepted Capability claims and accepted outcome assessments exist. Those prerequisites now exist in OCP-012 and OCP-011.

This discovery opens only that later decision. It does not reopen the accepted semantics of Operation, Assignment, Constraint, Organization, Event, OutcomeAssessmentRecord, CapabilityClaimRecord or Resource interchangeability. It also does not assume that `State` and `Readiness` must share one identity, one record family or one authority.

Revision `0.1.0` introduces no new Concept, schema, lifecycle value, result vocabulary, graph edge, validator or production contract. Its purpose is to make the competing outcomes and the evidence needed to separate them reviewable in human-readable form.

## 2. Decision questions

The State axis asks:

> Is there one independently identifiable Core subject called `State`, or are current state-like facts already better represented by local lifecycle histories, time-bounded observations, assessments and derived projections?

The Readiness axis asks:

> Does a concrete consumer need a governed, replayable preparedness conclusion for one exact subject, context and time, and if so is that conclusion a fundamental Concept, an attributable assessment, a constrained pattern or a domain-owned result?

The axes must be decided separately. Rejecting a generic State Concept does not reject a future governed Readiness conclusion. Accepting a constrained representation for Readiness does not create a universal State superclass.

## 3. Accepted evidence now available

The review may consume the following accepted contracts without expanding their authority:

- OCP-004 records Operation lifecycle through local transition history. A lifecycle stage is not fundamental State and does not establish success or Readiness.
- OCP-005 records Assignment lifecycle and separately derives temporal effectivity and participation. An `Established` or effective Assignment does not establish availability, Capability, authorization or Readiness.
- OCP-006 evaluates exact Constraint contexts and derives admissibility. `admissible` means that the governed Constraint set does not block that exact candidate context; it does not mean ready.
- OCP-007 supplies stable Organization identity. It does not make an Organization the same subject as its Resources or organizational units.
- OCP-010 separates Event occurrence identity from attributable observations. An occurrence or observation is not current State or Readiness by implication.
- OCP-011 supplies attributable, snapshot-bound OutcomeAssessmentRecord semantics for an exact Objective target. It is not a generic assessment container, mutable target state or accepted Readiness profile.
- OCP-012 supplies an attributable CapabilityClaimRecord for one exact Resource and Capability version. The claim proves only that the claimant made the recorded claim under the recorded authority and provenance.
- OCP-013 derives contextual Resource eligibility from an exact consumer requirement, effective claims and Constraint decision. A positive eligibility result is not availability, authorization, selection or Readiness.

These contracts provide more evidence than AD-002 had when its mandate was accepted. They also expose gaps that must not be hidden by a generic `state` or `ready` field.

## 4. Terms that must remain distinct

| Term | Narrow meaning in the accepted foundation | Not established by that term |
|---|---|---|
| lifecycle stage | local projection of one subject's authoritative transition history | universal State, success or preparedness |
| temporal effectivity | whether one governed record applies at time `t` | availability, Readiness or authorization |
| participation | exact Resource–Operation participation derived through an effective Assignment | suitability, capacity or permission to act |
| observation | attributable statement about an occurrence or condition | accepted truth, current State or Readiness |
| assessment | attributable conclusion under an exact target, criterion, evidence snapshot and evaluator | mutable target property or universal truth |
| Capability claim | attributable claim about one Resource and exact Capability definition | verified capability, availability or preparedness |
| admissibility | outcome of applicable Constraint evaluation for one exact context | positive Readiness, selection or authorization |
| eligibility | directional consumer-owned result for one exact Resource requirement | availability, ranking, selection or replacement |
| availability | whether a subject may actually be considered for use at a time | not defined by this discovery; remains a separate future decision |
| Readiness | candidate preparedness conclusion whose identity and authority remain under review | a synonym for any one accepted input above |
| operational State | candidate abstraction for condition over time whose independent identity remains unproved | a generic container for unrelated enums |
| authorization | permission from a separately governed authority | derivable from evidence count or positive inputs |

Conceptual explanations and examples must remain understandable without checker code. Executable evidence may later test an accepted rule, but it cannot decide the ontology boundary.

## 5. Independent-identity tests

A fundamental Concept outcome is admissible only if it answers all of these questions without relying on a generic container:

1. What stable identity persists when a value, observation, evaluator, criterion, context or time changes?
2. What proposition is the Concept authoritative about?
3. Which actor or contract owns creation, correction and supersession?
4. Why are existing lifecycle records, observations, assessments or projections insufficient?
5. Which other artifacts need to reference this identity independently of its subject and evidence?
6. How do two simultaneous but context-specific conclusions avoid becoming contradictory values of one global property?
7. How are history and replay preserved without treating the latest timestamp, list order or source count as authority?

If the only identity is a subject plus a criterion, context, time and evidence snapshot, the candidate may be an assessment or derivation rather than a fundamental Concept. If the only identity is a local lifecycle stage, it remains owned by that lifecycle.

## 6. State-axis candidates

### S0 — no shared State abstraction

Each accepted owner keeps its local lifecycle, observations, assessments and projections. Consumers name the exact source rather than translating unrelated values into a universal State.

S0 adds no shared identity or vocabulary. It is the fail-safe outcome if no cross-owner consumer demonstrates a conclusion that cannot be expressed through exact existing records.

### S1 — constrained state-like record pattern

Core defines a reusable set of obligations for any state-like identified record: exact subject and state-kind ownership, temporal applicability, provenance, authoritative history, correction and fail-safe projection. Each invoking specification owns its vocabulary and meaning.

S1 is a pattern, not a fundamental State Concept. It is admissible only if repeated accepted record contracts need the same obligations and the pattern does not turn local lifecycle values into members of one universal taxonomy. This discovery does not invoke P-001 or define another pattern.

### S2 — fundamental State Concept

State has stable identity independent of its subject, exact semantics shared across consumers and a justified cross-domain reference need. Local lifecycle stages, observations and assessments would remain separate evidence or inputs.

S2 carries the highest burden. A common word, an enum field or a desire for one dashboard filter is not independent identity. The candidate must explain why multiple contextual conclusions about one subject are not merely separate assessments or records.

## 7. Readiness-axis candidates

### R0 — no shared Readiness authority

Consumers display exact Capability claims, Constraint decisions, assignments, observations and assessments separately. They may make local workflow decisions, but Foundation emits no canonical `ready` conclusion.

R0 is a complete no-new-authority control, not a placeholder for a future boolean field.

### R1 — governed readiness assessment profile

A separately accepted contract defines an attributable preparedness assessment for one exact subject, context, criterion, evidence/input snapshots, evaluation time, evaluator and versioned rule. The result remains an assessment and does not mutate its target.

OCP-011 is evidence that such a shape can be fail-safe, but its accepted target is Objective and its accepted vocabulary is not a universal readiness vocabulary. R1 therefore requires a separately reviewed extension or sibling contract; AD-011 cannot silently reuse the OCP-011 result vocabulary for Resource or Organization.

### R2 — domain-owned Readiness with a Core interoperability envelope

Each domain owns its Readiness criteria and conclusions. Core defines only exact subject/context binding, provenance, snapshot, replay and cross-domain rejection rules.

R2 is admissible only if unknown domain meanings fail closed and a consumer cannot compare or aggregate domain results merely because both use the word `ready`.

### R3 — fundamental Readiness Concept

Readiness has independent stable identity, continuity and cross-domain authority that cannot be represented as a governed assessment or domain result. It remains explicitly contextual and time-bound.

R3 must prove why preparedness is an entity rather than an attributable conclusion. It must not become a mutable property bag or a universal superclass for availability, health, admissibility and lifecycle.

## 8. Mapping to the AD-002 outcomes

AD-002 named four candidate outcomes. AD-011 expands them without changing their meaning:

| AD-002 outcome | AD-011 comparison |
|---|---|
| separate State and Readiness Concepts | S2 + R3, with independent identity proved for each |
| one Concept plus a derived view | S2 with non-Concept Readiness, or R3 with local state-like projections; the direction must be explicit |
| domain-specific models rather than Core Concepts | S0 with R2, or another explicit no-Core-Concept combination |
| Constraint and time-bounded observations as the primary representation | S0 with R0 or R1; neither Constraint nor observation alone becomes Readiness |

An unspecified blend is not a decision. The Board act must name one S outcome and one R outcome and explain their interaction.

## 9. Required Resource example

Consider one non-sensitive Resource at one evaluation time:

- an effective OCP-012 record contains a positive attributable Capability claim;
- OCP-013 returns `positive` for one exact consumer requirement;
- the applicable OCP-006 Constraint set is `admissible`;
- an inspection ObservationRecord exists, but its freshness for the proposed use is not governed;
- no accepted availability, capacity, reservation or authorization conclusion exists.

The evidence may support a consumer review. It cannot produce a Foundation-authoritative `ready` conclusion under the current contracts. A candidate that returns `ready` from the claim, eligibility or admissibility result alone fails the AD-002 guardrails.

A positive-capable Readiness outcome must additionally name the exact preparedness criterion, context, evaluation time, evidence and input snapshots, evaluator or rule authority, evidence state and historical replay behavior. It must show which missing or conflicting input prevents a positive conclusion.

## 10. Required Organization example

Consider one Organization with relationships to several Resources:

- OCP-007 preserves the Organization's identity;
- one related Resource has a positive Capability claim and another has no effective claim;
- the Organization-to-Organizational-Resource boundary and direct Organization Capability-claim semantics remain unresolved under AB-006 and AB-052;
- no accepted rule says which Resources, roles, authorities or evidence constitute organizational preparedness.

The Organization is not ready merely because one related Resource has a positive claim or eligibility result. Resource evidence cannot be aggregated, inherited or transferred to Organization identity without a separately accepted mapping and criterion owner.

Any candidate unable to represent this example without inventing composition, holder mapping or aggregation authority must remain non-positive. AD-011 does not resolve AB-006, AB-047 or AB-052.

## 11. Mandatory counterexamples

External review must test every candidate against at least these cases:

1. A Resource has an effective positive Capability claim but the claim is attributable rather than independently verified.
2. A candidate context is `admissible`, but no availability or preparedness evidence exists.
3. An Assignment is `Established` and effective, but the Resource is unavailable or its evidence is stale.
4. An Operation is `Active` or `Completed`, but its lifecycle stage does not establish successful outcome or Readiness.
5. A recent Event or ObservationRecord is treated as current condition without a governed freshness rule.
6. Absence of negative evidence is treated as positive Readiness.
7. Two evaluators reach different conclusions from explicitly different criteria or snapshots.
8. Two contextual Readiness conclusions for the same subject and time differ without being globally contradictory.
9. A superseding assessment is selected by newest timestamp or list order rather than explicit history.
10. Resource evidence is inherited by an Organization or sibling Resource without an accepted mapping.
11. A positive eligibility result authorizes, selects, reserves or assigns the Resource.
12. A lifecycle value from one Concept is translated into a generic State vocabulary and reused by another Concept with different semantics.
13. An unknown domain Readiness code is treated as comparable to a known Core or domain code.
14. Missing, stale, ambiguous or conflicting evidence is collapsed into either `ready` or a durable negative claim.
15. One global `state` field overwrites simultaneous health, lifecycle, availability and preparedness conclusions owned by different authorities.

Each positive-capable candidate must state which exact rule rejects or safely contains each case. R0 and S0 must show that their absence of shared authority is operationally honest rather than a hidden caller-local positive path.

## 12. Evidence and authority matrix

| Input or conclusion | Current owner | Permitted contribution | Forbidden upgrade |
|---|---|---|---|
| Operation lifecycle | OCP-004 | exact local lifecycle fact and history | universal State, success or Readiness |
| Assignment effectivity and participation | OCP-005 | exact contextual participation at time `t` | availability, suitability or preparedness |
| Constraint decision | OCP-006 | admissibility for one bound context | positive Readiness or authorization |
| Organization identity and relationships | OCP-007 plus local relationship owners | exact subject and explicit relation evidence | inherited Resource claims or aggregate Readiness |
| Event and ObservationRecord | OCP-010 | occurrence and attributable evidence | truth, current State or freshness |
| OutcomeAssessmentRecord | OCP-011 | exact Objective assessment under accepted kinds | generic target assessment or mutable State |
| CapabilityClaimRecord | OCP-012 | attributable Resource claim | verified possession or Readiness |
| Resource eligibility | OCP-013 and its governed consumer requirement | directional requirement satisfaction | availability, selection or Readiness |
| freshness and deterministic replay semantics | AB-039, still open | future owner of machine-verifiable stale/ambiguous handling | assumed recency threshold in AD-011 |
| authorization, reservation and allocation | AB-017 and AB-025 | future independently governed decisions | inferred from Readiness evidence |

No source count, evaluator count, label match, latest-version lookup, newest timestamp or list order may replace an explicit authority.

## 13. Fail-safe and replay requirements

Any positive-capable shared Readiness outcome must, at minimum, bind:

```text
exact subject kind and reference
readiness kind and version
exact consumer context and criterion
evaluation time or interval
evidence bindings and immutable evidence snapshot
input snapshot
evaluator or deterministic rule authority
evidence state
attributable conclusion
evaluation and recording times
provenance
correction or supersession history
```

The list is an obligation set, not an accepted schema.

Until AB-039 defines machine-verifiable freshness and deterministic replay semantics, AD-011 must not claim that the checker can independently prove a dynamic input `fresh` or detect every `stale` or `ambiguous` case. An attributable evaluator may record such an evidence state under a future selected contract, but that is not the same as automatic Foundation truth.

Changing the subject, context, criterion, evaluation time, evidence snapshot, input snapshot, evaluator or rule version creates a different conclusion context. A prior conclusion must not silently migrate or overwrite history.

## 14. Candidate-separating questions for external review

Fable should attempt to determine:

1. whether any demonstrated consumer needs an independently referenced State identity rather than exact source records;
2. whether S1 has enough repeated cross-artifact need to justify a pattern without becoming a generic container;
3. whether Resource Readiness can be represented as an assessment while keeping Capability, eligibility, availability and authorization separate;
4. whether any accepted consumer currently owns a Readiness criterion and positive result;
5. whether R1 can reuse OCP-011 machinery without diluting its Objective-specific accepted contract;
6. whether Organization Readiness is decision-separable before AB-006 and AB-052 resolve holder and mapping semantics;
7. whether R2 can support cross-domain exchange while rejecting unknown meanings;
8. whether S2 or R3 has independent identity evidence beyond naming convenience;
9. whether all fifteen counterexamples are fairly handled by every applicable candidate; and
10. whether the document remains understandable without executable checker rules.

If the evidence cannot distinguish candidates on one axis, that axis must remain in `Discovery` even if the other axis is ready for a verdict.

## 15. Working hypotheses, not selections

S0 is the current no-new-authority baseline because accepted lifecycle histories, observations, assessments and projections already preserve their own semantics and no demonstrated consumer requires a shared State identity. S1 is the least-authority positive alternative if repeated record obligations justify a reusable pattern.

R1 is the leading positive-capable hypothesis because Readiness appears to be a contextual, attributable preparedness conclusion rather than an independently persistent entity. That hypothesis is blocked from selection until a concrete consumer, criterion owner, target contract and freshness/replay boundary are explicit. R0 remains the honest current behavior wherever those inputs are absent.

S2, R2 and R3 remain reviewable alternatives. This ordering does not pre-approve a pattern, an OCP-011 extension, a domain envelope or a Readiness result.

## 16. Discovery status and accounting

AD-011 opens AB-007 in `Discovery` for the subsequent decision required by accepted AD-002. State and Readiness remain `Deferred` as Concepts while this comparison is active.

Revision `0.1.0` does not modify Concept statuses, ADR-DRAFT-007, any accepted OCP contract, the Foundation map, schemas, checker rules or fixtures. It also does not resolve availability, health, authorization, reservation, capacity, Organization composition or Conflict.

The next revision may compare externally reviewed findings and propose separate S and R verdicts. Acceptance still requires exact-head Fable approval, Codex adjudication, green CI and explicit Pavlo or Architecture Board authorization before squash merge.

## 17. Comparison method and verdict vocabulary

This revision compares the two axes for external review. It does not select a State outcome, a Readiness outcome, a combined pair, a result vocabulary or a new artifact.

The comparison follows four rules:

1. S0 and R0 are complete no-new-authority controls, not unfinished implementations.
2. State identity and Readiness conclusion authority are evaluated separately.
3. A positive-capable outcome must name every owner and fail-safe input it adds; implementation convenience is not evidence.
4. Every candidate is tested against the same human examples and all fifteen counterexamples in §11, using evidence appropriate to that candidate.

The working verdicts below mean:

- **admissible control** — safe and complete when no shared authority is justified;
- **leading hypothesis** — the smallest currently plausible positive-capable direction, still subject to explicit evidence gates;
- **conditional alternative** — admissible only when a concrete consumer demonstrates the extra authority it needs; and
- **not supported by current evidence** — the candidate may remain reviewable, but the present repository cannot justify selecting it.

These are comparison verdicts for falsification. They are not Architecture Board selections.

## 18. State-axis comparison

The State axis asks whether Core needs a shared independently identifiable subject, a reusable record discipline or neither.

| Outcome | Plain-language effect | Added authority | Main benefit | Main risk | Separate working verdict |
|---|---|---|---|---|---|
| S0 — no shared State abstraction | Consumers name the exact lifecycle, observation, assessment or projection they mean. | None. | Preserves the accepted owner and meaning of every source. | Consumers cannot use one generic Core field for unlike facts. | **Admissible control and current default.** No demonstrated consumer needs a shared State identity. |
| S1 — constrained state-like record pattern | An invoking specification may reuse obligations for identity, time, provenance, history and fail-safe projection while owning its own vocabulary. | Only the invoking specification's existing record authority; the Pattern adds obligations, not meaning. | Could remove repeated governance text without creating a universal taxonomy. | A broad Pattern may become a generic container or silently translate local lifecycle values. | **Conditional alternative.** Repeated accepted invocations must first prove a stable common obligation set. |
| S2 — fundamental State Concept | State would have identity independent of its subject and be referenced across domains. | A new Core Concept and its owner. | Could support genuine cross-domain references if an independent subject exists. | A label or dashboard field can masquerade as identity and overwrite simultaneous facts owned by others. | **Not supported by current evidence.** No stable independent identity, continuity or cross-domain reference need has been demonstrated. |

### 18.1 State decision-separating evidence

External review should ask:

- Can a consumer requirement be expressed only by referencing a State identity, rather than the exact source record and context?
- Which value changes while that alleged identity persists?
- Which accepted record contracts repeat exactly the same obligations strongly enough to justify S1?
- Can S1 prohibit vocabulary translation and still be useful?
- Can S2 represent simultaneous lifecycle, condition and preparedness conclusions without turning them into competing values of one property?

S0 remains correct when those questions have no evidence-backed answer. S1 is not justified by similar field names alone. S2 requires new independent-identity evidence, not a stronger preference for a shared UI vocabulary.

## 19. Readiness-axis comparison

The Readiness axis asks whether Core needs a governed preparedness conclusion and, if so, which narrow owner can state it.

| Outcome | Plain-language effect | Added authority | Main benefit | Main risk | Separate working verdict |
|---|---|---|---|---|---|
| R0 — no shared Readiness authority | Consumers inspect exact inputs and make their own separately governed decisions; Foundation emits no canonical ready conclusion. | None. | Honest whenever no consumer, criterion or freshness authority exists. | Callers may invent incompatible local booleans and present them as Core Readiness. | **Admissible control and current behavior.** It remains binding wherever positive prerequisites are absent. |
| R1 — governed readiness assessment profile | A named evaluator or rule states one attributable preparedness conclusion for an exact subject, context, criterion, snapshots and time. | Only the exact assessment conclusion selected by a separately accepted contract. | Smallest positive-capable shape; keeps the conclusion contextual and non-mutating. | A generic profile may dilute OCP-011 or collapse Capability, availability, admissibility and authorization into ready. | **Leading hypothesis**, but **not yet selectable**: no concrete consumer, criterion owner, target contract or accepted freshness/replay boundary is complete. |
| R2 — domain-owned Readiness with Core envelope | A named domain owns meaning while Core governs exact bindings and mismatch rejection. | The domain owns only its exact versioned result. | Preserves legitimate domain-specific preparedness semantics. | Identical labels may hide incompatible criteria and invite invalid cross-domain comparison. | **Conditional alternative.** It needs at least two concrete profiles or one demonstrated interoperability boundary. |
| R3 — fundamental Readiness Concept | Readiness would be an independently persistent Core entity rather than a conclusion. | A new Core Concept and cross-domain authority. | Could support independent references if preparedness itself has durable identity. | An assessment is reified as an entity, or one global property absorbs unrelated evidence and authorities. | **Not supported by current evidence.** Existing evidence points to a contextual conclusion, not an independently persistent subject. |

### 19.1 Readiness decision-separating evidence

External review should ask:

- Which concrete consumer needs a shared conclusion rather than the exact OCP-006, OCP-011, OCP-012 and OCP-013 inputs?
- Who owns the preparedness criterion and the rule or evaluator authority?
- Is the target one Resource, an Organization, another subject or a domain-specific aggregate?
- Which exact missing, stale or conflicting input blocks a positive result?
- Can a domain result be exchanged without treating unlike meanings as comparable?
- What persists independently if R3 is claimed to be a Concept rather than an assessment?

R1 is the smallest plausible positive model because its conclusion remains attributable and contextual. It is deliberately blocked: AB-039 still owns freshness and replay semantics, while Organization targets additionally depend on AB-006 and AB-052. R0 is therefore not temporary permissiveness; it is the current fail-safe result wherever those owners are absent.

## 20. Axis independence and pair behavior

No S/R pair is selected by this comparison. The following combinations illustrate why the axes cannot decide one another:

- **S0 + R0** is the current safe behavior: exact source records remain authoritative and Foundation emits no shared preparedness conclusion.
- **S0 + R1** could later support a governed readiness assessment without creating a generic State abstraction.
- **S1 + R0** could standardize repeated record obligations while still declining to create any Readiness authority.
- **S1 + R1** would require two separate acceptance arguments: repeated record-pattern need and a concrete preparedness contract.
- **S2 + any R outcome** still needs independent State identity evidence; a Readiness conclusion cannot supply it.
- **any S outcome + R2/R3** still needs its own domain or identity evidence; State vocabulary cannot supply a criterion owner.

A proposed pair fails if changing State representation changes the meaning of Readiness, or if a Readiness conclusion becomes authority for lifecycle, availability, authorization or a generic State value.

### 20.1 Current Resource and Organization behavior

For the Resource example in §9, every S outcome must preserve the exact accepted inputs. Under R0 there is no governed readiness conclusion. R1–R3 must remain non-positive until the missing freshness, criterion and authority inputs are supplied.

For the Organization example in §10, every R outcome remains non-positive until an accepted Organization-to-Resource mapping and organization-level criterion exist. S1 or S2 cannot be used to aggregate Resource evidence, and R2 cannot invent a domain profile merely because an Organization groups Resources.

## 21. Normative authority accounting

“Unselected” below is an explicit evidence gap, not permission for an implementation to choose an owner.

| Binding or conclusion | Current or candidate owner | Fail-safe obligation |
|---|---|---|
| Subject identity | Existing Concept owner; any future R1/R2 contract must exact-bind subject kind and reference | Resource and Organization identities never collapse; an unresolved subject cannot yield a positive conclusion. |
| Lifecycle history | OCP-004 or OCP-005 for its own subject | Local stages are not translated into shared State or Readiness values. |
| Observations and occurrence evidence | OCP-010 record authors and Event identity | Observation count, age or existence does not establish freshness or truth by itself. |
| Objective assessment | OCP-011 evaluator under its accepted target and vocabulary | It cannot be silently retargeted to Resource or Organization Readiness. |
| Capability claim | OCP-012 claimant | Attribution does not become verified possession, availability or preparedness. |
| Admissibility | OCP-006 evaluator for one exact context | `admissible` does not become positive Readiness or authorization. |
| Eligibility | OCP-013 rule plus its governed consumer requirement | `positive` remains directional requirement satisfaction, not Readiness. |
| Availability | **Unselected** | Absence of a blocking fact cannot manufacture availability. |
| Preparedness criterion | **Unselected** for a shared R1–R3 conclusion | No positive-capable candidate may infer it from labels or existing result vocabulary. |
| Freshness and deterministic replay | AB-039, unresolved | Newest timestamp and caller-local age thresholds are not authority. |
| Readiness evaluator or rule | **Unselected** | Caller identity, source count or an implementation default cannot choose the conclusion. |
| Organization composition and holder mapping | AB-006 and AB-052 | Resource evidence is not inherited or aggregated into Organization identity. |
| Authorization, reservation and allocation | AB-017 and AB-025 | No State or Readiness result grants action authority. |

## 22. Mandatory counterexample mapping

Every row maps the complete §11 pressure to both axes. A range such as S0–S2 or R0–R3 means every candidate on that axis must provide the stated behavior.

| # | Pressure | State-axis required behavior | Readiness-axis required behavior | Future executable-evidence owner |
|---|---|---|---|---|
| 1 | Positive Capability claim is attributable, not independently verified | **S0–S2:** preserve the claim as its exact source; do not materialize generic possessed State. | **R0:** no conclusion. **R1–R3:** non-positive unless the selected criterion explicitly and legitimately accepts that evidence state. | OCP-012 compatibility plus any selected R contract. |
| 2 | `admissible` exists without availability or preparedness evidence | **S0–S2:** retain only the OCP-006 contextual decision. | **R0:** no conclusion. **R1–R3:** missing required inputs is non-positive. | OCP-006 compatibility plus selected R contract. |
| 3 | Assignment is effective while Resource evidence is stale or unavailable | **S0–S2:** Assignment history remains separate from condition evidence. | **R0:** no conclusion. **R1–R3:** stale or missing inputs cannot yield positive. | OCP-005 plus AB-039 and selected R contract. |
| 4 | Operation is Active or Completed without proven success or preparedness | **S0–S2:** local lifecycle is not universal State. | **R0–R3:** no readiness result follows from Operation stage. | OCP-004 and selected R contract. |
| 5 | Recent observation is treated as current condition without freshness rule | **S0:** expose exact observation only. **S1/S2:** no current-state projection without an accepted rule. | **R0:** no conclusion. **R1–R3:** non-positive until AB-039-owned semantics are bound. | OCP-010, AB-039 and any selected positive contract. |
| 6 | Absence of negative evidence becomes positive Readiness | **S0–S2:** absence does not create a state fact. | **R0:** no conclusion. **R1–R3:** positive requires explicit sufficient inputs; closed-world inference is forbidden. | Every selected R contract. |
| 7 | Evaluators differ because criteria or snapshots differ | **S0–S2:** preserve both contextual records; do not pick a global State winner. | **R0:** report no shared conclusion. **R1–R3:** bind each conclusion to its exact criterion and snapshot. | OCP-011 precedent plus selected R contract. |
| 8 | Contextual readiness conclusions differ for the same subject and time | **S0–S2:** do not collapse them into one global property. | **R1–R3:** different exact contexts may legitimately differ; R0 emits none. | Selected R contract. |
| 9 | Newest timestamp or list order selects a superseding assessment | **S0–S2:** only explicit governed history may select a head. | **R1–R3:** invalid or ambiguous lineage is non-positive; R0 emits none. | P-001 invocation if selected, plus the owning OCP. |
| 10 | Resource evidence is inherited by Organization or sibling Resource | **S0–S2:** preserve separate identities and exact relation evidence. | **R0–R3:** no transfer or aggregation without AB-006/AB-052 contracts. | OCP-007, AB-006, AB-052 and selected R contract. |
| 11 | Eligibility is reused as authorization, selection, reservation or Assignment action | **S0–S2:** no state-like representation adds those authorities. | **R0–R3:** reject forbidden coupling even if a readiness conclusion is positive. | OCP-013 compatibility, AB-017, AB-025 and AB-028 boundaries. |
| 12 | One lifecycle vocabulary is translated into generic State and reused elsewhere | **S0:** exact source vocabulary only. **S1:** Pattern must reject semantic translation. **S2:** Concept must prove shared meaning rather than label similarity. | **R0–R3:** translated State labels are not readiness evidence by default. | Every selected S1/S2 owner and selected R contract. |
| 13 | Unknown domain Readiness code is treated as comparable | **S0–S2:** State representation cannot normalize domain meaning. | **R2:** exact profile mismatch fails closed. **R1/R3:** unknown vocabulary is non-positive. **R0:** no conclusion. | R2 Core envelope and every participating domain profile. |
| 14 | Missing, stale, ambiguous or conflicting evidence becomes ready or durable negative | **S0–S2:** preserve the evidence gap rather than a global State. | **R1–R3:** return non-positive indeterminate or an explicitly owned review route; R0 emits none. | AB-039 plus every selected R contract. |
| 15 | One global `state` overwrites health, lifecycle, availability and preparedness | **S0:** no global field. **S1:** Pattern keeps vocabularies owner-scoped. **S2:** must prove independent identity and simultaneous-context behavior. | **R0–R3:** Readiness remains a separate conclusion and cannot overwrite other layers. | Every selected S/R normative owner. |

## 23. Executable-evidence plan by candidate

This comparison does not add checker code. It assigns evidence to the normative owner that would exist only after an outcome is selected.

| Candidate | Required downstream evidence |
|---|---|
| S0 | Compatibility regression showing exact lifecycle, observation, assessment and projection sources remain distinct and no generic State field is emitted. |
| S1 | A separately reviewed Pattern invocation suite proving owner-scoped vocabulary, exact subject/kind binding, effectivity, provenance, history and rejection of cross-owner translation. |
| S2 | A separate Concept cycle proving identity, lifecycle, reference consumers, simultaneous-context behavior and Concept-graph effect before any schema or fixture is accepted. |
| R0 | Compatibility regressions showing that positive claims, admissibility, eligibility, effectivity and observations do not manufacture a readiness result. |
| R1 | A separately accepted assessment contract with exact target, criterion, context, snapshots, evaluator/rule, evidence states, effectivity, provenance, history and all applicable §22 cases. |
| R2 | A Core envelope plus each named domain profile, with exact domain/version binding, unknown-profile rejection and cross-domain mismatch fixtures. |
| R3 | A separate Concept cycle proving independent identity and continuity before any positive result contract or graph edge is added. |

If S0 or R0 is later selected, no placeholder schema, record family or checker module is created merely to make the control appear implemented.

## 24. Comparison status and next decision gate

Revision `0.1.0` opened AD-011 and AB-007. Fable reviewed its exact head in two iterations, found one wording defect in the availability boundary, and approved the corrected discovery with green CI. Codex accepted the finding and recommendation; Pavlo authorized the PR; the discovery was squash-merged without changing any Concept status.

Revision `0.2.0` supplies the separate S and R comparisons, pair behavior, authority accounting, complete counterexample map and executable-evidence ownership. It remains `Discovery` and records no Architecture Board selection.

External adversarial review must now determine separately:

1. whether current evidence supports S0, S1 or S2;
2. whether current evidence supports R0, R1, R2 or R3, or leaves the axis in Discovery;
3. whether R1 is fairly treated as a leading but presently blocked hypothesis;
4. whether S0 and R0 are full controls rather than hidden caller-local positive paths;
5. whether all fifteen counterexamples are fairly mapped to every applicable candidate; and
6. whether the comparison remains understandable without checker code.

A later Board act must name one outcome per decidable axis. It may select a control, select a positive-capable outcome only with its missing owners resolved, or keep one axis in `Discovery` while deciding the other. The Board act may not create a Pattern, OCP contract, Concept, schema, checker rule or graph edge merely by selecting a direction.

Exact-head Fable approval, Codex adjudication, green CI and explicit Pavlo or Architecture Board authorization remain mandatory before squash merge of this comparison and of any later selection act.

## 25. Accepted axis selections

The Architecture Board records two independent no-new-authority outcomes. Selecting them together does not make State and Readiness one decision or one model.

### 25.1 State axis — S0

AD-011 selects **S0 — no shared State abstraction**.

The reviewed evidence shows no stable State identity that persists independently of a subject, local lifecycle, observation, assessment, criterion, context or time. No demonstrated consumer needs to reference one shared State subject instead of the exact accepted source record. Simultaneous lifecycle, condition, availability and preparedness statements remain owned by different contracts and cannot be reduced to values of one global property.

S1 is not selected because the repository has not demonstrated a repeated set of accepted state-like record invocations that justifies another Pattern without creating a generic container. S2 receives a negative independent-identity verdict under the current evidence.

Under S0, each accepted owner keeps its own lifecycle, observation, assessment and projection vocabulary. The word `state` may still be used descriptively or inside an explicitly owned local contract; that use does not create a shared foundation Concept or translate one owner's vocabulary into another's.

### 25.2 Readiness axis — R0

AD-011 separately selects **R0 — no shared Readiness authority**.

The reviewed evidence contains no concrete consumer requirement, accepted preparedness criterion owner, accepted Resource or Organization target contract, readiness evaluator or rule owner, availability contract, or complete freshness/replay boundary. Capability claims, admissibility, eligibility, Assignment effectivity, observations and assessments therefore cannot manufacture a Foundation-authoritative `ready` conclusion.

R1 remains the smallest plausible positive-capable direction but is not accepted by this act. It may be reconsidered only after a separate mandate names the concrete consumer, exact conclusion, criterion owner, target contract and evaluator/rule authority and binds the required AB-039 freshness/replay semantics. Organization targets additionally require the AB-006/AB-052 mapping boundary. R2 has no demonstrated domain profiles or interoperability pressure. R3 receives a negative independent-identity verdict under the current evidence.

Under R0, consumers may inspect exact accepted inputs and make decisions under their own separately governed authority. They may not expose a caller-local boolean as Core Readiness or infer it from absence of negative evidence.

### 25.3 Independent reopening

Either axis may be reopened without reopening the other. Reopening requires a separately accepted mandate and new decision-separating evidence:

- State reopening must demonstrate stable independent identity, an owner and a real cross-contract reference consumer that exact source records cannot satisfy.
- Readiness reopening must name a concrete consumer, exact preparedness conclusion and legitimate owners for its criterion, target, inputs, freshness/replay and evaluator or rule.

Implementation convenience, a dashboard field, a familiar label, a caller-local threshold or a new data source is not sufficient reopening evidence.

## 26. Concept registry effect

AD-002 kept State and Readiness `Deferred` only until a later evidence-based decision selected or rejected the candidates. AD-011 is that decision.

Because S0 and R0 reject shared foundation authority and S2/R3 fail the independent-identity test, `State` and `Readiness` are removed from the active OCP-000 Concept registry and generated Foundation map. This is not a transition to `Accepted`, `Deprecated` or `Archived`; both candidates are deregistered after negative current-scope identity and authority verdicts.

The removal does not ban the words `state`, `readiness`, `ready`, `condition` or `status`. It prevents an unowned local field or conclusion from masquerading as a registered Core Concept. Accepted local lifecycle stages, observations, assessments and projections retain their exact owners and meanings.

The non-normative future edges `Operation ⇢ State` and `Resource ⇢ Readiness` are removed. AD-011 supersedes ADR-DRAFT-007, which moves from `Draft` to `Superseded` and remains preserved as historical discovery material without current ontology authority.

## 27. Accepted effect

This selection has the following narrow effect:

- AD-011 is `Accepted` at version `0.3.0` with S0 and R0 recorded separately;
- AB-007 is `Resolved` for the current evidence;
- State and Readiness are deregistered as Concept candidates without creating replacement Concepts;
- OCP-000 and OCP-002 stop presenting State or Readiness as active registry or taxonomy questions;
- OCP-004, OCP-005 and OCP-006 retain their accepted local meanings while removing stale `Deferred` registry labels;
- the S0 and R0 compatibility obligations in §§20–23 remain binding guidance for consumers;
- R1 remains a gated future direction, not an accepted assessment profile, result vocabulary or positive authority; and
- no Pattern, OCP record contract, schema, checker derivation, result vocabulary or Concept graph edge is introduced.

Availability, freshness/replay, Organization composition, authorization, reservation, allocation and Assignment execution remain owned by their separate backlog and accepted-contract boundaries. Newest timestamp, list order, evaluator count, source count or caller identity cannot supply any missing authority.

This selection takes effect only through squash merge after exact-head Fable approval, Codex adjudication, green CI and explicit Pavlo or Architecture Board authorization. Until that merge, the PR carrying §§25–27 is a proposed Board act.
