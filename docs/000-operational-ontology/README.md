---
Document-ID: OCP-000
Title: Operational Ontology
Version: 1.6.0
Status: Canonical
Owner: Architecture Board
Depends-On: ADR-000
Used-By: Product Vision, Domain Model, Business Rules, Architecture, API, UI
Last-Review: 2026-08-13
---

# Operational Ontology

## Преамбула

> Ми не проєктуємо програму. Ми формалізуємо операційну модель реального світу, яку програма лише реалізує.

## Призначення

Operational Ontology є канонічним людськочитаним реєстром фундаментальних Concept OCP: він фіксує активне ім’я, lifecycle status і посилання на defining specification або рішення.

Онтологія описує реальний операційний світ, а не таблиці бази даних, API, екрани або конкретні технології.

Термін стає канонічним лише після проходження життєвого циклу, визначеного в OCP-001. Сам факт згадування в цьому документі не надає статусу Accepted або Canonical.

## Власник реєстру та межі повноважень

OCP-000 володіє лише membership активного Concept registry та зафіксованим status value кожного рядка. Суміжні повноваження залишаються розділеними:

- OCP-001 визначає lifecycle, status choreography, canonicalization і versioning rules;
- OCP-002 є синхронізованою taxonomy projection, а не другим реєстром;
- defining OCP володіє identity, responsibility, invariants, exclusions і dependencies конкретного Concept;
- Accepted AD або ADR володіє рішенням і reopening gates, на які посилається рядок;
- non-Concept records, rules, profiles і Patterns мають власні defining artifacts; їхня згадка тут не робить їх Concept; і
- Foundation map є generated projection і не може змінити registry status або створити dependency.

Якщо OCP-000, OCP-002, defining document або generated projection суперечать одне одному, mismatch є governance defect. Жоден споживач не має права вибрати найновіше, перше або найзручніше представлення.

## Сумісність `1.x`

OCP-000 `1.x` гарантує:

1. один активний registry row та унікальне ім’я для кожного candidate або визначеного фундаментального Concept;
2. явний lifecycle status кожного активного рядка;
3. одне defining specification/decision reference після positive identity act;
4. незалежність document status від Concept status;
5. атомарну синхронізацію OCP-000, OCP-002 і defining document під час Concept status change;
6. відсутність Concept identity, dependency або authority через саму згадку, порядок рядків чи однакову назву; і
7. збереження negative identity verdict та deregistration history до явного accepted reopening act.

`Canonical` для OCP-000 означає стабільність цієї registry-моделі, а не завершеність усієї онтології. Реєстр може одночасно містити `Proposed`, `Under Review`, `Accepted`, `Canonical`, `Deferred`, `Deprecated` або `Archived` Concept rows відповідно до OCP-001. Document status OCP-000 не передається жодному рядку.

Після `1.0.0` застосовується така SemVer-інтерпретація разом з OCP-001:

- PATCH виправляє редакційний текст або посилання без зміни membership, status, identity чи registry rule;
- MINOR додає сумісний candidate/Concept, виконує окремо схвалений status transition, deregister-ить лише pre-acceptance candidate після negative verdict або додає сумісне registry rule;
- MAJOR несумісно змінює registry authority/status meaning, фундаментальний принцип або identity/name/responsibility уже Canonical Concept, а також видаляє його без lifecycle migration.

Version OCP-000 не є версією жодного Concept або defining OCP. Споживач exact-bind-ить потрібний defining contract окремо.

## Канонічні принципи інтерпретації

1. **Explicit Operational Context** — спільне значення існує лише в явно визначеному governed context із названим semantic owner; foundation не припускає одного універсального container “Operational Space”.
2. **Operation First** — будь-яка координована активність моделюється як Operation.
3. **Resource Agnostic** — сили та засоби моделюються через універсальне поняття Resource.
4. **Separation of Structures** — штатна структура, оперативне підпорядкування й операційна координація є незалежними моделями.
5. **One Concept — One Name** — кожне прийняте поняття має одну назву та одне місце визначення.
6. **Knowledge Graph Model** — онтологія є мережею понять і типізованих зв’язків; технологія зберігання не визначається цим документом.

