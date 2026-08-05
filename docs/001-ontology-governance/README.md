---
Document-ID: OCP-001
Title: Ontology Governance
Version: 1.0.0
Status: Canonical
Owner: Architecture Board
Depends-On: OCP-000, OCP-016, AD-015
Used-By: All OCP specifications and AI development workflows
Last-Review: 2026-08-05
---

# Ontology Governance

## Мета

Визначити правила створення, зміни, канонізації та депрекації понять Operational Ontology.

## Обов’язкові правила

- Operational Ontology є єдиним джерелом канонічних визначень.
- Одне поняття має одну назву й одне місце визначення.
- Кожне нормативне правило має одне місце визначення; інші документи посилаються на defining document і section, а не створюють незалежні копії формули.
- Поняття реалізації не включаються до онтології.
- Нове фундаментальне поняття потребує явного рішення Architecture Board.
- Канонічні документи не змінюються напряму в `main`.
- Кожна зміна проходить окрему гілку, draft PR та затвердження Architecture Board.
- Згадування терміна не надає йому статусу Accepted або Canonical.
- Категорія таксономії не є визначеним Concept автоматично.
- Рішення Architecture Board про зміну статусу Concept повинно бути відображене в реєстрі OCP-000, OCP-002 і metadata defining document у тому самому PR до merge.
- Коригувальний цикл не змішується з новим Concept cycle, якщо Architecture Board явно не затвердила виняток і не зафіксувала його в PR.

## Нормативні класи артефактів і review

Машинозчитувана класифікація артефактів визначена в `architecture/artifact-taxonomy.yaml`; пояснення — в `architecture/artifact-taxonomy.md`.

Артефакти класів `binding` і `binding-when-invoked` проходять одну review-смугу:

1. окрема гілка та draft pull request;
2. зовнішнє adversarial review до рішення Architecture Board;
3. явне рішення Architecture Board;
4. squash merge після успішних required checks.

Чисті records — review-файли, backlog accounting і status-only updates, які прямо випливають із уже прийнятої хореографії, — не запускають рекурсивне review самих review.

Pattern є `binding-when-invoked`: артефакт не зобов’язаний використовувати Pattern, але versioned metadata `Uses-Patterns` робить Required Elements та обрані Optional Modules Pattern обов’язковими для цього артефакту. Pattern визначає форму моделювання, а не доменну семантику. Зміни Pattern версіонуються та проходять зовнішнє review.

Нові архітектурні рішення реєструються як `AD` у `architecture/discovery/`. Реєстр `adr/` заморожений для нових номерів; наявні ADR зберігають чинність і завершують уже розпочаті lifecycle.

## Обов’язковий Core Boundary review

[AD-015B §§33–40](../../architecture/discovery/AD-015-core-boundary-specification.md) обрав tiered semantic-authority routing у окремому human-readable OCP. OCP-001 володіє лише автоматичним trigger і review-хореографією; повний семантичний тест визначає [OCP-016 §§3–18](../016-core-boundary/README.md). Ці правила не дублюються між документами.

Core Boundary review є обов’язковим, якщо proposal створює або змістовно розширює хоча б один із таких об’єктів чи повноважень:

- фундаментальний Concept або current Concept dependency;
- Core non-Concept record, rule, consumer activation або local structured value;
- Pattern чи його обов’язкову reusable form;
- Core interoperability envelope над domain-owned semantics;
- domain-local contract, який має бути представлений або exact-referenced у Foundation;
- implementation structure, яку proposal подає як спільну семантику;
- machine-readable registry, status projection, score або checker behavior, що може бути помилково сприйнятий як admission authority;
- route movement, reopening, retirement, deregistration або іншу зміну вже прийнятої semantic authority.

Чисте редакційне виправлення, Review record або backlog accounting не запускає новий Core Boundary decision, доки воно не змінює семантичний owner, route, status, dependency, accepted scope чи нормативний результат.

Після trigger автор proposal повинен:

1. явно назвати candidate objects до вибору repository artifacts і відокремити semantic candidates від Pattern form proposal;
2. застосувати чинну exact version OCP-016;
3. запропонувати один primary semantic-authority route для кожного semantic candidate та, окремо, будь-яке Pattern creation/invocation;
4. подати authority ledger, concrete consumers, exact dependencies, evidence, non-implications і migration/reopening effect;
5. пройти external adversarial review; і
6. отримати явний Architecture Board act для admission, rejection, reopening або status change.

OCP-001 не визначає semantic route і не приймає candidate. OCP-016 не запускає review і не надає status. Candidate contract не може схвалити себе. Checker, registry, checklist total, newest timestamp, record order, issuer/source/deployment count або majority не замінюють Board act.

Якщо object class, legitimate owner, concrete consumer, exact version/profile або route лишається неоднозначним, proposal залишається Discovery чи поза Core; неоднозначність не дозволяє permissive default.

## Захист основної гілки

Правило роботи через PR повинно бути забезпечене механічно GitHub Ruleset або branch protection для `main`:

1. прямі push до `main` заборонені;
2. зміна `main` дозволена лише через pull request;
3. force push і видалення `main` заборонені;
4. правила застосовуються також до адміністраторів і власників репозиторію;
5. після появи ontology linter його успішна перевірка є required status check;
6. дозволений merge method — squash merge.

Аварійне виправлення також проходить через окрему гілку та PR. Швидкість виправлення не скасовує простежуваність зміни.

Repository checker може аудитувати історію merge лише постфактум. Превентивним контролем merge method і required review залишається GitHub Ruleset або branch protection.

## Статуси документа і Concept

Статус документа та статус Concept є незалежними характеристиками.

- `Document Status` показує зрілість конкретного документа.
- `Concept Status` показує зрілість поняття в реєстрі онтології.

Документ у статусі `Draft` може описувати Concept у статусі `Proposed`, `Under Review` або `Accepted`, але не робить його Canonical лише через факт публікації чи merge до `main`.

Документ, що визначає Concept, повинен містити metadata `Defines-Concepts` і `Concept-Status`. Значення `Concept-Status` повинно відповідати реєстру OCP-000 і представленню в OCP-002.

## Життєвий цикл поняття

`Proposed → Under Review → Accepted → Canonical → Deprecated → Archived`

Включення терміна до реєстру кандидатів означає лише його реєстрацію для подальшого розгляду.

`Accepted` означає, що Architecture Board прийняла поточну семантику як основу залежних специфікацій. `Accepted` не означає `Canonical` і не гарантує стабільність контракту версії `1.x`.

## Хореографія статусів Concept

Нормальний Concept cycle використовує таку послідовність:

1. **Draft PR відкрито або Concept зареєстровано як кандидат → `Proposed`.**
   Поки PR залишається Draft і проходить робочі або зовнішні review-цикли, Concept може залишатися `Proposed`.
2. **PR позначено ready for review → `Under Review`.**
   У тому самому commit синхронізуються OCP-000, OCP-002 і `Concept-Status` defining document.
3. **Architecture Board схвалила семантику → `Accepted`.**
   Статус оновлюється в тому самому PR після рішення Board і до merge. Нормальний merge нового Concept не повинен залишати його `Under Review` у `main`.
4. **Окремий canonicalization PR → `Canonical`.**
   Канонізація потребує стабільних залежностей, машинозчитуваних перевірок і окремого рішення Architecture Board.

Звичайний review-коментар або зовнішнє adversarial review не змінює Concept status автоматично. Статус змінюється лише явною процесною дією та синхронним оновленням усіх authoritative представлень.

Якщо status synchronization не виконано до merge, це governance defect і виправляється окремим коригувальним PR до початку наступного Concept cycle.

## Нормативні посилання на Concept і правила

Нормативне посилання дозволене, якщо Concept:

1. зареєстрований у Operational Ontology;
2. має явний статус;
3. має визначене місце специфікації або посилання на Architecture Backlog;
4. використовується відповідно до свого поточного статусу.

Concept у статусі `Proposed` або `Deferred` повинен бути явно позначений як невизначений або відкладений. Йому не можна передавати нормативну відповідальність так, ніби його модель уже прийнята.

