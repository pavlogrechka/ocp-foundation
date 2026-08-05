---
Document-ID: OCP-009
Title: Capability Concept
Version: 1.0.0
Status: Canonical
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, AD-005
Used-By: Capability Registry, Resource Claim Model, Operation Requirements, Interchangeability Decision
Defines-Concepts: Capability
Concept-Depends-On: []
Concept-Status: Canonical
Last-Review: 2026-08-05
---

# Capability Concept

## 1. Definition

**Capability** — ідентифіковане, версіоноване та повторно використовуване визначення здатності виконувати певний клас дії, забезпечувати стан або створювати визначений тип ефекту.

Capability має identity незалежно від конкретного Resource, Organization, Operation, Assignment, holder claim або поточного operational context.

Цей документ визначає definition-layer обраної в AD-005C двошарової моделі. Holder-specific Capability claim є окремим downstream record і не визначається OCP-009.

## 2. Purpose

Capability надає стабільний semantic reference, який може повторно використовуватися різними domain modules, майбутніми holder claims та Operation requirements без ототожнення label, holder або current usability з identity визначення.

OCP-009 відокремлює:

- reusable definition від holder-specific claim;
- definition identity від human-readable label;
- registry membership від possession;
- exact-version resolution від latest-version selection;
- supersession від прихованого переписування історичних references;
- Capability від Readiness, availability, capacity, authorization та admissibility.

## 3. Boundary

Capability не є автоматично:

- Resource або Resource type;
- Organization;
- Operation requirement;
- Assignment role;
- qualification, certification або accreditation;
- holder claim;
- current availability або capacity;
- Readiness або State;
- authorization, permission або admissibility;
- Constraint satisfaction;
- Event або Result;
- доказом того, що будь-який holder може застосувати здатність у поточному context.

Registry entry не створює relation `Resource has Capability` і не доводить possession.

## 4. Identity

Exact identity Capability визначається структурованим ключем:

```text
CapabilityReference
- namespace
- capability_id
- version
```

`namespace`, `capability_id` і `version` є окремими значеннями. OCP-009 не встановлює обов'язковий wire-format або delimiter для їх серіалізації.

Два records мають однакову exact identity тоді й лише тоді, коли всі три компоненти збігаються exact string equality після базової перевірки непорожності.

`label` не входить до identity. Однакові labels у різних namespaces або для різних `capability_id` не означають semantic equivalence.

## 5. Namespace governance

Кожен namespace має рівно одного `namespace_owner_ref` у межах одного registry dataset.

`namespace_owner_ref` є opaque reference на нормативного власника namespace — Core або domain specification, registry authority чи інший governed owner.

Namespace ownership визначає право публікувати definition records у namespace, але не надає operational authority, authorization або holder possession.

Domain modules можуть визначати specialized Capability у власних governed namespaces. Core не є універсальним каталогом domain labels.

## 6. Minimal Structure

```text
Capability
- namespace
- capability_id
- version
- label
- definition
- namespace_owner_ref
- published_at
- provenance_ref
- supersedes_capability_ref [optional]
```

### 6.1 namespace

Непорожня identity governed namespace.

### 6.2 capability_id

Непорожня стабільна identity Capability у межах namespace. Вона не залежить від holder, Operation або label.

### 6.3 version

Непорожній exact version token.

OCP-009 не вимагає SemVer. Registry та consumers порівнюють version за exact equality і не визначають latest version через lexical, numeric або timestamp ordering.

### 6.4 label

Непорожній human-readable label. Label призначений для представлення і пошуку, але не для identity resolution.

### 6.5 definition

Змістовне визначення здатності. Нормалізоване значення повинно містити щонайменше одну літеру або цифру.

Definition не містить holder-specific evidence, readiness, current availability або authorization.

### 6.6 namespace_owner_ref

Opaque reference на governed owner namespace.

### 6.7 published_at

Валідний timestamp публікації exact version у registry.

