---
Decision-ID: AD-042
Title: Route D Resource Occupancy Acceptance
Version: 0.1.0
Status: Accepted
Owner: Architecture Board
Depends-On: AD-029, AD-036, AD-040, AD-041, OCP-001, OCP-005, OCP-016, OCP-023
Applies-To: OCP-023
Review-After: A separately mandated activation names the exact completeness producer, baseline, protected rule, production snapshot/context and legitimate domain owner/evaluator
---

# AD-042 — Route D Resource Occupancy Acceptance

## 1. Decision and exact boundary

Architecture Board accepts OCP-023 `0.2.0` in the exact partial form reviewed as `0.1.0 / Draft`: one Route D statement derives `occupied=true` from one or more effective Assignments and retains every effective Assignment reference; `occupied=false` requires an exact complete Resource-wide Assignment snapshot; absent completeness remains indeterminate.

This act changes document lifecycle only. It does not activate a positive Core or domain rule, authenticate completeness evidence, name a production evaluator, change OCP-005, remove an Assignment blocker, introduce a Concept or start a promotion cycle.

## 2. Gate-first before acceptance form

The proposed form is lifecycle acceptance of an already reviewed Route D document. It is not a positive-capable rule, result or profile activation, so OCP-016 G4 does not apply to this act itself.

That conclusion does not exempt OCP-023 from G4. `occupied=true` remains positive-capable. A later production activation must exact-bind one Accepted consumer, baseline, protected need, rule version, input snapshot, evaluation context and legitimate owner/evaluator. This act supplies only the Accepted-consumer status element. It supplies no activation, completeness source or domain evaluation authority.

## 3. Predeclared readiness criterion

The criterion was declared before applying it:

1. the Board explicitly accepts the exact reviewed semantic body;
2. the current bounded contract is coherent and all declared behavior is executable;
3. direct dependencies resolve, and any applicable lifecycle floor passes;
4. no unresolved issue makes the current contract ambiguous now; explicit fail-safe partiality is admissible only when named as such; and
5. the acceptance act preserves semantic bytes, creates the AD-029 snapshot evidence and changes no activation authority.

`Canonical` requirements are deliberately excluded. OCP-001 defines Accepted as approval of current semantics for dependent specifications and applies direct-OCP dependency floor L2 only to Canonical OCPs.

## 4. Criterion applied independently

| Criterion | Live evidence | Result |
|---|---|---|
| Board decision | the mandate explicitly selects `OCP-023` `Draft → Accepted` in its reviewed partial form | pass |
| bounded contract | §§2 and 5–9 define one result, exact witnesses, fail-safe invalid behavior and explicit non-implications | pass |
| executable evidence | unchanged module, manifest, ten focused tests and six synthetic fixtures cover true, false-with-completeness, indeterminate-without-completeness, boundaries and defensive values | pass |
| dependencies | AD-041 is Accepted; OCP-001/OCP-003/OCP-016 are Canonical; OCP-005 is Draft but resolves exactly | pass for Accepted |
| current completeness | `false` is intentionally unavailable without completeness; this is the declared accepted boundary, not a missing text decision | pass |
| snapshot duty | the exact reviewed `0.1.0 / Draft` is registered and byte-identical | pass |

OCP-005 remaining Draft does not block this acceptance. OCP-001 L2 constrains Canonical OCPs, while current Accepted OCP-013, OCP-015, OCP-017, OCP-020 and OCP-021 already depend directly on OCP-005. OCP-023 makes no `1.x` stability claim and any later Canonical proposal must re-evaluate L2 independently.

## 5. Partiality is the accepted contract

The reviewed body says both what is derivable and what is not. One effective Assignment is sufficient to witness `occupied=true`. An empty caller-supplied list is not sufficient to witness `occupied=false`, because an omitted effective Assignment would reverse the result. Therefore a missing, non-synthetic or otherwise unacceptable completeness binding yields `occupied=None` in the reference proof.

Acceptance does not weaken, remove or disguise that boundary. It approves it as the current domain contract and preserves the direct unmet input token:

`assignment_set_complete_for_resource(resource_ref, evaluation_time, snapshot_ref)`.

The contract remains deliberately incomplete with respect to that external input. This is not a defect in the reviewed text and is not cured by lifecycle status.