Категорія таксономії може групувати поняття, але для нормативного використання як Concept потребує окремого визначення, статусу та рішення Architecture Board.

Формула, derivation rule, state machine або інший нормативний контракт визначається лише у defining document. Повторення в іншому документі дозволене лише як явно ненормативна ілюстрація, що містить посилання на джерело. Ontology linter повинен виявляти структурні дублікати нормативних rule identifiers; змістовну еквівалентність різних формулювань природною мовою встановлює зовнішнє adversarial review.

## Структурна цілісність нормативних ідентифікаторів і посилань

Канонічні primary artifacts класів `OCP`, `Pattern`, `AD`, `ADR` і `AB` утворюють єдиний машинно перевірний registry. Кожен exact identifier у цьому registry повинен належати рівно одному primary artifact, а identifier у metadata повинен відповідати repository path. Versioned reviewed-contract snapshots тієї самої OCP-специфікації не створюють нової artifact identity і не є окремими registry entries.

Frontmatter `Depends-On` виражає лише пряму залежність одного primary artifact від іншого. Кожне значення повинно:

1. бути exact token одного з форматів `OCP-NNN`, `P-NNN`, `AD-NNN`, `ADR-NNN`, `ADR-DRAFT-NNN` або `AB-NNN`;
2. exact-resolve до наявного primary artifact;
3. з'являтися в одному dependency list не більше одного разу;
4. не посилатися на artifact, якому належить цей list.

`Depends-On: P-NNN` означає залежність від Pattern artifact, але не invokes його obligations. Єдиним invocation authority лишається versioned `Uses-Patterns: P-NNN@x.y.z` за політикою `track-current`.

Rule identifier у `tools/ontology_checker/*rules.yaml` повинен бути глобально унікальним серед core та всіх module manifests. Кожен manifest entry повинен мати валідний identifier, допустимий `kind` і `source`, що починається з exact-resolvable `OCP-NNN`; відсутній `kind` має єдине визначене значення `validation`. Це source binding, а не передання нормативної влади executable manifest. Checker перевіряє exact OCP identifier, але не виводить тотожність семантики з prose, section label або схожості формулювань.

Механічний контроль навмисно обмежений структурованими registry entries, metadata і rule manifests. Виявлення прихованих дубльованих правил, суперечностей або перефразованої семантики у природній мові залишається обов'язком external review; відсутність machine finding не є доказом семантичної унікальності.

## Перевірка нового поняття

Поняття може бути запропоноване, якщо воно:

1. існує в реальній операційній діяльності;
2. має самостійне значення або життєвий цикл;
3. має власні правила чи зв’язки;
4. не є лише атрибутом іншого поняття;
5. не дублює наявне канонічне поняття.

## Канонічний шаблон Concept

- Name
- Definition
- Purpose
- Why Exists
- Lifecycle
- Owner
- Participants
- Inputs
- Outputs
- Dependencies
- Relationships
- Events
- Business Rules
- Semantic Rules
- Invariants
- Examples
- Open Questions

## Вимоги до інваріантів

Інваріант — універсальна булева умова, яка повинна залишатися істинною для кожного допустимого стану моделі.

Кожен інваріант повинен:

1. мати однозначну область застосування;
2. бути перевірним на моделі або knowledge graph;
3. допускати побудову контрприкладу, за якого він буде `false`;
4. не містити невизначених винятків або посилань на неописані правила;
5. не використовувати дозвільне формулювання `може` як основну умову;
6. квантифікувати лише ті сутності, властивості та зв’язки, для яких визначено спосіб створення, зберігання або виведення;
7. не повторювати визначення похідного зв’язку у формі тавтологічної перевірки;
8. обмежувати не лише обов’язкову присутність поля, а й заборонені стани його присутності, якщо поле впливає на derivation;
9. визначати авторитетне джерело та двосторонню узгодженість, якщо одна семантика представлена transition history і денормалізованими полями одночасно;
10. не дозволяти суперечливому stored result створювати більш permissive derivation, ніж відсутній або `indeterminate` result.

Твердження про відсутність імплікації, рекомендації, дозволи, derivation rules і пояснення належать до `Semantic Rules` або `Business Rules`, якщо вони не перетворені на самостійну перевірну умову.

