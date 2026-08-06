---
Decision-ID: AD-019
Title: Organization Stable-Surface Discovery
Version: 0.2.0
Status: Accepted
Owner: Architecture Board
Depends-On: AD-016, OCP-000, OCP-001, OCP-002, OCP-003, OCP-007, OCP-016, P-001
Applies-To: AB-062, Organization stable-surface remediation
Review-After: Completion or failure of the selected OCP-007 remediation; then a fresh blocker/stability audit before any lifecycle proposal or T5 topology reopening
---

# AD-019 — Organization Stable-Surface Discovery

## 1. Mandate and purpose

AD-016N selected O7D: prepare one outcome-fair discovery of the Organization stable surface. It authorized a comparison, not an Organization model or OCP-007 edit.

OCP-007 already contains three plausible stable responsibilities:

1. one identified Organization independent of display name, commander, current relations, Operation and Assignment;
2. authoritative Organization transition history and deterministic projections; and
3. one local identified `OrganizationRelationshipRecord` contract with temporal effectivity, transition history, supersession and structural graph checks.

The same document also contains four unresolved semantic-authority groups:

- continuity through merger, split, reorganization and constitutive redesignation;
- required classification references without an exact owner or resolution rule;
- relationship class/type alignment without a legitimate kind contract; and
- structural-scheme identity plus an exception admitted by prose but rejected by every executable path.

An exact P-001 audit exposes a fifth, orthogonal record-integrity gap: endpoint resolution is not executable, provenance is only a non-empty string, and Module C does not yet state branching, overlap/gap, independent effectivity or replacement-decision provenance completely.

Treating the whole document as one stable surface would hide those gaps. Extracting or mapping first would choose an authority arrangement before the gaps are compared. AD-019 therefore compares layout and semantics separately.

Revision `0.1.0` selects no outcome and changes no OCP, Concept, Pattern, dependency, graph edge, schema, checker rule, fixture or backlog status.

## 2. Exact baseline

This discovery starts from `main@bbdb476d804dda190244c05e4b343b7a7b81b0c6`, tree `bdf17a072ac6d449813526fba4cb03548bc1beb2`, after the separately authorized AD-016N merge.

The exact governing inputs are:

| Input | State | Git object | SHA-256 |
|---|---|---|---|
| AD-016N | `0.15.0 / Accepted`; O7D selected for discovery only | blob `1fb8d963f7becd2b88971196ee9fe46b34ddc99f` | `87a9079cab57e00b1e84c8014253ddf238d44ad48bbbbc8b3b8ba43563979e39` |
| OCP-003 Resource | `1.0.0 / Canonical`; Resource `Canonical` | blob `71485bb337cfd59def2e0f1b18b474a7959bd30c` | `f8656769dd046f221843f627c746d0d6040c2e83c736b900370d60244fce8315` |
| OCP-007 Organization | `0.3.2 / Draft`; Organization `Accepted` | blob `543d579f9ce1033ff38d478d1663c71a10b5f118` | `93fdf3e2e71e844888306b22da4f46468418ed30f3a2a62b8a39a98e7c6b387b` |
| OCP-000 registry | `1.3.0 / Canonical`; Organization `Accepted` | blob `547ccae7f417cf3d0bff92db20e0ccb9933cc8c5` | `a088d0b9c73035270480ddc266abbd3b5f847625053fef7744468eb667753332` |
| OCP-001 governance | `1.0.0 / Canonical` | blob `33524fa3d18f3253faa9a854500be7ddfb20815f` | `da74645aa4f3cae10c7c59ae7b87abd1840544700e4a58e9efd3f6600a27f1cc` |
| OCP-002 projection | `1.3.0 / Canonical`; Organization `Accepted` | blob `3b676afcff63ac4b600fb382a67283d67f766c7f` | `e0112f751b7922904d7217c76102cc8d5e3382ce49f13d94e99c31af1275669e` |
| OCP-016 Core Boundary | `1.0.0 / Canonical` | blob `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| P-001 | `0.1.0 / Accepted`; exact OCP-007 invocation | blob `f1e95efa055022a9342b16133bf7b3c3db90fa4f` | `cf6fb3501a1a5504aa873c372e97436813725c6e44a7fc682a2db404a7d97b82` |
| OCP-009 Capability | `1.0.0 / Canonical` | blob `31163eacb0ca2a78b17b9d2466d99ef0c8b2d272` | `29362c815cb14f07bfd06775d1398498a27ace5ee5a4acaafde0eb39e902152a` |
| OCP-012 CapabilityClaimRecord | `0.3.0 / Accepted`; Resource-only holder | blob `cd2df0f1961b6d03eea0db66c8fdfce1f97cb235` | `d4d5b4441cf2d1f7fea2dae572fcfa60f22b0ebce0e23ae6a86f71d9f4edd122` |
| OCP-013 interchangeability | `0.2.0 / Accepted`; Resource-only candidates | blob `658a291b4c3b9a0229aba09d485c1137723fe70b` | `a20659422f847f49a9231b8c1d1dabc0d8b911d9667c44013280b1826f621a74` |
| OCP-014 Coordination profile | `0.2.0 / Accepted`; no Organization-name authority | blob `23bd05b4bb14fd7a85101bd5a8b3dd733b53dd99` | `72c789c7b15ab2fd8997f60ba8cfd9d89f0e7730407763d18fb222bac5f06a8c` |
| OCP-015 Coordination workflow | `0.2.0 / Accepted`; no caller/name authority | blob `ea60634e54faedabb8c5e08b036030c2f0e4e20b` | `6077136b2460cfc56d0e06af9137338cb494ac9a8e14df036e662d9240415b1d` |
| foundation map | Organization `Accepted`; dashed future mapping only | blob `38011129ab9bf2e0362df2255a57fa15d3c90e54` | `f8af51e97e193820d24323cd0db5262d4fe0d353cb93c9bec910834e3e7b70e8` |
| architecture backlog | AB-006/044–047/051/052 Open; AB-062 Planned | blob `4a89ddff138c22d884a20c2bfc2946f97ff70a0c` | `e5140247edda94591590807bdecaa38ea9f5bf4c02188af73890d2a4dec2589e` |
| Organization checker | reference-only structural validator | blob `b099095ed1ee3bb652d320994b235a574c8691f6` | `7e1890443abe4f92abd2a5e823ebbc9aa61b34a6471e76e5f176dc49068a0276` |
| Organization rules manifest | `0.2.0`; OCP-007 sources | blob `fd8b1c629ff24f5c07c0b2c9bb7c048c6f91c4ba` | `f33a4dadfe9d98e34698c4c99548a0d15980c35129d74729414ec3b9ae3b90d7` |
| Organization primary fixtures | three files | tree `cefa81c9030ac3da8971a68a107d55c7565e6a3c` | recursive manifest `01fff80b7c2f9c1c94a7c830834d49968afb8886c2dba1e4779ec2032da6c44c` |
| Organization graph regressions | three files | tree `7936aa998c610429e1aa7c15cb92e45558200d0a` | recursive manifest `861ac4bb3e115bd85e1130692ca98d60d071ce46cc7272acbf4857f920e7fd9d` |
| complete fixture set | 119 non-sensitive fixtures | tree `fe02d8a9f5d302ff35ddceda0477f7722e861629` | recursive manifest `737d961afffd0e64981021b186861d690b49218dd8a155a5acdef0389e7efd67` |

The foundation has three Canonical and five Accepted fundamental Concepts. Readiness remains approximately 70%. Counts, order, recent work, hash equality and green CI identify the baseline; they do not select meaning or authority.

## 3. Inherited mandates

Every admissible outcome must preserve all of the following.

1. Organization remains the accepted fundamental Concept for one identified organizational entity independent of any Operation, Assignment or temporary relation.
2. `organization_id` is independent of display name, commander, personnel, location, current relations, Operation, Assignment and non-constitutive classification changes.
3. A relation, name, commander, support channel or current structural position cannot create, merge or replace Organization identity.
4. `Organization ≠ Resource`. A future mapping must preserve both identities and cannot arise from classification, membership, a shared referent or label equality.
5. Organization membership or composition creates no Assignment, participation, Resource ownership, Capability claim, Readiness, availability, authorization, admissibility, selection or interchangeability result.
6. CapabilityClaimRecord holders remain Resource-only. Any exact Organization-holder extension requires a separate accepted act; AD-019 cannot introduce it.
7. Exact OCP-009 Capability version binding remains unchanged and `Capability ≠ Readiness` remains binding.
8. OCP-013 remains directional and Resource-specific. Equal Organization classifications or relations do not make Resources or Organizations equal or interchangeable.
9. `OrganizationRelationshipRecord` remains a local identified non-Concept record unless a later explicit route/owner decision changes its artifact home. No new fundamental Concept is presumed.
10. OCP-007 invokes exact `P-001@0.1.0`: OrganizationTransitionRecord selects Module B; OrganizationRelationshipRecord selects Modules A, B and C. Pattern form never supplies Organization meaning.
11. Transition history remains authoritative over optional projections. Newest timestamp, storage order or materialized current fields never replace it.
12. Structural, operational, administrative, support and coordination semantics remain distinct. One kind creates no other kind by implication.
13. Coordination and support create no command, ownership or structural-subordination authority; names and caller identity create none either.
14. OCP-007 retains `Concept-Depends-On: []`. This discovery adds no Organization→Resource, Organization→Capability or other Concept edge.
15. Missing, unknown, conflicting, ownerless or incomparable evidence fails safe. Timestamp, record order, source/issuer/reviewer count, majority and implementation popularity are not authority rules.
16. OCP-016 Route C is the current discovery route for shared non-Concept Organization record/boundary repair. Route F is tested only for a genuinely distinct extracted authority and cannot self-admit.

## 4. Decision questions

AD-019 asks:

1. Which exact OCP-007 statements form a stable Organization identity/lifecycle kernel?
2. Can real-world continuity events be excluded while `organization_id` remains an honest exact-reference identity?
3. If continuity is included, what legitimate owner and record/evidence decide merger, split, reorganization and constitutive redesignation without newest-record authority?
4. Why must an Established Organization currently carry `classification_refs`, and what contract makes each reference exact and unambiguous?
5. Can classification be optional non-authoritative annotation, or is an exact external interoperability envelope required?
6. Does `relationship_class` own the stable behavior, does `relationship_type_ref`, or must one exact class/type alignment contract bind them?
7. Which owner defines directionality, endpoint roles, reflexivity, graph constraints and temporal rules for a relationship kind?
8. Can `scheme_ref` be only a dataset-scoped opaque partition key, or does it require governed identity and cross-scheme resolution?
9. Should multiple direct structural superiors fail closed unconditionally, or can a legitimate versioned exception contract be defined now?
10. Does the current lifecycle describe record recognition/existence only, and is its finite path set sufficient for compatibility?
11. Are Organization and relationship identities unique and exact-resolvable, and what completes endpoint, provenance and Module C supersession obligations?
12. Are organizational units/composition part of Organization identity or an explicitly excluded future relation/model?
13. Does any current consumer require Organization/Resource mapping or Organization Capability holders?
14. Can identity and local relationship semantics remain two readable surfaces under one OCP-007 owner?
15. Would extraction reduce ambiguity, or instead create duplicate authority and P-001/reference migration?
16. What evidence would justify a joint mapping scope or T5 topology reopening?
17. Which exact later Board act may authorize a remediation proposal, and what must remain separate after that?

## 5. Terms that must remain distinct

| Term | Meaning here | Not implied |
|---|---|---|
| Organization identity | exact identity of one represented organizational entity under `organization_id` | display name, commander, classification, structural position or Resource identity |
| exact-ID continuity boundary | existing references remain bound to one exact ID; Core makes no automatic same/different decision for a material continuity event | proof that a merger/split preserves or destroys real-world identity |
| continuity decision | governed treatment of merger, split, reorganization or constitutive redesignation | newest record, matching name, shared personnel or majority view |
| classification annotation | value carried with an Organization but not used by Core to derive identity, hierarchy, role or mapping | membership in a Core taxonomy |
| relationship class | coarse OCP-007 behavior family such as structural or support | a complete versioned relationship kind contract |
| relationship kind | exact versioned semantics for direction, endpoint roles, reflexivity, graph and temporal behavior | arbitrary string containing `@` |
| structural scheme | context that partitions structural graph evaluation | Organization identity, universal hierarchy or cross-scheme equivalence |
| exception | separately governed permission to violate a named fail-closed structural rule | a label, reviewer waiver or checker bypass |
| composition/unit identity | explicit part-whole or organizational-unit semantics | structural subordination, classification `unit@1` or Resource mapping |
| Organization/Resource mapping | explicit governed relation/projection between preserved identities | identity collapse, participation or Capability inheritance |
| in-place two-surface layout | one OCP-007 owner with separately bounded identity/lifecycle and local relationship-record sections | two independent semantic owners |
| extraction | transfer of one defining responsibility to another exact artifact with no duplicate normative prose | copying or moving text for convenience |

## 6. Current OCP-007 section ledger

The labels below are discovery classifications, not accepted outcomes:

- **K** — candidate stable statement;
- **B** — unresolved authority or identity question blocking inclusion;
- **S** — candidate explicit exclusion; and
- **C** — cleanup or evidence text that cannot carry semantic authority.

| Section | Candidate stable content | Current B/S/C boundary |
|---|---|---|
| §1 Purpose | independent Organization plus local relation-record responsibility | no blocker if the two surfaces stay readable and one-owned (K) |
| §2 Definition | identified entity independent of Operation/Assignment/temporary relation | material-event continuity remains B |
| §3 Boundary | identity/non-implications and `Organization ≠ Resource` | “owns classification references” lacks an exact classification contract (B); mapping/holders/authority stay S |
| §4 Identity | ID independence from name, commander, location, relations and classification changes | merger/split/reorganization/redesignation treatment is B |
| §5 Organization structure | ID, display, transition history, provenance projections and no universal hierarchy field | required classification reference is B; display is non-identity K |
| §6 Organization lifecycle | finite Draft/Established/Retired/Cancelled paths and authoritative history | AB-046 must confirm scope; no operational state/Readiness implication (K/B) |
| §7 OrganizationTransitionRecord | identified same-Organization transitions with time/provenance | P-001 Module B form is K; continuity-event authority is outside this record (S/B) |
| §8 Relationship decision | local non-Concept relation structure under AD-001 | K if one owner and exact P-001 invocation remain |
| §9 Relationship structure | record identity, endpoints, time, history, projections and supersession | class/type and scheme fields are B; endpoint resolution and Module C completeness are also B |
| §10 Initial classes | five coarse non-equivalent behavior families | stable non-implications are K; taxonomy/kind completeness and alignment are B |
| §11 Relationship lifecycle | finite Draft/Established/Closed/Revoked/Cancelled paths | AB-046 scope confirmation remains B; real-world authority is not implied |
| §12 Derivations | history-derived Organization/relationship effectivity and complete structural breakpoint sweep | scheme identity/cross-scheme interpretation is B |
| §13 Business rules | identity non-implications, no universal parent, independent classes and history-preserving replacement | “governed kinds” is B until exact type owner/alignment exists; replacement rule is incomplete for Module C |
| §14 Semantic rules | class non-implications, no transitive coordination and fail-safe unknown class | rule 9 admits an ownerless exception while the checker rejects all cases (B) |
| §15 Organization invariants | ID, lifecycle history/projections, provenance/time and forbidden hierarchy fields | invariant 15.2 classification requiredness is B |
| §16 Relationship invariants | identity/endpoints/history/projections/effectivity/supersession and graph checks | duplicate/endpoint ambiguity is untested; invariant 16.13 covers only self-supersession; invariants 16.2–3 and 16.14–16 carry class/type/scheme/exception B |
| §17 P-001 conformance | exact Module B and A/B/C invocation with OCP-007 semantic ownership | endpoint/provenance/Module C completeness, governed kind and exception inputs remain B; Pattern cannot repair them |
| §18 Examples | human evidence for structural, simultaneous and cross-vertical relations | examples cannot establish kind/scheme/exception authority (C/B) |
| §19 Explicit exclusions | honest list of deferred continuity, taxonomy, composition, mapping, authority and implementation work | continuity cannot be excluded by one phrase if §4 still overclaims it (B/S); “future Coordination Concept” is stale cleanup (C) |
| §20 Open questions | exact backlog visibility | accounting only; rows remain Open (C) |
| §21 Review target | falsification direction | review evidence only; no semantic authority (C) |

No B row is closed by the age of OCP-007, Accepted Concept status, lack of direct consumers or green fixtures.

## 7. Current field ledger

### 7.1 Organization fields

| Field | Current role | Discovery treatment |
|---|---|---|
| `organization_id` | stable exact identity | K candidate; duplicate/ambiguous dataset resolution must be added to a positive contract |
| `classification_refs` | required for Established/Retired lineage | B: no exact owner, resolution, version or ambiguity behavior |
| `display_name` | current designation independent of identity | K only with explicit non-authority |
| `transition_history` | authoritative lifecycle history | K candidate under Module B and AB-046 review |
| `created_at` | record creation time | K; never identity or authority priority |
| `lifecycle_stage` | optional projection | K if equal to history |
| `established_at` | optional projection | K if equal to history |
| `retired_at` | optional projection | K if equal to history |
| `establishment_provenance_ref` | optional projection | K if equal to establishment transition provenance; provenance does not decide continuity alone |

### 7.2 OrganizationRelationshipRecord fields

| Field | Current role | Discovery treatment |
|---|---|---|
| `relationship_id` | stable record identity | K candidate |
| `relationship_class` | one of five coarse behavior families | K for closed label/non-implications; B for alignment/kind authority |
| `relationship_type_ref` | version-looking governed kind reference | B: delimiter-only validation and no exact owner/resolver |
| `source_organization_ref` / `target_organization_ref` | directed Organization endpoints | K for direction/type; B for exact zero/one/many endpoint resolution |
| `scheme_ref` | required structural partition | B: identity, namespace, equality scope and cross-scheme behavior undefined |
| `validity_start` / `validity_end` | half-open temporal effectivity | K candidate under Module A |
| `transition_history` | authoritative lifecycle history | K candidate under Module B |
| `created_at` | record creation time | K; never priority authority |
| lifecycle/time/provenance projections | optional history-derived values | K if exactly equal to history |
| `supersedes_relationship_ref` | history-preserving replacement link | B: only self-reference rejects; target resolution, branching, overlap/gap, effectivity and replacement provenance are incomplete |

### 7.3 Transition-record fields

| Field | Current role | Discovery treatment |
|---|---|---|
| `transition_id` | stable identity of one transition | K candidate; duplicate ambiguity must reject |
| `organization_ref` / `relationship_ref` | same-subject transition endpoint | K for equality to the containing subject; external exact resolution remains bounded by that subject |
| `from_stage` / `to_stage` | one allowed path step | K candidate under Module B/Y1 |
| `occurred_at` | non-decreasing transition occurrence time | K; never newest-winner or authorization priority |
| `provenance_ref` | attributable transition provenance | K for required attribution; B unless the later contract says explicitly that it grants no actor/continuity/exception authority and defines any required resolver |

The field ledger shows why an editorial cleanup is insufficient: required inputs carry unresolved semantic authority, exact identity/endpoint ambiguity is not handled, Module C is incomplete, and one prose exception has no representable owner.

## 8. Consumer and executable evidence

### 8.1 Exact consumer sweep

On the exact §2 baseline, the repository contains:

- zero OCP documents with direct `Depends-On: OCP-007`;
- zero current `Concept-Depends-On: [Organization]` edges;
- four discovery/provenance records with OCP-007 in `Depends-On`: AD-005, AD-011, AD-014 and AD-018; and
- registry/taxonomy/foundation-map projections of current Organization status, none of which consume Organization semantics.

This proposed AD-019 record becomes the fifth such discovery/provenance dependency in the PR tree because its own frontmatter exact-binds OCP-007. It is not a normative OCP consumer. A post-merge AD-019A sweep must therefore expect five AD records while preserving the zero-OCP-consumer result.

Current OCP prose establishes only negative or local boundaries:

- Canonical OCP-003 keeps `Organization ≠ Resource`, rejects automatic mapping and leaves AB-006/AB-052 open;
- OCP-004/OCP-005/OCP-006 reject participation, Assignment or Constraint implications from Organization membership;
- OCP-009 registry membership creates no Organization Capability;
- OCP-012 rejects Organization holders under its Resource-only claim contract;
- OCP-013 evaluates Resource candidates and imports no Organization equality;
- OCP-014/OCP-015 reject authority from Organization names, caller identity or labels; and
- the foundation map contains only a dashed future mapping view.

The empty normative consumer surface bounds immediate migration pressure. It does not prove that Organization semantics are unimportant, select an outcome or allow an ownerless required field.

### 8.2 Current executable surface

The current Organization validator witnesses:

- non-empty Organization and relationship identities;
- finite transition paths, complete transition fields, same-record references and non-decreasing time;
- exact optional projections from authoritative histories;
- required non-empty classification for Established/Retired Organization lineage;
- absence of universal hierarchy fields;
- a closed five-label `relationship_class` vocabulary;
- only presence plus the `@` delimiter for `relationship_type_ref`;
- directed non-reflexive endpoints, validity intervals and structural `scheme_ref` presence;
- self-supersession rejection;
- breakpoint-complete effective structural-cycle checks; and
- unconditional multiple-superior rejection within one exact string-valued scheme group.

The validator does not perform repository/dataset-wide duplicate Organization, relationship or transition identity checks and does not resolve relationship endpoints or supersession targets.

The three primary fixtures cover one Established Organization, one valid structural relationship and one invalid class. The three graph regressions cover one fixed-time structural cycle, one transient cycle and one multiple-superior case.

### 8.3 Evidence not present

No current executable witness proves:

- merger/split/reorganization/redesignation continuity;
- legitimate classification owner or exact reference resolution;
- relationship kind ownership, type resolution or class/type agreement;
- scheme namespace, collision behavior or cross-scheme interpretation;
- a legitimate multiple-superior exception;
- duplicate/ambiguous Organization, relationship or transition identity resolution;
- unresolved relationship endpoints or supersession targets;
- Module C branching, overlap/gap, independent effectivity, cycle handling or replacement-decision provenance;
- provenance-reference ownership, resolution, trust or authorization semantics;
- Retired/Cancelled Organization or Closed/Revoked relationship coverage across all paths;
- composition/unit identity;
- Organization/Resource mapping; or
- Organization Capability-holder semantics.

Green tests prove the finite current shape. They do not choose any missing authority.

## 9. Authority and Core Boundary ledger

| Responsibility | Current owner / route hypothesis | Forbidden transfer |
|---|---|---|
| fundamental Organization identity | OCP-007 under existing Route F Concept boundary | classification, relationship, name, commander, Resource or checker cannot redefine it |
| Organization transition record/lifecycle | OCP-007 local Route C responsibility invoking P-001 Module B | Pattern or projection cannot supply lifecycle meaning |
| OrganizationRelationshipRecord integrity | OCP-007 local Route C responsibility invoking P-001 A/B/C | endpoint, provenance and supersession meaning cannot be supplied by Pattern or checker defaults |
| classification meaning | Route D by default; Route E only for a proved shared exact envelope | fixture occurrence cannot promote a taxonomy into Core |
| relationship-kind meaning | Route D by default; minimal Route E class-alignment envelope only with a concrete shared need | delimiter syntax cannot become kind authority |
| structural scheme | Route C only for a truly shared opaque partition contract; otherwise D/E by exact owner/consumer | string equality cannot imply cross-domain scheme equivalence |
| multiple-superior exception | fail-closed Core rule or separately governed C/D/E exception contract | reviewer waiver, flag or checker bypass cannot authorize it |
| composition/unit semantics | not selected; D/C/F depends on exact identity responsibility | structural relation or classification cannot imply part-whole identity |
| Organization/Resource mapping | not selected; C for an identified mapping record or F only for a proved identity invariant | mapping cannot collapse identities or inherit Assignment/claims |
| storage/API/UI/graph implementation | Route I | implementation shape cannot own shared meaning |

These are route hypotheses, not admission decisions. Route ambiguity keeps the candidate in Discovery. A new Pattern is not indicated: P-001 already supplies form, and no second reusable form gap has been shown.

## 10. Top-level authority/layout outcomes

### H0 — hold

Retain OCP-007 unchanged at Draft. No stable-surface remediation is prepared. Reopening requires concrete authority or compatibility evidence.

H0 is the fail-safe. Its cost is continued mixing of stable identity/record guarantees with unresolved required inputs and an executable/prose mismatch.

### H1 — one monolithic in-place contract

Keep all Organization identity, lifecycle, relationship, class/type, scheme, exception, composition and mapping decisions as one stable OCP-007 surface.

H1 preserves one artifact owner. Its principal risk is weakest-question coupling: one unresolved axis blocks the whole surface or is hidden by broad prose.

### H2 — one owner, two bounded in-place surfaces

Keep OCP-007 as the single defining artifact but distinguish:

1. a bounded Organization identity/lifecycle kernel; and
2. a separately bounded local `OrganizationRelationshipRecord` contract with its own exact P-001, kind, scheme and exception obligations.

Both surfaces remain owned by OCP-007 and version together until a later explicit extraction act says otherwise. Either may stay outside a future `1.x` promise if its blockers remain visible.

H2 can isolate independent evidence without moving references. Its principal risk is false decomposition: two headings may look separate while sharing hidden continuity/classification/scheme authority.

### H3 — extract the relationship contract

Keep fundamental Organization identity in OCP-007 and move the local relationship-record responsibility to one separate non-Concept defining artifact under Route C or F as proved.

H3 can create a clean authority boundary. Its risks are duplicate prose, changed P-001 invocation ownership, wrapper/reference migration and a relationship artifact that still depends on unresolved Organization continuity.

### H4 — mapping-inclusive joint scope

Stabilize Organization together with an explicit Organization↔Resource mapping/projection contract under legitimate owners of both preserved identities.

H4 directly addresses AB-006/AB-052. Its risks are importing optional mapping into Organization identity, reopening Canonical Resource, adding a record/edge without evidence and coupling all Organization blockers to a second Concept.

## 11. Outcome completeness

The five layouts cover the available authority-home treatments:

- do nothing (H0);
- keep one undivided owner/surface (H1);
- retain one owner but bound two internal semantic surfaces (H2);
- transfer one defining responsibility to another artifact (H3); or
- widen the owner/scope to include the cross-Concept mapping (H4).

Apparent alternatives reduce to these layouts:

- identity-only remediation is H2 with the relationship surface retained as deferred;
- relationship-only repair is H2 unless its authority home moves, then H3;
- a non-normative appendix is H2 if OCP-007 stays the sole owner;
- a new OrganizationRelationship Concept is H3 plus an unproved Route F identity claim;
- a one-way Organization→Resource projection is H4; and
- documenting the blockers without remediation is H0.

Layout does not decide semantic treatment. Every positive layout must still choose or explicitly hold each independent axis below.

## 12. Orthogonal semantic axes

### 12.1 C — material-event continuity

| Option | Treatment | Principal burden |
|---|---|---|
| C0 | retain the current unresolved continuity wording | admissible only with H0; cannot support a stable identity promise |
| C1 | define Core continuity/lineage rules for merger, split, reorganization and redesignation | legitimate event/decision owner, exact lineage identity, branching and provenance |
| C2 | stabilize exact-ID reference continuity while excluding automatic real-world continuity decisions | make material events explicitly unresolved/fail-safe; no implicit same-ID or new-ID inference |

C2 does not say material events are irrelevant. It says OCP-007 cannot derive their identity result without a separately governed continuity decision.

### 12.2 K — Organization classification

| Option | Treatment | Principal burden |
|---|---|---|
| K0 | retain required unresolved `classification_refs` | admissible only with H0; required ownerless references stay blocking |
| K1 | define a closed Core Organization taxonomy | prove Core responsibility, versioning and no domain-authority capture |
| K2 | require exact external owner/version resolution through a minimal envelope | named owners, zero/one/many resolution and ambiguity rejection |
| K3 | make classifications optional opaque non-authoritative annotations outside the stable identity kernel | remove identity/lifecycle dependence on labels and preserve raw values without semantic inference |

K3 is not an open string taxonomy. Values may be carried, but Core derives no identity, hierarchy, role, mapping or authority from them.

### 12.3 T — relationship class and kind

| Option | Treatment | Principal burden |
|---|---|---|
| T0 | retain the current class/type ambiguity | admissible only with H0 |
| T1 | define a closed Core registry of all relationship kinds | prove completeness, legitimate Core ownership and evolution rules |
| T2 | retain coarse OCP-007 classes and exact-bind every versioned external kind to one owner plus one class | exact resolver, class agreement and fail-safe unknown/multiple/mismatch behavior |
| T3 | replace the class/type pair with one OCP-local exact versioned kind vocabulary | record migration and proof that coarse Core kinds are sufficient |

T2 keeps domain meaning outside Core while making the shared alignment envelope exact. T3 is the lower-dependency control if no external kind owner exists.

### 12.4 S — structural scheme

| Option | Treatment | Principal burden |
|---|---|---|
| S0 | retain ownerless `scheme_ref` | admissible only with H0 |
| S1 | treat the value as an opaque dataset-scoped partition key used only by exact equality | define validation scope, collision boundary and no cross-scheme/cross-scope inference |
| S2 | define an exact governed scheme identity/profile | named owner/version/resolution and cross-scheme rules |
| S3 | remove schemes and validate one universal structural graph | migration plus proof that multiple verticals are unnecessary |

S1 deliberately owns less than a scheme registry. If shared scheme identity is required, S2 must be selected separately.

### 12.5 E — multiple-superior exception

| Option | Treatment | Principal burden |
|---|---|---|
| E0 | retain prose exception plus unconditional checker rejection | inadmissible for a positive outcome |
| E1 | remove the exception and fail closed on every multiple-superior case within one partition | replay current data and state a concrete reopening gate |
| E2 | define one versioned exception record/profile and authority | exact scope, owner, evidence, effectivity, conflicts and checker support |

E1 matches the current executable contract and adds no authority. E2 remains valid only if a legitimate exception consumer is demonstrated.

### 12.6 Y — lifecycle scope

| Option | Treatment | Principal burden |
|---|---|---|
| Y0 | retain unreviewed lifecycle semantics | admissible only with H0 |
| Y1 | stabilize the current finite paths as record recognition/existence lifecycle with authoritative history | add missing path/terminal evidence and keep continuity/Readiness separate |
| Y2 | expand or reinterpret the lifecycle | concrete consumer plus new stages/transitions/provenance and migration |
| Y3 | exclude lifecycle from the stable kernel | explain how identity and historical exact references remain useful without it |

Y1 does not make Established mean active, ready, available, authorized or participating.

### 12.7 R — relationship-record integrity and supersession

| Option | Treatment | Principal burden |
|---|---|---|
| R0 | retain the current incomplete endpoint/provenance/Module C contract | admissible only with H0 |
| R1 | complete exact identity/endpoints plus history-only branching supersession | reject duplicate/unresolved/cyclic targets; allow explicit branching and overlap/gaps; each record keeps independent effectivity; successor establishment provenance attributes the replacement without selecting a winner |
| R2 | remove supersession and Module C from the stable relationship surface | preserve existing records as historical opaque metadata or define exact migration; no replacement implication |

R1 adds no current-head projection. Supersession records lineage only: it never redirects an old reference, elects a latest record or makes one branch authoritative by count/order/time.

### 12.8 U — composition and organizational units

| Option | Treatment | Principal burden |
|---|---|---|
| U0 | explicitly exclude composition/unit identity; structural relation and `unit@1` imply neither | named reopening gate under AB-047 |
| U1 | define governed composition/unit semantics | identity, direction, lifecycle, graph, non-inheritance and temporary-group boundaries |

### 12.9 M — Organization/Resource mapping

| Option | Treatment | Principal burden |
|---|---|---|
| M0 | explicitly exclude mapping while preserving `Organization ≠ Resource` | named reopening under AB-006/AB-052 and no hidden projection |
| M1 | define an explicit mapping record/projection | legitimate owners of both identities, exact absence/ambiguity behavior and no Assignment/claim inheritance |

## 13. Common comparison axes

Every layout and combined semantic treatment is compared on:

1. truthful Organization identity and material-event continuity;
2. one defining authority per record, rule, status and result;
3. classification and relationship-kind ownership/version resolution;
4. structural-scheme and exception honesty;
5. lifecycle, temporal and P-001 completeness;
6. composition, unit and Resource-mapping non-implications;
7. current consumer/reference compatibility;
8. executable evidence and fail-safe ambiguity handling;
9. human readability without implementation knowledge;
10. OCP-016 route and future evolution;
11. migration and atomic rollback; and
12. response to unknown, ownerless or conflicting evidence.

## 14. Preliminary layout comparison

| Outcome | Identity/authority | Current compatibility | Readability | Migration/rollback | Preliminary result |
|---|---|---|---|---|---|
| H0 | preserves all current boundaries and blockers | byte-identical | leaves stable and unresolved text mixed | none | admissible fail-safe |
| H1 | one owner but every axis must mature together | no current consumer conflict | weakest-member coupling obscures the contract | potentially one large OCP/checker/fixture unit | admissible, not leading |
| H2 | one owner with explicit identity and relationship boundaries | no reference-home movement; each surface can replay independently | strongest if cross-surface dependencies are listed exactly | bounded in-place remediation; rollback can stay atomic | leading layout hypothesis |
| H3 | one owner per extracted artifact only if transfer is complete | requires exact P-001/reference-home migration | visually clean but wrapper risk | larger; duplicate-authority stop | admissible control, not leading |
| H4 | requires legitimate joint Organization/Resource owners | no current consumer needs mapping; Canonical Resource excludes it | mapping can dominate unrelated questions | largest; may affect data and two Concepts | blocked on current evidence |

The matrix does not select H2. It records why H2 deserves the strongest falsification attack.

## 15. Provisional combined hypothesis — Q2

The current evidence permits one concrete combined hypothesis for comparison:

```text
Q2 := H2 + C2 + K3 + T2 + S1 + E1 + Y1 + R1 + U0 + M0
```

In plain language, Q2 means:

- keep one OCP-007 owner and distinguish identity/lifecycle from the local relationship-record contract;
- stabilize exact ID/reference behavior but make material-event continuity explicitly unresolved rather than inferred;
- remove required classification authority from the identity kernel and treat current values as optional non-authoritative annotations;
- require every normative relationship kind to resolve exactly to one owner and agree with one coarse OCP-007 class;
- use structural scheme values only as opaque dataset-scoped partition keys;
- reject all multiple-superior cases until a separately governed exception exists;
- keep the finite history-based lifecycle as record recognition/existence, not operational state;
- complete exact record/endpoint resolution and use branching supersession as history only, never as redirect or winner selection;
- exclude composition/unit identity and Organization/Resource mapping; and
- preserve every inherited non-implication and exact P-001 module boundary.

Q2 is a discovery hypothesis, not a schema or remediation contract. Its principal risk is **false decomposition**: optional labels, external kinds and opaque partitions may appear to remove authority while actually hiding it in producers or datasets.

## 16. Provisional Q2 identity/lifecycle surface

A later Q2-aligned proposal would have to prove at least:

1. one non-empty exact `organization_id` is unique within the governed resolution scope and remains stable for all historical references to that ID;
2. display name, commander, personnel, location, current relation and optional classification annotation cannot change identity by themselves;
3. Core makes no automatic same/different identity decision for merger, split, reorganization or constitutive redesignation;
4. ambiguous material-event identity fails to unresolved rather than reusing the newest/similar ID or creating an automatic new ID;
5. Draft/Established/Retired/Cancelled paths describe governed record recognition/existence only;
6. transition history remains authoritative and projections remain exact;
7. Established/Retired do not imply operation, activity, availability, Readiness, authorization or Capability;
8. classification annotation absence or conflict cannot erase an exact Organization or choose continuity;
9. no universal parent/children field becomes identity authority; and
10. transition provenance is attributable but grants no actor, continuity, exception or newest-record authority by itself; and
11. any future continuity assertion requires its own exact owner, provenance, branching/conflict and OCP-016/P-001 treatment.

This boundary may be insufficient if consumers need real-world institutional continuity rather than exact record reference. That is an explicit falsification target, not a silent assumption.

## 17. Provisional Q2 relationship surface

A later Q2-aligned proposal would have to prove at least:

1. one unique exact `relationship_id`, directed Organization endpoints resolving exactly once, and preserved history;
2. exact P-001 Modules A/B/C remain complete and owned by one OCP-007 relationship surface;
3. one coarse OCP-007 class controls only shared class-level non-implications and graph behavior;
4. one exact versioned kind resolves to one legitimate owner and declares one compatible class;
5. zero, multiple, unknown or class-mismatched kind resolution rejects the record rather than defaulting to non-structural;
6. a structural partition key is compared by exact decoded equality only within one declared validation dataset/scope;
7. no structural relation or partition key creates Organization identity, composition, Resource mapping or cross-scheme equivalence;
8. every effective structural cycle is rejected over the complete breakpoint sweep;
9. every multiple-superior case in one partition is rejected unconditionally under E1;
10. duplicate record/transition IDs, unresolved/ambiguous endpoints, unresolved supersession targets and supersession cycles reject;
11. replacement uses a new identified record; branching, overlap and gaps are allowed; each branch has independent effectivity and no redirect/current-head/newest-winner authority;
12. successor establishment-transition provenance attributes the replacement decision but does not authorize it by label alone; and
13. structural, operational, administrative, support and coordination semantics remain non-interchangeable.

If no legitimate relationship-kind owner can be named, T2 fails and T3/H0 must lead. Q2 cannot treat an arbitrary `@` string as the missing owner.

## 18. Mandatory human scenarios

Every positive combined outcome must provide a readable deterministic treatment for:

1. one Organization changes display name but keeps the same exact ID;
2. one Organization changes commander and current relationships without identity change;
3. two Organizations merge while no continuity decision owner is available;
4. one Organization splits into two represented entities;
5. a reorganization or constitutive redesignation has conflicting same-ID and new-ID evidence;
6. an Established Organization has no classification annotation under K3;
7. two Organizations carry the same `organization-type://unit@1` value;
8. one classification reference has zero, two or incomparable external owners under K2;
9. a relationship kind resolves but declares a class different from the record's class;
10. a version-looking relationship kind has no resolver or owner;
11. two opposite structural edges exist in different partition keys;
12. a transient structural cycle exists only between two breakpoints;
13. one Organization has two direct structural superiors in one partition with no exception;
14. a producer supplies an “exception” label but no governed E2 record/profile;
15. the same source/target pair has simultaneous structural and operational records;
16. two Organizations or two relationship records reuse one ID;
17. a relationship endpoint or supersession target resolves to zero or multiple records;
18. two successors supersede one relationship while their effective intervals overlap;
19. a provenance label is proposed as actor authorization or continuity authority;
20. an Organization is Retired while historical exact references still resolve;
21. a `unit@1` classification appears without composition or Resource mapping;
22. an Organization and a Resource represent related real-world subjects without an authorized mapping;
23. an Organization is named as a Capability holder under the current OCP-012 contract;
24. equal Organization labels or relations are proposed as Resource interchangeability evidence; and
25. an Organization name/caller identity is proposed as Coordination or workflow authority.

