---
Decision-ID: AD-047
Title: Assignment Q9 Interval-Cardinality Sufficiency Attempt
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: AD-039, AD-044, AD-045, AD-046, OCP-001, OCP-005, OCP-016, OCP-023
Applies-To: AB-029, OCP-005 §6.3, §8, §19.9
Review-After: A separately mandated closed-world interval-cardinality or multi-interval representation proposal satisfies OCP-016 G4
---

# AD-047 — Assignment Q9 Interval-Cardinality Sufficiency Attempt

## 1. Conditional authority and exact result

This act tests whether current records are sufficient to close OCP-005 Q9: may one Assignment carry several non-contiguous applicability intervals, or must each interval use a separate Assignment? Closure authority exists only if the criterion in §3 passes.

It does not pass. Q9 remains open and `TEMPORAL_MODEL_UNRESOLVED` remains a `blocks-whole-document-freeze` blocker bound exactly to `[Q9]`. OCP-005 remains byte-identical at `0.3.0 / Draft`; Assignment remains `Accepted`. Q2, Q5, every status, readiness statement, promotion candidate and promotion-cycle field remain unchanged.

This is a completed negative result, not a failed search for a preferred positive answer. The evidence independently establishes that both single-interval and multiple-interval classes remain possible under current text, behavior and consumer pressure.

## 2. Gate-first before result form

The insufficiency record is not positive-capable under OCP-016 G4. It adds no Assignment field, cardinality rule, representation, derivation, profile, result or activation. Its form is therefore a Discovery AD, an exact witness and executable guards.

Either hypothetical Q9 closure would be positive-capable. Finalizing “one interval only” would add a closed-world prohibition that current validation does not enforce. Finalizing “multiple intervals allowed” would add representation, identity and effectivity rules. Both require a separately authorized G4 act. Accepted OCP-023 exists, but it expressly selects neither cardinality and cannot self-supply the missing rule.

## 3. Sufficiency criterion declared before application

Q9 may close only if all five conditions hold:

1. current owner text normatively fixes one cardinality rather than merely displaying a singular minimum shape;
2. current executable behavior rejects every alternative cardinality on an otherwise valid Assignment;
3. a current Accepted consumer excludes every alternative but one;
4. pressure and current-norm evidence leave exactly one Q9 class; and
5. finalization needs no new field, subject identity, representation or derivation rule.

A field list is not sufficient when its owner calls it a minimum verifiable contract rather than a database/API schema. Acceptance of an unknown extension is likewise not permission; it is evidence that no executable cardinality boundary exists.

## 4. Comparison with the Q3 threshold

The Q9 basis is weaker than the basis that closed Q3 on every material axis:

| Axis | Q3 at AD-046 | Q9 now |
|---|---|---|
| owner boundary | §8 already prohibited derived effectivity before authoritative `established_at` | §6.3 shows one start/end pair but §6 says the list is minimum and not a schema |
| executable discrimination | the same Assignment changes `false → true` when the query crosses `established_at` | adding two synthetic intervals leaves the otherwise valid Assignment valid |
| Accepted-consumer pressure | OCP-023 excluded both retroactive classes | OCP-023 and AD-044 retain both prospective cardinalities |
| survivor intersection | both survivors shared `prospective-only` | survivors differ exactly between `single` and `multiple` and both are `underdetermined` |
| new rule needed | none for the narrow negative lower bound | closed-world prohibition or positive representation/derivation rules |

No Q3 conclusion is transferred by analogy.

## 5. Complete Q9 evidence application

### 5.1 Owner text

OCP-005 §6.3 presents `applicability_start` and optional `applicability_end`. That proves the required minimum pair. Section 6 immediately limits the inference: the list is a minimum verifiable contract and is not a database or API schema. Q9 itself remains unstruck. No invariant says “exactly one interval,” forbids an additional interval-bearing structure, or specifies how several intervals affect `assignment_effective_at`.

### 5.2 Executable behavior

The current valid Established Assignment fixture is replayed unchanged. A subject-specific mutation adds `applicability_intervals` containing two separated synthetic intervals while retaining the required scalar start/end pair. `validate_assignment` accepts both the original and mutation and `assignment_effective_at` produces the same current-scalar result at `10:15Z`.

