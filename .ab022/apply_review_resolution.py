from __future__ import annotations

import copy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"expected one match in {path}, found {count}: {old[:80]!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


# OCP-004: remove wire encoding from the normative model.
replace_once(
    "docs/004-operation-concept/README.md",
    "`intent_version_ref` та `validation_rule_ref` є exact-version references і повинні містити непорожню identity та version, розділені символом `@`. `input_snapshot_ref` непрозоро ідентифікує точний evaluated input snapshot.",
    "`intent_version_ref` та `validation_rule_ref` є непрозорими exact-version references. Кожне посилання повинно однозначно розрізняти identity та immutable version; нормативна модель не приписує delimiter або wire encoding. `input_snapshot_ref` непрозоро ідентифікує точний evaluated input snapshot.",
)

replace_once(
    "docs/004-operation-concept/README.md",
    """Для використання explicit intent поза `Draft` має існувати рівно один структурно валідний validation record, який одночасно збігається з поточними:

1. `intent_version_ref`;
2. exact-version `validation_rule_ref`;
3. `input_snapshot_ref`.

Цей record також повинен містити валідні `validation_id`, `evaluated_at`, `evaluator_ref` і єдиний `result = passed`.

Будь-яка substantive зміна `ExplicitIntentRecord`, версії validation rule або evaluated input snapshot створює нове binding-значення та інвалідовує попередній `passed`. Missing, stale, conflicting або structurally invalid evidence не задовольняє intent invariant і fail-safe робить non-Draft Operation невалідною.

`validation_status`, якщо матеріалізований, є лише derived non-authoritative projection ефективного validation record. Він повинен дорівнювати авторитетному `result`; stored `passed` без точного evidence binding або всупереч evidence не має нормативної сили.""",
    """Для використання explicit intent поза `Draft` має існувати один або більше структурно валідних validation records, які одночасно збігаються з поточними:

1. `intent_version_ref`;
2. exact-version `validation_rule_ref`;
3. `input_snapshot_ref`.

Усі records із цим exact binding утворюють effective evidence set. Evidence є однозначним, якщо всі exact-binding records мають один і той самий `result`. Повторні immutable records з однаковим result є допустимими; порядок списку та `evaluated_at` не обирають авторитетний record. Якщо exact-binding records містять різні results, evidence є conflicting.

Кожен record повинен містити валідні `validation_id`, `evaluated_at`, `evaluator_ref` і `result`. Non-Draft explicit-intent branch є валідною лише тоді, коли effective evidence set дає один однозначний `result = passed`.

`intent_version_ref` позначає immutable version усього binding-relevant змісту explicit intent, включно зі `statement`. Будь-яка substantive зміна statement або іншої binding-властивості, версії validation rule чи evaluated input snapshot повинна створювати нову version/reference value та інвалідовує попередній `passed`. Повторне використання старого version token після зміни змісту порушує цю semantic rule незалежно від того, чи здатний reference checker виявити таке зловживання.

Missing, stale, conflicting або structurally invalid evidence не задовольняє intent invariant і fail-safe робить non-Draft Operation невалідною.

`validation_status`, якщо матеріалізований, є лише derived non-authoritative projection. Якщо effective evidence set має один однозначний result, projection повинна дорівнювати цьому result. Якщо однозначного effective result немає через missing, stale, conflicting або structurally invalid evidence, нормативна projection дорівнює `not_evaluated`; матеріалізований `passed` або `failed` є mismatch. Stored `passed` без точного evidence binding або всупереч evidence не має нормативної сили.""",
)

replace_once(
    "docs/004-operation-concept/README.md",
    """7. Explicit intent може використовуватися поза `Draft` лише коли рівно один authoritative validation record має exact binding до поточних intent version, validation rule version та input snapshot і містить `result = passed`.
8. Missing, stale, conflicting або structurally invalid explicit-intent evidence fail-safe не задовольняє intent invariant; mutable `validation_status` не може зробити Operation більш permissive.""",
    """7. Explicit intent може використовуватися поза `Draft` лише коли один або більше authoritative validation records мають exact binding до поточних intent version, validation rule version та input snapshot, усі дають один однозначний result і цей result дорівнює `passed`.
8. Missing, stale, conflicting або structurally invalid explicit-intent evidence fail-safe не задовольняє intent invariant; за відсутності однозначного effective result нормативна projection дорівнює `not_evaluated`, а mutable `validation_status` не може зробити Operation більш permissive.""",
)

