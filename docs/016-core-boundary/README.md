---
Document-ID: OCP-016
Title: Core Boundary Admission and Extension Contract
Version: 0.1.0
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000, AD-015
Used-By: All Core admission, extension, domain-envelope and semantic route reviews
Last-Review: 2026-08-05
Review-After: External adversarial review and Architecture Board acceptance
---

# OCP-016 — Core Boundary Admission and Extension Contract

## 1. Людське пояснення

Цей контракт допомагає людині відповісти на два різні питання:

1. **Хто повинен володіти значенням semantic candidate?**
2. **У якому governed artifact це значення має жити?**

Часто однакове поле, record shape або назва з’являється в кількох продуктах. Це ще не робить їх спільним Core поняттям. І навпаки, результат `not Core` не означає, що domain contract або implementation є помилковим.

OCP-016 маршрутизує proposal до найменшого легітимного semantic owner. Він не оцінює важливість за score, не приймає candidate і не замінює Architecture Board act.

Наприклад, opaque weather profile може лишатися domain-owned, тоді як Core володіє лише exact profile/version binding і ambiguity rejection. Такий envelope не отримує authority тлумачити weather semantics. Якщо ж два незалежні consumers потребують одного стабільного subject, proposal окремо доводить Core identity — сама наявність profile цього не робить.

## 2. Мандат і стан Draft

[AD-015B §§33–40](../../architecture/discovery/AD-015-core-boundary-specification.md) прийняв C3 (`G2 × H2`): tiered semantic-authority routing у окремому human-readable OCP. Він також встановив:

- один primary semantic-authority route для кожного semantic candidate;
- Pattern як окремий optional form route;
- G3 domain-first і G4 consumer activation як conditional obligations усередині G2;
- OCP-001 як owner автоматичного trigger і review process;
- Architecture Board act як єдине джерело admission та status change; і
- baseline без admission registry, numeric score, P-002 або mandatory checker projection.

Revision `0.1.0` реалізує цей мандат як Draft для зовнішнього adversarial review. Вона не reclassify-ить наявні artifacts, не створює Concept, dependency, Pattern, registry чи machine authority.

## 3. Визначені терміни

**candidate object** — точний subject, record, value, rule, profile, envelope, form або implementation structure, для якого proposal просить governed placement чи authority.

**semantic candidate** — candidate subject, record, value, rule, profile, envelope або implementation structure, для якого треба визначити semantic owner.

**Pattern form candidate** — proposal reusable modeling obligations без власної domain semantics; він отримує окремий form verdict, а не удаваний semantic owner.

**semantic authority** — легітимне право exact owner визначати один конкретний вид identity, meaning, invariant, input, rule, result або lifecycle.

**primary semantic-authority route** — єдине місце, де живе значення semantic candidate: fundamental Core, Core non-Concept, Core envelope, domain-local або implementation-local.

**Pattern form route** — окреме exact-version invocation reusable modeling form. Воно не є semantic route і не змінює domain owner.

**Core semantics** — identity, meaning, invariants або results, які Foundation прямо бере на себе для незалежного reuse кількома accepted consumers.

**Core envelope** — мінімальний shared contract для exact references, profiles, snapshots і fail-safe interoperability; specialized meaning лишається у named domain owner.

**domain-local semantics** — exact namespaced meaning і lifecycle, якими володіє named domain без заяви про universal Core equivalence.

**implementation-local structure** — storage, API, UI, transport або computation shape, що реалізує accepted semantics, але сам не є нормативним semantic artifact.

**admission** — явний Architecture Board act, який приймає exact reviewed scope, artifact і status. Routing result не є admission.

## 4. Застосування після OCP-001 trigger

[OCP-001 § «Обов’язковий Core Boundary review»](../001-ontology-governance/README.md) є єдиним defining location для автоматичного trigger і review-хореографії. Після trigger цей OCP застосовується повністю й автоматично; optional invocation не потрібна.

Перед routing proposal повинен окремо назвати кожен requested object:

- fundamental Concept;
- Concept dependency;
- identified record;
- local structured value;
- Pattern form;
- rule або result vocabulary;
- domain profile;
- interoperability envelope; або
- implementation structure.

