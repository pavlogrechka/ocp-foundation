---
Decision-ID: AD-031
Title: Event Dependency and Stable-Surface Discovery
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: AD-006, AD-016, OCP-001, OCP-004, OCP-008, OCP-010, OCP-011, OCP-016, OCP-017, P-001
Applies-To: AB-062, Y10D Event dependency and stable-surface discovery
Review-After: Separately mandated post-discovery reassessment; this discovery creates no Board selection, promotion or T6 authority
---

# AD-031 — Event Dependency and Stable-Surface Discovery

## 1. Mandate, subject and hard boundary

AD-016Z selected Y10D only as the scope of a future separately mandated Event dependency/stable-surface discovery. AD-016AA then proved that the discovery, post-discovery reassessment and candidate-specific Board selection were absent. Pavlo / Architecture Board has now separately mandated the first of those three links.

The subject is exact current `OCP-010 0.2.1 / Draft`; Concept `Event` remains `Accepted`. This act discovers current dependencies, candidate stable guarantees, moving surfaces, consumer costs and blockers. It does not:

- edit or accept OCP-010;
- promote any document or Concept to `Canonical`;
- open T6;
- create the post-discovery reassessment;
- select a candidate or lifecycle outcome;
- create an Operation/Event relation, graph edge, route, temporal model, kind registry or correlation rule; or
- transfer OutcomeAssessmentRecord authority away from Accepted OCP-011.

The fail-safe result is a bounded stable-surface candidate plus named unresolved work, not a promotion recommendation.

## 2. Exact baseline and full-chain anchors

The exact baseline is `main@ed1e338f52d87de42d56c66c20c7cf89891a589f`, tree `8216a44d79357a4f84977e7b2ddd9dadc33567bf`, with no open pull request. Every row was resolved path → Git blob, reverse-resolved through `git ls-tree -r --name-only`, and independently SHA-256 hashed.

| Evidence | Current fact | Git blob | SHA-256 |
|---|---|---|---|
| AD-016 | `0.28.0 / Accepted`; Y10D is the next missing link | `19bee8d85670548cf93b81649a391f5c99f8bca7` | `487df31da4dc3cccbb81728f70e2897b29da05f947c94d782f55365de440dea5` |
| OCP-001 | `1.0.0 / Canonical`; L2 and lifecycle governance | `33524fa3d18f3253faa9a854500be7ddfb20815f` | `da74645aa4f3cae10c7c59ae7b87abd1840544700e4a58e9efd3f6600a27f1cc` |
| OCP-004 | `1.0.0 / Canonical`; upstream Operation owner | `1ff548a1f213b574472a90a8b3cfe014f6c1ce11` | `9c9173d3a3dec044e2cae2eb8fd5b66d07a106318f497a973409fedf4677155b` |
| OCP-008 | `1.0.0 / Canonical`; upstream Objective owner | `24ed01e0f5d6bc8f349a7aedae4c5f100eb449ee` | `46f1ecb7b956b106f9c66da0626ec4266961e07492059e594110f63736be6f0d` |
| OCP-010 | `0.2.1 / Draft`; Event Concept `Accepted` | `3a49b75bfa479e24debb89a130b7a05d6c790a88` | `5ead70eb7238d6b6e630d2fa5850bb4a9325a752fed57d9239b9977642d67706` |
| OCP-011 | `0.3.0 / Accepted`; direct assessment consumer | `ff2608a372c6305db4c290f05c15e961ca96e6f6` | `1fb08e18fab560e671b468585d699a7d70bd55ed5be674315cb780a48bc70cc5` |
| OCP-016 | `1.0.0 / Canonical`; route ownership boundary | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| OCP-017 | `0.2.0 / Accepted`; direct lifecycle consumer | `0b2ea683df308babd1111ff47e9272c9b0742f78` | `061e2c8a4c9d3d02bb5a7492e9c8723cace11a462548970727552e18c645a030` |
| P-001 | `0.1.0 / Accepted`; exact ObservationRecord form | `c679f3e35eb015aecf6cb9a839aacd75a432e844` | `2c9dd172a19c2d340b58a159fe5e71b64215a3968ee05fa330790b7e6359c797` |
| global rule manifest | 34 Event validation IDs and two Event derivations | `8d00050e32cea2ceb27d13c3d7788b5e8554cc84` | `e861e860f576cf824aff755d99f0da3118256f20d742f25eb4b0434503c6042d` |
| Event checker | current identity/reference/scenario implementation | `e04b9bedbe4fe1d4923e4d0acc0cbd5f471ee5ea` | `d034fae851e8dd5e00c360cd19bbb3c38b0462856010af955a430ceaa1b7de64` |
| foundation map | Operation ⇢ Event remains a dashed non-edge | `faa71f329a3207bc6d3096b7cc86ecfab6130296` | `ea88b22d6a0543995e2b757daec0a60b62b0028c8c3583e237a6b178951be882` |

