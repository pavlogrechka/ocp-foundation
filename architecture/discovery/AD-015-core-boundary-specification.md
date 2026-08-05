---
Decision-ID: AD-015
Title: Core Boundary Admission and Extension Discovery
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: OCP-001, OCP-002, OCP-003, OCP-004, OCP-006, OCP-009, OCP-011, OCP-012, P-001, AD-001, AD-006, AD-010, AD-011, AD-014
Applies-To: AB-061, Core admission, domain extensions, interoperability envelopes
Review-After: External comparison of governance models and artifact homes
---

# AD-015 — Core Boundary Admission and Extension Discovery

## 1. Trigger

The foundation repeatedly requires a candidate to pass a **Core Boundary Test**, but no accepted artifact defines that test as one complete contract.

Current documents already say that:

- implementation concepts do not enter the ontology merely because software uses them;
- a taxonomy category is not a fundamental Concept;
- domain-specific Resource and Operation classifications do not enter Core automatically;
- a Pattern governs modeling form only when explicitly invoked;
- domain namespaces may own specialized Capability semantics;
- domain-owned predicates may not redefine Core Constraint results;
- a Core interoperability envelope may exact-bind a domain profile without importing its meaning;
- checker code and schemas implement normative contracts but do not create them; and
- a new Concept or graph edge requires a separate Architecture Board decision.

Those rules are individually sound, but they are scattered across governance, Concept specifications, Patterns and accepted decisions. The absence of one routing contract creates two opposite risks:

1. a widely reused product or domain field may be promoted into Core without independent semantic evidence; or
2. a genuinely shared operational responsibility may be kept in incompatible local models because no common admission path exists.

AD-015 opens AB-061 to decide the reusable boundary. Revision `0.1.0` does not select a model or artifact home.

## 2. Decision statement

AD-015 asks two independent questions:

1. **Semantic admission model:** what evidence distinguishes Core semantic authority from domain-local or implementation-local responsibility?
2. **Artifact home:** which governed artifact, if any, owns that reusable test and its machine-readable projection?

The Board must select both explicitly. Choosing a separate OCP does not prove that a candidate belongs to Core. Choosing a Pattern does not make every structurally conforming domain statement semantically equivalent. Choosing a machine-readable registry does not make the registry an authority source.

## 3. Scope

This discovery covers admission and extension decisions for:

- fundamental Concepts and their identity;
- current Concept dependency graph edges;
- non-Concept identified record contracts;
- local structured values owned by an accepted Concept;
- Pattern invocation and optional modules;
- exact rule, evaluator and result vocabularies;
- domain-owned namespace/profile extensions;
- Core interoperability envelopes;
- derived projections and stored assertions;
- executable fixtures, rule manifests and checker modules; and
- implementation-only schemas, APIs, UI models, indexes and caches.

It must define how a proposal is routed to one of those forms without using implementation convenience as ontology evidence.

## 4. Explicitly out of scope

AD-015 does not:

- admit or reject any specific new Concept;
- create OCP-016, P-002, a profile registry, schema or checker rule;
- add a current or future Concept graph edge;
- reopen an accepted decision without an explicit reopening act;
- decide Spectrum, Core location/geometry, authorization, visibility, agreement, Conflict, Risk, reservation or allocation;
- define a production plugin, module loader, API, persistence format or deployment boundary;
- define data classification, access control or sensitive-data handling policy;
- decide which domain modules the product must ship; or
- promote any document or Concept to Canonical.

No example may use real coordinates, unit identities, live infrastructure, operational plans, personnel or other sensitive data.

## 5. Terms

### 5.1 Foundation Core

**Foundation Core** is the smallest set of governed semantic contracts intended to be shared across foundation consumers under one explicit authority. Repository location, deployment centrality, database reuse or UI prominence does not make a contract Core.

### 5.2 Domain-local contract

A **domain-local contract** has a named domain owner and exact namespace/version. It may be rigorous, replayable and widely deployed while remaining outside Core semantic authority.

Domain-local does not mean informal, optional, low quality or unreviewed. It means that the stated semantics are not claimed as universal foundation semantics.

### 5.3 Implementation-local structure

An **implementation-local structure** exists to realize storage, transport, API, UI, indexing, caching or computation. It has no ontology authority unless a separately accepted contract assigns one.