Якщо один PR містить кілька semantic candidates, кожен отримує власний primary routing result та authority ledger. Pattern form candidate отримує окремий form verdict за §7. Useful reference не стає dependency, record не стає Concept, а Pattern-shaped object не стає Pattern лише через схожу форму.

## 5. Primary semantic-authority routes

### 5.1 Route F — fundamental Core Concept або dependency

Route F застосовується лише тоді, коли proposal доводить stable subject identity або identity/invariant dependency незалежно від representation, report, caller чи одного consumer.

Concept proposal проходить повний OCP-001 identity test. Dependency proposal окремо доводить, що source Concept не може зберігати свою accepted identity або invariants без target. Mention, data reference, useful lookup, process sequence чи shared deployment недостатні.

Route F потребує окремого Board act і atomic Concept registry, OCP-002, defining-document metadata та generated-map update. Він не є default для records, relationships, assessments, statuses або taxonomy categories.

### 5.2 Route C — Core non-Concept contract

Route C застосовується, коли Foundation легітимно володіє shared semantics, але candidate не має fundamental Concept identity.

До route можуть належати:

- identified attributable record;
- Core rule або finite result vocabulary;
- exact consumer activation;
- local structured value всередині owning Core Concept; або
- інший governed non-Concept contract.

Route C не є “Concept later”. Record history не доводить Concept identity, local value не створює reusable subject, а consumer-local result не стає global policy.

### 5.3 Route E — Core interoperability envelope

Route E застосовується, коли named domain зберігає specialized meaning, а concrete accepted consumer потребує мінімальних shared guarantees для exchange.

Core може володіти лише exact namespace/profile/version binding, reference resolution, immutable snapshot binding і fail-safe handling unknown, duplicate, ambiguous або incomparable input. Domain owner володіє vocabulary, interpretation і domain truth.

Envelope не перекладає profiles за label similarity, не вибирає newest version, не імпортує domain model у Core і не створює cross-profile equivalence без окремого exact contract.

### 5.4 Route D — governed domain-local contract

Route D застосовується, коли named domain має legitimate owner і exact contract, але concrete cross-domain consumer або shared Core responsibility не доведені.

Domain-local є валідним governed результатом. Foundation може exact-reference domain artifact, не приймаючи його vocabulary як universal Core meaning. Однакові labels або shapes у двох domains не створюють equivalence.

Якщо пізніше з’являється concrete interoperability consumer, proposal може просити Route E. Якщо з’являється independently reusable Core identity чи meaning, він проходить Route F або C; popularity та deployment count недостатні.

### 5.5 Route I — implementation-local structure

Route I застосовується, коли candidate описує table, API, UI field, cache, message, storage layout, transport envelope або computation detail, а accepted shared semantics уже визначені іншим artifact чи не доведені взагалі.

Implementation може бути повторно використаним і критичним для продукту, але reuse, central deployment або shared database не створює ontology authority. Route I не означає низьку якість і не забороняє product validation.

## 6. Неперекривність primary routes

Для одного semantic candidate proposal обирає рівно один primary route.

| Якщо Core володіє… | Primary route | Що Core не отримує автоматично |
|---|---|---|
| independent subject identity або identity/invariant dependency | F | authority над кожною domain specialization |
| shared non-Concept meaning, rule, result чи local-value contract | C | fundamental Concept identity або global activation |
| лише exact interoperability guarantees | E | domain vocabulary, truth або profile equivalence |
| нічим; named domain володіє meaning | D | universal Core semantics |
| нічим; software володіє representation | I | semantic admission через implementation reuse |

Якщо proposal одночасно стверджує, що Core володіє full meaning і лише envelope, Routes C та E конфліктують. Якщо domain і Core обидва названі defining owner одного rule/result, Routes C та D конфліктують. Якщо representation оголошено normative source, Routes I та будь-який semantic route конфліктують.

Конфлікт не вирішується precedence, score чи best effort. Proposal лишається Discovery, доки owner і scope не стануть однозначними.

## 7. Orthogonal Pattern form route

Після primary routing candidate у Route C, E або D може exact-invoke Accepted Pattern, якщо повторювана form потрібна незалежно від domain meaning.

`Uses-Patterns: P-NNN@x.y.z` імпортує лише Required Elements і explicitly selected modules чинної Pattern version за OCP-001 policy. Pattern не володіє candidate identity, vocabulary, truth, authority, result або admission status.

