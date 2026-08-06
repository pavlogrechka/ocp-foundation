---
Decision-ID: AD-018
Title: Resource Stable-Surface Discovery
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: OCP-001, OCP-003, OCP-007, OCP-016, AD-014, AD-016
Applies-To: AB-006, AB-052, AB-062, Resource 1.x compatibility boundary
Review-After: External comparison and a separate Architecture Board selection before any OCP-003 edit or lifecycle proposal
---

# AD-018 — Resource Stable-Surface Discovery

## 1. Mandate and purpose

AD-016J selected M3: prepare one bounded discovery of the Resource stable surface. It authorized a comparison, not a Resource model.

OCP-003 already contains a strong generic identity contract, but its current text mixes that contract with:

- a working taxonomy;
- an unresolved Organization/Organizational Resource/`Unit` boundary;
- informal structural relation labels;
- a general lifecycle without an exact transition authority; and
- stable infrastructure and consumable semantics embedded inside the working-taxonomy section.

That mixture makes two opposite shortcuts unsafe. Declaring the entire document stable could canonize unresolved authority. Excluding the entire taxonomy section could discard accepted identity distinctions that current examples and fixtures already rely on.

AD-018 compares five treatments of that surface. Revision `0.1.0` selects no outcome and changes no OCP, Concept, Pattern, dependency, graph edge, schema, checker rule, fixture or backlog status.

## 2. Exact baseline

This discovery starts from `main@359e0b3c05fb7ddf6940fc8e576c660ba6a6e989`, tree `4a30debf12d275e94550dbee0df1b8c313750650`, after the separately authorized AD-016J merge.

The exact governing inputs are:

| Input | State | Git blob | SHA-256 |
|---|---|---|---|
| AD-016 | `0.11.0 / Accepted` | `97f3e32453f13bf183c14d3f36e2dbc7132ed8da` | `fb1fdeda1e38932f6982c61e09eb87de38455a97cbcca86e994ff92a72248692` |
| OCP-003 Resource | `0.6.1 / Draft`; Resource `Accepted` | `721cad97a05970b6a089668040faeddd968cfe46` | `a90f651aa81f3f70f316566580d05aeca3be3359b33342ffdb0eb1d579526fbd` |
| OCP-007 Organization | `0.3.2 / Draft`; Organization `Accepted` | `543d579f9ce1033ff38d478d1663c71a10b5f118` | `93fdf3e2e71e844888306b22da4f46468418ed30f3a2a62b8a39a98e7c6b387b` |

The exact direct OCP-003 consumer set is:

| Consumer | State | Git blob | Resource dependency used here |
|---|---|---|---|
| OCP-004 Operation | `0.8.2 / Draft` | `f95acdec469baa8c44885853c055ad2fa326ac57` | Resource participates only through exact Assignment; AD-014 managed-site identity is preserved without a closed subtype or membership rule |
| OCP-005 Assignment | `0.2.2 / Draft` | `f50daff2f69898264f5a166c919f1299050ff456` | one exact Resource identity per Assignment; a Technical Resource example does not derive role from type |
| OCP-006 Constraint | `0.2.2 / Draft` | `5ae9245740b82e981880563287b3986574df4bfb` | Resource may be a subject; no Core subtype taxonomy is consumed |
| OCP-012 CapabilityClaimRecord | `0.3.0 / Accepted` | `cd2df0f1961b6d03eea0db66c8fdfce1f97cb235` | exact Resource-only holder identity and exact OCP-009 Capability version |
| OCP-013 Interchangeability | `0.2.0 / Accepted` | `658a291b4c3b9a0229aba09d485c1137723fe70b` | distinct candidate Resource identities under one directional requirement |
| OCP-014 Coordination profile | `0.2.0 / Accepted` | `23bd05b4bb14fd7a85101bd5a8b3dd733b53dd99` | exact contextual Resource requirement; no equality, ranking or selection authority |

The current Resource validator is anchored by blob `03586af0f94187b4e620076b3a29348025f26e40`, SHA-256 `45f68314e2b66b54facc786f0fb976d3ec98871400fbbb7a210808d86082db96`. The minimal Resource fixture is blob `765d8d898750ca1fa277d3cdbe0d0102ac2ecb97`, SHA-256 `a6e659a7c7d4ead2bbb378c26231172b267d994265bd82e1ba573a5661e46f16`.