replace_once(
    "docs/004-operation-concept/README.md",
    """13. Plural `objective_refs` не кодує alternative pursuit, priority, sequence, hierarchy, contribution strength або achievement aggregation.
14. `validation_status` є derived projection і не є авторитетним доказом без exact-binding validation record.""",
    """13. Plural `objective_refs` не кодує alternative pursuit, priority, sequence, hierarchy, contribution strength або achievement aggregation.
14. `validation_status` є derived projection: вона дорівнює однозначному effective result або `not_evaluated`, якщо такого result немає; projection не є авторитетним доказом і не може зробити Operation більш permissive.
15. `intent_version_ref` позначає immutable version усього binding-relevant змісту explicit intent; substantive зміна, включно зі зміною `statement`, вимагає нової version/reference value.""",
)

replace_once(
    "docs/004-operation-concept/README.md",
    """4. Non-Draft `ExplicitIntentRecord` містить непорожні `intent_id`, exact-version `intent_version_ref`, змістовний `statement`, exact-version `validation_rule_ref` і непорожній `input_snapshot_ref`.
5. Кожен validation record містить непорожній `validation_id`, exact `intent_version_ref`, exact `validation_rule_ref`, exact `input_snapshot_ref`, валідний `evaluated_at`, непорожній `evaluator_ref` і один result із `not_evaluated | passed | failed`.
6. Non-Draft explicit-intent branch є валідною лише коли існує рівно один structurally valid record, що точно збігається з поточними intent version, validation rule version та input snapshot і має `result = passed`.
7. Missing, stale, conflicting або structurally invalid explicit-intent evidence не задовольняє invariant 6 і fail-safe робить non-Draft Operation невалідною.
8. Матеріалізований `validation_status` є derived non-authoritative projection і дорівнює result єдиного ефективного validation record.""",
    """4. Non-Draft `ExplicitIntentRecord` містить непорожні `intent_id`, exact-version `intent_version_ref`, змістовний `statement`, exact-version `validation_rule_ref` і непорожній `input_snapshot_ref`; exact-version references однозначно розрізняють identity та immutable version без нормативно визначеного wire encoding.
5. Кожен validation record містить непорожній `validation_id`, exact `intent_version_ref`, exact `validation_rule_ref`, exact `input_snapshot_ref`, валідний `evaluated_at`, непорожній `evaluator_ref` і один result із `not_evaluated | passed | failed`.
6. Non-Draft explicit-intent branch є валідною лише коли один або більше structurally valid records точно збігаються з поточними intent version, validation rule version та input snapshot, усі exact-binding records мають один однозначний result і цей result дорівнює `passed`.
7. Missing, stale, conflicting або structurally invalid explicit-intent evidence не задовольняє invariant 6 і fail-safe робить non-Draft Operation невалідною.
8. Матеріалізований `validation_status` є derived non-authoritative projection: вона дорівнює однозначному effective result, а за його відсутності — `not_evaluated`; будь-яке інше матеріалізоване значення є mismatch.""",
)

# Validator: agreeing repeated evidence is valid; strict projection normalization applies in every no-result branch.
objective_path = ROOT / "tools/ontology_checker/ocp_checker/objective.py"
objective_text = objective_path.read_text(encoding="utf-8")
start = objective_text.index("def _validate_explicit_intent(intent: Any) -> list[str]:")
end = objective_text.index("\n\ndef _objective_index", start)
new_function = '''def _validate_explicit_intent(intent: Any) -> list[str]:
    if not isinstance(intent, dict):
        return ["OPERATION_EXPLICIT_INTENT_EVIDENCE_INVALID"]

    errors: list[str] = []
    top_level_valid = (
        _nonempty(intent.get("intent_id"))
        and _versioned_ref(intent.get("intent_version_ref"))
        and _has_alnum(intent.get("statement"))
        and _versioned_ref(intent.get("validation_rule_ref"))
        and _nonempty(intent.get("input_snapshot_ref"))
    )
    if not top_level_valid:
        errors.append("OPERATION_EXPLICIT_INTENT_EVIDENCE_INVALID")

    effective_result: str | None = None
    records = intent.get("validation_records")
    if not isinstance(records, list) or not records:
        errors.append("OPERATION_EXPLICIT_INTENT_EVIDENCE_MISSING")
    elif any(not _validation_record_valid(record) for record in records):
        errors.append("OPERATION_EXPLICIT_INTENT_EVIDENCE_INVALID")
    elif top_level_valid:
        exact = [
            record
            for record in records
            if record.get("intent_version_ref") == intent.get("intent_version_ref")
            and record.get("validation_rule_ref") == intent.get("validation_rule_ref")
            and record.get("input_snapshot_ref") == intent.get("input_snapshot_ref")
        ]
        if not exact:
            errors.append("OPERATION_EXPLICIT_INTENT_EVIDENCE_STALE")
        else:
            exact_results = {str(record["result"]) for record in exact}
            if len(exact_results) != 1:
                errors.append("OPERATION_EXPLICIT_INTENT_EVIDENCE_CONFLICT")
            else:
                effective_result = next(iter(exact_results))

    normative_projection = effective_result or "not_evaluated"
    if "validation_status" in intent and intent.get("validation_status") != normative_projection:
        errors.append("OPERATION_EXPLICIT_INTENT_STATUS_MISMATCH")
    if effective_result is not None and effective_result != "passed":
        errors.append("OPERATION_INTENT_REQUIRED")
    return errors
'''
objective_path.write_text(objective_text[:start] + new_function + objective_text[end:], encoding="utf-8")

