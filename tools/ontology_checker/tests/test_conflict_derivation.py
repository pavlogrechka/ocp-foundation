from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import (  # noqa: E402
    derive_conflict_establishment_result,
    load_fixture,
    validate_reference_fixture,
)
from ocp_checker.conflict_derivation import (  # noqa: E402
    CONFLICT_DERIVATION_DERIVATION_RULES,
    CONFLICT_DERIVATION_ERROR_CODES,
)


class ConflictDerivationBoundaryTests(unittest.TestCase):
    G4_BINDING_GROUPS = {
        "accepted_consumer": {"consumer_ref", "consumer_status"},
        "baseline_and_result_need": {"baseline_contract_ref", "result_need_ref"},
        "versioned_positive_rule": {"positive_rule_ref"},
        "input_snapshot_and_context": {
            "positive_input_snapshot_ref",
            "evaluation_context_ref",
        },
        "criterion_owner_and_evaluator": {"criterion_owner_ref", "evaluator_ref"},
        "object_class_decision": {"object_class_decision_ref"},
    }

    @classmethod
    def setUpClass(cls) -> None:
        fixture_root = ROOT / "fixtures/conflict_derivation"
        cls.fixtures = {
            path.stem: load_fixture(path) for path in sorted(fixture_root.glob("*.yaml"))
        }

    def test_evidence_grows_with_positive_and_material_negative_cases(self) -> None:
        self.assertGreaterEqual(len(self.fixtures), 22)
        self.assertGreaterEqual(
            len([item for item in self.fixtures.values() if item["expected"]["valid"]]), 4
        )
        self.assertGreaterEqual(
            len([item for item in self.fixtures.values() if not item["expected"]["valid"]]), 18
        )

    def test_all_fixtures_match_exact_expected_errors(self) -> None:
        for name, fixture in self.fixtures.items():
            with self.subTest(fixture=name):
                validation = validate_reference_fixture(fixture)
                self.assertEqual(validation.valid, bool(fixture["expected"]["valid"]))
                self.assertEqual(set(validation.errors), set(fixture["expected"].get("error_codes", [])))

    def test_one_or_many_violations_never_establish_conflict(self) -> None:
        for fixture_name in ("valid-single-violation", "valid-multiple-violations"):
            with self.subTest(fixture=fixture_name):
                snapshot = self.fixtures[fixture_name]["snapshot"]
                self.assertEqual(
                    derive_conflict_establishment_result(snapshot), "conflict_not_established"
                )

    def test_incomplete_conflicting_stale_or_indeterminate_inputs_fail_safe(self) -> None:
        for fixture_name in (
            "invalid-evaluation-unresolved",
            "invalid-evaluation-ambiguous",
            "invalid-binding-mismatch",
            "invalid-stale-input",
            "valid-indeterminate-evaluation",
        ):
            with self.subTest(fixture=fixture_name):
                snapshot = self.fixtures[fixture_name]["snapshot"]
                self.assertEqual(derive_conflict_establishment_result(snapshot), "indeterminate")

    def test_result_is_invariant_to_evaluation_order_and_extra_unreferenced_evidence(self) -> None:
        snapshot = copy.deepcopy(self.fixtures["valid-multiple-violations"]["snapshot"])
        snapshot["constraint_evaluations"].reverse()
        self.assertEqual(derive_conflict_establishment_result(snapshot), "conflict_not_established")
        extra = copy.deepcopy(snapshot["constraint_evaluations"][0])
        extra["evaluation_id"] = "EVAL-SYNTH-UNREFERENCED"
        extra["constraint_ref"] = "CONSTRAINT-SYNTH-UNREFERENCED"
        extra["constraint_version_ref"] = "constraint-synth-unreferenced@1"
        snapshot["constraint_evaluations"].append(extra)
        self.assertEqual(derive_conflict_establishment_result(snapshot), "conflict_not_established")
        conflicting_extra = copy.deepcopy(snapshot["constraint_evaluations"][0])
        conflicting_extra["evaluation_id"] = "EVAL-SYNTH-UNREFERENCED-CONFLICT"
        conflicting_extra["result"] = "satisfied"
        snapshot["constraint_evaluations"].extend([conflicting_extra, "MALFORMED-UNREFERENCED"])
        self.assertEqual(derive_conflict_establishment_result(snapshot), "conflict_not_established")

    def test_each_incomplete_positive_g4_binding_attempt_fails_safe(self) -> None:
        fixtures = {
            name: item
            for name, item in self.fixtures.items()
            if name.startswith("invalid-positive-g4-missing-")
        }
        self.assertEqual(len(fixtures), len(self.G4_BINDING_GROUPS))
        for name, fixture in fixtures.items():
            with self.subTest(fixture=name):
                attempt = fixture["snapshot"]["derivation_request"]["activation_attempt"]
                supplied_groups = {
                    group
                    for group, fields in self.G4_BINDING_GROUPS.items()
                    if fields <= set(attempt)
                }
                declared_missing = set(fixture["gate_probe"]["missing_groups"])
                self.assertEqual(
                    set(self.G4_BINDING_GROUPS) - supplied_groups,
                    declared_missing,
                )
                derived = derive_conflict_establishment_result(fixture["snapshot"])
                self.assertEqual(derived, "indeterminate")
                self.assertNotEqual(derived, "conflict")

    def test_complete_self_declared_positive_g4_attempt_has_no_authority(self) -> None:
        fixture = self.fixtures["invalid-positive-g4-unverified-complete"]
        attempt = fixture["snapshot"]["derivation_request"]["activation_attempt"]
        self.assertTrue(
            all(fields <= set(attempt) for fields in self.G4_BINDING_GROUPS.values())
        )
        self.assertEqual(fixture["gate_probe"]["missing_groups"], [])
        self.assertEqual(attempt["consumer_status"], "Accepted")
        validation = validate_reference_fixture(fixture)
        self.assertFalse(validation.valid)
        derived = derive_conflict_establishment_result(fixture["snapshot"])
        self.assertEqual(derived, "indeterminate")
        self.assertNotEqual(derived, "conflict")

    def test_manifest_is_complete(self) -> None:
        rules = yaml.safe_load(
            (ROOT / "conflict-derivation-rules.yaml").read_text(encoding="utf-8")
        )["rules"]
        validation_ids = {
            item["id"] for item in rules if item.get("kind", "validation") == "validation"
        }
        derivation_ids = {item["id"] for item in rules if item.get("kind") == "derivation"}
        self.assertEqual(validation_ids, set(CONFLICT_DERIVATION_ERROR_CODES))
        self.assertEqual(derivation_ids, set(CONFLICT_DERIVATION_DERIVATION_RULES))


if __name__ == "__main__":
    unittest.main()
