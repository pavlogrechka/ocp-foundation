---
Decision-ID: AD-030
Title: Order Authorization Establishment Boundary
Version: 0.1.0
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-004, OCP-005, OCP-006, OCP-008, OCP-016, OCP-017, OCP-018, P-001
Applies-To: AB-002
---

# AD-030 — Order Authorization Establishment Boundary

## 1. Mandate and decision

AB-002 is normatively registered by the OCP-000 `Order | Proposed | AB-002` row and asks whether Order is mandatory or one possible source of Operation authorization. OCP-018 `0.2.1 / Accepted` already supplies a general authorization-source contract without Order and explicitly leaves AB-002 separate.

The Board compares mandatory Order, optional/admissible Order, fundamental Order identity, domain-local ownership, no change and a governed negative non-Concept boundary. It selects **ON**, a Route C boundary implemented by OCP-022 `0.1.0 / Draft`. ON separately derives that mandatory, sufficient and admissible-source Order propositions are not established by current Core evidence. It does not assert that Order is absent in reality or prohibit a future separately governed profile.

Merge resolves AB-002 only at this negative establishment boundary. Order remains Proposed; no registry, taxonomy or graph change is authorized.

## 2. Exact baseline and anchor chain

The exact baseline is `main@68b5ac89a8a185ba8f4f1aa053d49d210438a1a5`, tree `ed627f76ffd7c22c8df1612e8dd57afbf9a1d7d3`. Each blob was resolved at that commit, reverse-resolved through `git ls-tree -r`, checked against the state inside the object and SHA-256 hashed from raw bytes.

| Artifact | Reverse-resolved path | Declared state | Git blob | SHA-256 |
|---|---|---|---|---|
| OCP-000 | `docs/000-operational-ontology/README.md` | `1.5.0 / Canonical`; Order Proposed | `7da7d7aad6ba505603cfbfa98ff1349c84892720` | `3f76ae4b55f01ce388bd865330f386c3ec0a6f6416e1aaed522145df96cfb7d6` |
| OCP-001 | `docs/001-ontology-governance/README.md` | `1.0.0 / Canonical` | `33524fa3d18f3253faa9a854500be7ddfb20815f` | `da74645aa4f3cae10c7c59ae7b87abd1840544700e4a58e9efd3f6600a27f1cc` |
| OCP-002 | `docs/002-concept-taxonomy/README.md` | `1.5.0 / Canonical`; no admitted Order projection | `aaa4ac27a7d77c52b74833a1c088c037538f1f06` | `335f3e8c2f51110f192ceb608188437b6d2fe5b908bbf12894c31e45a651e7c6` |
| OCP-004 | `docs/004-operation-concept/README.md` | `1.0.0 / Canonical`; Order possible, undefined | `1ff548a1f213b574472a90a8b3cfe014f6c1ce11` | `9c9173d3a3dec044e2cae2eb8fd5b66d07a106318f497a973409fedf4677155b` |
| OCP-005 | `docs/005-assignment-concept/README.md` | `0.2.7 / Draft`; Assignment Accepted | `7a82a051cfb572e31cceded52bdfbb8e917bffba` | `fbdbe9b4547f7b1f14c766e1925ff28d620c671a271cfc8721f8d6b8d4db7b5a` |
| OCP-006 | `docs/006-constraint-concept/README.md` | `0.3.1 / Draft`; Constraint Accepted | `95ef13a917e0f579cdd656672a6bd883060bb818` | `d1d2a8c4d85ffba3bbe22d38ed443946e8196558e42c67d929347436468632b6` |
| OCP-008 | `docs/008-objective-concept/README.md` | `1.0.0 / Canonical`; Objective is not Order | `24ed01e0f5d6bc8f349a7aedae4c5f100eb449ee` | `46f1ecb7b956b106f9c66da0626ec4266961e07492059e594110f63736be6f0d` |
| OCP-016 | `docs/016-core-boundary/README.md` | `1.0.0 / Canonical`; G4 current | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| OCP-017 | `docs/017-operation-lifecycle/README.md` | `0.2.0 / Accepted`; generic evidence consumer | `0b2ea683df308babd1111ff47e9272c9b0742f78` | `061e2c8a4c9d3d02bb5a7492e9c8723cace11a462548970727552e18c645a030` |
| OCP-018 | `docs/018-operation-authorization-source/README.md` | `0.2.1 / Accepted`; Order neither required nor excluded | `dc3148869f47af2bb27eb2fa74a188136d5fb568` | `e105e9c230277b6865721192ef4044ee77d9bfbff73505d164d7760c8ac31779` |
| P-001 | `patterns/P-001-identified-record-pattern.md` | `0.1.0 / Accepted`; binding only when invoked | `c679f3e35eb015aecf6cb9a839aacd75a432e844` | `2c9dd172a19c2d340b58a159fe5e71b64215a3968ee05fa330790b7e6359c797` |
| architecture backlog | `backlog/architecture-backlog.md` | AB-002 Open; AB-017 Resolved; AB-018/AB-005 Open | `21bc592f846348aea1d696a5083c07e673e611f2` | `68f6c4a78932b79c25a1e6bb39e4a373c878402bed1ac8a50f6e0964d32b9e7c` |