This does not authorize `applicability_intervals`. It proves that the checker has no Q9 cardinality discriminator. A separate control moves the required `applicability_end` before `applicability_start` and receives `ASSIGNMENT_APPLICABILITY_INTERVAL_INVALID`; the probe is therefore not relying on a validator that accepts every temporal mutation.

### 5.3 Consumer pressure and norm survivors

AD-044 tested every temporal resolution. After Q3 closure the Q9-relevant survivors are `PROSPECTIVE_ONLY_SINGLE_INTERVAL` and `PROSPECTIVE_ONLY_MULTIPLE_INTERVALS`; both use `current-three-bindings-adequate`. Accepted OCP-023 explicitly says it defines neither retroactivity nor multiple applicability intervals.

AD-045 classifies both Q9 survivors `underdetermined`, with no violation and `interval_cardinality` as the unresolved axis. The singular wording in OCP-004 is recorded as `considered-no-exclusion`, not as a cardinality rule. The complete intersection therefore contains two classes, not one.

## 6. Decision, projections and closure-test asymmetry

The criterion fails, so the conditional authority to edit OCP-005 is not exercised. No live projection changes: Q9 remains open; `TEMPORAL_EFFECTIVITY_EXTENSION` remains `[Q9]`; `TEMPORAL_MODEL_UNRESOLVED` remains `[Q9]`; Q2 and Q5 retain their blockers; `bounded_stable_candidate_not_selected` remains current; the promotion candidate set remains `[OCP-005, OCP-006, OCP-010]`; only `EVENT_T6` is complete and no cycle is active.

The mandate's reopen-Q9 and blocker-removal-with-readiness-change attacks apply only to the counterfactual closure branch. Applying them to this negative branch would contradict the authorized requirement that OCP-005 remain byte-identical. The executable guards therefore take the exact symmetric form required by the chosen outcome: they fail if Q9 is struck, if any other open question is struck, if the blocker is removed, or if status, readiness, candidate composition or promotion-cycle state changes.

Historical AD-039/044/045/046 records and witnesses remain byte-identical. Because no live quote changes, no historical-to-current quote-succession record is needed.

## 7. Versioning, migration and rollback

OCP-001 pre-canonical `Y` applies to substantive contract changes and `Z` to editorial changes. This act changes neither content nor metadata of OCP-005, so the document has no version transition: it remains `0.3.0`. Assigning either `Y` or `Z` would falsely claim a subject change.

AD-047 begins `0.1.0 / Discovery` because it records insufficiency and exercises no lifecycle closure. No Assignment data, reference, schema or consumer migration exists. Rollback removes AD-047 document, witness, checker, tests and accounting as one unit; it changes no Q9 state or live contract.

## 8. Executable enforcement

`architecture/assignment-q9-sufficiency.yaml` binds the predeclared criterion, gate split, seven-row evidence ledger, Q3 comparison, discriminating controls, two exact surviving Q9 classes, unchanged subject bytes, projections, promotion state, migration and protected artifacts.

The checker requires:

- exact OCP-005 bytes and `0.3.0 / Draft`, Assignment `Accepted`;
- Q9, Q2 and Q5 open while Q3 remains resolved;
- exact `[Q9]` temporal moving-surface and blocker membership;
- both current-three-binding pressure survivors and both `underdetermined` norm survivors;
- the subject-specific two-interval extension to remain valid without treating it as authorized;
- the reversed required interval control to remain invalid;
- stable discovery result, candidate set, statuses and promotion-cycle state; and
- every protected current and historical artifact byte.

The named `test_every_defensive_value_is_individually_fixture_and_mutation_live` mutates every witness scalar and every protective constant, map, set, token, digest and path individually. Eight test methods are added and no fixture is added or changed.

## 9. Exact baseline and full-chain anchors

Baseline is `main@7acced16b99790db04c8dccb9380a6191633af30`, tree `5cbaf6e9a9c588ca4ad14f447e8676b11afe95d2`. Each object below was resolved from that tree, reverse-resolved through `git ls-tree -r`, checked for the stated internal token/state, and SHA-256 hashed over the same raw blob bytes.

