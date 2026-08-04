---
Decision-ID: AD-006
Title: Event and Result Boundary
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: OCP-004, OCP-006, OCP-008, OCP-009, AD-002
Applies-To: AB-054, Event model, Result model, Objective achievement evidence
Review-After: External adversarial boundary review
---

# AD-006 — Event and Result Boundary

## 1. Trigger and current state

`Event` and `Result` are registered as `Proposed` Concepts, but neither has a defining specification.

Accepted foundation artifacts already use adjacent semantics:

- OCP-004 describes Operation as a context for events and results and records actual temporal bounds;
- OCP-008 separates Objective intent from achievement evidence and evaluation;
- OCP-006 separates a Constraint, its evaluation record and an admissibility decision;
- OCP-009 states that a successful Event or Result does not automatically establish a standing Capability claim;
- lifecycle transition records in Operation, Assignment and Constraint record governed changes without being declared universal Events;
- AD-002 prevents observed facts or evaluations from silently becoming fundamental State or Readiness.

These uses do not yet decide what Event or Result identifies, whether either has independent identity, how observations differ from occurrences, how results differ from assessments, or which records are authoritative.

AD-006 introduces no Event or Result structure, Concept status change, current graph edge, P-001 invocation, lifecycle, API, schema or implementation.

## 2. Boundary question

AD-006 asks two independent questions.

### 2.1 Event question

Should Core model Event as:

1. a real-world occurrence or change with identity independent of any report;
2. an attributable observation or assertion that something occurred;
3. a two-layer model separating occurrence identity from observation records;
4. a governed identified record pattern without a fundamental Event Concept;
5. domain-local records with no Core Event model?

### 2.2 Result question

Should Core model Result as:

1. a realized outcome or effect with independent identity;
2. an attributable assessment of an Objective, criterion or operational context;
3. an Operation-owned terminal summary;
4. a derived conclusion produced from exact evidence and evaluation rules;
5. a governed identified record pattern without a fundamental Result Concept;
6. domain-local records with no Core Result model?

The Architecture Board may select different outcomes for Event and Result. Registration of both terms does not prove that both deserve the same ontological status.

## 3. Semantic layers that must remain distinct

The discovery must distinguish at least the following layers:

- **occurrence** — something happened or changed in the operational world;
- **observation or report** — an attributable statement that an occurrence was perceived, measured or reported;
- **evidence item** — material used by an evaluation, which may include an observation but is not automatically true or sufficient;
- **evaluation** — application of an exact rule or criterion to an exact evidence and input snapshot;
- **result assessment** — an attributable conclusion about an Objective, criterion or operational context at a stated time;
- **realized outcome or effect** — the actual condition produced in the world, if Core can justify independent identity for it;
- **Operation lifecycle state** — the governed stage of an Operation, derived from its transition history;
- **Constraint evaluation result** — a local output of OCP-006 evaluation semantics;
- **current usability, Readiness or State** — separate downstream semantics governed by AD-002.

No layer is promoted to a fundamental Concept merely because it is useful for reporting or implementation.

## 4. Event boundary

A candidate Event occurrence represents a bounded fact that something happened or changed.

A candidate observation record represents an attributable assertion about an occurrence or condition. An observation may be incomplete, delayed, duplicated, mistaken, conflicting or later corrected.

The following statements are mandatory guardrails for this discovery:

- an observation is not automatically the occurrence itself;
- two reports with similar labels and nearby timestamps are not automatically the same Event;
- one occurrence may have zero, one or many observations;
- one observation may refer to an unresolved or uncertain occurrence;
- record order, newest timestamp or source count does not determine truth by default;
- a lifecycle transition record is not automatically a Core Event;
- a Constraint evaluation record is not automatically a Core Event;
- an Event does not automatically create Conflict, Risk, Result, State, Readiness or Capability evidence.

The downstream decision must specify whether occurrence deduplication is normative, domain-owned or explicitly absent.

## 5. Result boundary

The word `result` is currently overloaded. It may refer to:

- the realized effect of activity;
- a conclusion that an Objective was achieved, not achieved, partially achieved or remains indeterminate;
- a measurement or KPI value;
- a Constraint evaluation output;
- a terminal Operation summary;
- a software function return value.

Only the first two are candidates for a Core Result model in this discovery.

A Result must not be inferred solely from:

- Operation reaching `Completed`, `Cancelled` or `Aborted`;
- existence of one Event or observation;
- absence of negative evidence;
- an Assignment being established or terminated;
- a Constraint evaluation being satisfied or violated;
- a Capability definition or future holder claim;
- a human-readable success label.