All scenarios remain synthetic and non-sensitive.

## 19. Mandatory counterexamples

External review and the later Board act must reject these conclusions:

1. OCP-007 is the last T4 candidate, therefore it must be stabilized next.
2. Resource is Canonical, therefore Organization must map to it.
3. The same name or commander proves the same Organization after a material event.
4. The newest Organization record or most common ID wins a continuity conflict.
5. A stable `organization_id` already defines merger/split continuity.
6. An Established Organization requires a label, therefore Core owns that label's meaning.
7. A reference contains `@`, therefore it resolves to a legitimate classification or relationship-kind owner.
8. A checker-accepted type string has governed directionality or graph semantics.
9. A class label and kind label look similar, therefore they agree.
10. Equal classifications make Organizations identical, equivalent or interchangeable.
11. Equal `scheme_ref` strings from unrelated datasets prove the same governed scheme.
12. Different scheme keys permit a cross-scheme structural inference.
13. An “exception” flag, reviewer comment or source count authorizes multiple superiors.
14. Green cycle tests prove scheme identity or exception legitimacy.
15. Structural subordination implies composition, operational control, command or Resource ownership.
16. Organization membership creates Assignment, participation or a Capability claim.
17. `unit@1` makes an Organization a Resource or organizational unit by itself.
18. Equal Organization Capability assertions make Resources interchangeable.
19. Extracting prose automatically creates a legitimate owner or new Concept.
20. Keeping one file makes every section part of one compatibility surface.
21. P-001 supplies relationship-kind, scheme, continuity or exception meaning.
22. Non-empty endpoint strings prove that the referenced Organizations exist uniquely.
23. `supersedes_relationship_ref` selects a current head or redirects historical references.
24. The newest successor, most-supported branch or latest provenance wins a supersession conflict.
25. A provenance reference authorizes establishment, continuity or exception by itself.
26. Established means active, available, ready, authorized or participating.
27. AD-019 approval selects Q2 or authorizes an OCP-007 edit.
28. Fable approval, CI or owner authorization for this discovery transfers to AD-019A or remediation.

