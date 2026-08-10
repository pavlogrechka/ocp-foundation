---
Decision-ID: AD-027
Title: Constraint Application Order, Override and Contextual Waiver Boundaries
Version: 0.1.0
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-004, OCP-006, OCP-007, OCP-016, OCP-018
Applies-To: AB-036
---

# AD-027 — Constraint Application Order, Override and Contextual Waiver Boundaries

## 1. Decision

The Board selects three separate Route C owner-local negative boundaries inside OCP-006:

- **AN** — no normative Constraint application order is established; complete-set admissibility remains permutation invariant;
- **ON** — one Constraint does not override another; and
- **WN** — no contextual waiver is established.

OCP-006 advances from `0.2.5` to `0.3.0 / Draft`; the `Constraint` Concept remains `Accepted`. AB-036 is Resolved only for these current negative boundaries. A positive precedence, override or waiver proposal requires separate reopening and subject-specific OCP-016 G4 evidence.

The three selections do not imply one another and cannot exchange rule references, request shapes or result labels.

## 2. Exact baseline and anchor chain

This act starts from exact `main@bfa5362847dd38ece318196b02217b715cadbed1`, tree `7c253e83fccd608f522bb31af3c5bacb16228bc2`. It does not reuse the merged PR #145 branch as a semantic baseline.

Each anchor was resolved at that commit, reverse-resolved to its path and SHA-256 checked over raw blob bytes.

| Input | Reverse-resolved path | Declared state at baseline | Git blob | SHA-256 |
|---|---|---|---|---|
| OCP-000 | `docs/000-operational-ontology/README.md` | `1.5.0 / Canonical`; no Policy, Authority, Approval, Exception or Waiver Concept | `7da7d7aad6ba505603cfbfa98ff1349c84892720` | `3f76ae4b55f01ce388bd865330f386c3ec0a6f6416e1aaed522145df96cfb7d6` |
| OCP-001 | `docs/001-ontology-governance/README.md` | `1.0.0 / Canonical`; Core Boundary review current | `33524fa3d18f3253faa9a854500be7ddfb20815f` | `da74645aa4f3cae10c7c59ae7b87abd1840544700e4a58e9efd3f6600a27f1cc` |
| OCP-002 | `docs/002-concept-taxonomy-and-relations/README.md` | `1.5.0 / Canonical`; no status projection for the forbidden candidate terms | `aaa4ac27a7d77c52b74833a1c088c037538f1f06` | `335f3e8c2f51110f192ceb608188437b6d2fe5b908bbf12894c31e45a651e7c6` |
| OCP-004 | `docs/004-operation-concept/README.md` | `1.0.0 / Canonical`; relation provenance/value gives no permission or precedence | `1ff548a1f213b574472a90a8b3cfe014f6c1ce11` | `9c9173d3a3dec044e2cae2eb8fd5b66d07a106318f497a973409fedf4677155b` |
| OCP-006 | `docs/006-constraint-concept/README.md` | `0.2.5 / Draft`, Constraint `Accepted`; AB-036 questions open in §22 | `5d7404717e500c66c0c017263678ae0a1a405c7d` | `e0469604b1d8e6c2156c35e85017129eaca1fb929633a8be0287af4ef67a88aa` |
| OCP-007 | `docs/007-organization-concept/README.md` | `1.1.1 / Canonical`; provenance label grants no precedence | `9b89bbac9ae08e73e2b8fbe1e85a5aec86824e33` | `eee22fbfb9580960101e9ced677625a02aec6368ccdacd2283a1b7e9946fd810` |
| OCP-016 | `docs/016-core-boundary/README.md` | `1.0.0 / Canonical`; Route C and G4 current | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| OCP-018 | `docs/018-operation-authorization-source/README.md` | `0.2.1 / Accepted`; named no-precedence/no-override boundaries and protected questions current | `dc3148869f47af2bb27eb2fa74a188136d5fb568` | `e105e9c230277b6865721192ef4044ee77d9bfbff73505d164d7760c8ac31779` |
| OCP-019 | `docs/019-conflict-derivation-boundary/README.md` | `0.1.0 / Draft`; Conflict establishment remains negative and separate | `092770b40541de5959c18b37664b179c7dcb7880` | `8689327a770eecccd40a7d43dd147659c24eb2e1dc0cd117dfe3e75114676bec` |
| OCP-020 | `docs/020-quantitative-constraint-input/README.md` | `0.2.0 / Accepted`; quantitative input does not grant precedence or waiver | `0e1e7d0947ab3c7d1c0355258651179f618636a2` | `1783c32094aee9f09ca50ececb12bf9ec8f3c6599590331dba3894ad727d9b5c` |
| OCP-021 | `docs/021-reservation-allocation-boundary/README.md` | `0.1.0 / Draft`; no Reservation/Allocation authority | `af96e2a9a67977cf5de8c4c566b1e9293e23687f` | `85cdc7e3bb5281a6b2fe0af4d11b31bc47040b762de5786a0a8a10c2e000f683` |
| P-001 | `patterns/P-001-identified-record-pattern.md` | `0.1.0 / Accepted`; optional form only when exact-invoked | `c679f3e35eb015aecf6cb9a839aacd75a432e844` | `2c9dd172a19c2d340b58a159fe5e71b64215a3968ee05fa330790b7e6359c797` |
| architecture backlog | `backlog/architecture-backlog.md` | AB-036 `Open` | `c3675c842860d005bbf8f545c79943a89d6721b1` | `c4fca6f3e878138148ca0350e16c2cd309b62728fcec72c1967acac445c2bfe9` |
| roadmap | `backlog/roadmap.md` | operational rules `31%`, machine enforcement `77%`, overall `≈72%` | `606b50f6ea3701d05a5e6e3a6203623f2ca04495` | `d7e2db71ea1d656cf8382a91cfb807527116258318de7eb9e828d9ba1fb91063` |
| checker dispatch | `tools/ontology_checker/ocp_checker/__init__.py` | existing dataset classes only; no Constraint interaction dispatch | `9c98755f3ec10449b5c0b1ee13d4f30b858d4974` | `a9c2b2235fa09dfe8ad1126ed4b280cd6a244ad99ee9dc504fd537186b3ba096` |
| direct fixture-coverage test | `tools/ontology_checker/tests/test_manifest_fixture_coverage.py` | complete manifests require direct validation-ID fixture coverage | `1a8321cbd394db568302ceb9a2c80be5e42695a9` | `1168905eda069766da62a43008a9b2ab7ed6fb68ffa7083246c2e149cc63ce51` |

