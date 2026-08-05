from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import (  # noqa: E402
    load_fixture,
    validate_objective_correction_fixture,
    validate_operation,
    validate_reference_fixture,
)


class ObjectiveReviewFixTests(unittest.TestCase):
    def test_supersession_cycle_is_rejected_at_dataset_level(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/objective/invalid-supersession-cycle.yaml"
        )
        self.assertEqual(
            set(validate_reference_fixture(fixture).errors),
            {"OBJECTIVE_SUPERSESSION_CYCLE"},
        )

    def test_draft_unresolved_reference_is_valid_authoring_state(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/operation/valid-draft-unresolved-objective.yaml"
        )
        self.assertTrue(validate_reference_fixture(fixture).valid)

    def test_strict_correction_preserves_old_operation_and_assessment(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/objective/valid-strict-correction-consumers.yaml"
        )
        self.assertTrue(validate_reference_fixture(fixture).valid)

    def test_strict_correction_evidence_is_order_independent(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/objective/valid-strict-correction-consumers.yaml"
        )
        fixture["objectives"] = list(reversed(fixture["objectives"]))
        self.assertTrue(validate_objective_correction_fixture(fixture).valid)

    def test_editorially_similar_duplicate_identity_is_rejected(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/objective/invalid-duplicate-editorial-identity.yaml"
        )
        self.assertEqual(
            set(validate_reference_fixture(fixture).errors),
            {"OBJECTIVE_IDENTITY_DUPLICATE"},
        )

    def test_public_operation_validator_delegates_to_fixture_contract(self) -> None:
        operation = {
            "operation_id": "OP-DELEGATION-001",
            "lifecycle_stage": "Planned",
            "objective_refs": ["OBJ-MISSING"],
        }
        self.assertEqual(
            set(validate_operation(operation, {"objectives": []}).errors),
            {"OPERATION_OBJECTIVE_REFERENCE_UNRESOLVED"},
        )


if __name__ == "__main__":
    unittest.main()
