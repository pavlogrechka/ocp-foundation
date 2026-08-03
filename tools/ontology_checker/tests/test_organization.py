from __future__ import annotations

import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import DERIVATION_RULES, ERROR_CODES, load_fixture  # noqa: E402
from ocp_checker.organization import (  # noqa: E402
    ORGANIZATION_DERIVATION_RULES,
    ORGANIZATION_ERROR_CODES,
    graph_breakpoints,
    organization_relationship_effective_at,
    validate_organization,
    validate_organization_graph,
    validate_organization_relationship,
)


class OrganizationCheckerTests(unittest.TestCase):
    def test_entity_fixtures_match_exact_errors(self) -> None:
        for path in sorted((ROOT / "fixtures/organization").glob("*.yaml")):
            with self.subTest(path=path):
                fixture = load_fixture(path)
                if fixture["concept"] == "Organization":
                    result = validate_organization(fixture["entity"])
                else:
                    result = validate_organization_relationship(fixture["entity"])
                self.assertEqual(result.valid, fixture["expected"]["valid"])
                self.assertEqual(set(result.errors), set(fixture["expected"].get("error_codes", [])))

    def test_graph_regression_fixtures(self) -> None:
        root = ROOT / "regression_fixtures/organization_graph"
        for path in sorted(root.glob("*.yaml")):
            with self.subTest(path=path):
                fixture = yaml.safe_load(path.read_text(encoding="utf-8"))
                result = validate_organization_graph(fixture["records"], fixture.get("reference_time"))
                self.assertEqual(set(result.errors), set(fixture["expected_error_codes"]))

    def test_transient_cycle_is_found_by_sweep_but_not_after_interval(self) -> None:
        fixture = yaml.safe_load((ROOT / "regression_fixtures/organization_graph/transient-cycle.yaml").read_text(encoding="utf-8"))
        records = fixture["records"]
        self.assertTrue(validate_organization_graph(records, "2026-04-02T00:00:00Z").valid)
        self.assertIn("ORGANIZATION_STRUCTURAL_CYCLE", validate_organization_graph(records).errors)
        self.assertGreaterEqual(len(graph_breakpoints(records)), 5)

    def test_unknown_class_cannot_bypass_structural_governance(self) -> None:
        fixture = load_fixture(ROOT / "fixtures/organization/invalid-relationship-class.yaml")
        result = validate_organization_relationship(fixture["entity"])
        self.assertEqual(result.errors, ("ORGANIZATION_RELATIONSHIP_CLASS_INVALID",))

    def test_manifest_covers_organization_codes_and_derivations(self) -> None:
        rules = yaml.safe_load((ROOT / "organization-rules.yaml").read_text(encoding="utf-8"))["rules"]
        validation_ids = {item["id"] for item in rules if item.get("kind", "validation") == "validation"}
        derivation_ids = {item["id"] for item in rules if item.get("kind") == "derivation"}
        self.assertEqual(validation_ids, set(ORGANIZATION_ERROR_CODES))
        self.assertEqual(derivation_ids, set(ORGANIZATION_DERIVATION_RULES))
        self.assertTrue(set(ERROR_CODES))
        self.assertTrue(set(DERIVATION_RULES))


if __name__ == "__main__":
    unittest.main()