## 20. Unconditional evidence obligations

The following apply to H0/H1/H2/H3/H4 and every semantic-axis combination:

1. exact-anchor the baseline and every changed comparison input;
2. preserve Organization/Resource identity separation and all inherited non-implications;
3. account for every OCP-007 section and field without silently deleting accepted text;
4. reproduce the normative-consumer, Concept-edge, AD-provenance and negative-prose sweeps;
5. name one defining owner for every normative rule, record, projection and status—or retain hold;
6. preserve exact P-001 invocation and explain every invocation transfer under extraction;
7. keep real-world continuity, record-reference continuity and lifecycle distinct;
8. reject unknown, ownerless, ambiguous, conflicting or incomparable authority inputs;
9. provide human-readable scenarios, counterexamples, migration and rollback;
10. preserve exact historical references without newest-record redirect;
11. keep machine evidence structural and subordinate to cited human-readable rules; and
12. require a separate Board selection before any semantic implementation.

No unconditional fixture may require extraction, mapping, a Core taxonomy, an external type registry, a scheme registry, an exception record, composition or a continuity record. At least one admissible outcome rejects each mechanism.

## 21. Layout-conditional evidence and equivalents

| Layout | Conditional evidence | Equivalent for shared guarantees |
|---|---|---|
| H0 | byte-exact snapshot replay plus concrete reopening trigger; no invented migration | unchanged reference and checker behavior is the replay witness |
| H1 | one complete surface ledger proving every axis is mature and no unresolved field hides inside `1.x` | one authoritative contract replaces surface-boundary evidence |
| H2 | section/field relocation ledger, explicit cross-surface dependencies, one owner and no normative residue | one exact owner plus two readable bounded surfaces replaces extraction migration |
| H3 | one defining owner after transfer, exact wrapper/references, P-001 invocation movement, no duplicate prose and atomic rollback | exact single-owner resolution replaces in-place boundary evidence |
| H4 | two preserved identities, legitimate joint owners, exact mapping record/projection, absent/ambiguous mapping behavior and no inheritance | mapping determinism replaces mapping-exclusion evidence |

Evidence is outcome-fair only when hold does not fabricate a new layer and positive layouts cover the shared identity/authority guarantees through mechanisms they actually select.

## 22. Axis-conditional evidence and equivalents

| Axis choice | Required evidence | Outcome-fair equivalent |
|---|---|---|
| C1 | material-event kinds, owner, lineage identity, provenance, branching/conflict and replay | C2 proves explicit non-derivation plus ambiguity detection; C0 holds |
| K1/K2 | exact vocabulary/envelope owner, version resolution and ambiguity rejection | K3 proves no semantic derivation and optional-value replay |
| T1/T2/T3 | one exact versioned kind owner, class behavior and mismatch rejection | T0 holds without pretending syntax is authority |
| S1 | dataset/scope boundary, exact key equality and cross-scope non-inference | S2 proves exact governed identity; S3 proves complete single-graph migration |
| E1 | unconditional multiple-superior rejection and reopening gate | E2 proves exact exception authorization/effectivity/conflict handling |
| Y1/Y2 | complete paths, history/projections, terminal/historical reference behavior and non-Readiness | Y3 proves identity/reference usefulness without lifecycle; Y0 holds |
| R1 | duplicate/endpoint/target ambiguity rejection, explicit branching/overlap/gap/effectivity/provenance and no redirect/current head | R2 proves safe Module C removal/migration; R0 holds |
| U0 | explicit no-composition/unit inference and reopening gate | U1 proves identity, graph, lifecycle and non-inheritance |
| M0 | explicit no-mapping/projection/inheritance plus AB-006/AB-052 gate | M1 proves two-identity exact mapping and fail-safe absence/ambiguity |