Route F Concept не отримує identity від Pattern. Route I implementation не може послатися на Pattern, щоб перетворити storage shape на normative record. Structural similarity не є invocation.

Якщо proposal створює сам Pattern, reusable form є Pattern form candidate, а не шостим semantic route. Proposal повинен показати щонайменше два незалежні prospective або current invoker contexts, явно назвати semantic route кожного invoker і довести, що спільними є саме form obligations, а не vocabulary чи truth. Відсутність semantic object у Pattern artifact не звільняє його від external review та Board act, але Pattern не вигадує primary semantic owner для себе.

Mandatory Core Boundary review ніколи не реалізується через optional Pattern. Новий reusable admission-evidence Pattern потребував би окремого reopening H3/P-002; цей Draft його не створює.

## 8. Authority ledger

Кожен positive proposal подає читабельний ledger, а не machine score:

| Питання | Обов’язкова відповідь |
|---|---|
| Candidate | який exact object розглядається і яким object class він є? |
| Responsibility | яку реальну operational responsibility він несе незалежно від software representation? |
| Primary route | F, C, E, D або I; чому сусідні routes не підходять? |
| Semantic owner | хто легітимно володіє exact identity, meaning, rule, result або lifecycle? |
| Consumers | які concrete accepted consumers потребують заявлених shared guarantees? |
| Defining source | який human-readable artifact і exact version визначає semantics? |
| Dependencies | які exact Concepts, OCP, Pattern, AD або domain profiles потрібні прямо? |
| Evidence | які human examples та mechanically expressible counterexamples підтримують scope? |
| Non-implications | чого proposal явно не встановлює щодо identity, truth, Readiness, authorization, selection та Assignment? |
| Lifecycle | як працюють versioning, reopening, migration, retirement і historical references? |

Ledger може бути section у candidate AD/OCP або PR description. OCP-016 не вводить для нього schema, registry identity чи stored approval record. Відсутній або суперечливий ledger не дає permissive routing result.

## 9. G3 domain-first obligation

Specialized semantics за замовчуванням лишаються Route D, доки proposal не назве concrete consumer та не доведе мінімальний Route E envelope або independently shared Route F/C responsibility.

Для Route E обов’язкові exact namespace/profile/version/owner binding та rejection zero/multiple/unknown/incomparable resolution. Domain fixture може перевіряти private details поза Foundation, але Core guarantee має мати non-sensitive synthetic witness.

Domain-first не є permanent fragmentation rule. New evidence може відкрити route movement, але не переписує historical authority і не створює equivalence заднім числом.

## 10. G4 consumer-activation obligation

Positive-capable rule, result vocabulary або profile activation exact-bind-иться до одного accepted consumer, baseline contract, rule version, input snapshot, evaluation context і legitimate evaluator/owner.

Одна activation не успадковується іншими consumers, не змінює baseline semantics і не створює global lifetime, authority чи policy. Matching label або result shape не є portability contract.

Missing consumer, unresolved rule, stale/missing snapshot, ambiguous input або невизначений evaluator робить positive path non-permissive. Newest rule, current wall clock, caller identity чи majority не підставляються.

## 11. Routing і Architecture Board decision

Routing визначає лише належний semantic owner і required evidence. Він не встановлює, що evidence істинне або owner легітимний.

Positive admission потребує:

1. human-readable candidate contract;
2. complete authority ledger;
3. exact dependencies і version bindings;
4. external adversarial review;
5. outcome-appropriate human evidence та executable evidence для кожного mechanically expressible obligation;
6. explicit Architecture Board act; і
7. atomic accounting та generated-projection update, якщо вони змінюються.

Candidate contract не може declare себе Accepted. OCP-016 не створює status. Checker або registry може лише перевірити finite rule, який exact-resolve-иться до human defining source.

## 12. Accepted precedent routing

