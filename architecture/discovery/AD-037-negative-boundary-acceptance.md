---
Decision-ID: AD-037
Title: Negative Boundary Document Acceptance
Version: 0.1.0
Status: Accepted
Owner: Architecture Board
Depends-On: AD-022, AD-026, AD-029, AD-030, OCP-001, OCP-016, OCP-019, OCP-021, OCP-022
Applies-To: OCP-019, OCP-021, OCP-022
---

# AD-037 — Negative Boundary Document Acceptance

## 1. Decision, scope and gate-first result

Architecture Board accepts three already reviewed negative Route C contracts as one status-only lifecycle act:

- OCP-019 `0.1.0 / Draft → 0.2.0 / Accepted`;
- OCP-021 `0.1.0 / Draft → 0.2.0 / Accepted`; and
- OCP-022 `0.1.0 / Draft → 0.2.0 / Accepted`.

The acceptance form was selected only after applying OCP-016. Changing document status and accepted scope triggers Core Boundary review, but this act creates or expands no Concept, record, profile, positive-capable rule, result, activation or consumer. It preserves three already selected Route C negative boundaries. OCP-016 G4 therefore does not apply to the lifecycle evidence form; treating AD-037 or its snapshots as a positive consumer would be prohibited self-supply.

This act does not assume the three candidates are equally ready. §§4–6 apply the criterion declared in §2 to each independently. All three pass. The joint unit is authorized because the only shared change is the same lifecycle choreography, AD-029 snapshot-map expansion and derived accounting; it does not merge their semantics or let one candidate hide another's failure.

## 2. Predeclared Accepted-readiness criterion

The following test is fixed before application. A candidate may move from Draft to Accepted only if every item is true:

1. **Lifecycle meaning:** the Board is willing to approve the candidate's current semantics as a basis for dependent specifications. Accepted is pre-canonical and grants neither `1.x` stability nor production authority.
2. **Complete current contract:** every current result, request/evidence shape, fail-safe branch and non-implication needed by the candidate's claimed negative boundary is defined now.
3. **Executable evidence:** its rule manifest, checker behavior, focused tests and direct fixtures cover the declared finite surface, including every declared defensive value individually.
4. **Dependency admissibility:** every `Depends-On` token resolves to a current primary artifact. A Draft direct OCP dependency is permitted for Accepted but must be named as a future Canonical blocker; no Canonical-only L2 requirement may be silently imported into Accepted.
5. **Question disposition:** no unresolved question makes the current negative result incomplete. A separately gated future positive model is admissible only when the negative contract can fulfill its own present obligation without that future model.
6. **Acceptance evidence:** the exact reviewed Draft is preserved as one sibling `reviewed-contract-v<reviewed-version>.md`, linked by the current primary and bound in the AD-029 map by identity, status, version, path and SHA-256.
7. **No semantic delta:** the incorporated reviewed body and the domain manifest/module/tests/fixtures remain unchanged; only lifecycle authority, snapshot evidence and current repository projections move.

Canonical asks more. OCP-001 assigns Canonical documents a direct-OCP dependency floor L2, `1.x` version stability and a separate promotion act. Accepted means Board-approved current semantics for dependents without those guarantees. The repository already has Accepted OCP-011, OCP-013, OCP-014, OCP-015, OCP-017, OCP-018 and OCP-020 with direct Draft OCP-005 and/or OCP-006 dependencies. That live precedent confirms the normative distinction; it is evidence, not the source of the rule.

## 3. Dependency derivation from the exact tree

Every dependency is derived from current frontmatter and exact-resolved before readiness is evaluated.

| Candidate | Exact decision owner | Canonical OCP dependencies | Accepted OCP dependencies | Draft OCP dependencies | Accepted consequence |
|---|---|---|---|---|---|
| OCP-019 | AD-022 | OCP-001, OCP-016 | none | OCP-006 `0.3.2` | permitted; OCP-006 remains a Canonical blocker |
| OCP-021 | AD-026 | OCP-001, OCP-003, OCP-016 | OCP-020 `0.2.0` | OCP-005 `0.2.8`, OCP-006 `0.3.2` | permitted; both Draft inputs remain Canonical blockers |
| OCP-022 | AD-030 | OCP-001, OCP-004, OCP-016 | OCP-017 `0.2.0`, OCP-018 `0.2.1` | none | permitted; no pre-canonical direct OCP floor remains |