Machine evidence is required for every mechanically expressible selected obligation. Authority and real-world continuity claims that cannot be encoded must be labeled human-review-only; they cannot be marked executable by proxy.

## 23. Migration and rollback questions

This discovery creates no data, reference or semantic migration. A later Board selection must account for:

- preservation of every current `organization_id`, `relationship_id` and historical exact reference;
- treatment of current required `classification_refs` if K3 makes them optional or K2 makes them exact-resolved;
- class/type migration when current type strings have no named owner;
- whether `scheme_ref` is retained, renamed to an opaque partition key or migrated to a governed scheme identity;
- removal of the prose exception under E1 or introduction of an exact E2 record/profile;
- missing lifecycle-path fixtures without inventing historical transitions;
- duplicate identity, exact endpoint and Module C fixtures plus treatment of current supersession values under R1/R2;
- P-001 invocation and semantic-owner movement under H3;
- checker/rules/fixture updates required by every changed invariant;
- no OCP-003 or OCP-012 edit under M0; and
- atomic rollback without deleting records, merging identities, redirecting references, reinterpreting labels or selecting a newest winner.

Q2 is expected to require OCP-007, Organization checker/rules and bounded fixture changes in a later remediation. Zero direct consumers makes reference migration unlikely, but that is a hypothesis. Any actual external/current record migration must be stated rather than inferred away.

## 24. Falsification targets

External review and the later AD-019A selection must try to demonstrate any of the following:

1. a direct normative OCP-007 consumer or Organization Concept edge was missed;
2. a current consumer needs real-world merger/split/reorganization continuity rather than exact-ID resolution;
3. C2 cannot make `organization_id` truthful without a new continuity authority inside the stable kernel;
4. current valid Organization data requires classification meaning, not merely a carried value;
5. making classification optional under K3 weakens a current identity or lifecycle guarantee incompatibly;
6. a legitimate K2 classification envelope and concrete shared consumer already exist;
7. T2 cannot satisfy P-001 kind obligations without creating a registry or duplicate owner;
8. a current relationship consumer requires type-specific semantics not expressible by coarse classes plus an exact envelope;
9. T3 is strictly smaller and safer than T2 while preserving exact current records;
10. S1's dataset-scoped partition key cannot avoid collision or hidden cross-scope equivalence;
11. a current consumer requires governed scheme identity or cross-scheme interpretation;
12. a legitimate multiple-superior exception consumer/owner already exists;
13. unconditional E1 rejection invalidates a current valid structural case;
14. Y1's current lifecycle paths are semantically incomplete for exact current consumers;
15. exact duplicate/endpoint resolution or Module C completion cannot remain local to the relationship surface;
16. R1 branching/overlap/gap semantics create an unowned current-head or conflict-resolution rule;
17. successor establishment provenance is insufficient even as non-authorizing replacement attribution;
18. composition/unit identity is required to state Organization identity or structural relations truthfully;
19. Canonical Resource requires M1 mapping for Organization's own stable surface;
20. H2 cannot remain one readable owner without duplicate or hidden cross-surface authority;
21. H3 is necessary because no in-place boundary can preserve exact P-001 and human readability;
22. Route C is wrong for the candidate repair or Route F extraction has independent identity evidence now;
23. Q2 requires an unbounded registry, new Concept, graph edge, Organization Capability holder or joint Resource edit;
24. a legitimate sixth layout or additional independent semantic axis exists outside the current matrix;
25. an evidence obligation assumes a layer rejected by another outcome;
26. current checker/fixtures claim stronger authority than §8 reports; or
27. AD-019 required an OCP/checker/fixture edit merely to complete discovery evidence.

If 1–3 succeeds, Q2 continuity treatment loses its lead. If 4–6 succeeds, K2/K1 or hold must replace K3. If 7–9 succeeds, T2 must be revised or replaced. If 10–13 succeeds, S1/E1 loses its lead. If 14–17 succeeds, Y/R treatment must change. If 18–19 succeeds, U/M treatment must change. If 20–23 succeeds, H2/Q2 stops. If 24 succeeds, the matrix must be revised before selection. If 25 or 27 succeeds, outcome fairness fails and the discovery stops.

Unknown or conflicting evidence always returns to H0/C0/K0/T0/S0/E0/Y0/R0. It never becomes permissive continuity, classification, kind, scheme, exception, supersession, composition or mapping authority.

## 25. Preliminary recommendation

The strongest current hypothesis is **Q2 — H2 with exact-ID continuity, optional opaque classification, exact class/type envelope, opaque local structural partitions, fail-closed superior cardinality, bounded lifecycle, history-only branching supersession, and explicit composition/mapping exclusions**. H0 remains the fail-safe.

Q2 leads because:

- one existing OCP-007 owner can keep fundamental identity and the local relationship record readable without reference-home migration;
- exact-ID history can remain stable while material-event continuity stays explicitly unresolved rather than guessed;
- no current consumer requires classification semantics, composition, mapping or Organization Capability holders;
- the current relationship record genuinely needs exact versioned kind authority under P-001, while class alignment can be a narrow fail-safe envelope instead of a Core taxonomy;
- an opaque local partition explains exactly what the checker does without claiming cross-scheme identity;
- unconditional multiple-superior rejection matches every current executable witness and adds no exception authority;
- the finite history-based lifecycle is independently understandable and keeps Readiness/availability separate; and
- complete endpoint resolution plus history-only branching supersession can satisfy P-001 without introducing a current-head authority; and
- failure of any axis can return to H0 or a separately selected alternative without silently widening the scope.

The principal Q2 risk is **hidden producer authority**. Optional classifications, externally owned kinds and dataset-scoped partitions may appear neutral while producers still choose identity, type or grouping without a legitimate reviewed contract. A later Q2 selection/remediation must name every allowed input boundary, reject ambiguity and keep human text primary.

H1 does not lead because four independent blockers would be coupled into one weakest-member surface. H3 does not lead because no consumer or one-owner defect justifies extraction/P-001 migration. H4 does not lead because mapping is optional to Canonical Resource and absent from current Organization consumers. K1/T1/S2/E2/U1/M1 do not lead because no current evidence justifies their additional authorities.

This is a recommendation only. AD-019 does not select Q2, authorize AD-019A, edit OCP-007 or authorize lifecycle.

## 26. Exit criteria and mandatory next Board act

AD-019 is ready for Board selection only when external review confirms:

1. every §2 anchor and the complete consumer/evidence sweep;
2. complete §6 section and §7 field ledgers;
3. H0–H4 completeness and no hidden authority-home alternative;
4. C/K/T/S/E/Y/R/U/M independence and no missing semantic axis;
5. every §24 attack attempted with written results;
6. unconditional and conditional evidence obligations are outcome-fair;
7. exact P-001, OCP-016 and one-owner treatment;
8. inherited Resource, Capability, Assignment, Readiness and interchangeability boundaries;
9. bounded migration/rollback and fail-safe unknown handling; and
10. readability without checker code or PR history.

A separate **AD-019A — Select Organization Stable-Surface Outcome** Board act must then:

1. exact-anchor the then-current baseline;
2. accept, revise or reject every §6/§7 classification;
3. re-attempt all §24 falsification targets;
4. select H0–H4 plus one explicit treatment for every C/K/T/S/E/Y/R/U/M axis, or prove a complete alternative;
5. state the exact next artifact and allowed edit boundary;
6. define checker/fixture, migration, rollback, route, stop and non-transfer rules; and
7. authorize preparation only—not remediation merge, Concept/backlog status change, mapping, lifecycle transition or T5 reopening.

The next proposal is limited to appending that AD-019A selection to:

```text
architecture/discovery/AD-019-organization-stable-surface.md
```

and updating only its current projections in `README.md`, the AB-062 note in `backlog/architecture-backlog.md` and `backlog/roadmap.md`. It may set AD-019 to `0.2.0 / Accepted` only through its own reviewed and authorized merge. It may not edit OCP-007, checker, rules, fixtures, registry, taxonomy, map, P-001 or any Organization backlog status.

If Q2 is later selected, the next proposal may be one bounded OCP-007/checker/rules/fixtures remediation only. After that remediation completes or fails, a fresh blocker/stability audit and another Board act remain mandatory before any OCP-007 `1.0.0` lifecycle proposal.

## 27. Discovery status and accounting

When exact-head reviewed, explicitly authorized and squash-merged, AD-019 will:

- establish `AD-019 0.1.0 / Discovery`;
- record the exact Organization, consumer, P-001 and executable baseline;
- preserve H0 as fail-safe and record Q2 only as the leading hypothesis;
- keep H1/H3/H4 and every semantic-axis alternative admissible under their evidence conditions;
- require a separate AD-019A Board selection before any OCP-007/checker/rules/fixture remediation;
- retain OCP-007 at `0.3.2 / Draft`, Organization at `Accepted`, AB-006/044–047/051/052 `Open`, AB-062 `Planned` and readiness at approximately 70%; and
- change no OCP, Concept, Pattern, dependency, projection, registry row, graph edge, schema, checker rule, fixture or production authority.

Fable approval, Codex adjudication, green CI and explicit Pavlo/Architecture Board authorization apply only to this discovery record. They cannot select Q2, merge AD-019A, edit OCP-007, change checker/rules/fixtures, resolve Organization backlog, introduce mapping or Organization Capability holders, promote Organization, reopen T5 or authorize downstream work.

## 28. AD-019A Board question and exact baseline

AD-019A decides whether the externally reviewed discovery justifies one Organization stable-surface remediation direction. It does not perform that remediation, change an OCP or Concept status, resolve an Organization backlog item, create a mapping or authorize T5.

The exact decision baseline is `main@f6b492f3086359778618e3dbe6ea3d465a2f512b`, tree `962095efd9d8db67b3e17064e5d6672671294ae4`. On that baseline:

- AD-019 is `0.1.0 / Discovery`, blob `bff6194feaef6dc2ec90b65d41630545f6c479a2`, SHA-256 `8f6b8df7d1661182a6f0f15d42af8144cc832f62303c0b7b52127bc16354dd3c`;
- the architecture backlog is blob `71aab5bc0ff57d82b52778037a8c7a1fcd4c299a`, SHA-256 `0723888d65341fdc2ef3a443d38fd7360c2931612f64ebd8609d9dc9fc7a90a3`;
- the current README projection is blob `ead0d17b80235a93279b4981d3518d966567daec`, SHA-256 `e7dae8d6db3043a55692b46850d0e7867a8af24f3c05f04b7618a10383c3fd3a`;
- the current roadmap projection is blob `70e6fe01d4a136f942090bc3928d2d05708e2c49`, SHA-256 `5fe3e47a1d3db85e0b17e7196a52f2960c284b3aa1cfac157173ef522c748fc9`;
- the other nineteen semantic and executable anchors in §2 remain byte-identical; the exact baseline-to-baseline diff contains only AD-019 and its three accounting projections;
- OCP-007 remains `0.3.2 / Draft`, Organization remains `Accepted`, P-001 remains `0.1.0 / Accepted`, and the six Organization fixtures plus 119-fixture manifest remain unchanged;
- the post-merge consumer sweep finds zero direct normative OCP-007 consumers, zero Organization Concept edges and five AD provenance dependencies: AD-005, AD-011, AD-014, AD-018 and AD-019; and
- no OCP-007, checker, rules, fixture, remediation or lifecycle act is authorized.