Якщо правило вимагає поля provenance, source, evidence або validation result, документ повинен локально визначити мінімальний структурний контракт такого запису до введення інваріанта.

Структурна перевірність не дорівнює змістовній достатності. Core invariant може перевіряти наявність і валідний статус структурованого запису, а семантична достатність тексту або рішення повинна визначатися Business Rule чи domain validation rule.

Для lifecycle-моделі документ повинен явно визначити:

- допустимі переходи;
- чи є transition history авторитетним джерелом;
- правило обчислення поточного stage;
- узгодження timestamps і provenance з transition records;
- заборону розгалужених або взаємовиключних переходів для одного instance.

## Виконувана валідація

Після стабілізації перших взаємозалежних Concept кожен новий або змістовно змінений Concept повинен супроводжуватися машинозчитуваними fixtures настільки рано, наскільки це дозволяє поточний checker.

Контрприклад, прийнятий у review, повинен бути перенесений у regression fixture або executable test, якщо його можна виразити в поточному validation contract.

Discovery artifact, який порівнює кілька outcomes, повинен робити executable evidence outcome-fair:

1. безумовний блок містить лише спільні semantic obligations, виразимі для кожного admissible outcome;
2. obligations, що припускають конкретний record, derivation, storage, registry, Pattern або domain layer, належать explicit outcome-conditional block;
3. outcome, який реалізує спільну гарантію іншим механізмом, повинен назвати перевірний semantic equivalent, а не мовчки відкинути obligation;
4. external-review target повинен перевіряти, чи evidence obligations не припускають layer, відхилений самим outcome;
5. exit criteria повинні вимагати outcome-fair evidence coverage до Architecture Board selection.

Evidence matrix не може приховано робити один outcome неприйнятним лише тому, що вимагає артефакт або механізм, який цей outcome за визначенням не містить.

Reference checker, введений `PR-0006 — Add Executable Ontology Checker`, реалізує поточний структурний validation slice. Його наявність і зелений результат не розширюють semantic authority та не замінюють external review або рішення Architecture Board.

## Версіонування

### Pre-canonical документи

Для документів і Concept до першої Canonical версії використовується формат `0.Y.Z`:

- `Y` збільшується при змістовній зміні, включно з несумісною зміною, перейменуванням Concept або зміною структури моделі;
- `Z` збільшується лише при редакційному уточненні без зміни семантики.

Статус `Draft` не звільняє документ від версіонування.

### Canonical документи

Перша Canonical версія отримує номер `1.0.0`. Після цього застосовується Semantic Versioning:

- PATCH — редакційні або сумісні уточнення без зміни контракту;
- MINOR — сумісне додавання понять, зв’язків або правил;
- MAJOR — несумісна зміна фундаментальної моделі, перейменування або видалення канонічного Concept.

## Канонічна governance-поверхня `1.x`

OCP-001 `1.0.0` стабілізує не всі майбутні рішення Foundation, а спосіб, у який вони набувають нормативної сили. Для кожної сумісної версії `1.x` зберігаються такі гарантії:

1. Architecture Board лишається єдиним owner статусів документів і Concept; merge, checker або reviewer count не надають статус самі по собі.
2. Document Status і Concept Status лишаються незалежними осями.
3. Binding-зміна проходить окрему гілку, draft PR, зовнішнє adversarial review, явний Board act, required checks і squash merge.
4. Core Boundary trigger та review-хореографія визначаються тут, а semantic routes F/C/E/D/I — лише в exact current OCP-016; candidate не може схвалити себе.
5. Кожен primary artifact, normative rule і direct dependency має одну exact-resolvable identity та одне defining location.
6. Canonical OCP виконує direct-OCP dependency floor L2, визначений нижче.
7. Status, version, registry, taxonomy, defining-document і Pattern-invocation проєкції змінюються атомарно в межах свого promotion act.
8. Pattern лишається `binding-when-invoked`, має окремий lifecycle і імпортується лише exact `Uses-Patterns` binding за політикою `track-current`.
9. Discovery evidence лишається outcome-fair, а прийняті машинно виразимі контрприклади стають regression evidence.
10. Repository checker лишається advisory structural witness: він не визначає semantic readiness, truth, legitimate authority або Board approval.
11. Кожна lifecycle дія має явні non-implications, migration/rollback accounting та окрему authorization boundary.
12. Невизначеність object class, owner, consumer, exact contract або route зупиняє admission; permissive default заборонений.

