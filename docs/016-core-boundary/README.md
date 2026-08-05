---
Document-ID: OCP-016
Title: Core Boundary Admission and Extension Contract
Version: 0.2.0
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-000, AD-015
Used-By: All Core admission, extension, domain-envelope and semantic route reviews
Last-Review: 2026-08-05
Review-After: A concrete routed proposal falsifies route completeness or non-overlap, the H2 ownership split or the no-projection baseline
---

# OCP-016 — Core Boundary Admission and Extension Contract

## 1. Authority and incorporated contract body

Architecture Board accepts OCP-016 revision `0.2.0` as the human-readable Core Boundary routing contract selected by AD-015B C3 (`G2 × H2`) and the resolution of AB-061.

The complete externally reviewed Draft is preserved verbatim in [`reviewed-contract-v0.1.0.md`](reviewed-contract-v0.1.0.md). Sections 1–18 of that immutable artifact are incorporated into this Accepted specification without semantic alteration. Its frontmatter and §19 preserve the pre-acceptance Draft state and next-act wording as historical review evidence only; this README governs current lifecycle and acceptance.

The publication split changes no route, authority ledger, Pattern boundary, precedent mapping, counterexample, migration rule or executable boundary reviewed in PR #78.

## 2. Accepted routing baseline

Every semantic candidate receives exactly one primary semantic-authority route:

- **F — fundamental Core** for independently justified Concept identity or identity/invariant dependency;
- **C — Core non-Concept** for shared records, rules, consumer activations or local-value contracts without fundamental Concept identity;
- **E — Core interoperability envelope** for exact shared binding and ambiguity rejection over named domain-owned semantics;
- **D — governed domain-local** when a named domain owns meaning and no Core envelope or shared Core semantics are justified; or
- **I — implementation-local** for storage, API, UI, transport or computation structures that do not own shared meaning.

These are authority routes, not quality grades. `not Core` does not mean `invalid`. Route ambiguity is not resolved by default, precedence or score; the proposal remains Discovery until the semantic owner and scope are exact.

Core semantics, Core envelope, domain-local meaning and implementation representation remain non-overlapping. Reuse, label similarity, shared storage, newest version, document order, issuer/source/deployment count or majority never select a route.

## 3. Accepted Pattern form boundary

Pattern remains an orthogonal form verdict rather than a sixth semantic route.

A Route C, E or D candidate may exact-invoke an Accepted Pattern. Invocation imports only its reusable modeling-form obligations; every invoker retains its own identity, vocabulary, truth, rule, result and lifecycle authority.

A proposal for a new Pattern must show independent invoker contexts with their own semantic routes and prove that only form obligations are shared. Pattern-shaped similarity does not invoke a Pattern, and optional Pattern invocation cannot implement mandatory Core Boundary governance.

## 4. OCP-001 and OCP-016 ownership split

[OCP-001 § «Обов’язковий Core Boundary review»](../001-ontology-governance/README.md) is the single defining location for the automatic trigger and review choreography. It requires authors to identify candidate objects, apply the current exact OCP-016 contract, provide the ledger and complete external review plus an explicit Board act.

OCP-016 is the single defining location for semantic routing, authority questions, route movement, reopening and migration safeguards. It does not trigger its own application, judge evidence true or grant status.

Candidate contracts cannot approve themselves. Admission, rejection, reopening, retirement and status change remain explicit Architecture Board acts. This one-direction `OCP-001 → OCP-016` dependency avoids a circular normative definition while preserving the exact handoff.

## 5. Domain-first and consumer-activation safeguards

G3 domain-first behavior remains binding inside the accepted routes: specialized semantics stay Route D unless a concrete consumer proves a minimal Route E envelope or independently shared Route F/C responsibility. Route E exact-binds namespace, profile, version and owner and rejects zero, multiple, unknown or incomparable resolution without best-effort translation.

G4 consumer activation remains binding for positive-capable rules, results and profiles: each activation exact-binds one accepted consumer, baseline, rule version, input snapshot, evaluation context and legitimate owner/evaluator. One activation does not inherit globally, rewrite its baseline or transfer by matching labels.

