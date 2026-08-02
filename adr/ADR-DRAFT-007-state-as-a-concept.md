# ADR-DRAFT-007 — State as a Concept

- **Status:** Draft
- **Date:** 2026-08-02
- **Review-After:** Canonical descriptions of Operation and Assignment

## Context

Readiness, Availability, Health та Operational Status можуть потребувати власної ідентичності, історії, підтвердження, причини та джерела оцінки. Простого enum може бути недостатньо.

## Proposed Decision

Розглянути `State` як окремий Concept, спеціалізаціями якого можуть бути:

- Readiness;
- Availability;
- Health;
- Operational Status.

## Decision Deferred

Рішення відкладається до завершення опису `Operation` та `Assignment`, щоб перевірити модель на ключових сценаріях.
