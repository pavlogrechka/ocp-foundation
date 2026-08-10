---
Decision-ID: AD-026
Title: Reservation and Allocation Establishment Boundary
Version: 0.1.0
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-003, OCP-004, OCP-005, OCP-006, OCP-009, OCP-011, OCP-013, OCP-014, OCP-015, OCP-016, OCP-017, OCP-018, OCP-019, OCP-020, P-001
Applies-To: AB-025
---

# AD-026 — Reservation and Allocation Establishment Boundary

## 1. Mandate and decision

AB-025 asks whether Reservation is a fundamental Concept, an Assignment or Constraint specialization, or another governed form. The question has two independent branches: **E**, whole-Resource exclusivity and blocking of other Assignments, and **Q**, partial or quantitative reservation/allocation. This act derives and compares each branch separately.

The Board selects **EN** for E and **QN** for Q: one Route C non-Concept composition boundary with two different rules, derivations and result vocabularies. OCP-021 `0.1.0 / Draft` makes executable that an exact E evidence bundle or an exact Q bundle bound to Accepted OCP-020 still does not establish Reservation or Allocation authority. The result is negative authority, not a claim that reservation or allocation is absent in reality.

No positive model is selected. Merge fixes the Board selection and resolves AB-025 at this negative establishment boundary; later positive activation requires explicit reopening with new evidence and four fresh gates.

## 2. Exact baseline and anchor chain

The exact baseline is `main@d6c4fa334157d8fae7c3cc2f18ac084ab0ab4039`, tree `931b99c9b041e9e5ef275c9b1b1032d4e691ab46`. Each blob below was resolved at that commit, reverse-resolved through `git ls-tree -r` to the listed path, checked against the state declared inside the object and independently SHA-256 hashed from raw bytes.

| Artifact | Reverse-resolved path | Declared state | Git blob | SHA-256 |
|---|---|---|---|---|
| OCP-000 | `docs/000-operational-ontology/README.md` | `1.5.0 / Canonical`; no Reservation/Allocation/Capacity row | `7da7d7aad6ba505603cfbfa98ff1349c84892720` | `3f76ae4b55f01ce388bd865330f386c3ec0a6f6416e1aaed522145df96cfb7d6` |
| OCP-001 | `docs/001-ontology-governance/README.md` | `1.0.0 / Canonical`; governance and lifecycle | `33524fa3d18f3253faa9a854500be7ddfb20815f` | `da74645aa4f3cae10c7c59ae7b87abd1840544700e4a58e9efd3f6600a27f1cc` |
| OCP-002 | `docs/002-concept-taxonomy/README.md` | `1.5.0 / Canonical`; Reservation/Allocation remain an open question | `aaa4ac27a7d77c52b74833a1c088c037538f1f06` | `335f3e8c2f51110f192ceb608188437b6d2fe5b908bbf12894c31e45a651e7c6` |
| OCP-003 | `docs/003-resource-concept/README.md` | `1.0.0 / Canonical`; Resource identity excludes quantity/reservation | `71485bb337cfd59def2e0f1b18b474a7959bd30c` | `f8656769dd046f221843f627c746d0d6040c2e83c736b900370d60244fce8315` |
| OCP-005 | `docs/005-assignment-concept/README.md` | `0.2.6 / Draft`, Assignment `Accepted`; §13 boundary current | `6e78d6d54d53260fb42f4ef67776e3cf8b11daa7` | `fd77fbdc47d1d436a95c95c6a211521d65dd5261633ccd2eee17f9a761fef3ba` |
| OCP-006 | `docs/006-constraint-concept/README.md` | `0.2.5 / Draft`, Constraint `Accepted`; §§11–14 current | `5d7404717e500c66c0c017263678ae0a1a405c7d` | `e0469604b1d8e6c2156c35e85017129eaca1fb929633a8be0287af4ef67a88aa` |
| OCP-014 | `docs/014-coordination-profile/README.md` | `0.2.0 / Accepted`; reservation explicitly excluded | `23bd05b4bb14fd7a85101bd5a8b3dd733b53dd99` | `72c789c7b15ab2fd8997f60ba8cfd9d89f0e7730407763d18fb222bac5f06a8c` |
| OCP-016 | `docs/016-core-boundary/README.md` | `1.0.0 / Canonical`; G4 and non-transfer current | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| OCP-020 | `docs/020-quantitative-constraint-input/README.md` | `0.2.0 / Accepted`; neutral exact quantity input | `0e1e7d0947ab3c7d1c0355258651179f618636a2` | `1783c32094aee9f09ca50ececb12bf9ec8f3c6599590331dba3894ad727d9b5c` |
| P-001 | `patterns/P-001-identified-record-pattern.md` | `0.1.0 / Accepted`; binding only when invoked | `c679f3e35eb015aecf6cb9a839aacd75a432e844` | `2c9dd172a19c2d340b58a159fe5e71b64215a3968ee05fa330790b7e6359c797` |
| architecture backlog | `backlog/architecture-backlog.md` | AB-025, AB-018, AB-005, AB-002 and AB-036 `Open`; AB-037 `Resolved` | `4a3d1a102a88121490e0818fb925cb5553169a20` | `37fe29819ce35da18de6a7e93878580dbcbbe0917fb05895918968f95a1f678d` |

