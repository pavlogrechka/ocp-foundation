---
Decision-ID: AD-035
Title: Assignment Bounded Stable-Surface Discovery
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: AD-016, OCP-001, OCP-003, OCP-004, OCP-005, OCP-006, OCP-013, OCP-015, OCP-016, OCP-017, OCP-020, OCP-021
Applies-To: AB-062, Assignment bounded stable-surface discovery
Review-After: Separately mandated Assignment reassessment; this discovery creates no candidate selection, promotion cycle or lifecycle authority
---

# AD-035 — Assignment Bounded Stable-Surface Discovery

## 1. Mandate, subject and negative boundary

AD-016AB found two missing legality inputs for Assignment: a bounded compatibility surface and a later Architecture Board selection. Pavlo / Architecture Board separately mandated only the first input. The exact subject is current `OCP-005 0.2.8 / Draft`; Concept `Assignment` remains `Accepted`.

This act discovers current dependencies, direct consumers, candidate stable guarantees, moving surfaces and blockers. It does not:

- select Assignment or any joint unit;
- start a promotion cycle or edit `promotion_selections`;
- change OCP-005, any document `Status` or any `Concept-Status`;
- close, strike out or resolve an OCP-005 question;
- open T7 or authorize a reassessment, Board selection or promotion;
- create a Concept, graph edge, schema, Role/Provenance taxonomy, amendment model, temporal model, Reservation, Allocation or Conflict model; or
- transfer authority from Resource, Operation, Constraint or any Accepted consumer.

The discovery result is a bounded candidate surface plus named moving work. “Candidate” means discoverable and falsifiable, not selected or frozen.

## 2. Gate-first result before artifact form

OCP-016 G4 applies to positive-capable rules, results and profiles. This act creates an evidence map and a repository drift validator. Neither produces an operational result, activates a domain rule nor becomes a profile. G4 therefore does not apply, and no Accepted consumer activation is required. This result was established before choosing the map/module form and is recorded as a checked field in `assignment-stable-surface.yaml`.

The appropriate form is Route I governance/discovery evidence: AD-035 plus a machine-readable current-tree derivation. The form cannot approve itself and carries no lifecycle authority.

## 3. Exact baseline and full-chain anchors

The baseline is `main@6e83f34292fa818f62b1170e4b77aae98515a9a8`, tree `a9ecc632b0bba3bcb49e49328bdcb06b26626e0b`, with no open pull request. For every row below the path was resolved to the named blob, the blob was reverse-resolved through `git ls-tree -r --name-only`, the declared state was read from that object where applicable, and SHA-256 was recomputed from the same bytes. The declared path and reverse-resolved path matched in every row.

