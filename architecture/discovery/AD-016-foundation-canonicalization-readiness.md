---
Decision-ID: AD-016
Title: Foundation Canonicalization Readiness Discovery
Version: 0.9.0
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-016, P-001, AD-015
Applies-To: AB-062, OCP document lifecycle, Concept lifecycle, Pattern dependencies, canonicalization waves
Review-After: Preflight Capability-status correction before K8 authoring; then completion or failure of the OCP-008/Objective lifecycle proposal before any third T4 scope
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

## 38. AD-016C reassessment mandate and exact baseline

AD-016C recomputes the remaining readiness question on exact post-enabling baseline `main@645b22b27be8ff004bd98e4b918403335f300278`. It does not copy the pre-enabling conclusions in §§20–29 as current facts.

The completed enabling phase provides:

- OCP-000, OCP-016, OCP-001 and OCP-002 at `1.0.0 / Canonical`;
- P-001 at `0.1.0 / Accepted`, with six current primary invokers and unchanged exact bindings;
- L2 enforced mechanically for direct OCP dependencies;
- eight `Accepted` Concepts and no `Canonical` Concept;
- five `Accepted` non-Concept contracts, OCP-011 through OCP-015;
- a cycle-free direct dependency graph; and
- 161 unit tests plus 115 non-sensitive fixtures as mechanically expressible evidence.

These facts remove the shared root blockers. They do not prove any T4 candidate ready, select a first wave or transfer the authorizations used for T0–T3.

## 39. Exact remaining lifecycle inventory

| Slot | Artifact | Current document state | Concept state | Current L2 position |
|---:|---|---|---|---|
| T4 | OCP-003 Resource | `0.6.0 / Draft` | `Accepted` | root OCP dependencies are Canonical |
| T4 | OCP-007 Organization | `0.3.2 / Draft` | `Accepted` | root OCP dependencies are Canonical; P-001 is Accepted and exact-bound |
| T4 | OCP-008 Objective | `0.2.1 / Draft` | `Accepted` | root OCP dependencies are Canonical; P-001 is Accepted and exact-bound |
| T4 | OCP-009 Capability | `0.1.2 / Draft` | `Accepted` | root OCP dependencies are Canonical |
| T5 | OCP-004 Operation | `0.8.0 / Draft` | `Accepted` | waits for Resource and Objective |
| T5 | OCP-012 CapabilityClaimRecord | `0.3.0 / Accepted` | not a Concept | waits for Resource and Capability; P-001 is ready |
| T6 | OCP-005 Assignment | `0.2.2 / Draft` | `Accepted` | waits for Resource and Operation |
| T6 | OCP-010 Event | `0.2.0 / Draft` | `Accepted` | waits for Operation and Objective; P-001 is ready |
| T7 | OCP-006 Constraint | `0.2.2 / Draft` | `Accepted` | waits for Resource, Operation and Assignment |
| T8 | OCP-011 OutcomeAssessmentRecord | `0.3.0 / Accepted` | not a Concept | waits for Operation, Constraint, Objective and Event; P-001 is ready |
| T8 | OCP-013 Resource Interchangeability | `0.2.0 / Accepted` | not a Concept | waits for Resource, Assignment, Constraint and OCP-012 |
| T9 | OCP-014 Coordination Profile | `0.2.0 / Accepted` | not a Concept | waits for T4–T8 semantic dependencies |
| T10 | OCP-015 Coordination Workflow | `0.2.0 / Accepted` | not a Concept | waits for Assignment, Constraint and OCP-012–OCP-014; P-001 is ready |

No dependency edge changed during T0–T3, so the remaining T4–T10 topology in §22 is still cycle-free and topologically correct. Earlier-slot eligibility remains necessary, not sufficient.

## 40. Recomputed blocker, scope and cleanup audit

The B/S/C meanings remain those in §23. This table is the current audit and supersedes §23 only for post-enabling decisions.

| Candidate | B — must resolve before its promotion | S — may remain explicitly outside `1.x` | C — cleanup required, not a new decision |
|---|---|---|---|
| OCP-003 Resource | whether `Organizational Resource` and `Unit` are Resource identities, projections or only working taxonomy; the answer affects current subtype and identity text | availability, Resource Group, quantity/reservation and implementation mechanisms | none identified |
| OCP-007 Organization | identity continuity through merger/split/reorganization; stable class/type rules for current relationship records; Organization/Resource mapping wherever it changes identity | commander/personnel, staff, ownership, domain hierarchy exceptions and implementation contracts | replace the obsolete phrase “Coordination as a future Concept” and distinguish unresolved AB items from completed downstream contracts |
| OCP-008 Objective | who classifies a same-identity editorial correction and what immutable evidence prevents semantic change from bypassing supersession | typed relations, separate lifecycle, outcome taxonomy and domain equivalence policies outside Core | Event/Result future-tense and the assessment question now owned by OCP-010/OCP-011 |
| OCP-009 Capability | **none found inside the current definition/registry surface** | Operation requirement owner, domain taxonomy, and any domain policy that forbids new use of an exactly resolvable superseded version | holder-claim and AB-011 questions now owned by OCP-012/OCP-013 |
| OCP-004 Operation | authorization source, parent/child rules, minimum Planned data, lifecycle/terminal behavior and unfinished-Assignment alignment where they alter current transitions or composition | templates, reopened reusable spatial identity, domain geometry/environment and separate Conflict/Readiness models | wording that still defers work to already existing Constraint and superseded ADR-DRAFT-007 stages |
| OCP-012 CapabilityClaimRecord | none found inside the narrow accepted attributable-claim baseline | independent assessment, Organization holders and new claim kinds remain separately gated | historical “AB-011 next” wording must be reconciled with Accepted OCP-013 without rewriting the recorded act |
| OCP-005 Assignment | amendment and retroactivity; interval multiplicity; replacement overlap/gap; terminal Operation alignment where they alter lifecycle/history | Reservation, quantity, role taxonomy, coordination roles and availability/Readiness | obsolete reconsideration reference to superseded ADR-DRAFT-007 |
| OCP-010 Event | none found inside the occurrence/ObservationRecord baseline | interval, kind registry, correlation and Operation-to-Event relation | AB-056/OutcomeAssessmentRecord future-tense now owned by Accepted OCP-011 |
| OCP-006 Constraint | predicate compatibility; precedence/override/waiver; evaluation freshness and stored-versus-derived authority where they alter result behavior | future Conflict, quantity/capacity and domain geometry/spectrum semantics | stale deferrals to PR-0006 and superseded ADR-DRAFT-007 |
| OCP-011 OutcomeAssessmentRecord | none found inside the narrow accepted assessment baseline | new target/criterion kinds and future activations | none identified; historical act text remains clearly separated from current revision |
| OCP-013 Resource Interchangeability | none found inside the narrow accepted directional-eligibility baseline | additional consumers and separate selection/replacement workflows | “next Coordination profile” language is now completed by OCP-014 |
| OCP-014 Coordination Profile | none found inside the narrow accepted consumer-profile baseline | future workflows, authority and agreement semantics | AB-058 next-cycle language is complete through OCP-015 |
| OCP-015 Coordination Workflow | none found inside the narrow accepted evidence baseline | future authority, visibility or agreement extensions remain separately gated | AB-059 next-cycle language is complete through AD-010 |

The changed OCP-009 classification is evidence-based, not momentum-based. Its exact resolver already preserves a superseded Capability version without redirect, while a domain policy may separately forbid new references. The unresolved policy therefore does not change Core identity or exact resolution and is S, not B. Holder claims and Resource interchangeability now have accepted separate owners and are C cleanup in OCP-009.

## 41. L2 and exact-binding audit

L2 did not create a dependency cycle or force a mixed-lifecycle exception during T0–T3. It exposed a real distinction:

- a current normative `Depends-On` consumes the dependency artifact as a changing semantic authority; and
- a claim that only one stable fragment is consumed needs either removal of an unnecessary dependency or a separately governed exact compatibility binding.

