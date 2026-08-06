---
Document-ID: OCP-003
Title: Resource Concept
Version: 0.7.0
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, AD-014
Used-By: Operation Concept, Assignment Concept, Organization Model, Capability Model, Domain Model
Defines-Concepts: Resource
Concept-Depends-On: []
Concept-Status: Accepted
Last-Review: 2026-08-06
---

# Resource Concept

Цей документ є єдиним визначальним місцем для фундаментального Concept `Resource`. Його зміст має рівно три семантичні поверхні:

1. **Part I (§§1–12) — normative stable kernel:** позитивні гарантії identity та non-implication rules;
2. **Part II (§13) — explicit exclusions/deferred surface:** нормативна межа того, чого kernel не визначає;
3. **Part III (§14) — non-governed working catalog:** читабельні приклади classification values без Core authority.

Part I і Part II разом утворюють чинний контракт OCP-003. Part III не є другим власником семантики. Evidence, relocation і versioning appendices (§§15–20) пояснюють та перевіряють контракт, але не створюють четвертої семантичної поверхні.

## Part I — Normative stable kernel

## 1. Definition

**Resource** — один ідентифікований керований елемент реального операційного середовища на явно визначеному рівні гранулярності управління.

Resource може бути конкретною людиною або групою людей, технічним засобом, керованим інфраструктурним об’єктом, ідентифікованим матеріальним запасом або іншим операційно значущим subject. Належність до цієї множини визначає не назва classification, а наявність окремої керованої identity на обраній гранулярності.

Resource може бути exact-bound іншими контрактами, зокрема Assignment, CapabilityClaimRecord або Constraint. Сам факт такого binding не входить до Resource identity і не змінює її.

## 2. Purpose and scope

OCP-003 дає Core одне точне посилання на керований операційний subject. Це дає змогу іншим власникам пов’язувати той самий Resource з Operation, Assignment, Capability claim, Constraint або contextual requirement без повторного визначення його identity.

Resource не визначає:

- Organization identity, membership або Organization-to-Resource mapping;
- повноваження користувача чи актора;
- роль або участь у конкретній Operation;
- availability, health, Readiness або current use;
- location, geometry, environment чи lifecycle authority;
- coordination, admissibility, selection або interchangeability result; чи
- quantity, reservation, consumption або capacity model.

OCP-007 визначає власну Organization identity та Organization relations. Він не створює Resource, Resource membership або mapping між цими Concepts за implication. Участь і роль у конкретній Operation належать exact Assignment за OCP-005.

## 3. Identity and management granularity

Кожен Resource має непорожню стабільну identity на заявленому рівні операційного управління та відрізняється від інших Resource, навіть коли вони мають однакові classification values.

Для дискретних Resource identity належить конкретному subject або керованій групі, наприклад конкретній особі, екіпажу, борту, засобу РЕБ, ретранслятору чи майданчику запуску.

Для взаємозамінних або витратних матеріалів identity належить керованому запасу, партії, контейнеру, комплекту або іншій обліковій одиниці, а не абстрактному виду матеріалу чи кожній фізичній частці.

Identity Resource не залежить від:

- type/classification label;
- operational role або Assignment;
- Capability definition або CapabilityClaimRecord;
- availability, health чи Readiness;
- interchangeability, suitability або selection result; чи
- порядку, часу або кількості зовнішніх записів про Resource.

Зміна будь-якого з цих зовнішніх фактів сама по собі не merge-ить, не split-ить і не замінює Resource identity. Окреме майбутнє identity rule може визначити інший результат лише у власному accepted контракті.

## 4. Classification binding

Кожен Resource має щонайменше одне непорожнє classification value. Для Core це **opaque value**: OCP-003 не оголошує закритий або вичерпний словник, parent/child hierarchy, equivalence, precedence чи автоматичну відповідність Capability.

Поточні рядки на кшталт `Technical Resource`, `Platform`, `Human Resource` та будь-яке namespaced domain value однаково придатні як непорожні opaque values. Рівність або схожість таких значень не доводить рівність Resource, спільну роль, Capability, Organization membership або interchangeability.

