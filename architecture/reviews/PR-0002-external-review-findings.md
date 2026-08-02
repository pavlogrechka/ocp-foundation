---
Review-ID: REVIEW-PR-0002
Title: External Review Findings for Resource Concept
Status: Addressed in PR-0002A
Owner: Architecture Board
Reviewed-Document: OCP-003 v0.1.0
Last-Review: 2026-08-02
---

# External Review Findings — PR-0002

## Purpose

Зафіксувати зауваження зовнішнього архітектурного рев’ю до `OCP-003 — Resource Concept`, рішення Architecture Board та спосіб їх усунення.

## Findings

| ID | Finding | Decision | Resolution |
|---|---|---|---|
| RF-0002-01 | Абсолютна ідентичність Resource суперечила гілці Consumable Resource | Accepted | Ідентичність визначена на керованій гранулярності; витратний Resource є запасом, партією, контейнером, комплектом або обліковою одиницею |
| RF-0002-02 | OCP-003 нормативно посилався на невизначені `Position` і `Governance` | Accepted | Невизначені Concept references прибрані; OCP-001 отримав правила нормативних посилань і розмежування taxonomy category / Concept |
| RF-0002-03 | `Readiness` одночасно був «канонічним» в OCP-000 і відкритим питанням в OCP-003 | Accepted | Канонічний список замінено реєстром Concept зі статусами; Readiness і State позначені `Deferred` |
| RF-0002-04 | Частина тверджень у розділі Invariants не була перевірними булевими умовами | Accepted | Дозвільні та неімплікативні твердження перенесені до Business Rules і Semantic Rules; OCP-001 отримав формальні критерії інваріанта |
| RF-0002-05 | Версіонування Draft-документів було невизначеним | Accepted | Додано pre-canonical policy `0.Y.Z`; змістовні та несумісні зміни збільшують `Y`, редакційні — `Z` |

## Architecture Board Decision

Усі findings прийняті як дефекти узгодженості ранньої онтології. Виправлення виконуються окремим коригувальним PR і не змішуються з `PR-0003 — Define Operation Concept`.

## Dependency Impact

PR-0003 залишається Draft до виконання двох умов:

1. PR-0002A злитий у `main`;
2. гілка PR-0003 оновлена від нового `main` і перевірена на відповідність оновленим правилам OCP-001.