No remaining candidate currently proves that its listed dependency is reference-only. The waiting edges are therefore not classified as avoidable merely because they delay promotion. A candidate-local remediation may narrow an edge, but it must name the consumed semantics and pass external review; green tests, exact commits or current wording are insufficient.

L2 should remain the comparison floor unless AD-016D receives concrete counterevidence. The first T4 candidate identified below already satisfies L2 without an exception, so weakening the floor would not reduce its cost.

## 42. Stable-kernel extraction audit

T0 OCP-000 and T3 OCP-002 achieved readable stable surfaces in place. E was not required and no second normative owner was created.

For the remaining candidates:

- OCP-009 has one coherent definition/registry surface and does not need E;
- OCP-003 is the first named E candidate if its working taxonomy cannot be explicitly excluded or stabilized in place, because the `Organizational Resource` branch currently touches identity text;
- OCP-007 may justify a later Concept-kernel/relationship-contract split only if one defining location and exact migrated references are demonstrated; extraction cannot hide unresolved Organization identity continuity; and
- OCP-008 should first resolve its editorial-correction authority in place because extraction would not remove that identity question.

E remains a repair with a falsifiable trigger, not a maturity label or default document-shortening exercise.

## 43. Semantic and production evidence boundary after enabling

The remaining contracts promise semantic identity, authority, lifecycle, exact-reference and derivation behavior. They do not promise a production API, persistence model, authentication, deployment, scale, observability or domain-complete vocabulary.

Missing production evidence is therefore not a blocker unless a promotion proposal adds such a promise. Conversely, executable fixtures do not settle a B item about identity or authority. Every future compatibility surface must say which claims are human-reviewed, which are mechanically witnessed and which remain explicitly out of scope.

## 44. Compatibility and migration cost of the first credible T4 wave

OCP-009 Capability is the only T4 candidate with no recomputed B item. A one-candidate T4 micro-wave would require an atomic proposal with:

1. OCP-009 `0.1.2 / Draft → 1.0.0 / Canonical`;
2. Capability `Accepted → Canonical` in its defining metadata, the OCP-000 registry row and the exact OCP-002 status projection;
3. a readable `1.x` surface preserving exact `(namespace, capability_id, version)` identity, one namespace owner, exact resolution, history-preserving supersession and every non-equivalence with holder possession, Readiness, availability, authorization and interchangeability;
4. cleanup of resolved holder-claim and AB-011 questions without importing OCP-012/OCP-013 authority;
5. explicit retention of domain policy over whether new references may use an exactly resolvable superseded version;
6. no P-001, Concept dependency, graph-edge, schema, fixture or downstream document-version change; and
7. rollback as the same atomic document/status/projection unit.

OCP-009 directly depends only on Canonical OCP-000/OCP-001/OCP-002 and Accepted AD-005. Its current consumers do not bind the OCP document version, and its Capability references already bind exact Capability definition versions. The migration cost is therefore four normative projections plus repository accounting, not data migration or consumer rebinding.

The main risk is semantic overreach: treating exact resolution of a superseded version as universal permission for new use. The promotion surface must preserve exact resolution while leaving admission policy with the governed domain consumer.

## 45. Post-enabling strategy options

AD-016C compares five fair next-step options without selecting one:

| Option | Next action | Benefit | Main risk | Reassessment result |
|---|---|---|---|---|
| G0 — hold | retain all T4 states and remediate blockers | lowest immediate lifecycle risk | leaves the one unblocked candidate idle without new evidence | admissible control |
| G1 — full T4 slot | wait until OCP-003/OCP-007/OCP-008 blockers close, then promote all four | one visible Concept wave | couples independent rollback and lets three blocked candidates govern one ready candidate | not preferred |
| G2 — D-sized micro-waves inside C | let AD-016D authorize one separately reviewed candidate at a time under L2, starting with OCP-009 if its promotion evidence holds | preserves topology, local blockers and rollback | mixed T4 interval needs clear public accounting | leading hypothesis |
| G3 — E repair before T4 | extract a stable kernel for a named blocked candidate first | may isolate a genuinely stable surface | duplicate authority or hiding a B item | conditional for OCP-003/OCP-007, unnecessary for OCP-009 |
| G4 — reopen strategy or L2 | require new compatibility evidence before any T4 | correct if enabling exposed a contradiction | weakens safeguards for schedule or sunk cost without present counterevidence | no current trigger found |

G2 is not unconstrained selective promotion. It is the D-sized execution granularity already permitted inside the selected C topology: every candidate must satisfy L2, its own B/S/C audit, atomic projections, exact-head review and separate authorization.

## 46. Falsification targets and stop rules

External review should try to demonstrate:

1. an unresolved OCP-009 question that changes its current identity, registry authority or exact resolver;
2. a direct OCP-009 dependency below the L2 floor;
3. a downstream reference that must migrate when the OCP document moves to `1.0.0`;
4. a hidden Pattern invocation or Concept dependency edge in the proposed first wave;
5. a reason superseded-version domain admission must be owned by Core resolution;
6. a safe OCP-003, OCP-007 or OCP-008 `1.x` surface that disproves the named B item without silently excluding current normative text;
7. an avoidable L2 edge with an already governed exact compatibility binding;
8. a topology cycle or omitted remaining artifact;
9. a production property already promised by the first candidate but excluded from its evidence plan;
10. a reason G2 cannot be represented as C micro-wave granularity;
11. an E split that preserves one defining owner and is necessary before OCP-009; or
12. any inference based on completed-root count, elapsed time, green CI, reviewer count or sunk cost.

If targets 1–5 succeed, OCP-009 is not a credible first wave and G0 or remediation becomes leading. If target 7 or 10 succeeds, AD-016D must reopen the floor or strategy explicitly. No failed test may be converted into a permissive default, and no passing test may erase a semantic B item.

## 47. AD-016C recommendation and next act

Revision `0.4.0` records the AD-016C reassessment and recommends **G2 — D-sized micro-waves inside C, with OCP-009 Capability as the first candidate for a separate T4 promotion act**. G0 remains the honest control; E remains conditional for named blocked candidates.

This recommendation is not an Architecture Board selection and does not authorize OCP-009 or any other T4 proposal. A separate AD-016D act must accept, reject or amend the recommendation and state exact preparation scope. Authorization to merge AD-016C accepts only this comparison; it cannot be reused for AD-016D or a promotion act.

AD-016C changes no OCP, Concept, Pattern, status projection, dependency, registry row, graph edge, schema, checker rule or fixture. AB-062 remains `Planned`. Until AD-016C and AD-016D are separately reviewed, authorized and merged, no T4 artifact may enter a promotion PR.

## 48. Architecture Board selection proposal — AD-016D

AD-016D uses the accepted AD-016C comparison as its evidence input. Fable reviewed exact AD-016C head `895b138864cf395410f639615bef7a2a40827ef8`, reproduced the inventory and executable checks, found zero findings and approved the comparison. Codex accepted that verdict, Pavlo authorized AD-016C only, and PR #88 was squash-merged as `b0ae0636d01a5e35c87bc4620314e6491b3b89d5` with byte-identical reviewed/merged tree `70546fc7272a41882cbb339bd4a9660edfead135` and green post-merge CI.

That evidence does not select G2 by itself. The Architecture Board selects only through separate explicit authorization and merge of an exact-head reviewed AD-016D proposal.

This act decides preparation scope. It does not change an OCP or Concept lifecycle, merge a T4 promotion, resolve a candidate-local blocker or transfer authorization to a later PR.

## 49. Selected direction — G2 inside C/L2

AD-016D selects **G2 — D-sized micro-waves inside the existing C topology under L2**.

The selected rule is:

1. one candidate may be prepared only when its own B set is empty;
2. every earlier normative OCP dependency must already be Canonical or move in the same justified atomic act;
3. document and Concept lifecycle projections move together where the candidate defines a Concept;
4. each micro-wave has its own readable compatibility surface, rollback unit, exact-head review and owner authorization;
5. a successful candidate does not confer readiness or authorization on a sibling or downstream candidate; and
6. mixed lifecycle inside one topological slot must remain visible in repository accounting.

