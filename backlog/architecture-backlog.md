# Architecture Backlog

| ID | Тема | Статус | Наступна дія |
|---|---|---|---|
| AB-001 | Operational Situation як окремий Concept | Open | Перевірити після базових Concept |
| AB-002 | Order як фундаментальний Concept | Open | Визначити, чи є Order обов’язковим або одним із можливих джерел авторизації Operation |
| AB-003 | Погодження між незалежними вертикалями | Open | Включити до Coordination Model |
| AB-004 | Capability Registry | Open | Визначити межі Core і Capability |
| AB-005 | Risk Taxonomy | Open | Переглянути після OCP-006 і майбутнього Conflict model |
| AB-006 | Межа Organization / Resource | Open | Уточнити після Organization Concept; перевірити модель Organizational Resource |
| AB-007 | State як Concept | Deferred | Переглянути ADR-DRAFT-007 після Constraint, PR-0006 fixtures та стабілізації Accepted Operation і Assignment |
| AB-008 | Межа Infrastructure Resource / Environment | Open | Перевірити на Position Site, Launch Site і Relay Site |
| AB-009 | Resource Group як окремий Concept | Open | Перевірити групове залучення після OCP-005 |
| AB-010 | Модель кількості, резервування і споживання Consumable Resource | Deferred | Після Assignment і Constraint; використовувати managed stock як гранулярність Resource |
| AB-011 | Взаємозамінність Resource | Open | Описати взаємозамінність без втрати ідентичності екземплярів після Capability і Constraint |
| AB-012 | Автоматична перевірка нормативних Concept references | Planned | PR-0006: початковий checker; розширити до повного ontology linter до першої Canonical promotion |
| AB-013 | Машинозчитувані інваріанти | Planned | PR-0006: fixtures для lifecycle, двосторонніх field constraints і accepted counterexamples |
| AB-014 | Operational Intent як окремий Concept | Open | Перевірити після Objective Concept |
| AB-015 | Мінімальна повнота Operation | Open | Формалізувати domain validation rules для переходу Draft → Planned |
| AB-016 | Композиція Operation | Open | Визначити правила parent/child, ациклічність і межу з незалежною координацією |
| AB-017 | Авторизація Operation | Open | Визначити джерела авторизації без передчасного введення Authority, Approval або Policy |
| AB-018 | Conflict між Operation як факт або похідний результат | Open | Визначити межу між Constraint violation, агрегованим finding і Conflict Concept |
| AB-019 | Suspended у lifecycle Operation | Deferred | Переглянути після Constraint, Assignment і State |
| AB-020 | Operation Template як окремий Concept | Open | Перевірити після стабілізації Operation lifecycle і повторюваних Operation |
| AB-021 | Формальна derivation участі через Assignment | Resolved | Нормативне визначення в OCP-005 §§8–9; подальші зміни лише у defining document |
| AB-022 | Validation contract для explicit intent | Open | Визначити спільні Core-вимоги та domain validation rules |
| AB-023 | Provenance taxonomy для lifecycle і relationship records | Open | Уточнити після Event, Order і Coordination Concept |
| AB-024 | Автоматична синхронізація Concept status | Planned | PR-0006 має звіряти OCP-000, OCP-002 і Concept-Status; choreography визначена OCP-001 |
| AB-025 | Reservation / Allocation як окремий Concept | Open | Визначити межу з Assignment і Constraint |
| AB-026 | Amendment model для Assignment | Open | Визначити зміни role та applicability після Establishment без переписування історії |
| AB-027 | Role Taxonomy | Open | Визначити межу Core role codes і domain role namespaces |
| AB-028 | Узгодження lifecycle Operation та Assignment | Open | Визначити правила для незавершених Assignment при Completed, Cancelled або Aborted Operation після Constraint |
| AB-029 | Кілька applicability intervals в Assignment | Open | Вирішити: один Assignment з кількома інтервалами чи окремий Assignment на інтервал |
| AB-030 | Масове створення Assignment | Open | Визначити механізм для груп Resource без неявного успадкування участі |
| AB-031 | Lifecycle record consistency | Resolved for Assignment | OCP-005 використовує authoritative linear transition history; поширити патерн на Operation у межах AB-028 |
| AB-032 | Canonical rule reference integrity | Resolved as governance rule | OCP-001 вимагає єдине defining location; автоматичну перевірку включити до AB-012 |
| AB-033 | Захист гілки main | Planned | Налаштувати GitHub Ruleset: PR required, direct/force push і deletion заборонені, enforcement для адміністраторів |
| AB-034 | Constraint Concept | Draft | PR-0005 / OCP-006: виправити accepted review findings; після ready-for-review змінити Concept status на Under Review |
| AB-035 | Constraint expression language | Deferred | Після review OCP-006 вибрати machine-readable predicate та selector representation |
| AB-036 | Constraint precedence, override and waiver | Open | Визначити порядок застосування, exception semantics і provenance без передчасного Policy Concept |
| AB-037 | Quantity, demand and capacity model | Open | Визначити units, aggregation та capacity consumption для quantitative Constraint |
| AB-038 | Conflict derivation model | Open | Визначити, коли одне чи більше Constraint violation створюють збережений або похідний Conflict |
| AB-039 | Constraint evaluation freshness and replay | Open | Визначити строк актуальності dynamic evaluation, snapshot contract і deterministic replay |
| AB-040 | Executable ontology checker | Planned | PR-0006 одразу після Constraint: YAML fixtures, reference derivations, review counterexamples і initial CI |
