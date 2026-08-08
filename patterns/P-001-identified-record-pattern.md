---
Pattern-ID: P-001
Title: Identified Record Pattern
Version: 0.1.0
Status: Accepted
Normative-Level: binding-when-invoked
Owner: Architecture Board
Depends-On: AD-001, OCP-001
Last-Review: 2026-08-08
---

# P-001 — Identified Record Pattern

## 1. Purpose

P-001 defines a reusable modeling contract for a relation, assertion or contextual record that requires independent identity and one or more governed lifecycle, temporal, provenance or supersession properties.

P-001 defines form. It does not define domain meaning.

## 2. Invocation

A normative artifact invokes this pattern through versioned metadata:

```yaml
Uses-Patterns: P-001@0.1.0
```

Invocation is optional. Once invoked, all Required Elements are binding, and every selected Optional Module brings its stated obligations.

The invoking artifact remains the only normative home for domain semantics, endpoint meaning, allowed kinds and domain-specific invariants.

## 3. Applicability threshold

An identified record should be considered when a modeled relation or assertion requires at least one of:

- independent identity;
- explicit endpoint contract;
- temporal effectivity;
- lifecycle or transition history;
- provenance or evidence;
- supersession or amendment history;
- record-specific attributes;
- record-specific authorization or constraints.

A direct reference or derived edge may remain simpler when none of these properties is required.

## 4. Required Elements

Every P-001 invoker defines:

1. **Stable record identity** — a non-empty identifier unique in the invoking model.
2. **Owning semantic specification** — one normative location for the record's meaning.
3. **Endpoint contract** — named endpoint fields, allowed endpoint types and unambiguous directionality when endpoints exist.
4. **Governed kind reference** — a stable, versioned kind or type reference when multiple semantic kinds are permitted; arbitrary free-form type strings are not normative.
5. **Provenance contract** — the minimum provenance structure required to establish or authorize the record.
6. **Validation contract** — verifiable invariants, including at least one invalid counterexample for each material rule where expressible.
7. **Authority declaration** — which stored record or derivation is authoritative when the same semantics has multiple representations.

Not every identified record must connect two endpoints. An invoker may declare an endpoint-free assertion form, but must do so explicitly.

## 5. Optional Module A — Temporal Effectivity

When selected, the invoker defines:

- start boundary;
- optional end boundary;
- interval inclusivity or exclusivity;
- treatment of absent bounds;
- the exact `effective_at(record, t)` derivation;
- behavior for invalid or incomplete timestamps.

A stored convenience field must not silently create a more permissive effective result than missing or indeterminate authoritative data.

## 6. Optional Module B — Transition History and Projections

When selected:

1. allowed lifecycle stages and paths are explicit;
2. transition history is either declared authoritative or explicitly secondary;
3. every transition record has identity, record reference, source stage, target stage, occurrence time and provenance;
4. transition timestamps are ordered under a defined rule;
5. current stage and lifecycle timestamps are deterministic projections;
6. materialized projections are optional unless the invoker explicitly requires them;
7. when present, materialized projections equal authoritative derivations;
8. invalid branching or mutually exclusive paths are prohibited.

The invoker defines the exact projection names and lifecycle semantics.

## 7. Optional Module C — Supersession

When selected, the invoker defines:

- the superseded record reference;
- prohibition of self-supersession;
- whether supersession is one-to-one or may branch;
- whether overlap or gaps are allowed;
- which record is effective during overlap;
- provenance for the replacement decision.

Supersession does not rewrite the history of the prior record.

## 8. Optional Module D — Defense in Depth

P-001 does not create a separate universal defense-in-depth doctrine. Invokers follow the invariant requirements already defined in OCP-001.

Where invalid stored data can bypass validation, a derivation may independently normalize it to a non-permissive result. Such duplication must be documented as intentional and tested at both layers.

## 9. Anti-patterns

### AP-1 — Pattern as semantic container

Do not move domain meaning into P-001 or into generic type strings. Shared form is not shared semantics.

### AP-2 — Universal relationship object

Do not reduce Assignment, Constraint or another specialized Concept to a generic record merely because it has endpoints.