### 5.4 Admission claim

An **admission claim** is a reviewed proposal that one exact semantic responsibility belongs in Core, in a Core interoperability envelope, in a binding-when-invoked Pattern, or outside Core.

### 5.5 Interoperability envelope

A **Core interoperability envelope** governs only the exact shared boundary it names, such as subject/profile/version/provenance binding and ambiguity rejection. It does not import the full domain vocabulary or establish cross-profile equivalence automatically.

### 5.6 Extension

An **extension** adds exact domain-owned semantics behind an accepted extension point. It cannot change the identity, result vocabulary, authority or invariants of the Core contract it extends.

### 5.7 Semantic authority

**Semantic authority** is the legitimate right of one exact artifact, rule, evaluator or profile owner to state one exact kind of fact or conclusion. Authority is never selected by newest timestamp, storage order, issuer count, source count, deployment count, popularity or label similarity.

## 6. Existing evidence

The repository already supplies both positive and negative boundary cases.

| Case | Accepted boundary evidence |
|---|---|
| Resource, Operation, Assignment, Constraint, Organization, Objective, Capability, Event | fundamental Concepts with separately reviewed identity and responsibility |
| Organization relationships, observations, outcome assessments, Capability claims, coordination proposals/responses | identified records; record identity does not require fundamental Concept identity |
| P-001 | reusable form only when explicitly invoked; no domain semantics |
| Capability namespaces | Core definition/reference integrity with domain-owned specialized semantics |
| OCP-011 and OCP-012 activations | contract-local rule activation; one consumer does not create a global evidence policy |
| Result | rejected as a fundamental Concept; realized outcomes use governed assessment records |
| State and Readiness | no shared current authority; exact local sources remain authoritative |
| Operational Area and Environment | local Operation binding and taxonomy category; no reusable Core identity |
| visibility and agreement | no new shared authority without concrete consumer and legitimate rule/result owners |
| checker and manifests | executable reference implementation whose sources resolve to normative OCP rules |

The selected boundary must explain all of these without treating prior outcomes as arbitrary exceptions.

## 7. Admission object classification

Before evaluating importance or reuse, every proposal must state what kind of thing it asks Core to own.

| Requested object | Required first question | Common category error |
|---|---|---|
| fundamental Concept | does one subject have stable identity and responsibility independent of representation? | promoting a label, status, assessment or relationship |
| graph edge | does the source Concept normatively depend on the target under one owner? | turning a useful reference into current dependency |
| identified record | does an attributable assertion need its own identity/history? | promoting every record to a Concept |
| local structured value | is the value meaningful only inside one owning subject/context? | inventing a reusable registry for local state |
| Pattern | are form obligations repeated independently of domain semantics? | hiding domain vocabulary inside a reusable shape |
| rule/result vocabulary | who owns inputs, rule version, evaluation context and result meaning? | treating checker behavior as normative authority |
| domain profile | which exact namespace/version owner defines the specialized meaning? | assuming label or shape equivalence across domains |
| interoperability envelope | what minimum shared binding and rejection behavior is actually needed? | importing the entire domain model into Core |
| implementation structure | which accepted semantic contract does it realize? | deriving ontology from tables, APIs or screens |

If the requested object is not explicit, the admission claim is not reviewable.

## 8. Authority ledger

Every admissible governance model must preserve these authority limits.

| Actor or artifact | May own | Must not own by implication |
|---|---|---|
| Architecture Board | admission decision, lifecycle and reviewed scope | domain truth, evaluator correctness or product authorization |
| defining OCP | exact Core domain semantics it defines | unrelated domain specialization or implementation schema |
| Pattern | reusable form selected by invocation | Concept identity, domain vocabulary or truth |
| domain profile owner | exact namespaced specialized semantics | universal Core meaning or another profile's interpretation |
| interoperability envelope | exact shared binding and fail-safe rejection | hidden translation or equivalence between profiles |
| rule/evaluator owner | one exact result under named inputs/version/context | broader truth, authorization or downstream decision |
| executable checker | finite conformance evidence for cited normative rules | new semantics, legitimate authority or production validation |
| product implementation | storage, transport, UI and computation | ontology admission merely because a feature exists |

No row inherits another row's authority through reuse, reference, containment or technical control.

## 9. Minimum evidence questions

Every positive-capable admission model must answer, or explicitly decline to own, all of these:

1. **Operational reality:** what real-world responsibility exists independently of software representation?
2. **Object class:** is the proposal a Concept, record, local value, Pattern, rule, profile, envelope or implementation structure?
3. **Consumer:** which concrete accepted or separately reviewed consumer needs the shared semantics?
4. **Identity:** what remains the same across versions, contexts and representations, if anything?
5. **Owner:** who legitimately owns identity, vocabulary, change and interpretation?
6. **Authority:** exactly what may the admitted contract state or derive?
7. **Non-authority:** which tempting conclusions remain forbidden?
8. **Dependencies:** which accepted Concepts/contracts are required, and which graph edges are actually justified?
9. **Versioning:** what exact version/snapshot is replayed, and how are correction and supersession handled?
10. **Failure:** what happens for missing, ambiguous, conflicting, stale, unknown-version or incomparable input?
11. **Interoperability:** is shared meaning required, or only exact reference exchange and mismatch rejection?
12. **Evidence location:** which guarantees belong to Core fixtures and which require domain-owned fixtures?
13. **Sensitivity:** can foundation evidence remain synthetic and non-sensitive?
14. **Migration:** what registry, taxonomy, dependency, Pattern invocation and generated projections must change atomically?
15. **Reopening:** does the proposal contradict an accepted mandate, negative verdict or deferred boundary?

A positive admission claim fails if any authority-bearing answer is “the implementation”, “the latest record”, “the most issuers”, “the common label” or an unnamed future owner.

## 10. Semantic-governance models

### G0 — case-by-case decisions only

Each AD continues to construct its own boundary tests. OCP-001 retains only current general governance rules; no reusable Core Boundary contract is introduced.

This minimizes new doctrine. Its main risk is inconsistent admission criteria, repeated review defects and boundary drift across Concepts, records, profiles and result vocabularies.

### G1 — one binary Core / non-Core gate

A universal checklist returns only “Core” or “non-Core”. Positive proposals then choose their concrete artifact through the normal AD/OCP process.

This is easy to explain. Its main risk is collapsing domain-owned profiles, interoperability envelopes, Patterns, local structured values and implementation structures into one undifferentiated “non-Core” bucket.

### G2 — tiered admission and extension classes

One reusable contract routes proposals among explicit classes:

1. fundamental Core Concept or dependency;
2. Core non-Concept record/rule/local-value contract;
3. binding-when-invoked Pattern;
4. Core interoperability envelope with domain-owned semantics;
5. governed domain-local contract; or
6. implementation-local structure.

This matches the forms already present in the repository. Its main risk is creating a bureaucratic taxonomy whose class labels appear decisive even when owner and consumer evidence remain weak.

### G3 — domain-first with a minimal Core envelope

All new specialized semantics remain domain-local unless a concrete cross-domain consumer proves a minimum shared envelope. Fundamental Core admission remains possible only through a separate identity decision.

This strongly limits Core growth. Its main risk is fragmentation: genuinely shared responsibilities may acquire incompatible domain identities before the cross-domain need is acknowledged.

### G4 — consumer-specific activation

Core defines stable baseline identities/forms, while each positive-capable rule, result vocabulary or profile becomes active only for one exact accepted consumer contract. OCP-011 and OCP-012 provide precedents.

This prevents one local activation from becoming global policy. Its main risk is proliferation of near-duplicate consumer profiles and hidden divergence behind structurally similar results.

The models may be combined only if the Board states precedence and routing. For example, G2 may classify a proposal and G4 may govern activation inside the selected class. An implicit mixture is not an outcome.

## 11. Artifact-home outcomes

### H0 — no new home

Accepted ADs remain the only complete boundary records. External review compares each proposal directly against OCP-001 and precedent.

Risk: there is no single defining location and reviewers must reconstruct doctrine from history.

### H1 — extend OCP-001

Ontology Governance owns the complete Core Boundary Test, admission classes, evidence obligations and lifecycle.

Risk: OCP-001 may mix process governance with domain-architecture classification and become too broad.

### H2 — separate Core Boundary OCP

A later OCP, provisionally OCP-016, owns the reusable semantic admission and extension contract. OCP-001 owns only the trigger, review choreography and reference integrity.

Risk: a separate specification may duplicate OCP-001 or be mistaken for a registry that can approve candidates without a Board act.