| Accepted evidence | Route | Пояснення |
|---|---|---|
| Resource, Operation, Assignment, Constraint, Organization, Objective, Capability, Event | F | окремо доведені independent identity та responsibility |
| Organization relationships, observations, assessments, Capability claims, coordination proposals/responses | C | identified records із власною attribution/history без fundamental Concept identity |
| P-001 | Pattern form verdict | reusable form лише після exact invocation; кожен invoker зберігає власний semantic route |
| Capability namespaces | E для Core envelope; D для specialized profile | це окремі candidates: Core exact-resolution envelope не імпортує domain meaning |
| OCP-011/OCP-012 activations | C + G4 | exact consumer-local rules без global inheritance |
| Result negative identity verdict | C | realized outcome представлено governed assessment record, не fundamental Result |
| State і Readiness negative current-scope verdicts | D або I для exact local candidate; later shared proposal потребує reopening | exact local sources можуть лишатися valid без shared Core authority |
| Operational Area і Environment | C для Operation-local value; D для exact domain input | це окремі candidates: local binding не створює reusable area subject; Environment не є Concept |
| visibility та agreement no-new-authority controls | D або I для exact current candidate; later shared proposal потребує reopening | shared authority відсутня без concrete consumer і legitimate owners |
| checker і manifests | I | executable reference реалізує exact OCP rules і не створює semantics |

Таблиця є precedent guide, а не автоматична reclassification. Новий proposal усе одно подає власні evidence та Board act.

## 13. Mandatory counterexamples

| # | Pressure case | Required routing behavior |
|---:|---|---|
| 1 | однакове UI field у трьох products | Route I; reuse не є Core evidence |
| 2 | несумісні domain labels `ready` | Route D для exact contracts; немає shared Readiness authority |
| 3 | одна record shape, різні assertions | semantic routes лишаються окремими; shared Pattern form не зливає meaning |
| 4 | legitimate domain owner, але немає cross-domain consumer | Route D; відсутність Route E не робить domain invalid |
| 5 | два accepted consumers потребують exact shared identity/version | окремо перевірити Route F, C або E за object class та authority scope |
| 6 | taxonomy category прийнято за Concept | відхилити Route F без independent identity evidence |
| 7 | identified record прийнято за Concept через history | Route C або D; history не створює fundamental identity |
| 8 | repeated record form копіюється | semantic route зберігається; applicable Accepted Pattern exact-invokes окремо |
| 9 | Pattern smuggles domain result vocabulary | reject transfer; vocabulary лишається у Route C/D defining contract |
| 10 | checker rule не має normative source/owner | Route I implementation invalid проти governance; checker не створює owner |
| 11 | shared database table вважають shared identity | Route I; storage не є semantic evidence |
| 12 | unknown/duplicate profile перекладають best effort | Route E rejects zero/multiple/unknown resolution |
| 13 | newer profile обирають без exact caller binding | reject; exact version only, never newest |
| 14 | domain specialization змінює Core parent identity/invariant | reject або explicit reopening Route F/C; specialization не override-ить baseline |
| 15 | proposal суперечить accepted negative verdict | stop і explicit reopening з new evidence |
| 16 | equal local spatial payloads стають reusable area identity | лишаються Route C local values; equality не створює Route F |
| 17 | positive Capability claim стає availability/auth/Readiness | reject non-implication; OCP-012 attribution не переносить authority |
| 18 | generic assessment extension розмиває target/result/evidence owner | окремий Route C/D contract або reopening; shape reuse недостатньо |
| 19 | admission доказується лише sensitive data | positive Core guarantee не приймається без non-sensitive synthetic witness |
| 20 | machine registry каже `approved`, Board act відсутній | registry non-authoritative; admission відсутній |
| 21 | newest/order/issuer/source/deployment count обирає authority | reject для всіх routes |
| 22 | domain contract відхиляють лише тому, що він не Core | Route D є валідним governed outcome; `not Core ≠ invalid` |

## 14. Evidence і executable boundary

Human review встановлює operational responsibility, legitimate owner, consumer need, semantic non-overlap і достатність reopening evidence. Ці judgments не делегуються checker.

Executable evidence потрібне лише там, де obligation уже має finite representation. Чинний repository checker може перевіряти:

- uniqueness і path correspondence primary OCP/Pattern/AD/ADR/AB identifiers;
- exact-resolvable, non-duplicate `Depends-On` metadata;
- OCP, Pattern, AD, ADR та AB lifecycle values;
- Concept status/dependency projections;
- exact `Uses-Patterns` version binding; і
- rule-manifest identifier uniqueness та exact OCP source binding.

Додавання OCP-016 автоматично входить у ці existing checks. Це structural evidence існування та exact references документа, а не доказ правильного route чи Board approval.