| Evidence | Declared state / role | Git blob | SHA-256 |
|---|---|---|---|
| `architecture/discovery/AD-016-foundation-canonicalization-readiness.md` | `0.31.0 / Accepted`; AD-016AB Assignment blocker basis | `54b86a701e57314ad55e40f4b3068063f0b9804a` | `948aa9af8ebe5367814a3c35abf282f653f49ef34db9c648cad007cc42fa537c` |
| `docs/001-ontology-governance/README.md` | `1.0.0 / Canonical`; lifecycle/dependency governance | `33524fa3d18f3253faa9a854500be7ddfb20815f` | `da74645aa4f3cae10c7c59ae7b87abd1840544700e4a58e9efd3f6600a27f1cc` |
| `docs/003-resource-concept/README.md` | `1.0.0 / Canonical`; Resource `Canonical` | `71485bb337cfd59def2e0f1b18b474a7959bd30c` | `f8656769dd046f221843f627c746d0d6040c2e83c736b900370d60244fce8315` |
| `docs/004-operation-concept/README.md` | `1.0.1 / Canonical`; Operation `Canonical` | `37fab136c578d2b8fafd6e900261ef64144943d9` | `ff0480913044b4dff8abcf69808b2d1cafe80a7d9f58c7ec06d2adeb33745538` |
| `docs/005-assignment-concept/README.md` | `0.2.8 / Draft`; Assignment `Accepted` | `6e6c00e723b15a348e7610d4ca5a1ae23526c52b` | `a9226f4f5e168b945ae743626e73ba5e25d67318b390869a493e5fd30bdaa065` |
| `docs/006-constraint-concept/README.md` | `0.3.2 / Draft`; direct Draft consumer | `50f149cf5563083bb84d5d2197ec32c2ed15fa9b` | `0472d8ce4b15a8c64d58151ee7f706b450b930f708f6f0a7a40bdd87914b3b10` |
| `docs/013-resource-interchangeability/README.md` | `0.2.0 / Accepted`; direct Accepted consumer | `658a291b4c3b9a0229aba09d485c1137723fe70b` | `a20659422f847f49a9231b8c1d1dabc0d8b911d9667c44013280b1826f621a74` |
| `docs/015-coordination-workflow/README.md` | `0.2.0 / Accepted`; direct Accepted consumer | `ea60634e54faedabb8c5e08b036030c2f0e4e20b` | `6077136b2460cfc56d0e06af9137338cb494ac9a8e14df036e662d9240415b1d` |
| `docs/016-core-boundary/README.md` | `1.0.0 / Canonical`; G4 boundary | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| `docs/017-operation-lifecycle/README.md` | `0.2.0 / Accepted`; direct Accepted consumer | `0b2ea683df308babd1111ff47e9272c9b0742f78` | `061e2c8a4c9d3d02bb5a7492e9c8723cace11a462548970727552e18c645a030` |
| `docs/020-quantitative-constraint-input/README.md` | `0.2.0 / Accepted`; direct Accepted consumer | `0e1e7d0947ab3c7d1c0355258651179f618636a2` | `1783c32094aee9f09ca50ececb12bf9ec8f3c6599590331dba3894ad727d9b5c` |
| `docs/021-reservation-allocation-boundary/README.md` | `0.1.0 / Draft`; direct Draft consumer | `af96e2a9a67977cf5de8c4c566b1e9293e23687f` | `85cdc7e3bb5281a6b2fe0af4d11b31bc47040b762de5786a0a8a10c2e000f683` |
| `tools/ontology_checker/ocp_checker/checker.py` | Assignment validation and derivations | `120ada9dd00b1df0b46cf3060aef2b0c290948b1` | `3a093f0d76113bb5dd2799c7d0aaf73b51b752569dc13de145bb3d158a7b4a47` |
| `tools/ontology_checker/rules.yaml` | OCP-005 §8/§9 derivation sources | `8d00050e32cea2ceb27d13c3d7788b5e8554cc84` | `e861e860f576cf824aff755d99f0da3118256f20d742f25eb4b0434503c6042d` |
| `architecture/foundation-promotion-gate.yaml` | schema 5; only `EVENT_T6` complete; `active_cycle_id: null` | `78f5f75d84fe9b0bdbf43ad3922404fa34f6c2d1` | `ca11036e10397d24b308957e059d0d5def1a9d90177c0d82987191c919a56dfd` |

Hashes identify evidence, not authority. File order, recency, consumer count and green tests cannot select a lifecycle outcome.

## 4. Enumeration and classification criteria fixed before application

Four rules were fixed before reading the results:

1. **Concept dependency** is an exact token in current OCP-005 `Concept-Depends-On`. A prose mention does not add a dependency.
2. **Direct consumer** is a current primary `docs/[0-9][0-9][0-9]-*/README.md` whose structured `Depends-On` contains exact `OCP-005`. Its current `Status` determines Accepted versus Draft. `Used-By`, prose, snapshots, ADs and checker code do not add a primary consumer.
3. **Stable candidate** is a normative OCP-005 element with a named owner, an explicit or executable invariant, and no unresolved question capable of changing that element. **Moving** means at least one open question can alter the representation or rule.
4. An open question **blocks the whole-document freeze** if it can change Assignment identity, mandatory references/lifecycle/effectivity, or an Accepted consumer's required behavior; it is **local** if it can remain open without falsifying the bounded kernel; it is **outside** if another owner can answer it while the Assignment boundary stays unchanged.

Resolved strikeouts are historical members of the numbered inventory, not open questions. Discovery preserves them byte-for-byte and does not count them as newly closed.

## 5. Non-empty Concept dependency axis

The current `Concept-Depends-On` set is exactly `[Resource, Operation]`.

| Dependency | Live defining state | Consequence |
|---|---|---|
| Resource / OCP-003 | document `1.0.0 / Canonical`; Concept `Canonical` | the Assignment subject endpoint has a stable upstream identity owner |
| Operation / OCP-004 | document `1.0.1 / Canonical`; Concept `Canonical` | the Assignment context endpoint has a stable upstream identity owner |

