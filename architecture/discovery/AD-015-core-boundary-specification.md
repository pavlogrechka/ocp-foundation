---
Decision-ID: AD-015
Title: Core Boundary Admission and Extension Discovery
Version: 0.3.0
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-001, OCP-002, OCP-003, OCP-004, OCP-006, OCP-009, OCP-011, OCP-012, P-001, AD-001, AD-006, AD-010, AD-011, AD-014
Applies-To: AB-061, Core admission, domain extensions, interoperability envelopes
Review-After: OCP-016 implementation evidence falsifies the G2 routing contract, H2 ownership split or no-projection baseline
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

## 20. AD-015A comparison method

Revision `0.2.0` compares the two axes without selecting either one.

The comparison uses five questions in order:

1. **Coverage:** can the model route every accepted precedent and every §13 counterexample?
2. **Authority:** does it assign only the smallest legitimate semantic authority?
3. **Failure:** does missing ownership, consumer evidence or exact resolution remain non-permissive?
4. **Governance:** is there one human-readable defining location and an explicit Board act?
5. **Cost:** what new synchronization, review or fragmentation burden does the model create?

No numeric score is used. “Strong”, “conditional”, “weak” and “blocked” below summarize evidence, not approval status. A technically easy implementation receives no positive weight unless it closes the semantic and authority questions.

The comparison keeps three decisions separate:

- whether a reusable admission doctrine is needed at all;
- which semantic model provides the doctrine; and
- which artifact owns its normative text and any derived projection.

## 21. Concrete admission scenarios

### S1 — repeated product field

Three products expose a field named `coordination_state`, but each UI computes it from different local data. No accepted consumer needs one shared identity or result vocabulary.

The field is implementation-local. Reuse count is not Core evidence. G1 must return non-Core without calling the field invalid; G2 can route it explicitly to the implementation class. G3/G4 add no value unless a real domain or consumer contract appears.

### S2 — specialized domain Capability

A named domain defines an exact versioned Capability specialization. A Core consumer needs to preserve its identity and reject unknown versions but does not interpret the specialized payload.

The domain owns meaning; a Core envelope may own exact reference integrity. G3 is directly applicable, G2 can route the proposal to its envelope class, and G4 is relevant only if the consumer activates a rule/result beyond reference resolution.

### S3 — repeated attributable record form

Several contracts need stable record identity, provenance and history-preserving supersession, but their domain statements differ.

The repeated form may justify P-001 invocation. It does not make the records one Concept or give P-001 their domain vocabulary. G2 distinguishes Pattern form from record semantics; a binary gate must still explain that the Pattern is neither “the domain Concept” nor “outside governance”.

### S4 — realized outcome representation

A consumer needs an attributable conclusion about one exact Objective and evidence snapshot. A generic fundamental `Result` identity is not demonstrated.

Accepted precedent routes this to OutcomeAssessmentRecord rather than a Concept. A viable model must preserve the negative identity verdict while allowing a Core non-Concept contract.

### S5 — local spatial context

An Operation needs two exact opaque spatial payloads, but no reusable area subject exists across Operations.

Accepted precedent routes this to an Operation-owned local structured value. Equal payload does not create shared identity. G2 represents this class directly; G1 must avoid treating “not a Concept” as “not governed”.

### S6 — reusable occurrence identity

Independent observations and assessments need to reference the same occurrence across contexts and history. The occurrence remains identifiable independently of reports.

This is positive fundamental Concept evidence, represented by Event. Domain-first routing cannot deny a genuine shared identity merely because domain occurrence vocabularies also exist.

### S7 — consumer-local evidence activation

One accepted assessment kind needs an exact freshness/ambiguity rule, while other assessment kinds have no legitimate global lifetime.

G4 directly fits the activation. G2 can classify activation as a Core rule contract without global inheritance. The artifact home must keep the baseline contract and consumer-local rule source unambiguous.

### S8 — visibility conclusion without an owner

Product code can determine that bytes were technically exposed, but no accepted policy owner or shared result vocabulary exists.

No model may promote technical access into Core visibility authority. G0 records the negative case locally; G1 rejects Core admission; G2 routes implementation evidence separately; G3/G4 remain blocked until an exact domain/consumer owner exists.

### S9 — useful reference proposed as a graph edge

One OCP mentions another Concept in examples, but the source Concept's identity and invariants do not depend on the target.