Ці принципи спрямовують інтерпретацію реєстру, але не створюють Concept, graph edge, record, profile, result або authorization. У разі деталізації перевагу має exact defining contract у межах його прийнятої відповідальності.

### Межа кандидата Operational Space

Історичний ярлик `Operational Space First` не надавав і не надає фундаментальної identity. У `1.0.0` його замінено точнішим принципом `Explicit Operational Context`, який уже виконується через governed contexts і не потребує нового Concept.

Рядок `Operational Space: Proposed` залишається незалежним candidate marker. Він не має defining specification, нормативної відповідальності, current dependency edge або права бути неявним owner для Operation, spatial bindings, Environment, Coordination чи domain profiles. Його можна перевести з `Proposed` лише через повний OCP-001/OCP-016 cycle та окремий Board act.

## Активний реєстр Concept

| Concept | Status | Specification / Decision |
|---|---|---|
| Resource | Canonical | OCP-003; AD-014; AD-018A; AD-016L; separately authorized T4 act |
| Operation | Canonical | OCP-004; AD-020A; AD-016X; separately authorized WJ lifecycle act |
| Assignment | Accepted | OCP-005; Architecture Board approval of PR-0004 |
| Operational Space | Proposed | — |
| Organization | Canonical | OCP-007; AD-019A; AD-016T; separately authorized O9C lifecycle act |
| Objective | Canonical | OCP-008; AD-003; AD-017; AD-016G; separately authorized T4 act |
| Event | Canonical | OCP-010; AD-006C; AD-016AD; AD-032; separately authorized Event Concept canonicalization act |
| Spectrum | Proposed | — |
| Constraint | Accepted | OCP-006; Architecture Board approval of PR-0005 |
| Risk | Proposed | AB-005; після Constraint |
| Order | Proposed | AB-002 |
| Coordination | Proposed | — |
| Capability | Canonical | OCP-009; AD-005C; AD-016D; separately authorized T4 act |

Статуси в таблиці є статусами Concept, а не статусами документів. `Accepted` означає, що Architecture Board прийняла поточне визначення як основу подальшої роботи; це не означає `Canonical` і не змінює автоматично статус документа.

`Proposed` row фіксує лише точну назву питання для discovery. Він не обіцяє positive identity, майбутню семантику, місце в graph або наступний status. Candidate може бути уточнений, перейменований, відкладений або deregistered лише через видимий governance act; такі дії не змінюють status інших рядків.

## Negative identity decision for Result

AD-006C відхилив фундаментальний Concept `Result`: realized outcome не отримує універсальної незалежної identity у foundation ontology.

Architecture Board прийняла OCP-011 у PR-0013 і завершила migration accounting, тому тимчасовий рядок `Result: Proposed` видалено з активного Concept registry. Це не перехід у `Accepted`, `Deprecated` або `Archived`; кандидат deregistered після negative identity verdict.

Термін `result` може використовуватися описово або в локальних контрактах, зокрема `Constraint evaluation result`, але таке використання не створює фундаментальний Concept `Result`.

## Negative identity decision for Operational Area

AD-014B обрав Operation-local spatial binding і не підтвердив незалежну Core identity для `Operational Area`. OCP-004 `0.8.0` реалізує zero/one/many local bindings як versioned structured values owning Operation, тому тимчасовий рядок `Operational Area: Proposed` видалено з active Concept registry.

Це не перехід у `Accepted`, `Deprecated` або `Archived`. Назви `area`, `work area`, `corridor`, `route`, `point` чи `spatial context` можуть описувати локальне призначення або opaque domain payload, але не створюють reusable area identity, P-001 record чи graph node.

Managed Position Site, Launch Site і Relay Site лишаються Infrastructure Resource. Environment лишається taxonomy category і можливим domain input, а не фундаментальним Concept або alternative owner для managed-site identity. Reusable area record, fundamental Operational Area/Environment identity чи domain-profile authority можна reopen лише за gates AD-014 §32.

## Negative identity decisions for State and Readiness

AD-011 окремо прийняв S0 і R0. Поточний foundation не має shared State abstraction і не видає shared Readiness conclusion.

`State` не має доведеної identity незалежно від subject, локального lifecycle, observation, assessment, criterion, context або time. `Readiness` за поточними evidence є можливою contextual conclusion, але не має accepted consumer, criterion owner, target contract, evaluator/rule authority або complete freshness/replay boundary.