Both Concept dependencies and the corresponding direct OCP document dependencies pass the current dependency floor. This is necessary for a future freeze: Assignment cannot be more stable than either endpoint. It is not sufficient. It says nothing about Assignment's own amendment, temporal, partial-scope or consumer-compatibility blockers and supplies no selection authority.

That is the material difference from Event discovery: Event had an empty Concept dependency set; Assignment must preserve two upstream identities even for its bounded kernel.

## 6. Complete direct-consumer inventory

The structured sweep returns exactly six primary consumers.

| Consumer | State | Exact current Assignment reliance | Future compatibility consequence |
|---|---|---|---|
| OCP-006 | Draft | effective Assignment sets and the negative fact that `supersedes_assignment_ref` does not determine overlap/gap | may shape conflict/replacement surfaces, but is not an Accepted compatibility gate |
| OCP-013 | Accepted | exclusion of Assignment mutation, replacement execution and selection authority | identity/non-mutation boundary must remain true |
| OCP-015 | Accepted | Assignment identity preservation and no workflow-driven identity alteration | identity and non-mutation boundary must remain true |
| OCP-017 | Accepted | `operation_ref`, authoritative transition history and exact `assignment_effective_at` at terminal evaluation time | positive formula/lifecycle compatibility must be proved before promotion |
| OCP-020 | Accepted | existing Assignment artifacts remain valid; quantitative input cannot create/amend/terminate Assignment | non-authority and no-required-migration boundary must remain true |
| OCP-021 | Draft | Assignment references remain OCP-005-owned and cannot be renamed into Reservation/Allocation or mutation authority | may shape future composition, but is not an Accepted compatibility gate |

The Accepted set is exactly OCP-013/OCP-015/OCP-017/OCP-020; the Draft set is exactly OCP-006/OCP-021. OCP-017 is the only Accepted consumer of a positive OCP-005 derivation. The other three Accepted consumers constrain identity, non-mutation and non-authority. Treating all four as equivalent “document consumers” would hide this compatibility asymmetry.

All six structured document bindings are unversioned. Their presence establishes dependency, not compatibility with a future OCP-005 version. The later selection/promotion line therefore needs a separately reviewed compatibility contract.

## 7. Open-question classification

The complete numbered inventory has eleven entries: nine live open questions and two already-resolved historical strikeouts.

| ID | Current state | Classification | Surface and reason |
|---|---|---|---|
| Q1 | resolved historical | outside open set | Reservation object/Concept boundary was already answered negatively; preserved, not reopened |
| Q2 | open | blocks whole-document freeze | amendment after Establishment can change role/applicability mutability and consumer replay |
| Q3 | open | blocks whole-document freeze | retroactive Establishment can change the effective-at formula and historical truth |
| Q4 | open | local after bounded freeze | Role taxonomy can be separately governed while local `role_code` structure stays valid |
| Q5 | open | blocks whole-document freeze | partial composite-Resource scope can change the subject/reference identity model |
| Q6 | resolved historical | outside open set | quantitative input was answered by OCP-020/OCP-021; preserved, not reopened |
| Q7 | open | local after bounded freeze | role specializations can be separate profiles without changing the minimum kernel |
| Q8 | open | outside bounded surface | Constraint owns simultaneous-Assignment conflict; OCP-005 preserves only the handoff/non-automatic-conflict boundary |
| Q9 | open | blocks whole-document freeze | multiple applicability intervals can change the current single-interval temporal contract |
| Q10 | open | local after bounded freeze | provenance taxonomy can remain external while the opaque non-empty reference stays stable |
| Q11 | open | local after bounded freeze | replacement policy may govern overlap/gap while the stable no-auto-termination identity boundary remains true |

No question text, strikeout or disposition is changed by AD-035.

## 8. Candidate bounded stable surface

Six surfaces satisfy the predeclared candidate rule.

