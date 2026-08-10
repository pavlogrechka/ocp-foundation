from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import (  # noqa: E402
    derive_quantitative_reservation_boundary,
    derive_whole_resource_reservation_boundary,
    load_fixture,
    validate_reference_fixture,
)
from ocp_checker import reservation_boundary  # noqa: E402
from ocp_checker.reservation_boundary import (  # noqa: E402
    REQUEST_FIELDS,
    RESERVATION_BOUNDARY_DERIVATION_RULES,
    RESERVATION_BOUNDARY_ERROR_CODES,
    RESOURCE_SNAPSHOT_FIELDS,
)


class ReservationBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        fixture_root = ROOT / "fixtures/reservation_boundary"
        cls.fixtures = {
            path.stem: load_fixture(path) for path in sorted(fixture_root.glob("*.yaml"))
        }

    def test_all_declared_branch_action_combinations_are_valid(self) -> None:
        valid = {
            name: fixture
            for name, fixture in self.fixtures.items()
            if fixture["expected"]["valid"]
        }
        combinations = {
            (
                fixture["dataset"]["establishment_request"]["branch"],
                fixture["dataset"]["establishment_request"]["action"],
            )
            for fixture in valid.values()
        }
        self.assertEqual(
            combinations,
            {
                ("whole_resource_exclusivity", "reservation"),
                ("whole_resource_exclusivity", "allocation"),
                ("partial_quantitative", "reservation"),
                ("partial_quantitative", "allocation"),
            },
        )
        self.assertEqual(len(valid), 4)
        for name, fixture in valid.items():
            with self.subTest(fixture=name):
                request = fixture["dataset"]["establishment_request"]
                derivation = (
                    derive_whole_resource_reservation_boundary
                    if request["branch"] == "whole_resource_exclusivity"
                    else derive_quantitative_reservation_boundary
                )
                self.assertEqual(derivation(fixture["dataset"]), request["stored_result"])

    def test_all_fixtures_match_exact_expected_errors(self) -> None:
        self.assertEqual(len(self.fixtures), 21)
        for name, fixture in self.fixtures.items():
            with self.subTest(fixture=name):
                validation = validate_reference_fixture(fixture)
                self.assertEqual(validation.valid, bool(fixture["expected"]["valid"]))
                self.assertEqual(
                    set(validation.errors),
                    set(fixture["expected"].get("error_codes", [])),
                )

    def test_every_invalid_fixture_fails_safe_without_permissive_result(self) -> None:
        permissive = {"reserved", "allocated", "available", "capacity_sufficient"}
        self.assertTrue(permissive.isdisjoint(reservation_boundary.DERIVED_RESULTS))
        for name, fixture in self.fixtures.items():
            if fixture["expected"]["valid"] or name == "invalid-result-mismatch":
                continue
            with self.subTest(fixture=name):
                dataset = fixture.get("dataset")
                self.assertEqual(
                    derive_whole_resource_reservation_boundary(dataset), "indeterminate"
                )
                self.assertEqual(
                    derive_quantitative_reservation_boundary(dataset), "indeterminate"
                )

        mismatch = self.fixtures["invalid-result-mismatch"]["dataset"]
        self.assertNotEqual(
            derive_whole_resource_reservation_boundary(mismatch),
            mismatch["establishment_request"]["stored_result"],
        )

    def test_e_and_q_are_not_interchangeable(self) -> None:
        whole = self.fixtures["valid-e-reservation-not-established"]["dataset"]
        quantitative = self.fixtures["valid-q-reservation-not-established"]["dataset"]
        self.assertEqual(derive_quantitative_reservation_boundary(whole), "indeterminate")
        self.assertEqual(derive_whole_resource_reservation_boundary(quantitative), "indeterminate")
        for name in (
            "invalid-e-quantitative-coupling",
            "invalid-q-prerequisite-missing",
            "invalid-q-prerequisite-wrong",
            "invalid-self-supply-e",
            "invalid-self-supply-q",
        ):
            with self.subTest(fixture=name):
                self.assertFalse(validate_reference_fixture(self.fixtures[name]).valid)

    def test_every_declared_element_is_live(self) -> None:
        whole_fixture = self.fixtures["valid-e-reservation-not-established"]
        quantitative_fixture = self.fixtures["valid-q-allocation-not-established"]

        original_branches = reservation_boundary.BRANCHES
        original_actions = reservation_boundary.ACTIONS
        original_contract = reservation_boundary.QUANTITATIVE_CONTRACT_REF
        original_rules = dict(reservation_boundary.RULE_REFS)
        original_results = dict(reservation_boundary.NEGATIVE_RESULTS)
        try:
            for branch, fixture in (
                ("whole_resource_exclusivity", whole_fixture),
                ("partial_quantitative", quantitative_fixture),
            ):
                reservation_boundary.BRANCHES = original_branches - {branch}
                self.assertFalse(validate_reference_fixture(fixture).valid)
                reservation_boundary.BRANCHES = original_branches

            for action, fixture in (
                ("reservation", whole_fixture),
                ("allocation", quantitative_fixture),
            ):
                reservation_boundary.ACTIONS = original_actions - {action}
                self.assertFalse(validate_reference_fixture(fixture).valid)
                reservation_boundary.ACTIONS = original_actions

            reservation_boundary.QUANTITATIVE_CONTRACT_REF = "OCP-SYNTH-MUTATED@1"
            self.assertFalse(validate_reference_fixture(quantitative_fixture).valid)
            reservation_boundary.QUANTITATIVE_CONTRACT_REF = original_contract

            for branch, fixture in (
                ("whole_resource_exclusivity", whole_fixture),
                ("partial_quantitative", quantitative_fixture),
            ):
                reservation_boundary.RULE_REFS[branch] = "rule-synth-mutated@1"
                self.assertFalse(validate_reference_fixture(fixture).valid)
                reservation_boundary.RULE_REFS = dict(original_rules)

            for key, fixture in (
                (("whole_resource_exclusivity", "reservation"), whole_fixture),
                (("partial_quantitative", "allocation"), quantitative_fixture),
            ):
                reservation_boundary.NEGATIVE_RESULTS[key] = "negative_result_synth_mutated"
                self.assertFalse(validate_reference_fixture(fixture).valid)
                reservation_boundary.NEGATIVE_RESULTS = dict(original_results)

            for field in REQUEST_FIELDS:
                candidate = copy.deepcopy(quantitative_fixture)
                del candidate["dataset"]["establishment_request"][field]
                self.assertFalse(validate_reference_fixture(candidate).valid, field)
            for field in RESOURCE_SNAPSHOT_FIELDS:
                candidate = copy.deepcopy(quantitative_fixture)
                del candidate["dataset"]["resource_snapshots"][0][field]
                self.assertFalse(validate_reference_fixture(candidate).valid, field)
        finally:
            reservation_boundary.BRANCHES = original_branches
            reservation_boundary.ACTIONS = original_actions
            reservation_boundary.QUANTITATIVE_CONTRACT_REF = original_contract
            reservation_boundary.RULE_REFS = original_rules
            reservation_boundary.NEGATIVE_RESULTS = original_results

    def test_manifest_matches_exported_rules(self) -> None:
        rules = yaml.safe_load(
            (ROOT / "reservation-boundary-rules.yaml").read_text(encoding="utf-8")
        )["rules"]
        validation_ids = {
            item["id"] for item in rules if item.get("kind", "validation") == "validation"
        }
        derivation_ids = {item["id"] for item in rules if item.get("kind") == "derivation"}
        self.assertEqual(validation_ids, set(RESERVATION_BOUNDARY_ERROR_CODES))
        self.assertEqual(derivation_ids, set(RESERVATION_BOUNDARY_DERIVATION_RULES))


if __name__ == "__main__":
    unittest.main()
