---
Decision-ID: AD-016
Title: Foundation Canonicalization Readiness Discovery
Version: 0.3.0
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-016, P-001, AD-015
Applies-To: AB-062, OCP document lifecycle, Concept lifecycle, Pattern dependencies, canonicalization waves
Review-After: Completion of the T0-T3 enabling phase and mandatory reassessment before T4
---

# AD-016 — Foundation Canonicalization Readiness Discovery

## 1. Trigger and purpose

The foundation now has eight `Accepted` Concepts, six `Accepted` non-Concept OCP contracts, an Accepted Core Boundary contract, executable reference evidence and enforced governance. The roadmap therefore names canonicalization readiness as the next review direction.

That does not mean the repository is ready for a bulk `1.0.0` status change.

The current lifecycle is intentionally mixed:

- a Concept may be `Accepted` while its defining OCP document remains `Draft`;
- a non-Concept OCP may be `Accepted` while direct semantic dependencies remain Draft documents;
- a Pattern has its own lifecycle, which currently has no `Canonical` status;
- passing reference fixtures proves finite conformance, not production readiness or semantic completeness; and
- open questions may be scoped exclusions, real blockers or unrelated future work.

AD-016 opens AB-062 to decide what **ready for Canonical review** means, which unit should be promoted first, and which evidence gaps actually block promotion. Revision `0.1.0` changes no document, Concept, Pattern, AD, AB dependency or graph status.

## 2. Inherited governance mandates

OCP-001 already requires:

1. a separate canonicalization PR;
2. stable dependencies;
3. machine-readable checks appropriate to the governed claims;
4. an explicit Architecture Board decision;
5. atomic Concept-status synchronization; and
6. first Canonical version `1.0.0` followed by Semantic Versioning.

OCP-016 adds:

- one exact semantic owner per candidate;
- human-readable evidence before artifact/status selection;
- no self-approval by documents or tooling;
- exact dependency, Pattern and migration accounting;
- `not Core ≠ invalid`; and
- a stop-and-reopen rule before any new registry, score or machine authority.

Artifact taxonomy keeps OCP document lifecycle separate from Concept lifecycle. Pattern lifecycle is `Draft → Accepted → Deprecated → Archived`; it does not currently include `Canonical`. AD, ADR and AB artifacts also do not use OCP Canonical lifecycle.

AD-016 may not silently change any of those rules.

## 3. OCP-016 routing ledger for this discovery

| Ledger question | AD-016 answer |
|---|---|
| Candidate | a governance/status-transition contract for Canonical readiness, not a new domain subject |
| Object class | Core non-Concept rule and review decision |
| Primary route | Route C under OCP-016 |
| Semantic owner | OCP-001 owns lifecycle/version rules; OCP-016 owns routing; Architecture Board owns each status act |
| Consumers | human reviewers, AI authors and downstream implementers that need stable exact contracts |
| Defining source | a later selected AD-016 act plus the existing OCP-001/OCP-016 rules |
| Dependencies | exact current OCP and Pattern artifacts, Concept projections and accepted review evidence |
| Non-implications | Canonical does not mean production-ready, immutable forever, universally complete, authorized or true in every domain |
| Lifecycle effect | none in this revision; every promotion remains a separate exact-head Board act |

No Pattern is created or invoked. No machine registry or readiness score is requested.

## 4. Current lifecycle snapshot

The snapshot at `main@ba2864d3fefc244f7e0bbd46153138592828cc5b` is:

| Artifact group | Current state | Canonicalization pressure |
|---|---|---|
| OCP-000, OCP-001, OCP-002 | `Draft` | registry, governance and taxonomy are prerequisites for many downstream documents |
| OCP-003…OCP-010 | document `Draft`; eight Concepts `Accepted` | document and Concept lifecycle axes are not yet aligned |
| OCP-011…OCP-016 | document `Accepted` | direct dependencies include Draft OCP documents and, for several contracts, Draft P-001 |
| P-001 | `0.1.0 / Draft` | invoked by OCP-007, OCP-008, OCP-010, OCP-011, OCP-012 and OCP-015 |
| active Concept registry | eight `Accepted`, five `Proposed` candidates | Proposed entries must not be promoted or treated as defects merely because the registry document changes status |
| executable reference suite | 152 unit tests and 115 non-sensitive fixtures | strong finite evidence, explicitly not a production validator or semantic-completeness proof |

The five current `Proposed` Concept candidates are Operational Space, Spectrum, Risk, Order and Coordination. Their presence is not evidence that the eight Accepted Concepts are unstable, but a whole-registry promotion must state how mixed Concept statuses remain interpretable.

## 5. Terms that must remain distinct

**Accepted Concept** means Architecture Board accepts the current identity and semantic responsibility as a basis for dependent work.

**Accepted OCP document** means the exact pre-canonical contract is binding for its reviewed scope.

**Canonical OCP document** means the document enters the `1.x` compatibility regime after a separate readiness and Board act. It may still evolve through SemVer.

**Canonical Concept** means the Concept lifecycle projection changes atomically in OCP-000, OCP-002 and its defining document. It is not inferred from document version alone.

**Accepted Pattern** means its reusable form obligations are stable enough for exact invocation under Pattern lifecycle. Current taxonomy does not define a Canonical Pattern.

**semantic stability** means identity, authority, invariants, dependencies and exclusions are sufficiently bounded for a compatibility promise.

**reference conformance** means the current checker can exercise finite structured obligations with synthetic data.

**production readiness** includes operational security, persistence, API, scale, observability and deployment guarantees outside the current repository's semantic scope.

These terms may be related, but none substitutes for another.

## 6. Decision questions

AD-016 must answer:

1. What is the first promotion unit: one document, one Concept/document pair, a dependency wave, a stable kernel or the whole foundation?
2. Must every direct dependency be Canonical, or is exact Accepted status sufficient for some artifact classes?
3. What minimum status must an invoked Pattern have before an invoker can become Canonical?
4. Can OCP-000 become Canonical while it legitimately contains Proposed Concept candidates?
5. Which OCP-002 “working hypothesis” sections must stabilize before taxonomy canonicalization?
6. Does a defining OCP need document `Accepted` before its Concept can move `Accepted → Canonical` in the same act?
7. Which open questions are blockers, scoped exclusions or unrelated future work?
8. Which normative claims require executable witnesses, and which remain human semantic judgments?
9. What compatibility promise does `1.0.0` make for prose, identifiers, records, rules, Pattern invocations and generated projections?
10. How are later domain extensions admitted without reopening every Canonical Core document?
11. What atomic migrations are required for document status, Concept status, Pattern version and generated views?
12. What evidence would require postponing all promotion?

## 7. Candidate outcomes

### A — hold at Accepted/Draft

Do not promote any artifact. Close only the readiness audit and retain current statuses until named gaps are resolved.

Benefit: no premature compatibility promise. Risk: downstream authors lack a stable `1.x` baseline even for mature semantics.

### B — one atomic foundation baseline

Promote a reviewed set of governance, registry, taxonomy, Pattern, eight Concept definitions and accepted non-Concept contracts as one coordinated baseline.

P-001 would move only to a status permitted by Pattern lifecycle, never to an invented `Canonical` Pattern status.

Benefit: one coherent cut. Risk: weakest-member coupling, very large review surface and hidden pressure to promote unready artifacts.

### C — dependency-layered waves

Promote prerequisites and then dependent artifacts in explicit topological waves. A later wave cannot outrun the status/evidence gates selected for its direct dependencies.

Benefit: visible dependency closure and bounded reviews. Risk: deciding the first wave may itself require temporary mixed `0.x/1.x` operation.

### D — selective per-artifact promotion

Promote each document or Concept/document pair as soon as its own evidence is sufficient, even while peer artifacts remain pre-canonical.

Benefit: smallest PRs and no weakest-member delay. Risk: compatibility becomes difficult to understand across a mixed dependency set.

### E — stable-kernel extraction

Split evolving sections from stable normative kernels, then canonicalize only the kernels while extensions/open questions remain pre-canonical artifacts.

Benefit: precise compatibility surface. Risk: document restructuring may duplicate authority or hide semantic coupling.

### F — enabling baseline first, then reassess

Before any Concept promotion, stabilize only the lifecycle prerequisites: OCP-000/OCP-001/OCP-002/OCP-016 and P-001 at the status allowed by each artifact class. Then perform a new comparison of Concept and non-Concept waves.

Benefit: resolves shared governance blockers without preselecting domain promotions. Risk: an enabling wave may be mistaken for proof that downstream semantics are ready.

Outcomes may be composed only through an explicit Board act that states precedence and promotion units. For example, F may precede C; that composition is not assumed by this Discovery.

## 8. Dependency and lifecycle topology

The current dependency shape creates real ordering questions:

- OCP-001 directly depends on Draft OCP-000 and Accepted OCP-016;
- OCP-002 directly depends on Draft OCP-000 and OCP-001;
- every defining Concept OCP depends on Draft governance/registry/taxonomy artifacts;
- several Accepted record/workflow contracts depend on Draft Concept documents;
- six artifacts invoke Draft P-001; and
- Concept status synchronization spans OCP-000, OCP-002 and each defining document.

AD-016 must not invent a circular rule that every dependency must already be Canonical before any root artifact can move. It must distinguish:

1. **semantic dependency stability** — exact referenced responsibility is accepted and bounded;
2. **document lifecycle stability** — the dependency's document status/version supports the promised compatibility;
3. **artifact-class compatibility** — Pattern and AD lifecycles do not share the OCP Canonical state; and
4. **migration order** — which status and version updates must be atomic versus sequential.

Topological order is evidence, not authority. Repository order, OCP number or newest version cannot choose the first wave.

## 9. Readiness dimensions

Every candidate promotion unit must be assessed across all dimensions:

| Dimension | Required evidence | Not sufficient |
|---|---|---|
| semantic scope | stable identity/responsibility, explicit exclusions and non-implications | document age or term popularity |
| authority | one defining owner per rule/result/status | author count, reviewer count or implementation ownership |
| dependency closure | exact direct dependencies with compatible lifecycle treatment | alphabetical or numeric order |
| lifecycle | valid current status, explicit target status and atomic projections | editing `Version` alone |
| compatibility | stated `1.x` preservation and breaking-change behavior | “mature” label |
| human evidence | readable contract, scenarios, counterexamples and resolved findings | checker success alone |
| executable evidence | witnesses for every mechanically expressible normative obligation | production-readiness claim |
| extension boundary | safe domain/profile/consumer routes under OCP-016 | freezing all future specialization |
| migration | exact references, Pattern invokers and generated views remain coherent | best-effort rebinding or newest selection |
| open questions | each classified as blocker, scoped exclusion or unrelated follow-up | zero open-question count as a score |

No numeric total converts partial evidence into readiness. One unresolved authority, identity, dependency or migration blocker remains blocking.

## 10. Open questions and scoped evolution

Canonical does not require a document to predict every future feature. It does require the exact compatibility surface to be complete and honest.

Each open or deferred item must be classified:

- **blocking** — it can change identity, core invariant, authority, required dependency or wire-significant normative contract inside the proposed `1.x` scope;
- **scoped exclusion** — the Canonical contract explicitly does not define it, and later addition can follow SemVer plus OCP-016 without changing current guarantees; or
- **unrelated follow-up** — it belongs to another accepted owner and cannot alter this candidate's responsibility by implication.