# Unit tests: update strict-normalization expectations and add F1/F2 executable evidence.
test_path = ROOT / "tools/ontology_checker/tests/test_operation_intent_contract.py"
test_text = test_path.read_text(encoding="utf-8")ntest_text = test_text.replace(
    '{"OPERATION_EXPLICIT_INTENT_EVIDENCE_INVALID"},',
    '{"OPERATION_EXPLICIT_INTENT_EVIDENCE_INVALID", "OPERATION_EXPLICIT_INTENT_STATUS_MISMATCH"},',
    1,
)
test_text = test_text.replace(
    '{"OPERATION_EXPLICIT_INTENT_EVIDENCE_STALE"},',
    '{"OPERATION_EXPLICIT_INTENT_EVIDENCE_STALE", "OPERATION_EXPLICIT_INTENT_STATUS_MISMATCH"},',
    1,
)
marker = '''    def test_materialized_status_cannot_override_evidence(self) -> None:
'''
insert = '''    def test_agreeing_repeated_records_are_order_independent(self) -> None:
        fixture = valid_explicit_intent_fixture()
        records = fixture["entity"]["explicit_intent_record"]["validation_records"]
        repeated = copy.deepcopy(records[0])
        repeated.update(
            validation_id="INT-VAL-TEST-002",
            evaluated_at="2026-08-03T18:01:00Z",
            evaluator_ref="checker://intent-test-v2-repeat",
        )
        records.append(repeated)

        for ordered_records in (records, list(reversed(records))):
            with self.subTest(order=[record["validation_id"] for record in ordered_records]):
                candidate = copy.deepcopy(fixture)
                candidate["entity"]["explicit_intent_record"]["validation_records"] = copy.deepcopy(ordered_records)
                self.assertTrue(validate_reference_fixture(candidate).valid)

    def test_permissive_projection_cannot_override_failed_evidence(self) -> None:
        fixture = valid_explicit_intent_fixture()
        fixture["entity"]["explicit_intent_record"]["validation_records"][0]["result"] = "failed"
        self.assertEqual(
            set(validate_reference_fixture(fixture).errors),
            {"OPERATION_EXPLICIT_INTENT_STATUS_MISMATCH", "OPERATION_INTENT_REQUIRED"},
        )

'''
if marker not in test_text:
    raise RuntimeError("test insertion marker not found")
test_path.write_text(test_text.replace(marker, insert + marker, 1), encoding="utf-8")

# Existing fixtures become executable evidence for strict normalization.
for fixture_name, evidence_code in {
    "invalid-planned-explicit-intent-missing-evidence.yaml": "OPERATION_EXPLICIT_INTENT_EVIDENCE_MISSING",
    "invalid-planned-explicit-intent-stale-evidence.yaml": "OPERATION_EXPLICIT_INTENT_EVIDENCE_STALE",
    "invalid-planned-explicit-intent-conflicting-evidence.yaml": "OPERATION_EXPLICIT_INTENT_EVIDENCE_CONFLICT",
}.items():
    fixture_path = ROOT / "tools/ontology_checker/fixtures/operation" / fixture_name
    fixture_text = fixture_path.read_text(encoding="utf-8")
    needle = f"    - {evidence_code}\n"
    if fixture_text.count(needle) != 1:
        raise RuntimeError(f"fixture expectation marker not found exactly once: {fixture_name}")
    fixture_path.write_text(
        fixture_text.replace(
            needle,
            needle + "    - OPERATION_EXPLICIT_INTENT_STATUS_MISMATCH\n",
            1,
        ),
        encoding="utf-8",
    )

