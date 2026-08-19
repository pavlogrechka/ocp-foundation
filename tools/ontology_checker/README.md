# Executable Ontology Checker

This directory contains the executable reference slice for OCP Foundation.

The checker is **not** a production validator, persistence schema, policy engine, or independent normative source. OCP documents, accepted architecture decisions, governed Patterns and artifact taxonomy remain authoritative. Code here implements a deliberately limited subset so that reviewed invariants and counterexamples become repeatable tests.

## Current scope

Implemented validators:

- Resource identity and classification;
- Operation identity, Objective resolution, F1/V1 explicit-intent evidence, local spatial-binding exact profile/snapshot envelope, bounded IO2 values and Q3I composition checks;
- Accepted OCP-017 Operation lifecycle predecessor-chain history, exact completeness/authorization evidence bindings, stage projection and terminal Assignment alignment;
- Accepted OCP-018 authorization-source profiles, identified decision records, authorizer Organization/Capability/level bindings, effectivity, supersession and OCP-017 acceptance derivation;
- Accepted OCP-019 negative Conflict-establishment requests with exact ConstraintEvaluationRecord references and fail-safe incomplete/conflicting/stale evidence handling;
- Accepted OCP-020 quantitative profile/unit/snapshot bindings and exact-unit `demand | consumed` aggregation without capacity or reservation authority;
- Accepted OCP-021 separate whole-Resource and partial/quantitative Reservation/Allocation negative composition boundaries;
- Accepted OCP-022 separate mandatory, sufficient and admissible-source Order authorization negative establishment boundaries;
- Draft OCP-006 separate Constraint application-order, override and contextual-waiver negative boundaries;
- Accepted OCP-023 Route D Resource-occupancy reference derivation over one exact synthetic complete Assignment snapshot, with all effective Assignment witnesses and no activation or adjacent authority;
- Accepted OCP-024 Route D Assignment-set completeness-evidence recognition envelope with exact subject/scope/time/provenance/authority bindings, fail-safe indeterminacy, preserved reviewed body and no real evaluator, completeness supply or activation;
- Assignment consumer-pressure discovery with exact enumeration of three whole-freeze blockers and ten resolution classes, live consumer replays, per-resolution binding adequacy and three non-unique `pressured` results;
- Assignment survivor norm-compatibility discovery with all 25 current primary bodies, a bounded 64-hit six-axis lexical sweep with explicit source/rejection dispositions, three exact-guarded known out-of-vocabulary temporal deferrals, six pressure survivors, one compatible and five underdetermined results, plus causal exact-Resource/non-inheritance counterexamples; the sweep does not claim semantic-axis completeness;
- Assignment Q3 lifecycle resolution with an exact final `established_at` effectivity lower bound, ordered sufficiency ledger, causal before/at-boundary probe, Q3-only closure guard, Q9-only temporal blocker projection and immutable historical discovery witnesses;
- Assignment Q9 sufficiency discovery with a predeclared Q3-level threshold, exact subject preservation, causal acceptance of a synthetic two-interval extension beside rejection of a real scalar interval violation, two surviving cardinality classes and unchanged blocker/readiness/promotion projections;
- Assignment Q2 sufficiency discovery with a predeclared five-axis criterion calibrated between Q3 and Q9, separate direct/enumeration/silence argument policies, two accepted subject-specific field-change probes, one real rejection control, two surviving change-model classes and unchanged blocker/readiness/promotion projections;
- Assignment transition history, projections, applicability and participation derivation;
- Assignment Q2 amendment plus historical Q3/Q9 temporal and Q5 partial-scope negative-boundary attempts, with exact owner-text drift guards, an isolated pre-establishment effectivity control and executable accepted-gap probes;
- Constraint structure, lifecycle, effectivity, applicability and exact-version evaluation;
- Organization exact dataset identity/lifecycle and OrganizationRelationshipRecord kind, endpoint, partition, graph and supersession validation;
- Capability definition identity, namespace, supersession and exact resolution;
- Event occurrence identity and exact resolution;
- ObservationRecord attribution, optional Event linkage and Module C supersession;
- OutcomeAssessmentRecord exact target/criterion/evidence/input/evaluator binding, fail-safe evidence states, `objective-achievement@2` F1/A1 activation and Module C supersession;
- CapabilityClaimRecord exact Resource/Capability/claimant/condition binding, temporal effectivity, Module C supersession, activated F1/A1 evidence replay and fail-safe attributable projection;
- ResourceInterchangeabilityRequirement exact owner/context/version binding and deterministic candidate eligibility;
- OCP-014 CoordinationResourceRequirement exact accepted-owner profile binding;
- accepted OCP-015 proposal/response record validation and fail-safe coordination-evidence projection;
- the integrated non-sensitive foundation scenario;
- Concept status synchronization and dependency graph;
- Event Concept canonicalization probes that independently derive its empty Concept dependency set, Canonical direct-OCP floor and exact Accepted P-001 binding, execute four frozen semantic surfaces, require every current registry/taxonomy/peer/generated/gate carrier to say `Canonical`, and keep three baseline-bound Accepted witnesses valid and immutable;
- declared Resolved-AB/open-question synchronization with exact current-document strikeout and disposition-reference checks;
- declared Accepted-OCP reviewed-snapshot coverage with exact primary/status, reviewed-version filename, content digest, primary link and retained OCP-016 evidence checks;
- artifact governance and complete-history process audit.