Anchors establish inputs only. They do not select a route, form or result.

## 3. Predeclared inventory criterion

The inventory rule is fixed before classification. OCP-000, OCP-001, OCP-002, OCP-016 and P-001 enter both branches as registry, governance, routing and form controls. A semantic artifact enters **E** when its current primary text owns or explicitly bounds Resource, Operation, Assignment or Constraint identity/effectivity; simultaneous-Assignment exclusivity, blocking or admissibility; a possible positive consumer/evaluator; or Reservation/Allocation form. It enters **Q** under the same rule plus quantity, unit, demand, consumption or capacity inputs/results. An explicit non-implication or deferment naming the branch counts as a boundary or consumer check. Every current primary OCP is listed even when excluded.

## 4. Complete current-artifact inventory

| Artifact | E classification | Q classification and reason |
|---|---|---|
| OCP-000 | control | control; registry has no Reservation, Allocation or Capacity row |
| OCP-001 | control | control; governance and ambiguity stop rules only |
| OCP-002 | control | control; Assignment/Constraint are projected and Reservation/Allocation remain open |
| OCP-003 | included | included; Resource identity permits several Assignments while amount, consumption and reservation stay external |
| OCP-004 | included | included; Operation participation binds Assignment and defers simultaneous-use admissibility to Constraint, but owns no reservation result |
| OCP-005 | included | included; Assignment expressly creates neither exclusive reservation, blocking of other Assignments nor reserved quantity |
| OCP-006 | included | included; owns exact Constraint evaluation, working exclusive-Assignment and capacity-limit patterns, not Reservation authority |
| OCP-007 | excluded | excluded; Organization identity and relations provide no qualifying result or consumer |
| OCP-008 | excluded | excluded; Objective owns intent, not task allocation or reservation |
| OCP-009 | excluded | included boundary; Capability is not current capacity and supplies no capacity/reservation consumer |
| OCP-010 | excluded | excluded; occurrence and observation do not own either branch result |
| OCP-011 | excluded | included boundary; assessment is a result-form precedent but does not establish availability or reservation |
| OCP-012 | excluded | excluded; claim evidence is not availability, Assignment eligibility or reservation |
| OCP-013 | consumer check | consumer check; Accepted interchangeability excludes capacity, reservation, selection and Assignment mutation |
| OCP-014 | consumer check | consumer check; Accepted coordination requirement excludes capacity, reservation, allocation and Assignment mutation |
| OCP-015 | consumer check | consumer check; workflow confirmation is not selection, reservation, allocation or Assignment mutation |
| OCP-016 | control | control; G4 is decided before form selection |
| OCP-017 | consumer check | consumer check; lifecycle alignment does not mutate Assignment or establish availability |
| OCP-018 | boundary | boundary; authorization-source results cannot become selection or Assignment mutation |
| OCP-019 | boundary | boundary; negative Conflict derivation preserves OCP-006 refs and supplies no reservation consumer |
| OCP-020 | boundary; E is quantity-independent | accepted input plus boundary; closes only Q input status and forbids sufficiency/reservation inference |
| P-001 | form control | form control; no invocation without independent record identity |

