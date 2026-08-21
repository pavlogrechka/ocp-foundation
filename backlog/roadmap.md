# Foundation v1 Roadmap

## 1. Authority and decision boundary

This roadmap is the current, non-normative delivery plan for **Foundation v1**. It replaces the former open-ended milestone catalogue and its formula-free readiness percentages. Normative meaning remains in the OCP documents and governed decisions; this plan cannot change an OCP or Concept status, close an open question, activate a rule, select a candidate or authorize another act.

The current repository state is an input, not an effect of this roadmap:

- primary OCP documents: **25 total = 11 Canonical + 14 Accepted + 0 Draft**;
- defined Concepts: **8 total = 6 Canonical + 2 Accepted**;
- `OCP-005`: **1.0.0 / Canonical**, Concept `Assignment`: **Accepted**;
- `OCP-006`: **0.4.0 / Accepted**, Concept `Constraint`: **Accepted**;
- active promotion cycle: **`ASSIGNMENT_T6`**;
- cycle steps: **`CANDIDATE_BOARD_SELECTION=completed`, `DOCUMENT_PROMOTION=completed`, `CONCEPT_CANONICALIZATION=pending`**;
- current unmet positive need: **`RESOURCE_OCCUPANCY_ASSIGNMENT_SET_COMPLETENESS`**.

In lifecycle terms, OCP-005 document є Canonical, тоді як Assignment і Constraint Concepts лишаються Accepted. This is a current-state observation only; it does not select either disposition of `ASSIGNMENT_T6`.

These values are derived from primary frontmatter and the live promotion/consumer-need maps, not maintained as independent authority: [machine accounting](../architecture/current-numeric-accounting.yaml), [promotion gate](../architecture/foundation-promotion-gate.yaml), [consumer-need projection](../architecture/consumer-need-discovery.yaml). The repository test `test_v1_roadmap.py` fails if this rendering diverges from those sources.

## 2. Readiness scales

### 2.1 Primary decision scale — external-developer usability

This is the primary scale because the next project risk is no longer whether the repository can govern itself; it is whether an independent developer can implement and verify Foundation v1.

Every layer is one equally weighted, independently observable prerequisite:

| Layer | Current value | Live evidence |
|---|---|---|
| governed normative contracts | `1` | all 25 primary documents are Accepted or Canonical; derived from [primary frontmatter](../docs) |
| executable reference semantics | `1` | current validators and derivations are enumerated in the [checker guide](../tools/ontology_checker/README.md) |
| machine-readable exchange schemas | `0` | [schemas](../schemas/README.md) contains no schema artifact yet |
| production API/runtime/persistence contract | `0` | the [checker boundary](../tools/ontology_checker/README.md) explicitly excludes these roles |
| legitimate operational authority and source bindings | `0` | [OCP-024](../docs/024-completeness-evaluator/README.md) rejects production-shaped authority as unresolved |
| independent end-to-end conformance evidence | `0` | no tracked `external-conformance` evidence package exists |

Formula: **`(1 + 1 + 0 + 0 + 0 + 0) / 6 × 100 = 33.3%`**. Inputs are the six rows above; the roadmap test rederives every repository-observable row. The last row is an explicit repository-evidence observation: external execution itself cannot be manufactured by this repository.

### 2.2 Reference scale — lifecycle completion

This scale measures status transitions only. It does **not** measure semantic completeness, interoperability or production readiness.

Each primary document or defined Concept has two possible lifecycle transitions: `Draft → Accepted` and `Accepted → Canonical`. `Draft` contributes zero completed transitions, `Accepted` one and `Canonical` two.

- document transitions: **`11 × 2 + 14 × 1 + 0 × 0 = 36` completed of `25 × 2 = 50`**;
- Concept transitions: **`6 × 2 + 2 × 1 = 14` completed of `8 × 2 = 16`**;
- combined formula: **`(36 + 14) / (50 + 16) × 100 = 75.8%`**.

The inputs come from the same primary-frontmatter scan as [current numeric accounting](../architecture/current-numeric-accounting.yaml). This percentage is reference information only; a lifecycle transition may add no semantic or operational right.

