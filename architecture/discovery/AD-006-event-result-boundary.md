---
Decision-ID: AD-006
Title: Event and Result Boundary
Version: 0.2.0
Status: Discovery
Owner: Architecture Board
Depends-On: OCP-004, OCP-006, OCP-008, OCP-009, AD-002
Applies-To: AB-054, Event model, Result model, Objective achievement evidence
Review-After: Repeated external adversarial boundary review
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

## 2. Boundary questions

AD-006 asks two independent questions. The Architecture Board may select different outcomes for Event and Result. Registration of both terms does not prove that both deserve the same ontological status.

### 2.1 Event question

Should Core model Event as:

1. a real-world occurrence or change with identity independent of any report — E1;
2. an attributable observation or assertion that something occurred — E2;
3. a two-layer model separating occurrence identity from observation records — E3;
4. a governed identified-record pattern without a fundamental Event Concept — E4;
5. domain-local records with no Core Event model — E5?

### 2.2 Result question

Should Core model Result as:

1. a realized outcome or effect with independent identity — R1;
2. an attributable assessment promoted to a fundamental Result Concept — R2;
3. a governed attributable assessment record without a fundamental Result Concept — R3;
4. an Operation-owned terminal summary without independent Result identity — R4;
5. a derived conclusion recomputed from exact evidence and evaluation rules — R5;
6. domain-local Result models with no Core Result model — R6?

The numbering and semantics in this section map one-to-one to the admissible outcomes in §§13–14. No outcome contains an unstated fundamental-versus-record sub-choice.

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

Mandatory guardrails:

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

The word `result` is overloaded. It may refer to:

- the realized effect of activity;
- a conclusion that an Objective was achieved, not achieved, partially achieved or remains indeterminate;
- a measurement or KPI value;
- a Constraint evaluation output;
- a terminal Operation summary;
- a software function return value.

Only realized effect and attributable assessment are candidates for promotion to a **fundamental Result Concept**. R3–R6 are intentionally non-fundamental alternatives: a governed record, Operation-owned summary, derived-only value or domain-local model may be selected without implying independent Result identity.

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
- an ongoing Operation may already have provisional or partial assessment evidence;
- a successful Result does not determine the Operation lifecycle stage.

AD-006 does not add Event or Result fields to Operation and does not change OCP-004 lifecycle semantics.

Parent/child Operation composition remains governed by AB-016. A child Result does not aggregate into a parent Result without an explicit reviewed rule.

## 8. Constraint evaluation, Conflict and Risk boundary

OCP-006 already uses local evaluation records and values such as `satisfied`, `violated`, `not_applicable` or `indeterminate` within its own normative contract.

Those values are not automatically instances of a proposed fundamental Result Concept.

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

- an occurrence exists and remains referenceable even when no observation record exists yet;
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

No selected model may silently equate all timestamps or select truth by the latest record.

Corrections must preserve history. A corrected observation or revised stored assessment should normally be a new identified record, amendment or superseding record rather than an in-place rewrite of attributable evidence. A derived-only outcome must preserve exact snapshots and replayability rather than simulate record supersession. Any invocation of P-001 must be complete and versioned.

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

This outcome must prove cross-observation occurrence identity without heuristic truth selection and must support an occurrence with zero observations.

### E2 — observation/assertion as fundamental Event Concept

Event identifies an attributable observation or report, not the underlying occurrence.

This outcome must explain how multiple reports about one possible occurrence are related without claiming one hidden occurrence identity.

### E3 — two-layer occurrence and observation model

A reusable occurrence identity is separated from attributable observation records.

The Board must decide whether one or both layers are fundamental Concepts and whether the observation layer invokes P-001. Occurrence identity must remain valid with zero observations.

### E4 — governed record pattern only

Core defines a reusable identified-record contract for domain Event records but does not introduce a fundamental Event Concept.

This outcome must prove interoperability and reference integrity without one Core occurrence identity and must detect, rather than silently resolve, ambiguous cross-domain references.

### E5 — domain-local Event models

Core introduces neither a Concept nor a universal Event record contract.

This outcome must show that OCP-004, Objective evidence and coordination can operate without ambiguous cross-domain Event references. Label or timestamp similarity may not be used as an implicit Core identity bridge.

## 14. Admissible Result outcomes

### R1 — realized outcome as fundamental Result Concept

Result identifies an actual outcome or effect independently of assessments.

Assessments are separate records and may disagree about the same Result.