The reference does not become a current Concept dependency. G2's object classification separates reference use from graph admission; every model still requires a separate Board act for an edge.

### S10 — machine admission registry

A generated registry records proposal class, owner and review state. Its row says `approved`, but the exact human-readable Board act is missing.

The registry must fail governance validation or remain non-authoritative. H4 can only be a projection; H5 must define synchronization from human authority to machine state, never the reverse.

## 22. Semantic-model comparison

| Model | Coverage | Authority fit | Fail-safe behavior | Main benefit | Main risk | Current evidence |
|---|---|---|---|---|---|---|
| G0 — case-by-case | Can represent every decision by writing another AD. | Narrow per decision. | Depends on each AD repeating the doctrine correctly. | No new abstraction or migration. | Review drift, omissions and inconsistent routing recur. | **Admissible control, weak reusable answer.** Existing history proves viability and its cost. |
| G1 — binary gate | Distinguishes Core from non-Core, but does not route intermediate governed forms. | Simple Board authority. | Can fail closed on incomplete admission claims. | Easy for humans to apply initially. | “Non-Core” can collapse valid records, Patterns, envelopes and local contracts. | **Partial.** Useful first question, insufficient as the whole repository boundary. |
| G2 — tiered classes | Directly represents all existing artifact/semantic forms. | Authority can remain class-specific. | Ambiguous class or missing owner can reject. | One routing language for Concepts, records, Patterns, envelopes, domains and implementation. | Class bureaucracy or class labels substituting for evidence. | **Strong hypothesis, not selected.** Accepted precedents already occupy every proposed class. |
| G3 — domain-first envelope | Strong for specialized domain semantics and cross-domain exchange. | Preserves domain ownership and a narrow Core envelope. | Unknown/incompatible profiles reject exactly. | Limits Core growth and false equivalence. | Fragmentation and weak treatment of genuinely shared Concepts/local Core contracts. | **Strong conditional route, weak universal model alone.** |
| G4 — consumer activation | Strong for rule/result/profile activation under exact consumers. | Prevents local policy becoming global. | Missing consumer/rule/snapshot rejects. | Proven by OCP-011/OCP-012 activation practice. | Profile proliferation and near-duplicate semantics. | **Strong conditional route, not a complete Concept/record admission model alone.** |

### 22.1 Decision-separating observations

1. G0 proves that no new doctrine is logically required, but three repeated outcome-fairness defects and repeated reconstruction of authority ledgers are evidence of governance cost.
2. G1 captures the essential “implementation reuse is not Core” question, but accepted local values, non-Concept records and Patterns show that binary placement is not enough.
3. G2 fits the repository's existing forms without changing their authority. That is evidence of coverage, not proof that one taxonomy should govern them.
4. G3 supplies the strongest safe treatment of domain specialization, but cannot by itself explain Event, local OCP-004 binding or P-001 form ownership.
5. G4 supplies the strongest safe treatment of consumer-local rule activation, but cannot decide whether a new subject is a Concept, record or domain profile.

The leading comparison question for AD-015B is therefore whether G3 and G4 are independent universal alternatives, explicit routing modes inside G2, or obligations that any selected model must support. AD-015A does not answer it.

## 23. Artifact-home comparison

| Home | Mandatory applicability | Single defining location | Human-readable primacy | Machine projection | Main risk | Current evidence |
|---|---|---|---|---|---|---|
| H0 — no new home | Case-by-case only. | No; doctrine is reconstructed from precedents. | Yes, across many ADs. | None required. | Drift and discoverability failure. | **Admissible control.** |
| H1 — OCP-001 | Automatic governance rule. | Yes, if added once. | Strong. | Existing governance checker may project finite fields later. | OCP-001 becomes an oversized mix of process and semantic classification. | **Viable.** OCP-001 already owns Concept admission and outcome fairness. |
| H2 — separate OCP | Automatic via one OCP-001 trigger. | Yes, with explicit division from OCP-001. | Strong. | Optional later projection. | Duplicate governance or false self-approval by a “boundary specification”. | **Viable.** Best separation if non-duplication is proven. |
| H3 — Pattern | Optional until invoked. | Yes for selected form. | Strong. | Exact invocation metadata exists. | Cannot make mandatory governance optional or decide domain meaning/status. | **Blocked as the sole home; conditional for reusable admission-evidence form.** |
| H4 — registry | Only if a human rule makes it mandatory. | Machine source may be unique but cannot be normative alone. | Weak if used alone. | Native. | Shadow authority, score/status approval and stale state. | **Blocked as sole normative home; viable derived projection.** |
| H5 — layered | Mandatory trigger plus separate semantic owner. | Yes, if source boundaries are exact. | Strong. | Derived registry/checker possible. | Synchronization burden and duplicated rules across layers. | **Strong hypothesis, not selected.** |

