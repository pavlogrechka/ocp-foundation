from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import (  # noqa: E402
    derive_quantitative_total,
    load_fixture,
    validate_reference_fixture,
)
from ocp_checker.quantitative_input import (  # noqa: E402
    QUANTITATIVE_INPUT_DERIVATION_RULES,
    QUANTITATIVE_INPUT_ERROR_CODES,
)


class QuantitativeInputBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        fixture_root = ROOT / "fixtures/quantitative_input"
        cls.fixtures = {
            path.stem: load_fixture(path) for path in sorted(fixture_root.glob("*.yaml"))
        }

    def test_evidence_grows_with_positive_and_material_negative_cases(self) -> None:
        self.assertGreaterEqual(len(self.fixtures), 16)
        self.assertGreaterEqual(
            len([item for item in self.fixtures.values() if item["expected"]["valid"]]), 2
        )
        self.assertGreaterEqual(
            len([item for item in self.fixtures.values() if not item["expected"]["valid"]]), 14
        )

    def test_all_fixtures_match_exact_expected_errors(self) -> None:
        for name, fixture in self.fixtures.items():
            with self.subTest(fixture=name):
                validation = validate_reference_fixture(fixture)
                self.assertEqual(validation.valid, bool(fixture["expected"]["valid"]))
                self.assertEqual(set(validation.errors), set(fixture["expected"].get("error_codes", [])))

    def test_valid_demand_and_consumed_totals_are_exact(self) -> None:
        expected = {
            "valid-demand-total": {
                "magnitude_lexeme": "5.5",
                "unit_ref": "UNIT-SYNTH-A@1",
                "dimension_ref": "DIMENSION-SYNTH-A@1",
            },
            "valid-consumed-total": {
                "magnitude_lexeme": "2",
                "unit_ref": "UNIT-SYNTH-B@1",
                "dimension_ref": "DIMENSION-SYNTH-B@1",
            },
        }
        for name, total in expected.items():
            with self.subTest(fixture=name):
                self.assertEqual(derive_quantitative_total(self.fixtures[name]["dataset"]), total)

    def test_every_material_negative_fails_closed(self) -> None:
        for name, fixture in self.fixtures.items():
            if fixture["expected"]["valid"] or name == "invalid-result-mismatch":
                continue
            with self.subTest(fixture=name):
                self.assertIsNone(derive_quantitative_total(fixture.get("dataset")))

        mismatch = self.fixtures["invalid-result-mismatch"]["dataset"]
        self.assertNotEqual(
            derive_quantitative_total(mismatch),
            mismatch["aggregation_request"]["stored_total"],
        )

        capacity_attempt = copy.deepcopy(self.fixtures["valid-demand-total"]["dataset"])
        capacity_attempt["aggregation_request"]["role"] = "capacity_limit"
        for binding in capacity_attempt["input_snapshots"][0]["bindings"]:
            binding["role"] = "capacity_limit"
        self.assertIsNone(derive_quantitative_total(capacity_attempt))
        self.assertIn(
            "QUANTITATIVE_INPUT_AGGREGATION_INVALID",
            validate_reference_fixture(
                {"concept": "QuantitativeInputDataset", "dataset": capacity_attempt}
            ).errors,
        )

    def test_result_is_order_invariant_and_ignores_unreferenced_bindings(self) -> None:
        dataset = copy.deepcopy(self.fixtures["valid-demand-total"]["dataset"])
        expected = derive_quantitative_total(dataset)
        dataset["input_snapshots"][0]["bindings"].reverse()
        dataset["aggregation_request"]["operand_keys"].reverse()
        self.assertEqual(derive_quantitative_total(dataset), expected)

        extra = copy.deepcopy(dataset["input_snapshots"][0]["bindings"][0])
        extra["binding_key"] = "DEMAND-SYNTH-UNREFERENCED"
        extra["magnitude_lexeme"] = "999"
        dataset["input_snapshots"][0]["bindings"].append(extra)
        self.assertEqual(derive_quantitative_total(dataset), expected)

    def test_manifest_is_complete(self) -> None:
        rules = yaml.safe_load(
            (ROOT / "quantitative-input-rules.yaml").read_text(encoding="utf-8")
        )["rules"]
        validation_ids = {
            item["id"] for item in rules if item.get("kind", "validation") == "validation"
        }
        derivation_ids = {item["id"] for item in rules if item.get("kind") == "derivation"}
        self.assertEqual(validation_ids, set(QUANTITATIVE_INPUT_ERROR_CODES))
        self.assertEqual(derivation_ids, set(QUANTITATIVE_INPUT_DERIVATION_RULES))


if __name__ == "__main__":
    unittest.main()
