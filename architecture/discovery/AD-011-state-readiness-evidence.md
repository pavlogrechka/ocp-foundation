---
Decision-ID: AD-011
Title: State and Readiness Evidence Boundary
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: AD-002, ADR-DRAFT-007, OCP-003, OCP-004, OCP-005, OCP-006, OCP-007, OCP-010, OCP-011, OCP-012, OCP-013
Applies-To: AB-007, State, Readiness
Review-After: External adversarial review of the State and Readiness candidate separation and evidence matrix
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
| availability | whether a subject may actually be considered for use at a time | defined by this discovery |
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
