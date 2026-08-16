---
Decision-ID: AD-041
Title: Route D Resource Occupancy Scope
Version: 0.1.0
Status: Accepted
Owner: Architecture Board
Depends-On: AD-015, AD-036, OCP-001, OCP-003, OCP-005, OCP-016
Applies-To: OCP-023
Review-After: OCP-023 has an externally reviewed exact body and one legitimate Accepted consumer activation binding
---

# AD-041 — Route D Resource Occupancy Scope

## 1. Decision and exact boundary

The Architecture Board selects the minimum domain-local scope: one Resource-occupancy statement at one instant, derived from current Assignment truth and carrying every effective Assignment reference as evidence. OCP-023 `0.1.0 / Draft` prepares that exact Route D contract and a synthetic executable reference.

The decision does not create a Concept, change Core, activate the positive result or admit Conflict, priority, capacity, reservation, allocation, permission, authorization, lifecycle mutation or action recommendation. `not Core` is a valid OCP-016 routing result, not a defect.

## 2. Exact baseline and full anchor chain

The act starts from exact `main@5d60bfc4ba96f49382383d487d26ef971c4a0cde`, tree `33a3b7e39b5c59d76c5437f134f9af8fb237c2c7`. Each object below was resolved as `baseline:path → blob`, reverse-resolved through `git ls-tree -r`, checked against the state declared inside the object and SHA-256 hashed from raw blob bytes. The claimed path equals the reverse-resolved path in every row.

| Input | Reverse-resolved path | Declared baseline state | Git blob | SHA-256 |
|---|---|---|---|---|
| OCP-003 | `docs/003-resource-concept/README.md` | `1.0.0 / Canonical`, Resource Concept `Canonical`; operational occupancy outside identity | `71485bb337cfd59def2e0f1b18b474a7959bd30c` | `f8656769dd046f221843f627c746d0d6040c2e83c736b900370d60244fce8315` |
| OCP-005 | `docs/005-assignment-concept/README.md` | `0.2.8 / Draft`, Assignment Concept `Accepted`; single-Assignment effectivity current | `6e6c00e723b15a348e7610d4ca5a1ae23526c52b` | `a9226f4f5e168b945ae743626e73ba5e25d67318b390869a493e5fd30bdaa065` |
| OCP-016 | `docs/016-core-boundary/README.md` | `1.0.0 / Canonical`; Routes F/C/E/D/I and G4 current | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| AD-036 | `architecture/discovery/AD-036-consumer-need-discovery.md` | `0.1.0 / Discovery`; no then-current eligible artifact had an unmet positive need | `3f8642777c16015226065f29f745b2e31bb6cd3a` | `564bc5c5b7d12c2be95278af6b3518a3af773ade701e3fee1dc4a9a4daac5603` |
| Assignment checker | `tools/ontology_checker/ocp_checker/checker.py` | per-Assignment validation/effectivity and Operation-filtered participation, no Resource-only set result or witness set | `120ada9dd00b1df0b46cf3060aef2b0c290948b1` | `3a093f0d76113bb5dd2799c7d0aaf73b51b752569dc13de145bb3d158a7b4a47` |
| Checker dispatch | `tools/ontology_checker/ocp_checker/__init__.py` | no ResourceOccupancy fixture class or derivation export | `cf7aec93f299a072075adce93ffe4bcb6a3c5c99` | `bd4b4a9be22e4d6e8f9c50bb4b11a6b68406d18fac7445b9aa1714da7c16763d` |

## 3. Measured starting surface

The inventory criterion is declared before application: a checker function enters when it accepts Assignment values and can answer current truth for more than one Assignment of the same Resource without requiring a particular Operation.

No current function qualifies. `assignment_effective_at` and `assignment_projections` each accept one Assignment. `derived_participates_in` accepts an iterable but additionally requires one `operation_ref`, returns only a boolean and exposes no complete Resource witness set. Two valid overlapping Assignments for the same Resource therefore remain independently effective with a green suite; no Resource-occupancy result exists.

This is a scope boundary, not an implementation defect in OCP-005.

## 4. Route comparison before form

Every route is compared on the same axes: semantic owner, Core impact, consumer breadth, G4 consequence and rollback.

| Option | Owner and Core effect | G4 / rollback | Disposition |
|---|---|---|---|
| F — new fundamental Occupancy Concept | adds identity and registry/graph work without independent identity evidence | widest migration; unjustified | rejected |
| C — Core non-Concept aggregate | makes one Resource-state interpretation shared Core truth | G4 still applies; exceeds minimum scope | rejected |
| E — governed extension/profile | no interoperability profile or cross-domain exchange need is present | owner form unsupported | rejected |
| D0 — domain-local unbounded occupancy, activated now | correct semantic locality but self-supplies consumer/completeness/owner evidence | violates G4 | rejected |
| D1 — domain-local Draft plus synthetic reference proof | named Resource-occupancy domain, Core unchanged, exact missing input and activation stop visible | removable without migration | selected |
| I — implementation only | code would own semantic truth without a governed document | invalid owner | rejected |

