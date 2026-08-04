---
Document-ID: OCP-009
Title: Capability Concept
Version: 0.1.1
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, AD-005
Used-By: Capability Registry, Resource Claim Model, Operation Requirements, Interchangeability Decision
Defines-Concepts: Capability
Concept-Depends-On: []
Concept-Status: Under Review
Last-Review: 2026-08-04
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

## 17. Open Questions

- Який identified record та Pattern invocation використовуватиме holder-specific Capability claim?
- Який normative owner визначить Operation Capability requirements?
- Чи потрібна окрема domain policy для заборони нових references на superseded versions?
- Як AB-011 використовуватиме exact claims і Constraint results без втрати Resource identity?