Fable independently reproduced all twenty discovery anchors, both ledgers, the executable absence claims, H0–H4 completeness, the nine-axis space, all 25 scenarios, all 28 counterexamples and the outcome-fair evidence structure. Iteration 2 approved exact head `39361d7209b51803bd4b17423a8efad483c0034c` with zero findings after the §8.1 baseline/proposed-tree count was made explicit. The authorized discovery merged byte-identically as `f6b492f3086359778618e3dbe6ea3d465a2f512b`, and `main` CI succeeded.

The Board question is narrow: **does current evidence justify Q2 as the direction for one bounded OCP-007 remediation proposal, or must one or more layout/axis choices return to hold or another treatment?** File age, T4 order, authoring effort, review agreement, readiness percentage, hashes and green CI are not selection evidence.

## 29. Board treatment of the discovery

AD-019A accepts the discovery with these limits:

1. **The stable material is real but not monolithic.** Exact Organization identity/history and the local relationship-record form are independently readable candidates; continuity, classification, kind, scheme/exception and Module C gaps cannot enter a stable promise merely because they share OCP-007.
2. **The consumer surface is empty, not irrelevant.** Zero direct OCP consumers and zero Concept edges reduce migration pressure but do not create semantic authority.
3. **The R axis is an independent discovered blocker.** Exact endpoint/target resolution and P-001 Module C branching, overlap/gap, effectivity and replacement attribution are not supplied by the current record or Pattern.
4. **The current checker is an honest but partial witness.** It proves the finite lifecycle/projection and structural graph rules listed in §8.2 while proving none of the absence claims in §8.3.
5. **The five layouts and nine axes are complete for this decision.** External attempts to construct a sixth authority home or tenth independent axis reduced to an existing treatment.
6. **Q2 is not inherited from discovery approval.** It remains selectable only because its individual choices survive the commissioned attacks below.
7. **Every selected input boundary remains fail-safe.** An arbitrary producer string, `@` delimiter, label, source count, timestamp, record order or reviewer statement cannot stand in for exact resolution or legitimate ownership.
8. **Selection remains preparation-only.** A future remediation must prove its exact owner, resolver, migration and executable shape on its own reviewed head.

These results justify one remediation direction only while every non-waivable stop in §§35–40 remains enforceable.

## 30. Board disposition of the discovery ledgers

### 30.1 OCP-007 section disposition

| Section | AD-019A disposition |
|---|---|
| §1 Purpose | accept K with H2: one OCP-007 owner, two explicitly bounded surfaces |
| §2 Definition | accept the independent Organization definition; revise continuity to C2 exact-ID/non-derivation |
| §3 Boundary | accept identity and non-implications; replace required classification authority with K3; retain mapping/holder/authority exclusions |
| §4 Identity | accept name/commander/location/relation independence; remove any implication that the ID decides merger, split, reorganization or redesignation |
| §5 Organization structure | accept identity, display, history and projections; make `classification_refs` optional K3 annotations rather than lifecycle prerequisites |
| §6 Organization lifecycle | accept Y1 as record recognition/existence only; require complete path evidence and no operational reading |
| §7 OrganizationTransitionRecord | accept the local P-001 Module B form; keep material-event continuity outside the record |
| §8 Relationship decision | accept the local non-Concept relationship responsibility under the same OCP-007 owner |
| §9 Relationship structure | accept the identified record only after T2/S1/R1 exactness is supplied; current delimiter/presence checks are insufficient |
| §10 Initial classes | accept the five coarse non-equivalent class behaviors; reject a closed Core taxonomy and require T2 exact kind-to-class agreement |
| §11 Relationship lifecycle | accept Y1 record recognition/existence paths; require terminal-path evidence and no real-world authority inference |
| §12 Derivations | accept history-derived effectivity and complete breakpoint sweep; define S1 validation scope and R1 branch behavior explicitly |
| §13 Business rules | accept the identity/class/non-implication rules after kind resolution and Module C completion; no current-head projection is added |
| §14 Semantic rules | accept class non-implications and fail-safe unknown behavior; remove rule 9's ownerless exception under E1 |
| §15 Organization invariants | accept after classification requiredness is removed and dataset identity ambiguity rejects |
| §16 Relationship invariants | accept after duplicate/endpoints/kind/partition/E1/supersession obligations become exact and executable |
| §17 P-001 conformance | accept exact existing invocation; OCP-007 must fill every selected semantic slot and Pattern supplies none |
| §18 Examples | retain as human evidence only; examples cannot admit owners, kinds, schemes or exceptions |
| §19 Explicit exclusions | accept C2/K3/U0/M0 and inherited exclusions; remove stale Coordination cleanup and any contradictory continuity overclaim |
| §20 Open questions | retain all Organization backlog visibility; AD-019A resolves none of those items |
| §21 Review target | retain as falsification evidence; it carries no semantic authority |

Every prior B item is either assigned a selected treatment with a named stop condition or remains an explicit exclusion. No B item is silently relabelled K.

### 30.2 Organization-field disposition

| Field | Selected treatment |
|---|---|
| `organization_id` | exact non-empty identity, unique within the governed dataset/resolution scope; duplicate or ambiguous identity rejects |
| `classification_refs` | retained for compatibility as optional opaque K3 annotations; the field name does not make a value resolvable or authoritative |
| `display_name` | optional human designation with no identity, continuity, hierarchy or authority effect |
| `transition_history` | authoritative Y1 record lifecycle history under exact P-001 Module B |
| `created_at` | attributable creation time only; never priority or continuity authority |
| `lifecycle_stage` / `established_at` / `retired_at` | optional projections exactly equal to history |
| `establishment_provenance_ref` | optional exact history projection; attribution only, not actor/continuity/authorization authority |

### 30.3 Relationship-field disposition

| Field | Selected treatment |
|---|---|
| `relationship_id` | exact unique record identity within the governed dataset; duplicate ambiguity rejects |
| `relationship_class` | one closed coarse OCP-007 behavior family; not a full kind taxonomy |
| `relationship_type_ref` | exact T2 reference resolved once through a separately owned versioned kind profile and required to agree with `relationship_class`; syntax alone never admits it |
| `source_organization_ref` / `target_organization_ref` | directed endpoints that each resolve exactly once to an Organization in the declared resolution scope |
| `scheme_ref` | S1 opaque partition key compared by exact decoded equality only inside one declared validation dataset/scope |
| `validity_start` / `validity_end` | P-001 Module A half-open effectivity, independent for every relationship record/branch |
| `transition_history` | authoritative Y1 record lifecycle history under Module B |
| `created_at` | creation time only; never branch, head or authority priority |
| lifecycle/time/provenance projections | optional values exactly equal to authoritative history |
| `supersedes_relationship_ref` | R1 exact history link with explicit branching/overlap/gap and no redirect, winner or current-head meaning |

### 30.4 Transition-field disposition

| Field | Selected treatment |
|---|---|
| `transition_id` | exact identity unique in its governed transition dataset; duplicate ambiguity rejects |
| `organization_ref` / `relationship_ref` | exact same-subject reference and no implicit external rebinding |
| `from_stage` / `to_stage` | one allowed Y1 record-recognition path step |
| `occurred_at` | non-decreasing occurrence time; never newest-winner authority |
| `provenance_ref` | required attributable provenance; it cannot authorize continuity, exception, establishment or branch selection by itself |

## 31. Commissioned falsification closure

AD-019A re-attempts all twenty-seven AD-019 §24 attacks:

| # | Evidence rechecked | Board result |
|---:|---|---|
| 1 | exact consumer/dependency sweep on the merged baseline | zero OCP consumers, zero Concept edges and exactly five AD provenance records; missed consumer/edge not demonstrated |
| 2 | current OCP prose, fixtures and repository references | no consumer requiring real-world material-event continuity demonstrated |
| 3 | scenarios 3–5 and C2 failure behavior | exact-ID history remains truthful while material-event identity returns unresolved; contradiction not demonstrated |
| 4 | current Organization fields, fixtures and consumers | no identity/lifecycle guarantee requiring classification meaning demonstrated |
| 5 | Established/Retired shape under optional annotation replay | no incompatible weakening demonstrated; absence cannot erase identity/history |
| 6 | repository-wide owner/profile search | no ready K2 envelope or concrete shared classification consumer demonstrated |
| 7 | P-001 kind obligations versus current delimiter check | T2 remains possible only through an exact external kind-profile envelope; inability to define that envelope is a remediation stop, not permission to keep current strings |
| 8 | current relationship consumer sweep | no type-specific consumer beyond the coarse shared class behaviors demonstrated |
| 9 | T3 control and migration burden | no proof that collapsing the pair into an OCP-local vocabulary is strictly smaller or safer than an exact T2 envelope |
| 10 | S1 exact dataset/scope equality | collision or hidden cross-scope equivalence is avoided by scope-local comparison; failure not demonstrated |
| 11 | consumer and fixture sweep | no need for governed cross-scheme identity or interpretation demonstrated |
| 12 | OCP/checker/prose sweep | no legitimate multiple-superior exception owner or consumer demonstrated |
| 13 | current graph regressions | E1 matches all executable evidence; invalidation of a current valid case not demonstrated |
| 14 | Organization and relationship lifecycle paths | no current consumer requiring a broader semantic lifecycle demonstrated; missing path evidence is carried into remediation |
| 15 | one-owner H2/P-001 boundary | duplicate/endpoint/Module C completion can remain local to the relationship surface; contrary evidence not demonstrated |
| 16 | branching, overlap/gap and effectivity scenarios | R1 adds no head, redirect or conflict winner; unowned selection rule not demonstrated |
| 17 | successor establishment provenance | sufficient for non-authorizing replacement attribution; stronger authority is neither claimed nor demonstrated as required |
| 18 | identity, structural and `unit@1` scenarios | composition/unit identity is not required for truthful current Organization or relationship semantics |
| 19 | Canonical OCP-003 and zero mapping consumers | Resource does not require M1 for Organization's stable surface |
| 20 | complete section/field relocation ledger | one OCP-007 owner with two explicit surfaces remains readable; duplicate hidden owner not demonstrated |
| 21 | extraction/P-001/reference-home analysis | no evidence makes H3 necessary; in-place boundary remains sufficient |
| 22 | OCP-016 route audit | Route C remains correct for local records; no independent Route F identity for extraction exists |
| 23 | bounded Q2 contract | no unbounded registry, new Concept, graph edge, Organization holder or joint Resource edit is required; appearance of one stops remediation |
| 24 | external construction attempts | no sixth layout or tenth independent semantic axis demonstrated |
| 25 | unconditional/layout/axis evidence tables | no obligation assumes a layer rejected by another outcome |
| 26 | exact current checker/rules/fixtures | implementation claims no stronger authority than §8 reports |
| 27 | discovery diff and merge tree | discovery completed without OCP/checker/rule/fixture edits |

