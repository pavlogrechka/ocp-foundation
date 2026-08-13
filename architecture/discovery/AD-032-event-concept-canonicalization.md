---
Decision-ID: AD-032
Title: Event Concept Canonicalization
Version: 0.1.0
Status: Accepted
Owner: Architecture Board
Depends-On: AD-006, AD-016, AD-031, OCP-000, OCP-001, OCP-002, OCP-004, OCP-008, OCP-010, OCP-011, OCP-016, OCP-017, P-001
Applies-To: Event Concept Accepted to Canonical transition
---

# AD-032 — Event Concept Canonicalization

## 1. Mandate, Board input and boundary

Pavlo / Architecture Board explicitly selected `Event: Accepted → Canonical` as the input of this separate OCP-001 canonicalization cycle on `main@060b801e78b0ce88c0eb858be127cecce3e6569f`. This act proves the other two OCP-001 prerequisites—stable dependencies and machine-readable checks—and atomically synchronizes the authorized status. It does not infer the Board decision from CI, document status or earlier promotion.

OCP-010 is already `1.0.0 / Canonical`; only its Concept lifecycle metadata and PATCH accounting change. Sections 1–26 keep their semantic meaning and numbering. No new Concept, graph edge, identity, Event field, relation owner, rule, record contract, fixture or behavior enters this act.

Gate-first is resolved before form selection. This is a governance status transition for an existing Concept, not a positive-capable operational rule, result vocabulary or profile activation. OCP-016 G4 therefore does not apply and an Accepted activation consumer is not required. OCP-011 and OCP-017 remain real Accepted consumers and compatibility evidence, but neither self-authorizes canonicalization.

## 2. Exact base and full-chain anchors

The exact base tree is `a6aaedeeabd05a6951d4c8cbc456e1bbd5248d0a`. Each row was resolved at the base commit, reverse-resolved through `git ls-tree -r`, checked against the state inside the object and SHA-256 hashed from raw bytes.

| Artifact | Reverse-resolved path | Base state | Git blob | SHA-256 |
|---|---|---|---|---|
| OCP-000 | `docs/000-operational-ontology/README.md` | `1.5.0 / Canonical`; Event Accepted | `7da7d7aad6ba505603cfbfa98ff1349c84892720` | `3f76ae4b55f01ce388bd865330f386c3ec0a6f6416e1aaed522145df96cfb7d6` |
| OCP-001 | `docs/001-ontology-governance/README.md` | `1.0.0 / Canonical`; canonicalization rule owner | `33524fa3d18f3253faa9a854500be7ddfb20815f` | `da74645aa4f3cae10c7c59ae7b87abd1840544700e4a58e9efd3f6600a27f1cc` |
| OCP-002 | `docs/002-concept-taxonomy/README.md` | `1.5.0 / Canonical`; Event Accepted projection | `aaa4ac27a7d77c52b74833a1c088c037538f1f06` | `335f3e8c2f51110f192ceb608188437b6d2fe5b908bbf12894c31e45a651e7c6` |
| OCP-010 | `docs/010-event-concept/README.md` | `1.0.0 / Canonical`; Event Accepted | `6e6b570d6a13848977919943b895eea0811443a1` | `77713b0f368a2858e528ede9708f43931fb30d7b322330a89153dafd8d36f10f` |
| P-001 | `patterns/P-001-identified-record-pattern.md` | `0.1.0 / Accepted` | `c679f3e35eb015aecf6cb9a839aacd75a432e844` | `2c9dd172a19c2d340b58a159fe5e71b64215a3968ee05fa330790b7e6359c797` |
| Event rules | `tools/ontology_checker/rules.yaml` | Event reference and collection rules | `8d00050e32cea2ceb27d13c3d7788b5e8554cc84` | `e861e860f576cf824aff755d99f0da3118256f20d742f25eb4b0434503c6042d` |
| Event checker | `tools/ontology_checker/ocp_checker/event.py` | identity/reference/collection implementation | `e04b9bedbe4fe1d4923e4d0acc0cbd5f471ee5ea` | `d034fae851e8dd5e00c360cd19bbb3c38b0462856010af955a430ceaa1b7de64` |
| integrated Event fixture | `tools/ontology_checker/fixtures/event/valid-integrated-scenario.yaml` | valid Event/Observation assessment composition | `fac09db73a9101c8e01a88fba54014318daefbbe` | `bec708d446585d0ca4aa4cf3e815421a218d8e3fb05426dd08042dd1aabc39be` |
| lifecycle fixture | `tools/ontology_checker/fixtures/operation_lifecycle/valid-q3i-completed.yaml` | valid occurrence/provenance/non-causation consumer | `c85a65e217c7d0ecdbabf8e9adf76f1a88a7faff` | `901ce32b9af2dcf9e664b565c7a6a4fc8919c7329d40d666a38a3115d0fb5672` |
| generated map | `architecture/baselines/foundation-map.md` | Event Accepted and isolated | `faa71f329a3207bc6d3096b7cc86ecfab6130296` | `ea88b22d6a0543995e2b757daec0a60b62b0028c8c3583e237a6b178951be882` |

