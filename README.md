# OCP Foundation

**Operational Coordination Platform (OCP)** — платформа оперативної координації, що моделює реальний операційний простір та взаємодію сил і засобів.

Цей репозиторій є канонічним джерелом фундаментальних онтологічних, архітектурних та інженерних специфікацій OCP.

## Основний принцип

> Ми не проєктуємо програму. Ми формалізуємо операційну модель реального світу, яку програма лише реалізує.

## Правило затвердження

Жоден документ не потрапляє в `main`, поки його не затвердить Architecture Board.

Усі зміни проходять через окрему гілку та draft pull request.

## Межі репозиторію

Репозиторій містить:

- Operational Ontology;
- Ontology Governance;
- Concept Taxonomy;
- Architecture Decision Records;
- архітектурний backlog;
- reference checker, схеми та приклади без чутливих даних.

Репозиторій **не повинен містити**:

- реальні операційні дані;
- координати;
- відомості про підрозділи;
- персональні дані;
- ключі, токени та облікові дані;
- інші матеріали обмеженого доступу.

## Структура

```text
docs/          канонічні специфікації
adr/           архітектурні рішення
architecture/  діаграми та архітектурні моделі
schemas/       машинозчитувані схеми
tools/         reference checker та інженерні перевірки
backlog/       відкриті питання та дорожня карта
```

## Статус

**Foundation 0.3 — Executable Validation Foundation.**

- Resource, Operation, Assignment і Constraint мають статус `Accepted`;
- reference ontology checker перевіряє YAML fixtures, exact-version Constraint evaluation, lifecycle projections, status synchronization і прийняті regression counterexamples;
- GitHub Actions запускає unit tests і fixture validation для pull request та `main`;
- State і Readiness залишаються Deferred до завершення першого executable validation cycle та перегляду ADR-DRAFT-007;
- checker не є production validator або незалежним нормативним джерелом;
- орієнтовна загальна foundation-готовність після прийняття PR-0006: **≈35%**.

Детальна не-нормативна оцінка та послідовність робіт наведені в [Foundation Roadmap](backlog/roadmap.md).