AD-022, AD-026 and AD-030 are Accepted. The candidates do not turn their upstream Drafts into Accepted artifacts, do not inherit Concept status from them and do not acquire Canonical stability by transitivity.

## 4. OCP-019 readiness

OCP-019 passes all seven criteria independently.

- Its current obligation is exactly the negative Conflict establishment boundary: complete exact OCP-006 evidence derives `conflict_not_established`; malformed, ambiguous, stale, cross-bound or indeterminate evidence derives `indeterminate`.
- OCP-006 violation never becomes Conflict, Risk, lifecycle change, Assignment cancellation or remediation by implication. No positive result is required for OCP-019 to fulfill that obligation.
- Twelve manifest rules, ten focused test methods and twenty-five direct fixtures remain unchanged. The complete-coverage manifest and mutation tests exercise the finite result and defensive surface.
- OCP-006 is Draft, which is admissible for Accepted and explicitly blocks a later Canonical claim. OCP-019 consumes only the current evaluation contract; it does not promise an immutable OCP-006 version.
- §9 is a future positive activation gate. AB-018 and AB-005 remaining Open does not make the present negative result incomplete.
- §10's AB-036/AB-037/AB-002 status values are exact Draft-baseline history; the current wrapper points to the live backlog while preserving every exclusion.
- The exact reviewed Draft digest is `8689327a770eecccd40a7d43dd147659c24eb2e1dc0cd117dfe3e75114676bec`.

The old §14 sentence that Accepted would overstate absent positive-consumer and production evidence is retained as historical pre-acceptance caution. It is not a current claim that a complete negative boundary cannot be Accepted. §§15–18 of the current primary time-bound only that lifecycle inference and preserve every semantic exclusion.

## 5. OCP-021 readiness

OCP-021 passes all seven criteria independently.

- Branch E and branch Q remain separate. Their four exact negative results and `indeterminate` are complete; neither branch establishes Reservation, Allocation, capacity, availability or permission.
- Seventeen manifest rules, six focused test methods and twenty-one direct fixtures remain unchanged. Individual mutation evidence covers every branch, action, rule, result, exact OCP-020 binding, required field and defensive value.
- OCP-005 and OCP-006 are Draft but admissible for Accepted. They remain explicit Canonical blockers and are not promoted by implication.
- Q exact-binds Accepted `OCP-020@0.2.0`; E prohibits quantitative coupling. No positive consumer, owner/evaluator or object form is needed to fulfill either current negative result.
- §11 is a future positive reopening gate, not an unresolved current branch. AB-025's negative resolution and future positive reopening remain unchanged.
- §14's OCP-019/AB-002/AB-036 status values are exact Draft-baseline history and are time-bound by the current wrapper rather than rewritten.
- The exact reviewed Draft digest is `85cdc7e3bb5281a6b2fe0af4d11b31bc47040b762de5786a0a8a10c2e000f683`.

The old §14 overstatement warning is preserved and time-bounded in the same way as OCP-019: accepting the negative boundary does not manufacture the missing positive evidence.

## 6. OCP-022 readiness

OCP-022 passes all seven criteria independently.

- `mandatory_order`, `sufficient_order` and `admissible_order_source` are three closed machine inquiries with exact rules and distinct negative results. They are not unresolved Open Questions.
- Seventeen manifest rules, six focused test methods and thirty-five direct fixtures remain unchanged. Every question, rule, result, source-result value, exact source-contract reference, required field and twenty-one defensive-list members has individual mutation evidence.
- All direct OCP dependencies are already Accepted or Canonical. OCP-022 preserves exact `OCP-018@0.2.1` and does not take over OCP-018 owner-local questions.
- §11 is a future positive reopening gate. Order remains Proposed, and no positive Order-specific consumer, profile, owner, evaluator or object form is required for the present negative results.
- The exact reviewed Draft digest is `8e2562153738d140510d21742b9c50ee8d37588ecbfe2a3221ae79f04268a60a`.

The old §14 warning is historical lifecycle caution. Accepted status approves the negative results only; it does not make Order mandatory, sufficient or admissible and does not establish production evidence.