The set is evidence-led rather than term-frequency-led. Each included artifact supplies a governing boundary or tests a possible consumer; each exclusion fails the declared criterion by name.

## 5. Branch E gate before form

A positive E rule that establishes whole-Resource reservation, Allocation, exclusivity permission or blocking of other Assignments is positive-capable under OCP-016 G4. The exact baseline has no complete activation tuple:

| G4 element | E result |
|---|---|
| concrete Accepted consumer | absent; OCP-005/OCP-006 primaries are Draft and Accepted OCP-013–OCP-017 own different results or exclude reservation |
| consumer baseline and protected result need | absent; AB-025 is a question, not an operational consumer contract |
| versioned positive rule | absent; OCP-006 §14.1 is a working pattern and generic blocking is not an admitted reservation activation |
| exact input snapshot and evaluation context | generic fields exist, but no Accepted E activation binds one |
| legitimate owner/evaluator | absent; document ownership and an opaque evaluator reference do not establish operational legitimacy |
| object-form decision | absent; neither projection, identified record nor Concept form is admitted |

E is therefore G4-closed for every positive form. A negative boundary may proceed because it grants no reserved, allocated, available, permitted or lifecycle-changing result.

## 6. Branch Q gate before form

Q is evaluated independently. OCP-020 `0.2.0 / Accepted` supplies the exact quantitative-input prerequisite, but OCP-020 §§9–10 and §16 say that exact totals remain neutral and that every positive capacity/reservation activation still needs G4.

| G4 element | Q result |
|---|---|
| concrete Accepted consumer | absent; no Accepted artifact owns a protected quantitative reservation/allocation result |
| consumer baseline and protected result need | absent |
| versioned positive rule | absent; `exact-unit-quantity-sum@1` is neutral arithmetic, not sufficiency or reservation |
| exact activation snapshot and context | OCP-020 defines an input shape, but no Accepted consumer activation binds an instance |
| legitimate owner/evaluator | absent; profile ownership is attribution, and OCP-006 cannot self-supply as upstream definition |
| object-form decision | absent |

Q is G4-closed independently of E. Accepted OCP-020 removes one prerequisite and does not transfer a consumer, rule, owner or object form.

## 7. Predeclared outcome criteria

| Criterion | Requirement |
|---|---|
| C1 — branch separation | E and Q retain independent gates, rule refs, results and reopening paths |
| C2 — G4 honesty | no positive-capable form self-supplies consumer, rule, owner/evaluator or object form |
| C3 — owner fit | Assignment, Constraint and quantitative input keep their existing responsibilities |
| C4 — distinct responsibility | selected work must add a non-duplicative cross-artifact invariant |
| C5 — fail-safe replay | missing, ambiguous, stale or cross-bound evidence returns `indeterminate` |
| C6 — form parsimony | no Concept or identified-record identity without independent evidence |
| C7 — executable falsifiability | every finite rule has direct fixtures and tests, including valid declared-but-unused elements |
| C8 — non-implication | no availability, sufficiency, permission, authorization, lifecycle, Risk or Conflict result |

No criterion rewards closing AB-025, prior recommendation, document centrality, fixture count or green CI.

## 8. Outcome-fair comparison — branch E