fixtures_dir = ROOT / "tools/ontology_checker/fixtures/operation"
(fixtures_dir / "valid-planned-explicit-intent-agreeing-repeat.yaml").write_text(
    """case_id: operation-valid-planned-explicit-intent-agreeing-repeat-001
concept: Operation
expected:
  valid: true
  error_codes: []
entity:
  operation_id: OP-INTENT-REPEAT-001
  lifecycle_stage: Planned
  explicit_intent_record:
    intent_id: INT-REPEAT-001
    intent_version_ref: INT-REPEAT-001@1
    statement: Preserve access to the transit corridor
    validation_rule_ref: RULE-INTENT-001@2
    input_snapshot_ref: SNAP-INTENT-REPEAT-001
    validation_status: passed
    validation_records:
      - validation_id: INT-VAL-REPEAT-001
        intent_version_ref: INT-REPEAT-001@1
        validation_rule_ref: RULE-INTENT-001@2
        input_snapshot_ref: SNAP-INTENT-REPEAT-001
        evaluated_at: 2026-08-03T18:00:00Z
        evaluator_ref: checker://intent-v2-a
        result: passed
      - validation_id: INT-VAL-REPEAT-002
        intent_version_ref: INT-REPEAT-001@1
        validation_rule_ref: RULE-INTENT-001@2
        input_snapshot_ref: SNAP-INTENT-REPEAT-001
        evaluated_at: 2026-08-03T18:01:00Z
        evaluator_ref: checker://intent-v2-b
        result: passed
""",
    encoding="utf-8",
)
(fixtures_dir / "invalid-planned-explicit-intent-permissive-projection.yaml").write_text(
    """case_id: operation-invalid-planned-explicit-intent-permissive-projection-001
concept: Operation
expected:
  valid: false
  error_codes:
    - OPERATION_EXPLICIT_INTENT_STATUS_MISMATCH
    - OPERATION_INTENT_REQUIRED
entity:
  operation_id: OP-INTENT-PERMISSIVE-001
  lifecycle_stage: Planned
  explicit_intent_record:
    intent_id: INT-PERMISSIVE-001
    intent_version_ref: INT-PERMISSIVE-001@1
    statement: Preserve access to the transit corridor
    validation_rule_ref: RULE-INTENT-001@2
    input_snapshot_ref: SNAP-INTENT-PERMISSIVE-001
    validation_status: passed
    validation_records:
      - validation_id: INT-VAL-PERMISSIVE-001
        intent_version_ref: INT-PERMISSIVE-001@1
        validation_rule_ref: RULE-INTENT-001@2
        input_snapshot_ref: SNAP-INTENT-PERMISSIVE-001
        evaluated_at: 2026-08-03T18:00:00Z
        evaluator_ref: checker://intent-v2
        result: failed
""",
    encoding="utf-8",
)

# Checker README owns the harness-specific serialization and implementation limit.
replace_once(
    "tools/ontology_checker/README.md",
    "- Operation: identity and the accepted non-Draft intent gate subset;",
    "- Operation: identity, plural Objective resolution, and the accepted non-Draft explicit-intent exact-binding evidence contract;",
)
replace_once(
    "tools/ontology_checker/README.md",
    "## Materialized projections\n",
    """## Operation explicit-intent evidence envelope

OCP-004 treats `intent_version_ref` and `validation_rule_ref` as opaque references that distinguish identity and immutable version. The reference fixture harness serializes those references as `identity@version`; the `@` delimiter is checker-envelope syntax, not a normative OCP-004 wire format.

The checker selects explicit-intent evidence by exact string equality across `intent_version_ref`, `validation_rule_ref`, and `input_snapshot_ref`. Multiple exact-binding immutable records are permitted when all results agree. List order and `evaluated_at` never break a tie or select an authoritative record; divergent exact-binding results are conflicting.

The harness trusts `intent_version_ref` to identify an immutable version of all binding-relevant intent content, including `statement`. Detecting reuse of an old version token after substantive content changed is outside this reference checker's capability and must be prevented by the authoring/versioning authority.

When no unambiguous exact-binding effective result exists, the normative projection is `not_evaluated`. A materialized `validation_status: passed` or `failed` is therefore a mismatch and cannot create a more permissive Operation.

## Materialized projections
""",
)

# Sharpen manifest source attribution without changing emitted codes.
replace_once(
    "tools/ontology_checker/rules.yaml",
    "manifest_version: 0.3.1",
    "manifest_version: 0.3.2",
)
replace_once(
    "tools/ontology_checker/rules.yaml",
    "source: OCP-004 §7.2 and §17 invariants 6–7\n- id: OPERATION_EXPLICIT_INTENT_EVIDENCE_INVALID",
    "source: OCP-004 §7.2 and §17 invariant 6\n- id: OPERATION_EXPLICIT_INTENT_EVIDENCE_INVALID",
)
replace_once(
    "tools/ontology_checker/rules.yaml",
    "source: OCP-004 §7.2 and §17 invariants 6–7\n- id: OPERATION_EXPLICIT_INTENT_EVIDENCE_STALE",
    "source: OCP-004 §7.2 and §17 invariant 7\n- id: OPERATION_EXPLICIT_INTENT_EVIDENCE_STALE",
)
replace_once(
    "tools/ontology_checker/rules.yaml",
    "source: OCP-004 §7.2 and §17 invariants 6–7\n- id: OPERATION_EXPLICIT_INTENT_STATUS_MISMATCH",
    "source: OCP-004 §7.2 and §17 invariant 7\n- id: OPERATION_EXPLICIT_INTENT_STATUS_MISMATCH",
)

print("AB-022 review resolution materialized")
