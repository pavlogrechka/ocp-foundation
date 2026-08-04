from __future__ import annotations

import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import (  # noqa: E402
    derive_resource_interchangeability,
    load_fixture,
    resolve_interchangeability_requirement,
    validate_reference_fixture,
)
from ocp_checker.interchangeability import (  # noqa: E402
    INTERCHANGEABILITY_DERIVATION_RULES,
    INTERCHANGEABILITY_ERROR_CODES,
    validate_interchangeability_requirement,
)


class ResourceInterchangeabilityContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = load_fixture(
            ROOT / "fixtures/interchangeability/mandatory-counterexamples.yaml"
        )

    def test_requirement_dataset_is_exact_and_valid(self) -> None:
        self.assertTrue(validate_reference_fixture(self.fixture).valid)
        requirement = resolve_interchangeability_requirement(
            self.fixture["requirements"], "REQ-A@1"
        )
        self.assertIsNotNone(requirement)
        self.assertEqual(requirement["owner_ref"], "COORDINATION-REQUIREMENT-CONTRACT-001")
        self.assertIsNone(
            resolve_interchangeability_requirement(self.fixture["requirements"], "REQ-A@2")
        )

    def test_every_mandatory_counterexample_has_the_expected_outcome(self) -> None:
        for case_name, case in self.fixture["cases"].items():
            with self.subTest(case=case_name):
                self.assertEqual(
                    derive_resource_interchangeability(
                        case["evaluation"], self.fixture["requirements"]
                    ),
                    case["expected_outcome"],
                )

    def test_directionality_has_no_implicit_reverse(self) -> None:
        cases = self.fixture["cases"]
        self.assertEqual(
            derive_resource_interchangeability(
                cases["b_substitutes_for_a"]["evaluation"], self.fixture["requirements"]
            ),
            "positive",
        )
        self.assertEqual(
            derive_resource_interchangeability(
                cases["a_does_not_substitute_for_b"]["evaluation"],
                self.fixture["requirements"],
            ),
            "negative",
        )

    def test_two_positive_candidates_preserve_three_resource_identities(self) -> None:
        self.assertEqual(
            {item["resource_id"] for item in self.fixture["resources"]},
            {"R-A", "R-B", "R-C"},
        )
        cases = self.fixture["cases"]
        for case_name in ("b_substitutes_for_a", "second_candidate_same_requirement"):
            self.assertEqual(
                derive_resource_interchangeability(
                    cases[case_name]["evaluation"], self.fixture["requirements"]
                ),
                "positive",
            )
        self.assertNotIn(
            "interchangeable_with", cases["second_candidate_same_requirement"]["evaluation"]
        )

    def test_positive_does_not_change_availability_authorization_or_assignments(self) -> None:
        cases = self.fixture["cases"]
        external = cases["unavailable_or_unauthorized_is_outside_result"]
        self.assertEqual(
            derive_resource_interchangeability(
                external["evaluation"], self.fixture["requirements"]
            ),
            "positive",
        )
        self.assertEqual(external["outside_decision"], {"available": False, "authorized": False})

        mutation = cases["assignment_mutation_is_rejected"]
        self.assertEqual(
            derive_resource_interchangeability(
                mutation["evaluation"], self.fixture["requirements"]
            ),
            "indeterminate",
        )
        self.assertEqual(mutation["original_assignment"]["resource_ref"], "R-A")
        self.assertNotEqual(
            mutation["original_assignment"]["assignment_id"],
            mutation["proposed_new_assignment"]["assignment_id"],
        )

    def test_rule_version_is_part_of_replay_context(self) -> None:
        cases = self.fixture["cases"]
        self.assertEqual(
            derive_resource_interchangeability(
                cases["exact_rule_replay"]["evaluation"], self.fixture["requirements"]
            ),
            "positive",
        )
        self.assertEqual(
            derive_resource_interchangeability(
                cases["changed_rule_version"]["evaluation"], self.fixture["requirements"]
            ),
            "indeterminate",
        )

    def test_requirement_rejects_authorization_or_selection_coupling(self) -> None:
        requirement = dict(self.fixture["requirements"][0])
        requirement["authorization"] = "granted"
        self.assertEqual(
            set(validate_interchangeability_requirement(requirement).errors),
            {"INTERCHANGEABILITY_FORBIDDEN_COUPLING"},
        )

    def test_interchangeability_manifest_is_complete(self) -> None:
        rules = yaml.safe_load(
            (ROOT / "interchangeability-rules.yaml").read_text(encoding="utf-8")
        )["rules"]
        validation_ids = {
            item["id"]
            for item in rules
            if item.get("kind", "validation") == "validation"
        }
        derivation_ids = {
            item["id"] for item in rules if item.get("kind") == "derivation"
        }
        self.assertEqual(validation_ids, set(INTERCHANGEABILITY_ERROR_CODES))
        self.assertEqual(derivation_ids, set(INTERCHANGEABILITY_DERIVATION_RULES))


if __name__ == "__main__":
    unittest.main()