Для OCP-001 після `1.0.0`:

- PATCH може уточнювати prose, приклади або evidence без нової obligation чи зміни сумісного результату;
- MINOR може додавати сумісну governance obligation, artifact class handling або структурну перевірку, не послаблюючи дванадцять гарантій;
- MAJOR потрібен, щоб змінити Board authority, незалежність status axes, OCP-001/OCP-016 ownership split, L2 floor, atomic projection contract, Pattern invocation authority, fail-safe admission boundary або дозволити machine evidence діяти як approval.

`Canonical` означає стабільну versioned governance-поверхню. Воно не означає production readiness, authorization, truth, універсальну повноту або незмінність назавжди.

## Direct OCP dependency floor — L2

`Depends-On` позначає нормативну пряму залежність primary artifact. Для OCP у статусі `Canonical` кожна direct dependency класу OCP повинна бути:

1. уже `Canonical` у попередньому accepted act; або
2. переведена в `Canonical` у тому самому атомарному act і в тому самому proposed repository tree.

Кожен artifact у same-act group все одно подає власну compatibility surface, readiness evidence, migration і rollback boundary. Топологічна допустимість є необхідною, але не достатньою підставою канонізації.

Draft або merely Accepted OCP не може постачати Canonical OCP неверсіоновану рухому semantic dependency. Виняток потребує окремої reviewed зміни, яка або:

- доводить, що reference ненормативний, і видаляє його з `Depends-On`; або
- вводить human-readable exact compatibility-binding contract, що зберігає спожиту семантику незалежно від document lifecycle, разом із явним machine representation для цього винятку.

До появи такого representation checker fail-safe відхиляє direct Canonical-to-pre-canonical OCP dependency. Виняток не виводиться з commit SHA, зеленого CI, document order, version recency, reviewer/issuer count, deployment count або популярності downstream consumer.

Artifact-class floors не зливаються з OCP lifecycle:

- Accepted ADR та AD керуються replacement/reopening, а не вигаданим Canonical status;
- invoked Pattern повинен бути Accepted і exact-version-bound; його current lifecycle не має Canonical status;
- Canonical Concept рухається разом із Canonical defining OCP та точними OCP-000/OCP-002 projections;
- promotion non-Concept OCP не змінює Concept status за implication.

## Атомарні lifecycle acts і authorization boundary

Окремий artifact є default promotion unit. Групування дозволене лише тоді, коли proposal доводить, що same-act atomicity зменшує, а не приховує review та rollback risk.

| Promotion target | Мінімальний атомарний набір |
|---|---|
| OCP document без Concept-status зміни | `Version`, `Status`, readable compatibility surface, exact direct dependencies, evidence та repository accounting |
| Concept | defining OCP document, OCP-000 row, OCP-002 projection, defining metadata та будь-яка generated current-state projection |
| Pattern | Pattern status/version і кожен exact `Uses-Patterns` invoker, якщо version змінюється |
| Non-Concept record OCP | document contract і evidence; жодна Concept projection не змінюється за implication |
| Corrective rollback | новий reviewed PR, що повертає весь узгоджений набір; partial edit або history rewrite заборонені |

Fable approval, Codex adjudication, green CI та Pavlo/Architecture Board authorization повинні стосуватися exact proposed head. Змістовна зміна після такого рішення потребує нового exact-head review й authorization. Дозвіл на один promotion act не переноситься на наступний slot, artifact або follow-up PR.

Lifecycle effect виникає лише після authorized squash merge. Позначення PR як Ready, reviewer recommendation чи зміна frontmatter у незмердженій гілці самі по собі не змінюють стан `main`.

## Поточна R4-хореографія Foundation