Anchors establish inputs only. They do not select a result or route.

## 3. Predeclared inventory criterion

Before classification, the inventory is fixed as all twenty-two current primary OCP documents plus P-001. An artifact is semantically included when its current primary text: (a) contains a structured Order or authorization-source field/result/rule; (b) directly asks, delegates or bounds Order; or (c) is an exact consumer/producer of OCP-018 authorization evidence. Registry, governance, routing and form owners enter as controls.

Historical baseline/rollback references, `order` meaning list/time/precedence, generic process language and topic overlap do not qualify. Explicit exclusions are classified by name rather than silently omitted.

## 4. Complete current-artifact inventory

| Artifact | Classification and reason |
|---|---|
| OCP-000 | control; sole current registry contains `Order | Proposed | AB-002` |
| OCP-001 | control; governance, ambiguity stop and exact-head authority only |
| OCP-002 | control; no admitted Order Concept projection exists |
| OCP-003 | excluded; Resource identity and evidence boundaries own no Order or authorization-source result |
| OCP-004 | included; names Order as a possible authorization source while deferring command/authorization models |
| OCP-005 | included boundary; Order may be opaque Assignment provenance, but provenance is not authority |
| OCP-006 | included boundary; Order may be provenance and is expressly non-mandatory |
| OCP-007 | included owner check; Organization participates in OCP-018 source attribution but supplies no Order-specific legitimacy |
| OCP-008 | included boundary; Objective is not Order and provenance grants no authorization |
| OCP-009 | included dependency check; Capability scopes OCP-018 evidence but does not authorize or make Order admissible |
| OCP-010 | excluded; Event occurrence/evidence owns no Order or authorization-source result |
| OCP-011 | excluded; assessment attribution and conclusions own no authorization result |
| OCP-012 | excluded; CapabilityClaim evidence is not authorization, admissibility or source legitimacy |
| OCP-013 | consumer check; Accepted interchangeability excludes authorization, selection and Assignment mutation |
| OCP-014 | consumer check; Accepted coordination requirement has its own non-authority boundary |
| OCP-015 | consumer check; workflow confirmation is not authorization, approval or Assignment mutation |
| OCP-016 | control; G4 is decided before form selection |
| OCP-017 | included Accepted consumer; needs generic accepted evidence but cannot issue Order or prove source legitimacy |
| OCP-018 | included defining source; Accepted generic profile/decision contract expressly leaves AB-002 separate |
| OCP-019 | excluded boundary; Conflict establishment does not consume or define Order authorization |
| OCP-020 | excluded boundary; quantitative input and aggregation confer no authorization and leave AB-002 untouched |
| OCP-021 | excluded boundary; reservation/allocation results confer no authorization and leave AB-002 open |
| P-001 | form control; no invocation without independently justified identified-record identity |