### 2.3 Reference scale — production readiness

Production readiness requires all four currently missing operational layers from §2.1: machine schemas, production runtime/persistence, legitimate operational bindings and independent end-to-end conformance evidence.

Formula: **`(0 + 0 + 0 + 0) / 4 × 100 = 0.0%`**. The four inputs and their live evidence are the final four rows of §2.1. This does not devalue the normative/reference work; it prevents that work from being reported as deployable software.

No other readiness percentage is current. A future percentage is permitted only when its scale, inputs, formula and live evidence are present together and executable where repository observation is possible.

## 3. Foundation v1 scope

Every inclusion below is a yes/no contract boundary. Foundation v1 includes an item only when its named owner document remains in the stated lifecycle class and its executable surface remains present.

### 3.1 Included inputs

- [x] OCP-005 Assignment records restricted to the granted compatibility surface: identity/reference, transition-history lifecycle, structural role/provenance, single-interval effectivity and participation, non-inheritance/non-authority, supersession identity and the executable Assignment boundary.
- [x] OCP-006 Constraint and ConstraintEvaluationRecord inputs restricted to identity/supersession, structural lifecycle/effectivity, bounded applicability/evaluation/admissibility, fail-safe non-authority and target-scope non-inheritance.
- [x] OCP-017 Operation lifecycle evidence exact-bound to one Operation and its authoritative transition chain.
- [x] OCP-018 authorization-source evidence exact-bound to its source profile, owner, Operation, authorizer, Capability, level and snapshot.
- [x] OCP-023 occupancy requests and exact Resource-bound Assignment snapshots.
- [x] OCP-024 completeness-evidence envelopes with exact subject, coverage, time, provenance/authority reference and consistency fields.

The checkboxes record v1 inclusion, not current implementation completion. Their source contracts are [OCP-005](../docs/005-assignment-concept/README.md), [OCP-006](../docs/006-constraint-concept/README.md), [OCP-017](../docs/017-operation-lifecycle/README.md), [OCP-018](../docs/018-operation-authorization-source/README.md), [OCP-023](../docs/023-resource-occupancy/README.md) and [OCP-024](../docs/024-completeness-evaluator/README.md).

### 3.2 Included outputs

- [x] exact Assignment validation, `assignment_effective_at` and `derived_participates_in`;
- [x] exact Constraint validation, applicability, effective result, blocking and set decision;
- [x] Operation lifecycle stage and authorization-source result within the OCP-017/OCP-018 boundaries;
- [x] `occupied=true` with the complete sorted witness set when at least one exact-bound Assignment is effective;
- [x] `occupied=false` only when a separately legitimate completeness binding proves the exact Assignment snapshot complete;
- [x] `indeterminate` whenever completeness, authority, freshness, resolution or exact binding is absent, stale, ambiguous, conflicting or invalid;
- [x] machine-readable conformance diagnostics for every included input/output boundary.

### 3.3 Explicit non-goals

Foundation v1 does not:

- establish Conflict, Risk, priority or a winner among Assignments;
- derive capacity sufficiency, availability, remainder, reservation or allocation;
- establish Order as mandatory, sufficient or an authorization source;
- establish Constraint precedence, override or contextual waiver;
- grant permission, approval, authorization, truth or action recommendations outside the exact OCP-017/OCP-018 result boundaries;
- answer OCP-005 withheld Q2/Q4/Q5/Q7/Q8/Q9/Q10/Q11 by silence;
- answer OCP-006 open Q1/Q2/Q6/Q7/Q8/Q10/Q11/Q12 by silence;
- act as a general ontology editor, lifecycle engine, policy engine, persistence platform or production system of record;
- claim that synthetic fixtures authenticate a real source, owner, evaluator or complete observation cut;
- require every possible future Concept, positive model, production profile or T7–T10 programme to finish before v1 can finish.

