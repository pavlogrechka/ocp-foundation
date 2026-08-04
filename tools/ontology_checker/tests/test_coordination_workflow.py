from __future__ import annotations

import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import (  # noqa: E402
    derive_coordination_evidence,
    load_fixture,
    validate_reference_fixture,
)
from ocp_checker.coordination_workflow import (  # noqa: E402
    COORDINATION_WORKFLOW_DERIVATION_RULES,
    COORDINATION_WORKFLOW_ERROR_CODES,
)


class CoordinationWorkflowContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = load_fixture(
            ROOT / "fixtures/coordination_workflow/mandatory-cases.yaml"
        )

    def test_fixture_is_valid(self) -> None:
        self.assertTrue(validate_reference_fixture(self.fixture).valid)

    def test_every_case_has_the_expected_outcome(self) -> None:
        for name, case in self.fixture["cases"].items():
            with self.subTest(case=name):
                self.assertEqual(
                    derive_coordination_evidence(case["snapshot"]),
                    case["expected_outcome"],
                )

    def test_record_order_does_not_change_authority(self) -> None:
        positive = self.fixture["cases"]["all_invited_responders_confirm"]["snapshot"]
        reordered = self.fixture["cases"]["record_order_has_no_authority"]["snapshot"]
        self.assertEqual(derive_coordination_evidence(positive), "positive")
        self.assertEqual(derive_coordination_evidence(reordered), "positive")

    def test_positive_evidence_does_not_authorize_or_mutate_assignment(self) -> None:
        snapshot = dict(
            self.fixture["cases"]["all_invited_responders_confirm"]["snapshot"]
        )
        snapshot["assignment_mutation"] = {"resource_ref": "R-B"}
        self.assertEqual(derive_coordination_evidence(snapshot), "indeterminate")

    def test_manifest_is_complete(self) -> None:
        rules = yaml.safe_load(
            (ROOT / "coordination-workflow-rules.yaml").read_text(encoding="utf-8")
        )["rules"]
        validation_ids = {
            item["id"] for item in rules if item.get("kind", "validation") == "validation"
        }
        derivation_ids = {item["id"] for item in rules if item.get("kind") == "derivation"}
        self.assertEqual(validation_ids, set(COORDINATION_WORKFLOW_ERROR_CODES))
        self.assertEqual(derivation_ids, set(COORDINATION_WORKFLOW_DERIVATION_RULES))


if __name__ == "__main__":
    unittest.main()