Implemented reference derivations include:

- `assignment_effective_at`;
- `derived_participates_in`;
- `constraint_effective_at`;
- `constraint_applicable_to`;
- `effective_constraint_result`;
- `constraint_blocks`;
- `constraint_set_decision`;
- `derive_constraint_application_order_boundary`;
- `derive_constraint_override_boundary`;
- `derive_contextual_waiver_boundary`;
- `resolve_capability_definition`;
- `resolve_event`;
- `observations_for_event`;
- `resolve_outcome_assessment`;
- `outcome_assessment_heads`;
- `effective_outcome_conclusion`;
- `derive_outcome_evidence_usability`;
- `resolve_capability_claim`;
- `capability_claim_effective_at`;
- `capability_claim_heads`;
- `effective_capability_claim`.
- `resolve_interchangeability_requirement`;
- `derive_resource_interchangeability`.
- `derive_coordination_evidence`.
- `organization_established_at`;
- `organization_relationship_effective_at`;
- `organization_relationship_successor_ids` (all exact successors, never a head).
- `derive_resource_occupancy` (Draft synthetic reference only; not an activated Resource-state authority).

## Manifest discipline

The checker uses exact module manifests:

- `rules.yaml` — core, governance, Objective, Capability and Event/Observation codes and derivations;
- `organization-rules.yaml` — Organization module;
- `assessment-rules.yaml` — OCP-011 OutcomeAssessmentRecord module;
- `capability-claim-rules.yaml` — OCP-012 CapabilityClaimRecord module.
- `interchangeability-rules.yaml` — accepted OCP-013 Resource interchangeability module plus the OCP-014 exact-owner profile invariant.
- `coordination-workflow-rules.yaml` — accepted OCP-015 proposal/response record and evidence-projection module.
- `operation-lifecycle-rules.yaml` — OCP-004 `0.9.0` Q3I evidence kernel and Accepted OCP-017 LT2 lifecycle module; the harness remains exact-bound to the reviewed `0.9.0` body incorporated into OCP-004 `1.0.0`.
- `operation-authorization-rules.yaml` — Accepted OCP-018 exact source-profile, decision, level, eligibility, effectivity, supersession and OCP-017 acceptance rules.
- `conflict-derivation-rules.yaml` — Accepted OCP-019 negative establishment-boundary and prohibited positive-authority rules.
- `quantitative-input-rules.yaml` — Accepted OCP-020 exact quantitative-input envelope, fail-safe validation and neutral exact-unit sum.
- `reservation-boundary-rules.yaml` — Accepted OCP-021 separate E/Q evidence envelopes, negative establishment results and prohibited positive authority.
- `order-authorization-boundary-rules.yaml` — Accepted OCP-022 three-question evidence envelope, negative establishment results and individually guarded authority/Concept/selector/self-supply/side-effect fields.
- `constraint-interaction-rules.yaml` — Draft OCP-006 separate application-order, override and contextual-waiver evidence envelopes, negative results and prohibited positive authority.
- `resource-occupancy-rules.yaml` — Accepted OCP-023 exact request/snapshot binding, one occupancy derivation, synthetic completeness evidence and individually guarded activation/adjacent-authority exclusions; Accepted status supplies no production activation.
- `completeness-evaluator-rules.yaml` — Accepted OCP-024 synthetic recognition envelope; invalid, stale, mismatched, ambiguous, conflicting or ungrounded evidence stays indeterminate and no production authority, completeness or activation is inferred.

Each manifest is checked for exact equality against its exported code and derivation sets. Adding an emitted code or derivation without a cited defining source fails unit tests. Artifact governance additionally requires rule identifiers to be globally unique across manifests and every rule source to begin with an exact-resolvable OCP identifier.

Module manifests do not create independent normative authority. Their `source` fields point back to OCP specifications, decisions or governance contracts.

## Pattern invocation policy

A `Uses-Patterns` invocation uses `P-NNN@x.y.z` checker syntax and must resolve to an existing Pattern whose current `Version` exactly equals the invoked version.

The repository policy is **track-current**, not historical pinning. A Pattern version change must update all invokers atomically and pass the applicable review lane.

ObservationRecord and OutcomeAssessmentRecord invoke `P-001@0.1.0` with selected Module C supersession. CapabilityClaimRecord selects Modules A and C for time-bounded applicability plus history-preserving correction/withdrawal. Their domain semantics remain in OCP-010, OCP-011 and OCP-012 respectively.

