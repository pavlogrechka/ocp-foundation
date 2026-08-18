---
Decision-ID: AD-048
Title: Assignment Q2 Amendment-Model Sufficiency Attempt
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: AD-038, AD-044, AD-045, AD-046, AD-047, OCP-001, OCP-005, OCP-016, OCP-023
Applies-To: AB-026, OCP-005 §§5–7, 12, 14.6, 19.2
Review-After: A separately mandated amendment-model lifecycle proposal supplies a direct owner rule or an explicitly exhaustive rule from which one surviving Q2 class necessarily follows
---

# AD-048 — Assignment Q2 Amendment-Model Sufficiency Attempt

## 1. Conditional authority and exact result

This act tests whether current rules and invariants distinguish the two Q2 classes that survived AD-044 and AD-045. The conditional authority to edit OCP-005 exists only if the criterion in §3 passes.

It does not pass. Q2 remains open and `AMENDMENT_MODEL_ABSENT` remains a `blocks-whole-document-freeze` blocker bound exactly to `[Q2]`. OCP-005 remains byte-identical at `0.3.0 / Draft`; Assignment remains `Accepted`. Q5 and Q9, their blockers, every status, readiness statement, promotion candidate and promotion-cycle field remain unchanged.

This is a completed negative result. Direct owner text, enumerations and silence are each tested independently; none selects between `SUPERSEDING_ASSIGNMENT_FOR_CHANGE` and `POST_ESTABLISHMENT_IMMUTABILITY`.

## 2. Gate-first before result form

The insufficiency record is not positive-capable under OCP-016 G4. It adds no Assignment field, amendment transition, mutation permission, prohibition, provenance binding, result, profile or activation. Its form is therefore a Discovery AD, exact witness and executable guards.

The two hypothetical closures differ:

- `SUPERSEDING_ASSIGNMENT_FOR_CHANGE` is positive-capable. Making successor identity, linkage, provenance and replay mandatory would add a mechanism and requires G4 plus a separate lifecycle act.
- `POST_ESTABLISHMENT_IMMUTABILITY` is a pure negative prohibition and is not positive-capable under G4. It still requires a separately authorized Board lifecycle act because no current statement makes role or applicability immutable.

Accepted OCP-023 is a legitimate consumer, but it excludes only in-place amendment without an observation-cut binding. It does not select either survivor and cannot self-supply the missing amendment rule.

## 3. Sufficiency criterion declared before application

Q2 may close only if all five conditions hold:

1. one class is selected by a direct current owner statement or follows necessarily from an explicitly exhaustive normative enumeration;
2. current executable behavior distinguishes it from the alternative;
3. current Accepted-consumer evidence excludes the alternative;
4. AD-044 pressure and current norm intersect at exactly one Q2 class; and
5. finalization needs no new mutation prohibition, mandatory successor, provenance or replay rule.

Silence is never sufficient by itself. An enumeration is sufficient only when the norm marks it exhaustive for the exact semantic axis and the residual treatment follows necessarily. Traceability without an amendment model is not selection.

## 4. Calibration against Q3 and Q9

| Axis | Q3 at AD-046 | Q2 now | Q9 at AD-047 |
|---|---|---|---|
| owner selection | direct effectivity lower bound | direct traceability, model explicitly open | no closed-world cardinality boundary |
| executable discrimination | before/at `established_at` changes `false → true` | role and applicability replacements both remain valid | extra interval extension remains valid |
| Accepted-consumer exclusion | excludes both retroactive classes | excludes in-place amendment only; two classes remain | selects neither cardinality |
| survivor intersection | one shared prospective boundary | two change-model classes | two cardinality classes |
| new rule needed | no | yes | yes |

Q2 is stronger than Q9 because current text directly requires traceability and consumer pressure already removes in-place amendment. It remains below Q3 on every decisive closure axis: no owner selection, no executable discriminator, no consumer selection between the survivors, no unique intersection and no rule-free finalization. Neither neighboring conclusion is transferred by analogy.

## 5. Evidence by argument type

### 5.1 Direct normative statements

OCP-005 §14.6 directly says that any post-Establishment role or applicability change must be traceable. The same sentence directly says that the final amendment model remains open. This is enough to reject an untraceable in-place amendment, but it is compatible with both a traceable superseding Assignment and a prohibition on change.

OCP-005 §§5 and 14.2 make `resource_ref` and `operation_ref` immutable after Establishment and require a new Assignment for their replacement. Those statements do not name role or applicability. Extending endpoint immutability to different fields would add a rule. Direct statements therefore do not select either survivor and are insufficient alone.

### 5.2 Inference from enumeration

Section 6 enumerates a minimum verifiable contract, including optional `supersedes_assignment_ref`; it explicitly does not claim to be a database/API schema. Optional presence does not make supersession mandatory for role or applicability change.

