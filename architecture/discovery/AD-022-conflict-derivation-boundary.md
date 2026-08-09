---
Decision-ID: AD-022
Title: Conflict Derivation Boundary
Version: 0.1.0
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-001, OCP-006, OCP-011, OCP-013, OCP-015, OCP-016
Applies-To: AB-038
---

# AD-022 — Conflict Derivation Boundary

## 1. Mandate and decision form

AB-038 asks when one or more Constraint violations create a stored or derived Conflict. This act derives the available result space, fixes outcome-fair criteria before applying them, selects one result and prepares OCP-019 `0.1.0 / Draft` with executable evidence in the same atomic tree.

The act is semantic rather than a mandate for later discovery: it fixes the current answer that no positive Conflict derivation is legitimate without the OCP-016 G4 consumer/owner bindings, and it makes that negative boundary executable. Merge fixes the Board selection; Draft preparation, review and CI do not.

## 2. Exact baseline and anchor chain

The act starts from exact `main@f3e95e79ba0427f6cdf3556566e4baf6b407f03a`, tree `71f993adbc6fe7248d40c7055d7105807ed26812`.

For every row, the blob was resolved at that commit, reverse-resolved through `git ls-tree -r` to the listed path, its stated state was checked inside the blob and SHA-256 was recomputed from raw blob bytes.

| Input | Reverse-resolved path | Stated state | Git blob | SHA-256 |
|---|---|---|---|---|
| OCP-001 | `docs/001-ontology-governance/README.md` | `1.0.0 / Canonical` | `33524fa3d18f3253faa9a854500be7ddfb20815f` | `da74645aa4f3cae10c7c59ae7b87abd1840544700e4a58e9efd3f6600a27f1cc` |
| OCP-006 | `docs/006-constraint-concept/README.md` | `0.2.5 / Draft`; Constraint `Accepted` | `5d7404717e500c66c0c017263678ae0a1a405c7d` | `e0469604b1d8e6c2156c35e85017129eaca1fb929633a8be0287af4ef67a88aa` |
| OCP-011 | `docs/011-outcome-assessment-record/README.md` | `0.2.0 / Accepted`; non-Concept assessment record | `ff2608a372c6305db4c290f05c15e961ca96e6f6` | `1fb08e18fab560e671b468585d699a7d70bd55ed5be674315cb780a48bc70cc5` |
| OCP-013 | `docs/013-resource-interchangeability/README.md` | `0.2.0 / Accepted`; bounded aggregation precedent | `658a291b4c3b9a0229aba09d485c1137723fe70b` | `a20659422f847f49a9231b8c1d1dabc0d8b911d9667c44013280b1826f621a74` |
| OCP-015 | `docs/015-coordination-workflow/README.md` | `0.2.0 / Accepted`; disagreement is evidence, not Conflict | `ea60634e54faedabb8c5e08b036030c2f0e4e20b` | `6077136b2460cfc56d0e06af9137338cb494ac9a8e14df036e662d9240415b1d` |
| OCP-016 | `docs/016-core-boundary/README.md` | `1.0.0 / Canonical`; exact routes and G4 | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| OCP-000 | `docs/000-operational-ontology/README.md` | `Conflict` absent from the Concept registry | `7da7d7aad6ba505603cfbfa98ff1349c84892720` | `3f76ae4b55f01ce388bd865330f386c3ec0a6f6416e1aaed522145df96cfb7d6` |
| OCP-002 | `docs/002-concept-taxonomy/README.md` | `Conflict` absent from taxonomy projection | `aaa4ac27a7d77c52b74833a1c088c037538f1f06` | `335f3e8c2f51110f192ceb608188437b6d2fe5b908bbf12894c31e45a651e7c6` |
| AD-016 | `architecture/discovery/AD-016-foundation-canonicalization-readiness.md` | `0.27.1 / Accepted`; four registered carrier-counter debts | `c2236f78078884bbd2154ed90fc1d3d3daa30f45` | `b98d5df5f9f63d1a42063efbb0843f1a7f9d78a7b41d6b67453f63c6298a6cd3` |
| OCP-018 | `docs/018-operation-authorization-source/README.md` | `0.2.0 / Accepted`; debt registry and manual 12/12 coverage | `43cc40e673abf26f8576242b716867b706a95da2` | `730a333ddd1bdbdf5069c3f85a6cf4c5e460525a791e900930d4bb93ddea93dc` |
| P-001 | `patterns/P-001-identified-record-pattern.md` | `0.1.0 / Accepted`; unchanged input | `c679f3e35eb015aecf6cb9a839aacd75a432e844` | `2c9dd172a19c2d340b58a159fe5e71b64215a3968ee05fa330790b7e6359c797` |
| architecture backlog | `backlog/architecture-backlog.md` | AB-005, AB-018, AB-036, AB-037 and AB-038 `Open` | `ed6d7a3e8768d68e57092fe037d99f7f5257bb2e` | `9b60c1d62345614ef6e6fb4112353f0f3704073d7805394603b51022da2c290a` |
| Constraint checker | `tools/ontology_checker/ocp_checker/checker.py` | executable OCP-006 evaluation precedent | `120ada9dd00b1df0b46cf3060aef2b0c290948b1` | `3a093f0d76113bb5dd2799c7d0aaf73b51b752569dc13de145bb3d158a7b4a47` |

