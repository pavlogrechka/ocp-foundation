from __future__ import annotations

import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import DERIVATION_RULES, ERROR_CODES, load_fixture, validate_reference_fixture  # noqa: E402
from ocp_checker.organization import (  # noqa: E402
    ORGANIZATION_DERIVATION_RULES,
    ORGANIZATION_ERROR_CODES,
    graph_breakpoints,
    organization_relationship_successor_ids,
    validate_organization_dataset,
    validate_organization_graph,
)


class OrganizationCheckerTests(unittest.TestCase):
    def test_entity_fixtures_match_exact_errors(self) -> None:
        for path in sorted((ROOT / "fixtures/organization").glob("*.yaml")):
            with self.subTest(path=path):
                fixture = load_fixture(path)
                result = validate_reference_fixture(fixture)
                self.assertEqual(result.valid, fixture["expected"]["valid"])
                self.assertEqual(set(result.errors), set(fixture["expected"].get("error_codes", [])))

    def test_every_q2_case_has_exact_expected_errors(self) -> None:
        fixture = load_fixture(ROOT / "fixtures/organization/mandatory-q2-cases.yaml")
        for name, case in fixture["cases"].items():
            with self.subTest(case=name):
                actual = validate_organization_dataset(
                    case.get("organizations") or [],
                    case.get("relationships") or [],
                    case.get("relationship_kind_profiles") or [],
                    case.get("validation_scope_ref"),
                )
                self.assertEqual(set(actual.errors), set(case["expected_error_codes"]))

    def test_graph_regression_fixtures(self) -> None:
        root = ROOT / "regression_fixtures/organization_graph"
        for path in sorted(root.glob("*.yaml")):
            with self.subTest(path=path):
                fixture = yaml.safe_load(path.read_text(encoding="utf-8"))
                result = validate_organization_graph(fixture["records"], fixture.get("reference_time"))
                self.assertEqual(set(result.errors), set(fixture["expected_error_codes"]))

        q2 = load_fixture(ROOT / "fixtures/organization/mandatory-q2-cases.yaml")
        cycle_case = q2["cases"]["all_time_structural_cycle_rejects"]
        for scope, relationship in zip(("SCOPE-A", "SCOPE-B"), cycle_case["relationships"]):
            with self.subTest(scope=scope):
                self.assertTrue(validate_organization_dataset(
                    cycle_case["organizations"],
                    [relationship],
                    cycle_case["relationship_kind_profiles"],
                    scope,
                ).valid)

    def test_transient_cycle_is_found_by_sweep_but_not_after_interval(self) -> None:
        fixture = yaml.safe_load((ROOT / "regression_fixtures/organization_graph/transient-cycle.yaml").read_text(encoding="utf-8"))
        records = fixture["records"]
        self.assertTrue(validate_organization_graph(records, "2026-04-02T00:00:00Z").valid)
        self.assertIn("ORGANIZATION_STRUCTURAL_CYCLE", validate_organization_graph(records).errors)
        self.assertGreaterEqual(len(graph_breakpoints(records)), 5)

    def test_unknown_class_cannot_bypass_structural_governance(self) -> None:
        fixture = load_fixture(ROOT / "fixtures/organization/invalid-relationship-class.yaml")
        result = validate_reference_fixture(fixture)
        self.assertEqual(result.errors, ("ORGANIZATION_RELATIONSHIP_CLASS_INVALID",))

    def test_branch_order_exposes_all_successors_and_never_elects_a_head(self) -> None:
        fixture = load_fixture(ROOT / "fixtures/organization/mandatory-q2-cases.yaml")
        records = fixture["cases"]["branching_overlap_is_valid"]["relationships"]
        expected = ("REL-SUCCESSOR-B", "REL-SUCCESSOR-C")
        self.assertEqual(organization_relationship_successor_ids(records, "REL-A-B"), expected)
        self.assertEqual(organization_relationship_successor_ids(reversed(records), "REL-A-B"), expected)
        self.assertNotIn("head", ORGANIZATION_DERIVATION_RULES)

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
