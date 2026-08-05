from __future__ import annotations

from copy import deepcopy
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import (  # noqa: E402
    derive_outcome_evidence_usability,
    effective_outcome_conclusion,
    load_fixture,
    outcome_assessment_heads,
    resolve_outcome_assessment,
    validate_reference_fixture,
)
from ocp_checker.assessment import (  # noqa: E402
    OUTCOME_ASSESSMENT_DERIVATION_RULES,
    OUTCOME_ASSESSMENT_ERROR_CODES,
)


class OutcomeAssessmentContractTests(unittest.TestCase):
    @staticmethod
    def _derive(fixture: dict, *, query_time: str | None = None) -> dict:
        return derive_outcome_evidence_usability(
            fixture["assessments"][0],
            freshness_rules=fixture["freshness_rules"],
            ambiguity_rules=fixture["ambiguity_rules"],
            evidence_snapshots=fixture["evidence_snapshots"],
            input_snapshots=fixture["input_snapshots"],
            events=fixture.get("events") or [],
            observations=fixture.get("observations") or [],
            query_time=query_time,
        )

    def test_activated_cutoff_equality_is_fresh_and_replayable(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/assessment/valid-activated-fresh.yaml"
        )
        self.assertTrue(validate_reference_fixture(fixture).valid)
        first = self._derive(fixture)
        second = self._derive(fixture)
        self.assertEqual(first, second)
        self.assertEqual(first["freshness_state"], "fresh")
        self.assertEqual(first["ambiguity_state"], "clear")

    def test_activated_conclusion_projection_requires_exact_context(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/assessment/valid-activated-fresh.yaml"
        )
        arguments = (
            fixture["assessments"],
            "objective@1",
            "OBJ-FRESH",
            "neutral.condition@1",
        )
        self.assertEqual(effective_outcome_conclusion(*arguments), "indeterminate")
        self.assertEqual(
            effective_outcome_conclusion(
                *arguments,
                objectives=fixture["objectives"],
                observations=fixture["observations"],
                evidence_snapshots=fixture["evidence_snapshots"],
                input_snapshots=fixture["input_snapshots"],
                freshness_rules=fixture["freshness_rules"],
                ambiguity_rules=fixture["ambiguity_rules"],
            ),
            "achieved",
        )

    def test_explicit_later_query_does_not_mutate_historical_result(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/assessment/valid-activated-fresh.yaml"
        )
        assessment = fixture["assessments"][0]
        later = self._derive(fixture, query_time="2026-08-05T02:00:01Z")
        self.assertEqual(later["freshness_state"], "stale")
        self.assertEqual(assessment["freshness_state"], "fresh")
        self.assertEqual(assessment["evaluated_at"].isoformat(), "2026-08-05T02:00:00+00:00")

    def test_future_temporal_fact_is_rule_derived_ambiguity(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/assessment/valid-activated-temporal-ambiguity.yaml"
        )
        self.assertTrue(validate_reference_fixture(fixture).valid)
        derived = self._derive(fixture)
        self.assertEqual(derived["freshness_state"], "indeterminate")
        self.assertEqual(derived["ambiguity_state"], "ambiguous")
        self.assertEqual(
            derived["ambiguity_findings"][0]["reason_ref"],
            "temporal-fact-future@1",
        )

    def test_semantic_ambiguity_remains_attributable(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/assessment/valid-activated-attributable-ambiguity.yaml"
        )
        self.assertTrue(validate_reference_fixture(fixture).valid)
        derived = self._derive(fixture)
        self.assertEqual(derived["freshness_state"], "fresh")
        self.assertEqual(derived["ambiguity_findings"][0]["basis"], "attributable")

    def test_undeclared_attributable_dimension_is_rejected(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/assessment/valid-activated-attributable-ambiguity.yaml"
        )
        fixture["assessments"][0]["ambiguity_findings"][0]["dimension_ref"] = (
            "criterion@1"
        )
        self.assertIn(
            "OUTCOME_ASSESSMENT_AMBIGUITY_STATE_MISMATCH",
            validate_reference_fixture(fixture).errors,
        )

    def test_same_evidence_can_be_stale_for_one_criterion_and_fresh_for_another(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/assessment/valid-activated-stale.yaml"
        )
        short = self._derive(fixture)
        long = deepcopy(fixture)
        assessment = long["assessments"][0]
        assessment["criterion_ref"] = "long-window.condition@1"
        assessment["freshness_rule_ref"] = "objective-achievement-freshness.long-window@1"
        assessment["ambiguity_rule_ref"] = "objective-achievement-ambiguity.long-window@1"
        long["freshness_rules"][0]["rule_ref"] = assessment["freshness_rule_ref"]
        long["freshness_rules"][0]["criterion_ref"] = assessment["criterion_ref"]
        long["freshness_rules"][0]["evidence_policies"][0]["max_age_seconds"] = 1800
        long["ambiguity_rules"][0]["rule_ref"] = assessment["ambiguity_rule_ref"]
        long["ambiguity_rules"][0]["criterion_ref"] = assessment["criterion_ref"]
        input_snapshot = long["input_snapshots"][0]
        input_snapshot["criterion_ref"] = assessment["criterion_ref"]
        input_snapshot["freshness_rule_ref"] = assessment["freshness_rule_ref"]
        input_snapshot["ambiguity_rule_ref"] = assessment["ambiguity_rule_ref"]
        self.assertEqual(short["freshness_state"], "stale")
        self.assertEqual(self._derive(long)["freshness_state"], "fresh")

    def test_recorded_at_does_not_replace_rule_selected_observed_at(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/assessment/valid-activated-stale.yaml"
        )
        fixture["observations"][0]["recorded_at"] = "2026-08-05T01:59:59Z"
        self.assertEqual(self._derive(fixture)["freshness_state"], "stale")

    def test_unavailable_historical_input_fails_closed(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/assessment/valid-activated-fresh.yaml"
        )
        fixture["observations"] = []
        derived = self._derive(fixture)
        self.assertEqual(derived["freshness_state"], "indeterminate")
        self.assertEqual(derived["ambiguity_state"], "ambiguous")

    def test_unavailable_or_duplicate_snapshot_fails_closed(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/assessment/valid-activated-fresh.yaml"
        )
        missing = deepcopy(fixture)
        missing["input_snapshots"] = []
        duplicate = deepcopy(fixture)
        duplicate["evidence_snapshots"].append(
            deepcopy(duplicate["evidence_snapshots"][0])
        )
        duplicate_evidence = deepcopy(fixture)
        duplicate_evidence["observations"].append(
            deepcopy(duplicate_evidence["observations"][0])
        )
        for case in (missing, duplicate, duplicate_evidence):
            with self.subTest(case=case):
                derived = self._derive(case)
                self.assertEqual(derived["freshness_state"], "indeterminate")
                self.assertEqual(derived["ambiguity_state"], "ambiguous")

    def test_unknown_rule_version_fails_closed(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/assessment/valid-activated-fresh.yaml"
        )
        fixture["assessments"][0]["freshness_rule_ref"] = (
            "objective-achievement-freshness.neutral-condition@2"
        )
        derived = self._derive(fixture)
        self.assertEqual(derived["freshness_state"], "indeterminate")
        self.assertEqual(derived["ambiguity_state"], "ambiguous")

    def test_invalid_freshness_cutoff_or_precision_is_rejected(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/assessment/valid-activated-fresh.yaml"
        )
        invalid_cutoff = deepcopy(fixture)
        invalid_cutoff["freshness_rules"][0]["evidence_policies"][0][
            "max_age_seconds"
        ] = float("nan")
        invalid_precision = deepcopy(fixture)
        invalid_precision["freshness_rules"][0]["comparison_precision"] = (
            "millisecond"
        )
        for case in (invalid_cutoff, invalid_precision):
            with self.subTest(case=case):
                self.assertIn(
                    "OUTCOME_ASSESSMENT_FRESHNESS_RULE_INVALID",
                    validate_reference_fixture(case).errors,
                )

    def test_duplicate_ambiguity_dimension_is_rejected(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/assessment/valid-activated-fresh.yaml"
        )
        fixture["ambiguity_rules"][0]["machine_dimensions"].append("temporal@1")
        self.assertIn(
            "OUTCOME_ASSESSMENT_AMBIGUITY_RULE_INVALID",
            validate_reference_fixture(fixture).errors,
        )

    def test_unknown_assessment_kind_cannot_bypass_activation(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/assessment/invalid-unknown-assessment-kind.yaml"
        )
        self.assertEqual(
            set(validate_reference_fixture(fixture).errors),
            {"OUTCOME_ASSESSMENT_KIND_UNSUPPORTED"},
        )

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

    def test_assessment_rules_manifest_is_complete(self) -> None:
        rules = yaml.safe_load(
            (ROOT / "assessment-rules.yaml").read_text(encoding="utf-8")
        )["rules"]
        validation_ids = {
            item["id"]
            for item in rules
            if item.get("kind", "validation") == "validation"
        }
        derivation_ids = {
            item["id"] for item in rules if item.get("kind") == "derivation"
        }
        self.assertEqual(validation_ids, set(OUTCOME_ASSESSMENT_ERROR_CODES))
        self.assertEqual(
            derivation_ids, set(OUTCOME_ASSESSMENT_DERIVATION_RULES)
        )


if __name__ == "__main__":
    unittest.main()