Route D owns only the domain-local statement. It does not prepare later Core transfer.

## 5. G4 before result form

Two questions are separate. Route D answers where the meaning belongs. G4 answers whether a positive-capable rule is active. OCP-016 §5 and AD-015 §35.2 make consumer activation route-independent: domain-local activation still exact-binds an Accepted consumer and legitimate owner/evaluator.

The chosen result contains `occupied=true`, so activation requires G4. The current tree has no exact Accepted occupancy consumer, baseline, protected need, complete Assignment-set input, owner/evaluator or activation context. OCP-023 is Draft and cannot self-supply them; Board governance authority does not become domain evaluation authority. The selected form is therefore a Draft definition plus synthetic reference implementation with activation fields mechanically forbidden.

## 6. Consumer-need derivation

AD-036's predeclared three-part test is reused, not weakened. The new statement is a current normative Draft claim rather than an eligible Accepted G4 consumer, names the exact positive input result `assignment_set_complete_for_resource`, and cannot discharge its Resource-wide false case without that result.

The necessity is asymmetric and executable:

- one effective Assignment is a sufficient positive witness;
- zero effective values in an arbitrary caller list are not sufficient negative evidence;
- a complete exact set plus zero effective values supports `occupied=false`.

Accordingly OCP-023 is the first concrete claimant of the missing input, but not yet the Accepted consumer that permits activation. This act does not manufacture the completeness result. Synthetic `SYNTH-COMPLETE-*` references prove only the proposed computation and are rejected as production authority by the explicit Draft boundary.

## 7. Exact one-statement contract

The selected reference rule consumes one exact Resource, evaluation instant and complete synthetic Assignment snapshot. It validates every Assignment using current OCP-005 truth, evaluates each with `assignment_effective_at`, returns one nullable boolean and retains all effective Assignment IDs as witnesses in identity order.

`None` is the fail-safe implementation state for malformed or unauthorised input; it is not a second semantic output. Multiple witnesses cannot establish Conflict or priority. An empty witness set cannot establish availability, capacity or permission.

## 8. Executable evidence and individual liveness

Six new fixtures cover zero, one effective, two overlapping, two non-overlapping, inclusive start and exclusive end. They are the minimum required semantic matrix and use only synthetic Resource, Operation, Assignment and UTC-time values.

The reference validator independently checks exact request/snapshot resolution, Resource binding, completeness evidence, OCP-005 validity, Assignment identity uniqueness, stored result/witness agreement, activation absence and every forbidden adjacent field. `test_every_defensive_value_is_individually_fixture_and_mutation_live` mutates each declared field, activation field, forbidden field, identifier and synthetic completeness prefix separately. A reversed two-witness input retains the same sorted witnesses, proving input order supplies no priority.

## 9. Status and version derivation

OCP-023 begins `0.1.0 / Draft`: it is a new OCP surface, so no revision delta exists; its exact text and evidence had no prior external review; the Board mandate selected scope rather than accepting an unwritten body; and G4 activation remains absent. Accepted would require a later explicit lifecycle action and AD-029 reviewed snapshot. Canonical is inapplicable to this initial domain-local proposal.

AD-041 begins `0.1.0 / Accepted`. It records the Board's explicit Route D scope selection and the non-activation boundary. Discovery would understate a supplied Board decision; no existing AD version is revised.

## 10. Accounting, migration, rollback and non-transfer

The act adds one Draft OCP, one accepted decision, one module, one manifest, one focused test file and six new fixtures. Current numeric accounting derives the resulting totals from live metadata and executable files. No existing fixture, OCP-000–OCP-022 byte, Pattern, snapshot, baseline witness, graph, foundation map or promotion-gate state changes.

The non-formula roadmap percentages remain `93 / 33 / 77 / ≈72`. A Draft reference proof with blocked activation does not by itself justify moving a Board readiness judgment; the descriptive rows now name the added capability and its stop.

No stored data migrates. Rollback removes only the added Route D unit and descriptive accounting. The three Assignment semantic blockers remain, `promotion_reachable` remains false, `EVENT_T6` remains the only completed cycle and `active_cycle_id` remains null.

Merge does not accept or activate OCP-023, create a Concept, select Assignment, start a cycle, open T7, resolve AB-018/AB-005 or authorize another act. Exact-head Fable review, Codex adjudication, green required CI and fresh explicit Pavlo authorization are mandatory and non-transferable.
