from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import (  # noqa: E402
    effective_outcome_conclusion,
    load_fixture,
    outcome_assessment_heads,
    resolve_outcome_assessment,
    validate_reference_fixture,
)


class OutcomeAssessmentContractTests(unittest.TestCase):
    def test_conflicting_evidence_is_valid_only_as_indeterminate(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/assessment/valid-conflicting-indeterminate.yaml"
        )
        self.assertTrue(validate_reference_fixture(fixture).valid)

    def test_missing_evidence_is_valid_only_as_indeterminate(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/assessment/valid-missing-indeterminate.yaml"
        )
        self.assertTrue(validate_reference_fixture(fixture).valid)

    def test_late_evidence_creates_new_lineage_head(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/assessment/valid-late-evidence-supersession.yaml"
        )
        self.assertTrue(validate_reference_fixture(fixture).valid)
        assessments = fixture["assessments"]
        self.assertIsNotNone(resolve_outcome_assessment(assessments, "ASM-003A"))
        self.assertIsNotNone(resolve_outcome_assessment(assessments, "ASM-003B"))
        heads = outcome_assessment_heads(
            assessments,
            target_kind_ref="objective@1",
            target_ref="OBJ-ASM-003",
            criterion_ref="neutral.condition@1",
        )
        self.assertEqual([item["assessment_id"] for item in heads], ["ASM-003B"])
        self.assertEqual(
            effective_outcome_conclusion(
                assessments,
                "objective@1",
                "OBJ-ASM-003",
                "neutral.condition@1",
            ),
            "achieved",
        )

    def test_conflicting_heads_remain_indeterminate_in_both_orders(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/assessment/valid-conflicting-heads.yaml"
        )
        self.assertTrue(validate_reference_fixture(fixture).valid)
        for assessments in (
            fixture["assessments"],
            list(reversed(fixture["assessments"])),
        ):
            with self.subTest(order=[item["assessment_id"] for item in assessments]):
                self.assertEqual(
                    effective_outcome_conclusion(
                        assessments,
                        "objective@1",
                        "OBJ-ASM-004",
                        "neutral.condition@1",
                    ),
                    "indeterminate",
                )

    def test_supersession_cannot_change_binding_identity(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/assessment/invalid-binding-change.yaml"
        )
        self.assertEqual(
            set(validate_reference_fixture(fixture).errors),
            {"OUTCOME_ASSESSMENT_BINDING_MISMATCH"},
        )

    def test_result_and_lifecycle_fields_are_forbidden(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/assessment/invalid-result-coupling.yaml"
        )
        self.assertEqual(
            set(validate_reference_fixture(fixture).errors),
            {"OUTCOME_ASSESSMENT_RESULT_COUPLING_FORBIDDEN"},
        )

    def test_integrated_scenario_uses_normative_record_contract(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/event/valid-integrated-scenario.yaml"
        )
        self.assertTrue(validate_reference_fixture(fixture).valid)
        assessment = fixture["scenario"]["assessment"]
        self.assertEqual(assessment["target_kind_ref"], "objective@1")
        self.assertEqual(assessment["evidence_state"], "conflicting")
        self.assertEqual(assessment["conclusion"], "indeterminate")


if __name__ == "__main__":
    unittest.main()