## 7. Snapshot obligation and individual mutation evidence

AD-029 requires every current Accepted primary OCP to have exactly one mapped sibling reviewed snapshot. The shared map grows from nine to twelve entries: eleven `current-accepted` plus the retained OCP-016 historical acceptance evidence.

For all twelve entries, repository tests separately prove that each of the following fails: snapshot loss, filename/version mismatch, byte substitution, map-entry removal, primary-link removal and lifecycle drift. The three new primaries additionally prove that the current incorporated body starts with the exact reviewed body before the acceptance wrapper. The exact required test name `test_every_defensive_value_is_individually_fixture_and_mutation_live` removes every value of `ENTRY_KEYS` and `BASES` individually; zero defensive values may disappear silently.

This is governance evidence only. No new semantic fixture is added because acceptance changes no domain behavior.

## 8. Exact baseline and full anchor chain

The exact baseline is `main@24fff146bf1f44fc06cd7c9f0d1a2997383f4b2f`, tree `3ba05c5f9df090533546408982227c85470b55da`. Every row was resolved at that commit, reverse-resolved through `git ls-tree -r` to the stated path, checked against the declared state inside the object and SHA-256 hashed from raw bytes.

| Evidence | Reverse-resolved path | Declared state on exact base | Git blob | SHA-256 |
|---|---|---|---|---|
| OCP-019 | `docs/019-conflict-derivation-boundary/README.md` | `0.1.0 / Draft`; negative Conflict boundary | `092770b40541de5959c18b37664b179c7dcb7880` | `8689327a770eecccd40a7d43dd147659c24eb2e1dc0cd117dfe3e75114676bec` |
| OCP-021 | `docs/021-reservation-allocation-boundary/README.md` | `0.1.0 / Draft`; separate E/Q negative boundaries | `af96e2a9a67977cf5de8c4c566b1e9293e23687f` | `85cdc7e3bb5281a6b2fe0af4d11b31bc47040b762de5786a0a8a10c2e000f683` |
| OCP-022 | `docs/022-order-authorization-boundary/README.md` | `0.1.0 / Draft`; three Order negative inquiries | `27e5ed0abc8d06829436ca240b28070a1cd9afbc` | `8e2562153738d140510d21742b9c50ee8d37588ecbfe2a3221ae79f04268a60a` |
| AD-022 | `architecture/discovery/AD-022-conflict-derivation-boundary.md` | `0.1.0 / Accepted`; H0-B selected | `daba3472caaa650c41231437bddba1a70d895230` | `a52f0fb9cab2bdd32f23e5f2c529c4c76db1ffd8efe1ae6046fc3dda23747d54` |
| AD-026 | `architecture/discovery/AD-026-reservation-allocation-boundary.md` | `0.1.0 / Accepted`; EN/QN selected | `ad109d1003af32a019e6b525b4552db2c6e323b2` | `e258d714d242a5065b23c296a413a6d0d8c52e72d967b42798153888f6d872bd` |
| AD-030 | `architecture/discovery/AD-030-order-authorization-boundary.md` | `0.1.0 / Accepted`; ON selected | `01b7a6f01065b57130f8c0572242d683bcd22108` | `6ab90174bc1db423f403ac28a87d9eb0e1f84a7685cce881d94596a2fb9989bf` |
| OCP-001 | `docs/001-ontology-governance/README.md` | `1.0.0 / Canonical`; lifecycle and Canonical floor | `33524fa3d18f3253faa9a854500be7ddfb20815f` | `da74645aa4f3cae10c7c59ae7b87abd1840544700e4a58e9efd3f6600a27f1cc` |
| OCP-003 | `docs/003-resource-concept/README.md` | `1.0.0 / Canonical` | `71485bb337cfd59def2e0f1b18b474a7959bd30c` | `f8656769dd046f221843f627c746d0d6040c2e83c736b900370d60244fce8315` |
| OCP-004 | `docs/004-operation-concept/README.md` | `1.0.1 / Canonical` | `37fab136c578d2b8fafd6e900261ef64144943d9` | `ff0480913044b4dff8abcf69808b2d1cafe80a7d9f58c7ec06d2adeb33745538` |
| OCP-005 | `docs/005-assignment-concept/README.md` | `0.2.8 / Draft`; Assignment Accepted | `6e6c00e723b15a348e7610d4ca5a1ae23526c52b` | `a9226f4f5e168b945ae743626e73ba5e25d67318b390869a493e5fd30bdaa065` |
| OCP-006 | `docs/006-constraint-concept/README.md` | `0.3.2 / Draft`; Constraint Accepted | `50f149cf5563083bb84d5d2197ec32c2ed15fa9b` | `0472d8ce4b15a8c64d58151ee7f706b450b930f708f6f0a7a40bdd87914b3b10` |
| OCP-016 | `docs/016-core-boundary/README.md` | `1.0.0 / Canonical`; route and G4 boundary | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| OCP-017 | `docs/017-operation-lifecycle/README.md` | `0.2.0 / Accepted` | `0b2ea683df308babd1111ff47e9272c9b0742f78` | `061e2c8a4c9d3d02bb5a7492e9c8723cace11a462548970727552e18c645a030` |
| OCP-018 | `docs/018-operation-authorization-source/README.md` | `0.2.1 / Accepted` | `dc3148869f47af2bb27eb2fa74a188136d5fb568` | `e105e9c230277b6865721192ef4044ee77d9bfbff73505d164d7760c8ac31779` |
| OCP-020 | `docs/020-quantitative-constraint-input/README.md` | `0.2.0 / Accepted` | `0e1e7d0947ab3c7d1c0355258651179f618636a2` | `1783c32094aee9f09ca50ececb12bf9ec8f3c6599590331dba3894ad727d9b5c` |
| AD-029 | `architecture/discovery/AD-029-accepted-document-hygiene.md` | `0.1.0 / Accepted`; current-Accepted snapshot rule | `b33f218567c53bea06c10efdf93fa5bd78a29a1c` | `19e62307c98b6b6a62945b5a27c3be8a5e49914eabb94814667b330ca58160c8` |
| snapshot map | `architecture/accepted-document-snapshot-map.yaml` | schema 1; nine entries on base | `1918a4d400f475f5035622ee1571dec24cc4e435` | `5461ace22d4dc82622710b189a4cb11c82f2627bdaf0120ecad7c9204c8996ca` |
| Conflict module | `tools/ontology_checker/ocp_checker/conflict_derivation.py` | OCP-019 validation/derivation | `e1afc840b4523ca783d126742c03b1f98b113102` | `2a5edadc43c0e4a903e422f8de583f41a8765e73c43fedf4a5a9821d2d1c1bca` |
| Conflict manifest | `tools/ontology_checker/conflict-derivation-rules.yaml` | twelve rules, complete coverage | `640408c10844dd25416efe18ae6926f63292343c` | `44684a5bf48f9c1c79a0379da723179120cc3e867c8b1a1848a5087d5e4ef65d` |
| Conflict tests | `tools/ontology_checker/tests/test_conflict_derivation.py` | ten test methods | `fd5fc32ee28606de035205f63840a1a37d9e514a` | `236e4b27fbe9d4c16650edb31eb18cb30414accec7383d623259c52eb62a449e` |
| Reservation module | `tools/ontology_checker/ocp_checker/reservation_boundary.py` | OCP-021 E/Q validation/derivation | `29fd8b11d68f0d28d1f6d8314065cdaa1c4870c4` | `dd5277efbe014680659c08b5b54a54ae27cad6953522dc1656892fad1fb814e1` |
| Reservation manifest | `tools/ontology_checker/reservation-boundary-rules.yaml` | seventeen rules, complete coverage | `0a8b763de8d85e740071f15a0656785924bd004e` | `e4c1b9abb6a954d4d1fd442b839c126d546e0141cbcff772df8de00c52645279` |
| Reservation tests | `tools/ontology_checker/tests/test_reservation_boundary.py` | six test methods | `65c2497f6b50bb0e8306ffef904040db6f919ff4` | `3f977f0172acbdde7f0ef1757922d7c999dc006bc9c73381aa371418b682065e` |
| Order module | `tools/ontology_checker/ocp_checker/order_authorization_boundary.py` | OCP-022 validation/derivation | `792d9ac3da5f566ce8386f20565379d990d21a2e` | `0efb9e8d9e8f78c678cfecb458a691e79f41c8972994016c9ca3281d9fcba56e` |
| Order manifest | `tools/ontology_checker/order-authorization-boundary-rules.yaml` | seventeen rules, complete coverage | `4f0daf21368863ba784d32e2942f1bc9c0ddf0da` | `7a9ffb3d0f0d632077ad8e67eece85f0faa3dd549b74fd6aea2cacb341c94086` |
| Order tests | `tools/ontology_checker/tests/test_order_authorization_boundary.py` | six test methods | `b2e62349adde79c59d66539fd81b1b611b1c4060` | `91ccde52b424bbfd56707ee91ac7b9c45a6cb70f843637bbccc29d45185be98f` |