Classification is reviewed qualitatively. A document with one identity blocker may be less ready than a document with ten explicit scoped exclusions.

## 11. Evidence and production boundary

The current checker can support canonicalization evidence for:

- artifact identity and exact references;
- Concept status synchronization;
- Concept dependency graph and generated-map consistency;
- Pattern version invocation;
- rule-manifest source integrity;
- finite lifecycle, record, reference, replay and fail-safe cases already implemented; and
- full-history process conformance.

It cannot establish:

- production API or persistence compatibility;
- legitimate real-world owner authority;
- semantic completeness of prose;
- operational security, scale or deployment fitness;
- absence of every future extension; or
- metaphysical truth of a Concept identity.

Outcome A may treat missing production-facing contracts as blocking. Outcomes C/D/E/F may instead canonicalize a clearly bounded semantic contract while keeping production artifacts out of scope. The comparison must decide this explicitly rather than assume either position.

## 12. Mandatory counterexamples

Every admissible outcome must handle:

1. an `Accepted` Concept whose defining OCP document remains `Draft`;
2. an `Accepted` OCP with a direct Draft semantic dependency;
3. an invoker proposed for Canonical while P-001 remains Draft;
4. a Pattern incorrectly promoted to `Canonical` although its lifecycle lacks that status;
5. OCP-000 containing both Accepted and Proposed Concept entries;
6. one unresolved question that can change identity, hidden among many editorial questions;
7. ten open questions that are all explicit scoped exclusions;
8. green fixtures presented as proof of production readiness;
9. missing production API treated automatically as proof that semantic `1.0.0` is impossible;
10. a whole-foundation wave that promotes one weak artifact because all peers are ready;
11. selective promotion whose dependency promise cannot be explained to a human reader;
12. a stable-kernel split that duplicates one normative rule in two documents;
13. a document version changed to `1.0.0` without synchronized document/Concept registry status;
14. a Concept status changed because its document was promoted, without a separate identity/status act;
15. Proposed registry candidates silently promoted with the registry document;
16. an Accepted negative verdict reopened during canonicalization without new evidence;
17. a domain profile frozen into Core merely because a Canonical consumer references it;
18. newest version, OCP number, document age, test count or reviewer count selecting readiness;
19. a breaking semantic change labeled minor because pre-canonical versions used `0.x`; and
20. `Canonical` interpreted as authorization, Readiness, truth, universal completeness or immutability forever.

## 13. Unconditional evidence obligations

Every outcome must:

1. inventory exact current document, Concept, Pattern and dependency statuses;
2. keep document and Concept lifecycle axes separate;
3. preserve artifact-class lifecycle differences;
4. name the promotion unit and exact compatibility surface;
5. classify open questions without count-based scoring;
6. preserve human-readable normative primacy;
7. map all twenty §12 counterexamples;
8. state production scope and non-implications;
9. require exact version/dependency/Pattern binding and atomic projections;
10. reject status selection by newest/order/count/popularity;
11. preserve explicit reopening of accepted negative verdicts; and
12. make no status or `1.0.0` change in Discovery.

## 14. Outcome-conditional evidence

### 14.1 A — hold

- name exact blockers rather than citing general caution;
- define evidence that would reopen promotion; and
- show that delay does not silently remove Accepted authority.

### 14.2 B — atomic baseline

- prove every included artifact meets the same declared floor;
- expose the weakest member and rollback/migration effect; and
- prevent Proposed Concept entries from inheriting Canonical status.

### 14.3 C — layered waves

- provide a cycle-free dependency/status plan;
- define the permitted mixed-version interval; and
- prove each later wave exact-binds an eligible earlier baseline.

### 14.4 D — selective

- explain every mixed lifecycle dependency to human consumers;
- prevent a Canonical artifact from laundering Draft dependency semantics; and
- define when a peer difference becomes a compatibility break.

### 14.5 E — kernel extraction

- prove one defining location per normative rule;
- map old exact references to the split; and
- show that excluded extension points cannot mutate kernel identity/invariants.

### 14.6 F — enabling baseline

- define why each enabling artifact is a prerequisite;
- handle P-001 under Pattern lifecycle without inventing Canonical Pattern status; and
- demonstrate that enabling acceptance/canonicalization does not pre-approve downstream waves.

## 15. Outcome-fairness audit

No unconditional obligation may require:

- a bulk wave rejected by A or D;
- per-artifact promotion rejected by B;
- document splitting rejected by A/B/C/D/F;
- production schemas assumed unnecessary by A or mandatory by other outcomes;
- a Canonical Pattern status absent from the taxonomy; or
- machine readiness fields or scores rejected by OCP-016.

Each outcome must provide a semantic equivalent for dependency coherence, compatibility visibility, open-question treatment and fail-safe migration using only layers it accepts.

The falsification target is explicit: **the readiness evidence assumes the promotion unit, production layer or artifact lifecycle that the selected outcome rejects**.

## 16. External-review targets

External review must determine:

1. whether the six outcomes span credible promotion strategies;
2. whether F is a distinct outcome or only the first wave of C;
3. whether B creates unfair weakest-member pressure;
4. whether D can give a coherent compatibility promise across Draft dependencies;
5. whether E preserves one defining location;
6. whether A has falsifiable reopening gates rather than indefinite caution;
7. whether Pattern lifecycle is treated without inventing a new status;
8. whether Proposed Concept entries remain independent of OCP-000 document status;
9. whether production readiness is neither assumed nor dismissed automatically;
10. whether all twenty counterexamples are expressible without sensitive data or a new registry;
11. whether OCP-016 routing/authority rules are applied to canonicalization itself; and
12. whether a human can understand the compatibility promise without reading checker code.

## 17. Exit criteria

AD-016 may leave Discovery only when:

1. the current lifecycle/dependency inventory is externally verified;
2. all candidate outcomes are compared against all twenty counterexamples;
3. direct dependency and Pattern status floors are explicit;
4. document/Concept status synchronization is exact;
5. open questions are classified by semantic effect rather than count;
6. semantic and production readiness boundaries are explicit;
7. the selected promotion unit has a human-readable `1.x` compatibility promise;
8. outcome-fair human and mechanically expressible evidence plans exist;
9. no registry, score, newest/order/count rule or tool output selects readiness;
10. no accepted negative verdict or domain authority is reopened silently; and
11. the Board selection remains separate from every actual status/version promotion.

## 18. Discovery status and next act

Revision `0.1.0` opens AD-016 and AB-062 in `Discovery`. It creates no preferred outcome and changes no OCP, Concept, Pattern, AD, ADR, AB dependency, registry entry, generated map, checker rule, fixture or graph edge.

A later `AD-016A` comparison should map exact artifacts, dependency waves, open-question classifications and the twenty counterexamples across A–F. A separate `AD-016B` Board act may select a readiness strategy or retain current statuses. Every actual Canonical promotion remains a later separately reviewed PR with exact-head Fable approval, Codex adjudication, green CI and explicit Pavlo or Architecture Board authorization.

## 19. AD-016A comparison method

AD-016A compares the six Discovery outcomes on the repository state at `main@37d8b672891b348d1e8446a9513837749e0e8f0f`. The lifecycle inventory is unchanged from §4; this newer base adds the externally reviewed AD-016 Discovery itself.

The comparison uses four tests in order:

1. **authority test** — identify the human-readable owner of every compatibility promise;
2. **dependency test** — ask whether a candidate can remain compatible while each direct dependency evolves under its current lifecycle;
3. **surface test** — distinguish the exact `1.x` surface from explicit exclusions and future extensions; and
4. **migration test** — name the status, version, registry and Pattern references that must change together.

Passing fixtures are evidence within those tests. They do not choose an outcome or erase a semantic blocker. AD-016A makes no lifecycle change and is not an Architecture Board selection.

## 20. Exact artifact readiness audit

The table names the next lifecycle act each artifact class could lawfully receive. It does not authorize that act.

| Artifact or group | Current state | Earliest candidate act | Must move atomically | Current readiness issue |
|---|---|---|---|---|
| OCP-000 | `0.17.0 / Draft` | document `1.0.0 / Canonical` | document metadata only; Concept rows keep their own statuses | define the `1.x` registry promise while preserving five Proposed rows; resolve whether “Operational Space First” is a non-identity principle or depends on an undefined Concept |
| OCP-016 | `0.2.0 / Accepted` | document `1.0.0 / Canonical` | document metadata and exact incorporated baseline | direct OCP-000 dependency must meet the selected floor |
| OCP-001 | `0.9.0 / Draft` | document `1.0.0 / Canonical` | document metadata and the selected readiness rule | AD-016 dependency/Pattern floors and promotion-unit rules are not yet selected or incorporated |
| OCP-002 | `0.17.0 / Draft` | document `1.0.0 / Canonical` | document metadata; Concept projections remain independently synchronized | its top-level category tree is explicitly a non-Canonical working hypothesis and needs a clear normative/excluded boundary |
| P-001 | `0.1.0 / Draft` | Pattern `Accepted` at an exact reviewed version | Pattern metadata and all changed invocations, if the version changes | six current contracts already invoke it, but Pattern acceptance and its current evidence statement still need a dedicated act |
| OCP-003…OCP-010 | document `Draft`; eight Concepts `Accepted` | paired document `1.0.0 / Canonical` plus Concept `Canonical` | defining document, OCP-000 row and OCP-002 projection | candidate-local identity, lifecycle and deferred-question blockers in §23; exact OCP/Pattern prerequisites |
| OCP-011…OCP-015 | document `Accepted` | document `1.0.0 / Canonical` | document metadata and exact incorporated contract snapshot | direct OCP dependencies are pre-canonical; later extensions remain outside the accepted baseline |

OCP-016 is listed with the enabling group rather than OCP-011…OCP-015 because OCP-001 directly depends on it. That placement is dependency evidence, not a maturity ranking.

## 21. Lifecycle floors compared

Three direct-OCP dependency floors are credible enough to compare:

| Floor | Rule | Benefit | Failure pressure | AD-016A result |
|---|---|---|---|---|
| L0 — current-status floor | exact `Accepted` semantics may support a Canonical dependent even when the dependency document is Draft | smallest number of promotions | current `Depends-On` fields do not bind versions; a breaking `0.x` dependency change can silently alter the dependent's `1.x` promise | insufficient without a new exact-binding mechanism |
| L1 — Accepted-document floor | every direct OCP dependency must be at least document `Accepted` | separates reviewed contracts from drafts | Accepted remains pre-canonical and does not guarantee `1.x` compatibility | useful interim review floor, insufficient as the final compatibility floor |
| L2 — Canonical-or-same-act floor | every normative direct OCP dependency is Canonical in an earlier act or moves in the same atomic act | human-readable transitive compatibility and no unversioned Draft dependency laundering | more waves and a longer mixed-state interval | strongest current hypothesis |

AD-016A therefore uses L2 to test topology. A later act may permit an exception only if it proves that the listed dependency is reference-only, removes it from normative `Depends-On`, or introduces a separately governed exact compatibility binding. Repository order, commit recency and a passing downstream test are not such proof.

Artifact-class floors remain distinct:

- an ADR or AD dependency must be `Accepted` and remain governed by its own replacement/reopening rules; it never needs an invented Canonical state;
- an invoked Pattern must be `Accepted` and exact-version-bound through `Uses-Patterns`; it never needs an invented Canonical state;
- a Concept promotion requires its defining OCP document to become Canonical in the same act and requires atomic OCP-000/OCP-002 projection updates; and
- a non-Concept OCP promotion changes no Concept status by implication.