G2 is not unconstrained selective promotion. The published T4–T10 topology, L2 floor, B/S/C audit and one-candidate authorization boundary remain binding.

## 50. Authorized preparation scope — OCP-009 only

AD-016D authorizes preparation of one separate draft proposal for the OCP-009 Capability document/Concept pair. It authorizes neither Ready state nor merge of that proposal.

The exact pre-promotion baseline is:

- repository: `main@b0ae0636d01a5e35c87bc4620314e6491b3b89d5`;
- OCP-009 Git blob: `b28219bffef4e527507d495c34dded5c2fb79346`;
- OCP-009 SHA-256: `119a26424b4c62140446fee6eca8d9baf68b2cd875e565321d63b1cc8064ddbb`;
- document: `0.1.2 / Draft`;
- Capability Concept: `Accepted` in the defining metadata and OCP-000/OCP-002 projections;
- direct dependencies: Canonical OCP-000/OCP-001/OCP-002 and Accepted AD-005; and
- Pattern invocation and Concept dependencies: none.

Preparation authority does not include OCP-003 Resource, OCP-007 Organization or OCP-008 Objective. Discovery or remediation of their B items may proceed, but no promotion draft for those candidates is authorized by this act.

## 51. Mandatory OCP-009 proposal contract

The separate T4 proposal must carry one atomic, human-readable act that:

1. changes OCP-009 `0.1.2 / Draft → 1.0.0 / Canonical`;
2. changes Capability `Accepted → Canonical` in the defining metadata, OCP-000 registry row and exact OCP-002 projection;
3. preserves exact Capability identity as `(namespace, capability_id, version)` and never introduces latest-version, timestamp, record-order, publisher-count or popularity authority;
4. preserves one namespace owner, exact fail-closed resolution, historical exact-version resolution and non-redirecting supersession;
5. states explicitly that exact resolution of a superseded version is not permission or domain admission for new use;
6. keeps holder claims in OCP-012, Resource interchangeability in OCP-013 and Operation requirements with a future exact owner;
7. preserves `Capability ≠ holder possession, Readiness, availability, capacity, authorization, admissibility, Assignment eligibility or Resource interchangeability`;
8. cleans resolved holder-claim and AB-011 questions without rewriting their accepted downstream authorities;
9. changes no P-001 invocation, Concept dependency, graph edge, checker rule, fixture, consumer document version or Capability definition version;
10. provides explicit status/projection rollback as the inverse of the same atomic unit; and
11. includes human counterexamples plus the existing executable evidence for mechanically expressible exact-resolution claims.

If authoring or review reveals a B item, required consumer rebinding, hidden semantic change or L2 violation, the proposal must stop and return to G0/remediation. The Board may not waive that stop because AD-016D named OCP-009 first.

## 52. Alternatives and reopening gates

AD-016D does not select:

- **G0 as the active direction** because one candidate currently passes the recomputed gates; G0 remains the mandatory fallback on failed evidence;
- **G1 full T4 slot** because three candidates retain independent B items and one combined rollback unit would create weakest-member pressure;
- **G3 as a prerequisite** because OCP-009 has one coherent defining surface and does not need extraction; E remains available only for a named later candidate under the §42 safeguards; or
- **G4 reopening of R4/L2** because AD-016C found no cycle, exception need or exact-binding counterexample that would reduce the first candidate's cost.

G2 or L2 must be reopened if the OCP-009 proposal exposes a required pre-canonical OCP dependency, a compatibility promise that cannot survive one-candidate rollback, or an unavoidable same-slot atomicity requirement. Schedule, authoring effort, green CI, reviewer count or completed-root count is not reopening evidence.

## 53. Boundary after the first micro-wave

Even if OCP-009 later becomes Canonical:

- OCP-003, OCP-007 and OCP-008 retain their current statuses and B items;
- OCP-012 still cannot satisfy L2 until OCP-003 Resource is Canonical or an exact candidate-local dependency correction is separately accepted;
- no downstream T5–T10 artifact gains promotion authority;
- Capability claims do not become Capability truth, Readiness or Resource interchangeability; and
- one Canonical Concept does not make the remaining seven Concepts Canonical, less important or implicitly compatible.

Before any second T4 promotion proposal, the Board must issue a new explicitly scoped act against the then-current inventory and blockers. A successful OCP-009 merge is evidence for that act, not authorization of it.

## 54. AD-016D accounting and proposed effect

When externally reviewed, explicitly owner-authorized and merged, AD-016D will:

- set AD-016 to `0.5.0 / Accepted`;
- select G2 micro-waves inside C/L2;
- authorize preparation of one OCP-009 T4 draft only;
- retain G0 as the fail-safe fallback and E as a named candidate-local repair;
- keep AB-062 `Planned`;
- require a new Board scope act before a second T4 promotion proposal; and
- change no OCP, Concept, Pattern, status projection, dependency, registry row, graph edge, schema, checker rule or fixture.

Fable exact-head review, Codex adjudication, green CI and explicit Pavlo or Architecture Board authorization are required for AD-016D itself. A later OCP-009 proposal repeats all four gates and requires a separate merge authorization. Until AD-016D merges, G2 and the OCP-009 preparation scope in §§49–53 remain proposals only.

## 55. Post-first-wave baseline — AD-016E

AD-016E evaluates the next scope on `main@4e2cce4540f3598f7ff95b981d5a45962d25d3b1`. OCP-009 and Capability are `1.0.0 / Canonical`; OCP-000 and OCP-002 are `1.1.0 / Canonical`; post-merge CI is green. This is evidence that the first G2 unit completed, not evidence that a second candidate is ready.

The remaining T4 candidates are unchanged semantically:

| Candidate | State | Blocking item |
|---|---|---|
| OCP-003 Resource | `0.6.0 / Draft`; Concept `Accepted` | `Organizational Resource` / `Unit` identity and Organization mapping |
| OCP-007 Organization | `0.3.2 / Draft`; Concept `Accepted` | merger/split continuity, relationship class/type stability and Resource mapping |
| OCP-008 Objective | `0.2.1 / Draft`; Concept `Accepted` | authority and immutable evidence for same-identity editorial correction |

All three B sets are non-empty. Therefore no second T4 promotion draft is admissible now under G2.

## 56. Remediation-scope comparison

| Option | Scope | Benefit | Main risk | Result |
|---|---|---|---|---|
| J0 — hold only | open no remediation cycle | lowest immediate change | blockers remain untested | admissible fallback |
| J3 — Resource boundary first | resolve AB-006/AB-052 mapping from the Resource side | addresses a central dependency | cannot be decided honestly without Organization identity evidence | premature alone |
| J7 — Organization boundary first | resolve continuity, relationship kinds and mapping together | attacks the widest T4 surface | several independent decisions create a large rollback unit | not first |
| J8 — Objective correction discovery first | isolate same-identity correction authority and evidence | one bounded identity question with Canonical roots and Accepted P-001 | a convenience edit path could weaken immutable supersession | leading remediation scope |
| JE — extract a stable kernel | split OCP-003 or OCP-007 before semantic resolution | may later isolate stable text | can duplicate authority or hide the identity blocker | conditional, not selected |

J8 is preferred because the question is independently falsifiable and does not require deciding Organization/Resource mapping. This is not a readiness ranking and does not authorize Objective promotion.

## 57. Selected preparation scope — Objective correction discovery only

AD-016E selects J8 and authorizes preparation of a separate discovery for the OCP-008 same-identity editorial-correction boundary. The exact input is OCP-008 blob `c1a088aff6e61bf553a100ecb2dd9975a3b67657`, SHA-256 `35f1a24e7f9d085ca3b9a6300d39544d5aa13d660652a34935a38980e96535a2`, at the §55 baseline.

The discovery must compare at least:

1. strict immutability: every stored `statement` change creates a new Objective with explicit supersession;
2. a separately identified editorial-amendment record while Objective identity remains stable;
3. an exact versioned Objective snapshot with governed domain equivalence evidence; and
4. exclusion of display-only formatting from the stored normative statement.

