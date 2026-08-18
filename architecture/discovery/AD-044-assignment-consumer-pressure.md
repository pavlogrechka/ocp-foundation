---
Decision-ID: AD-044
Title: Assignment Consumer-Need Pressure Discovery
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: AD-035, AD-036, AD-038, AD-039, AD-040, AD-042, AD-043, OCP-005, OCP-016, OCP-023, OCP-024
Applies-To: OCP-005 §19.2, §19.3, §19.5, §19.9
Review-After: A real externally grounded completeness authority exists or a separately mandated Assignment resolution is proposed
---

# AD-044 — Assignment Consumer-Need Pressure Discovery

## 1. Question and result

This act asks whether the one current Accepted consumer need forces a particular resolution of any live `blocks-whole-document-freeze` Assignment blocker. A blocker is pressured only if a repository-grounded input makes the need satisfiable under some but not all of its exhaustive resolution classes.

The result is **not established from inside the repository** for all three blockers. Every enumerated resolution preserves the exact need signature, but the live tree has no legitimate completeness owner/evaluator or externally grounded all-Assignment coverage observation. Therefore no repository input proves satisfaction under any resolution, and no input selects exactly one.

This is not `neutral`: neutrality would require evidence that every resolution satisfies the need. It is not `pressured`: no resolution is excluded by a live satisfaction result. Each blocker is classified `undecidable-from-inside` and remains unchanged.

## 2. Gate-first before evidence form

OCP-016 G4 does not apply to this discovery result. The act classifies provenance of pressure and creates no positive-capable rule, result, profile or activation. Its synthetic probes never claim completeness.

Any later act that actually satisfies `assignment_set_complete_for_resource(resource_ref, evaluation_time, snapshot_ref)` remains G4-bound. OCP-023 supplies an Accepted consumer; the exact activation baseline, rule version, production snapshot/context and legitimate external owner/evaluator are still absent. Discovery cannot self-supply them.

The chosen form is a Discovery AD plus an executable governance witness. It changes no Core or Route D semantic contract.

## 3. Criterion declared before enumeration

The classifications are mutually exclusive:

- `pressured`: at least one resolution cannot satisfy the need while at least one other can on a live grounded input;
- `neutral`: every resolution satisfies the need on live grounded inputs; and
- `undecidable-from-inside`: testing satisfaction itself requires a real completeness authority or coverage observation absent from the repository.

The negative-proof rule is separate: enumerate every resolution class and show that no repository-grounded input selects exactly one. Structural preservation of the need token is necessary but is not counted as satisfaction.

## 4. Complete blocker and resolution inventory

The live criterion is every `architecture/assignment-stable-surface.yaml` blocker whose disposition is `blocks-whole-document-freeze`. The set is exactly three.

Resolution classes are exhaustive by externally visible representation:

| Blocker / questions | Exhaustive classes | Why exhaustive |
|---|---|---|
| `AMENDMENT_MODEL_ABSENT` / Q2 | in-place traceable amendment; new superseding Assignment; post-Establishment immutability | a change either retains identity, creates a new identity or is forbidden |
| `TEMPORAL_MODEL_UNRESOLVED` / Q3+Q9 | prospective/retroactive × one/multiple intervals | both open questions are binary and their Cartesian product has four members |
| `PARTIAL_SCOPE_IDENTITY_UNRESOLVED` / Q5 | whole Resource only; explicit part scope on Assignment; part receives Resource identity | partial scope is forbidden, represented below the Resource identity or represented as its own Resource identity |

No local-after-freeze or outside-bounded-surface question is imported. Q2, Q3, Q9 and Q5 remain open.

## 5. Q2 — amendment model

All three classes can expose an exact Assignment set for the same `resource_ref`, `evaluation_time` and `snapshot_ref`:

1. an in-place model includes the attributable version current in the named snapshot;
2. a superseding model includes the relevant predecessor/successor records; and
3. immutability includes the unchanged established record.

The consumer need cannot choose among them. What is missing is evidence that the named set contains every relevant Assignment/version. That external coverage problem is identical in all three classes. Classification: `undecidable-from-inside`.

This does not overturn AD-038: Q2 still lacks an owner rule and `AMENDMENT_MODEL_ABSENT` remains blocking.

## 6. Q3/Q9 — retroactivity and interval cardinality

The four Boolean combinations all preserve the need signature. Prospective-only models do not prove that the producer observed every Assignment; retroactive models additionally make later backdated records relevant, but a snapshot may still bind a closed observation cut if an external authority establishes it. One or several applicability intervals change effectivity representation, not whether a producer can attest complete set coverage.

The repository has neither the real coverage source nor an authority that can establish the observation cut. It therefore cannot demonstrate satisfaction for any of the four combinations or use the need to exclude one. Classification: `undecidable-from-inside`.

AD-039 remains intact: Q3/Q9 stay open and `TEMPORAL_MODEL_UNRESOLVED` remains blocking.

## 7. Q5 — composite Resource scope