OCP-004 separately maps endpoint-free ExplicitIntentRecord (F1) and validation-evidence (V1) families without an Optional Module. OCP-017 maps lifecycle transitions (LT2) with Module B. P-001 remains unchanged: its time-anchored T3 ledger is not edited when these two primary invokers are added, and structured `Uses-Patterns` metadata remains the current invoker-set authority.

## Structured governance references

The artifact-governance slice builds one primary registry for OCP, Pattern, AD, ADR and AB identifiers. Duplicate primary identities fail closed. Historical reviewed-contract snapshots remain versions of their owning OCP artifact and do not create another primary identity.

Primary-artifact `Depends-On` metadata accepts only exact identifiers in those registries. Unresolved, repeated, malformed and self references are rejected. `Depends-On: P-NNN` records an artifact dependency only; it cannot replace the versioned `Uses-Patterns` invocation contract.

Every primary OCP document must declare a SemVer `Version`. The checker enforces the mechanically expressible OCP-001 lifecycle boundary: `Draft` and `Accepted` documents use `0.x`, while `Canonical` documents use `1.x` or later. It also enforces the L2 repository-tree witness: a Canonical OCP cannot directly depend on a pre-canonical OCP. A same-act group passes only when every direct OCP dependency is Canonical in the same proposed tree. It does not decide that a document is semantically ready for Canonical status, prove compatibility, authorize an L2 exception or replace the separate Board act and external review.

OCP-002 `Concept-Statuses` is checked as an exact projection of Concepts declared by primary defining OCP metadata: every defined Concept must appear once with the same status, and duplicate keys plus extra category, candidate or non-Concept rows are rejected. OCP-000 may still contain Proposed candidate markers without defining OCPs; they do not enter this projection until a separate governed Concept act creates the defining metadata. The checker witnesses set/value consistency only and does not award a lifecycle status.

`STATUS_PEER_VIEW_MISMATCH` additionally checks the current human-readable peer-table shape: inside every defining-document section titled `Concept Status and Dependencies`, a table beginning with `Concept | Status` must render every registered Concept exactly once within that section, with the value from OCP-000. The rule scans all matching sections in all defining documents rather than a fixed path list. It ignores unregistered descriptive terms and does not cover historical tables outside those sections or ASCII `[Status]` tree labels. OCP-000 remains the sole status authority; this check only detects drift and cannot grant, select or infer lifecycle.

These checks are intentionally structural. They do not infer that two differently worded normative passages are semantically equal or contradictory. External adversarial review retains that responsibility.

## Authority and exact references

Checker fixtures serialize some opaque governed references as `identity@version`. The delimiter is harness syntax unless the owning OCP document explicitly makes it normative.

Resolvers use exact normalized identities. They do not select by:

- label;
- newest timestamp;
- list order;
- source count;
- evaluator count;
- superseding record recency;
- fuzzy similarity.

Zero or multiple exact candidates fail closed.

## Organization Q2 envelope

OCP-007 `1.1.1 / Canonical` keeps one semantic owner and exposes two bounded validation surfaces. Organization records have dataset-scoped exact IDs, authoritative finite history and optional opaque `classification_refs`. Equal or missing annotations do not change identity; merger/split continuity remains a human governance question rather than a checker projection.

Established relationship records resolve both Organization endpoints exactly once and bind `relationship_type_ref` to exactly one synthetic `OrganizationRelationshipKindProfile`:

```yaml
validation_scope_ref: SCOPE-A
relationship_kind_profiles:
  - kind_ref: domain-kind://structural@1
    profile_owner_ref: domain-owner://organization-relations@1
    relationship_class: structural
```

The checker validates only the shared exact-resolution/class-agreement envelope. A fixture owner reference is attribution, not proof of legitimate authority, and the profiles do not form a Core registry. Structural `scheme_ref` values are opaque exact partition keys inside one declared dataset/scope. The full breakpoint sweep rejects cycles and multiple direct superiors unconditionally.

Supersession targets resolve exactly and remain acyclic. Branching, overlap and gaps are allowed. `organization_relationship_successor_ids` exposes every branch in stable order but neither redirects an old reference nor elects a current head. The mandatory Q2 fixture covers all seventeen AD-019A mechanical evidence groups with exact expected error sets.

## Operation-local spatial-binding envelope

OCP-004 `0.8.0` implements AD-014B Outcome A without creating `Operational Area` identity. A fixture may omit `spatial_context`, provide an exact empty context, or carry one or many local bindings:

```yaml
entity:
  operation_id: OP-SPATIAL-001
  planned_start: 2026-08-06T09:00:00Z
  spatial_context:
    context_version_ref: OP-SPATIAL-001-CONTEXT@1
    bindings:
      - binding_id: LOCAL-WORK-AREA
        binding_version_ref: LOCAL-WORK-AREA@1
        purpose_ref: work-area@1
        representation_profile_ref: synthetic.opaque-spatial@1
        payload_snapshot_ref: SYNTH-SPATIAL-SNAPSHOT-A@1
        temporal_scope: planned-context
        provenance_ref: ACT-BINDING-A
references:
  spatial_representation_profiles:
    - profile_ref: synthetic.opaque-spatial@1
      profile_owner_ref: domain://synthetic-spatial
  spatial_payload_snapshots:
    - snapshot_ref: SYNTH-SPATIAL-SNAPSHOT-A@1
      representation_profile_ref: synthetic.opaque-spatial@1
      opaque_payload_ref: synthetic://spatial-payload/a@1
      provenance_ref: ACT-SPATIAL-A
```