The inventory is authority-led, not term-frequency-led. Every primary artifact is named and evaluated under the predeclared criterion.

## 5. G4 first, before form

All positive Order outcomes are tested before a route or object form is selected.

| G4 element | Exact baseline result |
|---|---|
| concrete Accepted consumer | OCP-017 exists for generic authorization evidence, not an Order-specific protected decision |
| consumer baseline and protected need | OCP-017 `0.2.0` is exact; no current clause requires, accepts or evaluates Order as such |
| versioned positive rule | absent; OCP-018 rules govern generic source decisions and cannot be relabelled as Order rules |
| exact snapshot and evaluation context | generic OCP-018 bindings exist; no Order-specific activation binds them |
| legitimate owner/evaluator | absent; OCP-018 attribution does not elect a legitimate Order source owner or evaluator |
| object form | absent; no projection, identified record, fundamental Concept or admitted domain profile is selected |

The generic consumer and source contract therefore do not complete G4. Mandatory Order additionally contradicts OCP-018's accepted non-mandatory boundary. A caller-declared complete tuple remains self-supply.

## 6. Predeclared outcome criteria

| Criterion | Requirement |
|---|---|
| C1 — G4 honesty | positive capability cannot self-supply an Order-specific consumer, rule, owner/evaluator or form |
| C2 — OCP-018 continuity | preserve the Accepted source contract and its owner-local open questions byte-for-byte |
| C3 — registry discipline | keep Order Proposed; no `Concept-Status`, taxonomy projection or graph edge |
| C4 — responsibility fit | add only a shared invariant not already owned by provenance or generic authorization |
| C5 — fail-safe replay | missing, ambiguous, stale, cross-bound or non-definitive evidence returns `indeterminate` |
| C6 — outcome separation | mandatory, sufficient and admissible-source questions remain distinct |
| C7 — executable falsifiability | every finite field, value, rule and defensive-list member has individual evidence |
| C8 — safety | fixtures remain abstract and contain no real order language or issuer details |

No criterion rewards closing AB-002, prior wording, document centrality, fixture count or green CI.

## 7. Outcome-fair comparison

| Outcome | Intended benefit | Current evidence and gate result | Disposition |
|---|---|---|---|
| O0 — introduce nothing | preserves every current owner | leaves the recurring inference unexecutable despite a registered AB question | lawful, not selected |
| OM — Order mandatory beyond OCP-018 | simple universal prerequisite | contradicts OCP-018 §§3/12 and lacks Order-specific need, rule, owner/evaluator and form | rejected |
| OA — Order one admissible source | permits source diversity | compatible in principle, but lacks a named legitimate profile owner, Order rule, activation and object form | G4-blocked |
| OF — fundamental Order Concept | could support identity/history/relations | no independent identity evidence; requires separately authorized OCP-000/OCP-002/graph change | out of scope and rejected now |
| OD — governed domain-local Order profile | lets a domain own concrete meaning | no named domain owner, profile, consumer or evaluator exists on the baseline | lawful future route, not selectable now |
| **ON — Route C negative establishment boundary** | makes all three current non-results explicit and executable without positive authority | cannot answer a future admitted profile, by design | **selected** |

ON is not a hidden prohibition. It records only that current Core cannot derive mandatory, sufficient or admissible-source Order authority. OA or OD may reopen with new G4 evidence; OF requires a separate Concept act.

## 8. Three distinct selected questions

OCP-022 preserves three independent exact rules and results:

- M: `mandatory_order_not_established` prevents generic accepted authorization evidence from becoming an extra universal Order prerequisite;
- S: `sufficient_order_authorization_not_established` prevents an opaque Order candidate or provenance label from authorizing an Operation; and
- A: `admissible_order_source_not_established` prevents a generic OCP-018 source from being reclassified as an admitted Order profile.

No result transfers to another question. All invalid evidence derives `indeterminate`, not a positive or global-negative answer.

## 9. OCP-016 authority ledger

