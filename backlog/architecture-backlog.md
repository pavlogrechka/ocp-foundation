# Architecture Backlog

| ID | Тема | Статус | Наступна дія |
|---|---|---|---|
| AB-001 | Operational Situation як окремий Concept | Open | Перевірити після базових Concept |
| AB-002 | Order як фундаментальний Concept | Open | Визначити, чи є Order обов’язковим або одним із можливих джерел авторизації Operation |
| AB-003 | Погодження між незалежними вертикалями | Open | Включити до Coordination Model |
| AB-004 | Capability Registry | Open | Визначити межі Core і Capability |
| AB-005 | Risk Taxonomy | Open | Після Constraint |
| AB-006 | Межа Organization / Resource | Open | Уточнити після Organization Concept; перевірити модель Organizational Resource |
| AB-007 | State як Concept | Deferred | Переглянути ADR-DRAFT-007 після Constraint та стабілізації Accepted Operation і Assignment |
| AB-008 | Межа Infrastructure Resource / Environment | Open | Перевірити на Position Site, Launch Site і Relay Site |
| AB-009 | Resource Group як окремий Concept | Open | Перевірити групове залучення після OCP-005 |
| AB-010 | Модель кількості, резервування і споживання Consumable Resource | Deferred | Після Assignment і Constraint; використовувати managed stock як гранулярність Resource |
| AB-011 | Взаємозамінність Resource | Open | Описати взаємозамінність без втрати ідентичності екземплярів після Capability і Constraint |
| AB-012 | Автоматична перевірка нормативних Concept references | Planned | Додати ontology linter до переходу перших документів у Canonical |
| AB-013 | Машинозчитувані інваріанти | Planned | Визначити формат після стабілізації schemas; перевіряти двосторонні field constraints і authoritative records |
| AB-014 | Operational Intent як окремий Concept | Open | Перевірити після Objective Concept |
| AB-015 | Мінімальна повнота Operation | Open | Формалізувати domain validation rules для переходу Draft → Planned |
| AB-016 | Композиція Operation | Open | Визначити правила parent/child, ациклічність і межу з незалежною координацією |
| AB-017 | Авторизація Operation | Open | Визначити джерела авторизації без передчасного введення Authority, Approval або Policy |
| AB-018 | Conflict між Operation як факт або похідний результат | Open | Уточнити в Coordination Model і Conflict Engine |
| AB-019 | Suspended у lifecycle Operation | Deferred | Переглянути після Constraint, Assignment і State |
| AB-020 | Operation Template як окремий Concept | Open | Перевірити після стабілізації Operation lifecycle і повторюваних Operation |
| AB-021 | Формальна derivation участі через Assignment | Resolved | Нормативне визначення в OCP-005 §§8–9; подальші зміни лише у defining document |
| AB-022 | Validation contract для explicit intent | Open | Визначити спільні Core-вимоги та domain validation rules |
| AB-023 | Provenance taxonomy для lifecycle і relationship records | Open | Уточнити після Event, Order і Coordination Concept |
| AB-024 | Автоматична синхронізація Concept status | Planned | Linter має звіряти OCP-000, OCP-002 і Concept-Status у defining document |
| AB-025 | Reservation / Allocation як окремий Concept | Open | Визначити межу з Assignment і Constraint |
| AB-026 | Amendment model для Assignment | Open | Визначити зміни role та applicability після Establishment без переписування історії |
| AB-027 | Role Taxonomy | Open | Визначити межу Core role codes і domain role namespaces |
| AB-028 | Узгодження lifecycle Operation та Assignment | Open | Визначити правила для незавершених Assignment при Completed, Cancelled або Aborted Operation після Constraint |
| AB-029 | Кілька applicability intervals в Assignment | Open | Вирішити: один Assignment з кількома інтервалами чи окремий Assignment на інтервал |
| AB-030 | Масове створення Assignment | Open | Визначити механізм для груп Resource без неявного успадкування участі |
| AB-031 | Lifecycle record consistency | Under Review | PR-0004A: transition history як source of truth, linear path, двостороння узгодженість stage і timestamps для Assignment; поширити патерн на Operation |
| AB-032 | Canonical rule reference integrity | Under Review | PR-0004A прибирає копії derivation з OCP-003/OCP-004; ontology linter має виявляти незалежні дублікати нормативних правил |
| AB-033 | Захист гілки main | Planned | Налаштувати GitHub Ruleset: PR required, direct/force push і deletion заборонені, enforcement для адміністраторів |
| AB-034 | Constraint Concept | Planned | Наступний Concept cycle PR-0005; визначити conflict, exclusivity, capacity, multiple roles та replacement overlap/gap до перегляду ADR-DRAFT-007 |