The checker validates local identity, exact version syntax, unique binding IDs/versions, exact single profile and snapshot resolution, profile agreement, planned/actual context presence and a closed fixture envelope. Spatial payload stays opaque; no coordinates, geometry or sensitive data enter Core fixtures.

`OperationSpatialTransitionEvidence` compares preserved previous/current snapshots. A substantive spatial change must mint a new context version, and changed content for the same local binding must mint a new binding version. The evidence does not introduce P-001 supersession lineage or select a current record by timestamp/order.

Equal payload references in two bindings or Operations remain distinct local subjects. Unknown, absent, duplicate, ambiguous or mismatched profile/snapshot input fails closed. Binding fields for Resource, Assignment, Organization, coordination, conflict, visibility, overlap, suitability, admissibility, availability, authorization, selection and Readiness are rejected; the checker derives none of those conclusions.

## Operation Q3I and lifecycle evidence

The bounded `OperationQ3IContractDataset` harness exact-binds current synthetic Operation examples to `OCP-004@0.9.0`. Existing OCP-004 `0.8.3` fixtures continue to replay without that marker; the marker distinguishes executable contract context and is not a production wire-schema field.

For OCP-004 the harness checks:

- fixed, separate F1/V1 kinds and provenance while preserving the existing exact intent/rule/input evidence-set semantics;
- unique Operation and record identities;
- exact parent resolution and acyclicity;
- IO2 source ownership, exact target resolution, the closed four-value kind set and duplicate-tuple rejection; and
- absence of independent IO2 record ID, effectivity, history, supersession or current-head fields.

For OCP-017, a lifecycle envelope names one exact Operation and carries an authoritative set of `operation-lifecycle-transition@1` records. `predecessor_transition_ref` creates the single chain. The current stage is the target of its unique leaf, not the last YAML item or greatest timestamp. Timestamp order is checked only along the already exact chain. Branches, cycles, disconnected records, competing roots/leaves and materialized-stage mismatch fail closed.

For Accepted OCP-018, `operation-authorization-decision@1` exact-binds one source profile, source owner, subject Operation, authorizer Organization, Capability version, decision level and input snapshot. A unique effective supersession head derives `accepted` only for an eligible `authorize` decision whose exact OCP-017 binding matches. Denial derives `denied`; stale, ineligible, wrong-level, conflicting, unresolved or forbidden coupling derives `indeterminate`. Stored `accepted`, newest timestamp, list order or source/issuer count cannot override the derivation.

For Accepted OCP-019, `conflict-establishment-boundary@1` exact-binds a derivation request to one or more OCP-006 `ConstraintEvaluationRecord` references, one context and one input snapshot. Complete definitive evidence derives only `conflict_not_established`; missing, duplicate, contradictory, cross-bound, stale or indeterminate evidence derives `indeterminate`. Neither one violation nor many violations can derive Conflict. Positive Conflict, Risk, lifecycle, Assignment, remediation, precedence/waiver and quantity/capacity couplings are rejected. AD-023 gate probes separately omit each OCP-019 §9 activation group and include one structurally complete but self-declared attempt; all remain invalid and derive only `indeterminate` without changing the OCP-019 manifest or checker behavior.

For Accepted OCP-020, `exact-unit-quantity-sum@1` exact-binds one profile owner, measurement profile, context and current input snapshot. It derives only a canonical decimal total for exact same-role, same-unit and same-dimension `demand` or `consumed` operands. Mixed, missing, ambiguous, stale, cross-bound or forbidden capacity/reservation coupling fails closed. The checker neither authenticates a production profile nor compares demand with capacity.

For Accepted OCP-021, `whole-resource-reservation-allocation-boundary@1` and `quantitative-reservation-allocation-boundary@1` remain mechanically separate. Exact current Resource/Assignment/Constraint evidence derives only the E-specific negative result; Q additionally requires exact `OCP-020@0.2.0` and one quantitative snapshot reference, but still derives only the Q-specific negative result. Branch crossover, stale/ambiguous/cross-bound evidence, caller self-supply and every positive Reservation/Allocation/availability/capacity coupling fail closed as `indeterminate`.

For Accepted OCP-022, three exact rules separately test whether Order is mandatory, sufficient or an admissible authorization source. One request exact-resolves one current synthetic evidence snapshot bound to `OCP-018@0.2.1`; even definitive `accepted | denied` source evidence derives only the matching negative establishment result. Malformed, stale, ambiguous, mismatched, convenience-selected, self-supplied, Concept-coupled or positively authoritative input fails closed as `indeterminate`. The checker does not define Order or authenticate an owner, evaluator or production profile.

