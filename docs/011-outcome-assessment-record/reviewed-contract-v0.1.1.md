---
Document-ID: OCP-011
Title: Outcome Assessment Record Contract
Version: 0.1.1
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-004, OCP-006, OCP-008, OCP-010, AD-006, P-001
Uses-Patterns: P-001@0.1.0
Used-By: Objective Achievement, Operation Outcome Views, Capability Claim Evidence, Coordination, Audit
Last-Review: 2026-08-04
---

# OCP-011 — Outcome Assessment Record Contract

## 1. Definition

**OutcomeAssessmentRecord** — ідентифікований attributable record, який фіксує оцінку одного exact target за одним exact criterion або rule на підставі exact evidence snapshot та exact input snapshot, із визначеним evaluator, evaluation time, recording time і provenance.

OutcomeAssessmentRecord реалізує outcome `R3` рішення AD-006C.

Він не є фундаментальним Concept `Result`, не представляє realized outcome як окрему універсальну identity і не є полем успіху Operation.

## 2. Purpose

Контракт потрібний для того, щоб assessment semantics не розчинялися у:

- lifecycle stage Operation;
- mutable achievement status Objective;
- Event або ObservationRecord;
- Constraint evaluation result;
- human-readable success label;
- newest record або list order;
- неатрибутованому derived field.

OutcomeAssessmentRecord дозволяє зберігати provisional, partial, conflicting, corrected і superseding assessments без переписування історії та без автоматичного перетворення оцінки на істину про реальний світ.

## 3. Ontological boundary

OutcomeAssessmentRecord є governed identified record за P-001, але не фундаментальним Concept.

Він не є автоматично:

- realized outcome або Event occurrence;
- ObservationRecord;
- Objective identity або authoritative mutable Objective state;
- Operation lifecycle stage, completion record, success або failure;
- Constraint evaluation record чи універсальний Constraint result;
- Conflict, Risk, State або Readiness;
- Capability definition або holder-specific Capability claim;
- authorization, approval, admissibility, certification або qualification;
- causal conclusion;
- aggregation of child або supporting Operations;
- current truth selected за timestamp, storage order або evaluator count.

## 4. Initial target contract

Revision `0.1.0` дозволяє один target kind:

```text
objective@1
```

Target binding складається з:

```text
target_kind_ref
target_ref
```

Для `objective@1`, `target_ref` exact-resolves рівно в один governed Objective identity.

Operation не є прямим assessment target у цій ревізії. Operation outcome view може показувати assessments пов'язаних Objectives, але не collapse-ить їх в один Operation success status.

Додавання нового target kind потребує окремого normative review, визначеного endpoint authority та executable ambiguity counterexamples.

## 5. Minimal structure

```text
OutcomeAssessmentRecord
- assessment_id
- assessment_kind_ref
- target_kind_ref
- target_ref
- criterion_ref
- evidence_bindings[]
  - evidence_kind_ref
  - evidence_ref
- evidence_snapshot_ref
- input_snapshot_ref
- evidence_state
- evaluator_ref
- evaluated_at
- recorded_at
- conclusion
- provenance_ref
- supersedes_assessment_ref [optional]
```

## 6. Field semantics

### 6.1 assessment_id

Стабільна непорожня identity attributable assessment record. Вона унікальна в assessment dataset.

Однакові target, criterion, snapshots, evaluator або timestamps не створюють identity equality.

### 6.2 assessment_kind_ref

Governed exact-version reference на вид assessment. Початковий checker envelope використовує `objective-achievement@1`.

Assessment kind не замінює criterion і не визначає conclusion автоматично.

### 6.3 target_kind_ref and target_ref

Exact endpoint contract оцінюваного об'єкта. У цій ревізії дозволено лише Objective.

Unresolved або ambiguous target не може отримати authoritative assessment.

### 6.4 criterion_ref

Exact-version reference на criterion або evaluation rule, за яким інтерпретується evidence.

Criterion identity не виводиться з label, evaluator, target type або попереднього assessment.

OCP-011 не визначає expression language criterion. Domain або інший normative owner визначає зміст rule, але record завжди зберігає exact reference.

### 6.5 evidence_bindings

Кожен evidence binding містить:

```text
evidence_kind_ref
evidence_ref
```

Початково підтримуються:

```text
observation-record@1
 event@1
```

`observation-record@1` exact-resolves ObservationRecord з OCP-010. `event@1` exact-resolves Event occurrence identity.

Evidence binding не означає, що evidence є істинним, достатнім або позитивним. Authority такої інтерпретації належить assessment criterion та evaluator.

Duplicate exact bindings у одному record заборонені. List order не має нормативного значення.

### 6.6 evidence_snapshot_ref

Exact reference на immutable evidence snapshot, який перелічує той самий normalized binding set, що й record.

