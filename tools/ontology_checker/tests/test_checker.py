from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import (  # noqa: E402
    assignment_effective_at,
    constraint_set_decision,
    derived_participates_in,
    effective_constraint_result,
    load_fixture,
    validate_fixture,
)


class FixtureContractTests(unittest.TestCase):
    def test_all_fixtures_match_expected_validity(self) -> None:
        for path in sorted((ROOT / "fixtures").rglob("*.yaml")):
            with self.subTest(path=path):
                fixture = load_fixture(path)
                result = validate_fixture(fixture)
                expected = fixture["expected"]
                self.assertEqual(result.valid, expected["valid"])
                self.assertTrue(set(expected.get("error_codes", [])).issubset(set(result.errors)))

    def test_assignment_reference_derivations(self) -> None:
        fixture = load_fixture(ROOT / "fixtures/assignment/valid-established.yaml")
        assignment = fixture["entity"]
        self.assertTrue(assignment_effective_at(assignment, "2026-08-02T10:30:00Z"))
        self.assertTrue(derived_participates_in([assignment], "R-001", "OP-001", "2026-08-02T10:30:00Z"))
        self.assertFalse(assignment_effective_at(assignment, "2026-08-02T09:59:59Z"))

        invalid = load_fixture(ROOT / "fixtures/assignment/invalid-silent-terminal.yaml")["entity"]
        self.assertTrue(assignment_effective_at(invalid, "2026-08-02T11:30:00Z"))

    def test_not_applicable_defense_in_depth(self) -> None:
        fixture = load_fixture(ROOT / "fixtures/constraint/invalid-applicable-not-applicable.yaml")
        constraint = fixture["entity"]
        context = fixture["contexts"][0]
        result = validate_fixture(fixture)
        self.assertIn("CONSTRAINT_NOT_APPLICABLE_CONTRADICTION", result.errors)
        self.assertEqual(effective_constraint_result(constraint, context), "indeterminate")
        self.assertEqual(constraint_set_decision([constraint], context), "inadmissible")

    def test_advisory_uncertainty_requires_review_not_inadmissible(self) -> None:
        fixture = load_fixture(ROOT / "fixtures/constraint/advisory-indeterminate.yaml")
        constraint = fixture["entity"]
        context = fixture["contexts"][0]
        self.assertEqual(constraint_set_decision([constraint], context), "review_required")


if __name__ == "__main__":
    unittest.main()