Anchors identify evidence and state only. They do not substitute for the Board decision or prove semantic sufficiency by recency.

## 3. Stable dependencies derived from live metadata

The derivation reads the current OCP-010 metadata before consulting the witness:

1. `Concept-Depends-On: []` means Event identity has no fundamental Concept dependency whose lifecycle could destabilize it. Empty is a concrete exact set, not missing data; the metadata key exists and the graph places Event among isolated defined Concepts.
2. Direct OCP dependencies are exactly OCP-000/001/002/004/008. Every one is already `Canonical` in the proposed tree, so OCP-001 L2 passes independently.
3. AD-006 is Accepted decision provenance and is not assigned a fictitious Canonical status.
4. P-001 is both a bare artifact dependency and exact `Uses-Patterns: P-001@0.1.0`; the current Pattern is `0.1.0 / Accepted`, satisfying the separate invoked-Pattern floor.
5. No current Operation↔Event Concept edge exists. Canonicalization freezes this no-edge boundary but does not manufacture a dependency or positive relation owner.

Mutations adding a Concept dependency, making any direct OCP Draft or making P-001 Draft fail `EVENT_CONCEPT_CANONICALIZATION_DEPENDENCY_UNSTABLE`. Stable dependencies are therefore proved, not copied from a claim.

## 4. Machine-readable semantic checks

The machine-readable requirement is met by four independent executable surfaces already governing the semantic body that canonicalization freezes:

| Surface | Executable proof | Frozen responsibility |
|---|---|---|
| Event identity and exact reference | OCP-010 rules plus `event.py::resolve_event` and reference fixtures | stable `event_id`, exact resolution, no label/time/order identity collapse |
| Observation collection and supersession | `event.py::observations_for_event`, P-001 conformance and negative fixtures | separate attributable ObservationRecord identity, optional linkage and history preservation |
| integrated Event assessment composition | `valid-integrated-scenario.yaml` replay | exact `event@1` / `observation-record@1` evidence without truth or assessment ownership transfer |
| primary consumer compatibility | integrated OCP-011 fixture plus the executable AD-016AD promotion witness and its OCP-017 Q3I replay | occurrence/provenance/non-causation behavior across both Accepted consumers |

The canonicalization checker validates every named token and executes both valid fixtures. It also depends on the already-live repository status-sync, artifact-governance, Concept graph and generated-map checks. Green evidence does not itself choose Canonical; it proves the separately Board-selected semantic surface is mechanically represented.

## 5. Current versus historical carrier criterion

The criterion is fixed before inventory:

- a **current carrier** is a live registry/taxonomy/defining metadata value, a current peer/status view, a generated current-state projection, a current gate/promotion subject, or repository/backlog prose that explicitly claims the state now; it must synchronize;
- a **historical carrier** is bound to its own exact `baseline`, appears in `baseline_subject_state`, `baseline_evidence_objects` or `baseline_gate_state`, or explicitly records a completed earlier acceptance/promotion state; it must remain byte-stable;
- a generic semantic mention of Event or an Accepted status of a different artifact is neither class.

One document may contain both. OCP-010 frontmatter and §27 are current, while §24 acceptance and §26 document-promotion statements are historical. OCP-005/OCP-006 current §4 rows change, while their earlier PATCH accounting remains history. AD-016 and AD-031 exact-base tables remain history even when the same files also explain later current acts.

The complete structured/current carrier inventory is encoded in `event-concept-canonicalization.yaml`: OCP-000, OCP-002, OCP-010, current OCP-004/005/006 peer views, generated map, future-intent basis, lifecycle-promotion subject, foundation gate candidate, README, roadmap and AB-062 accounting. The three baseline-bound witness maps—AD-031 stable surface, AD-016AB reassessment and AD-016AC selection—remain unchanged and valid.

## 6. Registry precedent and atomic transition

Five existing Canonical rows establish one form: defining OCP and exact lifecycle-decision provenance, ending with a separately authorized lifecycle act rather than only the original acceptance PR. Event therefore becomes:

`OCP-010; AD-006C; AD-016AD; AD-032; separately authorized Event Concept canonicalization act`.

This preserves distinct provenance: AD-006C selects Event/Observation identity, AD-016AD promotes the document, and AD-032 proves Concept canonicalization prerequisites. It does not copy another Concept's T4/WJ route labels.

The atomic set is OCP-000 `1.5.0 → 1.6.0` MINOR and OCP-002 `1.5.0 → 1.6.0` MINOR because each authoritative projection admits a newly Canonical Concept; OCP-010 `1.0.0 → 1.0.1`, OCP-004 `1.0.0 → 1.0.1`, OCP-005 `0.2.7 → 0.2.8` and OCP-006 `0.3.1 → 0.3.2` are PATCH because only lifecycle metadata/current peer projections and their accounting change without semantic behavior. Generated map/future-intent, gate/promotion maps, README, roadmap, backlog and checker documentation have no independent artifact SemVer.

## 7. Mutation proof, rollback and boundary

Repository status synchronization already rejects registry/taxonomy/defining metadata mismatches and current peer-table drift. AD-032 adds executable coverage for both current directions and the historical boundary:

- reverting any authoritative/current Event carrier to Accepted fails;
- changing any stable dependency or executable evidence token fails;
- all defensive sets and each declared value are individually mutation-live under `test_every_defensive_value_is_individually_fixture_and_mutation_live`;
- the three baseline-bound witnesses remain valid after canonicalization, while rewriting their baseline/status evidence fails.

Rollback is a new separately reviewed atomic Concept lifecycle act. It cannot edit only one projection, rewrite historical snapshots or infer that a semantic defect authorizes status reversal. OCP-005/OCP-006 remain Draft with Assignment/Constraint Accepted; P-001 bytes, reviewed snapshots, fixtures, `Review-After`, AB statuses other than descriptive AB-062 text and all other Concept statuses remain unchanged. No T7, OCP-019/021/022 acceptance, AB-018/AB-005 opening or next-act authority is created.

The exact base reproduces 283 unit tests and 274 synthetic fixtures. This act adds eight governance tests—seven dedicated canonicalization tests plus one historical-witness survival regression—and no fixture, producing 291 tests / 274 fixtures in both checker contexts. The repository readiness estimate changes only in the Core-domain row (`91% → 93%`) because the separately selected Concept lifecycle milestone completed; the overall `≈72%` remains unchanged because no operational workflow, production contract or implementation surface advanced.