The foundation has two Canonical and six Accepted Concepts; readiness remains approximately 69%. These are baseline facts, not evidence for an outcome. Hashes identify exact reviewed bytes; hash equality, Git order or recency never decides semantic authority.

## 3. Inherited mandates

Every admissible outcome must preserve all of the following.

1. Resource remains the accepted fundamental Concept for one identified managed element of the operational environment at a declared management granularity.
2. Resource identity is independent of type label, operational role, Assignment, Capability claim, availability, Readiness and interchangeability result.
3. `Organization ≠ Resource`. Any future mapping must be explicit and may not collapse either identity.
4. Exact Assignment is the sole current Core authority for Resource participation and operational role in one Operation.
5. Organization membership, Resource composition and shared classification do not create Assignment or participation by inheritance.
6. Capability definition and Resource-specific claim remain separate. CapabilityClaimRecord holders remain Resource-only and exact-bind one OCP-009 Capability version; claims do not inherit, aggregate or create transitive possession through Organization membership or Resource composition.
7. `Capability ≠ Readiness`; a positive claim creates no availability, authorization, admissibility, selection or Assignment.
8. OCP-013 interchangeability remains directional and consumer-specific. Equal type labels or claims do not make Resources equal, symmetric or automatically interchangeable.
9. AD-014's managed-infrastructure boundary remains binding: one managed site may be a Resource, while geometry, area, route, coverage and environment payload do not become that Resource by implication.
10. Consumable Resource identity remains the managed stock, lot, container, kit or accounting unit—not an abstract material kind or quantity value.
11. OCP-003 invokes no Pattern. AD-018 may not invent or inherit a P-001 invocation.
12. Resource retains `Concept-Depends-On: []`; no Organization, Capability, Assignment or other graph edge may be added in this discovery.
13. Domain-specific classification does not enter Core without the OCP-016 boundary route and a legitimate owner.
14. Unknown, conflicting or ownerless evidence fails safe. Newest timestamp, record order, label frequency, issuer count, reviewer count and implementation popularity are not authority rules.

## 4. Decision questions

AD-018 asks:

1. Which exact OCP-003 statements belong to a stable Resource `1.x` compatibility promise?
2. Which statements are working taxonomy, unresolved authority, scoped exclusion or cleanup?
3. Can Resource require at least one type/classification without owning a closed Core subtype vocabulary?
4. What semantic status do current labels such as `Technical Resource`, `Platform`, `Human Resource` and `Infrastructure Resource` have?
5. Does any current consumer require hierarchy or meaning from those labels, rather than merely carrying a non-empty classification value?
6. Can the Organization mapping be explicitly excluded while preserving `Organization ≠ Resource` and every current consumer guarantee?
7. Which stable infrastructure and consumable identity rules must survive even if the §5 tree is not part of `1.x`?
8. Is Resource composition part of stable identity semantics when no complete relationship-record authority is defined?
9. Is the current `Identified → Registered → Active → Retired` sequence admissible in `1.x` without an exact transition history, projection and provenance contract?
10. Can one document remain readable with both a stable normative kernel and a clearly non-governed working taxonomy?
11. Would extraction create a second defining owner or require reference migration?
12. What evidence would force joint Organization/Resource mapping work before Resource stabilization?
13. What is the smallest rollback unit for each outcome?
14. Which later Board act, if any, may authorize an OCP-003 remediation proposal?

## 5. Terms that must remain distinct

| Term | Meaning here | Not implied |
|---|---|---|
| Resource identity | one managed operationally significant subject at one declared granularity | type, role, holder claim, location payload or Organization identity |
| classification value | an explicit value attached to a Resource under some owner | membership in a closed Core taxonomy merely because the label appears in §5 |
| working taxonomy | the current illustrative §5 tree expressly marked non-Canonical | a governed exhaustive vocabulary or subtype reasoner |
| stable kernel | the smallest human-readable set of Resource identity, responsibility and non-implication guarantees proposed for versioned compatibility | a persistence schema or complete Resource model |
| Organization mapping | an explicit governed relation or projection between two preserved identities | identity collapse, membership inheritance or automatic Assignment |
| composition | one Resource contains or is composed of another while each modeled Resource keeps its identity | Organization structure, Assignment inheritance or transitive possession |
| lifecycle | governed existence-stage semantics under one transition authority | availability, Readiness, operational use or newest-record selection |
| explicit exclusion | a readable statement that a named surface is outside the compatibility promise | deletion, irrelevance or permission to reinterpret historical data |
| in-place split | one OCP with an explicit normative kernel and a clearly non-governed/deferred surface | two semantic owners inside one file |
| extraction | a separately governed defining surface with exact references and one owner | copying stable prose into a second authority |