Section 7.6 makes the listed paths exhaustive for lifecycle-stage transitions. It does not claim an exhaustive account of field-value mutation after Establishment. No residual amendment regime follows necessarily from either list. Enumeration inference is therefore insufficient alone.

### 5.3 Inference from silence

The absence of an amendment transition or amendment record proves only that no current positive amendment mechanism is defined. It does not prohibit changing the two fields and does not require a successor. Silence cannot select either survivor and is insufficient alone.

## 6. Executable behavior and survivor intersection

The existing valid Established Assignment is replayed. Two subject-specific mutations keep `assignment_id`, `transition_history`, `provenance_ref` and `supersedes_assignment_ref` unchanged while independently replacing `role_specification.role_code` and `applicability_end`. The current validator accepts the original and both mutations. This does not authorize in-place amendment; it proves that executable behavior does not distinguish supersession from immutability.

A rejection control replaces `role_code` with the invalid scalar `---` and receives `ASSIGNMENT_ROLE_REQUIRED`. The probe is therefore not relying on a validator that accepts every mutation.

AD-044 leaves exactly `SUPERSEDING_ASSIGNMENT_FOR_CHANGE` and `POST_ESTABLISHMENT_IMMUTABILITY`, both with `current-three-bindings-adequate`. AD-045 classifies both `underdetermined`, with `post_establishment_change_model` as the same unresolved axis and no violated statement. All six current Accepted consumers—OCP-013, OCP-015, OCP-017, OCP-020, OCP-021 and OCP-023—select neither. The intersection contains two classes, so the criterion fails.

## 7. Decision, projections and negative-branch guards

The conditional authority to edit OCP-005 is not exercised. Q2, Q5 and Q9 remain open. `AMENDMENT_AFTER_ESTABLISHMENT` remains `[Q2]`; the blockers remain `AMENDMENT_MODEL_ABSENT: [Q2]`, `TEMPORAL_MODEL_UNRESOLVED: [Q9]` and `PARTIAL_SCOPE_IDENTITY_UNRESOLVED: [Q5]`. `bounded_stable_candidate_not_selected`, the promotion candidate set `[OCP-005, OCP-006, OCP-010]`, the completed `EVENT_T6` cycle and `active_cycle_id: null` remain current.

The mandate's “Q2 reopens” attack applies only to the counterfactual closure branch. On this negative branch, OCP-005 must remain byte-identical. The symmetric executable guard therefore fails if Q2 is struck, if any other open question is struck, if the amendment blocker is removed, or if status, readiness, candidate composition or cycle state changes.

All previous ADs, witnesses and `baseline_*` objects remain byte-identical. No live quote changes, so no historical-to-current quote-succession record is needed.

## 8. Versioning, migration and rollback

OCP-001 pre-canonical `Y` applies to substantive contract changes and `Z` to editorial changes. This act changes neither content nor metadata of OCP-005, so no subject version transition exists; it remains `0.3.0`. Assigning `Y` or `Z` would falsely claim a subject change.

AD-048 begins `0.1.0 / Discovery` because it records insufficiency and exercises no lifecycle closure. No Assignment data, reference, schema or consumer migration exists. Rollback removes the AD-048 document, witness, checker, tests and accounting as one reviewed unit and changes no Q2 state or live contract.

## 9. Executable enforcement

`architecture/assignment-q2-sufficiency.yaml` binds the predeclared criterion, separate argument-type policies, Q3/Q9 calibration, ten evidence rows, two exact survivors, executable discriminator failure, unchanged subject and live projections, promotion guard, migration and protected bytes.

The checker requires exact OCP-005 bytes; Q2/Q5/Q9 open; exact amendment moving surface and all three blockers; both current-three-binding pressure survivors; both `underdetermined` norm survivors; acceptance of both subject-specific field replacements; rejection of a real invalid role scalar; stable readiness, statuses, candidate set and cycle state; and every protected current or historical artifact byte.

The named `test_every_defensive_value_is_individually_fixture_and_mutation_live` mutates every witness scalar and every protective constant, structure, token, digest and path individually. Eight test methods are added; no fixture is added or changed.

## 10. Exact baseline, accounting, safety and non-implications

Baseline is `main@4586bccbdc943c6a92daf052ce3df915d41fb976`, tree `efcce11913f0362e1611090978376358a455ad24`. The witness records nineteen full-chain anchors. For each, the stated blob was reverse-resolved through `git ls-tree -r`, the declared path matched, internal state tokens were checked in the raw object, and SHA-256 was recomputed over those same bytes.

Machine-derived accounting remains 302 non-sensitive fixtures and moves from 394 to 402 unit tests. The probe reuses synthetic `R-001`, `OP-001`, `A-001` and `2026-08-02` values. It introduces no coordinate, route, organization/unit, person, credential, key or token.

AD-048 does not close Q2 or another question; remove a blocker; change OCP-005; define or activate an amendment model; change status, readiness or promotion candidates; select Assignment; start a cycle; open T7; or authorize another act.