Timestamp не використовується для вибору authoritative або latest version.

### 6.8 provenance_ref

Непорожній opaque reference на attributable publication source або act.

Provenance не означає operational authorization, holder qualification або possession.

### 6.9 supersedes_capability_ref

Опційний exact `CapabilityReference` на попередню version того самого `(namespace, capability_id)`.

Supersession не є redirect, alias або mutation попереднього record.

## 7. Governed Registry Contract

`CapabilityRegistry` є governed collection та resolution authority для Capability definitions. Він не є окремим фундаментальним Concept.

Registry повинен:

1. зберігати exact identity кожного Capability record;
2. відхиляти duplicate exact identities;
3. забезпечувати однозначний exact-version lookup;
4. fail closed для malformed, missing або ambiguous references;
5. зберігати namespace ownership consistency;
6. перевіряти supersession targets та acyclicity;
7. не повертати іншу version замість requested exact version;
8. не виводити holder possession, Readiness, availability, authorization або admissibility.

Registry implementation, persistence, API та distribution model не визначаються OCP-009.

## 8. Exact Reference Resolution

Normative derivation:

```text
resolve_capability_definition(registry, reference)
```

Result є рівно одним Capability record, exact identity якого дорівнює requested `(namespace, capability_id, version)` і який задовольняє інваріанти OCP-009.

Якщо reference malformed, не має version, не має рівно одного candidate або candidate невалідний, authoritative resolution відсутня.

Resolver:

- не використовує label equality;
- не обирає latest version;
- не використовує `published_at` як tie-break;
- не переходить автоматично до successor;
- не виправляє namespace або version heuristic matching.

## 9. Supersession

Нова version може явно supersede попередню exact version того самого `(namespace, capability_id)`.

Supersession target:

- повинен існувати в registry;
- повинен мати той самий namespace і `capability_id`;
- повинен мати іншу version;
- не може створювати cycle.

Попередня exact version залишається валідним історичним Capability record та продовжує резолвитися за її exact reference.

Нові references на superseded version не redirect-яться автоматично. Domain policy може окремо забороняти нове використання superseded version, але Core registry resolution повертає exact requested record разом із наявною supersession інформацією.

Consumer references ніколи не переписуються автоматично.

## 10. Relationship and dependency boundary

Capability має `Concept-Depends-On: []`.

OCP-009 не вводить current Concept edge `Resource → Capability`, `Operation → Capability` або `Organization → Capability`.

Non-normative future edge `Resource ⇢ Capability` залишається planning intent до окремого holder-claim decision.

Operation requirement representation, holder claims та Resource interchangeability мають окремих normative owners.

## 11. Semantic Rules

1. Registry membership не означає, що Resource або Organization має Capability.
2. Resource classification або type label не створює Capability claim.
3. Assignment role не створює Capability claim.
4. Operation requirement не надає Capability holder.
5. Successful Event або Result не створює standing Capability claim автоматично.
6. Capability не означає Readiness, availability, capacity, authorization або admissibility.
7. Qualification, certification або accreditation можуть бути evidence input майбутнього claim, але не є Capability identity.
8. Label equality не є identity equality або equivalence.
9. Capability similarity не дозволяє автоматичну Resource substitution.
10. Holder-specific fields або claims не можуть бути вбудовані в Capability registry record.

## 12. Invariants

1. Кожен Capability record має непорожні `namespace`, `capability_id` і `version`.
2. Exact identity `(namespace, capability_id, version)` є унікальною в registry dataset.
3. `label` є непорожнім, а нормалізований `definition` містить щонайменше одну літеру або цифру.
4. `namespace_owner_ref` і `provenance_ref` є непорожніми opaque references.
5. `published_at` є валідним timestamp.
6. Усі Capability records одного namespace мають однаковий `namespace_owner_ref`.
7. Кожен `CapabilityReference` містить непорожні `namespace`, `capability_id` і exact `version`.
8. Exact reference резолвиться не більше ніж в один record; zero або multiple candidates не дають authoritative positive result.
9. `supersedes_capability_ref`, якщо присутній, є valid exact reference на існуючу іншу version того самого `(namespace, capability_id)`.
10. Граф supersession між exact Capability identities є ациклічним.
11. Resolution exact reference ніколи не повертає іншу version, включно з successor version.
12. Capability record не містить holder-specific possession, claim, readiness, availability, authorization або admissibility assertions.