## 22. Strict dependency sequence under L2

The following slots are a topological proof, not a required PR grouping. Artifacts in one slot may still receive separate exact-head promotion PRs.

| Slot | Eligible artifacts | Why not earlier |
|---:|---|---|
| T0 | OCP-000 | root OCP dependency is Accepted ADR-000, which has no Canonical lifecycle |
| T1 | OCP-016 | directly depends on OCP-000 |
| T2 | OCP-001 | directly depends on OCP-000 and OCP-016 |
| T3 | OCP-002; P-001 to `Accepted` Pattern status | both depend on OCP-001; P-001 uses its own lifecycle |
| T4 | OCP-003 Resource; OCP-007 Organization; OCP-008 Objective; OCP-009 Capability | their OCP prerequisites are in T0–T3; OCP-007/OCP-008 also require exact Accepted P-001 |
| T5 | OCP-004 Operation; OCP-012 CapabilityClaimRecord | OCP-004 needs Resource and Objective; OCP-012 needs Resource, Capability and P-001 |
| T6 | OCP-005 Assignment; OCP-010 Event | both need Operation; Event also needs Objective and P-001 |
| T7 | OCP-006 Constraint | needs Assignment as well as Resource and Operation |
| T8 | OCP-011 OutcomeAssessmentRecord; OCP-013 Resource Interchangeability | OCP-011 needs Constraint and Event; OCP-013 needs Constraint, Assignment and OCP-012 |
| T9 | OCP-014 Coordination Profile | needs OCP-013 and its Concept/record prerequisites |
| T10 | OCP-015 Coordination Workflow | needs OCP-014 plus OCP-012/OCP-013 and exact Accepted P-001 |

This sequence demonstrates three things:

1. the graph has a cycle-free promotion path;
2. F names T0–T3, while C governs the complete T0–T10 strategy; and
3. F is therefore a useful named phase, but not a distinct terminal readiness model.

An accepted dependency-edge correction may change a slot. It must not be made merely to accelerate promotion.

## 23. Open-question classification by semantic effect

The audit uses:

- **B** — blocker for the named candidate because the answer can change identity, authority, invariant, dependency or wire-significant behavior inside its current scope;
- **S** — scoped exclusion or future extension already outside the current responsibility; and
- **C** — stale or completed question requiring cleanup, not a new semantic decision.

| Candidate | B — resolve before promotion | S — may remain explicitly outside `1.x` | C — clean up before final review |
|---|---|---|---|
| OCP-000 | compatibility meaning of the “Operational Space First” principle while Operational Space remains Proposed | future Proposed candidates and later compatible registry additions | none identified |
| OCP-001 | selected dependency floors, promotion units and atomicity rules from AD-016 | production deployment policy outside ontology governance | historical roadmap prose that no longer describes the current checker phase |
| OCP-002 | whether the top-level category tree is normative, stabilized, or explicitly excluded from the Canonical surface | future categories and Concepts admitted through OCP-016 | projections for already resolved Result, State/Readiness and Operational Area decisions are already current |
| P-001 | Pattern acceptance evidence and exact version treatment for six current invokers | future optional modules and new domain invokers | §11's future-tense extraction/evidence statement |
| OCP-003 Resource | `Unit` / Organization / Organizational Resource identity mapping where it affects the current Resource subtype contract | availability, Readiness, Resource Group, quantity/reservation and implementation mechanisms | none identified |
| OCP-004 Operation | current lifecycle/authorization/composition questions that can change existing stages, transition validity, parent/child or terminal behavior | templates, reusable spatial identity, domain geometry/environment, future State/Readiness and separate conflict models | resolved Operational Area wording is already current |
| OCP-005 Assignment | amendment, retroactivity, interval and replacement overlap/gap rules that alter present lifecycle/history guarantees | Reservation, quantity, role taxonomy, coordination roles and future availability/Readiness | obsolete reference to reconsidering superseded ADR-DRAFT-007 |
| OCP-006 Constraint | predicate-expression compatibility, precedence/override/waiver and evaluation-freshness/storage choices where they change current result behavior | future Conflict, quantity/capacity, Readiness and domain geometry/spectrum semantics | none identified |
| OCP-007 Organization | identity continuity and relationship-class stability; Organization/Resource mapping where it changes current identity | commander/personnel, staff, ownership, domain hierarchy exceptions and implementation contracts | backlog questions already resolved elsewhere must be marked as such rather than carried indefinitely |
| OCP-008 Objective | semantic-equivalence rules for correction/supersession if they change stable Objective identity | typed relations, separate lifecycle and future outcome taxonomy | Result/assessment questions now owned by Accepted OCP-011 |
| OCP-009 Capability | compatibility policy for references to superseded exact versions | domain taxonomy, storage/API and Operation requirement semantics | holder claim and AB-011 questions now have OCP-012/OCP-013 owners |
| OCP-010 Event | none found inside the accepted occurrence/observation identity baseline | temporal interval, kind registry, correlation and Operation-to-Event relation | assessment-target question now owned by Accepted OCP-011 |
| OCP-011…OCP-016 | no unresolved question found that invalidates each narrow Accepted baseline | named future target kinds, profiles, activations and machine projections remain separate reopening/extension cycles | wrapper language may be editorially normalized during its own readiness audit |

This classification is deliberately stricter than counting headings. A candidate remains blocked by one B item even if every S item is well bounded. A Board act may reclassify an item only with a written compatibility argument.

## 24. Outcome comparison