Hashes identify evidence, not authority. Recency, file order, consumer count and green tests cannot select a later lifecycle outcome.

## 3. Enumeration criterion fixed before application

The discovery uses four separate classes and never promotes one class into another by prose frequency:

1. **Direct inputs** are exactly the tokens in current OCP-010 primary frontmatter `Depends-On`, plus the separately parsed `Uses-Patterns` binding. Order is preserved.
2. **Direct primary consumers** are exactly current primary `docs/[0-9][0-9][0-9]-*/README.md` files whose structured `Depends-On` includes exact token `OCP-010` or an explicit versioned OCP-010 token. `Used-By`, prose citations, discovery documents, snapshots, checker sources and accounting do not add a primary consumer.
3. **Executable consumers** are checker rules, code and fixtures whose current source or behavior is owned by OCP-010. They prove a finite surface but do not become document dependencies or semantic owners.
4. **Descriptive references** are every other current mention. They may expose compatibility pressure, but cannot add an edge, dependency or authority.

Binding is classified independently for each included item:

- a bare metadata token is **unversioned-document** or **unversioned-decision**;
- `Uses-Patterns: P-001@0.1.0` is an exact Pattern binding even though `Depends-On` also contains bare `P-001`;
- `event@1` and `observation-record@1` are exact semantic record-kind references, not exact OCP-010 document-version bindings; and
- words such as “exact Event provenance” without an `identity@version` token are semantic constraints, not a versioned reference.

This criterion is encoded in `architecture/event-stable-surface.yaml` and independently recomputed by `event_stable_surface.py`.

## 4. What OCP-010 consumes

The structured input inventory is exactly seven entries.

| Input | Current state / owner used by Event | Binding result | Adjudication |
|---|---|---|---|
| OCP-000 | `1.5.0 / Canonical`; Concept registry | bare `OCP-000`, unversioned document | keeps Event registry identity/status visible; no new registry edit |
| OCP-001 | `1.0.0 / Canonical`; governance | bare `OCP-001`, unversioned document | supplies lifecycle and dependency floors, not Event semantics |
| OCP-002 | `1.5.0 / Canonical`; taxonomy projection | bare `OCP-002`, unversioned document | keeps Event projection consistent; no taxonomy edit |
| OCP-004 | `1.0.0 / Canonical`; Operation | bare `OCP-004`, unversioned document | OCP-010 §10 consumes the identity/boundary while preserving no edge and no generation rule |
| OCP-008 | `1.0.0 / Canonical`; Objective | bare `OCP-008`, unversioned document | OCP-010 §11 consumes Objective identity while denying achievement inference |
| AD-006 | `Accepted`; Event/Result boundary and E3 | bare `AD-006`, unversioned decision | historical decision basis; not an exact artifact-version binding |
| P-001 | `0.1.0 / Accepted` | bare dependency **plus exact** `P-001@0.1.0` use | exact only for ObservationRecord; Event itself does not invoke P-001 |

The five direct OCP dependencies are all Canonical, so Event still passes L2. That pass is necessary but supplies no discovery, reassessment, selection or promotion authority.

## 5. What consumes OCP-010

The structured primary-consumer sweep returns exactly two documents.