The anchors identify inputs. They do not grant precedence, suppression, exemption, permission or production authority.

## 3. Predeclared inventory rule

The rule is fixed before applying it. OCP-000, OCP-001, OCP-002, OCP-016 and P-001 enter as governance/form controls. A semantic artifact enters when it owns Constraint/application/admissibility semantics; names precedence, priority, ordering, override, exception or waiver; contains a no-precedence/no-override boundary that could be disturbed; or is an Accepted candidate consumer whose protected operational result could independently require one of the three subjects. Every current primary OCP is listed even when excluded.

## 4. Complete current-artifact inventory

| Artifact | A — order | O — override | W — waiver | Adjudication |
|---|---|---|---|---|
| OCP-000 | control | control | control | registry remains unchanged; forbidden candidate terms gain no Concept row |
| OCP-001 | control | control | control | admission/non-implication governance only |
| OCP-002 | control | control | control | taxonomy projection remains unchanged |
| OCP-003 | excluded | excluded | excluded | Resource identity/quantity boundaries own no Constraint interaction result |
| OCP-004 | included boundary | excluded | excluded | §11.2 relation provenance/value grants no permission or precedence and no Constraint applicability |
| OCP-005 | included consumer check | included consumer check | included consumer check | Draft Assignment description names constraints but is not an Accepted G4 consumer for any positive result |
| OCP-006 | semantic owner | semantic owner | semantic owner | §§10–12 own applicability/evaluation/set decision; §22 asks the exact AB-036 questions |
| OCP-007 | included boundary | excluded | excluded | §9 provenance label grants no authority, continuity or precedence |
| OCP-008 | excluded | excluded | excluded | Objective statement contract owns no qualifying interaction need |
| OCP-009 | excluded | excluded | excluded | Capability identity does not establish a Constraint winner, suppression or exemption |
| OCP-010 | excluded | excluded | excluded | Event/Observation contract owns no qualifying result need |
| OCP-011 | included consumer check | included consumer check | included consumer check | Accepted assessment record consumes evidence but names no need for these operational effects |
| OCP-012 | excluded | excluded | excluded | CapabilityClaim contract owns holder evidence, not Constraint interaction |
| OCP-013 | included consumer check | included consumer check | included consumer check | Accepted interchangeability owns eligibility, but no positive A/O/W need or rule |
| OCP-014 | included consumer check | included consumer check | included consumer check | Accepted requirement profile owns directional eligibility, not A/O/W |
| OCP-015 | included consumer check | included consumer check | included consumer check | Accepted coordination workflow has no protected A/O/W result need |
| OCP-016 | gate/route control | gate/route control | gate/route control | G4 is applied separately before form selection |
| OCP-017 | included consumer check | included consumer check | included consumer check | Accepted Operation lifecycle owner does not consume any of the three results |
| OCP-018 | included boundary | included boundary | included consumer check | §§8, 11, 13 deny precedence/override shortcuts; §16 questions 3 and 6 remain OCP-018-owned |
| OCP-019 | included non-implication | included non-implication | included non-implication | Draft Conflict boundary forbids precedence/waiver coupling and supplies no positive consumer |
| OCP-020 | excluded | excluded | excluded | quantity input and neutral sum own no qualifying interaction result |
| OCP-021 | excluded | excluded | excluded | Draft reservation boundary supplies no Accepted positive consumer |
| P-001 | form control | form control | form control | identified-record form considered but not invoked by the selected inline negative boundary |