| Outcome | Dependency coherence | Human compatibility story | Treatment of current blockers | Review/migration pressure | Comparison result |
|---|---|---|---|---|---|
| A — hold | preserves the current graph without a new promise | clear only if exact reopening gates are named | safest immediate state, but resolves none | low now; indefinite drift if retained without triggers | admissible control and current execution state, not the leading long-term strategy |
| B — atomic baseline | coherent only through one very large same-act closure | one baseline is simple after merge | weakest artifact blocks all others or is pressured through | highest review surface, rollback and mixed lifecycle burden; P-001 still cannot become Canonical | not preferred under current evidence |
| C — dependency-layered waves | strongest under L2 and the T0–T10 proof | each wave states what earlier `1.x` promises it consumes | blockers stay local to the affected wave | more PRs and a visible mixed interval | leading complete strategy |
| D — selective per artifact | coherent only if every selected artifact still satisfies L2 | difficult without published wave/dependency context | local blockers stay local | smallest PRs, but unconstrained selection launders pre-canonical dependencies | viable only as one-artifact wave granularity inside C |
| E — stable-kernel extraction | can remove unstable text from a candidate surface | clear if one defining location is preserved | useful for OCP-000/OCP-002 if normative/excluded text cannot be separated in place | restructuring, reference migration and duplicate-authority risk | remedial technique, not a foundation-wide default |
| F — enabling baseline | closes the shared root prerequisites T0–T3 | strong first-phase explanation | exposes root blockers without pre-approving Concepts | cannot answer what follows by itself | strong first phase of C, not a terminal alternative |

## 25. Counterexample mapping — cases 1–10

| # | A | B | C | D | E | F |
|---:|---|---|---|---|---|---|
| 1 | keep statuses | pair blocked | pair in its slot | pair only | exclude or stabilize definition | not reached |
| 2 | keep statuses | same-act dependency | earlier/same L2 | blocked unless L2 | split only with one owner | roots only |
| 3 | keep statuses | accept exact P-001 in act | P-001 at T3 | invoker waits | no Pattern bypass | P-001 is explicit root obligation |
| 4 | reject invented status | reject invented status | Pattern becomes Accepted only | same | same | same |
| 5 | preserve row statuses | bulk act preserves rows independently | OCP-000 promise separates document/rows | same | registry kernel may exclude candidate semantics | handled at T0 |
| 6 | named B gate | blocks whole act | blocks candidate wave | blocks candidate | excluded text cannot hide identity question | root B gate if applicable |
| 7 | scoped exclusions survive | no weakest-member inference | no block when exclusions are honest | same | may remain outside kernel | same |
| 8 | no production claim | no production claim | semantic wave states limit | same | kernel states limit | enabling baseline states limit |
| 9 | may retain hold only with exact rationale | may define semantic-only baseline | semantic-only candidate remains possible | same | same | same |
| 10 | no promotion | weakest member blocks B | weak artifact delays only its wave | selected artifact still meets L2 | split cannot manufacture readiness | downstream not pre-approved |

## 26. Counterexample mapping — cases 11–20

| # | A | B | C | D | E | F |
|---:|---|---|---|---|---|---|
| 11 | no new mixed promise | one cut | wave ledger explains mix | must publish L2 context or reject | exact kernel references | explicit enabling/downstream boundary |
| 12 | no split | no split | no split required | no split required | one owner plus migrated references or reject | no split required |
| 13 | no version change | atomic metadata/projections | atomic per candidate | atomic per candidate | atomic for kernel owner | atomic enabling documents only |
| 14 | no implication | explicit Concept acts inside bulk act | paired Concept/document act | paired act | kernel document cannot auto-promote Concept | no downstream Concept promotion |
| 15 | preserve Proposed rows | preserve rows | preserve rows | preserve rows | registry kernel preserves status field | explicit T0 obligation |
| 16 | reopening still explicit | bulk act cannot reopen | wave cannot reopen | selection cannot reopen | extraction cannot reopen | enabling act cannot reopen |
| 17 | domain remains outside | bulk act excludes domain profile | OCP-016 extension route preserved | same | kernel excludes profile authority | same |
| 18 | forbidden selector | forbidden selector | topology is not authority | per-artifact readiness is evidence-based | extraction is not maturity proof | enabling label is not readiness proof |
| 19 | no new SemVer claim | one reviewed `1.0.0` cut | each wave states its `1.x` surface | each act does so | old references migrate explicitly | roots define their own surface only |
| 20 | non-implications stay explicit | stated once and per artifact | stated per wave/artifact | stated per act | stated for kernel only | enabling status does not imply downstream truth/readiness |

All six outcomes can satisfy the counterexamples without a new registry or sensitive data. The deciding difference is not evidence availability; it is the amount and location of compatibility authority each outcome asks one act to carry.

## 27. Semantic and production evidence boundary

For a semantic Canonical act, the repository can require:

- readable identity, responsibility, exclusions and compatibility text;
- exact direct dependencies and Pattern invocations;
- atomic lifecycle and projection changes;
- synthetic positive, negative, ambiguity and replay evidence for mechanically expressible rules;
- full-history governance checks; and
- external exact-head falsification plus Board authorization.

It cannot honestly require production deployment, persistence, API, security, scale or observability evidence unless the candidate's own current responsibility promises those properties. Missing production artifacts therefore do not block a narrowly semantic `1.x` contract by default. They do block any text that claims production interoperability or operational fitness.

Outcome A remains free to argue that a particular semantic contract is not useful enough to canonicalize without a production consumer. That argument must identify the affected compatibility promise; “no production API exists” is not an automatic fail rule.

## 28. Decision-separating strategy set

AD-016A reduces the six labels to five Board choices without selecting one:

### R0 — retain A

Keep all current states and name the exact B items that must close before another comparison.

### R1 — select B