## 6. Authority, evidence and fail-safe behavior

Every positive proposal must provide the reviewed human-readable authority ledger: candidate, operational responsibility, primary route, semantic owner, concrete consumers, defining source, exact dependencies, evidence, non-implications and lifecycle/migration effect.

Routing is not approval. Missing or conflicting owner, consumer, route, exact dependency, profile, rule, snapshot or accepted-reopening evidence is non-permissive. A prior negative verdict remains current until an explicit reopening act closes its evidence gate.

Route movement starts from an exact reviewed baseline and never rewrites historical authority. Registry, taxonomy, dependency, Pattern invocation and generated-projection changes remain atomic; temporary dual authority is forbidden.

OCP-016 grants no domain truth, Resource equality or interchangeability, Readiness, availability, suitability, admissibility, authorization, approval, selection, ranking, reservation, allocation, Assignment mutation, transitive possession, profile equivalence, production validation or actor authentication.

## 7. Executable conformance boundary

The accepted initial baseline contains no admission registry, numeric score, route field, schema, P-002, new checker rule or mandatory machine projection.

The existing checker validates only finite structural obligations already governed elsewhere: primary artifact identity/path, exact `Depends-On`, lifecycle values, Concept projections, Pattern version binding and rule-manifest source integrity. Its successful output is evidence of those checks, not semantic routing or Board approval.

If a later implementation requires structured authority fields or a mandatory projection, it must stop and reopen AD-015 C4/H4/H5. It may not add the layer as an editorial or implementation convenience.

Human external review remains authoritative for operational responsibility, legitimate ownership, consumer need, route non-overlap, semantic evidence and the twenty-two incorporated counterexamples. Foundation examples remain synthetic and non-sensitive.

## 8. External review evidence

Fable externally reviewed exact Draft head `ff09df68cad178d6e1f3ee7cf743f14bdf1bb9a9` in an isolated clone and approved it with zero findings at iteration 1 of 5. The review verified all ten AD-015B §39 obligations, route completeness and non-overlap, the one-direction dependency, Pattern form handling, ten precedent families, twenty-two counterexamples, thirteen review questions and the absence of a hidden machine layer.

Codex independently accepted the verdict and merge recommendation without changes. Pavlo explicitly authorized squash merge of the reviewed Draft. PR #78 was squash-merged as `971a5f95cd3689c91bfb415bfb169510113bf9bd`; its merged tree exactly matched the authorized head, and post-merge ontology-checker run `31016196536` succeeded.

## 9. Architecture Board decision

On 2026-08-05, Architecture Board:

1. accepts OCP-016 revision `0.2.0` as the binding human-readable Core Boundary routing contract;
2. accepts Routes F/C/E/D/I and the rule of exactly one primary route per semantic candidate;
3. accepts Pattern creation/invocation as an orthogonal form verdict without semantic transfer;
4. retains G3 domain-first and G4 consumer-activation safeguards inside the selected G2 model;
5. retains OCP-001 trigger/choreography authority, OCP-016 routing authority, candidate defining-source authority and external Board admission authority as separate responsibilities;
6. retains the no-projection baseline and the mandatory C4/H4/H5 stop-and-reopen rule;
7. resolves AB-061 for the accepted human-readable Core Boundary contract; and
8. creates or changes no Concept, Concept status, dependency, Pattern, schema, registry, checker rule, fixture or graph edge.

## 10. Accepted effect and future use

After acceptance, every proposal within the OCP-001 Core Boundary trigger applies the exact current OCP-016 contract before artifact selection or Board admission. Existing accepted artifacts are not silently reclassified or grandfathered into new authority.

AB-061 becomes `Resolved`. A future proposal may expose a route or trigger defect, but it must cite a concrete candidate and counterexample and proceed through explicit AD-015 reopening. Implementation preference or desire for machine scoring is not reopening evidence.

This acceptance takes effect only through squash merge after exact-head Fable review, Codex adjudication, green CI and explicit Pavlo or Architecture Board authorization. Until that merge, this README is an acceptance candidate and the reviewed `0.1.0 / Draft` remains current.
