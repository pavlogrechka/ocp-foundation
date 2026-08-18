---
Decision-ID: AD-045
Title: Assignment Survivor Norm-Compatibility Discovery
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: AD-035, AD-039, AD-044, OCP-002, OCP-003, OCP-004, OCP-005, OCP-016, OCP-017, OCP-023
Applies-To: OCP-005 §19.2, §19.3, §19.5, §19.9
Review-After: An Accepted or Canonical source changes one evaluated axis, or a separately mandated Assignment lifecycle resolution is proposed
---

# AD-045 — Assignment Survivor Norm-Compatibility Discovery

## 1. Question and result

This act asks whether current normative text excludes any of the six Assignment resolution classes that survived AD-044 consumer pressure. It tests norm compatibility only. It does not repeat completeness or consumer-need analysis.

No surviving class is `incompatible`. `WHOLE_RESOURCE_ONLY` is `compatible`: every defining axis is addressed by current exact-one-Resource and component non-inheritance guarantees. The other five are `underdetermined`: current norm explicitly delegates or defers the axis that distinguishes them.

The result excludes nothing and selects nothing. Q2, Q3, Q9 and Q5 stay open; all three `blocks-whole-document-freeze` entries stay unchanged. Even a future discovery result leaving one compatible class would still lack lifecycle authority to close a question or remove a blocker.

## 2. Gate-first before evidence form

OCP-016 G4 does not apply to this discovery classification. AD-045 creates no positive-capable rule, result, profile or activation. It only compares already inventoried candidate classes with current Accepted/Canonical statements.

Any later act that defines or activates an Assignment resolution remains separately gated. Discovery cannot convert compatibility, silence or underdetermination into permission. The selected form is a Discovery AD, a machine-readable witness and synthetic probes; no Core or Route D semantic contract changes.

## 3. Criterion and source floor declared before enumeration

Classification is ordered and mutually exclusive:

1. `incompatible`: at least one current Accepted or Canonical statement is violated; the statement id, document, section and exact quote are required;
2. `underdetermined`: no violation exists, but at least one defining axis is explicitly unowned, undefined or deferred by current norm; and
3. `compatible`: every defining axis is addressed and no current statement is violated.

Only the current body of an `Accepted` or `Canonical` OCP is a normative source. OCP-005 is `Draft`, so it supplies the open-question and class subject but cannot prove incompatibility. AD-035, AD-039 and AD-044 supply current discovery inventory only. Historical reviewed snapshots and every `baseline_*` object are evidence of earlier states, never sources for this classification.

The negative proof is its own enumeration: every survivor is tested against every current statement on its defining axes. Failure to find an incompatibility is not converted to `compatible` when the relevant owner says the axis is deferred.

## 4. Complete survivor inventory

The live survivor criterion is every AD-044 `resolution_inventory` row whose `need_adequacy_effect` is `current-three-bindings-adequate`. The result is exactly six:

| Blocker | Surviving classes |
|---|---|
| `AMENDMENT_MODEL_ABSENT` / Q2 | `SUPERSEDING_ASSIGNMENT_FOR_CHANGE`; `POST_ESTABLISHMENT_IMMUTABILITY` |
| `TEMPORAL_MODEL_UNRESOLVED` / Q3+Q9 | `PROSPECTIVE_ONLY_SINGLE_INTERVAL`; `PROSPECTIVE_ONLY_MULTIPLE_INTERVALS` |
| `PARTIAL_SCOPE_IDENTITY_UNRESOLVED` / Q5 | `WHOLE_RESOURCE_ONLY`; `EXPLICIT_PART_SCOPE_ON_ASSIGNMENT` |

No failed AD-044 class is silently reintroduced, and no new class is invented.

## 5. Q2 — both survivors are underdetermined

Canonical OCP-002 §Assignment says exactly:

> Assignment є ідентифікованим контекстним зв’язком рівно одного Resource з рівно однією Operation.

Canonical OCP-004 §10 adds:

> Кожен Assignment пов’язує рівно один Resource з рівно однією Operation, має власну ідентичність, RoleSpecification, applicability interval та lifecycle record.