Snapshot mismatch, absence або unresolved snapshot робить assessment неавторитетним.

Late evidence не дописується до існуючого snapshot. Воно створює новий snapshot і новий assessment record або explicit successor.

### 6.7 input_snapshot_ref

Exact reference на immutable input snapshot для criterion execution або human evaluation context.

Input snapshot може включати governed parameters, contextual selections або rule inputs, але OCP-011 не визначає їх wire schema.

Відсутній або unresolved input snapshot не може бути замінений поточним станом системи під час replay.

### 6.8 evidence_state

Початковий governed vocabulary:

```text
sufficient
missing
stale
ambiguous
conflicting
```

`evidence_state` є attributable assessment assertion, а не властивістю самих Event або ObservationRecord.

Reference checker додатково виявляє очевидне disagreement між bound ObservationRecord statements як finite defense-in-depth probe. Ця перевірка не є універсальним truth або semantic-conflict engine.

### 6.9 evaluator_ref

Непорожня attributable identity evaluator. OCP-011 не робить evaluator автоматично authorized, qualified або correct.

Evaluator authorization і qualification належать окремим policies або Constraints.

### 6.10 evaluated_at and recorded_at

`evaluated_at` — час виконання оцінки.

`recorded_at` — час створення attributable record.

Якщо обидва timestamps подані точно:

```text
evaluated_at <= recorded_at
```

Вони відрізняються від Event `occurred_at`, ObservationRecord `observed_at`/`recorded_at`, Operation lifecycle time та evidence snapshot creation time.

### 6.11 conclusion

Початковий vocabulary:

```text
achieved
not_achieved
partially_achieved
indeterminate
```

Conclusion належить одному exact assessment binding. Він не є універсальним Result status.

`partially_achieved` не визначає percentage, weighting або aggregation. Такі semantics потребують окремого criterion contract.

### 6.12 provenance_ref

Непорожній opaque reference на act, process або source, що створив assessment record.

### 6.13 supersedes_assessment_ref

Optional exact reference на prior OutcomeAssessmentRecord у тій самій binding identity:

```text
assessment_kind_ref
target_kind_ref
target_ref
criterion_ref
```

Supersession не може змінити target або criterion під виглядом correction. Зміна binding identity створює незалежну assessment lineage.

## 7. Evidence-state and conclusion matrix

Fail-safe baseline:

| Evidence state | Allowed authoritative conclusion baseline |
|---|---|
| `sufficient` | criterion може підтримати `achieved`, `not_achieved`, `partially_achieved` або `indeterminate` |
| `missing` | лише `indeterminate` |
| `stale` | лише `indeterminate` |
| `ambiguous` | лише `indeterminate` |
| `conflicting` | лише `indeterminate` |

Відсутність негативного evidence не означає positive achievement.

Наявність одного Event або одного ObservationRecord не означає sufficient evidence автоматично.

Domain criterion може бути суворішим за цю матрицю, але не permissive-нішим без окремого reviewed normative owner.

## 8. Authority declaration

OutcomeAssessmentRecord authoritative лише щодо такого твердження:

> визначений evaluator у визначений час застосував визначений criterion до exact target, exact evidence snapshot та exact input snapshot і зафіксував визначені evidence state та conclusion з визначеною provenance.

Record не є authoritative щодо:

- occurrence truth;
- correctness або reliability evidence source;
- causal relation;
- current Objective state поза exact assessment binding;
- Operation success або lifecycle;
- Capability, Readiness, authorization, admissibility, Conflict, Risk чи State.

## 9. Exact assessment resolution

```text
resolve_outcome_assessment(assessments, assessment_ref)
```

Resolver повертає рівно один structurally valid record за exact `assessment_id`.

Zero або multiple candidates fail closed. Resolver не використовує newest timestamp, evaluator rank, conclusion або storage order як tie-break.

## 10. Supersession heads

```text
outcome_assessment_heads(
    assessments,
    target_kind_ref,
    target_ref,
    criterion_ref
)
```

Derivation повертає unsuperseded records exact binding lineage.

Branching дозволений. Кілька heads не collapse-яться автоматично.

Head не означає truth, current authority або preferred evaluator. Це лише graph position за explicit supersession references.

## 11. Effective conclusion projection

```text
effective_outcome_conclusion(
    assessments,
    target_kind_ref,
    target_ref,
    criterion_ref
)
```

Reference projection повертає definitive conclusion лише коли unsuperseded exact-bound head set має:

1. один exact evidence snapshot binding;
2. один exact input snapshot binding;
3. одну conclusion value.

Якщо heads відсутні, projection повертає no conclusion. Якщо heads disagree або мають різні snapshots, projection повертає `indeterminate`.

Projection не обирає newest assessment і не замінює attributable records.