### AP-3 — Hidden authoritative convenience field

Do not allow a materialized lifecycle or effectivity field to override the declared authoritative history or derivation.

### AP-4 — Invocation without version

Do not declare `Uses-Patterns: P-001` without a version reference.

### AP-5 — Partial invocation by silence

An invoker may omit an Optional Module, but may not use that module's fields while avoiding its obligations.

## 10. Conformance statement

A conforming invoking artifact documents:

- the P-001 version;
- selected optional modules;
- mapping from P-001 elements to local field names;
- domain-specific rules and invariants;
- positive and negative fixtures where the executable reference supports them.

## 11. T3 acceptance evidence

At the T3 acceptance merge `645b22b27be8ff004bd98e4b918403335f300278`, P-001 had six primary invoking contracts. Those contracts exercised endpoint-bearing and endpoint-free records, temporal effectivity, transition history, supersession and explicit authority boundaries without moving their domain meaning into this Pattern.

This paragraph is evidence for that exact acceptance baseline, not a live count at read time. The current invoker set is always derived from structured `Uses-Patterns` metadata in the tree being reviewed.

Similarity of implementation helpers alone does not justify a new pattern. Future patterns require repeated independent use, stable form, demonstrated drift reduction and absence of domain semantics.

## 12. Accepted `0.1.0` compatibility surface

Acceptance stabilizes the form already defined in §§1–10 at exact version `0.1.0`. It does not make P-001 Canonical, because Pattern lifecycle has no `Canonical` status, and it does not make invocation mandatory.

For an exact `P-001@0.1.0` invocation:

1. the seven Required Elements in §4 are binding;
2. Optional Modules A–D are binding only when the invoker selects them;
3. the invoker owns its field mapping, domain semantics, endpoint meaning, allowed kinds and domain-specific invariants;
4. an omitted module creates no permission to use its fields or semantics silently;
5. no stored convenience field, timestamp, record order, issuer count or record count gains authority unless the invoker explicitly defines it; and
6. P-001 creates no universal record kind, fundamental Concept, Concept graph edge, domain authority or machine admission decision.

A future change to a Required Element, Optional Module or invocation obligation requires an explicit Pattern version change and external review. Under the repository's `track-current` policy, that change must update every current invoker atomically. The same act must explicitly classify immutable reviewed snapshots and, if their historical pins are to remain unchanged, amend the checker policy rather than creating a silent exception.

## 13. Exact T3 invoker evidence ledger

At the exact T3 acceptance baseline, these six primary invoking artifacts all bound `P-001@0.1.0`:

| Invoker | Identified record form | Selected modules |
|---|---|---|
| OCP-007 | OrganizationTransitionRecord | B |
| OCP-007 | OrganizationRelationshipRecord | A, B, C |
| OCP-008 | endpoint-free Objective record | C |
| OCP-010 | ObservationRecord; Event itself does not invoke P-001 | C |
| OCP-011 | OutcomeAssessmentRecord | C |
| OCP-012 | CapabilityClaimRecord | A, C |
| OCP-015 | separate CoordinationProposalRecord and CoordinationResponseRecord invocations | A, C for each form |

OCP-007 appears twice because one invoking artifact owns two independently mapped record families; table-row count is not invoker count.

Immutable reviewed-contract snapshots for OCP-011, OCP-012 and OCP-015 preserve the same exact `0.1.0` historical binding. Because this acceptance act does not change the Pattern version or §§1–10 obligations, every primary invocation and historical snapshot remains exact; no invoker migration is required.

The ledger is time-anchored human-readable review evidence, not a second invocation registry. Structured `Uses-Patterns` metadata and the repository checker remain authoritative for the current invoker set and reference completeness. No fixed current count is repeated in prose.

## 14. Mechanical and review boundary

Repository checks enforce the Pattern identifier, allowed lifecycle status, SemVer syntax, dependency resolution, exact `Uses-Patterns` syntax and the `track-current` version rule. They do not prove that an invoker has mapped all seven Required Elements correctly, selected every semantically used module, preserved a non-permissive authority boundary or kept domain meaning outside the Pattern.