If Result is an assessment, the downstream model must bind it to exact criteria, evidence, input snapshot, evaluator and evaluation time or explain why those dimensions are unnecessary.

If Result is a realized outcome Concept, the downstream model must prove identity independent of any assessment and show how consumers reference it without collapsing occurrence, evidence and interpretation.

## 6. Objective achievement boundary

OCP-008 defines Objective as intended outcome and explicitly excludes authoritative achievement status.

AD-006 preserves these rules:

- Objective validity does not depend on achievement;
- Operation completion does not imply Objective achievement;
- one Operation may pursue multiple Objectives with different assessments;
- multiple Operations may contribute evidence relevant to one Objective without becoming one Operation;
- one Event may be relevant to several Objective assessments without proving any of them automatically;
- Objective supersession does not rewrite historical evidence or Result references automatically;
- partial satisfaction, confidence and conflicting assessments require explicit semantics rather than one permissive boolean.

The downstream owner must decide whether a Result assessment targets an Objective, an Operation, another criterion, or an explicit combination, and whether multiple target kinds require separate record types.

## 7. Operation lifecycle boundary

Operation lifecycle and operational outcome are independent axes.

Examples:

- a completed Operation may fail to achieve every Objective;
- a cancelled Operation may still produce relevant Events or partial effects;
- an aborted Operation may produce a valuable observation;
- an ongoing Operation may already have provisional or partial Result assessments;
- a successful Result does not determine the Operation lifecycle stage.

AD-006 does not add Event or Result fields to Operation and does not change OCP-004 lifecycle semantics.

Parent/child Operation composition remains governed by AB-016. A child Result does not aggregate into a parent Result without an explicit reviewed rule.

## 8. Constraint evaluation, Conflict and Risk boundary

OCP-006 already uses local evaluation records and values such as `satisfied`, `violated`, `not_applicable` or `indeterminate` within its own normative contract.

Those values are not automatically instances of the proposed fundamental Result Concept.

A Constraint violation may be evidence for a later finding or Conflict model, but:

- violation does not automatically create a stored Conflict;
- several violations do not automatically aggregate into one Conflict;
- an advisory finding does not automatically become an Operation Result;
- `indeterminate` remains fail-safe under the owning Constraint rule;
- replay and freshness semantics remain bound by AB-039 and are not solved by renaming evaluation output as Result.

AD-006 must remain compatible with AB-018 and AB-038 without resolving them implicitly.

## 9. Capability, Readiness and State boundary

A successful Event or Result may become evidence input to a future Capability claim only through a separate exact, attributable and reviewed claim rule.

It never automatically creates:

- a standing Capability claim;
- current availability;
- Readiness;
- authorization;
- admissibility;
- a fundamental State.

AD-002 remains authoritative: observed facts and assessments do not justify a State or Readiness Concept without independent identity and fail-safe evidence semantics.

## 10. Independent identity tests

### 10.1 Event identity test

A fundamental Event Concept is justified only if review confirms identity that remains meaningful independent of any single observation, report, Operation or storage record.

Evidence for independent occurrence identity may include:

- several independent observations refer to the same occurrence without becoming one observation;
- the occurrence is referenced by multiple Operations, Objective assessments or audits;
- correction of one observation does not mutate the occurrence identity;
- occurrence identity survives changes in labels, reporting systems and evidence formats;
- domain modules can specialize occurrence semantics without losing Core identity.

Evidence against a fundamental Event Concept includes:

- every useful Event is only a source-specific assertion;
- identity is always reducible to one report record;
- deduplication cannot be governed without domain-specific heuristics;
- lifecycle transitions and local evaluation records already provide all required identity.

### 10.2 Result identity test

A fundamental Result Concept is justified only if review confirms identity independent of a single evaluator, rule execution or Operation summary.

Evidence for independent identity may include:

- the same realized outcome is referenced by several assessments or Operations;
- assessment records can be amended or superseded without mutating the realized outcome;
- Result remains meaningful without embedding Operation lifecycle;
- cross-domain consumers need one governed Result reference.

Evidence against a fundamental Result Concept includes:

- all useful semantics are an attributable assessment of `target + rule + evidence snapshot`;
- identity is reducible to an evaluation record;
- a Result only summarizes one Operation and has no independent lifecycle or reuse;
- the term merely aliases Constraint evaluation output or a status field.

Event and Result require separate identity verdicts.