### 23.1 Decision-separating observations

- H0 preserves current authority but leaves the named Core Boundary Test without one definition.
- H1 has the lowest artifact count and the highest scope-expansion risk.
- H2 gives semantic admission its own readable document, but must not become an artifact that “admits” candidates without the Board.
- H3 matches repeated form obligations, not mandatory admission authority. It can supplement another home, not replace it under current Pattern semantics.
- H4 is valuable only if exact mismatch with the Board act fails closed and the human artifact remains primary.
- H5 can combine those strengths, but is justified only if H1 or H2 alone cannot supply sufficient review and mechanical integrity.

## 24. G × H compatibility matrix

The matrix identifies structural fit, not approval.

| Model \ Home | H0 | H1 | H2 | H3 | H4 | H5 |
|---|---|---|---|---|---|---|
| G0 | **Native control** | Tension: codifying a full reusable test would cease to be G0 | Tension for the same reason | Conditional only for repeated evidence form | Projection cannot replace absent doctrine | Usually excessive; could only improve precedent discovery |
| G1 | Possible but repeated in every AD | **Strong fit** | **Strong fit** | Blocked as sole mandatory gate | Conditional derived yes/no projection | Viable, probably more layers than a binary gate needs |
| G2 | Possible but high drift | Viable, with OCP-001 scope risk | **Strong fit** | Partial: Pattern may own evidence form, not class authority | Conditional derived class/status projection | **Strong fit** if synchronization is justified |
| G3 | Possible per domain AD | Viable as universal domain/envelope rule | **Strong fit** | Partial for envelope form after invocation | Conditional profile/admission projection | **Strong fit** for human rule plus exact profiles |
| G4 | Possible per activation AD/OCP | Viable as consumer-activation doctrine | **Strong fit** | Partial for reusable activation form | Conditional consumer-profile projection | **Strong fit** if profile proliferation needs mechanical control |

Any `Tension`, `Partial` or `Conditional` combination needs an explicit resolution in AD-015B. `Blocked as sole` does not prohibit using the artifact for a narrower selected sub-responsibility.

## 25. Authority and complexity accounting

| Candidate | New semantic authority | New artifact authority | Synchronization burden | Failure pressure |
|---|---|---|---|---|
| G0 × H0 | none beyond each later AD | none | low per artifact, high across history | doctrine omission remains manual-review risk |
| G1 × H1 | binary admission rule in OCP-001 | no new class | low | valid intermediate governed forms may be mislabeled |
| G2 × H2 | tiered routing semantics | one later OCP | medium | ambiguous classification must fail review |
| G2 × H5 | tiered routing plus explicit projections | later OCP and derived registry/checker | high | source duplication or stale projection |
| G3 × H2/H5 | domain-first/envelope rule | human rule plus optional profiles | medium/high | unknown/incompatible profile must reject |
| G4 × H2/H5 | consumer activation rule | human rule plus optional consumer projection | medium/high | missing exact consumer/rule must reject |

“New semantic authority” means authority to classify or route an admission claim, not authority over the candidate's domain truth. Every candidate still requires its own Board act and defining contract.

## 26. Accepted-precedent mapping across G0–G4