Both superseding Assignment and post-Establishment immutability can preserve those guarantees. Accepted OCP-017 §10 then places the differentiating axis outside its authority:

> Any such lifecycle coordination requires a separate owner and Board act.

No current Accepted/Canonical source chooses whether post-Establishment role/applicability change creates a successor or is forbidden. OCP-005 asks that question while Draft and is not promoted into authority by this discovery. Both classes are therefore `underdetermined`, not incompatible and not selected.

## 6. Q3/Q9 — both prospective survivors are underdetermined

The two classes preserve exact-one-Resource binding. Their difference is interval cardinality, while both also assert a prospective-only policy. Accepted OCP-023 §7 explicitly says:

> It neither defines retroactivity nor multiple applicability intervals.

OCP-004's singular phrase `applicability interval` identifies the current bounded field but does not say that a future owner must forbid additional intervals, nor does it establish prospective-only behavior. Treating English grammatical number as an `incompatible` rule would invent a quote the document does not contain.

Both `PROSPECTIVE_ONLY_SINGLE_INTERVAL` and `PROSPECTIVE_ONLY_MULTIPLE_INTERVALS` are therefore `underdetermined`. Neither is excluded or preferred.

## 7. Q5 — whole Resource compatible; explicit part scope underdetermined

`WHOLE_RESOURCE_ONLY` exact-binds one Resource and asserts no automatic component inheritance. It satisfies OCP-002/OCP-004 exact-one-Resource statements and Canonical OCP-003 §7:

> Composite Assignment не створює Assignment або participation для component автоматично.

Every defining axis is addressed and no violation exists, so this class is `compatible`.

`EXPLICIT_PART_SCOPE_ON_ASSIGNMENT` also keeps one `resource_ref` and explicitly does not assert automatic component participation. It therefore does not violate non-inheritance. But OCP-003 §7 says exactly:

> Цей kernel не визначає record shape, directionality, effectivity, cycle rules або authority для `contains`, `part_of` чи іншої composition relation.

The representation needed to distinguish an explicit part scope is deliberately deferred. This class is `underdetermined`, not incompatible. The one compatible/one underdetermined result is not a Q5 selection and cannot close it.

## 8. Executable evidence and causal discrimination

`architecture/assignment-norm-compatibility.yaml` binds the source floor, six exact current statements, six AD-044 survivors, per-class claims and the unchanged promotion gate. Six fully synthetic `SYNTH-NORM-001..006` probes provide one record per survivor.

All six classifications are explicitly `evidence_mode: analytic`. The machine can observe the source floor and tokens: it reads each named current document, requires its live status to be `Accepted` or `Canonical`, isolates the named section and requires the exact quote once. Missing, moved, duplicated, rewritten or lifecycle-demoted source text fails rather than becoming `underdetermined`. But the reference checker cannot derive natural-language entailment or contradiction, so the mapping from those exact quotes to `allow-only`, `forbid` or `underdetermined` is a human-reviewed analytic policy, not a fabricated behavioral observation.

The classifier is not a constant-result guard. A control that changes `resource_cardinality` from `one` to `many` becomes `incompatible` with both exact-one-Resource statements. A separate control that asserts automatic component inheritance becomes `incompatible` with OCP-003. An unknown axis or malformed probe produces no classification. Thus an unrelated invalid input cannot carry the negative result.

The named test `test_every_defensive_value_is_individually_fixture_and_mutation_live` mutates every probe field, forbidden field/outcome, blocker/question/resolution binding, candidate claim, source path/status/section/quote/axis/effect, axis-policy kind/value/source, criterion, gate value and scalar token individually. Source, survivor, probe and gate drift are also attacked separately.

## 9. Exact baseline and full-chain anchors

The baseline is `main@734dd019425b636f47187bf1c342612550028400`, tree `5bfc5e0d09f6c52f7576e2a5ea60630875eed224`. Every row was resolved at that commit, reverse-resolved through `git ls-tree -r`, checked for its declared state/token and SHA-256 hashed over the same raw blob bytes.