Anchors establish inputs only; they do not select an outcome.

## 3. Already-fixed semantic boundary

OCP-006 §11 fixes four local evaluation results and an attributable `ConstraintEvaluationRecord`. Section 12 derives admissibility without authorization. Section 13 fixes five non-implications and requires later aggregation to preserve evaluation-record references.

The act cannot weaken those rules. In particular, one violation and many violations have identical absence of automatic Conflict authority. `constraint_set_decision = inadmissible` is not a substitute positive rule.

## 4. Predeclared comparison criteria

| Criterion | Outcome-fair test |
|---|---|
| C1 — accepted-boundary preservation | preserves every OCP-006 §13 non-implication and exact record references |
| C2 — consumer/owner legitimacy | satisfies OCP-016 G4 without self-supplied authority |
| C3 — object-class honesty | distinguishes projection, record and fundamental Concept rather than naming by intuition |
| C4 — exact evidence and replay | exact rule, context, snapshot and attributable evaluation references; no count/newest/order authority |
| C5 — fail-safe behavior | incomplete, conflicting, stale and indeterminate input cannot permissively derive Conflict |
| C6 — route and ownership | chooses one acyclic OCP-016 route with a legitimate semantic owner |
| C7 — executable falsifiability | finite obligations have direct manifest, tests and positive/material-negative fixtures |
| C8 — migration restraint | no invented production data, rebinding, registry/graph change or implicit backlog resolution |

No criterion rewards prior recommendation, file centrality, closing AB-038, fixture count or green CI.

## 5. Outcome space

### H0-B — negative Conflict-establishment boundary

Add a Route C non-Concept contract that preserves exact evaluation references and returns only `conflict_not_established | indeterminate`. It gives no positive Conflict authority but turns the current boundary into falsifiable shared semantics.

### HP — positive derived projection

Define a deterministic Route C projection from exact evaluations to `conflict | no_conflict | indeterminate` without durable identity. This is the smallest plausible positive model once a concrete Accepted consumer and criterion owner exist.

### HR — independently identified Conflict record

Persist an attributable Route C record and invoke P-001. This supports history and replay when a concrete consumer needs an independently addressable fact, but current evidence establishes neither that consumer nor record identity.

### HD — domain-owned positive profile

Keep rule meaning in Route D and let each domain define exact positive criteria while Foundation preserves only the evaluation-reference envelope. This can be legitimate for a future domain consumer, but no such governed profile or shared consumer exists now.

### HF — fundamental Conflict Concept

Add a Route F identity and graph edges. This could be appropriate if Conflict becomes a reusable subject of lifecycle and relations, but Conflict is absent from OCP-000/OCP-002 and AB-018 has not established that identity.

### HI — implementation-only detector

Implement a checker convention without a normative artifact. It could demonstrate code behavior but would place semantic authority in tooling and fail OCP-016.

## 6. Outcome-fair application

| Outcome | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| H0-B | exact | no positive activation needed | honest non-record boundary | exact refs | complete | Route C | complete now | minimal | **selected** |
| HP | possible | fails: no Accepted consumer/criterion owner | projection plausible | designable | designable | Route C | possible | restrained | leading future hypothesis, inadmissible now |
| HR | possible | fails | record identity unproved | strongest history | designable | Route C + P-001 | possible | premature storage | not selected |
| HD | possible | no actual domain profile | domain-local | profile-dependent | profile-dependent | Route D | no shared witness now | restrained | admissible future family, not current result |
| HF | would change boundary | fails | identity unproved | unknown | unknown | separate Route F act | unavailable in scope | highest | recommendation only if future evidence requires identity |
| HI | may preserve runtime behavior | hidden owner | wrong class | code-local | testable | fails Route I | executable | low | inadmissible |

Evidence distinguishes H0-B because every positive option lacks a concrete Accepted consumer and legitimate criterion owner. “Not enough evidence for positive authority” is the substantive result, not a delay.

## 7. Board selection

The selected outcome is **H0-B — Route C negative Conflict-establishment boundary**. OCP-019 `0.1.0 / Draft` fixes the result vocabulary, exact evidence obligations and fail-safe derivation.

