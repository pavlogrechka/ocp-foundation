---
Document-ID: OCP-016
Title: Core Boundary Admission and Extension Contract
Version: 1.0.0
Status: Canonical
Owner: Architecture Board
Depends-On: OCP-000, AD-015
Used-By: All Core admission, extension, domain-envelope and semantic route reviews
Last-Review: 2026-08-05
Review-After: A concrete routed proposal falsifies route completeness or non-overlap, the H2 ownership split or the no-projection baseline
---

# OCP-016 — Core Boundary Admission and Extension Contract

## 1. Authority and incorporated contract body

Architecture Board accepted OCP-016 revision `0.2.0` as the human-readable Core Boundary routing contract selected by AD-015B C3 (`G2 × H2`) and the resolution of AB-061.

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

PR #79 satisfied that Accepted-state gate. The preceding sentence remains historical process evidence and does not make the current T1 lifecycle conditional.

## 11. Canonical baseline and exact content anchors

T1 promotes the current Accepted routing contract without changing its semantic result.

The exact pre-T1 Accepted wrapper is preserved by Git history at `main@f51da17b54eae67e1e29978488813c7165ea95df`:

- Git blob: `66dab8ef737b0d1d7c7dc895980120046540de54`;
- SHA-256: `a00117db5278f3468728e5f74a3053fef500068fa879aec27be3b4e4e37fc1c9`.

The immutable full reviewed Draft remains [`reviewed-contract-v0.1.0.md`](reviewed-contract-v0.1.0.md):

- Git blob: `3196f09f4a0b99160b42d1d1d27cc5a8387aae27`;
- SHA-256: `111e676ac750a2bfbe17d34fb1e8d2984af860fd38c856b824b4aff8c261c155`.

Sections 1–10 above retain the Accepted wrapper semantics. Sections 1–18 of the immutable reviewed artifact remain incorporated exactly as stated in §1. Historical Draft/Accepted frontmatter and next-act wording record their original lifecycle state; they cannot override this README's current Canonical frontmatter or §§11–15.

Content hashes are evidence of the reviewed inputs, not semantic authority or a newest-version selector. Git history, exact links and the human-readable incorporation rule establish which body is current.

## 12. Compatibility surface for `1.x`

OCP-016 `1.x` preserves these guarantees:

1. every semantic candidate receives exactly one primary route from the closed set F/C/E/D/I;
2. the primary routes remain non-overlapping authority locations rather than quality grades;
3. Pattern remains an orthogonal, exact-versioned form verdict and never a sixth semantic route;
4. OCP-001 owns the mandatory trigger/choreography, OCP-016 owns routing, each candidate contract owns its semantics and Architecture Board owns admission/status;
5. Route D remains valid governed work and `not Core ≠ invalid`;
6. G3 domain-first and G4 consumer-activation safeguards remain mandatory inside the applicable routes;
7. every positive proposal supplies a human-readable authority ledger, exact dependencies, concrete consumers, evidence and non-implications;
8. routing never proves evidence, invents an owner, grants status or approves the candidate;
9. missing, conflicting, ambiguous or unresolved authority/reference evidence remains non-permissive;
10. route movement and migration preserve historical authority and update normative/generated projections atomically;
11. the no-projection baseline remains in force until an explicit AD-015 C4/H4/H5 reopening; and
12. the explicit non-implications in §6 and incorporated §17 remain binding.

After `1.0.0`, SemVer applies at this routing-contract boundary:

- PATCH may correct prose, links, review evidence or examples without changing a route, ledger obligation, authority owner, fail-safe result or non-implication;
- MINOR may add a compatible example, precedent, counterexample or clarification that leaves every existing route/result interpretable and every previously conforming ledger conforming; and
- MAJOR is required to add/remove/rename/redefine a primary route, make Pattern a semantic route, change the OCP-001/OCP-016/Board ownership split, add an obligation that invalidates a previously conforming ledger, weaken non-permissive behavior, transfer domain meaning into an envelope, remove a non-implication or authorize a machine projection as admission authority.

A routed candidate, Board act or downstream OCP exact-binds the current OCP-016 version it claims to apply. OCP-016 document version is not the version of any candidate, route result, domain profile or Pattern.

## 13. Canonical OCP-000 dependency and OCP-001 handoff

OCP-016 consumes OCP-000 only as the Canonical registry owner established by T0. A row provides current membership and status; it does not preselect a route:

- `Proposed` does not imply Route F, future admission or semantic ownership;
- `Accepted` or `Canonical` does not prove that every extension belongs to Route F/C/E;
- a deregistered negative candidate remains governed by its exact decision/reopening gate; and
- row order, status recency or registry presence cannot replace the OCP-016 ledger and Board act.

The OCP-001 link remains a one-direction handoff rather than a reverse dependency. OCP-001 depends on OCP-016 and invokes this routing contract after its trigger. OCP-016 does not consume OCP-001 semantics to define F/C/E/D/I, does not trigger itself and does not copy OCP-001 choreography. This preserves L2 without creating an OCP-001 ↔ OCP-016 cycle.

Accepted AD-015 remains the decision dependency for C3 and its reopening gates. AD artifacts have their own lifecycle and require no invented Canonical status.

## 14. Canonical evidence and machine boundary

The current checker can witness OCP-016 identity/path, `1.0.0 / Canonical` version-lifecycle consistency, exact dependency resolution and source-bound structural governance. It cannot decide route fit, legitimate ownership, consumer need, evidence truth, route movement or Board approval.

T1 adds no route field, authority schema, admission registry, score, Pattern, P-002, checker routing rule or fixture. The content-anchor hashes are independently reproducible but do not become a machine admission layer.

Any future proposal for structured route projection must still stop and reopen AD-015 C4/H4/H5. Passing the lifecycle/version checker is necessary structural evidence, never proof that this or another contract deserved Canonical status.

## 15. T1 canonicalization act

T1 establishes OCP-016 `1.0.0 / Canonical` as the stable Core Boundary routing contract.

This act:

- preserves Routes F/C/E/D/I without addition, removal, renaming or changed precedence;
- preserves Pattern as an orthogonal form verdict;
- preserves G3/G4 safeguards, authority ledger, fail-safe routing, migration and non-implications;
- exact-consumes Canonical OCP-000 without importing Concept row status into route selection;
- preserves the OCP-001 trigger / OCP-016 routing / candidate semantics / Board approval ownership split;
- changes no Concept, Concept status, Pattern, dependency, registry row, graph edge, schema, checker behavior or fixture; and
- does not authorize T2 OCP-001 or any downstream promotion.

Canonical status takes effect only after exact-head Fable approval, Codex adjudication, green CI, a new explicit Pavlo/Architecture Board authorization specifically for T1 and squash merge. T0 authorization cannot be reused. Until that merge, this section and frontmatter are a proposed T1 act.