| Consumer | Structured binding | Exact semantic binding found | Current reliance and cost |
|---|---|---|---|
| OCP-011 `0.3.0 / Accepted` | bare `OCP-010`; unversioned document | `event@1`, `observation-record@1` | freezes pressure on Event/Observation identity, evidence fields and time meanings; it does not exact-bind OCP-010 `0.2.1` |
| OCP-017 `0.2.0 / Accepted` | bare `OCP-010`; unversioned document | none | relies on independent occurrence, zero/one/many relevance and exact Event provenance while denying generation, causation and reverse edge |

The following classes are adjudicated separately and do not change the two-consumer result:

- OCP-004 and OCP-008 are upstream inputs, not downstream consumers.
- OCP-000/OCP-002 and the foundation map are registry/taxonomy/topology projections, not semantic consumers.
- AD-011/012/013/020/023–030 cite Event evidence or boundaries for discovery; they are not primary OCP consumers.
- P-001 lists OCP-010 as an invoker but is the consumed form contract, not a reverse document consumer.
- `rules.yaml`, `event.py`, seventeen Event fixtures and tests are executable evidence owned by OCP-010, not a third primary consumer.
- README, roadmap and backlog references are current accounting only.
- immutable reviewed snapshots remain historical evidence and are not current primary consumers.

## 6. Stable-surface classification rule

Each current OCP-010 element receives exactly one discovery disposition:

- **candidate** — already Accepted semantics with an identifiable owner, current consumer need and executable or explicit invariant evidence;
- **moving** — an intentionally open owner/model/representation or a legacy seam whose future treatment is not selected;
- **historical/accounting** — Board record and PATCH history, preserved but not a semantic compatibility surface.

“Candidate” does not mean selected or frozen. A later reassessment must compare complete outcomes and a separate Board act must select one.

## 7. Candidate stable surface

| ID | OCP-010 elements | Candidate guarantee | Evidence and consumer relevance |
|---|---|---|---|
| EVENT_IDENTITY_KERNEL | §§1, 4–5, 8, 15–16 | one stable non-empty `event_id`; kind/time/label/source/order do not replace identity; exact fail-closed resolution | OCP-011 uses `event@1`; OCP-017 relies on independent occurrence; checker enforces identity and reference failures |
| OBSERVATION_RECORD_KERNEL | §§6, 9, 15–16 | separate attributable identity, optional exact Event link, unresolved linkage without hidden Event, history-preserving acyclic supersession | OCP-011 uses `observation-record@1`; current fixtures preserve zero/many/conflicting observations |
| P001_OBSERVATION_BINDING | §§7 and 20 | exact `P-001@0.1.0` for ObservationRecord only, with endpoint/provenance/authority/supersession boundary | Pattern bytes and binding remain unchanged; no Pattern is inherited by Event |
| CROSS_DOMAIN_NON_IMPLICATIONS | §§3 and 10–13, 19, 21 | Event/Observation does not imply lifecycle transition, achievement, Conflict, Risk, Capability, Readiness, State, authorization or truth | both direct consumers depend on these separations; no graph edge or authority transfer is required |
| EXECUTABLE_REFERENCE_BOUNDARY | §§8–9, 16–17 plus checker rules | 34 validation IDs, `resolve_event`, `observations_for_event` and seventeen synthetic Event fixtures witness the finite current identity/reference boundary | proves existing behavior only; it cannot decide owners for moving surfaces |

This is the narrowest current positive candidate. It is larger than `event_id` alone because both direct consumers require Observation/evidence and non-implication guarantees. It is smaller than the whole document because §14 and four open §22 surfaces remain moving.

## 8. Moving surface