Інваріанти 2, 6, 9 і 10 є dataset-level. Інваріанти 8 і 11 визначають resolver behavior.

## 13. Executable Evidence

Reference checker повинен містити щонайменше:

- позитивну deterministic resolution fixture: valid namespace + capability_id + exact version → рівно один record;
- namespace-collision fixture: однаковий label у двох namespaces лишається двома identities;
- unresolved exact reference fixture, що fail closed;
- duplicate exact identity fixture, що не може дати authoritative resolution;
- supersession-cycle fixture;
- exact historical reference fixture: superseded version резолвиться сама в себе, без redirect на successor;
- namespace-owner conflict fixture;
- holder-coupling fixture, що відхиляє possession assertions у registry record;
- valid context fixture, де наявність same-type Resources не створює holder claim.

Кожен emitted validation code входить до `ERROR_CODES`, має source у `rules.yaml` і бере участь в exact manifest equality. `resolve_capability_definition` входить до `DERIVATION_RULES`.

## 14. Examples

### Example A — deterministic resolution

Reference `(mobility, navigate, v1)` повертає рівно Capability `(mobility, navigate, v1)`, навіть якщо `(mobility, navigate, v2)` також існує.

### Example B — namespace collision

`label = "Relay"` у namespaces `communications` і `logistics` не створює одну identity. Resolver потребує exact namespace.

### Example C — historical superseded version

`v2` supersedes `v1`. Reference на `v1` продовжує повертати `v1`; Core не redirect-ить його на `v2`.

### Example D — registry is not possession

Registry містить definition `communications/relay/v1`. Це не створює твердження, що Resource `R-001` має таку Capability.

## 15. Non-Examples

Не є Capability definition самі по собі:

- текстовий label без governed identity;
- характеристика конкретного holder;
- поточний стан готовності;
- capacity measurement;
- qualification certificate;
- Operation requirement;
- Assignment role;
- факт успішного виконання;
- registry search result без exact version.

## 16. Explicitly Not Defined

OCP-009 свідомо не визначає:

- Capability Claim schema або lifecycle;
- relation `Resource has Capability`;
- Organization holder semantics;
- claim evidence, confidence або temporal applicability;
- Readiness, availability або capacity model;
- Operation requirement field;
- matching, ranking або optimization;
- Resource interchangeability;
- authorization, qualification або certification policy;
- domain Capability taxonomy;
- registry storage, API, replication або access control;
- latest-version selection policy;
- automatic migration або redirect;
- P-001 invocation.

## 17. Governed extensions and completed routing

Питання, які були відкритими у версії `0.1.2`, тепер мають явні межі:

- OCP-012 визначає holder-specific CapabilityClaimRecord з exact OCP-009 binding; claim не входить до Capability definition і не invokes P-001 від імені OCP-009;
- OCP-013 визначає directional Resource interchangeability для exact consumer requirement; однакові Capability claims не роблять Resources тотожними або взаємозамінними автоматично;
- exact owner Operation Capability requirements лишається окремим майбутнім contract і не виводиться з definition registry; і
- domain policy може заборонити нові references на superseded Capability version, але не змінює Core exact resolution і не переписує історичні references.

Це routing завершених і відкладених відповідальностей, а не імпорт downstream authority до OCP-009.

## 18. Architecture Board decision — PR-0010