Тому рядки `State: Deferred` і `Readiness: Deferred` видалено з active Concept registry. Це не перехід у `Accepted`, `Deprecated` або `Archived`. Терміни можуть лишатися описовими або domain-owned, але не створюють Core Concept чи positive authority. Reopening регулюється AD-011 §25.3.

## Governed assessment records

OCP-011 визначає Accepted `OutcomeAssessmentRecord` як P-001 identified record, а не фундаментальний Concept. Record exact-bind-ить Objective target, criterion, evidence snapshot, input snapshot, evaluator, evaluation time, conclusion і provenance та зберігає correction history через explicit supersession.

OutcomeAssessmentRecord не є Operation lifecycle stage, mutable Objective status, Event truth або універсальним realized outcome. Missing, stale, ambiguous чи conflicting evidence не може створювати definitive conclusion за baseline contract.

Цей абзац є registry guardrail. Нормативним owner полів, інваріантів, lifecycle і future extensions лишається OCP-011.

## Governed Capability Claim records

OCP-012 визначає Accepted `CapabilityClaimRecord` як P-001 identified record, а не фундаментальний Concept. Record exact-bind-ить Resource holder, одну точну OCP-009 Capability version, claimant, condition set, authority, evidence/support, effectivity та provenance; однакові claims не роблять Resources однаковими або взаємозамінними.

`holder-capability@1` зберігає attributable F0/A0 baseline. `holder-capability@2` явно розділяє declaration-only та evidence-backed modes; лише evidence-backed mode може invoke exact OCP-012-local F1/A1 source-use rules. Така classification не є Capability truth, Readiness, availability, authorization, admissibility або downstream eligibility.

Цей абзац є registry guardrail. Нормативним owner claim semantics, modes, evidence rules і future extensions лишається OCP-012.

## Робоче рішення щодо Resource

`Actor` не є окремим фундаментальним Concept. Людина, екіпаж, розрахунок, технічний засіб або інший залучений елемент моделюється як Resource. Його операційна роль визначається через Assignment.

## Незалежні моделі

- Organizational Model — штатна належність.
- Command Model — актуальне управління та підпорядкування.
- Operational Model — участь в операціях.
- Coordination Model — взаємодія між учасниками, зокрема між незалежними вертикалями у спільній операційній зоні.

Назви моделей не створюють однойменні фундаментальні Concept автоматично.

## Питання поза compatibility surface `1.0.0`

Наведені питання не мають registry authority й не блокують `1.0.0`, тому що OCP-000 не визначає відповідні identities або contracts. Кожна positive відповідь потребує власного OCP-001/OCP-016 cycle, exact owner, evidence і Board act:

- Межі між Resource та Organization.
- Канонічна модель Operational Situation.
- Канонічна модель погодження між незалежними вертикалями.
- Межа між Constraint violation та майбутнім Conflict Concept.
- Наступні contract-local freshness/ambiguity activations після окремих OCP-011 і OCP-012 activations; жодна з них не створює глобального evidence lifetime.

## T0 canonicalization act

T0 встановлює OCP-000 `1.0.0 / Canonical` як registry contract і не змінює жодного Concept row, defining OCP, dependency або generated map.

Зокрема, цей act:

- замінює двозначний `Operational Space First` на `Explicit Operational Context` без нового Concept;
- зберігає `Operational Space`, `Spectrum`, `Risk`, `Order` і `Coordination` у status `Proposed` без semantic authority;
- зберігає вісім Accepted Concepts у status `Accepted`;
- не reopen-ить Result, Operational Area, State або Readiness;
- не приймає OCP-001, OCP-002, OCP-016 або P-001 за implication;
- не додає graph edge, record family, registry field, production schema або implementation authority; і
- не авторизує T1 чи будь-який downstream promotion.

Canonical status набуває чинності лише після exact-head Fable approval, Codex adjudication, green CI, окремої явної авторизації Павла/Architecture Board саме для T0 та squash merge. До merge цей розділ і frontmatter є proposed T0 act.

## Revision `1.1.0` — Capability status transition