## 11. Time, provenance, correction and uncertainty

The downstream decision must distinguish, where applicable:

- when an occurrence happened;
- when it was observed;
- when it was recorded;
- when evidence was evaluated;
- the as-of time or input snapshot of a Result assessment.

AD-006 does not select a canonical timestamp structure or uncertainty model.

However, no selected model may silently equate all timestamps or select truth by the latest record.

Corrections must preserve history. A corrected observation or revised Result assessment should normally be a new identified record, amendment or superseding record rather than an in-place rewrite of attributable evidence. Any invocation of P-001 must be complete and versioned.

Missing, stale, ambiguous or conflicting evidence must not become an authoritative positive Result by default.

## 12. Candidate relationships and Concept graph

Candidate relationships for review include:

```text
Observation reports occurrence
Event relates to Operation
Event provides evidence for assessment
Result assessment evaluates Objective
Result assessment references evidence
Result assessment supersedes prior assessment
```

These labels are hypotheses, not accepted relation types.

AD-006 introduces no current Concept edge.

The existing non-normative future edge `Operation ⇢ Event` remains planning intent only. A downstream specification must justify every current dependency explicitly and prove acyclicity.

Potential graph risks include:

- Event depends on Operation while Operation depends on Event;
- Result depends on Objective and Operation while Operation is changed to depend on Result;
- Event is defined through State while State is later derived from Event;
- Result is defined through Conflict while Conflict is derived from Result-like evaluations.

## 13. Admissible Event outcomes

### E1 — occurrence as fundamental Event Concept

Event identifies the occurrence. Observations are separate local or identified records.

This outcome must prove cross-observation occurrence identity without heuristic truth selection.

### E2 — observation/assertion as fundamental Event Concept

Event identifies an attributable observation or report, not the underlying occurrence.

This outcome must explain how multiple reports about one occurrence are related without claiming one hidden occurrence identity.

### E3 — two-layer occurrence and observation model

A reusable occurrence identity is separated from attributable observation records.

The Board must decide whether one or both layers are fundamental Concepts and whether the observation layer invokes P-001.

### E4 — governed record pattern only

Core defines a reusable identified-record contract for domain Event records but does not introduce a fundamental Event Concept.

This outcome must prove interoperability and reference integrity without one Core occurrence identity.

### E5 — domain-local Event models

Core introduces neither a Concept nor a universal Event record contract.

This outcome must show that OCP-004, Objective evidence and coordination can operate without ambiguous cross-domain event references.

## 14. Admissible Result outcomes

### R1 — realized outcome as fundamental Result Concept

Result identifies an actual outcome or effect independently of assessments.

Assessments are separate records and may disagree about the same Result.

### R2 — Result as attributable assessment record

Result identifies an evaluation of one exact target under one exact rule and evidence snapshot.

It may be a governed local or P-001 record without becoming a fundamental Concept by default.

### R3 — Result as Operation-owned summary

Result is local to one Operation and summarizes its assessed outcome without independent identity outside that Operation.

This outcome must not collapse lifecycle completion into success.

### R4 — derived Result only

Result is not stored as an authoritative object; it is recomputed from exact evidence, criteria and snapshots.

This outcome must define replay, freshness, conflict and historical-reference behavior.

### R5 — domain-local Result models

Core introduces no Result Concept or universal assessment record.

This outcome must still support Objective achievement evidence without uncontrolled status fields.

## 15. Required downstream deliverables

The selected Event and Result outcomes must define:

1. separate independent-identity verdicts for Event and Result;
2. occurrence versus observation ownership;
3. realized outcome versus assessment ownership;
4. allowed targets and references;
5. provenance and authority;
6. timestamp distinctions and uncertainty boundary;
7. correction, amendment or supersession behavior;
8. deduplication and ambiguity behavior;
9. exact evidence, rule and snapshot binding where evaluations exist;
10. handling of missing, stale and conflicting evidence;
11. Objective achievement and partial-assessment semantics;
12. Operation lifecycle non-equivalence;
13. Constraint evaluation, Conflict and Risk boundaries;
14. Capability, Readiness and State non-implications;
15. current Concept dependencies and graph acyclicity;
16. complete P-001 conformance for every invocation;
17. executable evidence and a non-sensitive integrated example dataset.

## 16. Required executable counterexamples

The downstream normative owner must include mechanically reviewable evidence for at least these cases:

1. a completed Operation whose Objective remains not achieved or indeterminate;
2. an ongoing Operation with a provisional Result assessment;
3. one occurrence reported by two sources without automatic identity collapse by label or timestamp proximity;
4. two conflicting observations where record order and latest timestamp cannot select truth;
5. distinct occurrence, observation, recording and evaluation times;
6. a lifecycle transition record that does not automatically become a Core Event;
7. one Event that is relevant evidence but insufficient to prove Objective achievement;
8. one Operation pursuing multiple Objectives with different assessment outcomes;
9. several Operations contributing evidence to one Objective without identity collapse;
10. stale, missing or conflicting evidence producing no authoritative positive assessment;
11. late evidence creating a new or superseding assessment rather than mutating history;
12. a Constraint violation that does not automatically create Conflict or a fundamental Result;
13. a successful Event or Result that does not automatically create a Capability claim, Readiness or authorization;
14. a child Operation Result that does not automatically aggregate into a parent Operation;
15. repeated evaluation under the same exact rule and snapshot being deterministic or explicitly indeterminate.

## 17. First integrated non-sensitive scenario

The first downstream evidence set must include one coherent, non-sensitive scenario spanning the accepted foundation rather than isolated single-Concept fixtures.

Recommended neutral scenario:

- one Objective to confirm the condition of a generic infrastructure asset;
- one Operation pursuing that Objective;
- two Resources participating through explicit Assignments;
- at least one temporal or exclusivity Constraint;
- two source observations concerning one candidate occurrence;
- one missing or conflicting evidence item;
- separate Result assessments for at least two criteria or Objectives;
- Operation lifecycle completion that does not force a successful Result;
- no coordinates, real units, personal data or operationally sensitive details.

The scenario must exercise cross-Concept references and fail-safe behavior. It must not invent the final Event or Result schema before the Board selects outcomes.

## 18. What is explicitly not defined

AD-006 intentionally does not define:

- Event or Result fields, lifecycle or storage schema;
- canonical Event taxonomy;
- canonical Result status enum;
- truth, confidence or source-reliability scales;
- automatic occurrence deduplication;
- causal inference or causal graph;
- partial-achievement weighting or scoring;
- automatic Objective achievement;
- Operation success, failure or completion rules;
- Conflict, Risk, State or Readiness model;
- Capability claim evidence policy;
- authorization or approval semantics;
- canonical time or uncertainty representation;
- cryptographic evidence or non-repudiation;
- current Concept graph edges;
- P-001 invocation;
- API, database, UI or message contracts.

## 19. External review target

Attempt to falsify the discovery with cases where:

1. Event silently means both occurrence and report;
2. Result silently means both realized effect and assessment;
3. Operation completion is treated as Objective achievement;
4. a single observation is treated as authoritative truth;
5. duplicate reports are collapsed by label or timestamp proximity;
6. latest record order selects truth or assessment authority;
7. conflicting evidence produces a permissive positive Result;
8. Constraint evaluation output is reclassified as the universal Result Concept;
9. lifecycle transitions are reified as Events without independent identity;
10. Event or Result creates Conflict, Risk, Readiness, State or Capability by implication;
11. partial or multi-Objective achievement is forced into one boolean;
12. revised assessments rewrite historical evidence;
13. parent/child or multi-Operation aggregation is implied;
14. proposed graph dependencies become circular;
15. a P-001 record is used without complete endpoint, authority, provenance and validation contracts;
16. the selected model cannot support one integrated non-sensitive scenario without hidden fields or domain assumptions.

## 20. Exit criteria

AD-006 is ready for Architecture Board decision when:

- Event and Result receive separate independent-identity verdicts;
- occurrence, observation, evidence, evaluation and assessment boundaries survive adversarial review;
- explicit Event and Result outcomes are selected or named evidence gaps return the AD to Discovery;
- Objective achievement remains independent from Operation lifecycle;
- Constraint evaluation and future Conflict semantics remain separate;
- Capability, Readiness and State guardrails are preserved;
- correction, uncertainty and fail-safe behavior are explicit;
- proposed dependencies are explicit and acyclic;
- executable counterexamples are assigned to downstream normative owners;
- the integrated non-sensitive scenario contract is accepted;
- unresolved semantics are recorded in Architecture Backlog.

## 21. Architecture Board decision

No Event or Result outcome is selected by revision `0.1.0`.

AD-006 remains `Discovery`. It changes no Concept status and introduces no normative model beyond the discovery guardrails and review obligations in this document.

The next act is external adversarial review of the Event and Result boundary and the admissible outcome matrices before any OCP-010 or OCP-011 specification is opened.