### H3 — new binding-when-invoked Pattern

A later Pattern, provisionally P-002, owns the reusable admission/evidence shape. Candidate artifacts opt in through exact `Uses-Patterns` metadata.

Risk: admission is mandatory governance, whereas Patterns are optional until invoked; Pattern form also cannot legitimately decide domain semantics or Concept status.

### H4 — machine-readable admission registry

A structured registry records proposal class, owner, consumer, decision, exact dependencies and evidence status. Human-readable documents remain normative.

Risk: fields and status automation may become a shadow authority or encode weak evidence as a passing score.

### H5 — layered human-readable contract plus derived projection

OCP-001 owns the mandatory trigger and review lane; a separate OCP owns the human-readable semantic test; a machine-readable registry is only a checked projection; Patterns are invoked only when the selected proposal actually needs reusable form.

Risk: several artifacts must remain synchronized and each boundary between them needs a single defining owner.

## 12. Combination constraints

Any selectable `G × H` combination must state:

- the single defining location of every normative rule;
- whether the boundary applies automatically or only through invocation;
- who creates and who approves an admission claim;
- whether a machine-readable representation is authoritative or derived;
- how a candidate moves between domain-local, envelope and Core classes;
- what event requires reopening rather than ordinary versioning;
- how a rejected or superseded candidate is removed from registries and generated maps;
- which conditions require executable evidence now and which are impossible before selection; and
- how a human reader can understand the decision without inspecting code or a registry row.

No combination may make a numeric score, checklist total or tool output sufficient for admission.

## 13. Mandatory counterexamples

Every admissible model must handle these cases:

1. the same field appears in three products, but it is only UI state;
2. several domains use the label `ready` with different criteria and times;
3. two domains use the same record shape for semantically different assertions;
4. one domain has a legitimate profile owner but no cross-domain consumer;
5. two accepted consumers need one exact identity and version contract;
6. a taxonomy category is mistaken for a fundamental Concept;
7. an identified record is mistaken for a Concept only because it has history;
8. a repeated record form is copied instead of invoking an applicable Pattern;
9. a Pattern-conforming record smuggles domain result vocabulary into Core;
10. a checker implements a rule whose normative source and legitimate owner are absent;
11. a shared database table is treated as proof of shared semantic identity;
12. an unknown or duplicate domain profile is translated by best effort;
13. a newer profile version is selected without exact caller binding;
14. a domain specialization changes the identity or invariant of its Core parent;
15. a proposal contradicts an accepted negative verdict without reopening it;
16. equal local spatial payloads are treated as a reusable Core area identity;
17. a positive Capability claim is promoted to availability, authorization or Readiness;
18. a generic assessment family is extended even though target/result/evidence authority no longer fits;
19. evidence needed for admission can be shown only with sensitive operational data;
20. a machine registry says “approved” while the human-readable Board act is absent;
21. newest timestamp, issuer count, source count, deployment count or list order selects authority; and
22. a domain-local contract is rejected merely because it is not Core.

Examples must use synthetic identities and opaque values. The model must distinguish “not Core” from “invalid”.

## 14. Unconditional evidence obligations

The following apply to G0–G4 and H0–H5:

1. identify the requested object class before selecting its artifact;
2. name concrete consumers and legitimate owners for every authority-bearing input/result;
3. preserve accepted Concept, record, Pattern and domain-profile responsibilities;
4. reject promotion based only on reuse, storage, UI, label, popularity or implementation convenience;
5. require explicit reopening when an accepted mandate would be contradicted;
6. preserve exact version/snapshot replay and fail-safe unresolved behavior where the proposal carries authority;
7. keep domain-local semantics explicit and reject unknown/incompatible profile equivalence;
8. state non-implications, especially for identity, truth, readiness, authorization, selection and Assignment;
9. require atomic registry/taxonomy/dependency/generated-projection migration when applicable;
10. retain human-readable normative meaning as the primary review surface;
11. use non-sensitive synthetic evidence; and
12. treat checker and registry output as evidence, not Board authority.

No unconditional fixture may require a new OCP, Pattern, registry, domain profile or checker module because at least one admissible outcome rejects each of those forms.

## 15. Model-conditional evidence

### 15.1 G0