Every stated path equals the reverse resolution. Duplicate-content paths, where present elsewhere in the tree, do not substitute for the declared primary path.

## 9. Version classification, migration and rollback

Each OCP is classified independently as `0.2.0 / Accepted`. The `0.1.0 → 0.2.0` MINOR transition records substantive pre-canonical lifecycle authority while retaining the complete compatible semantic body. PATCH would understate the status change. `1.0.0` would overstate Canonical stability. No candidate borrows another candidate's version justification.

AD-037 is `0.1.0 / Accepted`: it is the first Board act that applies the readiness criterion and selects these three status changes. The snapshot map stays schema 1 because only its complete entry set grows; its validation meaning is unchanged. README, roadmap, backlog descriptions and checker documentation are status/accounting projections, not new semantic owners. The AD-035 live consumer projection reclassifies OCP-021 from Draft to Accepted. The AD-036 live scope grows to twenty-two lifecycle artifacts, thirty-one Accepted governance acts and thirteen candidate mentions by admitting OCP-019/OCP-021/OCP-022 plus AD-037 and rechecking their future-positive tokens; its result remains `no_unmet_positive_consumer_need_declared`, and all immutable `baseline_evidence_objects` remain untouched.

In each discovery witness, `baseline` and `baseline_evidence_objects` are historical coordinates of the original measurement, while scope and candidate lists are current projections synchronized by every act that changes artifact lifecycle status.