Спеціалізоване значення classification може тлумачитися лише через exact named owner/profile поза цим kernel. Domain-specific classification входить до Core лише через OCP-016 Core Boundary route та легітимного owner. Якщо owner, profile або exact version не визначені чи конфліктують, specialized meaning є unresolved і fail-safe не застосовується; саме Resource та його opaque value залишаються валідними.

Newest timestamp, record order, label frequency, issuer count, reviewer count або implementation popularity не є правилами вибору classification authority.

## 5. Stable managed-site and managed-stock identity

### 5.1 Managed infrastructure

Конкретний керований Position Site, Launch Site, Relay Site або інший infrastructure subject з власною стабільною identity, management boundary та use history може бути Resource відповідно до accepted AD-014 boundary.

Його footprint, geometry, area, route, coverage, environment payload або condition snapshot не є цією identity. Рівність таких descriptions не merge-ить два Resource, а зміна description сама по собі не змінює Resource identity і не створює Assignment.

### 5.2 Managed consumable stock

Consumable Resource ідентифікує керований запас, партію, контейнер, комплект або іншу облікову одиницю. Абстрактний material kind, окрема фізична частка або значення quantity, mass, volume, charge чи remainder не є Resource.

Наприклад, `Fuel Stock FS-001` може бути Resource, а `120 l` — лише зовнішня вимірювана характеристика. Зміна кількості сама по собі не змінює identity запасу. Reservation, consumption, capacity, unit-of-measure і списання лишаються поза цим контрактом.

Ці правила є частиною normative kernel незалежно від того, які illustrative labels наведені в §14.

## 6. Roles, participation and Assignment

Resource не має сталої операційної ролі. Exact Assignment за OCP-005 є єдиним поточним Core owner участі Resource в Operation і його ролі у відповідному контексті.

```text
Resource + exact Assignment + Operation context = contextual operational role
```

Один Resource може мати різні Assignment до різних Operation. Допустимість одночасних Assignment визначають лише застосовні exact Constraint та окремі accepted contracts.

Organization membership, classification, composition, Capability claim, availability або готовність не створюють Assignment чи participation. OCP-003 не визначає прямий авторитетний зв’язок `Resource participates_in Operation`; derivation належить OCP-005.

## 7. Component identity and non-inheritance

Якщо component моделюється як окремий Resource, він зберігає identity, відмінну від identity composite Resource. Composite Assignment не створює Assignment або participation для component автоматично.

Цей kernel не визначає record shape, directionality, effectivity, cycle rules або authority для `contains`, `part_of` чи іншої composition relation. Він визначає лише identity та non-inheritance гарантії, що мають зберігатися в будь-якому майбутньому relation contract.

Organization membership і Resource composition не створюють Capability claim inheritance, aggregation або transitive possession.

## 8. Capability, Constraint and interchangeability boundaries

Capability definition та holder-specific proposition є різними шарами. OCP-012 CapabilityClaimRecord:

- exact-bind-ить одного holder типу Resource;
- exact-bind-ить одну версію OCP-009 Capability; і
- не стає властивістю Resource identity.

Organization не є допустимим direct holder за поточним контрактом. Positive claim не створює Readiness, availability, authorization, admissibility, selection, Assignment або фактичне використання. `Capability ≠ Readiness`.

Resource може бути subject exact Constraint, але Constraint не змінює його identity. OCP-013 interchangeability є directional та consumer-specific: рівні classification values або Capability claims не створюють Resource equality, symmetry, transitivity чи автоматичної заміни. OCP-014 contextual requirement також не надає ranking, selection або replacement authority.

## 9. Organization boundary

`Organization ≠ Resource`. Organization classification, membership, unit label або shared referent не створюють Resource identity і не collapse-ять дві identities.

Статус `Unit`, можливий `Organizational Resource` та exact mapping `Organization ↔ Resource` лишаються відкритими під AB-006 і AB-052. До окремого accepted рішення:

- жоден Organization не проєктується в Resource автоматично;
- Organization membership не створює Assignment, participation або Capability claim; і
- однаковий label чи зовнішній referent не є mapping authority.

## 10. Spatial, temporal and lifecycle non-implications

Operation-local spatial binding за OCP-004 є opaque payload у межах owning Operation. Він не є Resource location, footprint ownership, Resource identity або доказом Assignment.

OCP-003 не визначає general Resource lifecycle stages, transition history, provenance чи authoritative current-state projection. Майбутній exact reference на retired або іншим чином неактивний Resource може лишатися історично точним, але цей документ не визначає, як такий стан встановлюється.

Availability, health, Readiness, current use та location/effectivity потребують окремих exact owners. Жоден timestamp, порядок записів або візуальний lifecycle label не створює їх за implication.

## 11. Semantic rules and authority discipline

1. Resource identity належить одному managed subject на declared granularity; classification не замінює identity.
2. Exact Assignment є єдиним поточним Core owner участі й operational role.
3. Organization membership і Resource composition не створюють Assignment або participation.
4. Capability definition, CapabilityClaimRecord, Constraint і interchangeability result не входять до Resource identity.
5. Positive Capability claim не створює Readiness або будь-який downstream operational verdict.
6. Equal classification або equal claims не роблять Resources рівними чи взаємозамінними.
7. Managed-site identity не дорівнює geometry/environment description.
8. Managed-stock identity не дорівнює material kind або quantity value.
9. Domain classification meaning потребує exact owner/profile та OCP-016 route; occurrence у fixtures чи catalog нічого не admits.
10. Unknown, conflicting або ownerless semantic evidence fails safe без newest/order/count authority.
11. Цей документ не створює Concept dependency, graph edge, schema relation або P-001 invocation; `Concept-Depends-On: []` є визначальною проєкцією.
12. Жоден consumer, checker або example не може розширити цей kernel без окремої governance зміни OCP-003.

## 12. Invariants

### 12.1 Identity and classification invariants

1. Кожен Resource має непорожній стабільний identifier у межах заявленої management granularity.
2. Два різні Resource не мають одного й того самого identifier.
3. Кожен Resource має щонайменше одне непорожнє opaque classification value; OCP-003 не виводить з нього hierarchy, equivalence, role, Capability або Organization mapping.
4. Кожен managed-stock Resource ідентифікує запас, партію, контейнер, комплект або облікову одиницю, а не material kind чи quantity value.
5. Кожен managed-site Resource зберігає identity окремо від geometry, area, route, coverage та environment payload.

### 12.2 Composition invariants

1. Resource не може бути власним окремим component; якщо `A` і `B` моделюються як Resource у composite context, їх identifiers різні.
2. Зв’язок composite/component не створює Assignment або participation component автоматично.
3. Organization membership або Resource composition не створює Capability claim inheritance, aggregation чи transitive possession.

### 12.3 Consumer-preservation invariants

1. Assignment, CapabilityClaimRecord, Constraint, OCP-013 requirement та OCP-014 context exact-bind Resource identity без rebinding через classification.
2. Resource-specific CapabilityClaimRecord holder лишається Resource-only і exact-bind-ить одну OCP-009 Capability version.
3. Directional interchangeability не перетворюється на equality, symmetry, transitivity, ranking або selection.

## Part II — Explicit exclusions and deferred surface

## 13. Exclusions, future owners and reopening gates

Нижченаведені виключення є нормативною межею kernel. Вони зберігають питання видимими, але не надають їм current authority.