Окремий T4 lifecycle act змінює рівно один active registry value: `Capability: Accepted → Canonical`. За SemVer policy OCP-000 це MINOR revision, тому document version синхронно переходить `1.0.0 → 1.1.0`.

Registry membership, row identity, status vocabulary, Board authority, Proposed markers, negative identity verdicts і всі інші Concept rows лишаються незмінними. Revision не додає Capability semantics: defining authority залишається в OCP-009, а OCP-000 лише відображає окремо авторизований status.

## Revision `1.2.0` — Objective status transition

Окремий другий T4 lifecycle act змінює рівно один active registry value: `Objective: Accepted → Canonical`. За SemVer policy OCP-000 це MINOR revision, тому document version синхронно переходить `1.1.0 → 1.2.0`.

Registry membership, row identity, status vocabulary, Board authority, Proposed markers, negative identity verdicts і всі інші Concept rows лишаються незмінними. Revision не додає Objective semantics, amendment/revision identity, lifecycle або achievement authority: defining contract залишається в OCP-008, а OCP-000 лише відображає окремо авторизований status.

## Revision `1.3.0` — Resource status transition

Окремий третій T4 lifecycle act змінює рівно один active registry value: `Resource: Accepted → Canonical`. За SemVer policy OCP-000 це MINOR revision, тому document version синхронно переходить `1.2.0 → 1.3.0`.

Registry membership, row identity, status vocabulary, Board authority, Proposed markers, negative identity verdicts і всі інші Concept rows лишаються незмінними. Revision не додає Resource taxonomy, Organization mapping, relation, operational lifecycle, availability, Readiness, quantity або Capability semantics: defining contract залишається в OCP-003, а OCP-000 лише відображає окремо авторизований status.

## Revision `1.4.0` — Organization status transition

Окремий четвертий T4 lifecycle act змінює рівно один active registry value: `Organization: Accepted → Canonical`. За SemVer policy OCP-000 це MINOR revision, тому document version синхронно переходить `1.3.0 → 1.4.0`.

Registry membership, row identity, status vocabulary, Board authority, Proposed markers, negative identity verdicts і всі інші Concept rows лишаються незмінними. Revision не додає Organization/Resource mapping, taxonomy, continuity, composition, relationship-kind meaning, exception, availability, Readiness, Assignment, authority або Capability-holder semantics: defining contract залишається в OCP-007, а OCP-000 лише відображає окремо авторизований status.

## Revision `1.5.0` — Operation status transition

Окремий T5 WJ lifecycle act змінює рівно один active registry value: `Operation: Accepted → Canonical`. За SemVer policy OCP-000 це MINOR revision, тому document version синхронно переходить `1.4.0 → 1.5.0`.

Exact Canonical provenance є `OCP-004; AD-020A; AD-016X; separately authorized WJ lifecycle act`. Первинне прийняття Operation у PR-0003 лишається історією acceptance, а не provenance цього Canonical переходу.

Registry membership, row identity, status vocabulary, Board authority, Proposed markers, negative identity verdicts і всі інші Concept rows лишаються незмінними. Revision не додає Operation stage, authorization source, Event relation, outcome, Readiness, Assignment mutation, IO2 record identity або production semantics: defining authority залишається в OCP-004, а OCP-000 лише відображає окремо авторизований status.

## Revision `1.6.0` — Event status transition

Окремий Event Concept canonicalization act змінює рівно один active registry value: `Event: Accepted → Canonical`. За SemVer policy OCP-000 це MINOR revision, тому document version синхронно переходить `1.5.0 → 1.6.0`.

Exact Canonical provenance є `OCP-010; AD-006C; AD-016AD; AD-032; separately authorized Event Concept canonicalization act`. PR-0012 лишається історією acceptance, AD-016AD — окремим просуванням defining document, а AD-032 доводить OCP-001 canonicalization prerequisites і атомарну status synchronization.

Registry membership, row identity, status vocabulary, Board authority, Proposed markers, negative identity verdicts і всі інші Concept rows лишаються незмінними. Revision не додає Operation↔Event edge, relation owner, temporal interval, correlation, Event-kind registry, truth, assessment, Conflict, Risk, Readiness, authorization або production semantics: defining authority залишається в OCP-010, а OCP-000 лише відображає окремо авторизований Concept status.