External review therefore remains responsible for those semantic questions. At minimum it must try to falsify the invocation with a missing Required Element, an undeclared module, an ambiguous authority split, a permissive fallback or domain semantics hidden in generic record form.

## 15. Acceptance counterexamples

The following conclusions are invalid:

1. `Accepted` means `Canonical` or creates a stronger Pattern lifecycle state.
2. One accepted Pattern makes every relation or assertion a P-001 record.
3. Shared P-001 form makes two record families semantically equivalent.
4. A timestamp, newest record, storage order, issuer count or record count selects authority by default.
5. An invoker may use temporal, transition or supersession fields without selecting the corresponding module.
6. P-001 may supply domain meaning that the invoker has not defined.
7. A future Pattern version may merge before all current invokers and historical-snapshot treatment are explicit in the same reviewed act.
8. Completion of this T3 act authorizes any T4 promotion.

## 16. T3 acceptance act

The reviewed pre-acceptance baseline is Git blob `6750b65944c25a637fcfc621c8ccebde165e1604` with SHA-256 `af4de9980efdac3ed06b24d3d959a55eb418d4acc53832a05440b4f4711e0215`.

This act changes only the Pattern lifecycle status from `Draft` to `Accepted` and replaces the stale future-tense evidence statement with §§11–15. It keeps:

- version `0.1.0` and the complete §§1–10 form unchanged;
- `binding-when-invoked` scope;
- direct dependencies on Accepted AD-001 and Canonical OCP-001;
- all six primary invokers and three reviewed snapshots at exact `P-001@0.1.0`;
- domain authority in each invoking artifact; and
- every existing Concept, Concept status and Concept graph edge unchanged.

Architecture Board authorization for this act is separate from the T3 OCP-002 act and does not transfer to AD-016C, AD-016D or any T4 proposal. After acceptance, the T0–T3 enabling phase is complete, but AD-016C must recompute the readiness comparison and a separate AD-016D Board act must select what, if anything, proceeds next.

## 17. Evidence-accounting correction act

### 17.1 Exact baseline and defect

This correction starts from `main@34c4b5db52ce3627e727d8f69051352d14bd2c8d`, tree `33405dcfead41ba4a1ee1ce2aa11c3c5c55e1142`. P-001 is blob `f1e95efa055022a9342b16133bf7b3c3db90fa4f`, SHA-256 `cf6fb3501a1a5504aa873c372e97436813725c6e44a7fc682a2db404a7d97b82`, at `0.1.0 / Accepted`.

On that exact tree, structured metadata yields six primary invokers:

- OCP-007;
- OCP-008;
- OCP-010;
- OCP-011;
- OCP-012; and
- OCP-015.

Three immutable reviewed-contract snapshots—OCP-011 `0.1.1`, OCP-012 `0.1.0` and OCP-015 `0.1.0`—also preserve exact `P-001@0.1.0`. The complete mechanical footprint is therefore nine files, although only the six primary artifacts count as current invokers.

Sections 11 and 13 described that T3 acceptance evidence in the present tense as “six current” invokers. A later exact invocation by OCP-004 or OCP-017 would make those sentences false even though the Pattern form remained unchanged. Section 16 does not have this defect: its “This act ... keeps” construction records what the T3 acceptance act kept, and its exact pre-acceptance blob makes that historical claim independently replayable. Within the inherited §§11–16 body, this correction changes only §§11 and 13 and preserves §16 byte-for-byte; the updated `Last-Review` field and this new §17 record the correction itself.

### 17.2 Versioning adjudication

Two readings of OCP-001 must be distinguished explicitly.

1. **Literal byte-change reading.** OCP-001 says that Pattern changes are versioned and externally reviewed. Read without its preceding subject, any edit to this file would require `0.1.1`.
2. **Binding-form reading.** The preceding OCP-001 sentence defines a Pattern as modeling form. P-001 §12 binds version `0.1.0` to the complete §§1–10 form and requires a new version for a changed Required Element, Optional Module or invocation obligation. OCP-001's atomicity table requires invoker fan-out only **if** the Pattern version changes.