## 6. Historical AD-036 result and current projection

The classification rule is fixed before inventory:

- a baseline-bound result describes the exact tree named by its own `baseline` and remains historical;
- a current projection enumerates live Accepted/Canonical primaries and must change when their lifecycle changes.

| Carrier | Class | Treatment |
|---|---|---|
| AD-036 prose, `baseline: f64b3a2...` and `baseline_evidence_objects` | historical discovery evidence | unchanged; its empty result remains true on that base |
| `architecture/consumer-need-discovery.yaml` result and lifecycle inventory | current projection layered over AD-036 history | schema 2 separates the historical empty result from the current OCP-023 need |
| `architecture/assignment-stable-surface.yaml` OCP-023 status | current consumer-status projection | `Draft → Accepted`; consumed elements unchanged |
| `architecture/assignment-consumer-compatibility.yaml` Accepted inventory | current compatibility projection | grows from five to six and replays OCP-023 on its existing synthetic fixture |
| `architecture/assignment-amendment-q2-attempt.yaml` Accepted inventory | current Q2 consumer review layered over historical AD-038 | grows from five to six; OCP-023 consumes current Assignment truth without amendment authority |
| README, roadmap, backlog and checker guide OCP-023 labels | current descriptive projections | synchronized to `0.2.0 / Accepted` |
| AD-041 and all `baseline_*` objects | historical act evidence | unchanged |

The current consumer-need projection now contains exactly one unmet need declared by OCP-023. The historical AD-036 empty set is not rewritten into a claim that it was wrong at its own baseline.

## 7. Accepted-consumer consequence without activation

After merge OCP-023 satisfies the Accepted-consumer status class used by G4. It also becomes the sixth current Accepted OCP-005 consumer. Its consumed Assignment surface remains bounded to exact identity/reference validation and `assignment_effective_at`; the existing `valid-one-effective` fixture replays the positive reference derivation, while removal of completeness returns indeterminate rather than changing Assignment truth.

This consequence removes no Assignment semantic blocker. `AMENDMENT_MODEL_ABSENT`, `TEMPORAL_MODEL_UNRESOLVED` and `PARTIAL_SCOPE_IDENTITY_UNRESOLVED` remain, `promotion_reachable` remains false and the promotion gate remains one completed `EVENT_T6` cycle with `active_cycle_id: null`.

## 8. Reviewed snapshot and byte identity

AD-029 requires every current Accepted OCP to have exactly one declared sibling reviewed snapshot. `docs/023-resource-occupancy/reviewed-contract-v0.1.0.md` is exactly the OCP-023 Draft blob from the acceptance base: 9,360 bytes, Git blob `8d5f5c2b340f78b84ce3de96c52ae18d0780ca66`, SHA-256 `c8a765053c3bd398eba18508c080f15dbe49a784565faa59bb8a88d266d872d4`.

The primary retains the snapshot body and appends only §§11–14 after changing frontmatter lifecycle fields. Loss, rename, content substitution, digest substitution, map-entry removal or primary-status drift fails the shared snapshot guard.

## 9. Exact acceptance baseline and anchor chain

The exact base is `main@e3ab36c25f4e5e69489b39c87748a9cbdea313a5`, tree `6bbc2557b47d55e7556edb4e9b218d30e291dcc2`. Every anchor was resolved there, reverse-resolved through `git ls-tree -r` to the stated path, checked for the declared state inside the object and SHA-256 hashed over raw blob bytes.

