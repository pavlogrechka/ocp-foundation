---
Decision-ID: AD-016
Title: Foundation Canonicalization Readiness Discovery
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-016, P-001, AD-015
Applies-To: AB-062, OCP document lifecycle, Concept lifecycle, Pattern dependencies, canonicalization waves
Review-After: External comparison of promotion units, dependency gates and production-evidence boundaries
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