The inventory is complete by the declared rule, not by term frequency. Included consumer checks are allowed to fail; Accepted status does not transfer an unrelated need.

## 5. G4 first — application order

| Candidate capability | G4? | Exact-baseline result |
|---|---|---|
| deterministic implementation traversal with no semantic effect | no | implementation-local and outside this act |
| complete-set permutation-invariant negative boundary | no | creates no positive operational result; admissible for comparison |
| priority order that changes applicability, blocking effect or set decision | yes | closed: no Accepted consumer need, exact positive rule, protected snapshot/context or legitimate owner/evaluator |
| identified precedence record or profile | yes for its positive effect | same missing elements; identity/history need also absent |

No Accepted artifact in §4 names a protected need for a winner-selection result. The checker cannot act as consumer or evaluator.

## 6. G4 first — override

| Candidate capability | G4? | Exact-baseline result |
|---|---|---|
| negative non-establishment boundary over two exact Constraint inputs | no | creates no suppression; admissible for comparison |
| one Constraint suppresses applicability/evaluation/enforcement of another | yes | closed: all five G4 elements absent |
| convenience or stored override field | yes | closed and independently conflicts with OCP-018 §13's no-convenience-override boundary |
| identified override decision record/profile | yes | closed; object identity and consumer need absent |

OCP-006 remains the owner of Constraint effects, but ownership alone cannot self-supply an Accepted downstream consumer.

## 7. G4 first — contextual waiver

| Candidate capability | G4? | Exact-baseline result |
|---|---|---|
| negative non-establishment boundary over one exact affected Constraint input | no | creates no exemption; admissible for comparison |
| context-specific release from applicability, evaluation or blocking | yes | closed: all five G4 elements absent |
| waiver/exception/policy/approval record or profile | yes | closed; no admitted identity, consumer, rule or legitimate owner/evaluator |
| producer/caller bypass flag | yes | closed and fails the fail-safe non-implication boundary |

The words waiver and exception remain descriptive candidate labels only; this act creates neither Concepts nor records under those names.

## 8. Predeclared outcome criteria

| Criterion | Requirement |
|---|---|
| C1 — subject separation | A, O and W retain independent gates, rules, requests, results and reopening paths |
| C2 — complete-set truth | application-order result preserves §12 full-set `any`/`none` semantics and permutation invariance |
| C3 — G4 honesty | no positive-capable form self-supplies its consumer, rule, context/snapshot or owner/evaluator |
| C4 — owner fit | Constraint interaction stays owner-local to OCP-006 without competing with OCP-018 |
| C5 — named non-disturbance | every five-source boundary is stated and mechanically guarded where finite |
| C6 — fail-safe replay | missing, ambiguous, stale, cross-bound or malformed evidence returns `indeterminate` |
| C7 — form parsimony | no Concept, record identity, Pattern invocation or registry/graph change without evidence |
| C8 — coverage honesty | every declared finite value is individually proved or explicitly named category-only |