## 6. Current OCP-003 surface ledger

The labels below are discovery classifications, not accepted lifecycle results:

- **K** — candidate stable-kernel statement;
- **B** — unresolved authority/identity question that blocks inclusion;
- **S** — candidate explicit exclusion from the stable surface; and
- **C** — current-state or wording cleanup that must not change identity.

| OCP-003 surface | Evidence that may be stable | Current B/S/C issue |
|---|---|---|
| §§1–4 definition, scope and identity | managed operational subject, declared granularity, discrete and managed-stock identity, type does not replace identity | §2 lists availability, belonging and use as model purposes although exact owners live elsewhere; §3 says Organization defines belonging without a mapping contract (B/C) |
| §5 working taxonomy | useful examples of people, technical assets, managed sites and consumable stocks | the tree is explicitly non-Canonical; no exhaustiveness, hierarchy authority, label identity or versioning contract exists (B/S) |
| §5.1 Human Resource | a person or identified group may satisfy generic Resource identity; Actor remains contextual | `Human Resource`, `Crew` and `Duty Team` are not governed as a closed Core vocabulary (S) |
| §5.2 Organizational Resource | explicitly states Organization and Organizational Resource are not identical | `Unit` status and mapping owner remain open under AB-006/AB-052 (B) |
| §5.3 Technical Resource | domain characteristics stay outside generic Resource identity | wording that specialized “types belong to Capability” risks confusing classification with Capability definition/claim ownership (C) |
| §5.4 Infrastructure Resource | AD-014 supplies a stable managed-site discriminator and spatial/environment non-implications | stable semantics are embedded in the working taxonomy and must not disappear under blanket exclusion (B for placement) |
| §5.5 Consumable Resource | managed-stock identity and quantity non-identity are explicit and used by OCP-003 invariants | stable semantics are embedded in the working taxonomy; exact quantity/reservation/consumption stays deferred (B for placement, S for quantity model) |
| §6 Assignment boundary | exact Assignment owns operational role and participation | no blocker found; status wording may need current projection cleanup only (K/C) |
| §7 structural relation labels | membership and composition must not imply participation | `belongs_to`, `may_be_part_of` and `may_contain` have no exact record, owner, directionality, effectivity or mapping contract (B/S) |
| §7 Capability/Constraint boundary | claim is separate from identity; positive claim has no Readiness/selection implication | no new Resource→Capability edge or Organization holder may appear (K) |
| §7 spatial/temporal boundary | Operation-local payload is not Resource location or Assignment evidence | Resource location/effectivity authority remains excluded (K/S) |
| §8 composition | a modeled component keeps distinct identity; composition is not Organization structure | no complete composition relation, cycle, effectivity or authority contract exists (K for non-implications, B/S for representation) |
| §9 lifecycle | existence lifecycle is distinct from availability/Readiness | stage sequence has no record shape, allowed-transition contract, authoritative history, provenance or projection rule (B/S) |
| §§10–12 rules and invariants | identity, managed-stock granularity, contextual role, no Assignment inheritance and no quantity-as-Resource are stable candidates | invariant 12.3 requires type/classification but does not define its owner or whether free labels, references or profiles satisfy it (B) |
| §§13–14 examples/non-examples | expose intended identity boundaries in readable form | battalion example remains conditional; examples cannot create taxonomy authority (C/B) |
| §§15–16 open/deferred questions | honestly preserve availability, grouping, quantity and Organization mapping gaps | none may silently enter `1.x` or be marked resolved (S) |
| §17 PATCH history | exact historical status correction | historical evidence only; not part of the semantic kernel (C) |

The provisional ledger shows that the stable candidate is larger than “resource_id only” but smaller than the current document. It also shows why a whole-section deletion is not automatically safe.

## 7. Consumer and executable evidence

### 7.1 Direct consumers

The exact §2 direct consumers require the following and no more:

- OCP-004 resolves Resource participation through Assignment and rejects ownership, membership, spatial or readiness implication.
- OCP-005 exact-binds one Resource identity; type does not define role; Organization membership and composition do not inherit Assignment.
- OCP-006 may target Resource or Resource-related scopes but does not use the §5 subtype hierarchy as evaluation authority.
- OCP-012 resolves a Resource-only holder by exact `resource_id`; exact Capability binding and claim evidence remain outside Resource identity.
- OCP-013 preserves candidate identities and evaluates one directional consumer requirement; matching labels or claims do not create equality.
- OCP-014 activates one exact Coordination requirement owner and creates no Resource equality, ranking, selection or replacement authority.

No direct consumer requires `Unit`, Organizational Resource, `Resource belongs_to Organization`, the §9 lifecycle sequence or a closed subtype hierarchy.

### 7.2 Classification values in fixtures

The current suite and direct-consumer prose do use classification labels:

- the minimal Resource fixture uses `Technical Resource` and `Platform`;
- CapabilityClaimRecord and interchangeability fixtures use `Technical Resource`;
- integrated Event scenarios use `Human Resource` and `Infrastructure Resource`;
- OCP-004 preserves the AD-014 managed-site `Infrastructure Resource` discriminator, while OCP-005 uses a `Technical Resource` example without deriving its role from that label; and
- the Organization fixture value `organization-type://unit@1` is an Organization classification reference, not a Resource subtype or mapping.

Those uses defeat the claim “the working taxonomy is unused.” They do **not** prove that the labels form a closed Core taxonomy. The current Resource validator checks only:

1. non-empty `resource_id`;
2. at least one non-empty entry in `classifications`; and
3. no direct self-reference in `contains_refs`.

It does not validate classification membership, parent/child hierarchy, label equivalence, Organization mapping, lifecycle, composition closure or semantic authority. Green fixtures are finite compatibility witnesses, not a Board decision about the label vocabulary.

### 7.3 Evidence boundary

Machine evidence can prove exact references, non-empty classifications, identity preservation in current scenarios, self-containment rejection, Assignment non-mutation, exact Capability version resolution and absence of a Concept edge. It cannot decide:

- whether `Unit` has one identity or two;
- whether a classification label belongs in Core;
- whether a human-readable section is unambiguously normative;
- whether an Organization mapping owner is legitimate;
- whether a general lifecycle is semantically complete; or
- whether extraction creates one owner rather than duplicate authority.

## 8. Authority boundary

AD-018 assigns no new authority. Every later option must respect this ledger:

| Responsibility | Current owner | Forbidden transfer |
|---|---|---|
| generic Resource identity | OCP-003 | taxonomy label, Capability claim, Organization or checker cannot redefine it |
| operational role/participation | exact Assignment under OCP-005 | membership, composition, type or claim cannot create it |
| Organization identity/relations | OCP-007 and future accepted mapping owner | Resource prose cannot collapse or project Organization implicitly |
| Capability definition | exact OCP-009 version | Resource classification does not become Capability |
| Resource-specific Capability proposition | OCP-012 claimant/record contract | Resource identity or registry membership does not make it true |
| directional suitability/interchangeability | OCP-013 plus exact consumer contract | equal label/claim, checker result or incumbent Resource cannot generalize it |
| managed-site discriminator | OCP-003 with accepted AD-014 boundary | geometry/environment payload cannot become identity authority |
| domain classification vocabulary | named domain owner unless separately admitted | frequency or Core fixture use cannot promote it |
| executable validation | cited OCP rules | checker shape cannot create taxonomy or lifecycle meaning |

### 8.1 Conditional OCP-016 route hypotheses

| Candidate responsibility | Route hypothesis | Stop condition |
|---|---|---|
| generic Resource identity and invariants | F — existing fundamental Concept boundary in OCP-003 | a second defining Resource owner appears |
| local Resource classification value | F only for the minimal Resource-owned binding; D for domain meaning; E only if a concrete shared consumer proves an exact envelope | Core starts governing specialized label meaning by occurrence |
| Organization/Resource mapping | F if it is an invariant relation between existing Concepts; C if a separately identified mapping/projection record is proved necessary | no legitimate owner, identity collapse or hidden graph dependency |
| working classification catalog | D or I unless separately admitted | catalog placement is treated as semantic admission |
| extracted Resource surface under RX | artifact-home change inside F, not a new Concept | two defining locations or incomplete consumer resolution |