| ID | Current evidence | Why it stays moving | What a later act would have to supply |
|---|---|---|---|
| TEMPORAL_EXTENSION | optional `occurred_at`; no interval, uncertainty, timezone policy or canonical temporal model; §22 question open | an instant-validity check cannot select a general temporal model | named owner, representation, compatibility and replay rule |
| OPERATION_EVENT_RELATION | §10 preserves zero/one/many relevance and no edge; §21/§22 leave relation-record owner open | adding a relation/edge would change topology and ownership | separate OCP-016 route, owner, cardinality, authority and migration |
| EVENT_CORRELATION | identity resolution is exact; automatic dedup is denied; domain candidate linkage is open | correlation may propose linkage but cannot mutate Core identity | domain owner, proposal record/rule, evidence and rejection/replay semantics |
| EVENT_KIND_GOVERNANCE | kind refs must be versioned, but canonical Event taxonomy/registry is absent | exact syntax does not establish a Core vocabulary owner | legitimate registry/profile owner and admission route |
| LEGACY_ASSESSMENT_ENVELOPE | §14 still defines a checker-local envelope and denial of AB-056 authority; OCP-011 is now Accepted | keeping the negative scenario is useful, but the local shape overlaps the current normative owner and cannot enter a whole-document freeze unclassified | preserve as explicitly legacy test envelope, migrate scenario to OCP-011, or remove local shape with equivalent fail-safe evidence |

Board/PATCH history in §§24–25 stays byte-preserved historical/accounting evidence. It neither belongs to the candidate semantic kernel nor requires normalization in this act.

## 9. Outcome-fair discovery comparison

The following treatments are compared under the same axes: owner uniqueness, exact dependency truth, consumer compatibility, topology preservation, executable falsifiability, migration cost, rollback and no self-supplied lifecycle authority.

| Outcome | Benefit | Cost / stop | Discovery result |
|---|---|---|---|
| Y0 — hold without a candidate | makes no compatibility claim | discards an already Accepted and executable identity/Observation kernel, leaving the reassessment without a bounded positive option | admissible fail-safe, not leading |
| YW — whole OCP-010 freeze | one simple document boundary | would freeze unresolved relation/time/correlation/kind ownership and the legacy assessment envelope; conflicts with exact open questions | blocked |
| YK — bounded in-place kernel | preserves the five §7 candidate surfaces and leaves all five §8 surfaces explicit/moving under one readable owner | later remediation must make the kernel/deferred boundary explicit and prove OCP-011/OCP-017 compatibility | **leading candidate for later reassessment; not selected** |
| YC — consumer-defined surface | exact current consumers define only what they use | their document dependencies are unversioned and OCP-017 has no exact record-kind token; consumer intersection is too weak to own Event semantics | insufficient alone |
| YX — extracted stable contract | could isolate stable bytes | creates artifact-home, reference and possible duplicate-owner migration with no current consumer demand | not justified on current evidence |

YK leads because it preserves Accepted meaning without pretending the moving seams are resolved. This is a discovery conclusion only. It creates neither a post-discovery recommendation nor Board selection.

## 10. Named blockers and consumer cost

Four blockers must remain visible:

1. **UNRESOLVED_OPERATION_EVENT_OWNER** blocks a whole-document freeze. The current no-edge boundary is stable candidate evidence; a positive relation owner is not.
2. **LEGACY_ASSESSMENT_ENVELOPE_OVERLAP** blocks a whole-document freeze. OCP-011 is Accepted, while OCP-010 §14 still owns a checker-local shape and legacy AB-056 wording.
3. **UNVERSIONED_PRIMARY_CONSUMER_BINDINGS** requires explicit compatibility evidence. OCP-011 exact-binds record kinds but neither consumer exact-binds OCP-010 `0.2.1`; OCP-017 has no exact Event record-kind token.
4. **NEXT_LIFECYCLE_GATES_ABSENT** blocks promotion even after this discovery: post-discovery reassessment and candidate-specific Board selection remain absent.

The bounded consumer cost of any later YK remediation is:

- OCP-011 must retain `event@1`/`observation-record@1` meanings, exact evidence/time bindings and non-positive behavior for insufficient evidence;
- OCP-017 must retain independent Event occurrence/provenance and the no-generation/no-causation/no-reverse-edge boundary;
- current Event rule IDs, two derivations and seventeen fixtures need compatibility or explicit migration evidence;
- the P-001 binding must remain exact or change only through a separate Pattern-version act; and
- any treatment of §14 must preserve `Completed ≠ achieved` and conflicting-evidence fail-safe behavior while leaving normative assessment ownership in OCP-011.

