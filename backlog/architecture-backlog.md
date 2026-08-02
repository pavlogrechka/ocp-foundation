# Architecture Backlog

| ID | Тема | Статус | Наступна дія |
|---|---|---|---|
| AB-001 | Operational Situation як окремий Concept | Open | Перевірити після базових Concept |
| AB-002 | Order як фундаментальний Concept | Open | Визначити, чи є Order обов’язковим або одним із можливих джерел авторизації Operation |
| AB-003 | Погодження між незалежними вертикалями | Open | Включити до Coordination Model |
| AB-004 | Capability Registry | Open | Визначити межі Core і Capability |
| AB-005 | Risk Taxonomy | Open | Після Constraint |
| AB-006 | Межа Organization / Resource | Open | Уточнити після Organization Concept; перевірити модель Organizational Resource |
| AB-007 | State як Concept | Deferred | Після Operation та Assignment |
| AB-008 | Межа Infrastructure Resource / Environment | Open | Перевірити на Position Site, Launch Site і Relay Site |
| AB-009 | Resource Group як окремий Concept | Open | Перевірити після Assignment Concept |
| AB-010 | Модель кількості, резервування і споживання Consumable Resource | Deferred | Після Assignment і Constraint; використовувати managed stock як гранулярність Resource |
| AB-011 | Взаємозамінність Resource | Open | Описати взаємозамінність без втрати ідентичності екземплярів після Capability і Constraint |
| AB-012 | Автоматична перевірка нормативних Concept references | Planned | Додати ontology linter до переходу перших документів у Canonical |
| AB-013 | Машинозчитувані інваріанти | Planned | Визначити формат після стабілізації schemas; заборонити квантифікацію невизначених або суто похідних зв’язків |
| AB-014 | Operational Intent як окремий Concept | Open | Перевірити після Objective Concept |
| AB-015 | Мінімальна повнота Operation | Open | Формалізувати domain validation rules для переходу Draft → Planned |
| AB-016 | Композиція Operation | Open | Визначити правила parent/child, ациклічність і межу з незалежною координацією |
| AB-017 | Авторизація Operation | Open | Визначити джерела авторизації без передчасного введення Authority, Approval або Policy |
| AB-018 | Conflict між Operation як факт або похідний результат | Open | Уточнити в Coordination Model і Conflict Engine |
| AB-019 | Suspended у lifecycle Operation | Deferred | Переглянути після Assignment і State |
| AB-020 | Operation Template як окремий Concept | Open | Перевірити після стабілізації Operation lifecycle і повторюваних Operation |
| AB-021 | Формальна derivation участі через Assignment | Planned | Визначити в OCP-005 кардинальність, чинність і часову семантику derived_participates_in |
| AB-022 | Validation contract для explicit intent | Open | Визначити спільні Core-вимоги та domain validation rules |
| AB-023 | Provenance taxonomy для lifecycle і relationship records | Open | Уточнити після Event, Order і Coordination Concept |
| AB-024 | Автоматична синхронізація Concept status | Planned | Linter має звіряти OCP-000, OCP-002 і Concept-Status у defining document |