Prepare one atomic baseline only after every included artifact independently satisfies the same declared floor and the Pattern lifecycle difference is explicit.

### R2 — select C under L2

Use the T0–T10 topology, with each actual promotion as a separate reviewed act or an explicitly atomic same-slot group.

### R3 — select D as micro-wave C

Allow one-artifact waves, but preserve L2 and the published dependency ledger. Pure unconstrained selective promotion is not admissible.

### R4 — select F → C, with E only where needed

Treat T0–T3 as the enabling phase, then reassess and continue the C topology. Use kernel extraction only when a candidate cannot otherwise state one exact normative surface.

R4 differs from R2 in governance commitment, not graph structure: R4 authorizes only the enabling phase before mandatory reassessment; R2 accepts the whole layered strategy while every promotion still needs its own act.

## 29. Preferred hypothesis and unresolved proof

AD-016A does not make a Board selection. Current evidence supports this ordering for external attack:

- **R4 (`F → C`) is the leading cautious hypothesis.** It resolves shared lifecycle roots first, does not pre-approve a Concept, and requires reassessment before T4.
- **R2 (complete C under L2) is the leading simpler strategy** if the Board is prepared to commit to the full topology now.
- **R3 is useful only as PR granularity within C.** Without L2 it creates an unintelligible mixed compatibility surface.
- **E is a targeted repair**, especially for OCP-000/OCP-002, not evidence that every document needs extraction.
- **A is the honest current execution state** until a later act selects a strategy and candidate-local B items close.
- **B has no demonstrated benefit large enough to justify weakest-member and rollback pressure.**

External review should try to falsify the leading hypothesis by constructing:

1. a reason OCP-000 cannot become Canonical while preserving independent Proposed rows;
2. a reason the OCP-002 working hypothesis cannot be cleanly stabilized or excluded;
3. a safe current mechanism by which a Canonical dependent can consume a changing unversioned pre-canonical OCP dependency, disproving L2;
4. a reason P-001 may remain Draft while a Canonical invoker exact-binds it;
5. a real dependency cycle or omitted artifact in T0–T10;
6. a candidate for which D is coherent but cannot be expressed as a small C wave;
7. evidence that a foundation-wide E split reduces rather than duplicates authority; or
8. a production property already promised by a candidate that the semantic-only boundary incorrectly excludes.

## 30. AD-016A status and next act

Revision `0.2.0` completes the initial comparison while AD-016 and AB-062 remain `Discovery`. It changes no OCP, Concept, Pattern, dependency, registry row, graph edge, schema, checker rule, fixture, status or `1.0.0` version.

After external review, a separate `AD-016B` Architecture Board act may select R0–R4, require another comparison, or state a different composition with exact precedence. Selection does not itself promote any artifact. Every T0–T10 promotion remains a later exact-head reviewed PR with its own human-readable compatibility surface and explicit owner authorization.

## 31. Architecture Board decision — AD-016B

The Architecture Board accepts this decision by act **AD-016B** on **2026-08-05**, after Fable reviewed the complete AD-016A comparison on exact head `d596788f6f7683e7a31e37b553e50a99737c830b`, independently verified the inventory, L2 argument, T0–T10 topology, open-question classifications and twenty-by-six counterexample matrix, found no defects and recommended merge. Codex independently accepted that verdict, Pavlo authorized the merge, and PR #81 was squash-merged with exact tree identity and green post-merge CI.

This act selects a canonicalization strategy and dependency floor. It does not make any OCP or Concept Canonical, make P-001 Accepted, change a version to `1.0.0`, resolve a candidate-local blocker, amend a dependency, create a registry or schema, add a graph edge, or change checker behavior.

### 31.1 Selected strategy — R4 (`F → C`)

AD-016 selects **R4 — the F enabling phase followed by the C dependency-layered strategy, with E available only where a candidate needs a clean normative/excluded split**.

F is not a separate terminal model. It names the shared-root phase T0–T3 of the same dependency graph governed by C. R4 is selected instead of committing to complete R2 because the evidence is sufficient to stabilize the enabling roots, but §23 still identifies candidate-local blockers that must be audited before any T4 Concept/document pair moves.

The selected strategy therefore has a mandatory governance boundary:

1. complete separately reviewed T0–T3 acts;
2. preserve the exact post-enabling baseline;
3. run a new AD-016C comparison against the remaining T4–T10 artifacts and their then-current blockers; and
4. require a separate AD-016D Board act before the first T4 promotion.

Successful T0–T3 completion is evidence for reassessment, not proof that any downstream Concept or non-Concept contract is ready.

## 32. Selected lifecycle floor — L2

AD-016B selects **L2 — Canonical-or-same-act** for normative direct OCP dependencies:

- a Canonical OCP may depend normatively only on an OCP already Canonical or promoted in the same atomic act;
- a same-act group must still give every included artifact its own readiness evidence and compatibility surface;
- a Draft or merely Accepted OCP cannot supply an unversioned changing semantic dependency to a `1.x` promise; and
- topological eligibility is necessary but never sufficient for promotion.

An exception requires a separate reviewed change that proves one of two conditions:

1. the reference is non-normative and is removed from `Depends-On`; or
2. a human-readable exact compatibility-binding contract preserves the consumed semantics independently of the dependency's document lifecycle.

No exception may be inferred from a commit SHA, current test success, document order, version recency, reviewer count or downstream popularity.

Artifact-class floors remain those established in §21:

- Accepted ADR and AD decisions remain governed by replacement/reopening, not an invented Canonical status;
- an invoked Pattern must be Accepted and exact-version-bound, never Canonical under the current Pattern lifecycle;
- a Canonical Concept moves atomically with its defining Canonical document and OCP-000/OCP-002 projections; and
- a non-Concept OCP promotion changes no Concept status by implication.