| §6 precedent | G0 | G1 | G2 | G3 | G4 |
|---|---|---|---|---|---|
| eight fundamental Concepts | separate identity AD for each | Core positive, artifact still separate | fundamental Concept class | domain-first exception when shared identity proves necessary | not sufficient; activation cannot create identity |
| identified record contracts | separate record decision | governed but binary route is underspecified | Core non-Concept record class | domain record plus envelope when semantics remain local | applies only to consumer-local rules over the record |
| P-001 | separate Pattern decision | neither cleanly Core Concept nor non-Core | binding-when-invoked Pattern class | domain records may invoke it without importing semantics | activation may invoke form only if exact contract selects it |
| Capability namespaces | handled in AD-005/OCP-009 | Core reference contract, domain semantics outside | envelope/domain classes | direct positive precedent | consumer activation optional, not global |
| OCP-011/OCP-012 activations | separate act for every activation | Core positive but scope risk remains | Core rule/consumer-profile route | domain owner possible only after reopening | direct positive precedent |
| Result negative identity | AD-006 exception preserved | non-Concept, but record route unspecified | Core record rather than Concept class | could remain domain-local if no shared assessment contract | activation cannot reverse identity verdict |
| State/Readiness no authority | AD-011 negative act | non-Core current outcome | domain/local/implementation route pending future evidence | domain profile possible only after reopening | consumer activation possible only after exact mandate |
| Operational Area/Environment | AD-014 local decision | non-Concept, but local governance underspecified | local structured value/category route | domain spatial profiles remain exact inputs | consumer geometry/suitability rules remain separately gated |
| visibility/agreement no authority | AD-010 negative act | non-Core current outcome | implementation/domain/consumer route only with owners | named domain policy possible after reopening | exact consumer policy activation possible after reopening |
| checker/manifests | each OCP cites implementation | non-Core implementation evidence | implementation/derived-projection class | domain fixtures can complement Core evidence | consumer-local executable evidence remains source-bound |

No model may reinterpret a prior negative verdict as invalid domain work. No model may reinterpret an Accepted Concept as evidence that every specialization belongs to Core.

## 27. Counterexample mapping — cases 1–11

| # | Pressure | G0 | G1 | G2 | G3 | G4 |
|---:|---|---|---|---|---|---|
| 1 | repeated UI field | reject in case AD/review | non-Core | implementation-local class | domain only if a real owner exists; otherwise implementation | no consumer activation |
| 2 | incompatible `ready` labels | preserve separate negative/domain decisions | non-Core shared meaning | domain contracts; no shared Readiness class | exact profiles, mismatch rejects | exact consumer criteria only after reopening |
| 3 | same record shape, different assertions | separate semantic decisions | shape does not make Core meaning | Pattern form separated from record semantics | domain meanings remain namespaced | consumers bind exact kind/profile |
| 4 | legitimate domain, no cross-domain consumer | keep domain-local | non-Core but valid | governed domain class | direct domain-local outcome; no envelope need proved | no Core activation without consumer |
| 5 | two consumers need exact shared identity | separate identity AD | candidate Core positive | Concept/record/envelope selected by object class | Core envelope only if domain meaning remains local | activation only if shared need is a rule/result, not subject identity |
| 6 | taxonomy category mistaken for Concept | reject by OCP-001 precedent | non-Core Concept result | category/local class | domain taxonomy may remain local | activation irrelevant |
| 7 | record mistaken for Concept | preserve record precedent | Core/non-Core binary insufficient to pick form | Core/domain record class | domain record if meaning local | activation does not create Concept identity |
| 8 | copied repeated record form | each AD must notice P-001 | binary gate misses invocation choice | Pattern class and exact invocation review | domain contract may invoke P-001 | consumer contract cannot silently copy Pattern obligations |
| 9 | Pattern smuggles result vocabulary | reject in case review | no Core domain authority follows | Pattern owns form only | domain vocabulary stays profile-owned | exact consumer owns only its result kind |
| 10 | checker rule lacks owner/source | reject implementation as authority | non-Core/unowned | implementation invalid against missing normative contract | domain checker needs exact domain owner | activation unavailable without exact consumer/rule owner |
| 11 | shared table treated as identity | reject in case review | non-Core evidence | implementation-local structure | shared storage does not merge domains | shared deployment does not activate semantics |

## 28. Counterexample mapping — cases 12–22