[AD-016B §§31–37](../../architecture/discovery/AD-016-foundation-canonicalization-readiness.md) обрав R4 (`F → C`) з L2 як обмежену Foundation migration, а не як загальний semantic route:

1. T0 OCP-000 і T1 OCP-016 завершені окремими Canonical acts;
2. цей T2 пропонує окрему канонізацію OCP-001;
3. T3 OCP-002 і T3 P-001 лишаються двома окремими promotion acts зі своїми lifecycle floors;
4. після T0–T3 AD-016C повинен заново обчислити post-enabling baseline, topology, blockers і migration cost;
5. окремий AD-016D Board act є обов’язковим до першого T4 promotion PR.

Завершення roots, зелений CI, витрачений час, schedule pressure або кількість уже виконаних slots не доводять готовність T4. Discovery чи remediation T4 blockers дозволені, але не надають promotion authority.

AD-016B є decision provenance цієї migration. Він не додається до `Depends-On` OCP-001: AD-016 уже нормативно залежить від OCP-001, а після інкорпорації L2 та lifecycle rules їхнім defining owner стає цей документ. Зворотний edge створив би цикл і дублювання authority.

## Machine evidence і fail-safe контрприклади

Reference checker механічно перевіряє identity/path, artifact lifecycle vocabulary, SemVer/status consistency, exact dependency resolution, Pattern bindings, Concept-status synchronization, rule-source integrity та complete-history constraints. Для L2 він додатково відхиляє Canonical OCP, що прямо залежить від OCP у pre-canonical status у тому самому proposed tree.

Ця перевірка доводить лише структурний факт. Вона не доводить semantic compatibility, sufficient evidence, production quality, legitimate owner або чинність Board act.

Обов’язкові людські контрприклади для promotion review:

1. Canonical OCP прямо залежить від Draft OCP — L2 порушено, навіть якщо всі тести зелені.
2. Два OCP переходять у Canonical в одному tree, але один не має власної compatibility surface — same-act group неприйнятний.
3. Canonical OCP посилається на Accepted AD — OCP floor не вигадує для AD статус Canonical.
4. OCP invokes Draft Pattern або stale Pattern version — OCP readiness не обходить Pattern lifecycle чи `track-current`.
5. Concept defining document змінено без синхронних OCP-000/OCP-002 projections — promotion неатомарний.
6. Non-Concept OCP стає Canonical, а його читач виводить Canonical status для пов’язаного Concept — implication хибна.
7. Checker, newest commit/timestamp, record order або reviewer/issuer count обирає authority — рішення недійсне.
8. Authorization T2 повторно використовується для T3 — non-transfer boundary порушено.
9. Candidate або його machine registry сам обирає OCP-016 route чи admission — self-approval заборонений.
10. Після помилки відкат змінює лише один authoritative projection — repository лишається governance-defective до атомарної корекції.

## T2 canonicalization act

Pre-T2 OCP-001 `0.9.0 / Draft` baseline має Git blob `effad195632e466a503b1f630f822453bf05005d` і SHA-256 `b9de3dcfe1477d352162bd115e05bd9fc80ccdb2533f161387ad6528673f4fbe`. T2 зберігає його чинні governance obligations, прибирає застаріле future-tense твердження про ще не створений checker і додає описану вище `1.x`-поверхню.

Direct dependencies лишаються exact і cycle-free:

- OCP-000 `1.0.0 / Canonical` постачає registry membership/status contract;
- OCP-016 `1.0.0 / Canonical` постачає semantic routing contract після trigger;
- AD-015 `0.3.0 / Accepted` лишається decision source для обраного C3 ownership split.

T2 атомарно змінює лише OCP-001 document version/status, readable governance contract, L2 structural witness та repository accounting. Він не змінює Concept/Pattern status, OCP-000 row, OCP-002 projection, OCP-016 route, dependency edge, domain contract, schema або production authority.

OCP-001 `1.0.0 / Canonical` набуває чинності лише після Fable approval exact head, Codex adjudication, green CI, окремої явної Pavlo/Architecture Board authorization саме для T2 та squash merge. Авторизація T1 не може бути повторно використана. До merge цей розділ і frontmatter є proposed T2 act; merge T2 не авторизує T3.