| Outcome | Intended benefit | Evidence against current selection | Result |
|---|---|---|---|
| E0 — introduce nothing | preserves every existing owner and gate | leaves the three-document question non-executable | lawful, not selected |
| EF — recommend fundamental Concept | independent identity could support history and relations | no identity, lifecycle, reference or consumer evidence; registry act is separately gated | rejected now |
| EA — Assignment specialization | colocates participation and exclusivity | OCP-005 expressly separates Assignment from reservation/blocking; positive form is G4-closed | blocked |
| EK — Constraint specialization | fits forbidden-overlap evaluation | proves only a governed violation/block; absence of block cannot establish reservation or availability | useful input, insufficient answer |
| EC — governed positive non-Concept contract | smallest positive projection or record | no Accepted consumer, exact positive rule, owner/evaluator or object form | blocked |
| **EN — Route C negative composition boundary** | makes Assignment refs plus optional ConstraintEvaluation refs insufficient for reservation/allocation authority | cannot answer whether a future reservation exists | **selected** |

EN is not a duplicate of OCP-005 or OCP-006. Those documents separately own Assignment non-implication and Constraint evaluation. EN owns the cross-artifact composition invariant: even their exact references in one current Resource/context snapshot do not manufacture reservation or allocation authority.

## 9. Outcome-fair comparison — branch Q

| Outcome | Intended benefit | Evidence against current selection | Result |
|---|---|---|---|
| Q0 — introduce nothing | leaves neutral OCP-020 untouched | does not make the combined Assignment/Constraint/quantitative inference executable | lawful, not selected |
| QF — recommend fundamental Concept | could support independent quantity/reservation identity | no identity/history/consumer evidence; registry act is separately gated | rejected now |
| QA — Assignment specialization | colocates reserved amount with participation | OCP-005 explicitly leaves quantity outside Assignment; positive form is G4-closed | blocked |
| QK — Constraint specialization | natural later home for demand-versus-limit evaluation | OCP-006 is upstream and cannot self-supply an Accepted consumer; positive rule absent | blocked |
| QC — governed positive non-Concept contract | could project sufficiency/reservation without Concept identity | consumer, rule, owner/evaluator and object form are absent | blocked |
| **QN — Route C negative composition boundary** | exact-binds Accepted `OCP-020@0.2.0` and its snapshot while refusing reservation/allocation inference | supplies no positive capacity or reservation answer | **selected** |

QN extends rather than duplicates OCP-020. OCP-020 owns quantitative validity and neutral totals; QN owns the separate composition invariant that exact quantitative input combined with Assignment and Constraint references still confers no reservation or allocation authority.

## 10. Separate selections and non-transfer

E and Q share a document only because the unresolved responsibility is one cross-artifact establishment boundary. They do not share an activation:

- E uses `whole-resource-reservation-allocation-boundary@1`, forbids quantitative coupling and has E-specific negative results;
- Q uses `quantitative-reservation-allocation-boundary@1`, requires exact `OCP-020@0.2.0` plus a quantitative snapshot reference and has Q-specific negative results;
- one branch's result label, rule, evidence or future consumer cannot satisfy the other branch; and
- a caller-declared complete G4 tuple remains self-supply and returns `indeterminate` in both branches.

## 11. OCP-016 authority ledger

| Ledger field | Decision |
|---|---|
| Candidate | EN and QN negative establishment boundary |
| Operational responsibility | preserve the absence of reservation/allocation authority across composed Resource, Assignment, Constraint and quantitative evidence |
| Route | C, Core non-Concept |
| Semantic owner | OCP-021 for the composition boundary only |
| Consumers | reservation/allocation review and audit; neither is a positive G4 activation consumer |
| Defining sources | OCP-005 §13, OCP-006 §§11–14, OCP-020 §§9–10 and 16 |
| Exact dependencies | OCP-003, OCP-005, OCP-006, OCP-016 and OCP-020 |
| Evidence | two derivations, exact manifest, focused tests and fully synthetic fixtures |
| Non-implications | no Concept, record identity, P-001, availability, sufficiency, permission, Assignment mutation, Risk, Conflict or authorization |
| Lifecycle/migration | new `0.1.0 / Draft`; zero migration |