| # | Pressure | G0 | G1 | G2 | G3 | G4 |
|---:|---|---|---|---|---|---|
| 12 | unknown/duplicate profile translated | each AD must define rejection | no Core equivalence | envelope/domain route rejects ambiguity | exact zero/multiple resolution rejects | exact consumer cannot activate unknown profile |
| 13 | newest profile selected | exact caller binding required per decision | non-permissive | no latest-selection in any class | exact version only | consumer activation exact-binds baseline/profile/rule |
| 14 | domain specialization changes Core parent | separate amendment/reopening act | reject Core compatibility | extension invariant forbids identity/semantic override | profile owns only specialization | activation cannot change baseline identity/results |
| 15 | accepted negative verdict contradicted | explicit reopening AD | fail admission pending reopening | reopening route before reclassification | domain evidence cannot silently override verdict | consumer activation blocked without reopening mandate |
| 16 | equal spatial payload becomes area identity | preserve AD-014A outcome | non-Core reusable identity | local structured value route | exact domain profile, no Core subject equivalence | geometry consumer rule cannot create subject identity |
| 17 | Capability claim becomes Readiness/auth | preserve OCP-012 boundary | reject broader Core conclusion | claim/eligibility/readiness classes stay distinct | domain result cannot masquerade as Core | consumer result exact and non-transitive |
| 18 | generic assessment extension dilutes semantics | separate comparison act | reject unless shared meaning proved | record extension vs sibling route by target/result/evidence fit | domain assessment remains namespaced | exact consumer activation cannot change baseline vocabulary |
| 19 | only sensitive evidence can prove admission | retain Discovery/no selection | fail positive gate | evidence-gap/review route | domain evidence remains outside Core; synthetic envelope still required | no activation until non-sensitive conformance evidence exists |
| 20 | registry says approved, Board act absent | registry ignored | no admission | derived projection mismatch fails | profile publication is not Board admission | consumer row is not activation authority |
| 21 | count/order/newest selects authority | reject in every case | forbidden gate input | forbidden across all classes | exact owner/version only | exact consumer/rule/snapshot only |
| 22 | domain-local rejected for not being Core | preserve valid local outcome | “non-Core” explicitly not “invalid” | governed domain class | direct valid outcome | consumer-local contract may coexist without global Core result |

## 29. Evidence ownership and executable boundary

| Evidence | Human-readable owner | Executable evidence owner | Not established |
|---|---|---|---|
| candidate object class | selected boundary contract plus candidate AD | structural admission fixture if selected | domain truth or Board approval |
| Concept identity | candidate defining OCP/AD | Concept status/dependency checker subset | metaphysical proof from a passing test |
| record vs Pattern form | domain OCP plus invoked Pattern | module fixtures and invocation metadata | shared domain meaning from shared shape |
| domain profile identity/version | exact domain contract | domain fixtures plus Core ambiguity rejection | cross-profile equivalence |
| consumer activation | baseline OCP plus exact consumer contract | contract-local rule/profile fixtures | global rule inheritance |
| implementation placement | product architecture | optional conformance tests | ontology authority |
| admission status | Architecture Board act | derived consistency check only | approval by registry/checker output |

Foundation fixtures must remain synthetic. A domain may own sensitive operational validation outside this repository, but a Core admission claim still needs non-sensitive conformance evidence for every shared guarantee it asks Foundation to own.

## 30. Candidate combinations for Board comparison

AD-015A reduces the full matrix to six decision-separating combinations without selecting one:

### C0 — G0 × H0: precedent-only control

Continue case-by-case ADs. Improve review guidance informally but create no reusable admission contract.

This is the minimum-change control. It is credible only if external review concludes that repeated doctrine reconstruction is acceptable.

### C1 — G1 × H1: binary gate in OCP-001

Add one mandatory Core/non-Core test to existing governance.

This is the smallest positive reusable contract. It must show where valid records, Patterns, envelopes, local values and domain contracts go after a non-Core result.

### C2 — G2 × H1: tiered routing inside OCP-001

OCP-001 owns both process and admission classes.

This minimizes artifact count but risks making governance too broad and mixing choreography with semantic architecture.

### C3 — G2 × H2: tiered routing in a separate OCP

OCP-001 requires the boundary review; the later OCP owns object classification, authority/evidence questions and migration behavior.

This supplies one readable semantic owner with moderate synchronization. It must prove non-duplication and keep the Board act external to the specification.

### C4 — G2 with G3/G4 routes × H5

A separate OCP defines tiered routing; domain-first envelopes and consumer activations are explicit routes; a derived registry/checker enforces finite structural integrity.

This covers the most accepted precedents but has the highest bureaucracy and shadow-authority risk. It is justified only if C3 cannot express profiles/activations clearly without the extra layer.

### C5 — G3 or G4 × H2 with optional H3/H4 support

Select only one narrow reusable doctrine — domain envelopes or consumer activation — and leave all other admission questions case-by-case.

This is narrower than G2, but cannot claim to be the complete Core Boundary specification unless it explains Concept, record, local-value and implementation routing elsewhere.

## 31. Preferred hypotheses and unresolved proof

AD-015A does not make a Board selection. The current evidence supports this ordering for further review:

- **C3 is the leading minimal complete hypothesis** because it routes every accepted artifact form through one readable semantic owner without requiring a registry or Pattern.
- **C1 is the leading smaller alternative** if a binary gate plus existing artifact choreography can route intermediate forms without ambiguity.
- **C4 is the leading mechanically reinforced hypothesis** only if external evidence proves that a separate projection is needed; its additional layers are not free.
- **C0 remains the honest no-new-contract control.**
- H3 and H4 remain useful subordinate mechanisms but are not credible sole authority homes under current governance.
- G3 and G4 remain proven narrow practices; the unresolved question is whether they are top-level models or routes/obligations within a more complete model.

External review must challenge the “minimal complete” claim for C3. In particular, it should try to construct:

1. a valid accepted precedent that C3/G2 cannot route without importing domain semantics;
2. a reason OCP-001 cannot own the same rule cleanly under C2;
3. a machine integrity property that truly requires C4 rather than later implementation evidence; and
4. a smaller combination not represented by C0–C5.

## 32. AD-015A status and next act

Revision `0.2.0` completes the initial comparison while AD-015 and AB-061 remain `Discovery`. It changes no OCP, Pattern, schema, registry, checker rule, Concept status or graph edge.

After external review, a separate `AD-015B` Board act may:

- select one combination;
- select a stated composition with explicit precedence and source ownership;
- require another comparison because a viable model is missing; or
- retain G0/H0 and close the request for a reusable specification.

Implementation remains a later PR even if AD-015B selects H1, H2, H4 or H5.

## 33. Architecture Board decision — AD-015B

The Architecture Board accepts this decision by act **AD-015B** on **2026-08-05**, after Fable reviewed the complete AD-015A comparison on exact head `947677114b85766cb011c3ac3b8361df598fb18d`, found no defects and recommended merge. Codex independently accepted that verdict, Pavlo authorized the merge, and PR #76 was squash-merged with green post-merge CI.

This act selects a reusable semantic-routing model and its human-readable artifact home. It does not create or amend OCP-001 or OCP-016, define an admission schema, create a Pattern or registry, add checker code or fixtures, admit or remove a Concept, change Concept status, or add a graph edge.

### 33.1 Selected combination — C3 (`G2 × H2`)

AD-015 selects **C3 — tiered admission and extension routing in a separate Core Boundary OCP**.

The evidence supports a reusable routing contract because the repository already governs more than a binary Core/non-Core distinction: fundamental Concepts, Core non-Concept records and local values, binding-when-invoked Patterns, Core envelopes over domain-owned semantics, valid domain-local contracts and implementation-local structures all exist. Reconstructing those distinctions from precedent in every review has produced repeated drift.

A separate human-readable OCP is selected because semantic object classification, authority boundaries and migration behavior are substantial enough to obscure OCP-001's process-governance role. OCP-001 remains the mandatory trigger and review owner; the separate OCP owns the reusable semantic test. Neither document approves a candidate by itself.

C3 is the smallest compared combination that covers every accepted precedent and mandatory counterexample without requiring a registry, checker projection or optional Pattern invocation as governance authority.

## 34. Selected G2 routing contract

### 34.1 One primary semantic-authority route

Every admission proposal must identify exactly one primary semantic-authority route for each candidate object:

1. **fundamental Core Concept or dependency** — Core owns stable subject identity or an identity/invariant dependency after a separate positive Board act;
2. **Core non-Concept contract** — Core owns shared semantics for a record, rule, consumer activation or local structured value without granting fundamental Concept identity;
3. **Core interoperability envelope** — Core owns exact profile/reference resolution and fail-safe exchange guarantees while a named domain owns the referenced meaning;
4. **governed domain-local contract** — a named domain owns the meaning and lifecycle; Core does not claim cross-domain equivalence or a shared envelope;
5. **implementation-local structure** — software owns the representation and no shared semantic artifact is admitted.

These are authority routes, not quality grades. Domain-local and implementation-local results are not invalid merely because they are not Core. A Core envelope is not a weaker copy of domain semantics, and a Core non-Concept contract is not a provisional Concept.

One act may review several candidate objects, but each object must receive its own route and authority ledger. A label such as `Core`, `domain` or `record` is never sufficient evidence for the route.

### 34.2 Pattern is an orthogonal form route