These are route hypotheses, not admission decisions. RI must separately decide whether any identified mapping record invokes P-001 and, if so, provide a complete exact-version invocation; no Resource or Organization contract supplies it by inheritance.

## 9. Candidate outcomes

### R0 — hold

OCP-003 remains Draft with no stable-surface remediation selected. The accepted Resource Concept and current consumers remain unchanged. Reopening requires a concrete consumer, authority or compatibility fact that makes one positive option reviewable.

R0 is the fail-safe. Its cost is that verified generic guarantees remain mixed with unresolved surfaces and cannot support a lifecycle proposal.

### RI — resolve and include mapping

A future Resource surface includes an explicit Organization ↔ Organizational Resource/`Unit` mapping. The mapping must preserve two identities, name one legitimate relation/projection owner, define directionality and replay, and state when no Resource projection exists.

RI may not use same label, shared real-world referent, Organization classification or participation as identity proof. Its principal risk is importing OCP-007 continuity/classification blockers and resolving AB-006/AB-052 inside an oversized Resource change.

### RE — explicit exclusion

A future Resource `1.x` surface explicitly excludes the working taxonomy and Organization mapping. Current classification values remain accepted only as opaque values under their actual owners; Core promises neither their hierarchy nor equivalence. Stable managed-site and managed-stock rules must be restated outside the excluded tree if retained.

RE is the smallest direct boundary. Its principal risk is normative residue: readers may still treat detailed §5 prose and examples as governed, or blanket exclusion may accidentally discard accepted identity semantics embedded there.

### RS — in-place stable kernel

OCP-003 remains the single defining document but is reorganized into:

1. one explicit normative stable kernel;
2. one explicit exclusions/deferred section; and
3. one clearly non-governed working classification catalog.

Stable infrastructure, consumable, Assignment, Capability and composition non-implications may move into the kernel without governing the taxonomy tree. Unresolved mapping, lifecycle, location, availability and quantity models remain outside `1.x`.

RS preserves one owner and can make the mixed surface readable. Its principal risk is a false split: two sections in one file may still act as competing authorities unless section-level versioning and wording are exact.

### RX — extracted stable kernel

A separately governed defining surface owns the Resource stable kernel, while OCP-003 becomes a wrapper or working companion with exact references and no duplicated normative prose.

RX can create a visually clean boundary. Its principal risks are a second defining owner, dangling links, consumer migration and uncertainty about which artifact defines Resource identity. Extraction is inadmissible unless one owner and one exact resolution path are proved.

## 10. Outcome completeness and interaction

The outcome set spans the available governance treatments:

- leave the question undecided (R0);
- decide and include the disputed mapping (RI);
- decide and exclude the disputed surface (RE);
- split stable and working surfaces under one owner (RS); or
- split them across artifacts with one exact defining owner (RX).

Common apparent alternatives reduce to those treatments:

- deleting §5 is RE plus cleanup;
- delegating all labels to domain profiles is RE with named owners;
- a one-way Organization→Resource projection is RI;
- moving the tree to a non-normative annex is RS if the owner/file stays one, or RX if the authority home changes; and
- retaining the current document until more evidence appears is R0.

RI/RE describe the treatment of disputed semantics; RS/RX describe how a stable/working split is governed. A later Board may select an explicit composite only if it states precedence and proves there is still one defining Resource authority. An implicit mixture is not an outcome.

## 11. Comparison axes

Every option is compared on the same axes:

1. Resource identity preservation;
2. Organization identity and mapping authority;
3. classification ownership and versioning;
4. current direct-consumer compatibility;
5. fixture replay without label reinterpretation;
6. Assignment, Capability and interchangeability non-implications;
7. infrastructure, consumable and composition semantics;
8. lifecycle/exclusion honesty;
9. one defining location and human readability;
10. migration and rollback size;
11. future OCP-003 versioning behavior; and
12. fail-safe response to unknown/conflicting evidence.

## 12. Preliminary comparison matrix