| ID | OCP-005 owner | Candidate guarantee | Current executable/consumer relevance |
|---|---|---|---|
| `ASSIGNMENT_IDENTITY_REFERENCE_KERNEL` | §§1, 5, 6.1, 16 | stable `assignment_id`; one Resource/Operation; established endpoint refs immutable | OCP-013/OCP-015 require identity/non-mutation; OCP-017 consumes `operation_ref` |
| `TRANSITION_HISTORY_LIFECYCLE_KERNEL` | §§7, 15–16 | authoritative finite linear transition history and derived stage/timestamps/provenance | checker validates paths/projections; OCP-017 forbids mutation and reads lifecycle truth |
| `STRUCTURAL_ROLE_PROVENANCE_KERNEL` | §§6, 14, 16 | required established-lineage refs, minimally valid role, applicability start and attributable establishment provenance | current validator fails missing/invalid structural fields; taxonomies stay outside |
| `NON_INHERITANCE_NON_AUTHORITY_BOUNDARY` | §§11, 13–15, 18 | no automatic composition inheritance, reservation, availability, Readiness, authorization or result | OCP-013/OCP-015/OCP-020 rely on these negative guarantees |
| `SUPERSESSION_IDENTITY_BOUNDARY` | §§12, 14, 16 | successor intent never edits identity or silently terminates the prior Assignment | Draft OCP-006/OCP-021 may add policy/composition later without reversing this guarantee |
| `EXECUTABLE_ASSIGNMENT_BOUNDARY` | checker plus rule manifest | `validate_assignment`, `assignment_effective_at` and `derived_participates_in` remain current falsifiable behavior | proves present behavior, not future compatibility or readiness |

This bounded set is useful but not a whole-document freeze. In particular, the current effective-at implementation is executable evidence but its temporal extension remains moving under Q3/Q9. A future contract must distinguish preserving current consumer behavior from freezing every future temporal option.

## 9. Moving surfaces

| ID | Question(s) | Why moving | Required future owner/result |
|---|---|---|---|
| `AMENDMENT_AFTER_ESTABLISHMENT` | Q2 | no rule says whether role/applicability is amended, superseded or replaced | Assignment lifecycle/amendment act with replay and migration |
| `TEMPORAL_EFFECTIVITY_EXTENSION` | Q3, Q9 | retroactivity and multiple intervals can alter the current formula | named temporal owner, compatibility and historical replay |
| `ROLE_GOVERNANCE` | Q4, Q7 | no Core taxonomy or specialization form is selected | separate taxonomy/profile route if concrete consumer need appears |
| `COMPOSITE_RESOURCE_SCOPE` | Q5 | partial subject can alter what `resource_ref` identifies | Resource/Assignment identity decision |
| `CONSTRAINT_CONFLICT_HANDOFF` | Q8 | positive Conflict model remains under separate Constraint/Conflict ownership | AB-018 route; OCP-005 keeps only non-automatic boundary |
| `PROVENANCE_TAXONOMY` | Q10 | opaque reference exists but canonical types do not | separate provenance-governance owner |
| `REPLACEMENT_POLICY` | Q11 | overlap/gap policy is deferred while no-auto-termination remains stable | Constraint or amendment owner with explicit policy |

## 10. Named blockers

1. `AMENDMENT_MODEL_ABSENT` blocks whole-document freeze because Q2 can change post-Establishment mutability and replay.
2. `TEMPORAL_MODEL_UNRESOLVED` blocks whole-document freeze because Q3 and Q9 can change effective historical truth.
3. `PARTIAL_SCOPE_IDENTITY_UNRESOLVED` blocks whole-document freeze because Q5 can change the subject/reference model.
4. `ACCEPTED_CONSUMER_COMPATIBILITY_UNPROVEN` blocks promotion, not discovery. Four Accepted consumers must receive an exact compatibility/migration/rollback proof; bare `Depends-On: OCP-005` cannot supply it.

Q4/Q7/Q10/Q11 remain local, and Q8 remains an external-owner handoff, only because the bounded candidate explicitly excludes their positive models. Expanding the candidate would require reclassification.

## 11. Outcome-fair discovery comparison

The same axes are applied to every discovery outcome: dependency truth, Accepted-consumer compatibility, open-question integrity, executable falsifiability, migration cost, rollback and absence of self-supplied lifecycle authority.

