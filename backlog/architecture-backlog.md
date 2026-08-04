# Architecture Backlog

| ID | Тема | Статус | Наступна дія |
|---|---|---|---|
| AB-001 | Operational Situation як окремий Concept | Open | Перевірити після базових Concept |
| AB-002 | Order як фундаментальний Concept | Open | Визначити, чи є Order обов’язковим або одним із можливих джерел авторизації Operation |
| AB-003 | Погодження між незалежними вертикалями | Open | Включити до Coordination Model |
| AB-004 | Capability Registry | Resolved | PR-0010 / OCP-009: прийнято reusable Capability definition, governed namespace, exact-version resolution і supersession contract; holder claims залишаються окремим downstream-рішенням |
| AB-005 | Risk Taxonomy | Open | Переглянути після OCP-006 і майбутнього Conflict model |
| AB-006 | Межа Organization / Resource | Open | Уточнити після Organization Concept; перевірити модель Organizational Resource |
| AB-007 | State як Concept | Deferred | Переглянути ADR-DRAFT-007 після Constraint, PR-0006 fixtures та стабілізації Accepted Operation і Assignment |
| AB-008 | Межа Infrastructure Resource / Environment | Open | Перевірити на Position Site, Launch Site і Relay Site |
| AB-009 | Resource Group як окремий Concept | Open | Перевірити групове залучення після OCP-005 |
| AB-010 | Модель кількості, резервування і споживання Consumable Resource | Deferred | Після Assignment і Constraint; використовувати managed stock як гранулярність Resource |
| AB-011 | Взаємозамінність Resource | Planned | Після Capability claim model визначити взаємозамінність за exact Capability claims, Constraint results і operational context без втрати Resource identity |
| AB-012 | Автоматична перевірка нормативних Concept references | Planned | PR-0006 додає повний rules manifest для emitted checks і CI; duplicate/reference linter залишається до першої Canonical promotion |
| AB-013 | Машинозчитувані інваріанти | Planned | PR-0006 реалізує reference subset, lifecycle fixtures і accepted counterexamples; розширювати з кожним Concept cycle |
| AB-014 | Operational Intent як окремий Concept | Resolved | AD-004C: окремий фундаментальний Concept не вводиться; reopening потребує нових доказів independent identity за AD-004 §3 |
| AB-015 | Мінімальна повнота Operation | Open | Формалізувати domain validation rules для переходу Draft → Planned |
| AB-016 | Композиція Operation | Open | Визначити правила parent/child, ациклічність і межу з незалежною координацією |
| AB-017 | Авторизація Operation | Open | Визначити джерела авторизації без передчасного введення Authority, Approval або Policy |
| AB-018 | Conflict між Operation як факт або похідний результат | Open | Визначити межу між Constraint violation, агрегованим finding і Conflict Concept |
| AB-019 | Suspended у lifecycle Operation | Deferred | Переглянути після Constraint, Assignment і State |
| AB-020 | Operation Template як окремий Concept | Open | Перевірити після стабілізації Operation lifecycle і повторюваних Operation |
| AB-021 | Формальна derivation участі через Assignment | Resolved | Нормативне визначення в OCP-005 §§8–9; reference implementation у PR-0006 |
| AB-022 | Validation contract для explicit intent | Resolved | PR #23: OCP-004 v0.7.0, plural objective_refs semantics, immutable exact-binding evidence, fail-safe projections and executable fixtures merged |
| AB-023 | Provenance taxonomy для lifecycle і relationship records | Open | Уточнити після Event, Order і Coordination Concept |
| AB-024 | Автоматична синхронізація Concept status | Resolved | PR-0006 звіряє OCP-000, machine-readable projection OCP-002 і Concept-Status defining documents у CI |
| AB-025 | Reservation / Allocation як окремий Concept | Open | Визначити межу з Assignment і Constraint |
| AB-026 | Amendment model для Assignment | Open | Визначити зміни role та applicability після Establishment без переписування історії |
| AB-027 | Role Taxonomy | Open | Визначити межі Core role codes і domain role namespaces |
| AB-028 | Узгодження lifecycle Operation та Assignment | Open | Визначити правила для незавершених Assignment при Completed, Cancelled або Aborted Operation після Constraint |
| AB-029 | Кілька applicability intervals в Assignment | Open | Вирішити: один Assignment з кількома інтервалами чи окремий Assignment на інтервал |
| AB-030 | Масове створення Assignment | Open | Визначити механізм для груп Resource без неявного успадкування участі |
| AB-031 | Lifecycle record consistency | Resolved | OCP-005 використовує authoritative linear transition history; regression fixture у PR-0006; узагальнення форми винесено в P-001 |
| AB-032 | Canonical rule reference integrity | Resolved | OCP-001 вимагає єдине defining location; rules manifest у PR-0006; повний duplicate linter у AB-012 |
| AB-033 | Захист гілки main | Resolved | Ruleset `Foundation Main Protection` підтверджено під час review PR #25: PR required, linear/squash history, force-push і deletion заборонені, required check `reference-checker`; post-merge main-context check succeeded |
| AB-034 | Constraint Concept | Resolved | OCP-006 Accepted рішенням Architecture Board у PR-0005 |
| AB-035 | Constraint expression language | Deferred | Після review OCP-006 вибрати machine-readable predicate та selector representation |
| AB-036 | Constraint precedence, override and waiver | Open | Визначити порядок застосування, exception semantics і provenance без передчасного Policy Concept |
| AB-037 | Quantity, demand and capacity model | Open | Визначити units, aggregation та capacity consumption для quantitative Constraint |
| AB-038 | Conflict derivation model | Open | Визначити, коли одне чи більше Constraint violation створюють збережений або похідний Conflict |
| AB-039 | Constraint evaluation freshness and replay | Open | Визначити строк актуальності dynamic evaluation, snapshot contract і deterministic replay; є майбутнім owner для машинної перевірки `stale`/`ambiguous` evidence state в OCP-011 |
| AB-040 | Executable ontology checker | Resolved | PR-0006 merged; reference checker, exact-version evaluation, manifests, fixtures, status sync and CI accepted |
| AB-041 | Relationship as foundation | Resolved | AD-001 Accepted: Option C — Relationship as a governed modeling pattern; P-001 defines reusable identified-record form |
| AB-042 | Foundation artifact taxonomy | Resolved | PR-0006A merged; artifact taxonomy, P-001 invocation and normative review lane accepted |
| AB-043 | Foundation checker expansion | Resolved | PR #25 merged as `93c04f6`: artifact governance, exact Pattern references, AD↔AB synchronization and post-baseline linear-history audit externally approved and verified against real `main` history |
| AB-044 | Organizational identity continuity | Open | Визначити continuity through redesignation, merger, split and reorganization |
| AB-045 | Organization relationship type taxonomy | Open | Визначити governed classes/types and class-to-type consistency rules |
| AB-046 | Organization lifecycle review | Open | Перевірити lifecycle після реальних fixtures і залежних Coordination use cases |
| AB-047 | Organization composition and organizational units | Open | Визначити межу Organization, sub-unit, crew and temporary grouping |
| AB-048 | One Concept — One Responsibility | Proposed | Переглянути після OCP-007 та relationship-record практики |
| AB-049 | Consolidate OCP Architectural Doctrine | Proposed | Review after 10–12 fundamental Concepts |
| AB-050 | Explicitly Not Defined section | Proposed | Перевірити як обов’язковий шаблон після OCP-007 |
| AB-051 | Structural schemes and multiple verticals | Open | Визначити scheme identity, exceptions and cross-scheme interpretation |
| AB-052 | Organization-to-Organizational-Resource mapping | Open | Визначити explicit mapping without identity collapse |
| AB-053 | Concept dependency source migration | Resolved | Перенести current edges з `concept-dependencies.yaml` у `Concept-Depends-On` defining-документів, перемкнути generator і видалити staging source; одночасна наявність обох джерел є помилкою |
| AB-054 | Event and Result boundary | Resolved | AD-006C: прийнято E3 — occurrence Event + attributable observation records; R3 — governed OutcomeAssessmentRecord без фундаментального Result Concept |
| AB-055 | Event occurrence та ObservationRecord contract | Resolved | PR-0012 / OCP-010: прийнято occurrence identity, zero-observation validity, P-001 ObservationRecord, fail-closed references і перший integrated non-sensitive scenario; Event став восьмим Accepted Concept |
| AB-056 | OutcomeAssessmentRecord та Result registry resolution | Resolved | PR-0013 / OCP-011: прийнято exact target/criterion/evidence/input/evaluator binding, P-001 Module C branching, fail-safe evidence matrix та normative integrated-scenario assessment; fundamental Result candidate deregistered після negative identity verdict AD-006C |
| AB-057 | Holder-specific Capability Claim boundary | Discovery | AD-007 v0.3.0: externally compare A/B/C/C-prime/D/E/F against declaration/evaluation authority, replay, contradiction, OCP-011 fit, Core/domain interoperability, human readability and the exact fail-safe input required by AB-011; select no outcome until evidence separates B from D and other viable variants |