For Draft OCP-006 `0.3.0`, `constraint-application-order-boundary@1`, `constraint-override-boundary@1` and `constraint-waiver-boundary@1` remain mechanically separate. Exact current Constraint-version inputs bound to one context/snapshot derive only `constraint_application_order_not_established`, `constraint_override_not_established` or `contextual_waiver_not_established`. Application-order replay is permutation and provenance invariant. Missing, ambiguous, stale, cross-bound, cross-branch, self-targeting or positive-coupled evidence fails closed as `indeterminate`; the checker creates no precedence, suppression or exemption authority.

Manifests may opt into direct fixture coverage with `fixture_coverage.status: complete` and one fixture concept. A generic test requires the exact validation-ID set to be named by direct fixture expectations. OCP-006 interaction boundaries, OCP-018, OCP-019, OCP-020, OCP-021 and OCP-022 opt in; legacy manifests make no untrue completeness claim.

Every transition exact-binds one domain completeness profile and passed input snapshot. Only the transition to `Authorized` carries an exact external authorization-evidence binding; the checker validates its structural agreement but neither authenticates the source owner nor grants permission. Terminal transitions exact-enumerate Assignment dispositions at the transition time using OCP-005 `assignment_effective_at`; the evidence cannot mutate Assignment.

The positive synthetic fixture covers a complete `Draft → Planned → Authorized → Active → Completed` path and a still-effective Assignment that remains independently effective. Four separate invalid fixtures make missing F1 authoring provenance, missing V1 evidence provenance, branched LT2 history and hidden IO2 record identity fail through the same fixture gate in both contexts. Focused unit attacks cover the remaining ambiguous/missing/failing evidence, invalid time/projections, unresolved relations, composition cycles and forbidden authorization/Event/outcome/Readiness coupling.

This module is not a lifecycle engine, authorization mechanism, persistence schema, Constraint evaluator, Event generator or outcome assessor. Legitimate ownership, domain sufficiency, external permission and production behavior remain human-reviewed responsibilities.

## Event and ObservationRecord envelope

OCP-010 defines Event as reusable occurrence identity and ObservationRecord as a separate attributable record.

`resolve_event(events, event_ref)` compares exact `event_id` only. Equal kind or time does not collapse identity.

`observations_for_event(observations, event_ref)` returns all structurally valid exact-linked observations. The deterministic output sort has no truth or priority meaning.

ObservationRecord without `event_ref` remains a valid unresolved assertion. Supersession preserves prior records, allows branching and defines no newest/current/truth winner.

## OutcomeAssessmentRecord envelope

OCP-011 defines the assessment fixture contract:

```yaml
assessment:
  assessment_id: ASM-001
  assessment_kind_ref: objective-achievement@1
  target_kind_ref: objective@1
  target_ref: OBJ-001
  criterion_ref: neutral.asset-condition-assessment@1
  evidence_bindings:
    - evidence_kind_ref: observation-record@1
      evidence_ref: OBS-001
  evidence_snapshot_ref: SNAP-EVIDENCE-001
  input_snapshot_ref: SNAP-INPUT-001
  evidence_state: sufficient
  evaluator_ref: EVALUATOR-001
  evaluated_at: 2026-08-04T01:00:00Z
  recorded_at: 2026-08-04T01:01:00Z
  conclusion: achieved
  provenance_ref: ACT-ASM-001
  supersedes_assessment_ref: ASM-000 # optional
```

The initial reference subset supports:

- target kind `objective@1`;
- evidence kinds `event@1` and `observation-record@1`;
- conclusions `achieved`, `not_achieved`, `partially_achieved`, `indeterminate`;
- evidence states `sufficient`, `missing`, `stale`, `ambiguous`, `conflicting`.

Definitive conclusions require `evidence_state: sufficient`. Missing, stale, ambiguous or conflicting evidence permits only `indeterminate` in the baseline contract.

Evidence bindings must exact-resolve and exactly equal the immutable set stored under `evidence_snapshot_ref`. `input_snapshot_ref` must resolve independently. Current repository state is never substituted during replay.

The finite conflict probe detects disagreement among normalized bound ObservationRecord statements. It is a regression guard, not a production truth, semantic-equivalence or source-reliability engine.

For `objective-achievement@1`, the checker mechanically derives and cross-checks `missing` and the finite `conflicting` probe; `stale` and `ambiguous` remain evaluator-attributed F0/A0 declarations.

Exact `objective-achievement@2` activates the OCP-011 F1/A1 envelope. Its record and immutable input snapshot exact-bind one criterion-local freshness rule plus one ambiguity rule. The checker derives inline `freshness_state`, `ambiguity_state` and findings from exact Event/ObservationRecord temporal facts and offset-aware `evaluated_at`, using explicit microsecond comparison precision and integer-second cutoffs, then cross-checks `evidence_state`. Unknown rules, mismatched snapshots, missing evidence, future/incomparable time and declared-state disagreement fail closed.