## 33. Authorized strategy scope — T0 through T3

AD-016B authorizes preparation of the following promotion cycles in dependency order. It does not authorize their merge or lifecycle effects.

| Slot | Candidate cycle | Required gate before its promotion act |
|---:|---|---|
| T0 | OCP-000 | define the stable registry `1.x` surface; preserve independent Proposed rows; resolve whether “Operational Space First” is a non-identity principle or an undefined semantic dependency |
| T1 | OCP-016 | exact-bind its incorporated human baseline and consume Canonical OCP-000 without importing Concept-row status |
| T2 | OCP-001 | incorporate the selected L2 rule, R4 choreography, atomic projection requirements and separate-Board-act boundary without duplicating OCP-016 routing |
| T3 | OCP-002 | stabilize or explicitly exclude the working-hypothesis category tree while preserving exact Concept projections |
| T3 | P-001 | receive a separate Pattern acceptance act at an exact reviewed version; update every invocation atomically if that version changes |

Each row is its own default PR. Same-slot grouping is allowed only when the proposal proves that atomicity reduces rather than hides review and rollback risk.

The T0 act is the next cycle. It must remain a Draft until its exact compatibility surface and blockers are reviewed. AD-016B does not pre-authorize `OCP-000 1.0.0 / Canonical`; owner authorization of this selection PR cannot be reused as authorization of T0.

## 34. Blocker, exclusion and evidence rules

The B/S/C classification in §23 remains binding review input:

- one unresolved B item stops its candidate even if every test passes;
- an S item may remain only when the `1.x` contract states the exclusion and later change can follow SemVer plus OCP-016 without changing current guarantees;
- a C item must be cleaned up so readers do not mistake completed work for an unresolved semantic question; and
- a checker result cannot change B, S or C classification.

Every T0–T3 proposal must carry:

1. one readable compatibility surface;
2. exact direct dependencies and artifact-class floors;
3. explicit non-implications, including `Canonical ≠ production-ready, authorized, true, complete or immutable`;
4. migration and rollback accounting for status, version, registry projections and Pattern invocations;
5. human counterexamples plus executable evidence for mechanically expressible claims; and
6. separate Fable exact-head review, Codex adjudication, green CI and Pavlo or Board authorization.

Missing production API, persistence, security, scale or deployment evidence is not an automatic blocker for a narrowly semantic contract. A candidate that promises such a property must prove it or remove the promise from the proposed surface.

## 35. Mandatory post-enabling reassessment

After T0–T3, AD-016C must recompute rather than copy:

- exact document, Concept, Pattern and dependency states;
- the remaining T4–T10 topology;
- every candidate-local B/S/C classification;
- whether L2 created avoidable coupling or exposed missing exact-binding needs;
- whether E was required and preserved one defining location;
- semantic versus production evidence boundaries; and
- the compatibility and migration cost of the first proposed T4 wave.

AD-016C may recommend continuing C, using D-sized micro-waves inside C, applying E to a named candidate, retaining current states or reopening the strategy. It may not infer continuation from schedule, sunk cost, number of completed roots or green CI.

No T4 artifact may enter a promotion PR before the AD-016C comparison and separate AD-016D Board decision are merged. Discovery or remediation work on T4 blockers may proceed, but it grants no promotion authority.

## 36. Alternatives not selected and reopening gates

### 36.1 R0 — indefinite hold

R0 is not selected as the strategy because the root blockers are finite and the T0–T3 dependency path is testable. The repository nevertheless remains at its current statuses until each later act is separately authorized. R0 may be reconsidered if T0 cannot state a stable registry surface without resolving currently unowned identity or authority questions.

### 36.2 R1 — atomic foundation baseline

R1 is not selected because P-001 has a distinct lifecycle, candidate maturity is uneven and one large act would couple rollback and weakest-member pressure across all artifacts. It may be reconsidered only if later evidence proves a compatibility property that cannot survive layered promotion and shows how every included artifact remains independently reviewable.

### 36.3 R2 — commit now to complete C

R2 is not selected because T4–T10 candidate-local blockers have not yet been audited against a completed enabling baseline. It may be selected after AD-016C if that audit shows that the full remaining topology can be governed without another strategic branch.

### 36.4 R3 — selective promotion

Unconstrained D/R3 remains rejected because it can launder pre-canonical dependency semantics. One-artifact PRs remain available as micro-waves inside L2/C; PR size does not create a different dependency strategy.

### 36.5 E — stable-kernel extraction

E remains a conditional repair, not a default restructuring mandate. A candidate may use it only when in-place normative/excluded labeling cannot state one compatibility surface. The split must preserve one defining location and exact reference migration; convenience or shorter prose is insufficient.

L2 itself may be reopened only by the exact compatibility-binding evidence described in §32. A weaker floor cannot be selected merely because T0–T3 takes longer than expected.

## 37. Accounting and accepted effect

This Board act has the following narrow effects:

- AD-016 becomes `0.3.0 / Accepted`;
- R4 (`F → C`) becomes the selected canonicalization-readiness strategy;
- L2 becomes the selected direct-OCP dependency floor;
- preparation authority covers only T0–T3, with T0 OCP-000 as the next separately reviewed cycle;
- AD-016C reassessment and a separate AD-016D Board act become mandatory before T4;
- E remains an explicit candidate-local repair with one-owner safeguards;
- AB-062 moves `Discovery → Planned` for the T0–T3 enabling phase; and
- no OCP, Concept, Pattern, dependency, registry row, graph edge, schema, checker rule, fixture, status or `1.0.0` version is changed by this act.

Exact-head Fable approval, Codex adjudication, green CI and explicit Pavlo or Architecture Board authorization remain mandatory before squash merge. Until that merge, §§31–37 are a proposed Board act rather than an accepted decision.
