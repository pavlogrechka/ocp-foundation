from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import (  # noqa: E402
    derive_operation_authorization_result,
    load_fixture,
    validate_reference_fixture,
)
from ocp_checker.operation_authorization import (  # noqa: E402
    OPERATION_AUTHORIZATION_DERIVATION_RULES,
    OPERATION_AUTHORIZATION_ERROR_CODES,
)


class OperationAuthorizationSourceContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        fixture_root = ROOT / "fixtures/operation_authorization"
        cls.fixtures = {
            path.stem: load_fixture(path) for path in sorted(fixture_root.glob("*.yaml"))
        }

    def test_fixture_set_contains_positive_and_material_negatives(self) -> None:
        self.assertGreaterEqual(len(self.fixtures), 6)
        valid = [item for item in self.fixtures.values() if item["expected"]["valid"]]
        invalid = [item for item in self.fixtures.values() if not item["expected"]["valid"]]
        self.assertGreaterEqual(len(valid), 1)
        self.assertGreaterEqual(len(invalid), 5)

    def test_all_fixtures_match_exact_expected_errors(self) -> None:
        for name, fixture in self.fixtures.items():
            with self.subTest(fixture=name):
                validation = validate_reference_fixture(fixture)
                self.assertEqual(validation.valid, bool(fixture["expected"]["valid"]))
                self.assertEqual(set(validation.errors), set(fixture["expected"].get("error_codes", [])))

    def test_valid_decision_is_accepted(self) -> None:
        snapshot = self.fixtures["valid-authorize-decision"]["snapshot"]
        self.assertEqual(derive_operation_authorization_result(snapshot), "accepted")

    def test_decision_order_has_no_authority(self) -> None:
        snapshot = copy.deepcopy(self.fixtures["valid-authorize-decision"]["snapshot"])
        snapshot["decisions"] = list(reversed(snapshot["decisions"]))
        self.assertEqual(derive_operation_authorization_result(snapshot), "accepted")

    def test_mismatched_ocp017_binding_fails_safe(self) -> None:
        snapshot = copy.deepcopy(self.fixtures["valid-authorize-decision"]["snapshot"])
        snapshot["authorization_evidence_binding"]["subject_operation_ref"] = "OP-SYNTH-OTHER"
        self.assertEqual(derive_operation_authorization_result(snapshot), "indeterminate")

    def test_stale_or_ineligible_never_becomes_accepted(self) -> None:
        for fixture_name in ("invalid-stale-decision", "invalid-ineligible-authorizer"):
            with self.subTest(fixture=fixture_name):
                snapshot = self.fixtures[fixture_name]["snapshot"]
                self.assertEqual(derive_operation_authorization_result(snapshot), "indeterminate")

    def test_malformed_registry_or_lineage_member_never_becomes_accepted(self) -> None:
        for fixture_name in (
            "invalid-malformed-authorizer-organization",
            "invalid-malformed-capability-registry",
            "invalid-malformed-historical-lineage-member",
        ):
            with self.subTest(fixture=fixture_name):
                snapshot = self.fixtures[fixture_name]["snapshot"]
                self.assertEqual(derive_operation_authorization_result(snapshot), "indeterminate")

    def test_explicit_denial_is_not_accepted(self) -> None:
        snapshot = self.fixtures["invalid-denied-decision"]["snapshot"]
        self.assertEqual(derive_operation_authorization_result(snapshot), "denied")

    def test_forbidden_concept_or_order_coupling_fails_safe(self) -> None:
        snapshot = self.fixtures["invalid-forbidden-coupling"]["snapshot"]
        self.assertEqual(derive_operation_authorization_result(snapshot), "indeterminate")

    def test_manifest_is_complete(self) -> None:
        rules = yaml.safe_load(
            (ROOT / "operation-authorization-rules.yaml").read_text(encoding="utf-8")
        )["rules"]
        validation_ids = {
            item["id"] for item in rules if item.get("kind", "validation") == "validation"
        }
        derivation_ids = {item["id"] for item in rules if item.get("kind") == "derivation"}
        self.assertEqual(validation_ids, set(OPERATION_AUTHORIZATION_ERROR_CODES))
        self.assertEqual(derivation_ids, set(OPERATION_AUTHORIZATION_DERIVATION_RULES))


if __name__ == "__main__":
    unittest.main()