The Board chooses the binding-form reading for this correction. The reason is semantic, not merely the size of the diff:

- §§1–10 and every binding obligation in §12 remain byte-identical;
- no invoker receives a new or changed obligation;
- no Optional Module, authority rule, applicability threshold or conformance requirement changes;
- merge `645b22b27be8ff004bd98e4b918403335f300278` already established the reviewed precedent by adding §§11–16 and accepting the Pattern while retaining version `0.1.0`; and
- changing only the Pattern version would trigger `PATTERN_VERSION_MISMATCH` across six primary invokers and three immutable snapshots, falsely representing an unchanged form as a new contract and forcing unrelated historical treatment.

Version `0.1.0` therefore remains exact. Git history, exact-head external review and Board authorization version this evidence-accounting act as repository history; they do not manufacture a new Pattern-form version.

This is not permission for unreviewed same-version edits. Any future change to Pattern form, Required Elements, Optional Modules, invocation obligations, applicability or binding behavior requires a Pattern version change and the complete `track-current` atomic treatment. Any future evidence-only correction still requires exact-head external review, Codex adjudication, green CI and explicit Board authorization.

### 17.3 Non-recurring accounting rule

The correction time-anchors §§11 and 13 to the T3 acceptance merge instead of replacing six with another live number. Future invokers do not edit this ledger merely because they invoke the unchanged form.

For every proposed tree:

1. the current primary invoker set is the exact set of primary artifacts whose structured frontmatter contains `Uses-Patterns: P-001@0.1.0`;
2. reviewed-contract snapshots remain immutable historical bindings and do not become primary registry entries;
3. the repository checker verifies exact `track-current` version equality and reference completeness;
4. external review verifies each invoking family's Required Elements, selected modules, semantic owner and authority boundary; and
5. no prose count, timestamp, file order, consumer count or review count overrides structured metadata.

This rule prevents the same stale-counter defect when the seventh, eighth or later primary invoker is added. It does not make checker output semantic authority or allow a new invocation without its own artifact review.

### 17.4 Executable and rollback boundary

The admissible footprint for this act is exactly this P-001 file. It must preserve:

- `Version: 0.1.0`, `Status: Accepted` and `Normative-Level: binding-when-invoked`;
- §§1–10 and §12 obligations byte-identically;
- §§14–16 byte-identically;
- all six primary invoker files and all three reviewed snapshots byte-identically;
- the `track-current` checker policy and every checker rule/test/fixture; and
- every Concept, Concept status, dependency, graph edge, backlog status and readiness projection.

Required executable evidence is:

1. the nine-file structured binding sweep reproduces on the exact baseline;
2. no unanchored “six current” statement remains in §§11 or 13;
3. changing only P-001 `Version` to `0.1.1` would be rejected by existing `PATTERN_VERSION_MISMATCH` behavior, so this act does not disguise a cheap compatible bump;
4. artifact governance, process audit, Concept graph and generated map checks remain green; and
5. all unit tests and fixtures replay unchanged in PR and main contexts.

Rollback is one reviewed revert of this file. It changes no invoker or stored record. Reintroducing a live counter would restore the known defect and therefore requires an explicit contrary Board decision rather than an unreviewed text rollback.

### 17.5 Authorization boundary and effect

When exact-head reviewed, explicitly authorized and squash-merged, this act:

- time-anchors P-001 §§11 and 13 to the T3 acceptance evidence;
- keeps P-001 at `0.1.0 / Accepted` with its complete binding form unchanged;
- leaves §16 as the unmodified historical T3 acceptance record;
- makes structured `Uses-Patterns` metadata the sole current invoker-set source, consistently with §13's existing non-registry boundary; and
- removes the evidence-accounting blocker identified by AD-020A §37.4 without authorizing any new invocation.

It does not edit or authorize OCP-004, create or authorize OCP-017, change P-001 form or version, update an invoker or snapshot, alter checker policy, add a Concept/edge, resolve backlog or authorize the bounded Operation remediation. That remediation remains a separate future act with four fresh exact-head gates.