Whole-Resource-only, explicit part scope and part-as-Resource identity can each bind a Resource-named snapshot. Their identity granularity differs, but OCP-023's current need asks whether the exact snapshot contains every Assignment relevant to the named Resource and instant. None of the three representations proves that coverage by itself.

Because the external coverage observation is absent, no current input establishes satisfaction under one class or all classes. Classification: `undecidable-from-inside`.

AD-039 remains intact: Q5 stays open and `PARTIAL_SCOPE_IDENTITY_UNRESOLVED` remains blocking.

## 8. Executable proof and individual coverage

`architecture/assignment-consumer-pressure.yaml` binds the exact blocker inventory, criterion, one current need, ten resolution classes, external missing inputs and unchanged promotion gate. Ten synthetic fixtures provide exactly one probe per resolution.

Every probe binds `OCP-023@0.2.0`, the exact need token, `R-001`, a synthetic snapshot and `2026-08-02T10:00:00Z`. Each derives `signature_effect=preserved` and `classification=undecidable-from-inside`; `completeness_authority_ref` is null. Supplying an authority locally is rejected as self-supply rather than converted into satisfaction.

The named test `test_every_defensive_value_is_individually_fixture_and_mutation_live` covers every declared probe field, forbidden field/outcome, blocker/question mapping, resolution value/detail, reason, gate/criterion value and scalar binding individually. Separate mutations prove blocker, current-need, probe and promotion-gate drift.

## 9. Exact baseline and full-chain anchors

The baseline is `main@6099a1ce042624b86fb4289f75d396a53fa9addb`, tree `158f95c07cc3eaad2300535c3b9922bcd602d0b7`. Each anchor was resolved at that commit, reverse-resolved through `git ls-tree -r`, checked for its declared token and SHA-256 hashed over the same raw blob bytes.

| Evidence | Reverse-resolved path / state | Git blob | SHA-256 |
|---|---|---|---|
| OCP-005 | `docs/005-assignment-concept/README.md`; `0.2.8 / Draft`, Assignment Accepted, Q2/Q3/Q5/Q9 open | `6e6c00e723b15a348e7610d4ca5a1ae23526c52b` | `a9226f4f5e168b945ae743626e73ba5e25d67318b390869a493e5fd30bdaa065` |
| OCP-016 | `docs/016-core-boundary/README.md`; `1.0.0 / Canonical`, G4 | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| OCP-023 | `docs/023-resource-occupancy/README.md`; `0.2.0 / Accepted`, exact unmet need | `a846333fae80aff2b3697e811d2b155c91f04122` | `5ec9aca56de4524b4ab78a9e98e2cf5d7561d6f13bac8cf7778d66a99f5490d9` |
| OCP-024 | `docs/024-completeness-evaluator/README.md`; `0.1.0 / Draft`, real legitimacy unresolved | `2713c99ca6653d35fc52435eaeaeb8f9f5174b1d` | `0c77e0527ec3adf9ed7cf5bbd32e0a63e55a1c3780f007d35a0ef2630cc18753` |
| blocker witness | `architecture/assignment-stable-surface.yaml`; exactly three whole-freeze blockers | `eea05626eddfba594508c5e6d4c4d5bd851c0f5a` | `b887717a064d479830b7aa0f360d2793a3cba4e54d2b1537d19374e553b3b593` |
| current need | `architecture/consumer-need-discovery.yaml`; exactly one unmet positive need | `b4882b4b91bf7dfd433fef9fdca08a297c8a6945` | `a07d9826deaf4455ea5acbe065f5edd2be2cacb8d80bf3bed6e796ab111e5351` |
| promotion gate | `architecture/foundation-promotion-gate.yaml`; schema 5, EVENT_T6 complete, no active cycle | `78f5f75d84fe9b0bdbf43ad3922404fa34f6c2d1` | `ca11036e10397d24b308957e059d0d5def1a9d90177c0d82987191c919a56dfd` |

## 10. Version, accounting, safety and rollback

AD-044 begins `0.1.0 / Discovery`: it is a new evidence record, not an OCP rule or lifecycle decision. The witness begins schema 1 because it introduces a bounded pressure-classification language. No existing artifact version changes.

Current accounting changes only by ten synthetic fixtures and focused tests; OCP, Concept, snapshot and P-001 counts do not move. Fixtures contain no real operation, coordinate, route, unit, organization, person, credential, key or token.

Rollback removes AD-044, its witness, checker integration, tests, ten fixtures and descriptive accounting as one unit. It cannot remove a blocker or resolve a question.

## 11. Non-implications

OCP-005, its open questions, all three blocker entries, OCP-023, OCP-024, every Concept/status/graph edge, P-001, reviewed snapshots, historical `baseline_*` objects and the promotion gate remain byte-identical. `EVENT_T6` remains the only completed cycle and `active_cycle_id` remains null.

This act does not select an Assignment rule, remove a blocker, resolve a question, activate completeness or occupancy, change a Concept, start T7, authorize a future act or establish that consumer pressure is absent in reality. It establishes only that pressure cannot be attributed from the current repository evidence.

Merge still requires exact-head Fable review, Codex adjudication, green CI on the same head and fresh explicit Pavlo authorization naming that head.