### R2 — attributable assessment as fundamental Result Concept

Each Result identifies an attributable evaluation of one exact target under one exact rule and evidence snapshot.

This outcome must justify why assessment identity deserves fundamental Concept status rather than a governed record contract.

### R3 — governed assessment record pattern only

Core defines a reusable identified assessment-record contract, potentially through a complete P-001 invocation, but does not introduce a fundamental Result Concept.

This outcome must define endpoints, authority, provenance, exact binding, correction and validation semantics.

### R4 — Operation-owned summary

Result is local to one Operation and summarizes its assessed outcome without independent identity outside that Operation.

This outcome must not collapse lifecycle completion into success and must explain how Objective-specific assessments remain distinct.

### R5 — derived Result only

Result is not stored as an authoritative object; it is recomputed from exact evidence, criteria and snapshots.

This outcome must define deterministic replay, freshness, conflict, historical-reference behavior and recomputation after late evidence without pretending that a stored assessment was superseded.

### R6 — domain-local Result models

Core introduces no Result Concept or universal assessment record.

This outcome must still support Objective achievement evidence without uncontrolled status fields and must detect or reject cross-domain ambiguity rather than accepting unresolved positive conclusions.

## 15. Required downstream deliverables

The selected Event and Result outcomes must define:

1. separate independent-identity verdicts for Event and Result;
2. occurrence versus observation ownership;
3. realized outcome versus assessment ownership;
4. allowed targets and references;
5. provenance and authority;
6. timestamp distinctions and uncertainty boundary;
7. correction, amendment, supersession or recomputation behavior;
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

## 16. Required executable evidence

Evidence obligations are divided into an unconditional core and outcome-conditional blocks. An outcome is evaluated only against cases expressible under its selected semantic ownership; no option is penalized for declining a layer that it explicitly does not define.

### 16.1 Unconditional core — all Event and Result outcomes

Every selected combination must provide mechanically reviewable evidence that:

1. a completed Operation can have an Objective that remains not achieved or indeterminate;
2. a lifecycle transition record does not automatically become a Core Event;
3. one Operation may pursue multiple Objectives with different assessment or derived outcomes;
4. several Operations may contribute evidence to one Objective without identity collapse;
5. stale, missing or conflicting evidence produces no authoritative positive achievement conclusion;
6. a Constraint violation does not automatically create Conflict or a fundamental Result;
7. a successful Event, observation, assessment or derived conclusion does not automatically create a Capability claim, Readiness or authorization;
8. a child Operation outcome does not automatically aggregate into a parent Operation;
9. repeated evaluation under the same exact rule and snapshot is deterministic or explicitly indeterminate.

For non-Core outcomes such as E5 or R6, these obligations may be demonstrated through governed integration fixtures or domain-owned records, but the Core boundary must still prevent permissive implicit inference.

### 16.2 Event outcome-conditional evidence

**E1 and E3 must additionally prove:**

- an occurrence can exist with zero observations and retains identity independent of reports;
- one occurrence may be reported by two sources without collapsing the observation records;
- conflicting observations do not allow list order, newest timestamp or source count to select truth;
- occurrence, observation and recording times remain distinct when all are represented.

**E2 must additionally prove:**

- two attributable observations about one possible real-world occurrence remain separate Event identities;
- Core does not manufacture an unmodeled occurrence identity from label or timestamp similarity;
- correction preserves attributable observation history.

**E4 must additionally prove:**

- governed domain records resolve through the selected record contract;
- ambiguous or incompatible cross-domain references are detected and rejected;
- the absence of a fundamental occurrence identity does not authorize heuristic identity collapse.

**E5 must additionally prove:**

- cross-domain consumers cannot treat equal labels or nearby timestamps as equal Event identities;
- unresolved domain Event references fail closed or remain explicitly unresolved;
- OCP-004 and Objective evidence can consume governed domain outputs without a hidden universal Event object.

### 16.3 Result outcome-conditional evidence

**R1 must additionally prove:**

- multiple assessments may refer to one realized outcome without becoming the outcome itself;
- conflicting assessments do not mutate realized-outcome identity;
- an Event relevant to the outcome is insufficient by itself to prove Objective achievement.

**R2, R3 and R4 must additionally prove:**

- an ongoing Operation may have a provisional or partial stored assessment without changing lifecycle stage;
- late evidence creates a new, amended or superseding attributable assessment rather than rewriting prior history;
- exact target, rule, evidence snapshot and evaluator bindings determine the assessment authority;
- conflicting stored assessments remain visible and cannot be resolved by record order alone.