| Outcome | Benefit | Cost / failure | Discovery disposition |
|---|---|---|---|
| A0 — no stable surface | maximally conservative | discards already executable identity/lifecycle/non-authority guarantees and gives later comparison no bounded option | lawful fallback, not leading |
| AW — whole-document surface | simple boundary | freezes Q2/Q3/Q5/Q9 and overstates compatibility of unversioned consumers | blocked |
| AK — bounded in-place kernel | preserves six named guarantees while leaving all seven moving surfaces explicit | later act must prove consumer compatibility and select a lifecycle outcome | leading discovery candidate; not selected |
| AC — Accepted-consumer intersection | minimizes promises to observed use | three consumers mostly require negative boundaries while OCP-017 requires positive temporal/lifecycle behavior; intersection is too weak to own Assignment semantics | insufficient alone |
| AX — extracted contract | could isolate stable bytes | creates a second artifact/owner and migration burden without an Accepted consumer asking for extraction | not justified |

AK is the most informative discovery result because it separates a useful kernel without pretending the blockers are solved. It is not an Architecture Board selection, does not start a gate cycle and cannot authorize promotion.

## 12. Executable evidence

`architecture/assignment-stable-surface.yaml` records the exact baseline, G4 result, unchanged promotion-gate state, two Concept dependencies, six direct consumers with their concrete consumed elements, all eleven question dispositions, six candidate surfaces, seven moving surfaces, four blockers and six forbidden outcomes.

`assignment_stable_surface.py` independently:

- re-parses OCP-005 lifecycle and Concept dependencies;
- re-derives the complete direct-consumer set from every primary OCP frontmatter;
- verifies current consumer status class and every declared consumed token;
- checks all eleven question tokens and the exact nine-open/two-historical split;
- checks every declared stable evidence token against its live source;
- verifies both Concept dependency states from their defining documents; and
- proves schema 5 still has only completed `EVENT_T6` and `active_cycle_id: null`.

Eight new unit tests move the exact suite from **299 to 307**; fixtures remain **274** because discovery adds no domain behavior or synthetic scenario. The required test `test_every_defensive_value_is_individually_fixture_and_mutation_live` individually attacks every member of ten defensive sets and every key of six expected-value maps. Separate tests attack every subject lifecycle field, Concept dependency state, consumer binding/status/consumed element, question token/state/classification, stable evidence token, anchor field and promotion-gate guard. Claims match actual coverage: no fixture coverage is claimed.

## 13. Version classification, footprint and protected state

AD-035 begins at `0.1.0 / Discovery`: it is a new evidence artifact, not a change to OCP-005 or any semantic contract. `assignment-stable-surface.yaml` begins at schema 1 because it introduces a new evidence language. The checker module/tests are executable support and carry no OCP SemVer.

README, roadmap, AB-062 descriptive text and checker guide are current accounting/documentation projections with no artifact SemVer. The derived central test count changes from 299 to 307 because eight discoverable test methods are added; fixture count remains 274.

The following remain byte-identical: OCP-000, OCP-002, every OCP body, every Concept status, graph and foundation map, P-001, all reviewed snapshots, all historical `baseline_*` objects, all fixtures and the promotion-gate map. OCP-005 remains `0.2.8 / Draft`; OCP-006 remains `0.3.2 / Draft`; Assignment and Constraint remain `Accepted`; OCP-010/Event remain `1.0.1 / Canonical`; concept distribution remains six Canonical/two Accepted; P-001 remains blob `c679f3e35eb015aecf6cb9a839aacd75a432e844`.

## 14. Migration, rollback and lawful continuation

Discovery performs no record, schema, reference, graph, Pattern, fixture, consumer or lifecycle migration. Rollback removes AD-035, its map/module/tests/check integration and the four accounting/documentation updates as one reviewed unit. Partial rollback is invalid because prose without executable evidence overstates reproducibility, while a validator without its discovery act loses its authority source.

Return to A0 if the two Concept dependencies, six-consumer inventory, nine-open/two-historical question split, evidence tokens or unchanged promotion-gate state no longer reproduce.

The shortest lawful continuation is a separately mandated post-discovery reassessment that compares AK and then-current alternatives. Its recommendation still has no selection authority. A later separate Board act may select at most one candidate, and only a still later separately mandated lifecycle act may start a cycle or edit OCP-005 status. AD-035 authorizes none of those acts by implication.

AD-035 itself requires exact-head Fable review, explicit Codex adjudication, green CI on the same head and fresh Pavlo merge authorization naming that head. Any head change resets all four gates.