| Evidence | Reverse-resolved path / state | Git blob | SHA-256 |
|---|---|---|---|
| OCP-002 | `docs/002-concept-taxonomy/README.md`; `1.6.0 / Canonical`, exact Assignment pair | `295512bdfaffd679ae021d0876072cdbcb2be75e` | `d49e9f896508d246994fd954174f04c69e0b4d32dfacc1dd612659263118df77` |
| OCP-003 | `docs/003-resource-concept/README.md`; `1.0.0 / Canonical`, non-inheritance and deferred composition form | `71485bb337cfd59def2e0f1b18b474a7959bd30c` | `f8656769dd046f221843f627c746d0d6040c2e83c736b900370d60244fce8315` |
| OCP-004 | `docs/004-operation-concept/README.md`; `1.0.1 / Canonical`, Assignment identity/interval/lifecycle boundary | `37fab136c578d2b8fafd6e900261ef64144943d9` | `ff0480913044b4dff8abcf69808b2d1cafe80a7d9f58c7ec06d2adeb33745538` |
| OCP-005 subject | `docs/005-assignment-concept/README.md`; `0.2.8 / Draft`, Q2/Q3/Q5/Q9 open; excluded as normative source | `6e6c00e723b15a348e7610d4ca5a1ae23526c52b` | `a9226f4f5e168b945ae743626e73ba5e25d67318b390869a493e5fd30bdaa065` |
| OCP-016 | `docs/016-core-boundary/README.md`; `1.0.0 / Canonical`, G4 | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| OCP-017 | `docs/017-operation-lifecycle/README.md`; `0.2.0 / Accepted`, separate Assignment owner/act | `0b2ea683df308babd1111ff47e9272c9b0742f78` | `061e2c8a4c9d3d02bb5a7492e9c8723cace11a462548970727552e18c645a030` |
| OCP-023 | `docs/023-resource-occupancy/README.md`; `0.2.0 / Accepted`, temporal axes not defined | `a846333fae80aff2b3697e811d2b155c91f04122` | `5ec9aca56de4524b4ab78a9e98e2cf5d7561d6f13bac8cf7778d66a99f5490d9` |
| AD-044 current projection | `architecture/assignment-consumer-pressure.yaml`; six `current-three-bindings-adequate` survivors | `2a96810984b79374c04bff20663cbc6953744c3d` | `d20f8b8330b4efdb6a23c09aa6f02b2182182ddd022486c370b11afb1d8f61b2` |
| blocker witness | `architecture/assignment-stable-surface.yaml`; exactly three whole-freeze blockers | `eea05626eddfba594508c5e6d4c4d5bd851c0f5a` | `b887717a064d479830b7aa0f360d2793a3cba4e54d2b1537d19374e553b3b593` |
| promotion gate | `architecture/foundation-promotion-gate.yaml`; schema 5, EVENT_T6 complete, no active cycle | `78f5f75d84fe9b0bdbf43ad3922404fa34f6c2d1` | `ca11036e10397d24b308957e059d0d5def1a9d90177c0d82987191c919a56dfd` |

## 10. Version, accounting, safety and rollback

AD-045 begins `0.1.0 / Discovery`: it is a new evidence record, not an OCP rule or lifecycle decision. Its witness begins schema 1. No existing artifact version changes.

The act adds six synthetic fixtures and eight discoverable test methods. Machine-derived accounting moves from `296 / 370` to `302 / 378`. The fixtures carry only `SYNTH-NORM-001..006`, blocker/question/resolution identifiers and abstract claim values; they contain no operation, coordinate, route, organization/unit, person, credential, key or token.

Rollback removes AD-045, its witness, checker integration, tests, six fixtures and descriptive accounting as one unit. It cannot remove a blocker, resolve a question or make an underdetermined class incompatible.

## 11. Non-implications

OCP-000 through OCP-024, AD-044, every open question and blocker, every Concept/status/edge, P-001, reviewed snapshot, historical `baseline_*` object and the promotion gate remain byte-identical. `EVENT_T6` stays the only completed cycle and `active_cycle_id` remains null.

AD-045 does not select a resolution, change OCP-005, remove a blocker, resolve Q2/Q3/Q5/Q9, activate a model, start T7 or authorize another act. Its complete result is only that current norm excludes none of the six survivors: one is compatible and five remain underdetermined.