For each outcome it must name authority, provenance, replay, P-001 impact, migration, invalid counterexamples and how semantic change fails safe. A domain label, newest timestamp, record order, editor count or similarity score cannot establish equivalence.

## 58. Non-transfer and stop rules

This act does not authorize editing OCP-008 normative semantics, changing its version/status, promoting Objective, creating an amendment record, invoking another Pattern, or changing any projection or graph edge. Those effects require later comparison, Board selection and exact-head implementation acts.

If discovery shows that same-identity correction cannot preserve immutable replay without new authority, strict immutability remains the fail-safe control. Successful discovery does not make Objective ready; the resolved contract must still undergo a fresh B/S/C audit and a new Board promotion-scope act.

OCP-003 and OCP-007 remediation may be researched, but no promotion draft or identity decision for them is authorized here.

## 59. Counterexamples

1. Capability succeeded, so another T4 candidate must follow — false; G2 has no momentum rule.
2. Objective has only one named B item, so it is already ready — false; one B item stops promotion.
3. Spell-check similarity proves semantic equivalence — false without governed authority and replayable evidence.
4. Same `objective_id` permits in-place statement mutation — false under the current supersession guarantee.
5. P-001 Module C automatically supplies editorial correction semantics — false; the invoker owns domain meaning.
6. Green fixtures, newest edit or reviewer count selects an outcome — false.
7. J8 selection authorizes OCP-008 promotion — false; it authorizes discovery preparation only.
8. Resolving Objective opens OCP-004 automatically — false; Resource and Operation-local blockers remain.

## 60. AD-016E proposed effect

When exact-head reviewed, explicitly authorized and merged, AD-016E will set AD-016 to `0.6.0 / Accepted`, retain G2/L2 with J0 as fallback, create AB-063 as `Planned`, and authorize only the separate Objective correction discovery. AB-062 remains `Planned`.

It changes no OCP, Concept, Pattern, dependency, registry row, status projection, graph edge, checker rule, fixture or readiness percentage. Authorization of AD-016E cannot transfer to the discovery decision, OCP-008 promotion or any other candidate.

## 61. AD-017 handoff accounting

AD-017 `0.1.0 / Discovery` becomes the active decision owner for AB-063. AD-016 remains the accepted decision provenance for selecting J8 and authorizing discovery preparation, but no longer lists the active backlog item in `Applies-To`.

This `0.6.1` PATCH handoff prevents overlapping active ownership. It changes no J8 scope, OCP-008 rule, Objective status, promotion authority, evidence obligation or non-transfer boundary.

## 62. AD-016F mandate and exact post-implementation baseline

AD-016F performs the fresh blocker/stability/compatibility audit required by §§58 and 60 after the accepted OCP-008A implementation. It does not select a second T4 scope or authorize a promotion draft.

The exact audit baseline is `main@53c00c4489e2aa3c9efc6af6235be573069aee83`, tree `204302b77de6734fb51c454a5764b230ca0bd6b7`. On that baseline:

- OCP-008 is `0.3.0 / Draft`, Objective is `Accepted`, and the defining file is Git blob `07756e9129a4f11a826b646831dde01939d89336`, SHA-256 `6965cb2f3fbd695a33b16f5eca061f87b33123ee4321aaa8742f709537e1d2e0`;
- AD-017 is `0.3.0 / Accepted`, selects strict stored-statement immutability plus display exclusion, and retains concrete reopening gates for amendment or revision models;
- AB-063 is `Resolved` by normative text, duplicate-identity rejection and exact historical-consumer evidence;
- OCP-000, OCP-001 and OCP-002 are Canonical; P-001 is `0.1.0 / Accepted` and OCP-008 remains exact-bound to it;
- Capability is the only Canonical Concept; Objective and the other six remaining defined Concepts stay Accepted; and
- the reference suite has 164 unit tests and 117 non-sensitive fixtures, with post-merge `main` CI green.

The successful implementation and green checks are inputs, not a readiness verdict. AD-016F must still ask whether the former B item is actually gone, whether another B item is exposed, which questions can remain outside a `1.x` surface, and what migration the current consumers and projections would require.

## 63. Fresh B/S/C method

AD-016F reuses the classifications in §§23, 34 and 40:

- **B — blocker:** an unresolved identity, authority, dependency or compatibility question that can invalidate the proposed `1.x` guarantee;
- **S — scoped exclusion:** a named extension that current consumers do not require and that can remain outside `1.x` without weakening the present contract; and
- **C — cleanup:** stale or misleading text/projection that must be corrected before promotion but does not require a new semantic decision.

The audit applies four controls:

1. no implementation may satisfy an obligation that its selected semantic model rejects;
2. no fixture, timestamp, commit order, reviewer count or completed prior wave may choose lifecycle status;
3. a question is not B merely because it is open, and it is not S merely because it is difficult; and
4. a current consumer incompatibility, unstable authority or hidden migration overrides schedule and stops the candidate.

This structure keeps K0 hold and a future K8 Objective proposal evidence-accessible. It does not make successful A+D evidence a hidden weight that an alternative scope cannot meet.

## 64. Recomputed Objective B item

The previous B item in §40 asked who classifies a same-identity editorial correction and what immutable evidence prevents a semantic change from bypassing supersession. That question no longer exists inside the selected OCP-008 surface because Core no longer permits a changed stored statement to retain the same identity.

The closure is semantic before it is mechanical:

1. one `objective_id` identifies one immutable stored normative statement;
2. every changed stored value creates another Objective and another `objective_id`;
3. optional explicit supersession preserves both records, permits branching and never redirects an existing reference;
4. display transformation remains outside the stored statement, while write-back becomes a stored-value change;
5. no newest, current, similar or most-supported projection exists; and
6. Operations and OutcomeAssessmentRecords keep exact historical Objective references until their own governed act changes them.

The checker then witnesses the expressible subset: it rejects duplicate IDs, preserves two visible correction successors, validates the prior Operation and assessment against the prior Objective, and remains valid when Objective order is reversed. The checker does not classify language equivalence or select authority.

No current OCP-004, OCP-010 or OCP-011 consumer requires one logical Objective ID to survive changed stored text. No current dataset or fixture requires an amendment head, revision identity, mutable current statement or consumer rebinding. AD-017B §§35.1–35.2 retain fail-safe reopening gates if such concrete evidence later appears.

**AD-016F therefore finds no current B item inside the OCP-008 `0.3.0` semantic surface.** This is an audit result, not a promotion selection. A newly demonstrated consumer incompatibility or B/C reopening case would replace this result and stop K8.

## 65. Scoped exclusions that may remain outside Objective `1.x`

The following questions are S under the current evidence:

| Scoped extension | Why it does not block the current surface | Required future gate |
|---|---|---|
| Objective hierarchy, decomposition, contribution, support, conflict or equivalence relations | no current Objective identity or consumer reference depends on them | separate owner, consumer, route and relation contract; P-001 decision if identified records are used |
| Objective lifecycle or temporal effectivity | current validity and exact resolution are intentionally independent of a current/effective projection | separate lifecycle model with authority, history, overlap/gap and fail-safe derivation |
| same-identity amendment or versioned-revision model | current consumers work with immutable exact IDs; A+D deliberately rejects an unproved head | accepted AD-017 reopening evidence and full migration contract |
| domain taxonomy for outcome, condition and effect | the definition is sufficient without a closed classification tree | domain or later Core taxonomy act with a concrete consumer |
| automatic free-text conversion, language normalization and semantic equivalence | Core consumes the stored value after any attributable pre-creation rule | separate input/tooling contract; it cannot rewrite Objective history |
| display metadata and renderer behavior | presentation is deliberately implementation-local | Route I implementation contract if a product needs one; no Core identity authority |
| advanced achievement/partial-satisfaction views | OCP-011 already owns exact assessment records and fail-safe activation; Objective remains free of mutable achievement state | extension of the exact OCP-011 target/criterion/activation surface, not an Objective status field |

These exclusions must be readable in a future `1.x` compatibility surface. Canonical would not mean that they are solved, forbidden forever or delegated to an unnamed owner.

