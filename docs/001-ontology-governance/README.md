---
Document-ID: OCP-001
Title: Ontology Governance
Version: 0.8.0
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000
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

Перший reference checker вводиться окремим `PR-0006 — Add Executable Ontology Checker` одразу після Constraint cycle, до подвоєння кількості визначених Core Concept.

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