`derive_outcome_evidence_usability` replays the historical record without wall clock or current-state lookup. An optional explicit query time creates a new view and never mutates the historical record. The non-sensitive 600/3600-second fixture policies belong only to their exact reference criterion and are not defaults.

`effective_outcome_conclusion` fails closed to `indeterminate` for an activated head unless the caller supplies the complete exact Objective, evidence, snapshot and rule context. A structurally valid record alone is not activation authority.

OutcomeAssessmentRecord supersession:

- preserves prior exact resolution;
- rejects self-reference, unresolved targets and cycles;
- allows branching;
- requires assessment kind, target and criterion binding identity to remain unchanged across an edge;
- does not select a newest or preferred record.

`outcome_assessment_heads` returns unsuperseded exact-bound records. `effective_outcome_conclusion` returns `indeterminate` when heads disagree or use different evidence/input snapshots. List order does not affect the projection.

The validator rejects embedded Result, Operation lifecycle-success, Objective mutable status, Capability, Readiness, authorization, Conflict, Risk and State convenience fields.

## CapabilityClaimRecord envelope

OCP-012 defines a separate identified record for one claimant's proposition about one exact Resource and one exact OCP-009 Capability version under one condition set. The checker keeps declaration authority narrow: `support_state: declared` records what the claimant said and never marks it independently verified.

`holder-capability@1` retains the F0/A0 baseline: the checker cross-checks support/evidence shape and snapshots, while `sufficient`, `stale`, `ambiguous` and `conflicting` remain attributable recorder statements. Activation fields on that legacy kind are rejected.

Exact `holder-capability@2` requires an explicit `declaration-only` or `evidence-backed` mode. Declaration-only carries no external evidence or evidence-rule fields. Evidence-backed mode exact-binds the OCP-012 source use, a governed evidence expectation, immutable evidence and rule-input snapshots, `support_evaluated_at`, condition-local F1/A1 rule versions and inline states. The checker replays Event `occurred_at`, ObservationRecord `observed_at` or OutcomeAssessmentRecord `evaluated_at` only when the exact local rule selects that fact.

The only accepted mode-changing Module C edge is same-assertion `declaration-only → evidence-backed`. Reverse and polarity-changing transitions reject; predecessors and branches remain visible. `derive_capability_claim_support_usability` reproduces historical classification or accepts a later explicit query time without mutating the claim. Missing rules, snapshots or historical evidence fail closed, and an activated positive projection requires complete exact validation context.

The reference slice supports Resource-only holders, exact Capability resolution, half-open effectivity intervals, evidence snapshots and branching supersession. Withdrawal is a successor assertion distinct from negative polarity. `capability_claim_heads` performs as-of replay; `effective_capability_claim` returns `indeterminate` for missing, stale, ambiguous or conflicting support and for disagreeing heads. It never uses newest timestamp, list order, claimant count or source count as authority.

Matching claim projections for two Resources preserve two Resource identities and do not decide AB-011 interchangeability.

## Resource interchangeability envelope

Accepted OCP-013 supplies the separate AB-011 decision. The checker resolves one consumer-owned exact requirement and derives one directional result from exact OCP-012 claim projections plus the OCP-006 decision for the same candidate, context and time.

The checker verifies generic requirement structure and exact resolution. It cannot establish whether an arbitrary `owner_ref` is a legitimate governed consumer contract; that authority remains with Architecture Board review. Accepted OCP-014 supplies one finite profile binding: a `CoordinationResourceRequirement` must use exact owner `ocp-coordination-consumer@0.1.0`, and a different owner fails safe. This check does not authenticate or authorize the caller.

The output vocabulary is `positive`, `negative`, `indeterminate` and `review_required`. Missing, stale, ambiguous, conflicting, mismatched or unknown-version input cannot produce positive. A positive result is contextual eligibility only: it carries no availability, authorization, ranking, selection or Assignment-execution authority.

The mandatory-counterexamples fixture covers every AD-008 §12 case and exact rule-version replay. It deliberately preserves Resource and Assignment identities and contains no Resource-to-Resource equality edge.

## Accepted Coordination workflow envelope

Accepted OCP-015 keeps one proposal revision separate from every invited vertical's response. The checker validates immutable record identity, exact proposal binding, responder scope, temporal effectivity and one-to-one acyclic supersession for both record families.

`derive_coordination_evidence` returns `positive`, `negative`, `withdrawal` or `indeterminate` for one exact snapshot under `coordination-evidence@1`. Missing responses, conflicting heads, stale proposal revisions, malformed lineage or forbidden authorization/selection/Assignment coupling fail safe. Record order, timestamps and response count do not choose authority.

The fixture's actor references are opaque pre-bound test inputs. The checker proves neither actor authentication nor authorization and cannot turn a positive evidence projection into permission, commitment, Resource selection, reservation or Assignment execution.

## Integrated non-sensitive scenario

`IntegratedEventScenario` composes:

```text
Objective
→ Completed Operation
→ Resource + Established Assignment participation
→ applicable Constraint
→ Event
→ conflicting ObservationRecords
→ OutcomeAssessmentRecord
```

The cross-Concept joints are executable:

- `derived_participates_in` verifies Assignment participation;
- `constraint_applicable_to` verifies the Constraint target/context joint;
- `effective_constraint_result` verifies exact evaluation selection;
- Event and Observation references resolve exactly;
- OutcomeAssessmentRecord binds the exact Objective, evidence and input snapshots.

The accepted PR-0012 scenario now uses the proposed OCP-011 record contract rather than the former checker-local assessment probe. Conflicting evidence produces `evidence_state: conflicting` and `conclusion: indeterminate`.

The scenario proves that `Completed ≠ achieved`. Assessment conclusion does not mutate Operation lifecycle or create Capability, Readiness, authorization, admissibility, Conflict, Risk or State.

## Process-audit boundary

GitHub Rulesets remain the preventive authority for pull-request-only, squash-only and linear-history enforcement. The checker is a post-factum audit.

In `pr` context the audit skips the synthetic GitHub merge ref. In explicit `main` context it requires complete non-shallow history, validates the governed baseline and rejects any later merge commit.

PR CI also checks out the actual proposed head and runs the repository checker in `main` context. This is the mechanical Board-gate used for atomic Concept or registry transitions.

## Fixture contract

Each YAML fixture includes:

```yaml
case_id: stable-test-id
concept: governed fixture class
expected:
  valid: true | false
  error_codes: []
```

Depending on the fixture class it may also include:

```yaml
entity: {}
entries: []
events: []
observations: []
objectives: []
assessments: []
evidence_snapshots: []
input_snapshots: []
scenario: {}
contexts: []
reference: {}
```

For invalid fixtures, `error_codes` must equal the complete emitted set. Unexpected additional or missing errors fail CI.

The fixture format is a test harness, not an implementation-facing API schema.

## Regression evidence

The suite includes, among other cases:

- silent Assignment termination and invalid projections;
- contradictory or stale Constraint evaluations;
- exact Capability references and supersession;
- zero-observation Event and distinct equal-time Events;
- unresolved, duplicate and conflicting observations;
- missing/conflicting assessment evidence with `indeterminate`;
- stale evidence attempting a definitive conclusion;
- unresolved assessment target/evidence/snapshots;
- late evidence producing a successor without rewriting history;
- branching assessment heads and order-independent `indeterminate` projection;
- assessment supersession cycle and binding-identity change;
- forbidden Result/lifecycle coupling;
- zero/one/many local spatial bindings and equal-payload identity separation;
- unresolved/duplicate profiles and snapshots, profile mismatch and invalid temporal scope;
- spatial context/binding version reuse and forbidden authority coupling;
- valid and invalid integrated scenarios;
- artifact, Pattern, Concept-status, graph and Git-history governance probes.
- foundation promotion-gate probes that validate schema-5 append-only candidate cycles, independently derive every OCP-005/006/010 dependency and L2 result, preserve selection → document promotion → Concept canonicalization ordering, reject selection self-supply/skipped steps and prove a complete later cycle reachable in an isolated tree without changing checker code;
- foundation post-discovery reassessment probes that derive L2 from live OCP frontmatter before cross-checking gate claims, pin the common five-axis comparison across hold/Assignment/Event/joint Assignment+Constraint/Constraint remediation, reject recommendation-to-selection transfer, and bind every historical evidence path to its baseline blob/SHA-256;
- Event stable-surface discovery probes that independently derive all seven OCP-010 inputs and both primary consumers, distinguish exact Pattern/record-kind bindings from unversioned document bindings, pin every declared stable/moving/blocker evidence token and retain candidate-specific Board selection as the sole remaining lifecycle gate.
- Assignment stable-surface discovery probes independently derive the non-empty Resource/Operation Concept dependency floor and all six direct consumers, distinguish five Accepted compatibility obligations from one Draft influence after OCP-021 acceptance, classify all eleven OCP-005 questions, pin six bounded candidates/seven moving surfaces/four blockers and prove that the Event cycle remains the only completed cycle with no active successor.
- Constraint stable-surface discovery probes enumerate all twelve current OCP-006 questions, bind the four resolved entries to AD-025/026/027, reuse the existing whole/local/outside vocabulary, pin five bounded candidates and eight moving surfaces, and isolate Q6 dynamic-input evaluation currentness as the sole whole-document blocker without editing OCP-006 or opening T7.
- Constraint Q6 sufficiency probes derive OCP-006, all six direct dependencies and all nine Accepted direct consumers; classify every freshness basis as direct norm, non-exhaustive list inference or silence; prove OCP-011 horizons are contract-local and non-transferable; and replay ancient/future `evaluated_at` mutations beside an exact-binding control. The current checker remains age-blind, OCP-006 expressly keeps general freshness open, and Q6 plus its whole-freeze blocker remain unchanged.
- Constraint document-status readiness probes derive seven lifecycle criteria from exact current OCP-001/OCP-016 tokens, reject promotion criteria invented by stable-surface practice, scan all 23 Accepted/Canonical primary OCP documents and bind five current open-question carriers. They assess every criterion separately: an OCP-006 Accepted transition remains possible only through a separate complete act, while Canonical L2 fails on Draft OCP-005; no status, question, candidate or cycle changes.
- Assignment Q2 amendment-attempt probes keep the question and `AMENDMENT_MODEL_ABSENT` blocker open, derive all five current Accepted consumers, bind four absent owner obligations and prove with unchanged-history variants that current validation accepts changed established role/applicability values without supersession or amendment provenance; the evidence itself remains non-positive while the hypothetical closure is G4-gated.
- consumer-need discovery probes derive every current Accepted/Canonical lifecycle artifact and Accepted governance act from live frontmatter, now including the three Accepted negative boundaries and AD-037; they distinguish current own-obligation need from negative, deferred, historical and already-satisfied statements, pin every candidate/output/gate token and reject any invented unmet need, activation or promotion-cycle start.
- Assignment consumer-compatibility evidence derives all five current Accepted `Depends-On: OCP-005` documents, pins each consumed text token to the AD-035 bounded surface, replays four negative-exclusion fixtures and the positive OCP-017 terminal-alignment fixture, rejects any restored compatibility blocker or changed consumer result, and leaves all moving surfaces, three semantic blockers and promotion gates unchanged.
- Assignment Q9 sufficiency probes compare the current minimum record shape, executable discrimination, Accepted-consumer ownership and both pressure/norm survivor classes against a predeclared five-part threshold; the extra-interval probe remains valid while an end-before-start control fails, so Q9, all other open questions, the temporal blocker, Assignment readiness/status and the promotion candidate set are held unchanged.
- Assignment Q2 sufficiency probes separately evaluate direct owner text, non-exhaustive enumerations and silence, compare Q2 against the Q3-pass/Q9-fail calibration, replay role/applicability replacements beside an invalid-role control and require both pressure/norm survivors; Q2, every other open question, the amendment blocker, Assignment readiness/status and promotion state remain unchanged.
- Draft Route D Resource-occupancy probes reuse current single-Assignment effectivity over an exact synthetic complete Resource snapshot, retain every effective witness in identity order, cover zero/one/overlap/gap/start/end cases and fail closed on missing completeness, activation or conflict/priority/capacity/reservation/authorization coupling.
- Event promotion-selection probes that keep the recorded OCP-010 subject Draft while binding its exact baseline state and per-path evidence blob/SHA-256, the exact Board selection, both Accepted consumers, all three compatibility blockers, zero-at-selection migration and atomic rollback; completed discovery/reassessment witnesses bind immutable baseline objects while the live gate separately requires the Event lifecycle promotion act.
- Event Concept canonicalization probes separate current status carriers from immutable baseline witnesses, reject any registry/taxonomy/defining/current-projection drift, rederive stable dependencies from live metadata and replay Event identity, observation-history, integrated-assessment and primary-consumer evidence without changing fixtures.
- Event lifecycle-promotion probes independently require all three precondition proofs, stable absence of a Core Operation↔Event edge, OCP-011 governed assessment ownership, live OCP-011/OCP-017 compatibility fixtures, atomic final-gate completion and immutable historical subject witnesses before OCP-010 may be `1.0.0 / Canonical`.
- current numeric-accounting probes derive the primary OCP and defined-Concept status distributions from live frontmatter, snapshot evidence from its governed map, P-001 invokers from structured `Uses-Patterns`, and fixture/test totals from the executable tree; the exact central README claim must follow those sources while historical act-local counts and non-formula readiness estimates remain outside the derivation.

## Time handling

ISO-8601 timestamps with offsets are normalized to UTC. A naive timestamp is interpreted as UTC by this reference checker. Canonical time, interval uncertainty and clock-source policy remain separate decisions.

## Run locally

```bash
python -m pip install -r tools/ontology_checker/requirements.txt
python -m unittest discover -s tools/ontology_checker/tests -v
python tools/ontology_checker/check.py tools/ontology_checker/fixtures
python tools/ontology_checker/check.py tools/ontology_checker/fixtures --context main
```

## Explicitly deferred

This slice does not provide:

- production persistence, API, UI or transport contracts;
- a production Event registry, correlation or truth-selection engine;
- universal source reliability, confidence or causal inference;
- criterion expression language or evaluator authorization;
- quantitative partial-achievement semantics;
- automatic multi-Objective or multi-Operation aggregation;
- production holder-claim persistence or API contracts;
- Constraint-result assessment evidence kind;
- reusable area identity, geometry/CRS/topology or overlap/containment evaluation;
- cross-profile spatial equivalence or a production domain-profile registry;
- authorization, Conflict, Risk, Readiness or State semantics;
- machine-complete semantic duplicate detection in natural-language normative prose.
