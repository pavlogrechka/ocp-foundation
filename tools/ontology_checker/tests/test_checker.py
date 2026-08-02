from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import (  # noqa: E402
    DERIVATION_RULES,
    ERROR_CODES,
    assignment_effective_at,
    constraint_set_decision,
    derived_participates_in,
    effective_constraint_result,
    load_fixture,
    validate_fixture,
    validate_repository,
)


class FixtureContractTests(unittest.TestCase):
    def test_all_fixtures_match_exact_expected_errors(self) -> None:
        for path in sorted((ROOT / "fixtures").rglob("*.yaml")):
            with self.subTest(path=path):
                fixture = load_fixture(path)
                result = validate_fixture(fixture)
                expected = fixture["expected"]
                self.assertEqual(result.valid, expected["valid"])
                self.assertEqual(set(result.errors), set(expected.get("error_codes", [])))

    def test_assignment_reference_derivations(self) -> None:
        fixture = load_fixture(ROOT / "fixtures/assignment/valid-established.yaml")
        assignment = fixture["entity"]
        self.assertTrue(assignment_effective_at(assignment, "2026-08-02T10:30:00Z"))
        self.assertTrue(
            derived_participates_in([assignment], "R-001", "OP-001", "2026-08-02T10:30:00Z")
        )
        self.assertFalse(assignment_effective_at(assignment, "2026-08-02T09:59:59Z"))

        invalid = load_fixture(ROOT / "fixtures/assignment/invalid-silent-terminal.yaml")["entity"]
        self.assertTrue(assignment_effective_at(invalid, "2026-08-02T11:30:00Z"))

    def test_not_applicable_defense_in_depth(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/constraint/invalid-applicable-not-applicable.yaml"
        )
        constraint = fixture["entity"]
        context = fixture["contexts"][0]
        version_ref = fixture["reference"]["constraint_version_ref"]
        result = validate_fixture(fixture)
        self.assertIn("CONSTRAINT_NOT_APPLICABLE_CONTRADICTION", result.errors)
        self.assertEqual(
            effective_constraint_result(constraint, context, version_ref),
            "indeterminate",
        )
        self.assertEqual(
            constraint_set_decision(
                [constraint],
                context,
                {constraint["constraint_id"]: version_ref},
            ),
            "inadmissible",
        )

    def test_advisory_uncertainty_requires_review_not_inadmissible(self) -> None:
        fixture = load_fixture(ROOT / "fixtures/constraint/advisory-indeterminate.yaml")
        constraint = fixture["entity"]
        context = fixture["contexts"][0]
        version_ref = fixture["reference"]["constraint_version_ref"]
        self.assertEqual(
            constraint_set_decision(
                [constraint],
                context,
                {constraint["constraint_id"]: version_ref},
            ),
            "review_required",
        )

    def test_stale_version_cannot_make_decision_permissive_or_order_dependent(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/constraint/stale-version-permissive.yaml"
        )
        constraint = fixture["entity"]
        context = fixture["contexts"][0]
        version_ref = fixture["reference"]["constraint_version_ref"]
        versions = {constraint["constraint_id"]: version_ref}

        self.assertTrue(validate_fixture(fixture).valid)
        self.assertEqual(
            effective_constraint_result(constraint, context, version_ref),
            "violated",
        )
        self.assertEqual(
            constraint_set_decision([constraint], context, versions),
            "inadmissible",
        )

        constraint["evaluation_records"].reverse()
        self.assertEqual(
            effective_constraint_result(constraint, context, version_ref),
            "violated",
        )
        self.assertEqual(
            constraint_set_decision([constraint], context, versions),
            "inadmissible",
        )

    def test_rules_manifest_covers_every_error_and_derivation(self) -> None:
        manifest = yaml.safe_load((ROOT / "rules.yaml").read_text(encoding="utf-8"))
        rules = manifest["rules"]
        validation_ids = {
            item["id"] for item in rules if item.get("kind", "validation") == "validation"
        }
        derivation_ids = {
            item["id"] for item in rules if item.get("kind") == "derivation"
        }
        self.assertEqual(validation_ids, set(ERROR_CODES))
        self.assertEqual(derivation_ids, set(DERIVATION_RULES))

    def test_repository_status_sync(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "docs/000-operational-ontology").mkdir(parents=True)
            (root / "docs/002-concept-taxonomy").mkdir(parents=True)
            (root / "docs/003-resource-concept").mkdir(parents=True)

            (root / "docs/000-operational-ontology/README.md").write_text(
                "| Concept | Status | Specification / Decision |\n"
                "|---|---|---|\n"
                "| Resource | Accepted | OCP-003 |\n",
                encoding="utf-8",
            )
            (root / "docs/002-concept-taxonomy/README.md").write_text(
                "---\n"
                "Concept-Statuses:\n"
                "  Resource: Accepted\n"
                "---\n",
                encoding="utf-8",
            )
            (root / "docs/003-resource-concept/README.md").write_text(
                "---\n"
                "Defines-Concepts: Resource\n"
                "Concept-Status: Accepted\n"
                "---\n",
                encoding="utf-8",
            )
            self.assertTrue(validate_repository(root).valid)


if __name__ == "__main__":
    unittest.main()