| Outcome | Identity/authority | Current compatibility | Readability | Migration/rollback | Preliminary result |
|---|---|---|---|---|---|
| R0 | preserves every current boundary | byte-identical | leaves mixed stable/working prose | none | admissible fail-safe |
| RI | positive only with explicit two-identity mapping owner | could preserve consumers, but none currently requires mapping | clear only after Organization decisions | largest; may touch both OCPs and data profiles | blocked on current evidence |
| RE | can preserve generic identity and opaque labels | viable if every stable §5 guarantee is restated and fixtures keep replaying | risk of normative residue in detailed excluded prose | bounded but requires exact inclusion/exclusion ledger | admissible, not leading |
| RS | preserves one OCP-003 owner and can retain stable scattered rules | strongest path to replay current consumers/labels without claiming closed taxonomy | strongest if normative and working sections are unmistakable | one-document remediation; rollback can be atomic | leading hypothesis only |
| RX | can isolate a clean kernel if one owner remains | requires exact reference and consumer resolution | visually clean | unnecessary reference/home migration unless RS fails | admissible control, not leading |

The matrix does not select RS. It records why RS currently deserves the strongest attack in external comparison.

## 13. Provisional stable-kernel guarantees

Any positive option must either preserve these guarantees or demonstrate that a named guarantee belongs outside Resource `1.x` without weakening a current consumer:

1. one Resource has one non-empty stable identity at a declared management granularity;
2. identity is independent of type/classification and two equally classified Resources remain distinct;
3. a discrete object/group and a managed stock/lot/container/kit may each satisfy Resource identity under their declared granularity;
4. abstract material kind, quantity value, geometry, role, status and Capability definition are not Resource identities;
5. exact Assignment owns participation and operational role; membership, composition and type do not create Assignment;
6. a separately modeled component keeps identity and does not inherit the composite Resource's Assignment;
7. managed infrastructure remains distinct from its footprint, coverage, area and environmental description;
8. managed consumable identity remains distinct from quantity, reservation and consumption state;
9. Resource-specific Capability claims remain separate identified records with Resource-only holders and exact OCP-009 version binding;
10. Capability, claim support and registry membership create no Readiness, availability, authorization, admissibility, selection or Assignment;
11. contextual interchangeability preserves candidate identities and creates no symmetry, transitivity or general equality; and
12. classifications may be required structurally without becoming a closed Core hierarchy unless a later accepted owner/version contract says so.

This list is a comparison hypothesis, not a `1.x` contract. The later selection must accept, revise or reject every row explicitly.

## 14. Mandatory human scenarios

Each positive outcome must give one readable deterministic treatment for:

1. two separately identified technical assets carry the same `Platform` classification;
2. one crew participates in two Operations under two exact Assignments;
3. one composite technical Resource contains a separately identified component;
4. the composite has an Assignment but the component does not;
5. one managed launch site and one equal-geometry Operation spatial payload coexist;
6. one fuel stock has a changing quantity while its Resource identity remains stable;
7. a battalion is an Organization, while no Organizational Resource projection has been authorized;
8. a domain profile uses a specialized Resource classification unknown to Core;
9. two Resources have equal positive Capability claims but fail or differ under one directional requirement;
10. a Resource is retired under some future local lifecycle, while historical Assignment/claim references still resolve;
11. one current fixture uses `Technical Resource` after the Core working taxonomy is excluded or split; and
12. an Organization fixture contains `organization-type://unit@1` without creating a Resource or mapping.

All scenarios remain synthetic and non-sensitive.

## 15. Mandatory counterexamples

External review and the later Board act must reject these conclusions:

1. `Technical Resource` appears in many fixtures, therefore it is a Canonical Core subtype.
2. The checker accepts a classification string, therefore it governs that label's meaning.
3. Two Resources share classifications, therefore they are equal or interchangeable.
4. Two Resources share Capability claims, therefore either may replace the other.
5. A Resource belongs to an Organization, therefore it participates in an Operation.
6. A composite Resource is assigned, therefore every component is assigned.
7. `Unit` is an Organization classification value, therefore the same instance is also a Resource.
8. `Resource belongs_to Organization` is written in §7, therefore a current Concept edge or mapping record exists.
9. A Resource is `Active`, therefore it is available, ready, authorized or in use.
10. A managed site and equal geometry are the same Resource.
11. A fuel quantity change creates a new Resource automatically, or quantity itself is a Resource.
12. Excluding a taxonomy permits deleting stable infrastructure/consumable identity guarantees.
13. Keeping one file makes all its sections equally normative.
14. Extracting prose automatically creates a legitimate new defining owner.
15. Newest taxonomy version, record order, source count, issuer count or majority selects meaning.
16. P-001 applies because other identified records use it.
17. Resource Canonicalization would make Operation, Assignment, Constraint or Organization Canonical.
18. AD-018 approval selects RS or authorizes an OCP-003 edit.