## 12. P-001 conformance

OCP-011 invokes `P-001@0.1.0`.

### 12.1 Required Elements

- stable record identity: `assessment_id`;
- owning semantic specification: OCP-011;
- endpoint contract: `target_kind_ref + target_ref`, початково лише Objective;
- governed kind: `assessment_kind_ref`;
- provenance: `evaluator_ref`, `evaluated_at`, `recorded_at`, `provenance_ref`;
- validation: §§15–16 та executable fixtures;
- authority: §8.

### 12.2 Selected Module C — Supersession

- superseded reference: `supersedes_assessment_ref`;
- self-supersession: prohibited;
- target existence: required;
- graph acyclicity: required;
- branching: allowed;
- overlap and gaps: allowed;
- authoritative record during overlap: none selected automatically;
- replacement provenance: successor `provenance_ref` plus evaluator/timestamps;
- binding identity change: prohibited within one supersession edge;
- prior history: retained and exact-resolvable.

Modules A and B are not selected. Evaluation timestamps do not create record effectivity or lifecycle.

## 13. Objective and Operation boundary

Objective does not gain an authoritative mutable `achievement_status` field.

One Objective may have multiple assessments under different criteria or snapshots. Several Operations may contribute evidence without becoming assessment identity.

One Operation may pursue multiple Objectives with different conclusions. A completed Operation may have `not_achieved`, `partially_achieved` або `indeterminate` assessments.

Assessment conclusion does not change Operation lifecycle. `Completed` does not force `achieved`.

Child, parent, supporting або parallel Operation assessments do not aggregate automatically.

## 14. Event, Observation and Constraint boundary

Event occurrence та ObservationRecord можуть бути evidence bindings, але не є assessment.

Conflicting observations remain visible in their own records. OutcomeAssessmentRecord records how an evaluator handled the exact evidence set; it does not rewrite observations or Event identity.

Constraint evaluation result may be included in a future evidence kind only after an explicit binding contract. This revision does not reclassify Constraint output as universal Result.

Constraint violation does not create Conflict, Risk або OutcomeAssessmentRecord automatically.

## 15. Semantic rules

1. Assessment identity is exact `assessment_id`.
2. Assessment authority is determined by exact target, criterion, evidence snapshot, input snapshot, evaluator and time bindings.
3. Record order, newest timestamp and evaluator count do not select authority.
4. Missing, stale, ambiguous or conflicting evidence cannot yield an authoritative definitive conclusion by default.
5. Reference checker mechanically derives and cross-checks `missing` and its finite `conflicting` probe from governed bindings; until AB-039 accepts freshness and replay semantics, truth of `stale` and `ambiguous` remains attributable evaluator responsibility, and declared `sufficient` is not proof that evidence is current or unambiguous.
6. Late evidence creates a new immutable snapshot and new record; prior record is not mutated.
7. Supersession preserves history and may branch.
8. Supersession cannot silently change target or criterion binding identity.
9. Conflicting heads remain visible and project to `indeterminate` unless explicitly reconciled by a new reviewed record lineage.
10. Operation completion and assessment conclusion are independent.
11. Assessment does not create Capability, Readiness, authorization, admissibility, Conflict, Risk або State.
12. No universal fundamental Result Concept is introduced.

## 16. Invariants

1. Every record has a non-empty unique `assessment_id`.
2. `assessment_kind_ref`, `target_kind_ref` and `criterion_ref` are governed exact-version references.
3. Initial `target_kind_ref` is `objective@1`, and `target_ref` exact-resolves one Objective.
4. Every evidence binding has a supported exact kind and non-empty exact reference.
5. Evidence bindings are unique as normalized `(kind, ref)` pairs.
6. Every evidence reference exact-resolves in the governed dataset.
7. `evidence_snapshot_ref` resolves and contains exactly the normalized evidence binding set.
8. `input_snapshot_ref` resolves to the exact evaluation input snapshot.
9. `evidence_state` and `conclusion` belong to governed vocabularies.
10. Missing, stale, ambiguous or conflicting evidence permits only `indeterminate` under the baseline contract.
11. `evaluator_ref`, `evaluated_at`, `recorded_at` and `provenance_ref` are present.
12. `evaluated_at <= recorded_at` when both are precise.
13. Self-supersession is prohibited; target exists; graph is acyclic.
14. A supersession edge preserves assessment kind, target and criterion binding identity.
15. Result, lifecycle-success, Objective status, Capability, Readiness, authorization, Conflict, Risk and State convenience fields are forbidden in the record.
16. Exact-bound unsuperseded disagreement cannot project a definitive conclusion.

## 17. Executable evidence

Reference implementation includes:

- missing evidence with `indeterminate`;
- conflicting observations with `indeterminate`;
- stale evidence attempting a definitive conclusion and failing closed;
- unresolved target and evidence references;
- evidence snapshot mismatch;
- late evidence creating a successor record while preserving prior exact resolution;
- supersession cycle;
- supersession binding-identity change;
- multiple unsuperseded assessments that disagree without order-based selection;
- forbidden Result and Operation lifecycle coupling;
- the integrated OCP-010 scenario migrated from checker-local envelope to OutcomeAssessmentRecord.

Assessment codes and derivations are covered by `assessment-rules.yaml` with exact manifest equality, following the existing module-manifest precedent.

## 18. Integrated non-sensitive scenario

The accepted PR-0012 scenario remains structurally unchanged on the occurrence axis:

```text
Objective
→ Completed Operation
→ Resource + Assignment participation
→ applicable Constraint
→ Event
→ conflicting ObservationRecords
```

OCP-011 replaces only the temporary checker-local assessment envelope with a governed OutcomeAssessmentRecord:

```text
exact Objective target
+ exact criterion
+ exact evidence snapshot
+ exact input snapshot
+ attributable evaluator
+ evidence_state: conflicting
+ conclusion: indeterminate
```

The scenario continues to prove `Completed ≠ achieved` and uses the accepted derivations `derived_participates_in`, `constraint_applicable_to` and `effective_constraint_result` for its cross-Concept joints.

## 19. Result registry migration

AD-006C gave a negative independent-identity verdict for a fundamental Result Concept.

During OCP-011 external review, the historical registry entry remains:

```text
Result | Proposed
```

This temporary state is migration accounting, not an endorsement of Result as a future Concept.

The Architecture Board acceptance act for OCP-011 must atomically:

1. accept the OutcomeAssessmentRecord R3 contract;
2. resolve AB-056;
3. remove `Result` from the active Concept registry in OCP-000;
4. remove Result from generated Concept projections;
5. record in ontology/taxonomy prose that the fundamental Result candidate was rejected by AD-006C and replaced by the governed record contract;
6. avoid introducing `Result: Accepted`, `Result: Deprecated` or any defining Concept document.

Until that atomic act, OCP-011 does not claim registry resolution.

## 20. Explicitly not defined

OCP-011 does not define:

- a fundamental Result Concept or realized-outcome identity;
- canonical criterion expression language;
- universal evaluator authorization or qualification;
- confidence, probability, trust or source-reliability scale;
- percentage or weighted partial achievement;
- automatic multi-Objective, multi-Operation or parent/child aggregation;
- automatic Operation success/failure;
- Constraint-result evidence kind;
- Conflict, Risk, State or Readiness;
- Capability Claim evidence sufficiency;
- authorization, approval or admissibility;
- canonical time or uncertainty representation;
- cryptographic evidence or non-repudiation;
- database, API, UI, transport or persistence schema.

## 21. Open questions

- Який normative owner визначить additional target kinds beyond Objective?
- Чи потрібен окремий governed criterion registry?
- Які exact evidence kinds слід додати для Constraint evaluation та future Capability Claim?
- Чи потрібний explicit reconciliation record для conflicting assessment heads, чи достатньо нового superseding assessment?
- Які domain contracts можуть визначати quantitative partial achievement без Core weighting model?

## 22. External review target

Attempt to falsify OCP-011 with cases where:

1. OutcomeAssessmentRecord silently becomes a fundamental Result Concept;
2. Operation completion or lifecycle fields manufacture achievement;
3. Objective gains mutable authoritative achievement state;
4. target, criterion, evidence or input snapshot binding is implicit, latest-selected or unresolved;
5. missing, stale, ambiguous or conflicting evidence produces a definitive positive conclusion;
6. late evidence rewrites historical record or snapshot;
7. supersession changes target/criterion identity;
8. branching or conflicting heads are resolved by timestamp, evaluator count or list order;
9. Event or ObservationRecord is treated as assessment truth automatically;
10. Constraint evaluation becomes universal Result by relabeling;
11. P-001 endpoint, authority, provenance, validation or Module C obligations are incomplete;
12. the integrated scenario loses its loaded derivation joints;
13. `Result: Proposed` is removed before the Board acceptance act or promoted instead of removed.

## 23. Architecture Board status

Revision `0.1.0` opened OCP-011 and AB-056 as `Under Review`.

Revision `0.1.1` resolves external Finding 1 by making the checker trust boundary for self-declared `stale` and `ambiguous` states explicit; the document remains `Draft`, AB-056 remains `Under Review`, and `Result: Proposed` remains unchanged pending repeated external verification and a separate atomic acceptance act.

No Architecture Board acceptance is recorded by this revision. OutcomeAssessmentRecord remains a proposed governed record contract, and the temporary `Result: Proposed` registry entry remains unchanged pending external adversarial review and a separate atomic acceptance act.