No criterion rewards closing AB-036, richer form, document order, term count, fixture count or green CI.

## 9. Outcome-fair comparison — application order

| Outcome | Intended benefit | Evidence against current selection | Result |
|---|---|---|---|
| A0 — no act | preserves current implicit set behavior | leaves the repeated no-precedence boundary unenforced and AB-036 unanswered | lawful, not selected |
| AP — positive priority relation/profile | deterministic winner selection across Constraint | G4 closed; conflicts with current no-precedence inputs absent explicit reopening | blocked |
| AR — identified precedence record | auditable priority history/provenance | no independent identity/history need or Accepted consumer; G4 closed | blocked |
| AI — implementation traversal | deterministic computation | cannot own shared semantic truth and would be unsafe if observable as result | implementation-only |
| **AN — Route C negative order boundary** | makes permutation invariance and no semantic traversal executable | cannot answer a future legitimate priority need | **selected** |

## 10. Outcome-fair comparison — override

| Outcome | Intended benefit | Evidence against current selection | Result |
|---|---|---|---|
| O0 — no act | adds no suppression authority | leaves override question and convenience-field risk unbounded | lawful, not selected |
| OP — positive override rule | expresses one Constraint suppressing another | G4 closed; semantics could alter applicability, enforcement and decision | blocked |
| OR — identified override decision record | preserves attributable suppression history | no identity/consumer evidence; G4 closed | blocked |
| OS — encode override as supersession | reuses existing lineage | supersession does not Retire automatically and cannot mean contextual suppression | rejected |
| **ON — Route C negative override boundary** | exact two-input proof that no override is established | cannot authorize a future true override | **selected** |

## 11. Outcome-fair comparison — contextual waiver

| Outcome | Intended benefit | Evidence against current selection | Result |
|---|---|---|---|
| W0 — no act | avoids new exemption vocabulary | leaves an explicit OCP-006 question and bypass risk open | lawful, not selected |
| WP — positive contextual-waiver profile | governed context-specific exemption | G4 closed and no legitimate owner/evaluator or admitted object form | blocked |
| WR — identified Waiver/Exception record | auditable identity, provenance and history | independent identity need absent; would introduce a forbidden candidate form | blocked |
| WE — enforcement flag extension | colocates exception with Constraint | changes established enforcement semantics and can silently become permissive | rejected |
| **WN — Route C negative waiver boundary** | exact proof that context/reference alone creates no exemption | cannot answer a future legitimate waiver need | **selected** |

## 12. Route, owner and form

AN, ON and WN are Route C Core non-Concept rules because they preserve shared Constraint semantics without independent identity. OCP-006 is the exact semantic owner: it already owns applicability, evaluation, enforcement and `constraint_set_decision`, and its §22 asks both AB-036 questions.

A new OCP would create a competing Constraint-interaction owner. Route F lacks identity evidence; Route E lacks a named interoperability consumer/profile; Route D has no narrower named domain; Route I cannot own the shared negative truth. P-001 is not invoked because no identified record is selected.

The three rules share OCP-006 only because they constrain one owner's interaction surface. Shared placement does not merge their activation, result or future reopening.

## 13. Named non-disturbance adjudication

| Existing boundary | Preservation in this act |
|---|---|
| OCP-018 §8 — multiple source profiles provide no equivalence or precedence | `precedence_source_count` and cross-profile winner inference are forbidden; no profile order is created |
| OCP-018 §11 item 11 — timestamp, record order, source/issuer count, caller identity provide no precedence | each of the five named selectors is individually forbidden and mutation-proved |
| OCP-018 §13 authority row — convenience fields do not override derivation | `convenience_override` is individually forbidden and mutation-proved |
| OCP-007 §9 — provenance label grants no precedence | `precedence_provenance_label` is individually forbidden; provenance remains attribution only |
| OCP-004 §11.2 — relation provenance/value grants no permission or precedence and creates no Constraint applicability | `precedence_operation_relation_value` is individually forbidden; OCP-004 remains unchanged |
| OCP-018 §16 question 3 — multi-level expression without universal/list order | remains OCP-018-owned and unanswered; `operation_authorization_level_order` takeover is forbidden |
| OCP-018 §16 question 6 — stored/convenience inputs overriding authorization derivation | remains OCP-018-owned and unanswered; `operation_authorization_derivation_override` takeover is forbidden |