Revision `0.1.0` навмисно не додає admission registry, numeric score, route field, schema, new checker rule або fixture. Якщо implementation потребує structured authority fields чи mandatory projection, робота зупиняється і повертається до AD-015 C4/H4/H5 reopening. Такий layer не додається “для зручності”.

Foundation examples використовують лише synthetic identities та opaque values. Sensitive operational data не потрібні й не можуть бути єдиним доказом shared Core guarantee.

## 15. Route movement і historical preservation

Route movement є новим reviewed decision від exact baseline:

- I → D потребує named domain owner і defining contract;
- D → E потребує concrete interoperability consumer та exact ambiguity contract;
- D/E → C потребує доказу, що Core володіє meaning, а не лише transport;
- C/D/E → F потребує full independent-identity/dependency test;
- Core → D, retired або deregistered потребує Board act та atomic cleanup normative/generated projections.

Movement не змінює authority historical versions. Existing exact references лишаються interpretable або отримують explicit migration. Equal payload, label, shape чи storage не merge-ить identities.

Accepted negative verdict contradict-иться лише через explicit reopening з new evidence. Відсутність evidence зберігає попередній boundary; вона не обирає permissive destination.

## 16. Atomic migration

Якщо decision змінює Concept status, dependency, registry membership, taxonomy presentation, Pattern invocation або generated projection, усі authoritative representations оновлюються в одному reviewed PR до merge.

Temporary dual authority заборонена. Не можна лишити старий Concept marker і водночас назвати candidate domain-local; не можна мати дві current rule sources; не можна додати generated row до human Board act.

Historical review records та exact superseded versions не переписуються. Migration record пояснює, що стало current, що лишається historical і які consumers повинні exact-rebind.

## 17. Explicit non-implications

Жоден routing або admission result сам по собі не встановлює:

- domain truth чи objective correctness;
- equality або interchangeability Resources;
- Readiness, availability, capacity, suitability чи admissibility;
- authorization, permission, approval, selection чи ranking;
- reservation, allocation або Assignment mutation;
- inheritance, aggregation або transitive possession;
- equivalence між domain profiles; або
- production validation чи actor authentication.

Такі conclusions потребують окремого exact owner, consumer, rule, evidence snapshot і Board mandate.

## 18. Review checklist

Reviewer повинен мати змогу відповісти `yes` на всі питання:

1. Candidate objects названі до artifact selection і semantic candidates відокремлені від Pattern form proposals?
2. Кожен semantic candidate має рівно один primary semantic-authority route?
3. Pattern form verdict, creation або invocation, якщо є, exact-versioned і не переносить domain semantics?
4. Core semantics, envelope, domain та implementation owners не перекриваються?
5. Усі positive guarantees мають legitimate owner і concrete consumers?
6. Exact versions, dependencies, profiles, rules та snapshots fail safe?
7. Accepted negative verdict або route movement має explicit reopening evidence?
8. Domain-local outcome не трактовано як invalid?
9. Human-readable Board act лишається єдиним admission/status authority?
10. Machine evidence обмежене finite structural obligations?
11. Non-implications і forbidden authority shortcuts явні?
12. Migration та generated projections атомарні, якщо applicable?
13. Приклади synthetic і достатні без sensitive data?

Одна відповідь `no` або `unknown` блокує positive admission. Checklist не має total score: дванадцять інших `yes` не компенсують один unresolved authority gap.

## 19. Draft effect і наступний акт

Revision `0.1.0 / Draft`:

- реалізує AD-015B C3 як human-readable routing proposal;
- визначає Routes F/C/E/D/I та orthogonal Pattern form route;
- зберігає G3/G4 safeguards, Board authority і no-projection baseline;
- покриває accepted precedents та всі двадцять два mandatory counterexamples; і
- додає лише primary OCP artifact, який перевіряється existing structural checker.

Вона не створює Concept, dependency, Pattern, P-002, schema, registry, score, checker rule, fixture чи graph edge.

Після exact-head external review окремий acceptance act може опублікувати reviewed contract як OCP-016 `0.2.0 / Accepted`, узгодити OCP-001 lifecycle wording і перевести AB-061 `Planned → Resolved`. До такого act цей документ лишається Draft і не може бути джерелом admission для іншого candidate.