- demonstrate that existing case-by-case ADs remain consistent without a reusable rule owner;
- provide a review method that detects drift across earlier decisions; and
- show how future reviewers find the full doctrine without reconstructing repository history manually.

### 15.2 G1

- define a binary result without treating every non-Core proposal as invalid;
- show how records, Patterns, envelopes and domain contracts are routed after a negative Core result; and
- reject score-based admission.

### 15.3 G2

- define mutually distinguishable admission classes and migration/reopening rules;
- test borderline cases where one proposal could appear to fit two classes; and
- prove that classification does not replace authority/consumer evidence.

### 15.4 G3

- exact-bind namespace/profile/version/owner and reject cross-profile ambiguity;
- show when a cross-domain consumer is strong enough to justify a Core envelope; and
- prevent domain-first placement from becoming permanent fragmentation by default.

### 15.5 G4

- exact-bind every activation to one consumer and baseline contract;
- reject global inheritance of consumer-local rule/result semantics; and
- detect near-duplicate profiles whose labels hide different authority.

### 15.6 H0–H5

Each artifact-home outcome must demonstrate its own governance semantics:

- H0: precedent discoverability and consistency;
- H1: separation of process governance from semantic classification inside OCP-001;
- H2: non-duplication and clear dependency between OCP-001 and the new OCP;
- H3: why optional invocation can satisfy a mandatory admission boundary;
- H4: registry ambiguity, stale status and Board-act mismatch detection;
- H5: exact source ownership and synchronization across layers.

## 16. Outcome-fairness audit

External review must reject any evidence plan that assumes the selected artifact home or admission model.

In particular:

- G0/H0 cannot be required to provide a new registry or invocation;
- G1 cannot be rejected only because it lacks G2's tier labels;
- G3 must show exact ambiguity rejection, not a universal Core vocabulary;
- G4 must show consumer-specific replay, not one global activation;
- H1/H2 must remain human-readable without requiring executable registry fields;
- H3 may use Pattern evidence only if the invocation/mandatory-governance contradiction is resolved;
- H4/H5 must treat machine state as a projection of reviewed authority, not the authority itself; and
- no model may use sensitive domain fixtures to make another model appear unevaluable.

The falsification target is explicit: **the evidence plan assumes the Core/domain boundary mechanism that the selected outcome rejects**.

## 17. External-review falsification targets

External review must try to disprove:

1. that semantic admission and artifact home are genuinely separate axes;
2. that “Core” means shared semantic authority rather than code or deployment centrality;
3. that the object classification covers Concepts, records, local values, Patterns, rules, profiles, envelopes and implementation structures;
4. that every positive route names concrete consumers and legitimate owners;
5. that domain-local is preserved as a valid governed outcome rather than treated as failure;
6. that exact profile/version mismatch fails closed without label translation;
7. that Pattern form cannot silently create domain meaning;
8. that checker/registry state cannot approve an admission claim;
9. that accepted decisions can be contradicted only through explicit reopening;
10. that migration accounting remains atomic when status or graph projections change;
11. that evidence obligations remain outcome-fair across G0–G4 and H0–H5;
12. that no excluded domain decision, sensitive data or implementation schema entered the discovery; and
13. that the document is usable by a human reviewer without reading code.

## 18. Exit criteria

AD-015 may leave Discovery only when:

1. external comparison evaluates G0–G4 independently of H0–H5;
2. at least the accepted cases in §6 and all §13 counterexamples are mapped;
3. the selected combination has one defining owner for each normative rule;
4. object-class routing and authority ledgers are complete;
5. “domain-local”, “Core envelope” and “Core semantics” have non-overlapping meanings;
6. reopening, migration and negative/deregistration behavior are explicit;
7. outcome-fair human and executable evidence plans exist;
8. no numeric score or machine registry can substitute for a Board act;
9. synthetic evidence is sufficient; and
10. the Board selection remains separate from any OCP, Pattern, schema, checker, Concept-status or graph change.

## 19. Discovery status and next cycle

Revision `0.1.0` opens AD-015 and AB-061 in `Discovery`. It records no preferred `G × H` combination.

A later `AD-015A` comparison should map accepted precedents and counterexamples across both axes. A separate `AD-015B` Board act may select a combination or retain Discovery. Any OCP-001 amendment, OCP-016, P-002, registry, schema, checker rule, Concept status or graph change requires a later separately reviewed PR.