| Excluded/deferred surface | Current result | Reopening gate / possible owner |
|---|---|---|
| closed або exhaustive Core Resource subtype taxonomy | не визначена; §14 labels є opaque та illustrative | named domain owner/profile і окремий OCP-016 admission decision |
| Organization / `Organizational Resource` / `Unit` identity чи mapping | не визначені; `Organization ≠ Resource` | окремий AB-006/AB-052 proposal з OCP-007 continuity та legitimate mapping owner |
| authoritative `belongs_to`, `may_be_part_of`, `may_contain` або composition record | record shape, direction, effectivity та authority не визначені | окремий accepted relation contract; non-inheritance invariants §§7/12 зберігаються |
| general `Identified → Registered → Active → Retired` lifecycle | sequence вилучена з normative surface; transition/history/provenance відсутні | fresh post-remediation audit і окремий Board act з exact owner |
| Resource location, availability, health, Readiness та current use | не визначені | окремі exact owners; Readiness/health reopening також під межами AD-011 |
| quantity, reservation, consumption, capacity, unit-of-measure і write-off | не визначені; quantity не є identity | окремий accepted consumable/measurement contract |
| Resource Group identity та bulk Assignment | не визначені | окремий identity verdict і, за потреби, зміна OCP-005 через власний review |
| Organization Capability claims | заборонені current OCP-012 direct-holder contract | окреме holder-expansion рішення після AB-006/AB-052; без inheritance |
| automatic projection, identity collapse, inheritance, aggregation або transitive possession | не допускаються | лише окремий accepted owner може запропонувати точний вузький rule; жодне припущення не успадковується |

Жодна excluded surface не стає дозволеною через відсутність правила. Ownerless або conflicting evidence лишається unresolved. Якщо future work потребує зміни OCP-007, direct consumer, checker, graph або Resource data, воно виходить за межі цієї remediation і має зупинитися.

## Part III — Non-governed working classification catalog

## 14. Illustrative classification values

Цей catalog допомагає людині читати наявні дані. Він **не є normative stable kernel**, не є вичерпним, не визначає hierarchy/equivalence та не допускає labels до Core. Indentation нижче показує лише історичне тематичне групування; вона не є subtype relation:

```text
Resource examples
├── Human Resource: Person, Crew, Duty Team
├── Organizational Resource: Unit
├── Technical Resource: Platform, Equipment, Communication Asset, EW Asset
├── Infrastructure Resource: Position Site, Launch Site, Relay Site
└── Consumable Resource: Fuel Stock, Energy Stock, Other Consumable Stock
```

Правила catalog:

1. Будь-який current label у цьому списку лишається сумісним opaque value за §4.
2. Namespaced value, якого немає у списку, так само валідне, якщо воно непорожнє.
3. Catalog не визначає identity, parent/child hierarchy, equivalence, role, Capability, Organization mapping або interchangeability.
4. `Human Resource`, `Technical Resource`, `Infrastructure Resource` і `Consumable Resource` є читабельними прикладами, а не Canonical Core subtypes.
5. `Organizational Resource` і `Unit` не вирішують AB-006/AB-052 і не створюють Resource з Organization.
6. Domain-specific labels мають значення лише під exact external owner/profile; catalog не є таким owner.
7. Stable site/stock semantics визначені тільки у §5. Catalog не може їх змінити або бути їх єдиним джерелом.

Приклади `Technical Resource`, `Platform`, `Human Resource` та `Infrastructure Resource` у поточних fixtures не доводять semantic admission. Приклад `example.resource-class://specialized-asset@1` навмисно відсутній у catalog і демонструє opacity, а не новий доменний стандарт.

## 15. Selected RS scenarios and counterexamples

Цей evidence appendix не розширює §§1–14. Він робить selected AD-018A results читабельними без звернення до історії PR.

### 15.1 Scenario results