The selection does not assert that Conflict is absent, define a positive Conflict criterion, or prevent a later positive comparison after G4 inputs exist. Any attempt to add a positive fixture, a `conflict` result, a Conflict record or Concept before that separate act returns this decision to H0-B.

## 8. OCP-016 authority ledger

| Ledger question | Selected answer |
|---|---|
| Responsibility | govern when existing evaluation evidence does not establish authoritative Conflict |
| Primary route | C: shared non-Concept rule/result boundary |
| Semantic owner | OCP-019 owns only its two-result boundary |
| Consumer | conflict derivation review and audit; neither is a positive Accepted activation consumer |
| Defining source | OCP-019 `0.1.0 / Draft` |
| Dependencies | OCP-006 evaluations and OCP-016 routing/G4 |
| Evidence | exact rules, checker, unit tests and synthetic fixtures |
| Non-implications | no Concept/record/P-001, Risk, lifecycle, Assignment, remediation, precedence, quantity or authorization |

Route F fails for absent fundamental identity; Route E fails because this is not an interoperability envelope; Route D-only fails because the negative OCP-006 boundary is shared; Route I fails because the result is semantic. A separate OCP avoids changing Draft OCP-006 while giving the bounded responsibility one owner.

## 9. AB-018, AB-005, AB-036 and AB-037

AB-018 remains Open. This act supplies evidence for its lower boundary but does not select a fundamental Conflict Concept or resolve the boundary between a future aggregated finding and such a Concept.

AB-005 remains Open. Risk is neither an output nor an implication, and no taxonomy is selected. AB-036 and AB-037 remain Open and outside scope: no precedence/override/waiver or quantity/capacity semantics enter any result. `Policy` is not introduced as a Concept.

AB-038 is resolved only to the current evidence: H0-B is the selected derivation model and names the exact reopening gate for a positive model. Resolution does not transfer to AB-018 or AB-005.

## 10. Executable evidence and manifest-fixture closure

The tree adds a dedicated manifest, checker module, central dispatch, focused unit tests and fifteen fully synthetic fixtures. Four valid fixtures cover one violation, several violations, definitive mixed results and an indeterminate evaluation. Eleven material negatives directly cover malformed envelopes/evaluations, duplicate or unresolved references, contradictory results, cross-bound evidence, stale evidence, stored-result mismatch, prohibited positive authority and forbidden coupling.

The suite grows beyond the `201` tests and `141` fixtures on the base. A generic test enforces exact direct fixture coverage for manifests that declare `fixture_coverage.status: complete`; OCP-018 and OCP-019 opt in. This closes the known OCP-018 `12/12` manifest-to-fixture gap without falsely claiming that all legacy manifests have complete direct coverage.

## 11. Carrier-counter debt resolution

AD-016 §23, both current-facing statements in §218 and §234 are repaired by binding their original six-invoker evidence to exact historical baselines. No `six` is replaced by `nine`; the facts remain true for their own acts. AD-016 changes `0.27.1 → 0.27.2 / Accepted`, a PATCH because only historical temporal scope changes.

OCP-018 §25 now names all four statements explicitly and records their resolution without the ambiguous “the latter two”. Its `0.2.0 → 0.2.1 / Accepted` change is a PATCH: semantics, status, dependencies, source-profile contract and executable authorization behavior are unchanged; only its current debt registry is clarified. The technical expectation that `0.2.0` remain unchanged cannot coexist with the owner-mandated edit inside OCP-018, so the governing SemVer rule wins visibly rather than hiding a byte change.

## 12. Version, accounting, migration and rollback

AD-022 is `0.1.0 / Accepted` because merge would be the first Architecture Board comparison and selection for AB-038. OCP-019 is `0.1.0 / Draft` because it is a new bounded contract with no production consumer or acceptance evidence.

No Concept count, Concept status, registry, taxonomy, graph, foundation map, P-001 byte, existing `Review-After`, production profile or T6 surface changes. AB-002, AB-005, AB-018, AB-036 and AB-037 remain Open. There is no record migration.

Rollback removes AD-022/OCP-019 and executable evidence, restores AB-038 Open and reverts the two PATCH clarifications atomically. It does not rewrite OCP-006 history or create a positive Conflict authority. Partial rollback would leave executable and documentary authority divergent.

## 13. Safety and exact-head gates

All evidence is synthetic and abstract. No real geometry, corridors, sectors, windows, callsigns, unit details, personal data, credentials or structures copied from another project are present.

The selection requires one unchanged head: exact-head Fable review, Codex adjudication, green required CI and fresh explicit Pavlo authorization naming that head. Any head change resets all gates. This mandate supplies only preparation authority and cannot authorize merge or any later positive, acceptance, Concept, Review-After, Y10D, YR or T6 act.