G2's original six-class list included **binding-when-invoked Pattern**. AD-015B makes its relationship to the semantic routes explicit: Pattern selection is a secondary form decision, not a competing semantic owner.

A candidate in the Core non-Concept, Core-envelope or domain-local route may invoke an Accepted Pattern when it needs that reusable modeling form. The invocation exact-binds the Pattern and imports only its stated form obligations. It does not transfer subject identity, vocabulary, truth, authority or admission status.

No proposal invokes a Pattern merely by resembling an existing record shape. Mandatory Core Boundary governance cannot be implemented as an optional Pattern invocation.

### 34.3 Routing is not approval

The selected OCP may determine what evidence and authority questions apply to a candidate. It may not decide that the evidence is true, create an owner or consumer, or grant Accepted status.

Positive admission still requires:

- a human-readable candidate contract;
- named legitimate owners and concrete consumers for every positive guarantee;
- exact dependencies and version bindings;
- an explicit Architecture Board act;
- outcome-appropriate human evidence plus executable evidence for every mechanically expressible obligation; and
- complete atomic accounting when registries, status projections or graph views change.

Missing ownership, unresolved exact references, conflicting routes or evidence that depends on an unselected layer remain non-permissive.

## 35. Placement of G3 and G4

AD-015B does not select G3 or G4 as universal top-level models. It accepts their proven safeguards as conditional routing obligations inside G2.

### 35.1 G3 domain-first obligation

Specialized semantics remain in the governed domain-local route unless a concrete consumer proves either:

- a minimal Core envelope that preserves domain ownership and exact profile/version ambiguity rejection; or
- independently reusable Core identity or semantics that pass the full Concept or non-Concept admission path.

Domain popularity, repeated labels, deployment count or implementation reuse never prove the move. A Core envelope owns interoperability guarantees only; it cannot translate unknown profiles by similarity or import domain truth.

### 35.2 G4 consumer-activation obligation

A positive-capable rule, result vocabulary or profile is active only under its exact accepted consumer contract. Consumer activation may occur in the Core non-Concept, Core-envelope or domain-local route according to who owns the protected use.

Activation cannot create subject identity, change a baseline contract, become global policy, inherit into another consumer, or transfer by matching labels. Missing exact consumer, rule, input snapshot or evaluator authority rejects the positive path.

These obligations give C3 the safe domain and consumer behavior found in accepted precedents without selecting C4's additional registry/checker layer.

## 36. Selected H2 ownership and precedence

The later implementation must preserve one defining owner for each responsibility:

| Responsibility | Defining owner |
|---|---|
| mandatory Core Boundary trigger, review choreography and reference integrity | OCP-001 |
| semantic-authority routes, required authority/evidence questions, route movement and migration safeguards | separate Core Boundary OCP, provisionally OCP-016 |
| candidate identity, vocabulary, invariants, results and lifecycle | candidate's accepted defining OCP or named domain contract |
| reusable modeling-form obligations | exact Accepted Pattern invoked by the candidate contract |
| admission, rejection, reopening and status change | explicit Architecture Board act |
| finite consistency checks, if later authorized | derived checker implementation tied to an exact human-readable rule |

OCP-001 must point to the separate OCP rather than duplicate its routing table. The Core Boundary OCP must point back to OCP-001 for governance procedure rather than defining a second approval process. A candidate contract may satisfy the selected route but cannot declare itself admitted.

The human-readable artifacts are primary. AD-015B selects no admission registry, score, generated status field or mandatory checker projection. Any later projection needs a separately reviewed source mapping and must fail on mismatch with the human Board act; it can never be the source of approval.

The selected contract applies prospectively to new proposals and amendments that broaden shared semantics or authority. It does not silently reclassify accepted historical artifacts. A contradiction with an accepted decision requires an explicit reopening act.

## 37. Route movement, negative results and migration

A candidate may move between routes only through evidence and governance appropriate to the destination:

- implementation-local → domain-local requires a named domain owner and defining contract;
- domain-local → Core envelope requires a concrete interoperability consumer, exact profile/version contract and ambiguity rejection;
- domain-local or envelope → Core semantics requires evidence that Core owns the shared meaning rather than only transport;
- non-Concept → fundamental Concept requires the complete independent-identity test and a separate Board act;
- Core → domain-local, retired or deregistered requires an explicit Board act and atomic cleanup of every normative and generated projection.