Architecture Board прийняла OCP-009 і Concept `Capability` **4 серпня 2026 року** після повторного зовнішнього review head `65e41a8`, яке підтвердило закриття Findings 1–2 та відповідність мандату AD-005C.

Рішення Board:

- прийняти reusable Capability definition та governed registry contract, визначені OCP-009;
- встановити `Concept-Status: Accepted` на версії `0.1.2`;
- завершити AB-004 як `Resolved`;
- зберегти Capability як isolated Concept без current dependency edge;
- не вводити holder claim, `Resource has Capability`, Organization-holder semantics, Readiness, matching, interchangeability або P-001 invocation;
- залишити AB-011 та holder-specific Capability Claim окремими downstream-рішеннями.

`Accepted` не означає `Canonical`. Подальші зміни definition identity, namespace governance, exact resolution або supersession contract потребують нового явного normative cycle.

## 19. Canonical compatibility surface `1.x`

OCP-009 `1.x` стабілізує reusable Capability definition і governed registry contract у §§1–16. Воно гарантує:

1. exact Capability identity є трійкою `(namespace, capability_id, version)`;
2. label, holder, Operation, Assignment, claim, timestamp або registry order не входять до identity;
3. кожен namespace має одного governed `namespace_owner_ref` у межах registry dataset;
4. exact reference або резолвиться рівно в один валідний record тієї самої version, або не дає authoritative result;
5. resolver не обирає latest, не redirect-ить до successor і не виправляє reference евристично;
6. supersession зберігає обидві exact identities, історичну resolution та ациклічний same-definition lineage;
7. registry membership не створює holder possession, Resource relation, Readiness, availability, capacity, authorization, admissibility або Assignment eligibility;
8. CapabilityClaimRecord, Resource interchangeability та Operation requirements зберігають окремих normative owners; і
9. Capability лишається isolated fundamental Concept з `Concept-Depends-On: []`.

Canonical означає стабільну human-readable compatibility promise. Воно не означає production API, storage, distribution, universal taxonomy, truth, current usability, authorization, completeness або незмінність назавжди.

Для document lifecycle:

- PATCH може уточнювати prose, examples або links без зміни гарантій вище;
- MINOR може додати сумісну optional registry information або явно routed extension, якщо old exact records/references і всі дев'ять гарантій зберігаються; і
- MAJOR потрібен для зміни identity key, namespace authority, exact-resolution behavior, supersession semantics, definition/claim split або будь-якої non-equivalence boundary.

## 20. Independent version axes and admission boundary

OCP document version `1.0.0` не є значенням `CapabilityReference.version` і не переверсіоновує жоден Capability definition record. Capability definition version лишається opaque exact token під authority його namespace owner; OCP-009 не нав'язує SemVer або спільний clock цим records.

Core exact resolution і domain admission відповідають на різні питання:

```text
Core resolution: which exact governed definition does this reference name?
Domain admission: may this consumer create or accept this reference for this use?
```

Якщо `v2` supersedes `v1`, reference на `v1` продовжує exact-resolve-итися у `v1`. Це не дозволяє нове використання `v1`, не забороняє його і не обирає `v2`. Exact domain consumer може окремо прийняти policy, що забороняє нові `v1` references, але така policy не mutates registry history і не стає Core resolver authority.

## 21. Dependencies and evidence boundary

OCP-009 прямо залежить від:

- OCP-000 `1.1.0 / Canonical` для registry membership/status contract та синхронного Capability row;
- OCP-001 `1.0.0 / Canonical` для governance, L2 та atomic lifecycle rules;
- OCP-002 `1.1.0 / Canonical` для exact Concept-status projection та синхронного Capability value; і
- AD-005 `0.3.0 / Accepted` як decision source двошарової Capability моделі.

Жоден direct OCP dependency не є pre-canonical, тому L2 виконується без exception або same-act dependency promotion. OCP-009 не invokes P-001 і не має Concept dependency.