No domain data, reference, schema, positive result, production profile, module, manifest, focused domain test or fixture migrates. The only migration is document lifecycle plus three required immutable snapshots and their map/accounting entries.

Rollback is atomic for this one reviewed unit: a separately reviewed act restores all three primaries to `0.1.0 / Draft`, removes the three current-Accepted map entries, restores current accounting/status prose and adjudicates retention of the immutable snapshots without rewriting them. Rollback cannot activate any positive model or reopen/rescind the earlier negative AB resolutions by implication.

## 10. Accounting, boundaries and safety

The resulting current distribution is twenty-three primary OCP documents: ten Canonical, eleven Accepted and two Draft. Governed reviewed snapshots become twelve: eleven current Accepted plus one retained historical. The unit-test total grows only through snapshot-governance proof; fixtures remain 274 and are unchanged.

OCP-005 remains `0.2.8 / Draft`, OCP-006 remains `0.3.2 / Draft`; Assignment and Constraint Concepts remain Accepted. The Concept distribution stays six Canonical and two Accepted. OCP-000, OCP-002, the Concept graph, foundation map, P-001, every `Concept-Status`, promotion-gate state, historical `baseline_*`, existing reviewed snapshots and every AB status remain unchanged.

AB-018 and AB-005 remain Open. Order remains Proposed. No Conflict, Reservation, Allocation, Capacity, Order, Authority, Approval or Policy Concept is created. No positive model, profile, consumer, owner/evaluator or production authority is activated. No candidate is selected, no promotion cycle begins and no next act is authorized.

The three new snapshots contain only the already reviewed synthetic/abstract contract prose. The act adds no operational data, coordinates, geometry, time windows, unit or issuer identifiers, personal data, credentials, keys, tokens or material copied from another project.

## 11. Exact-head gates

This proposed decision becomes effective only after Fable external review of one exact unchanged head, Codex adjudication, green required CI on that same head, fresh explicit Pavlo authorization naming it and squash merge. Until then the three Accepted frontmatter values and this decision are proposed repository state only. No gate transfers from the Draft-creation acts or any earlier PR.