| Ledger field | Decision |
|---|---|
| Candidate | ON, three-question negative Order authorization establishment boundary |
| Operational responsibility | prevent current generic authorization/provenance evidence from manufacturing Order authority |
| Route | C, Core non-Concept |
| Semantic owner | OCP-022 for this composition boundary only |
| Consumers | Operation authorization review and audit; neither is a positive G4 activation consumer |
| Defining sources | OCP-004 §4, OCP-005 §6.4, OCP-006 §4, OCP-017 §9, OCP-018 §§3 and 12 |
| Exact dependencies | OCP-004, OCP-016, OCP-017 and OCP-018 |
| Evidence | one derivation, exact manifest, six focused tests and thirty-five synthetic fixtures |
| Non-implications | no Concept, P-001 record, source profile, permission, lifecycle effect, registry/taxonomy/graph change |
| Lifecycle/migration | new `0.1.0 / Draft`; zero migration |

Route F lacks identity evidence. Route E lacks a named shared profile/consumer pair. Route D is a possible future concrete source-profile route but lacks a current owner. Route I cannot own semantic truth. P-001 is not invoked because the request and snapshot are bounded evidence envelopes, not independently governed record families.

## 10. Selected Draft contract

OCP-022 evaluates one request against one exact current evidence snapshot bound to `OCP-018@0.2.1`, the subject Operation, source owner, input snapshot and evaluation context. `order_candidate_ref` remains opaque and grants no identity.

The checker recognizes only `accepted | denied` generic source results as definitive inquiry input. Either remains insufficient for every Order proposition. Unknown, malformed, stale, unresolved, ambiguous, mismatched, self-supplied or positively coupled input returns `indeterminate`.

## 11. Executable evidence and individual coverage

The tree adds one checker module, one complete-coverage manifest, dispatcher export, six focused unit tests and thirty-five fully synthetic fixtures. Three valid fixtures cover every question/result pair, both definitive source-result values, unreferenced-snapshot isolation and order independence. Thirty-two material negatives cover every validation class and provide one direct fixture for every defensive-list member.

Mutation tests remove in turn all three question values, all three rule mappings, all three result mappings, both source-result values, the exact OCP-018 reference, every required dataset field, every required request field, every required snapshot field and each of twenty-one members across five defensive sets. Each mutation makes a previously valid or previously rejected probe expose the removed obligation. The coverage claim is therefore individual, not categorical.

The suite grows from `240` to `246` tests and from `239` to `274` fixtures.

## 12. Backlog and neighbouring authority disposition

AB-002 becomes Resolved at ON. This means only that no current Core derivation establishes mandatory, sufficient or admissible-source Order authority. Order remains Proposed in OCP-000; reopening or deregistration requires its own act and cannot be inferred from `Resolved`.

AB-017 remains Resolved exactly as before. OCP-018 remains `0.2.1 / Accepted` and byte-unchanged, including its owner-local open questions. AB-018 and AB-005 remain Open. No Authority, Approval or Policy Concept is introduced.

## 13. Version, migration, rollback and safety

AD-030 is `0.1.0 / Accepted` because merge is the first Board comparison and selection for this bounded AB-002 resolution. OCP-022 is `0.1.0 / Draft`, the first pre-canonical contract surface; PATCH/MINOR does not apply and Accepted/Canonical would overstate absent positive profile evidence.

No Operation, decision, provenance, source profile or consumer migrates. No existing OCP, Pattern, registry, taxonomy, graph or foundation map changes. Rollback removes AD-030, OCP-022 and its executable evidence, restores AB-002 Open and reverses accounting atomically.

All fixtures use abstract `SYNTH` values only. They contain no real order wording, requisites, identifiers, numbers, issuer positions, organization/unit names, coordinates, geometry, frequencies, windows, personnel, credentials or material from another project.

## 14. Exact-head gates

Merge requires Fable external review on one exact head, Codex adjudication, green required CI on that same head and fresh explicit Pavlo authorization naming it. Draft preparation, review, CI and this proposed decision text do not authorize merge, production use or a next act.