“Not demonstrated” remains narrower than “impossible.” Attacks 7, 15, 20 and 23 become non-waivable authoring/review stops. If any succeeds, Q2 loses authority and H0 is the immediate fallback; the proposal cannot silently substitute T3, extraction, a registry, mapping or a new Concept.

## 32. Architecture Board selection — Q2

AD-019A selects the complete Q2 direction without changing its axes:

```text
Q2 := H2 + C2 + K3 + T2 + S1 + E1 + Y1 + R1 + U0 + M0
```

In human terms, the selected direction is:

- one OCP-007 owner with a clearly bounded Organization identity/lifecycle surface and local relationship-record surface;
- exact-ID reference continuity without automatic real-world continuity decisions;
- optional opaque classification annotations outside identity and lifecycle;
- an exact externally owned relationship-kind profile that agrees with one coarse OCP-007 class;
- dataset-scoped opaque structural partitions;
- unconditional rejection of multiple direct structural superiors in one partition;
- finite history-based record recognition/existence lifecycle;
- exact endpoint/target resolution plus history-only branching supersession;
- explicit exclusion of composition/unit identity and Organization/Resource mapping; and
- every inherited Resource, Capability, Assignment, Readiness, authority and interchangeability boundary unchanged.

Q2 is selected because each component has an independent evidence basis and an explicit failure path. It is not selected because it was the preliminary recommendation, because Fable approved discovery, because OCP-007 is the remaining T4 candidate, because the diff can be small or because green tests prefer it.

H0 remains the immediate fail-safe. Q2 authorizes preparation of one remediation draft only. It neither makes the selected semantics effective nor authorizes merge of that draft.

## 33. Selected Organization identity/lifecycle contract

The future remediation must make the Organization surface readable without reference to checker code or this decision history. It must establish all of the following together:

1. `organization_id` identifies one represented Organization exactly within a declared dataset/resolution scope and rejects duplicate or ambiguous identities.
2. Existing exact historical references remain bound to that ID; they are never redirected to a newer, similar or more-supported record.
3. Display name, commander, personnel, location, current relationships and classification annotations cannot create, merge, split or replace Organization identity.
4. Merger, split, reorganization and constitutive redesignation are material-event continuity questions for which Core makes no automatic same-ID/new-ID decision.
5. Missing, conflicting or ownerless material-event evidence returns an unresolved continuity result; same name, shared personnel, newest record or source count supplies no default.
6. `classification_refs` remains serially compatible but becomes optional opaque K3 annotation. Core does not resolve its values or derive identity, lifecycle, hierarchy, role, mapping, Capability, Readiness or authority from them.
7. Draft/Established/Retired/Cancelled describe record recognition/existence only. Established never means active, participating, available, ready, admissible or authorized.
8. Exact P-001 Module B OrganizationTransitionRecord history is authoritative; optional lifecycle/time/provenance projections must equal it.
9. Every allowed path, terminal state, duplicate transition ID and projection mismatch has executable evidence.
10. Transition and establishment provenance is attributable but grants no actor authority, continuity decision or precedence by itself.
11. Historical exact references remain valid after Retired; Cancelled means the record was not established, not that a different Organization identity wins.
12. Universal parent/children fields, composition, unit identity, Resource mapping and Organization Capability holders remain explicitly excluded.

The surface must state C2 positively: exact reference stability is a useful Core guarantee even when real-world institutional continuity is unresolved. It must not imply that unresolved continuity is unimportant.

## 34. Selected OrganizationRelationshipRecord contract

The future remediation must establish all of the following together:

1. `relationship_id` and every relationship transition ID are unique within the declared validation dataset; duplicates reject without order dependence.
2. Each directed source/target reference resolves exactly once to an Organization in the declared resolution scope. Zero or multiple matches reject.
3. The five `relationship_class` values remain coarse, mutually non-equivalent OCP-007 behavior families. They do not become a complete relationship taxonomy.
4. Each normative `relationship_type_ref` resolves exactly once to one versioned kind profile supplied by a legitimate external/domain owner context. The profile declares exactly one compatible coarse class.
5. Missing, duplicate, unknown, incomparable or class-mismatched kind-profile resolution rejects. A delimiter, fixture value or producer-declared label does not create ownership.
6. OCP-007 owns only the T2 interoperability envelope and coarse class-level shared behavior; the exact profile owner owns the kind's specialized meaning. If that one-owner split cannot be stated without a registry or duplicate authority, remediation stops.
7. A structural `scheme_ref` is an S1 opaque partition key. It is compared by exact decoded equality only inside one declared validation dataset/scope and creates no cross-scope or cross-scheme equivalence.
8. Directed endpoints, half-open validity, authoritative lifecycle history and exact projections remain under P-001 Modules A and B.
9. The complete structural breakpoint sweep rejects every effective cycle. Every multiple-direct-superior case in one exact partition rejects under E1; there is no exception field, waiver or bypass.
10. `supersedes_relationship_ref` resolves exactly once, never targets self, remains acyclic and records history only.
11. One predecessor may have explicit successor branches. Overlap and gaps are allowed; every branch retains independent effectivity and lifecycle.
12. Supersession never redirects an old reference, elects a current head or selects a winner by time, storage order, provenance, issuer/reviewer count, majority or branch count.
13. Successor establishment-transition provenance attributes the replacement decision but does not authorize it or resolve branch conflicts by itself.
14. Structural, operational, administrative, support and coordination records remain distinct; no class implies another, composition, command, ownership, Assignment or mapping.
15. Unknown class/kind/scope/effectivity evidence fails safe. No record defaults to non-structural merely to avoid a graph rule.

The exact external kind-profile envelope is the principal Q2 risk. The remediation must show a finite synthetic resolver context and a human-readable ownership boundary. It may not create a Core kind registry merely because the checker needs test data.

## 35. Selected Core Boundary and Pattern result

| Responsibility | Selected route | Owner/result |
|---|---|---|
| fundamental Organization identity | F — existing Concept boundary | OCP-007 remains the single defining artifact; C2 limits material-event claims |
| Organization record lifecycle | C — local identified record | OCP-007 owns semantics and invokes exact P-001 Module B |
| OrganizationRelationshipRecord | C — local identified record | OCP-007 owns record/class/shared graph semantics and invokes exact P-001 A/B/C |
| specialized relationship-kind meaning | D by default; E envelope only for exact shared interoperability | named external/domain profile owner; OCP-007 owns only exact resolution/class agreement |
| structural partition | C — local validation context | OCP-007 owns S1 scope-local equality only, not scheme identity |
| multiple-superior treatment | C — shared fail-closed invariant | E1 unconditional rejection; no exception authority selected |
| classification annotation | D/I carried value | no Core semantic owner or identity/lifecycle effect under K3 |
| material-event continuity decision | not selected | exact C2 non-derivation; future owner requires a separate act |
| composition/unit semantics | not selected | U0 exclusion under AB-047 |
| Organization/Resource mapping | not selected | M0 exclusion under AB-006/AB-052 |

No new Concept, graph edge, Pattern, mapping record, Organization Capability-holder extension, Core taxonomy, kind registry, scheme registry or exception profile is selected. OCP-007 retains `Concept-Depends-On: []`. P-001 stays `0.1.0 / Accepted`; its form does not supply Organization, kind, partition, continuity or exception meaning.

## 36. Mandatory OCP-007 remediation contract

The separately reviewed remediation proposal must:

1. exact-anchor AD-019, OCP-007, P-001, OCP-016, Canonical OCP-003, OCP-009/OCP-012/OCP-013/OCP-014/OCP-015, the zero-consumer/zero-edge/five-AD sweeps, Organization checker/rules/tests, both Organization fixture trees and the complete fixture manifest;
2. change OCP-007 `0.3.2 → 0.4.0` while retaining document `Draft`, Organization `Accepted`, current `Depends-On` and `Concept-Depends-On: []`;
3. reorganize OCP-007 into one explicit Organization identity/lifecycle surface, one explicit local relationship-record surface, shared inherited boundaries and a visible deferred/excluded surface—without creating a second defining artifact;
4. provide a line-by-line relocation ledger from every §30.1 section and every §30.2–§30.4 field to selected rule, selected exclusion, cleanup, example or historical record;
5. implement all twelve §33 guarantees in human-readable prose before describing executable evidence;
6. retain current `classification_refs` values as compatible optional opaque annotations, remove their Established/Retired requiredness and forbid semantic inference from presence, absence, equality or disagreement;
7. implement the exact T2 kind-profile resolver envelope in §34.4–§34.6 without adding a Core registry or treating fixture profiles as normative owners; if no legitimate external/domain owner boundary can be stated, stop and return to H0;
8. define S1's validation dataset/scope and exact partition-key equality; prohibit cross-dataset, cross-scope and cross-key inference;
9. remove the ownerless multiple-superior exception from prose and enforce E1 unconditionally with one named reopening gate;
10. define Y1 for both Organization and relationship paths, including every terminal/historical-reference behavior and explicit non-Readiness/non-availability language;
11. complete R1 identity, endpoint, transition, target, cycle, branching, overlap/gap, independent effectivity and successor-attribution semantics with no redirect/head/winner projection;
12. preserve exact P-001 Module B and A/B/C invocation; complete every semantic slot locally and add no Pattern responsibility;
13. update only the Organization-specific checker module, Organization rules manifest and dedicated Organization tests, plus the minimal checker routing/import glue needed for dataset validation; no unrelated checker rule may change;
14. preserve all six current Organization fixtures unless an exact selected-rule migration is recorded, and add a finite manifest-complete synthetic evidence set for these eighteen mechanical groups: optional/no classification, opaque equal classifications, duplicate Organization IDs, duplicate transition IDs, lifecycle terminal paths/projections, missing/duplicate kind profiles, kind/class mismatch, missing/ambiguous endpoints, duplicate relationship IDs, exact partition scope, transient/all-time cycles, unconditional multiple superiors, unresolved/ambiguous supersession targets, supersession cycles, valid branching overlap, valid branching gaps/independent effectivity and record-order-independent no-head behavior;
15. map every new/changed validation or derivation identifier exactly once in `organization-rules.yaml` and make rule completeness fail closed;
16. update human-readable checker documentation and only the mechanical fixture/test-count projections produced by the bounded evidence set;
17. keep OCP-003, OCP-009, OCP-012–OCP-015, registries, taxonomy, foundation map, P-001, every Concept status and all non-Organization checker semantics byte-unchanged;
18. include all twenty-five §18 scenarios and twenty-eight §19 counterexamples with selected results in prose or exact references;
19. state data/reference migration, version compatibility, rollback and failure handling without deleting records, rebinding exact references, inventing transitions or choosing a newest winner;
20. preserve U0/M0, Resource-only CapabilityClaimRecord holders, exact OCP-009 binding, `Capability ≠ Readiness`, OCP-013 directionality and every Assignment/authority/interchangeability non-implication;
21. limit edits to OCP-007, the Organization checker/rules/tests and fixture directories, human-readable checker documentation, root README and the AB-062/roadmap projections; any need for another OCP, Concept projection, schema, graph or backlog-status edit stops the proposal; and
22. state that remediation completion or failure triggers a fresh exact blocker/stability/consumer/Pattern/route/migration audit and another Board act before any OCP-007 `1.0.0`, Organization lifecycle transition or T5 proposal.