**R5 must additionally prove:**

- late evidence creates a new exact input snapshot and a new recomputation result;
- the historical result remains reproducible from its original snapshot;
- no stored assessment is invented or mutated;
- missing, stale or conflicting inputs produce no authoritative positive derivation.

**R6 must additionally prove:**

- uncontrolled domain status fields cannot silently become Core Objective achievement;
- incompatible or ambiguous cross-domain Result references are detected and rejected;
- the absence of a universal Result record does not allow lifecycle completion or latest-record heuristics to select a positive conclusion.

## 17. First integrated non-sensitive scenario

The first downstream evidence set must include one coherent, non-sensitive scenario spanning the accepted foundation rather than isolated single-Concept fixtures.

Recommended neutral scenario:

- one Objective to confirm the condition of a generic infrastructure asset;
- one Operation pursuing that Objective;
- two Resources participating through explicit Assignments;
- at least one temporal or exclusivity Constraint;
- evidence with at least one missing, delayed or conflicting item;
- Objective-specific assessment or derived outcomes according to the selected R-outcome;
- Operation lifecycle completion that does not force a successful Result;
- no coordinates, real units, personal data or operationally sensitive details.

The Event representation in the scenario is outcome-dependent:

- E1/E3 use occurrence identity and observation records, including the zero-observation case in a dedicated fixture;
- E2 uses attributable observations without a hidden occurrence object;
- E4 uses governed domain Event records;
- E5 uses domain-local evidence with explicit cross-domain ambiguity handling.

The Result representation is likewise outcome-dependent:

- R1 separates realized outcome from assessments;
- R2–R4 use the selected stored assessment or summary ownership;
- R5 uses deterministic derivation and replay;
- R6 uses governed domain-local evidence without creating a Core Result identity.

The scenario must exercise cross-Concept references and fail-safe behavior. It must not invent a schema for a layer rejected by the selected outcomes.

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
16. evidence obligations assume a semantic layer rejected by the selected outcome;
17. the selected model cannot support one integrated non-sensitive scenario without hidden fields or domain assumptions.

## 20. Exit criteria

AD-006 is ready for Architecture Board decision when:

- Event and Result receive separate independent-identity verdicts;
- occurrence, observation, evidence, evaluation and assessment boundaries survive repeated adversarial review;
- explicit Event and Result outcomes are selected or named evidence gaps return the AD to Discovery;
- the six Result outcomes remain one-to-one across the question, outcome and evidence sections;
- evidence obligations are outcome-fair and no rejected layer is reintroduced through fixtures;
- Objective achievement remains independent from Operation lifecycle;
- Constraint evaluation and future Conflict semantics remain separate;
- Capability, Readiness and State guardrails are preserved;
- correction, uncertainty and fail-safe behavior are explicit;
- proposed dependencies are explicit and acyclic;
- executable counterexamples are assigned to downstream normative owners;
- the integrated non-sensitive scenario contract is accepted;
- unresolved semantics are recorded in Architecture Backlog.

## 21. External review resolution

External adversarial review of revision `0.1.0` raised:

- **F1 Moderate:** unconditional evidence requirements were not expressible under all outcomes;
- **F2 Minor:** the Result option lists did not define one consistent decision space;
- **Suggestion:** add an occurrence-with-zero-observations counterexample for E1/E3.

Revision `0.2.0` addresses them by:

1. splitting §16 into an unconditional core and outcome-conditional Event and Result obligations;
2. defining six Result outcomes consistently in §§2.2, 5 and 14;
3. separating fundamental Result candidates R1/R2 from non-fundamental alternatives R3–R6;
4. defining derived-only late-evidence behavior as recomputation rather than stored-record supersession;
5. requiring E4/E5 and R6 to detect and reject ambiguity without hidden Core identity;
6. adding the zero-observation occurrence case to E1/E3 identity and executable evidence.

F1 and F2 are addressed pending repeated external verification of this revision.

## 22. Architecture Board decision

No Event or Result outcome is selected by revision `0.2.0`.

AD-006 remains `Discovery`. It changes no Concept status and introduces no normative model beyond the discovery guardrails and review obligations in this document.

The next act is repeated external adversarial review of the corrected outcome matrices and evidence obligations before Architecture Board outcome selection and before any OCP-010 or OCP-011 specification is opened.
