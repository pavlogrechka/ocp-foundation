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
    validate_reference_fixture,
    validate_repository,
)
from ocp_checker.organization import validate_organization, validate_organization_relationship  # noqa: E402


def validate_any_fixture(fixture: dict):
    concept = fixture.get("concept")
    if concept == "Organization":
        return validate_organization(fixture.get("entity") or {})
    if concept == "OrganizationRelationshipRecord":
        return validate_organization_relationship(fixture.get("entity") or {})
    return validate_reference_fixture(fixture)


class FixtureContractTests(unittest.TestCase):
    def test_all_fixtures_match_exact_expected_errors(self) -> None:
        for path in sorted((ROOT / "fixtures").rglob("*.yaml")):
            with self.subTest(path=path):
                fixture = load_fixture(path)
                result = validate_any_fixture(fixture)
                expected = fixture["expected"]
                self.assertEqual(result.valid, expected["valid"])
                self.assertEqual(set(result.errors), set(expected.get("error_codes", [])))

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
        constraint, context = fixture["entity"], fixture["contexts"][0]
        version_ref = fixture["reference"]["constraint_version_ref"]
        result = validate_reference_fixture(fixture)
        self.assertIn("CONSTRAINT_NOT_APPLICABLE_CONTRADICTION", result.errors)
        self.assertEqual(effective_constraint_result(constraint, context, version_ref), "indeterminate")
        self.assertEqual(constraint_set_decision([constraint], context, {constraint["constraint_id"]: version_ref}), "inadmissible")

    def test_advisory_uncertainty_requires_review(self) -> None:
        fixture = load_fixture(ROOT / "fixtures/constraint/advisory-indeterminate.yaml")
        constraint, context = fixture["entity"], fixture["contexts"][0]
        version_ref = fixture["reference"]["constraint_version_ref"]
        self.assertEqual(constraint_set_decision([constraint], context, {constraint["constraint_id"]: version_ref}), "review_required")

    def test_stale_version_is_not_permissive_or_order_dependent(self) -> None:
        fixture = load_fixture(ROOT / "fixtures/constraint/stale-version-permissive.yaml")
        constraint, context = fixture["entity"], fixture["contexts"][0]
        version_ref = fixture["reference"]["constraint_version_ref"]
        versions = {constraint["constraint_id"]: version_ref}
        self.assertTrue(validate_reference_fixture(fixture).valid)
        self.assertEqual(effective_constraint_result(constraint, context, version_ref), "violated")
        self.assertEqual(constraint_set_decision([constraint], context, versions), "inadmissible")
        constraint["evaluation_records"].reverse()
        self.assertEqual(effective_constraint_result(constraint, context, version_ref), "violated")

    def test_objective_bootstrap_operation_uses_resolvable_reference(self) -> None:
        fixture = load_fixture(ROOT / "fixtures/operation/valid-planned-objective.yaml")
        self.assertTrue(validate_reference_fixture(fixture).valid)

    def test_objective_and_explicit_intent_conflict_is_fail_safe(self) -> None:
        fixture = {
            "concept": "Operation",
            "references": {
                "objectives": [
                    {
                        "objective_id": "OBJ-003",
                        "statement": "Preserve access to the route",
                        "created_at": "2026-08-03T03:15:00Z",
                        "provenance_ref": "SOURCE-003",
                    }
                ]
            },
            "entity": {
                "operation_id": "OP-CONFLICT-001",
                "lifecycle_stage": "Planned",
                "objective_refs": ["OBJ-003"],
                "explicit_intent_record": {
                    "intent_id": "INT-003",
                    "statement": "Preserve access to the route",
                    "validation_status": "passed",
                    "validation_rule_ref": "RULE-INTENT-001",
                    "validated_at": "2026-08-03T03:20:00Z",
                },
            },
        }
        self.assertEqual(
            set(validate_reference_fixture(fixture).errors),
            {"OPERATION_INTENT_REPRESENTATION_CONFLICT"},
        )

    def test_unresolved_objective_reference_fails_closed(self) -> None:
        fixture = {
            "concept": "Operation",
            "entity": {
                "operation_id": "OP-OBJ-002",
                "lifecycle_stage": "Planned",
                "objective_refs": ["OBJ-MISSING"],
            },
        }
        self.assertEqual(
            set(validate_reference_fixture(fixture).errors),
            {"OPERATION_OBJECTIVE_REFERENCE_UNRESOLVED"},
        )

    def test_draft_may_temporarily_hold_both_intent_branches(self) -> None:
        fixture = {
            "concept": "Operation",
            "references": {
                "objectives": [
                    {
                        "objective_id": "OBJ-DRAFT-001",
                        "statement": "Draft intended outcome",
                        "created_at": "2026-08-03T03:25:00Z",
                        "provenance_ref": "SOURCE-DRAFT-001",
                    }
                ]
            },
            "entity": {
                "operation_id": "OP-DRAFT-002",
                "lifecycle_stage": "Draft",
                "objective_refs": ["OBJ-DRAFT-001"],
                "explicit_intent_record": {
                    "intent_id": "INT-DRAFT-001",
                    "statement": "Draft fallback intent",
                    "validation_status": "not_evaluated",
                },
            },
        }
        self.assertTrue(validate_reference_fixture(fixture).valid)

    def test_objective_cannot_supersede_itself(self) -> None:
        fixture = {
            "concept": "Objective",
            "entity": {
                "objective_id": "OBJ-002",
                "statement": "Establish a protected transit corridor",
                "created_at": "2026-08-03T03:05:00Z",
                "provenance_ref": "SOURCE-002",
                "supersedes_objective_ref": "OBJ-002",
            },
        }
        self.assertEqual(
            set(validate_reference_fixture(fixture).errors),
            {"OBJECTIVE_SELF_SUPERSESSION"},
        )

    def test_core_rules_manifest_is_complete(self) -> None:
        rules = yaml.safe_load((ROOT / "rules.yaml").read_text(encoding="utf-8"))["rules"]
        validation_ids = {item["id"] for item in rules if item.get("kind", "validation") == "validation"}
        derivation_ids = {item["id"] for item in rules if item.get("kind") == "derivation"}
        self.assertEqual(validation_ids, set(ERROR_CODES))
        self.assertEqual(derivation_ids, set(DERIVATION_RULES))

    def test_repository_status_sync(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "docs/000-operational-ontology").mkdir(parents=True)
            (root / "docs/002-concept-taxonomy").mkdir(parents=True)
            (root / "docs/003-resource-concept").mkdir(parents=True)
            (root / "docs/000-operational-ontology/README.md").write_text(
                "| Concept | Status | Specification / Decision |\n|---|---|---|\n| Resource | Accepted | OCP-003 |\n",
                encoding="utf-8",
            )
            (root / "docs/002-concept-taxonomy/README.md").write_text(
                "---\nConcept-Statuses:\n  Resource: Accepted\n---\n", encoding="utf-8"
            )
            (root / "docs/003-resource-concept/README.md").write_text(
                "---\nDefines-Concepts: Resource\nConcept-Status: Accepted\n---\n", encoding="utf-8"
            )
            self.assertTrue(validate_repository(root).valid)

    def test_repository_status_sync_rejects_missing_taxonomy_projection(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "docs/000-operational-ontology").mkdir(parents=True)
            (root / "docs/002-concept-taxonomy").mkdir(parents=True)
            (root / "docs/003-resource-concept").mkdir(parents=True)
            (root / "docs/000-operational-ontology/README.md").write_text(
                "| Concept | Status | Specification / Decision |\n|---|---|---|\n| Resource | Accepted | OCP-003 |\n",
                encoding="utf-8",
            )
            (root / "docs/002-concept-taxonomy/README.md").write_text(
                "---\nConcept-Statuses: {}\n---\n", encoding="utf-8"
            )
            (root / "docs/003-resource-concept/README.md").write_text(
                "---\nDefines-Concepts: Resource\nConcept-Status: Accepted\n---\n", encoding="utf-8"
            )
            self.assertEqual(set(validate_repository(root).errors), {"STATUS_TAXONOMY_MISSING"})

    def test_repository_status_sync_rejects_mismatched_taxonomy_projection(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "docs/000-operational-ontology").mkdir(parents=True)
            (root / "docs/002-concept-taxonomy").mkdir(parents=True)
            (root / "docs/003-resource-concept").mkdir(parents=True)
            (root / "docs/000-operational-ontology/README.md").write_text(
                "| Concept | Status | Specification / Decision |\n|---|---|---|\n| Resource | Accepted | OCP-003 |\n",
                encoding="utf-8",
            )
            (root / "docs/002-concept-taxonomy/README.md").write_text(
                "---\nConcept-Statuses:\n  Resource: Proposed\n---\n", encoding="utf-8"
            )
            (root / "docs/003-resource-concept/README.md").write_text(
                "---\nDefines-Concepts: Resource\nConcept-Status: Accepted\n---\n", encoding="utf-8"
            )
            self.assertEqual(set(validate_repository(root).errors), {"STATUS_MISMATCH"})

    def test_repository_status_sync_rejects_extra_taxonomy_projection(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "docs/000-operational-ontology").mkdir(parents=True)
            (root / "docs/002-concept-taxonomy").mkdir(parents=True)
            (root / "docs/003-resource-concept").mkdir(parents=True)
            (root / "docs/000-operational-ontology/README.md").write_text(
                "| Concept | Status | Specification / Decision |\n|---|---|---|\n| Resource | Accepted | OCP-003 |\n",
                encoding="utf-8",
            )
            (root / "docs/002-concept-taxonomy/README.md").write_text(
                "---\nConcept-Statuses:\n  Resource: Accepted\n  Environment: Proposed\n---\n",
                encoding="utf-8",
            )
            (root / "docs/003-resource-concept/README.md").write_text(
                "---\nDefines-Concepts: Resource\nConcept-Status: Accepted\n---\n", encoding="utf-8"
            )
            self.assertEqual(set(validate_repository(root).errors), {"STATUS_TAXONOMY_EXTRA"})

    def test_repository_status_sync_rejects_duplicate_taxonomy_projection(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "docs/000-operational-ontology").mkdir(parents=True)
            (root / "docs/002-concept-taxonomy").mkdir(parents=True)
            (root / "docs/003-resource-concept").mkdir(parents=True)
            (root / "docs/000-operational-ontology/README.md").write_text(
                "| Concept | Status | Specification / Decision |\n|---|---|---|\n| Resource | Accepted | OCP-003 |\n",
                encoding="utf-8",
            )
            (root / "docs/002-concept-taxonomy/README.md").write_text(
                "---\nConcept-Statuses:\n  Resource: Accepted\n  Resource: Accepted\n---\n",
                encoding="utf-8",
            )
            (root / "docs/003-resource-concept/README.md").write_text(
                "---\nDefines-Concepts: Resource\nConcept-Status: Accepted\n---\n", encoding="utf-8"
            )
            self.assertEqual(set(validate_repository(root).errors), {"STATUS_TAXONOMY_DUPLICATE"})


if __name__ == "__main__":
    unittest.main()