Route F fails for absent independent identity. Route E lacks a named interoperability consumer/profile. Route D cannot own a boundary shared across Assignment, Constraint and quantitative input. Route I cannot own semantic truth. A separate Route C document avoids amending Canonical or existing defining documents.

## 12. Selected Draft contract

OCP-021 owns a strict `ReservationBoundaryDataset`: one request exact-resolves a current Resource/context snapshot containing at least one Assignment reference, zero or more ConstraintEvaluation references and, for Q only, an exact quantitative snapshot reference. References are opaque exact pointers; OCP-021 neither redefines nor revalidates upstream record truth.

Four branch/action results are deliberately distinct:

- `whole_resource_reservation_not_established`;
- `whole_resource_allocation_not_established`;
- `quantitative_reservation_not_established`; and
- `quantitative_allocation_not_established`.

Every invalid, stale, ambiguous, cross-bound, cross-branch, self-supplied or positive-authority input yields only `indeterminate`.

## 13. Executable evidence and completeness

The tree adds one checker module, one complete-coverage manifest, dispatcher export, six focused unit tests and twenty-one fully synthetic fixtures. Four valid fixtures cover every E/Q × reservation/allocation combination, both empty and non-empty ConstraintEvaluation reference lists, and the exact Q prerequisite. Seventeen material negatives cover malformed envelopes and requests, invalid branch/action, malformed/unresolved/ambiguous snapshots, binding mismatch, stale evidence, E/Q coupling errors, missing/wrong OCP-020 binding, positive authority, complete caller self-supply for each branch, forbidden adjacent coupling and stored-result crossover.

Mutation tests remove every branch, action, rule mapping, result mapping, exact OCP-020 reference and required request/snapshot field in turn; each change makes an otherwise valid fixture fail. This directly prevents the unused-declared-element gap found in PR #143. The suite grows from `218` to `224` tests and from `184` to `205` fixtures.

## 14. Backlog disposition

AB-025 is Resolved as the Board selection of EN and QN negative establishment boundaries. Resolution means only that current exact evidence does not establish reservation or allocation authority and that no fundamental Concept or positive object form is selected. A later positive proposal must explicitly reopen AB-025 with new G4 evidence.

AB-037 remains Resolved. AB-018, AB-005, AB-002 and AB-036 remain Open and unchanged. OCP-019 remains `0.1.0 / Draft`; OCP-020 remains `0.2.0 / Accepted`.

## 15. Version, migration, rollback and safety

AD-026 is `0.1.0 / Accepted` because merge would be the first Board comparison and selection for both AB-025 branches. OCP-021 is `0.1.0 / Draft`, the first pre-canonical version of a new non-Concept contract; PATCH/MINOR classification does not apply and Accepted/Canonical would overstate absent positive-consumer evidence.

No Resource, Assignment, Constraint, quantitative input, production profile or stored record migrates. No Concept, Concept status, registry row, taxonomy projection, graph edge, foundation-map entry, P-001 invocation or `Review-After` changes. Rollback removes AD-026, OCP-021 and its executable evidence, restores AB-025 Open and reverses accounting atomically.

All fixtures contain only abstract `SYNTH` references. They contain no magnitudes, unit names, coordinates, geometry, sectors, windows, callsigns, organization/unit identifiers, personal data, credentials, keys, tokens or material from another project.

## 16. Exact-head gates

Merge requires Fable external review on one exact head, Codex adjudication, green required CI on that same head and fresh explicit Pavlo authorization naming it. Preparation, review, CI and this proposed decision text do not authorize merge, production use or a next act.