## 16. Unconditional evidence obligations

The following apply to R0/RI/RE/RS/RX:

1. exact-anchor the baseline and all changed comparison inputs;
2. preserve Resource and Organization identity separation;
3. preserve exact current consumer resolution and historical Resource references;
4. account for every current classification-bearing fixture without treating label occurrence as semantic authority;
5. preserve Assignment, CapabilityClaimRecord and interchangeability ownership boundaries;
6. reject identity, participation, readiness, authorization and equality implications not owned by an exact contract;
7. state one defining Resource authority or retain hold;
8. make missing, ambiguous, conflicting or ownerless evidence fail safe;
9. provide human-readable scenarios, counterexamples, migration and rollback; and
10. keep machine evidence structural and subordinate to cited normative text.

No unconditional fixture may require an Organization mapping, closed taxonomy, extracted artifact, in-place section layout, lifecycle record or domain profile. At least one admissible outcome rejects each mechanism.

## 17. Outcome-conditional evidence and equivalents

| Outcome | Conditional evidence | Equivalent for the shared guarantees |
|---|---|---|
| R0 | exact baseline replay and a concrete reopening trigger; no invented migration | unchanged current resolution is the replay witness |
| RI | two-identity mapping/projection cases, legitimate owner/version, absent-mapping behavior, no automatic Assignment and AB-006/AB-052 resolution path | mapping determinism plus fail-safe absence replaces exclusion evidence |
| RE | exact included/excluded section ledger, current-consumer replay, opaque-label preservation and detection/rejection of mapping assumptions | explicit ambiguity rejection replaces mapping fixtures |
| RS | section-level defining/non-governed boundary, stable-rule relocation ledger, readable snapshot review and no duplicate in-file authority | one resolvable kernel plus working-surface exclusion replaces extraction migration |
| RX | one defining owner, exact wrapper/consumer references, no duplicated normative prose, complete migration and atomic rollback | exact single-owner resolution replaces same-file boundary evidence |

Evidence is outcome-fair only if each selected mechanism covers the shared identity and replay guarantees without being required to implement a layer it rejects.

## 18. Migration and rollback questions

This discovery creates no migration. A later selection must account for:

- preservation of every existing `resource_id` and exact consumer reference;
- whether current unversioned classification strings remain valid as opaque values;
- whether `contains_refs` remains structural evidence or gains a separately governed relation contract;
- movement of stable infrastructure and consumable rules without semantic loss;
- treatment of the current lifecycle text without inventing historical transitions;
- exact status/version projections if OCP-003 is later remediated;
- no OCP-007 edit or Organization-reference migration unless a separately selected RI/M37 scope authorizes it; and
- rollback without deleting Resources, merging identities, rebinding Assignments/claims or reinterpreting historical labels.

RE and RS should normally require no data migration if labels remain opaque and Resource identity is unchanged. That is a hypothesis to falsify, not a granted compatibility conclusion. RX must prove reference-home migration. RI must prove mapping migration and absent-mapping semantics.

## 19. Falsification targets

External review and the later Board selection must try to demonstrate any of the following:

1. a direct current consumer requires `Unit` or Organizational Resource semantics;
2. a current valid fixture relies on parent/child meaning or closed membership of the §5 taxonomy;
3. Resource identity cannot remain exact when classification meaning is domain-owned or opaque to Core;
4. OCP-004/OCP-005/OCP-006/OCP-014 relies on classification meaning beyond the accepted managed-site discriminator or illustrative example, rather than exact Resource identity/context;
5. `Resource belongs_to Organization` already creates an unavoidable compatibility guarantee;
6. stable managed-infrastructure or consumable semantics cannot survive exclusion of the taxonomy tree;
7. a current consumer requires the §9 lifecycle stages as authoritative Resource state;
8. RS cannot make one file human-readable without two semantic owners;
9. RX is necessary because no in-place boundary can produce one exact defining surface;
10. a legitimate RI mapping owner and sufficient Organization continuity evidence already exist;
11. a genuinely distinct sixth treatment exists outside R0/RI/RE/RS/RX;
12. the evidence matrix assumes a mapping, storage, section or extraction layer rejected by an outcome;
13. current checker/fixture behavior claims stronger classification semantics than §7 reports; or
14. a positive option requires an OCP-003/OCP-007 edit merely to complete discovery evidence.