## 66. Cleanup and current-state projection audit

The audit finds C work, but no new semantic decision:

1. OCP-008 frontmatter still says `Result Model` in `Used-By`; the current owner is OCP-011 OutcomeAssessmentRecord, while fundamental Result identity was rejected.
2. OCP-008 §§2, 9, 13 and 15–16 still contain future-tense or open-question wording for Event/Result evidence even though OCP-010 and OCP-011 now govern those boundaries.
3. OCP-008 §§17–18 are historical accepted-act records and must not be rewritten. A future lifecycle section must add a clear current bridge so their former `Draft`/`Accepted` state cannot be mistaken for the post-act state.
4. A future compatibility section must distinguish the accepted OCP-011 assessment baseline from still-scoped advanced activation, partial-satisfaction and lifecycle questions.
5. OCP-004 contains two human-readable current-state labels that render Objective as `Accepted` (§3 table and §4 tree). A future Objective status transition must update or remove that volatile status snapshot so the consumer document does not contradict the authoritative projections.
6. README and the generated Foundation map are current-state projections/accounting and must move atomically with any selected status act; historical AD sections and milestone baselines must not be rewritten.

Items 1–4 are defining-document cleanup and current-history clarification. Item 5 is a non-semantic consumer PATCH or status-decoupling edit, not an OCP-004 promotion and not a change to `Operation → Objective`. It may be included only with explicit atomic migration accounting. None of these items may be ignored as “editorial” if it would leave a human reader with a false current state.

## 67. Stability audit

OCP-008 now has one coherent semantic owner and one compatible record model:

- identity is the stable `objective_id` of one endpoint-free P-001 record;
- authority is the exact immutable Objective, not a current projection, mutable view or assessment;
- the minimal fields and validation obligations are explicit;
- provenance remains attributable creation evidence and never becomes authorization;
- Module C owns explicit, acyclic, branching, non-redirecting supersession;
- Objective remains independent of Operation, while Operation owns the only current Concept dependency;
- Objective carries no achievement, Readiness, availability, admissibility or command conclusion; and
- the stored/display boundary is explicit and falsifiable.

Recent implementation is not itself stability evidence. The stronger evidence is that AD-017 compared four authority models, commissioned adversarial attacks, selected the least-authority complete model, and the implementation preserved current P-001 and consumer contracts without migration. The remaining open questions no longer change the meaning of an existing Objective record or reference.

The AD-017 reference in OCP-008 is accepted decision provenance. AD-017 exact-anchors the pre-implementation OCP-008 input; it does not create a Concept edge, a floating current-statement authority or an OCP lifecycle exception. AD-003 and AD-017 remain governed by Accepted decision lifecycle rather than an invented Canonical AD status.

## 68. Candidate `1.x` compatibility surface

If a later Board act selects K8, the proposed OCP-008 `1.x` surface must preserve at least:

1. Objective as one identified intended outcome, condition or effect, independent of any Operation;
2. exact one-record-per-`objective_id` identity and the minimal stored fields;
3. immutable stored normative `statement`, with every changed value creating a new ID;
4. decoded-value identity distinct from serialization bytes and display rendering;
5. attributable non-authorizing provenance;
6. explicit Module C supersession with self/cycle rejection, visible branching, overlap/gap tolerance and no redirect;
7. exact historical consumer resolution with no automatic rebinding;
8. no current/latest Objective derivation and no authority from timestamp, order, similarity or count;
9. no Objective hierarchy, lifecycle, effectivity, achievement or authorization by implication;
10. exact `P-001@0.1.0` invocation and endpoint-free form;
11. `Concept-Depends-On: []`, while OCP-004 continues to own `Operation → Objective`; and
12. explicit S exclusions and AD-017 reopening gates.

The future proposal must state how PATCH, MINOR and MAJOR changes apply to that surface. In particular, a later additive relation or lifecycle contract is not automatically MINOR: it must follow OCP-016 and use MAJOR if it weakens identity, exact resolution, authority or consumer replay guarantees.

## 69. Dependency, consumer and migration cost

OCP-008's direct OCP dependencies—OCP-000 `1.1.0`, OCP-001 `1.0.0` and OCP-002 `1.1.0`—are Canonical. P-001 is Accepted at the exact invoked `0.1.0`; Accepted AD-003 and AD-017 supply decision provenance under their own artifact lifecycle. L2 therefore needs no exception or same-act dependency promotion.

The exact direct consumers inspected on the §62 baseline are:

| Consumer | Exact baseline | Compatibility result |
|---|---|---|
| OCP-004 Operation | `0.8.0 / Draft`, blob `969cacab45e6e3f8b9bcf302786a60a5464a6888` | `objective_refs` resolve exact Objective IDs; no rebinding or semantic change, but the two current-status labels require C cleanup |
| OCP-010 Event | `0.2.0 / Draft`, blob `d73bab07acac3c316a9a2a4f4d25cb1f9b1bdc06` | Event identity remains independent; no Objective mutation, achievement implication or reference migration |
| OCP-011 OutcomeAssessmentRecord | `0.3.0 / Accepted`, blob `ff2608a372c6305db4c290f05c15e961ca96e6f6` | `target_ref` exact-binds `objective@1`; assessment history and activation never mutate or redirect Objective |

On the current baseline, an eventual Objective lifecycle proposal would have this minimum atomic footprint:

1. OCP-008 `0.3.0 / Draft → 1.0.0 / Canonical` and defining `Concept-Status: Accepted → Canonical`;
2. OCP-000 `1.1.0 → 1.2.0` with only the Objective row changing `Accepted → Canonical`;
3. OCP-002 `1.1.0 → 1.2.0` with the exact Objective projection and current prose/tree synchronized;
4. generated Foundation map and README current-state accounting synchronized;
5. OCP-004 `0.8.0 → 0.8.1` only for a non-semantic status-label update or removal of volatile status rendering, with its own compatibility and rollback note; and
6. no OCP-010/OCP-011 version, P-001 version, record schema, Objective ID, Operation reference, assessment reference, Concept dependency or graph-edge change.

The exact versions and blobs must be recomputed if `main` changes before a proposal. Existing valid records need no data migration. A duplicate-ID dataset remains invalid or quarantined; promotion cannot synthesize a newest winner, merge IDs or rewrite historical consumer bindings.

Corrective rollback would be a new reviewed act that restores document/Concept status and all current projections together. It cannot roll back strict record immutability, delete Objectives or redirect references by editing only a status projection.

## 70. Outcome-fair scope options for AD-016G

AD-016F compares scope choices without selecting one:

| Option | Next preparation scope | Evidence in favor | Main risk | Audit result |
|---|---|---|---|---|
| K0 — hold | authorize no second T4 draft | lowest immediate lifecycle and migration cost | retains a bounded candidate at Draft without new counterevidence | admissible control |
| K8 — Objective micro-wave | authorize preparation of one OCP-008/Objective lifecycle draft | B is empty; S and C are explicit; L2 and P-001 floors hold; consumers need no semantic migration | a promotion draft may overclaim completeness or hide OCP-004/current-state cleanup | leading hypothesis, not selected |
| K3 — Resource remediation | prioritize the Organizational Resource/Unit identity boundary | attacks a real remaining T4 blocker | cannot make Resource ready without Organization mapping evidence | admissible remediation, not a promotion alternative for Objective evidence |
| K7 — Organization remediation | prioritize continuity, relationship kinds and Resource mapping | addresses the widest remaining T4 identity surface | large coupled decision and rollback unit | admissible later comparison, not currently bounded |
| K37 — joint Resource/Organization discovery | compare the shared mapping boundary before another lifecycle act | may avoid contradictory one-sided decisions | can couple independent continuity and resource-identity questions | admissible discovery only |
| KX — reopen AD-017 B/C | reconsider amendment or revision authority | valid only if the exact §35 consumer evidence appears | convenience pressure could reintroduce floating history | unsupported on the current baseline |

