# ADR-003 — Ontology as Knowledge Graph

- **Status:** Accepted
- **Date:** 2026-08-02

## Decision

Operational Ontology моделюється як граф понять і типізованих зв’язків.

## Consequences

- Domain Model, API та ERD є проєкціями онтології.
- Реалізація не зобов’язана використовувати графову базу даних.
- Канонічними є Concept і Relationship, а не таблиця чи DTO.