Machine evidence is required for the mechanically expressible parts of C2/K3/T2/S1/E1/Y1/R1/U0/M0. Legitimacy of external kind ownership and real-world continuity remain human-review boundaries; they cannot be marked executable by proxy.

## 37. Selected scenario results

| # | Scenario | Required Q2 result |
|---:|---|---|
| 1 | display-name change | same exact Organization ID; name history/meaning is not identity authority |
| 2 | commander and relationship changes | same exact ID unless a separately governed continuity decision says otherwise |
| 3 | merger without a continuity owner | unresolved material-event identity; no automatic survivor ID |
| 4 | split into two represented entities | no automatic ID reuse or branch winner; exact new/retained identities require external decision evidence |
| 5 | conflicting same-ID/new-ID redesignation evidence | unresolved; no newest, majority or similar-ID selection |
| 6 | Established Organization without classification | valid under K3 when identity/history are otherwise valid |
| 7 | equal `organization-type://unit@1` annotations | two distinct Organizations; no unit/composition/mapping inference |
| 8 | K2 reference with zero/two/incomparable owners | K2 is not selected; K3 carries no classification meaning and makes no resolution claim |
| 9 | resolved kind declares a different class | relationship rejects with exact mismatch evidence |
| 10 | version-looking kind without resolver/owner | relationship rejects; `@` is syntax only |
| 11 | opposite structural edges in different partition keys | no cross-key cycle inference; neither key proves cross-scheme equivalence |
| 12 | transient structural cycle | rejects through the complete breakpoint sweep |
| 13 | two direct superiors in one partition | rejects unconditionally under E1 |
| 14 | producer supplies an exception label | no effect; no E2 owner/profile exists |
| 15 | simultaneous structural and operational records | two distinct records and meanings; neither collapses into the other |
| 16 | duplicate Organization or relationship ID | dataset rejects independent of order |
| 17 | endpoint or supersession target resolves zero/many | dataset rejects fail-safe |
| 18 | two overlapping successor branches | both branches remain visible with independent effectivity; no winner/head projection |
| 19 | provenance proposed as actor authorization | rejected; attribution alone grants no authority |
| 20 | Retired Organization with historical references | references continue to resolve to the same exact ID; Retired is not deletion |
| 21 | `unit@1` without composition/mapping | remains an opaque annotation only |
| 22 | related Organization and Resource without mapping | both identities remain; no projection is synthesized |
| 23 | Organization named as Capability holder | rejected by unchanged Resource-only OCP-012 contract |
| 24 | equal labels/relations offered as interchangeability evidence | rejected; OCP-013 remains Resource-specific and directional |
| 25 | Organization name/caller offered as Coordination authority | rejected by OCP-014/OCP-015 and Q2 non-authority rules |

## 38. Selected counterexample results

All twenty-eight AD-019 §19 counterexamples remain rejected under Q2:

1. remaining-T4 position does not select stabilization;
2. Canonical Resource does not require Organization mapping;
3. same name or commander does not decide post-event identity;
4. newest record or most common ID does not win continuity conflict;
5. stable exact ID does not define merger/split continuity;
6. a currently required label does not give Core its meaning;
7. `@` syntax does not prove a legitimate owner or resolver;
8. checker-accepted text does not acquire governed kind behavior;
9. similar class/kind labels do not prove agreement;
10. equal classifications do not create identity, equivalence or interchangeability;
11. equal partition strings from different scopes do not establish one scheme;
12. different partition keys do not authorize a cross-partition inference;
13. exception labels, reviewer comments and source counts do not authorize multiple superiors;
14. green graph tests do not prove scheme or exception authority;
15. structural subordination creates no composition, command, control or Resource ownership;
16. membership creates no Assignment, participation or Capability claim;
17. `unit@1` creates neither Resource nor unit identity;
18. equal Organization assertions create no Resource interchangeability result;
19. moving prose does not create a legitimate owner or Concept;
20. one file does not make every section one compatibility surface;
21. P-001 supplies no kind, partition, continuity or exception meaning;
22. non-empty endpoint strings do not prove exact endpoint resolution;
23. supersession creates no redirect or current head;
24. newest successor, source count or provenance does not win a branch conflict;
25. provenance alone authorizes no establishment, continuity or exception;
26. Established creates no activity, availability, Readiness, authorization or participation;
27. AD-019/AD-019A acceptance does not edit or implement OCP-007; and
28. review, CI and owner authorization do not transfer to remediation.

## 39. Alternatives not selected and reopening gates

### 39.1 Layout alternatives

- **H0 — hold** is not selected because the verified finite Q2 direction can be prepared under one owner without current consumer/reference migration. H0 becomes immediate fallback whenever a §36 or §40 stop fires.
- **H1 — monolithic in-place contract** is not selected because independent continuity, classification, kind, partition/exception and record-integrity burdens would be hidden behind the weakest unresolved member. It may reopen only if an exact proposal proves every axis inseparable under one compatibility promise.
- **H3 — extraction** is not selected because no current consumer, identity or one-owner defect requires reference-home or P-001 invocation transfer. It may reopen only when an attempted H2 remediation proves two readable surfaces cannot coexist without duplicate authority.
- **H4 — mapping-inclusive scope** is not selected because Canonical Resource and all current consumers permit M0. It may reopen only through concrete mapping-consumer evidence and a separate AB-006/AB-052 owner/identity act.

### 39.2 Axis alternatives

- **C0/C1:** C0 remains H0 only. C1 may reopen through a legitimate material-event decision owner, exact lineage identity, branching/conflict and provenance contract.
- **K0/K1/K2:** K0 remains H0 only. K1 requires evidence that Core owns a closed taxonomy. K2 classification requires named external owners plus a concrete shared classification consumer; neither is present.
- **T0/T1/T3:** T0 remains H0 only. T1 requires a proved complete Core kind registry. T3 may reopen only if the exact T2 envelope cannot be built and a separate comparison proves an OCP-local vocabulary and migration are smaller and semantically sufficient.
- **S0/S2/S3:** S0 remains H0 only. S2 requires a shared governed scheme consumer/owner. S3 requires proof that one universal structural graph preserves multiple verticals.
- **E0/E2:** E0 is internally contradictory and inadmissible. E2 requires a concrete legitimate exception consumer, versioned owner, effectivity and conflict contract.
- **Y0/Y2/Y3:** Y0 remains H0 only. Y2 requires a current consumer and exact additional stages/meaning. Y3 requires proof that historical exact identity remains useful without lifecycle.
- **R0/R2:** R0 remains H0 only. R2 requires an exact migration that removes Module C/supersession without reinterpreting or losing current history.
- **U1:** may reopen only under AB-047 through an explicit composition/unit identity, direction, lifecycle, graph and non-inheritance act.
- **M1:** may reopen only under AB-006/AB-052 with legitimate owners of both identities, exact absence/ambiguity behavior and no Assignment/Capability inheritance.

No alternative gains authority automatically from Q2 failure. A stop returns to H0 and requires a fresh Board comparison before another treatment is prepared.

## 40. Migration, rollback and failure handling

AD-019A itself changes no Organization or relationship record, consumer reference, checker behavior or lifecycle state.

The selected remediation is expected to preserve data mechanically:

- every `organization_id`, `relationship_id`, transition ID and historical exact reference remains unchanged;
- current `classification_refs` values remain replayable as optional opaque annotations;
- current class values remain coarse OCP-007 labels;
- current type values must either resolve through the exact T2 fixture/profile context or be reported as unresolved—never silently admitted;
- current `scheme_ref` values remain byte-preserved and gain only the narrower S1 dataset-local equality meaning;
- current lifecycle and effectivity histories are not invented, reordered or rewritten;
- existing supersession links remain historical inputs and gain no redirect/head meaning; and
- no Organization/Resource mapping, composition, Capability holder, Assignment or authority projection is synthesized.

Any type value that cannot satisfy T2 is migration evidence, not a reason to fabricate an owner. The remediation must list every affected fixture/value and either provide an exact legitimate test profile or stop. It cannot silently reinterpret T2 as T3.

Rollback of the later remediation must revert OCP-007, all Organization checker/rules/tests/documentation changes, Organization fixtures and mechanical count projections as one unit. It must not delete records, merge identities, rebind exact references, restore an ownerless exception, invent classifications/transitions or elect a newest branch.

The remediation stops and returns to H0/Board if it discovers:

- a direct normative OCP-007 consumer or Organization Concept edge omitted by AD-019;
- a current dependency on real-world continuity, required classification meaning, governed cross-scheme identity or a multiple-superior exception;
- no legitimate external/domain boundary capable of owning T2 kind profiles;
- a need for a Core registry, new Concept, Pattern, graph edge, mapping record, Organization Capability holder or joint Resource edit;
- exact endpoint/target resolution or Module C semantics that cannot remain under the one OCP-007 relationship owner;
- a need to choose a current head, redirect, newest record, majority or issuer/reviewer count;
- two plausible defining Organization or relationship surfaces;
- unreadable normative prose whose meaning depends on checker code or PR history;
- an OCP/checker/schema/backlog-status edit outside §36.21; or
- any non-replayable data/reference migration.

The proposal may not widen itself because the discovered edit appears small. Stop evidence must be recorded and reviewed before another direction is authored.

## 41. Authorization boundary

AD-019A selects only Q2 as the preparation direction and authorizes authoring one exact §36 remediation draft.

The OCP-007 remediation requires its own exact-head Fable review, Codex adjudication, green CI and explicit Pavlo/Architecture Board merge authorization. AD-019A authorization cannot merge that remediation, change OCP-007/Organization lifecycle, resolve AB-006/AB-044–AB-047/AB-051/AB-052/AB-062, create mapping or reopen T5.

After remediation completes or fails, a fresh audit must recompute blockers, stable surfaces, consumers, exact P-001/route ownership, executable evidence, migration and lifecycle readiness. A later Board act may then authorize another preparation step or retain hold. No authorization transfers across these gates.

## 42. Accepted effect and next gate

When exact-head reviewed, explicitly authorized and squash-merged, AD-019A will:

- set AD-019 to `0.2.0 / Accepted`;
- select Q2 (`H2 + C2 + K3 + T2 + S1 + E1 + Y1 + R1 + U0 + M0`) as the Organization stable-surface remediation direction;
- authorize preparation of one OCP-007 `0.4.0 / Draft` remediation under §36;
- retain H0 as immediate fail-safe and preserve every alternative reopening gate in §39;
- keep OCP-007 at `0.3.2 / Draft`, Organization at `Accepted`, P-001 unchanged, AB-006/AB-044–AB-047/AB-051/AB-052 `Open`, AB-062 `Planned` and readiness at approximately 70%; and
- change no OCP, Concept, Concept status, Pattern, dependency, registry row, taxonomy projection, foundation-map edge, schema, checker rule, fixture, backlog status or production authority.

AB-006, AB-044–AB-047, AB-051 and AB-052 remain the active backlog owners of mapping, continuity, kind, lifecycle, composition and scheme questions. Once AD-019 becomes Accepted, they no longer appear in its `Applies-To` metadata because this selection neither resolves them nor takes over their active ownership. This metadata handoff changes no question, status, scope or future reopening gate.

Authorization applies only to AD-019A. It cannot implement Q2, merge the OCP-007 remediation, admit an external kind owner, create a registry or mapping, introduce Organization Capability holders, promote Organization or authorize any lifecycle/T5 act.