Every option uses the unconditional repository inventory, artifact floors, non-transfer rules and current consumer evidence. K8 alone additionally bears the complete `1.x`, projection, cleanup, migration and rollback obligations in §§68–69. K0 is not required to fabricate promotion fixtures; K3/K7/K37 are not required to satisfy Objective-specific evidence. This prevents the evidence design from assuming the layer chosen by another option.

## 71. Falsification targets and counterexamples

Before AD-016G may select K8, review must try to demonstrate any of the following:

1. a current consumer must preserve one logical Objective ID across changed stored text;
2. strict value immutability conflicts with the exact P-001 invocation or Module C;
3. OCP-004, OCP-010 or OCP-011 needs semantic migration or reference rebinding;
4. a direct OCP dependency is pre-canonical or a Pattern binding is stale;
5. the `1.x` surface cannot exclude lifecycle, hierarchy, taxonomy or display without weakening a current guarantee;
6. the C cleanup changes identity or authority rather than only removing stale current-state language;
7. promotion would create a Concept dependency, Concept-graph cycle or current/latest Objective authority;
8. a current valid dataset requires the forbidden same-ID mutation; or
9. the migration footprint cannot be rolled back atomically without rewriting record history.

If one succeeds, K8 loses its leading position and the proposal stops. The following remain explicit negative controls:

- OCP-008A merged, therefore Objective must be promoted — false;
- CI and 164 tests decide readiness — false;
- one resolved B item means every open question is closed — false;
- Canonical Objective makes Operation, Event or OutcomeAssessmentRecord Canonical — false;
- Accepted P-001 transfers status or domain semantics to its invoker — false;
- newest timestamp, record order, similarity, author count or consumer count selects an Objective — false;
- OCP-004's stale `Accepted` label may remain because it is non-authoritative — false for readable repository consistency;
- Objective promotion authorizes amendment/revision, lifecycle, hierarchy, display or achievement semantics — false; and
- authorization of OCP-008A or AD-016F transfers to AD-016G or a lifecycle PR — false.

## 72. AD-016F recommendation

The strongest current hypothesis is **K8: one separately scoped OCP-008/Objective micro-wave inside the already selected G2/L2 strategy**. It is stronger than K0 because no unresolved B item or hidden consumer migration was found, and stronger than K3/K7/K37 as the immediate bounded lifecycle candidate because those scopes still contain identity blockers.

This is a recommendation only. The principal K8 risk is semantic overreach: treating `Canonical` as proof that Objective lifecycle, taxonomy, equivalence, display, achievement or all downstream consumers are complete. The future `1.x` surface and non-implications must make that inference impossible.

AD-016F does not authorize an OCP-008 branch, version/status edit or projection change. A separate AD-016G Board act must decide whether to select K8, retain K0, choose remediation scope or require another comparison.

## 73. Mandatory AD-016G decision contract

AD-016G must:

1. exact-anchor the then-current `main` baseline and recompute any changed version/blob/status facts;
2. accept, revise or reject each B/S/C finding with evidence;
3. attempt all nine §71 falsification targets;
4. select one explicit scope or retain hold without inferring momentum from prior work;
5. preserve L2, Pattern lifecycle, atomic projections, OCP-016 routing and separate authorization boundaries; and
6. state the next act, stop conditions, migration unit and non-transfer rule.

If AD-016G selects K8, it may authorize preparation of one OCP-008 lifecycle draft plus only the exact status projections, accounting and bounded OCP-004 PATCH required by §69. That later proposal must independently provide the exact compatibility surface in §68, atomic footprint in §69, C cleanup, human counterexamples, machine evidence appropriate to the claims, rollback accounting, exact-head Fable review, Codex adjudication, green CI and a new explicit Pavlo/Architecture Board merge authorization.

AD-016G must not select K8 if a current consumer requires amendment/revision identity, if OCP-004/OCP-010/OCP-011 needs a semantic change, if P-001 must change, if strict historical replay fails, or if status synchronization cannot remain atomic. In those cases it stops and routes the discovered object through OCP-016 rather than improvising inside a promotion draft.

## 74. AD-016F accounting and effect

When exact-head reviewed, explicitly authorized and squash-merged, AD-016F will:

- set AD-016 to `0.7.0 / Accepted`;
- record that the former OCP-008 B item is closed and no new B item was found on the exact §62 baseline;
- classify the remaining Objective questions as explicit S exclusions or C cleanup;
- record K8 as the leading hypothesis while leaving K0 and remediation scopes admissible;
- keep AB-062 `Planned` and require a separate AD-016G Board decision; and
- retain foundation readiness at approximately 68% because no document or Concept lifecycle changes in this audit.

This act changes no OCP, Concept, Pattern, status projection, dependency, registry row, graph edge, schema, checker rule, fixture or production authority. Fable approval, Codex adjudication, green CI and explicit Pavlo/Architecture Board authorization apply only to AD-016F. They cannot authorize AD-016G, an OCP-008 lifecycle proposal, OCP-004 cleanup or another T4 candidate.

## 75. AD-016G Board question and exact baseline

AD-016G decides the next preparation scope after the accepted AD-016F audit. It does not perform the Objective lifecycle transition itself.

The exact decision baseline is `main@5396c706191e0d67e6587d8b69edad01867d6be9`, tree `e93e3f0031efd3216aa0230a0f7b51737429b0ff`. On that baseline:

- AD-016 `0.7.0 / Accepted` is blob `a3406bb802d9fe93daa8689c0a4a264223ff0a36`, SHA-256 `92af2218aa3a361aa5e0d6cb63692283c72f61ae6e9ce3e6404965c11ec610dd`;
- OCP-008 remains `0.3.0 / Draft`, Objective remains `Accepted`, and the defining file remains blob `07756e9129a4f11a826b646831dde01939d89336`, SHA-256 `6965cb2f3fbd695a33b16f5eca061f87b33123ee4321aaa8742f709537e1d2e0`;
- the accepted audit finds no current Objective B item, seven bounded S rows and six C findings;
- K8 is the leading hypothesis, while K0, K3, K7, K37 and evidence-triggered KX remain explicit controls; and
- no second T4 lifecycle proposal is currently authorized.

The Board question is therefore narrow: **does the accepted audit justify preparation of one OCP-008/Objective micro-wave under G2/L2, or should the repository retain hold or choose remediation instead?** Merge history, authoring effort, green CI and the number of completed acts are not reasons to select K8.

## 76. Board treatment of the AD-016F audit

AD-016G accepts the AD-016F classifications as decision input:

1. **B is empty on the exact baseline.** A changed stored statement cannot preserve Objective identity, so the former classifier/equivalence-authority question has no same-identity operation to govern.
2. **The seven S rows remain exclusions.** Relations, lifecycle/effectivity, amendment/revision, taxonomy, automatic language processing, display and advanced assessment views are not required by a current Objective identity or consumer contract.
3. **The six C findings are finite.** They consist of stale current/future wording, historical-state bridging, compatibility text, OCP-004 status labels and current-state projections; none requires a new identity or authority decision.
4. **Current consumers remain exact.** OCP-004 pursues exact Objective IDs, OCP-010 does not turn Event into Objective truth, and OCP-011 exact-targets Objective without mutation or redirect.
5. **Artifact floors hold.** Direct OCP dependencies are Canonical; P-001 is Accepted and exact-bound; Accepted AD-003 and AD-017 remain decision provenance under their own lifecycle.

Accepting the audit does not make its recommendation self-executing. The Board still owns the scope choice, and a later lifecycle proposal still owns its own exact content, evidence, rollback and merge authorization.

## 77. Commissioned falsification closure

AD-016G attempts all nine AD-016F §71 attacks before selection:

| Attack | Evidence checked | Result |
|---|---|---|
| a current consumer must preserve one logical ID across changed text | OCP-004 `objective_refs`, OCP-010 boundaries and OCP-011 `target_ref` use exact immutable IDs; no amendment head is consumed | not demonstrated |
| strict immutability conflicts with P-001 or Module C | OCP-008 keeps one endpoint-free record identity and uses Module C only for explicit non-redirecting supersession | not demonstrated |
| a consumer needs semantic migration or rebinding | prior Operation and assessment evidence validate against the prior Objective after two successors exist; no consumer contract selects a successor | not demonstrated |
| a dependency floor fails | OCP-000/OCP-001/OCP-002 are Canonical and `P-001@0.1.0` is Accepted; no L2 exception is needed | not demonstrated |
| an S exclusion weakens a current guarantee | every S row names why current consumers do not require it and the separate future gate that would own it | not demonstrated |
| C cleanup changes identity or authority | each C item is a stale label, current-state projection, compatibility explanation or historical bridge; normative identity remains unchanged | not demonstrated |
| promotion creates a Concept edge, Concept-graph cycle or current/latest authority | `Concept-Depends-On: []` stays fixed; OCP-004 keeps the only current `Operation → Objective` edge; no selector is introduced | not demonstrated |
| a valid current dataset needs same-ID mutation | valid evidence uses distinct IDs; duplicate same-ID statements are already invalid and receive no permissive migration | not demonstrated |
| the migration cannot roll back atomically | defining status, OCP-000/OCP-002, map/accounting and bounded OCP-004 rendering form one enumerated unit with no record-history rewrite | not demonstrated |

All attacks fail on the exact baseline. “Not demonstrated” is deliberately narrower than “impossible”: later concrete evidence invokes the stop and reopening rules below.

## 78. Architecture Board selection — K8

AD-016G selects **K8 — one Objective micro-wave** as the next preparation scope inside the already accepted G2/L2 strategy.

K8 is selected because:

- the candidate-local B set is empty after a separately selected and implemented semantic correction boundary;
- the stable Objective identity, authority, supersession and replay guarantees can be stated as one readable `1.x` surface;
- all direct artifact floors are already satisfied without an exception or same-act dependency promotion;
- the exact consumers need no semantic change or reference migration;
- the remaining S exclusions and C cleanup are bounded and falsifiable; and
- the lifecycle/projection unit is finite and can be reviewed and rolled back atomically.

K8 is not selected because Objective is older, more edited, easier to promote, next in a numeric list or supported by more tests. G2 permits one-candidate progression only when candidate-local evidence holds; it does not create a queue or momentum rule.

This selection authorizes preparation of a draft. It does not change OCP-008 or Objective status and does not authorize merge of the later proposal.

## 79. Selected preparation scope

The next proposal may contain only the following lifecycle unit, recomputed against its exact base:

1. OCP-008 `0.3.0 / Draft → 1.0.0 / Canonical` with `Concept-Status: Accepted → Canonical`;
2. OCP-000 `1.1.0 → 1.2.0` with only the Objective registry row changing `Accepted → Canonical`;
3. OCP-002 `1.1.0 → 1.2.0` with the exact Objective projection and human-readable current views synchronized;
4. Foundation map and README current-state/accounting updates;
5. OCP-004 `0.8.0 → 0.8.1` only to update or remove its two volatile Objective status labels, with no Operation semantic change; and
6. OCP-008 C cleanup and a new current lifecycle section that preserves historical §§17–18 rather than rewriting them.

The exact versions in items 1–5 assume the §75 baseline. Any intervening `main` change requires recomputation before authoring. The proposal may not silently add another artifact because it appears in the same topological slot.

The selected scope changes no OCP-010/OCP-011 version, P-001 version or invocation, Objective record schema, existing Objective ID, Operation/assessment reference, Concept dependency, graph edge, amendment/revision authority, display schema or production data.

## 80. Mandatory OCP-008 lifecycle proposal contract

The separately reviewed proposal must:

1. exact-anchor its pre-change OCP-008, OCP-000, OCP-002 and OCP-004 inputs by Git blob and SHA-256;
2. publish one human-readable `1.x` compatibility surface containing all twelve AD-016F §68 guarantees;
3. state PATCH/MINOR/MAJOR handling without assuming that a later relation or lifecycle addition is automatically compatible;
4. retain exact `P-001@0.1.0`, endpoint-free form and Optional Module C without new Pattern semantics;
5. preserve `Concept-Depends-On: []` and the OCP-004-owned `Operation → Objective` edge;
6. enumerate every Objective status projection and update the authoritative/current set atomically;
7. bound OCP-004 `0.8.1` to the two status renderings and provide its own compatibility/rollback note;
8. remove or bridge the six C findings without rewriting historical accepted-act records;
9. keep all seven S rows explicit and route any reopening to its named owner;
10. reuse accepted immutable-history evidence and add evidence only for a genuinely new mechanically expressible claim;
11. include human counterexamples for current/latest selection, status implication, achievement leakage, display write-back, authority transfer and partial rollback; and
12. state that Canonical is a versioned semantic compatibility promise, not production readiness, truth, authorization, completeness or immutability forever.

Checker status synchronization, L2 and fixtures are structural witnesses only. They cannot approve the `1.x` surface or replace human review.

## 81. Stop, failure and reopening rules

The OCP-008 proposal must stop and return to the Board if authoring or review discovers:

- a current consumer that needs one logical Objective ID across changed stored text;
- a required amendment/revision identity, current head or semantic-equivalence authority;
- any OCP-004/OCP-010/OCP-011 semantic change or reference rebinding;
- a P-001 version/module change or incomplete invocation;
- C cleanup that changes identity, authority, supersession or achievement behavior;
- an OCP-004 edit broader than the two status views and their local explanation;
- an unenumerated Objective status projection or non-atomic migration;
- a valid current dataset that cannot preserve exact historical values and references;
- a new Concept dependency, graph edge, display authority or current/latest Objective projection; or
- a rollback that would require deleting records, merging IDs, redirecting references or rewriting history.

Consumer evidence for same-identity correction routes back through AD-017 §35. A new candidate object or authority routes through OCP-016. A changed repository baseline is recomputed; it is not repaired by copying old version numbers or selecting the newest artifact.

K0 becomes the immediate fallback if any stop condition succeeds. Failure of the draft does not authorize K3, K7, K37 or another lifecycle candidate automatically.

## 82. Alternatives not selected and reopening gates

### 82.1 K0 — hold

K0 is not selected because no current blocker, dependency exception or consumer migration was found. It remains the fail-safe outcome if the later exact proposal cannot satisfy §§79–81. Avoiding a bounded review is not safer if it merely leaves verified compatibility unstated, but schedule pressure is also not evidence against hold.

### 82.2 K3, K7 and K37 — Resource/Organization remediation

These remain legitimate remediation scopes, but they do not disprove Objective readiness. Resource still needs Organizational Resource/Unit identity evidence; Organization still needs continuity, relationship-kind and mapping evidence. Joint discovery may later reduce contradiction risk, but it is not promoted into this rollback unit.

Research may proceed without lifecycle authority. A future preparation scope still requires a new Board act after the selected Objective proposal completes or fails.

### 82.3 KX — reopen amendment/revision outcomes

KX is not selected because no AD-017 §35 consumer evidence exists on the exact baseline. UI preference, spelling frequency, edit count, similarity, newest timestamp, issuer count or implementation convenience cannot reopen B/C. If the exact reopening evidence appears, it stops the lifecycle proposal before any identity migration.

## 83. Migration, rollback and authorization boundary

AD-016G changes no lifecycle state. It selects only the allowed preparation scope.

If later proposed, the migration unit in §79 must move or roll back together. OCP-004 remains Draft and Operation remains Accepted; its PATCH changes only a volatile current-status rendering. OCP-010 and OCP-011 remain byte-unchanged unless a stop condition ends the proposal.

Existing valid Objective records and exact consumer references need no data migration. Invalid duplicate-ID data remains invalid or quarantined; it cannot receive a synthetic current winner. Corrective rollback is a new reviewed act over document/Concept status and all projections, never a history rewrite.

Fable approval, Codex adjudication, green CI and explicit Pavlo/Architecture Board authorization for AD-016G authorize only this selection. The later OCP-008 proposal repeats all four gates on its own exact head. Marking that draft Ready, passing CI or citing this selection does not authorize its merge.

## 84. AD-016G accounting and accepted effect

When exact-head reviewed, explicitly authorized and squash-merged, AD-016G will:

- set AD-016 to `0.8.0 / Accepted`;
- select K8 as the next G2/L2 preparation scope;
- authorize one OCP-008/Objective lifecycle draft plus only the exact projections, accounting and bounded OCP-004 PATCH in §79;
- retain K0 as fail-safe and the Resource/Organization scopes as separately gated future work;
- keep AB-062 `Planned`; and
- retain foundation readiness at approximately 68% because no OCP or Concept lifecycle changes in this selection act.

This act changes no OCP, Concept, Pattern, status projection, dependency, registry row, graph edge, schema, checker rule, fixture or production authority. It does not authorize a third T4 scope, OCP-003/OCP-007 promotion, downstream T5–T10 promotion or merge of the selected lifecycle draft.

## 85. AD-016H trigger — K8 preflight stop

Authoring the selected K8 lifecycle proposal exposed a pre-existing human-readable current-state defect before any normative OCP edit was made.

AD-016G §81 requires the proposal to stop if OCP-004 needs an edit broader than its two Objective status views. The exact baseline `main@6d4c24808f4f9fbe058e269429de26bfd7efe801`, tree `9b951d1e14b490fca07d1c946d5f9844f5b804b6`, contains:

- OCP-004 §4 row `Capability | Accepted`, although Capability is already Canonical; and
- OCP-003 current boundary text stating that Capability and Constraint are both Accepted.

Updating either Capability statement inside the K8 atomic unit would exceed the AD-016G §79/§81 boundary. Leaving the statements untouched would knowingly preserve false current prose in documents meant to be read by humans. Therefore K8 authoring stops before a branch is published or a lifecycle head is proposed.

This stop is evidence that the supporting cleanup scope was incomplete. It is not evidence against Objective identity, the empty B set, P-001 conformance, consumer replay or the K8 semantic direction.

## 86. Exact stale-view footprint

The preflight audit distinguishes current prose from historical records:

| Artifact | Exact baseline | Current stale view | Classification |
|---|---|---|---|
| OCP-003 Resource | `0.6.0 / Draft`, blob `4e76de5c56c35625a385e001742fffd7f7f76479`, SHA-256 `f5d2815a635e16f4e994b1f4dbb23e064356311a7f498436820c7667c2dfe85b` | §7 says Capability and Constraint are Accepted | C — update only Capability to Canonical |
| OCP-004 Operation | `0.8.0 / Draft`, blob `969cacab45e6e3f8b9bcf302786a60a5464a6888`, SHA-256 `6690118cfaaa37358d868ec2610c60a3f381906890f4baed034655454f703f1c` | §4 table says Capability is Accepted | C — update only the Capability row |

README, OCP-000, OCP-002 and the generated Foundation map already render Capability as Canonical. OCP-009's lifecycle act, OCP-000/OCP-002 transition sections, OCP-012 accepted-act text and accepted AD records describe the state at their recorded acts; they are history and must not be rewritten as current-prose cleanup.

No `Capability [Accepted]` tree annotation or additional current Capability-status view was found. The two rows above are the complete preflight correction footprint on the exact baseline.

## 87. Repair options

| Option | Repair sequence | Benefit | Main risk | Result |
|---|---|---|---|---|
| Q0 — hold K8 indefinitely | make no correction and open no lifecycle draft | no new edit | leaves known false human-readable state and does not test a finite repair | admissible fail-safe, not preferred |
| Q1 — separate preflight PATCH | correct the two stale Capability views first; then recompute and resume K8 | preserves independent rollback and restores the exact AD-016G Objective-only boundary | adds one separately governed correction cycle | leading repair |
| Q2 — expand the K8 atomic unit | correct Capability and Objective status views together | fewer PRs | violates the accepted scope, couples an old defect to Objective rollback and obscures which change required which authority | not selected |
| Q3 — remove consumer-local status rendering generally | redesign current-status prose across consumer OCPs | may prevent future churn | creates a broader governance policy and migration without evidence that all such prose has one role | deferred; requires separate discovery if pursued |

Q1 carries only exact current-prose correction evidence. It does not require the preflight PATCH to prove Objective promotion claims. K8 retains its own complete lifecycle obligations after the correction. Q0 is not required to fabricate correction evidence, and Q3 is not rejected merely because it is broader.

## 88. Architecture Board repair selection — Q1

AD-016H selects **Q1 — a separate preflight PATCH**.

The selected order is:

1. prepare and separately review one non-semantic Capability-status correction for OCP-003 and OCP-004;
2. merge that correction only after its own exact-head Fable review, Codex adjudication, green CI and explicit Pavlo/Architecture Board authorization;
3. recompute all K8 input blobs, versions and current-state renderings on the new `main`; and
4. prepare the OCP-008/Objective lifecycle draft under the unchanged semantic selection, with its own fresh gates.

K8 is paused, not revoked. Q1 does not authorize either later merge and does not allow Objective changes in the preflight PATCH.

## 89. Mandatory preflight correction contract

The separate correction proposal may change only:

1. OCP-003 `0.6.0 → 0.6.1`, retaining `Draft` and Resource `Accepted`, to change the current sentence from “Capability and Constraint are Accepted” to “Capability is Canonical; Constraint is Accepted”;
2. OCP-004 `0.8.0 → 0.8.1`, retaining `Draft` and Operation `Accepted`, to change only the Capability status cell `Accepted → Canonical`;
3. `Last-Review` metadata for those two touched OCPs;
4. one local PATCH-accounting note in each touched OCP explaining that no domain semantics, dependency or Concept status changed; and
5. README/backlog/roadmap accounting needed to record completion and the recomputed next step.

It must not change either OCP's definition, identity, fields, lifecycle, Concept dependencies, direct dependencies, Objective views, Resource/Operation status, Capability semantics, graph edge, P-001 invocation, schema, checker rule or fixture.

If another non-historical stale Capability status view is found, if either wording change alters a semantic guarantee, or if a generated/authoritative projection is inconsistent, the correction stops and Q1 returns to the Board.

## 90. K8 resumption contract

After the preflight correction is accepted and merged:

- the K8 selection in §78 remains the semantic preparation mandate;
- the later proposal recomputes every exact anchor and version from the new `main` rather than copying §79 numbers;
- OCP-004 is expected to start from `0.8.1` and, if no other change intervenes, move to `0.8.2` only for its two Objective status views and local lifecycle-accounting note;
- the six-part §79 footprint otherwise remains unchanged; and
- every §80 obligation and §81 stop condition remains binding.

Completion of Q1 does not itself make Objective Canonical or satisfy lifecycle review. Failure of Q1 activates K0 hold and authorizes no alternative T4 scope.

## 91. Non-transfer and rollback

AD-016H, the preflight correction and the resumed K8 lifecycle proposal are three separate authorization boundaries.

Rollback of the preflight correction is a new reviewed PATCH that restores only the affected prose/version metadata if evidence shows the status rendering was wrong. It does not roll back Capability status, because OCP-000/OCP-002/OCP-009 remain authoritative and unchanged. A rollback that would alter Capability lifecycle or Resource/Operation semantics is outside Q1.

Newest commit, document order, edit count, reviewer count or the existence of an unfinished lifecycle branch cannot bypass any gate. The unpublished stopped branch carries no authority and no proposed state.

## 92. AD-016H accounting and accepted effect

When exact-head reviewed, explicitly authorized and squash-merged, AD-016H will:

- set AD-016 to `0.9.0 / Accepted`;
- record the AD-016G stop before any OCP lifecycle edit;
- select Q1 as a separate preflight correction sequence;
- pause K8 until the exact two-view correction is accepted and merged;
- retain K8's semantic selection and K0 as fail-safe;
- keep AB-062 `Planned`; and
- retain foundation readiness at approximately 68% because this Board act changes no lifecycle or OCP text.

This act changes no OCP, Concept, Pattern, projection, dependency, registry row, graph edge, schema, checker rule, fixture or production authority. Its merge authorization cannot authorize the correction proposal, resume K8 by itself, merge the later lifecycle proposal or select another T4 scope.