These non-goals preserve the live normative exclusions in [OCP-005](../docs/005-assignment-concept/README.md), [OCP-006](../docs/006-constraint-concept/README.md), [OCP-016](../docs/016-core-boundary/README.md), [OCP-019](../docs/019-conflict-derivation-boundary/README.md), [OCP-021](../docs/021-reservation-allocation-boundary/README.md), [OCP-022](../docs/022-order-authorization-boundary/README.md) and the [checker boundary](../tools/ontology_checker/README.md).

## 4. Completion conditions

Foundation v1 is complete only when every row is `satisfied`. “Externally observable” means the repository can verify the presence and binding of evidence but cannot create the underlying fact.

| ID | Yes/no completion condition | Verification mode | Current result |
|---|---|---|---|
| V1-C1 | §§2–3 remain one current, formula-backed scope and readiness contract | machine | satisfied by this roadmap after merge |
| V1-C2 | `active_cycle_id` is `null` after a separately authorized forward completion or atomic corrective rollback | machine | not satisfied |
| V1-C3 | every included v1 input/output has a machine-readable exchange schema with a version and normative source | machine | not satisfied |
| V1-C4 | a versioned implementation-facing package exposes the included validators/derivations without claiming independent authority | machine | not satisfied |
| V1-C5 | a named Accepted external consumer supplies one exact use case, source-of-record, success criterion and responsible owner | externally observable | not satisfied |
| V1-C6 | a legitimate evaluator/authority binding and exact completeness observation-cut protocol exist for the selected use case | externally observable | not satisfied |
| V1-C7 | the selected use case passes an end-to-end run including fail-safe negative/indeterminate cases | mixed | not satisfied |
| V1-C8 | an implementation independent of the reference checker passes the published conformance package | externally observable | not satisfied |
| V1-C9 | every positive need required by the selected v1 use case is either satisfied by an exact G4 binding or explicitly removed from v1 scope by a separately reviewed scope decision | mixed | not satisfied |
| V1-C10 | every remaining open question is proven not to change an included v1 input/output, or v1 remains blocked | mixed | not yet verifiable before the external use case is fixed |
| V1-C11 | current status, version, cycle and numeric claims are derived from live sources; historical claims remain explicitly baseline-bound | machine | satisfied |

`V1-C5`, `V1-C6` and `V1-C8` cannot become true through repository-internal prose or synthetic fixtures. `V1-C10` is deliberately marked not yet verifiable rather than treated as satisfied by silence.

## 5. Ordered path to v1

1. **[internal] Dispose `ASSIGNMENT_T6`.** Choose one of the two paths in §6 under a separate mandate; this roadmap chooses neither.
2. **[internal] Freeze the v1 contract.** Maintain §§3–4 as the sole current scope/completion list; remove work that is neither required by an included output nor by a completion condition.
3. **[external] Bind a real consumer use case.** Required input: exact obligation, source-of-record, success criterion and responsible product/domain owner. Provider: the system/product team that must consume the result.
4. **[internal, externally informed] Publish implementation-facing contracts.** Add versioned schemas, package/API boundary and conformance data only for the frozen v1 surface. Reopen the OCP-016 no-schema baseline through its required governance route rather than smuggling a mandatory projection into implementation code.
5. **[external] Bind completeness and authority.** Required input: observation-cut semantics, source coverage, evaluator delegation, freshness/validity policy and failure ownership. Providers: system-of-record owner, domain/data owner and security/identity authority.
6. **[mixed] Run the end-to-end pilot.** Repository work supplies the reference package and fail-safe cases; the external consumer supplies production-shaped, non-sensitive evidence and judges the declared success criterion.
7. **[mixed] Resolve only demonstrated blockers.** A semantic act may open only for a failure observed in the selected pilot and must retain the exact consumer/source/success binding that exposed it.
8. **[external] Obtain independent conformance evidence.** Provider: an implementation team that did not author or reuse the reference checker as its implementation.
9. **[internal] Declare Foundation v1 complete.** This occurs only after every §4 row is satisfied and rechecked on one exact head; completion grants no authority to expand v1.

## 6. Current-cycle disposition without selection by implication

The live cycle is closable in both directions under [the current selection witness](../architecture/assignment-promotion-selection.yaml):

