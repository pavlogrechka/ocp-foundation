# ADR-001 — Domain-Driven First

- **Status:** Accepted
- **Date:** 2026-08-02

## Decision

Послідовність проєктування OCP: Reality → Ontology → Operational Models → Domain Model → Business Rules → Architecture → Implementation.

## Consequences

- Жодна сутність БД не створюється без доменного обґрунтування.
- Жоден API не створюється без описаного процесу та правила.
- UI є проєкцією доменної та операційної моделей.