Existing checker rules and fixtures механічно перевіряють duplicate identity, exact resolution, namespace collision/ownership, unresolved references, supersession target/cycle, historical non-redirect, holder coupling та registry-not-possession. Вони не доводять legitimate namespace ownership, semantic quality definition, domain admission, holder truth, Readiness або production fitness. Ці питання лишаються human/domain review boundaries.

## 22. Atomic migration and rollback

T4 migration є одним узгодженим lifecycle unit:

1. OCP-009 document `0.1.2 / Draft → 1.0.0 / Canonical`;
2. defining `Concept-Status: Accepted → Canonical`;
3. OCP-000 `1.0.0 → 1.1.0`, де Capability row змінюється `Accepted → Canonical`;
4. OCP-002 `1.0.0 → 1.1.0`, де exact Capability projection змінюється `Accepted → Canonical`; і
5. generated current-state Foundation map та repository accounting синхронізуються з тими самими authoritative values.

Цей act не змінює Capability definition version, downstream document version, OCP-012 exact definition binding, P-001 invocation, Concept dependency, graph edge, checker rule, fixture, schema або production data. Existing exact Capability references не потребують rebinding.

Corrective rollback, якщо буде потрібний, проходить новий reviewed PR і повертає document/Concept status та всі projections разом. Partial projection edit або history rewrite заборонені.

## 23. Human counterexamples

1. Два records мають label `Relay`, тому це одна Capability — хибно без exact triple equality.
2. Capability є в registry, тому Resource володіє нею — хибно; потрібен окремий attributable claim contract.
3. `v2` supersedes `v1`, тому reference на `v1` повертає `v2` — хибно; resolver повертає exact `v1`.
4. `v1` exact-resolves, тому новий consumer зобов'язаний його допустити — хибно; admission належить exact domain policy.
5. Найновіший `published_at`, registry order або найбільша кількість publishers обирає version — хибно.
6. OCP-009 має version `1.0.0`, тому всі Capability definitions отримують version `1.0.0` — хибно; це незалежні version axes.
7. Canonical Capability доводить Readiness, availability, capacity, authorization або admissibility holder-а — хибно.
8. Два Resources мають однакові claims, тому вони тотожні або взаємозамінні — хибно; OCP-013 потребує exact directional consumer context.
9. Capability Canonical, тому Organization holder claims дозволені — хибно; OCP-012 initial holder boundary лишається Resource-only.
10. OCP-012 invokes P-001, тому OCP-009 теж invokes його — хибно; Pattern invocation не переноситься між owners.
11. Один Concept стає Canonical, тому сім інших Accepted Concepts змінюють status або compatibility — хибно.
12. Green checker або reviewer count обирає lifecycle status — хибно; статус виникає лише через exact-head review, Board authorization і merge.

## 24. T4 canonicalization act

Pre-T4 OCP-009 `0.1.2 / Draft` baseline має Git blob `b28219bffef4e527507d495c34dded5c2fb79346` і SHA-256 `119a26424b4c62140446fee6eca8d9baf68b2cd875e565321d63b1cc8064ddbb` на `main@b0ae0636d01a5e35c87bc4620314e6491b3b89d5`.

Sections 1–16 and the historical PR-0010 act in §18 remain semantically unchanged. Section 17 updates only responsibility routing after OCP-012/OCP-013, and §§19–23 make the existing compatibility, evidence and migration boundaries explicit.

When exact-head reviewed, separately owner-authorized and squash-merged, this act makes OCP-009 `1.0.0 / Canonical` and Capability the first `Canonical` fundamental Concept. The other seven defined Concepts remain `Accepted`; all Proposed candidate markers remain unchanged.

Authorization of AD-016D allowed preparation only and cannot authorize this merge. This T4 act requires fresh Fable approval, Codex adjudication, green CI and explicit Pavlo/Architecture Board authorization on its exact head. Its merge will not authorize OCP-003, OCP-007, OCP-008, OCP-012, any second T4 micro-wave or any T5–T10 promotion.