Movement is forward from an exact reviewed baseline; it never rewrites the authority of historical versions. Existing exact references remain interpretable or receive an explicit governed migration. Equal payload, similar label, shared storage or copied shape does not merge identities or routes.

A negative Core verdict leaves valid domain or implementation work available in its legitimate route. Reopening requires new evidence that closes the prior gate. Newest timestamp, document order, issuer count, source count, deployment count, majority or checker status cannot select a route or authority.

## 38. Alternatives not selected and reopening gates

### 38.1 C0 and C1

C0 is not selected because accepted history demonstrates recurring review drift when the doctrine must be reconstructed case by case. It may be reconsidered only if the implementation shows that a reusable contract adds no stable guidance and materially worsens review quality.

C1 is not selected because a binary result cannot by itself distinguish valid domain-local contracts, Core envelopes, non-Concept Core contracts, local structured values and optional Pattern form. It may be reconsidered only with a complete routing explanation that preserves those distinctions outside the binary gate without restoring case-by-case ambiguity.

### 38.2 C2

C2 remains the nearest artifact-home alternative. It may be reconsidered if OCP-016 implementation proves that the OCP-001/OCP-016 ownership split necessarily duplicates normative rules, creates contradictory precedence or makes the human review materially harder. Lower artifact count alone is insufficient.

### 38.3 C4 and machine projection

C4 is not selected because external review found no integrity property that requires a mandatory registry/checker projection now. A later derived projection may be proposed only after a concrete synchronization or omission failure is demonstrated. It must name its exact human source and reject stale, missing, duplicate or contradictory state.

### 38.4 C5, H3 and H4

C5 is not selected because domain-first and consumer-activation doctrines alone do not route Concepts, dependencies, records, local values, Patterns and implementation structures.

H3 remains available only when a particular accepted candidate needs reusable form. H4 remains available only as a separately authorized derived projection. Neither can become the sole home of mandatory boundary governance.

## 39. Separate OCP implementation obligations

The next separately reviewed implementation cycle must amend OCP-001 and introduce the separate human-readable Core Boundary contract, provisionally OCP-016. At minimum it must:

1. define the automatic trigger for new or broadened Concept, dependency, record, rule, local-value, Pattern, envelope, domain-contract and machine-projection proposals;
2. define the five primary semantic-authority routes and the orthogonal Pattern form route in language usable without checker code;
3. distinguish Core semantics, Core envelope, domain-local meaning and implementation representation without overlap;
4. require one authority ledger, concrete consumers, exact dependencies and explicit non-implications for every positive proposal;
5. preserve G3 domain-first and G4 consumer-activation safeguards inside the selected routing model;
6. define fail-safe handling for missing owner, ambiguous route, unresolved version/profile, conflicting authority and prior-decision contradiction;
7. define reopening, route movement, historical-reference preservation and atomic migration behavior;
8. include human-readable examples covering all accepted precedent forms and all twenty-two §13 counterexamples;
9. state exactly which finite structural obligations, if any, existing checker facilities can validate without creating semantic or Board authority; and
10. update backlog, roadmap and governance references atomically.

The initial implementation must not add an admission registry, numeric score or P-002. It may use existing checker capabilities only for finite consistency against the human contract. If executable implementation would require new structured authority fields or a new projection, the cycle must stop and reopen C4/H4/H5 rather than add them silently.

No existing candidate is grandfathered into a new status by the OCP implementation. No Concept, dependency or candidate contract becomes Accepted merely because it appears as an example or passes a structural check.

## 40. Accepted effect

This Board act has the following narrow effects:

- AD-015 becomes `0.3.0 / Accepted`;
- C3 (`G2 × H2`) becomes the selected Core Boundary direction;
- exactly one primary semantic-authority route plus an optional Pattern form route becomes the selected routing shape;
- G3 domain-first and G4 consumer activation become conditional obligations inside G2, not independent universal models;
- human-readable OCP-001 plus a separate Core Boundary OCP become the selected ownership split;
- machine registry/checker projection remains unselected and non-authoritative;
- AB-061 moves `Discovery → Planned` for the separate OCP implementation; and
- no OCP, Pattern, schema, registry, checker rule, fixture, Concept status, dependency or graph edge is created or changed by this act.

Exact-head Fable approval, Codex adjudication, green CI and explicit Pavlo or Architecture Board authorization remain mandatory before squash merge. Until that merge, §§33–40 are a proposed Board act rather than an accepted decision.