| Evidence | Reverse-resolved path and baseline condition | Git blob | SHA-256 |
|---|---|---|---|
| OCP-001 version rule | `docs/001-ontology-governance/README.md`; `1.0.0 / Canonical`, pre-canonical `Y`/`Z` rule | `33524fa3d18f3253faa9a854500be7ddfb20815f` | `da74645aa4f3cae10c7c59ae7b87abd1840544700e4a58e9efd3f6600a27f1cc` |
| OCP-005 subject | `docs/005-assignment-concept/README.md`; `0.3.0 / Draft`, Q9 open | `1dd975a17ec65df751357fdd049c8ca928739bd1` | `de84c9dafdb6126ff68a3a33218a344ddc250cf1a28e63c91407fd416e7e161b` |
| OCP-016 G4 | `docs/016-core-boundary/README.md`; `1.0.0 / Canonical`, exact G4 boundary | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| Accepted consumer | `docs/023-resource-occupancy/README.md`; `0.2.0 / Accepted`, no interval-cardinality ownership | `a846333fae80aff2b3697e811d2b155c91f04122` | `5ec9aca56de4524b4ab78a9e98e2cf5d7561d6f13bac8cf7778d66a99f5490d9` |
| current stable projection | `architecture/assignment-stable-surface.yaml`; Q9-only temporal blocker | `6cc326c64e5dc5d84cbc60e1f95548db9dd0abad` | `cd093bd36ab29a203ad56ccded32baee671989be768b7ad415f65850e2b6d3d9` |
| AD-039 attempt witness | `architecture/assignment-temporal-scope-attempt.yaml`; two-interval gap probe | `9fa12f7c527c7d66ebbba24cf063fc353973d8ae` | `4a8899d58ddf9edcf613760d330ff0003a3f982c1d6c188c4283c52fc364f7fb` |
| AD-044 pressure witness | `architecture/assignment-consumer-pressure.yaml`; both prospective classes adequate | `2a96810984b79374c04bff20663cbc6953744c3d` | `d20f8b8330b4efdb6a23c09aa6f02b2182182ddd022486c370b11afb1d8f61b2` |
| AD-045 norm witness | `architecture/assignment-norm-compatibility.yaml`; both Q9 classes underdetermined | `7abda1ed215fb15a520e56682c442db9c9e042b4` | `6e32c5ed98df564c4cf23b1791bff86a80772ecd6be2135ab786d924ac4066dd` |
| AD-046 Q3 witness | `architecture/assignment-retroactivity-q3-resolution.yaml`; Q9 still open | `0262964d9754325fe897871734ed2e1f0ec1ff9e` | `aa6b8fc70d320ad5a5c920dcd46379fb3119cfbfab938ba58600747cd0482d7a` |
| causal fixture | `tools/ontology_checker/fixtures/assignment/valid-established.yaml`; valid Established Assignment | `354de6880fe59429c40179eedd4037e52ff5208a` | `3f2ea38f35292b821a7297ed4604a1764efd12c5399ee61a64ea7a2aa5b91117` |
| promotion gate | `architecture/foundation-promotion-gate.yaml`; schema 5, only `EVENT_T6` complete, no active cycle | `78f5f75d84fe9b0bdbf43ad3922404fa34f6c2d1` | `ca11036e10397d24b308957e059d0d5def1a9d90177c0d82987191c919a56dfd` |

## 10. Accounting, safety and non-implications

Machine-derived accounting remains 302 non-sensitive fixtures and moves from 386 to 394 unit tests. All probe values reuse the existing synthetic `R-001`, `OP-001`, `A-001` fixture and synthetic `2026-08-02` timestamps. No coordinate, route, organization/unit, person, credential, key or token is introduced.

AD-047 does not close Q9 or any other question; remove any blocker; change OCP-005; define interval cardinality or representation; treat an unknown field as authorized; change status, readiness or promotion candidates; activate a positive model; select Assignment; start a cycle; open T7; or authorize another act.