- **Forward completion** is admissible only if a separate Concept-canonicalization act proves an explicit user-facing compatibility promise for `Assignment`, satisfies the applicable Concept criteria and does more than clear `active_cycle_id`. It completes only `CONCEPT_CANONICALIZATION` and then sets `active_cycle_id: null` as the mechanical cycle consequence.
- **Formal collapse** is required when that incremental promise cannot be demonstrated or when keeping the cycle open obstructs v1 without adding a user-facing contract. The defined mechanism is a new reviewed atomic corrective-rollback PR restoring the whole cycle unit and `active_cycle_id: null`; a one-file gate edit or history rewrite is invalid.

This roadmap does not select either disposition, canonicalize `Assignment` or alter the gate.

## 7. What cannot be supplied from inside the repository

| Missing fact | Why internal acts cannot establish it | Required external input and provider | Normative boundary |
|---|---|---|---|
| legitimate completeness evaluator | reference shape cannot prove real delegation or whole-subject observation | delegated evaluator and authority basis from the operational domain/data owner | [OCP-024 §§3–4](../docs/024-completeness-evaluator/README.md) |
| complete Assignment snapshot | a caller-provided or synthetic list cannot prove that no effective Assignment was omitted | observation-cut and coverage proof from the system-of-record owner | [OCP-023 §4](../docs/023-resource-occupancy/README.md) |
| production `occupied=false` | the negative result is unsafe without the preceding completeness fact | authenticated complete snapshot protocol from the source/evaluator owners | [OCP-023 §§4, 13](../docs/023-resource-occupancy/README.md) |
| positive Conflict/capacity/reservation/order/override models | positive activation requires an Accepted consumer, baseline, rule, snapshot, context and legitimate owner/evaluator | protected result need and complete activation binding from a product/domain consumer and semantic owner | [OCP-016 §5](../docs/016-core-boundary/README.md) |
| permission, authorization or truth outside existing exact boundaries | Core routing and structural checking cannot grant operational authority | policy decision, identity evidence and authority delegation from security/policy/system owners | [OCP-016 §§6–7](../docs/016-core-boundary/README.md) |
| dynamic Constraint currentness lifetime | current OCP-006 does not define a freshness magnitude or currentness evaluator | freshness/SLO and risk policy from the dynamic-input producer and domain owner | [OCP-006 §30](../docs/006-constraint-concept/README.md) |
| independent interoperability | the reference implementation cannot prove that an independent implementation interprets the contract identically | conformance result from an independent implementation team | [checker authority boundary](../tools/ontology_checker/README.md) |
| production API, persistence and profiles | the current checker explicitly excludes those responsibilities | implementation contracts and operated profiles from platform/integration owners | [roadmap gap source](../tools/ontology_checker/README.md) |

The repository may record and validate these inputs after their owners provide them. It may not manufacture them by naming the Architecture Board, a synthetic fixture or the checker as the owner.

## 8. Binding stop rule

**No new semantic act that adds, selects, activates or legitimizes a positive model may be opened until an external consumer is named with all of: an exact use case, its source-of-record, a binary success criterion and the responsible product/domain owner.**

The input must be present in an Accepted consumer contract and must satisfy the current OCP-016 G4 admission boundary before implementation work begins. A roadmap entry, Architecture Board preference, synthetic fixture, open question, perceived usefulness or reference-checker capability is not a substitute.

Permitted work during the stop is limited to: disposition of the already open cycle under §6; non-semantic defects; v1 schemas/package/conformance preparation that does not invent missing truth; and collection/validation of the required external input. Each remains separately mandated and gains no authorization from this roadmap.

## 9. Evidence proportionality and maintenance rule

This roadmap is its own current planning carrier. It intentionally creates no AD, baseline copy, snapshot, projection mirror or per-token mutation inventory. Its proof is limited to:

- formula and source reproduction for every readiness number;
- live status/version/cycle/need synchronization;
- source-backed non-goals; and
- the ordinary full repository test and fixture checks.

Git history preserves the replaced roadmap. A future roadmap edit changes this file and the minimum derived accounting/tests only; it does not copy every current projection merely to prove that the plan changed.