| Scenario | Result under this contract |
|---|---|
| two equally classified assets | це два distinct Resource; label equality нічого не merge-ить |
| one crew in two Operations | потрібні два exact Assignment; classification не визначає роль |
| composite and component | identities distinct; relation representation deferred |
| composite assigned, component not | Assignment/participation не успадковуються |
| managed site and equal geometry | site Resource зберігається; payload є окремим description |
| fuel stock quantity changes | той самий managed-stock Resource, якщо окремий owner не визначив інше; quantity не є identity |
| battalion without mapping | Organization лишається exact; Organizational Resource не виникає |
| unknown domain classification | непорожнє opaque value валідне; Core не тлумачить hierarchy/equivalence |
| equal positive claims | Resource identities distinct; exact directional requirement вирішує eligibility |
| future retired Resource | historical exact references можуть зберігатися; lifecycle authority тут відсутня |
| current `Technical Resource` fixture | валідна як opaque value, не Canonical subtype |
| Organization `unit@1` fixture | це лише Organization classification evidence, не Resource mapping |

### 15.2 Rejected counterexamples

1. Fixture frequency не Canonicalize-ить subtype.
2. Checker acceptance не визначає semantic meaning label.
3. Equal classifications не створюють equality або interchangeability.
4. Equal claims не створюють replacement authority.
5. Organization membership не створює participation.
6. Composition не успадковує Assignment.
7. Organization `Unit` classification не створює Resource identity.
8. Informal `belongs_to` prose не створює graph edge чи mapping.
9. Label `Active` не створює availability, Readiness або authorization.
10. Geometry не стає managed-site identity.
11. Quantity не стає Resource і сама по собі не змінює identity.
12. Винесення catalog за межі kernel не може відкинути stable site/stock rules §5.
13. Один файл не робить усі його секції однаково нормативними.
14. Extraction сама по собі не створює legitimate ownership.
15. Timestamp, record order, source/issuer count або majority не вибирають meaning.
16. OCP-003 не успадковує P-001 invocation.
17. Resource remediation не promote-ить consumers.
18. Acceptance AD-018/AD-018A не реалізує lifecycle і не авторизує `1.0.0`.

## 16. Exact remediation baseline and executable evidence

Remediation починається з `main@db13ba706f51986987767ab250d3fa7441eec738`, tree `b4436e7aea34d7cd26354e679a1f2d87b5f82c37`. Hashes ідентифікують exact reviewed bytes; recency або hash equality не визначають semantic authority.

| Input | Baseline state | Git object | SHA-256 |
|---|---|---|---|
| AD-018 | `0.2.0 / Accepted` | `e4aa8d261587e393e9da87663e3c247a3cb0518c` | `ac39ff8848c78380513ddf1a76412ce58272c41cef4525b7e45d906b86fd95e7` |
| OCP-003 | `0.6.1 / Draft`; Resource `Accepted` | `721cad97a05970b6a089668040faeddd968cfe46` | `a90f651aa81f3f70f316566580d05aeca3be3359b33342ffdb0eb1d579526fbd` |
| OCP-007 | `0.3.2 / Draft`; Organization `Accepted` | `543d579f9ce1033ff38d478d1663c71a10b5f118` | `93fdf3e2e71e844888306b22da4f46468418ed30f3a2a62b8a39a98e7c6b387b` |
| OCP-004 | `0.8.2 / Draft` | `f95acdec469baa8c44885853c055ad2fa326ac57` | `de9e786759af436c71a7cd56ed834f27e3b52cb1f479dd56d9164a8babfd5b2e` |
| OCP-005 | `0.2.2 / Draft` | `f50daff2f69898264f5a166c919f1299050ff456` | `aa39c06ed076cfd8e6efd4f7f5a4547f3f579fb3d608667ebc05c0d7dabbcf74` |
| OCP-006 | `0.2.2 / Draft` | `5ae9245740b82e981880563287b3986574df4bfb` | `dc8b3249c9c4d1b003b9cd8132430c2145be3cf5d566ba9e0d154a23056d68cc` |
| OCP-012 | `0.3.0 / Accepted` | `cd2df0f1961b6d03eea0db66c8fdfce1f97cb235` | `d4d5b4441cf2d1f7fea2dae572fcfa60f22b0ebce0e23ae6a86f71d9f4edd122` |
| OCP-013 | `0.2.0 / Accepted` | `658a291b4c3b9a0229aba09d485c1137723fe70b` | `a20659422f847f49a9231b8c1d1dabc0d8b911d9667c44013280b1826f621a74` |
| OCP-014 | `0.2.0 / Accepted` | `23bd05b4bb14fd7a85101bd5a8b3dd733b53dd99` | `72c789c7b15ab2fd8997f60ba8cfd9d89f0e7730407763d18fb222bac5f06a8c` |
| Resource validator | three structural rules | `03586af0f94187b4e620076b3a29348025f26e40` | `45f68314e2b66b54facc786f0fb976d3ec98871400fbbb7a210808d86082db96` |
| existing Resource fixture | `resource-valid-001` | `765d8d898750ca1fa277d3cdbe0d0102ac2ecb97` | `a6e659a7c7d4ead2bbb378c26231172b267d994265bd82e1ba573a5661e46f16` |
| complete baseline fixture set | 117 files, including every current classification carrier | tree `3b2ffcccd42a2dd8e4053f9eb74f1e3c82ff1812` | recursive `git ls-tree` manifest `3b562f5ee8a1176eb03a67d2e296f466c737bf88ef754fc6617a960b35363116` |