Thus OCP-018's two questions are protected inputs, not AB-036 outputs. This act cannot be cited as their resolution.

## 14. Selected OCP-006 contract

OCP-006 §27 defines one strict `ConstraintInteractionDataset` with exact request and current `ConstraintApplicationInput` references. It exposes three derivations:

- `derive_constraint_application_order_boundary` under `constraint-application-order-boundary@1`;
- `derive_constraint_override_boundary` under `constraint-override-boundary@1`; and
- `derive_contextual_waiver_boundary` under `constraint-waiver-boundary@1`.

Their only valid non-indeterminate results are respectively:

- `constraint_application_order_not_established`;
- `constraint_override_not_established`; and
- `contextual_waiver_not_established`.

The harness exact-resolves selected opaque Constraint version pointers and binds one context/snapshot. Its `current` marker is a structural fixture assertion, not authenticated freshness, and it does not prove that a caller supplied every applicable Constraint; full-set completeness remains an upstream §12 precondition. It neither revalidates upstream Constraint records nor mutates applicability, evaluation, enforcement, lifecycle or set decision.

## 15. Executable evidence and exact coverage claim

The act adds one validator/derivation module, one complete-coverage manifest, dispatcher integration, seven focused tests and thirty-four fully synthetic fixtures. Three valid fixtures prove the three distinct negative outcomes. Thirty-one invalid fixtures cover structure, resolution, ambiguity, context/snapshot binding, staleness, self-targeting override, cross-result use and every named defensive value.

The finite defensive vocabulary contains exactly `20` values and all `20/20` have both an individual fixture and an individual mutation assertion:

- 7 precedence selectors;
- 1 convenience override field;
- 2 protected OCP-018 takeover fields;
- 7 waiver/exception/bypass/forbidden-Concept fields; and
- 3 positive result labels.

No defensive-list value is category-only. The tests additionally remove every interaction kind, rule mapping, negative result mapping, request field, input field, dataset field and evidence state in turn. The coverage claim does not extend to arbitrary lexical synonyms or production payloads.

The suite grows from `224` to `231` tests and from `205` to `239` fixtures. Counts are necessary regression evidence, not authority.

## 16. Backlog and adjacent decisions

- **AB-036 — Resolved:** only AN, ON and WN are selected; any positive branch must explicitly reopen it.
- **AB-025 and AB-037 — Resolved and unchanged:** no reservation, allocation, quantity or capacity decision is reopened.
- **AB-018, AB-005 and AB-002 — Open and unchanged:** no Conflict, Risk or Order model is inferred.
- OCP-018 §16 questions 3 and 6 remain with OCP-018.

OCP-000, OCP-002, the dependency graph and generated foundation map remain byte-identical. Policy, Authority, Approval, Exception and Waiver are not introduced as Concepts. OCP-019, OCP-020, OCP-021, P-001 and reviewed snapshots remain byte-identical. No `Review-After` field changes.

## 17. Version, migration, rollback and safety

AD-027 is `0.1.0 / Accepted` because it is the first Board selection for this decision identity. OCP-006 `0.2.5 → 0.3.0` is MINOR: three additive owner-local negative rules change the current semantic boundary without breaking existing Constraint records. OCP-006 remains `Draft`; `Constraint` remains `Accepted`.

No existing Constraint, EvaluationRecord, Operation authorization record or consumer migrates. The new dataset is optional executable evidence. Rollback removes AD-027, OCP-006 §27, the manifest/module, thirty-four fixtures, seven tests and synchronized accounting, restores OCP-006 `0.2.5` and AB-036 Open, and cannot introduce a positive result.

All fixtures are synthetic and contain only abstract `SYNTH` references. They contain no real magnitudes, frequencies, coordinates, geometry, sectors, time windows, callsigns, organization/unit designators, personal data, credentials or material from another project on this machine.

## 18. Exact-head gates

This act is the first of four gates. Merge requires Fable external review on one exact head, Codex adjudication, green required CI on that unchanged head and fresh explicit Pavlo authorization naming it. Any content-changing commit invalidates prior review, CI and authorization.

Preparation and external review do not authorize merge, production behavior, a positive A/O/W model, OCP-018 question resolution, Y10D, a normative `Review-After` act, YR or T6. No next act begins without its own mandate.