| Artifact | Reverse-resolved path | Declared base state | Git blob | SHA-256 |
|---|---|---|---|---|
| OCP-023 | `docs/023-resource-occupancy/README.md` | `0.1.0 / Draft`; partial Route D body | `8d5f5c2b340f78b84ce3de96c52ae18d0780ca66` | `c8a765053c3bd398eba18508c080f15dbe49a784565faa59bb8a88d266d872d4` |
| OCP-001 | `docs/001-ontology-governance/README.md` | `1.0.0 / Canonical`; Accepted distinct from Canonical, L2 Canonical-only | `33524fa3d18f3253faa9a854500be7ddfb20815f` | `da74645aa4f3cae10c7c59ae7b87abd1840544700e4a58e9efd3f6600a27f1cc` |
| OCP-005 | `docs/005-assignment-concept/README.md` | `0.2.8 / Draft`; Assignment truth owner | `6e6c00e723b15a348e7610d4ca5a1ae23526c52b` | `a9226f4f5e168b945ae743626e73ba5e25d67318b390869a493e5fd30bdaa065` |
| OCP-016 | `docs/016-core-boundary/README.md` | `1.0.0 / Canonical`; Route D and G4 | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| AD-029 | `architecture/discovery/AD-029-accepted-document-hygiene.md` | `0.1.0 / Accepted`; snapshot obligation | `b33f218567c53bea06c10efdf93fa5bd78a29a1c` | `19e62307c98b6b6a62945b5a27c3be8a5e49914eabb94814667b330ca58160c8` |
| AD-036 | `architecture/discovery/AD-036-consumer-need-discovery.md` | `0.1.0 / Discovery`; baseline-bound empty result | `3f8642777c16015226065f29f745b2e31bb6cd3a` | `564bc5c5b7d12c2be95278af6b3518a3af773ade701e3fee1dc4a9a4daac5603` |
| snapshot map | `architecture/accepted-document-snapshot-map.yaml` | schema 1; twelve entries | `c4d35d99ba46db310b9dfe9c84268914171f0e28` | `694ecb76da4851ba8228a738039256a4226a6e4848013c557c37213aa648755a` |
| need projection | `architecture/consumer-need-discovery.yaml` | schema 1; current empty result | `b6d85009db5d2a7adbbf80327d6a521f344f6045` | `bb742bf55e4e7fd3bade6ce88af78f754f6fb64104c3dab9f207dcd0be9ef544` |
| occupancy module | `tools/ontology_checker/ocp_checker/resource_occupancy.py` | reference derivation and fail-safe validator | `3d7ee96ac0d9f51cb04fd860cb5117806b422549` | `a44caaa19f1964e72b3c97f23175fa65695ce3b95e54f4b6f76fdf6bf96658c3` |
| occupancy manifest | `tools/ontology_checker/resource-occupancy-rules.yaml` | exact OCP-023 rule sources | `32e7ac535b6a24fc30784deee59411597725998d` | `16cf4094dff5775e34731862dafc3b455b6b31eac0d17733d7fd3496ca06e496` |
| occupancy tests | `tools/ontology_checker/tests/test_resource_occupancy.py` | ten focused tests including named defensive template | `e20a3ab0e52b352d119c2b3b769ae376c0f0ac82` | `4205d139689428a63831deed0cf6efdf42ec71b87c1dd9172cc04119686ac680` |

## 10. Version, evidence and accounting

OCP-023 moves `0.1.0 / Draft → 0.2.0 / Accepted`. This is a pre-canonical MINOR because lifecycle authority changes while semantic bytes do not. AD-042 begins `0.1.0 / Accepted` as the first exact acceptance decision; there is no prior revision to classify.

No fixture is added or changed. Unit tests grow only for acceptance snapshot, anchor, current-projection and replay enforcement. Current numeric accounting is mechanically derived from live metadata and the snapshot map; it must report one fewer Draft, one more Accepted and one more current Accepted snapshot, with unchanged Concepts, P-001 invokers and fixtures.

## 11. Safety, rollback and non-transfer

The snapshot contains only the already reviewed synthetic OCP-023 body. No operational record, coordinate, route, unit, organization identity, personal datum, key, token or credential is added.

Rollback requires a separate reviewed lifecycle act restoring `0.1.0 / Draft` together with snapshot-map, current need, consumer-status, compatibility and accounting projections while preserving historical AD-036 and AD-041 evidence. Partial rollback is invalid because it would leave authoritative current representations inconsistent.

This act does not activate a positive model, authorize `assignment_set_complete_for_resource`, authenticate `SYNTH-COMPLETE-*`, change OCP-005 or any Core artifact, remove Assignment blockers, create a Concept, change the graph, choose a candidate, start T7, resolve AB-018/AB-005 or authorize another act.

The decision becomes effective only after exact-head Fable review, Codex adjudication, green CI on the same head, fresh explicit Pavlo authorization naming that head and squash merge.