If 1, 5 or 10 succeeds, RE/RS lose their immediate lead and the work returns to M37/RI Board consideration. If 6 succeeds, blanket RE loses strength while RS or R0 remains. If 8 succeeds, RS loses its lead to RE/RX/R0. If 9 succeeds, RX becomes the leading hypothesis. If 11 succeeds, the matrix must be revised before selection. If 12 or 14 succeeds, the discovery fails outcome-fairness and stops.

Unknown or conflicting evidence always returns to R0; it never becomes a permissive classification or mapping.

## 20. Preliminary recommendation

The strongest current hypothesis is **RS — one in-place stable Resource kernel**, with R0 as fail-safe.

RS leads because:

- current consumers need generic Resource identity and non-implications, not the disputed Organization mapping;
- current fixtures carry useful classification labels without depending on a closed hierarchy;
- stable infrastructure and consumable rules are embedded in the working-taxonomy section and should not be discarded by blanket exclusion;
- one OCP-003 owner avoids the reference and authority migration introduced by RX; and
- an explicit kernel/working split can keep unresolved lifecycle, mapping, quantity and classification semantics visible without placing them in `1.x`.

The principal RS risk is **false readability**: a document may claim that one section is non-governed while detailed examples and familiar labels continue to be read as normative. A later RS proposal must use unmistakable section-level language, an exact relocation ledger and human counterexamples. If it cannot, R0, RE or RX is safer.

RI does not lead because the legitimate mapping owner and Organization continuity evidence are not ready. RE does not lead because excluding the whole working section is too blunt until stable embedded guarantees are relocated. RX does not lead because no evidence yet justifies a second artifact or reference migration.

This is a recommendation only. AD-018 does not select RS or authorize preparation of an OCP-003 patch.

## 21. Exit criteria and mandatory next Board act

AD-018 is ready for Board selection only when external review confirms:

1. exact baseline and direct-consumer completeness;
2. a complete K/B/S/C surface ledger;
3. fair R0/RI/RE/RS/RX definitions and no missing treatment;
4. all §19 attacks attempted with written results;
5. unconditional and conditional evidence obligations cover every outcome fairly;
6. current fixture labels are accounted for without Core taxonomy promotion;
7. stable infrastructure/consumable semantics are not lost;
8. Organization, Assignment, Capability and interchangeability boundaries remain intact;
9. migration/rollback is bounded for every positive option; and
10. the argument is readable without checker code or historical PR context.

A separate **AD-018A — Select Resource Stable-Surface Outcome** Board act must then:

1. exact-anchor the then-current baseline;
2. accept, revise or reject every §6 classification;
3. attempt all §19 targets again against any changed evidence;
4. select R0, RI, RE, RS, RX or a newly proved complete alternative;
5. state the exact next artifact and allowed edit boundary;
6. define stop conditions, migration/rollback and non-transfer; and
7. authorize preparation only—not merge, Concept status change or lifecycle transition.

If RS is later selected, the next proposal may be an OCP-003 remediation draft only. After that remediation completes or fails, a fresh blocker/stability audit and another Board act are still required before any OCP-003 `1.0.0` lifecycle proposal.

## 22. Discovery status and accounting

When exact-head reviewed, explicitly authorized and squash-merged, AD-018 will:

- establish `AD-018 0.1.0 / Discovery`;
- record the exact Resource/Organization and direct-consumer baseline;
- preserve R0 as fail-safe and record RS only as the leading hypothesis;
- keep RI/RE/RX fully admissible under their evidence conditions;
- require a separate AD-018A Board selection before any OCP-003/OCP-007 edit;
- leave AB-006 and AB-052 `Open`, AB-062 `Planned`, and readiness at approximately 69%; and
- change no OCP, Concept, Pattern, dependency, projection, registry row, graph edge, schema, checker rule, fixture or production authority.

Fable approval, Codex adjudication, green CI and explicit Pavlo/Architecture Board authorization apply only to this discovery record. They cannot select RS, merge AD-018A, edit OCP-003/OCP-007, resolve AB-006/AB-052, change Resource/Organization status or authorize a third T4 lifecycle act.