No current data or production consumer inventory exists in this repository. The cost is therefore a contract/test migration obligation, not evidence that any production migration is safe.

## 11. Executable discovery evidence

`architecture/event-stable-surface.yaml` records the subject, seven inputs, two direct consumers, exactness classification, five candidate surfaces, five moving surfaces, four blockers, two remaining gates and five forbidden outcomes. `event_stable_surface.py` independently derives current frontmatter, finds the complete primary-consumer set, checks exact record refs and requires every literal evidence token.

Seven new unit tests take the exact repository command from **252 → 259** while fixtures remain **274**. The technical mandate carried 258 as baseline, but `python3 -m unittest discover -s tools/ontology_checker/tests -p 'test_*.py'` on exact base reproduces 252; proposed 259 exceeds both the measured base and the carried floor.

The exact mandated test name `test_every_defensive_value_is_individually_fixture_and_mutation_live` covers every value in eight defensive collections: seven dependency IDs, two consumer IDs, three binding kinds, five stable-surface IDs, five moving-surface IDs, four blocker IDs, two remaining-gate IDs and five forbidden outcomes. Separate attacks mutate every subject lifecycle field, each dependency, each consumer/record binding, every declared evidence token and all three self-supply routes. No test obtains its expected collection from the production constant it attacks.

The existing promotion-gate witness changes only current sequence truth: Y10D becomes complete, while `POST_DISCOVERY_REASSESSMENT` and `CANDIDATE_BOARD_SELECTION` remain required and `promotion_selections` remains empty. It still rejects OCP-010 becoming Canonical without selection.

## 12. Version, footprint and protected bytes

AD-031 begins at `0.1.0 / Discovery`. This is a new evidence/comparison artifact, not a version change to OCP-010 or any semantic contract. No `Accepted` or `Canonical` status is created.

The intended footprint is:

- new AD-031, evidence map, checker module and seven tests;
- the existing promotion-gate map/module/test updated from absent Y10D to completed Y10D with two gates still absent;
- `check.py` and checker guide integration; and
- README, roadmap and AB-062 accounting text with AB-062 status unchanged.

OCP-000, OCP-002, Concept taxonomy, graph, foundation map, P-001, every reviewed snapshot, every OCP body/version/status, every Concept status, every AB status, existing rule manifest, Event module and all 274 fixtures remain byte-identical. Event remains `Accepted`; OCP-010 remains `0.2.1 / Draft`.

## 13. Migration, rollback and stop conditions

This discovery performs no stored-record, API, schema, reference, graph, Pattern, fixture or consumer migration. It records future costs only.

Rollback removes AD-031/map/module/tests/check integration, restores promotion-gate Y10D state to absent and restores accounting as one reviewed unit. Partial rollback is invalid: a completed gate without the discovery evidence would self-supply completion; discovery prose without the executable map would overstate reproducibility.

Return to Y0 if the current primary-consumer sweep ceases to reproduce two documents, any direct input differs, OCP-010/Event lifecycle changes, P-001 ceases exact binding, a relation edge appears, OCP-011 stops owning normative assessment, evidence tokens drift, or a later act treats YK as selected.

## 14. Shortest lawful continuation and exact-head gates

After this act merges, the shortest lawful continuation remains two separate links before any promotion proposal:

1. a separately mandated post-discovery reassessment compares Y0/YW/YK/YC/YX and then-current alternatives against this evidence; its recommendation is not selection;
2. a separate Architecture Board act selects at most one exact candidate/remediation surface with compatibility, migration and rollback terms;
3. only a later separately mandated lifecycle proposal may edit OCP-010 status, and only if every then-current prerequisite passes.

AD-031 itself requires exact-head Fable review, explicit Codex adjudication, green CI on the same head and fresh Pavlo merge authorization naming that head. Any head change resets all four gates. Merge accepts discovery evidence only; it does not authorize the next act by implication.