OCP-007, all six direct consumers, registry/taxonomy projections, Concept graph, rules manifest and checker code remain byte-unchanged by this proposal.

The fixture delta is exactly two synthetic non-sensitive files:

| Fixture | Git blob | SHA-256 | Required result |
|---|---|---|---|
| `resource/valid-opaque-namespaced-classification.yaml` | `9b74656b4104e7231575e88d2ac79f1e6e5fbd50` | `5232dc8b57f58d5190fba0577fc38a2f86ce636f8534d1537200154c5956b192` | valid; proves a non-§14 namespaced value is accepted as opaque |
| `resource/invalid-missing-classification.yaml` | `ef6ee1a34f3ebfb98d94f8170be43165cac767b8` | `252d7016e98a81e2f1bc42db46e723ac5374ee484c93e9deda0b3f321ad7d86a` | invalid with exactly `RESOURCE_CLASSIFICATION_REQUIRED` |

The existing fixture plus these two cases witness only §12.1 invariants 1 and 3 and the current self-containment check. They do not prove taxonomy membership, domain meaning, lifecycle, Organization mapping або relation authority.

## 17. OCP-003 `0.6.1 → 0.7.0` relocation ledger

Кожен рядок AD-018 §6 має один явний disposition:

| Prior OCP-003 surface | K/B/S/C disposition | `0.7.0` location and result |
|---|---|---|
| §§1–4 definition, purpose, scope, identity | K retained; belonging/availability wording C-qualified | §§1–4; identity is normative, while participation/availability/mapping are assigned to exact external owners or excluded |
| §5 working taxonomy | S → working catalog | §14 only; non-exhaustive opaque examples outside stable promise |
| §5.1 Human Resource | S → working catalog | §14 illustrative labels; person/group identity remains generically covered by §§1/3 |
| §5.2 Organizational Resource | B → exclusion/catalog | §13 mapping exclusion + §14 illustrative unresolved labels; AB-006/AB-052 remain open |
| §5.3 Technical Resource | C → working catalog | §14; old claim that types “belong to Capability” removed, classification and Capability are separated in §§4/8 |
| §5.4 Infrastructure Resource | K moved; S catalog labels | normative managed-site semantics moved to §5.1; labels remain only in §14 |
| §5.5 Consumable Resource | K moved; quantity S | normative managed-stock semantics moved to §5.2; labels remain §14; quantity model excluded §13 |
| §6 Assignment boundary | K retained; status prose C-cleaned | §6 exact Assignment ownership and non-inheritance |
| §7 structural relation labels | B/S → exclusion | code-like unowned relation assertions removed; §7 preserves only identity/non-inheritance, §13 defers record authority |
| §7 Capability/Constraint boundary | K retained | §8 exact Resource-only OCP-012 holder, exact OCP-009 binding and non-implications |
| §7 spatial/temporal boundary | K/S split | §5.1 and §10 preserve payload non-identity; §13 excludes location/effectivity authority |
| §8 composition | K non-implications; B/S representation | §§7/12 preserve separate identity and no Assignment inheritance; §13 defers relation contract |
| §9 lifecycle | B/S → exclusion | sequence removed; §10/§13 state no lifecycle authority and require fresh audit + Board act |
| §§10–12 rules and invariants | K retained; classification B resolved narrowly | §§11–12; non-empty opaque value is Resource-local invariant, specialized meaning external |
| §§13–14 examples/non-examples | C → evidence | selected results appear in §15 without creating catalog/taxonomy authority |
| §§15–16 open/deferred questions | S → explicit exclusions | §13 assigns reopening gates without resolving any deferred model |
| §17 PATCH history | C → historical record | §20; exact `0.6.1` effect preserved as history only |

This ledger leaves no normative Resource statement inside §14. Stable site/stock wording exists in §5 before the catalog is marked non-governed. Any ambiguous residue is a stop condition under §19.

## 18. Compatibility and future version handling

Revision `0.7.0` is a MINOR Draft remediation. It does **not** claim that OCP-003 or Resource is lifecycle-ready for `1.0.0`; Resource remains `Accepted`, document status remains `Draft`.

If a later Board act establishes a `1.x` stable surface:

- **PATCH** may correct wording or references without changing a guarantee, exclusion, owner, invariant or accepted opaque value;
- **MINOR** may add a backward-compatible guarantee or clarification only when it does not reinterpret existing identity/classification values, import an excluded authority or require consumer rebinding; and
- **MAJOR** is required to remove or weaken a stable guarantee, reinterpret an accepted identity/classification contract, change Resource granularity incompatibly or admit a previously excluded authority in a breaking way.

Adding a domain label under its own exact owner does not by itself version OCP-003. Changing that label’s external semantics follows the owner/profile contract and cannot silently alter Resource identity.

Completion of this remediation triggers a fresh blocker/stability audit. Only a separate reviewed Board act may decide whether any OCP-003 `1.0.0` proposal is admissible.

## 19. Migration, rollback and stop rules

No Resource data or consumer reference requires migration:

- every `resource_id` and existing classification string remains valid;
- Assignment, CapabilityClaimRecord, Constraint, OCP-013 and OCP-014 bindings remain exact;
- no Organization mapping, lifecycle history or domain meaning is synthesized; and
- no consumer, checker, schema, registry projection, Concept dependency or graph edge changes.

Atomic rollback reverts this OCP-003 revision, both §16 synthetic fixtures and their fixture-count/accounting projections as one unit. Rollback does not delete or merge Resource identities, rebind consumers, reinterpret labels or restore unowned mapping/lifecycle prose.

The remediation stops and returns to R0/Architecture Board rather than widening itself if review discovers:

1. a seventh direct normative consumer or changed consumer requirement;
2. a dependency on closed taxonomy membership or `Unit` mapping;
3. a need to edit OCP-007 or any OCP-004/005/006/012/013/014 consumer;
4. a need to change checker code, schema, Concept dependency or graph edge;
5. incomplete relocation of stable site/stock semantics;
6. two plausible defining Resource surfaces inside this file;
7. lifecycle, composition, classification or mapping authority that must be selected rather than excluded; або
8. data/reference migration beyond opaque-label replay.

## 20. Version history

### `0.7.0` — stable-kernel remediation proposal

Implements the exact AD-018A RS contract inside one defining OCP: normative stable kernel, explicit exclusions and non-governed working catalog. It adds exactly two bounded Resource fixtures and changes no Concept status, dependency, graph edge, Pattern invocation, consumer contract or checker code.

### `0.6.1` — volatile status PATCH

Corrected only the then-current Capability status rendering in former §7. It did not change definition, identity, working taxonomy, dependencies, Concept status, graph edges or P-001 invocation. The exact baseline bytes remain anchored in §16; superseded wording is historical evidence, not a second current authority.
