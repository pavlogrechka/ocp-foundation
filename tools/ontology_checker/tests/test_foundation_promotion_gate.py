from __future__ import annotations

from pathlib import Path
from unittest.mock import patch
import shutil
import sys
import tempfile
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools/ontology_checker"))

from ocp_checker import foundation_promotion_gate  # noqa: E402
from ocp_checker.foundation_promotion_gate import (  # noqa: E402
    FOUNDATION_PROMOTION_GATE_CANDIDATE_DRIFT,
    FOUNDATION_PROMOTION_GATE_L2_MISMATCH,
    FOUNDATION_PROMOTION_GATE_MAP_INVALID,
    FOUNDATION_PROMOTION_GATE_SELECTION_REQUIRED,
    validate_foundation_promotion_gate,
)


EXPECTED_COMPLETED_STEPS = {
    "T0", "T1", "T2", "T3", "AD-016C", "AD-016D", "T4", "T5", "AD-016Y", "AD-016Z", "Y10D"
}
EXPECTED_COMPLETED_STEP_ORDER = (
    "T0", "T1", "T2", "T3", "AD-016C", "AD-016D", "T4", "T5", "AD-016Y", "AD-016Z", "Y10D"
)
EXPECTED_NEXT_GATES = {
    "POST_DISCOVERY_REASSESSMENT", "CANDIDATE_BOARD_SELECTION"
}
EXPECTED_NEXT_GATE_ORDER = (
    "POST_DISCOVERY_REASSESSMENT", "CANDIDATE_BOARD_SELECTION"
)
EXPECTED_CANDIDATES = {"OCP-005", "OCP-006", "OCP-010"}
EXPECTED_L2_RESULTS = {"pass", "fail"}
EXPECTED_DEPENDENCIES = {
    "OCP-005": ("OCP-000", "OCP-001", "OCP-002", "OCP-003", "OCP-004"),
    "OCP-006": ("OCP-000", "OCP-001", "OCP-002", "OCP-003", "OCP-004", "OCP-005"),
    "OCP-010": ("OCP-000", "OCP-001", "OCP-002", "OCP-004", "OCP-008"),
}


class FoundationPromotionGateTests(unittest.TestCase):
    gate_path = Path("architecture/foundation-promotion-gate.yaml")

    def payload(self, root: Path = ROOT) -> dict:
        return yaml.safe_load((root / self.gate_path).read_text(encoding="utf-8"))

    def copy_inputs(self, destination: Path) -> None:
        target = destination / self.gate_path
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / self.gate_path, target)
        for primary in (ROOT / "docs").glob("*/README.md"):
            relative = primary.relative_to(ROOT)
            copied = destination / relative
            copied.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(primary, copied)

    def write_payload(self, root: Path, payload: dict) -> None:
        (root / self.gate_path).write_text(
            yaml.safe_dump(payload, sort_keys=False), encoding="utf-8"
        )

    def test_repository_foundation_promotion_gate_is_valid(self) -> None:
        self.assertTrue(validate_foundation_promotion_gate(ROOT).valid)
        payload = self.payload()
        self.assertEqual(set(payload["sequence"]["completed_steps"]), EXPECTED_COMPLETED_STEPS)
        self.assertEqual(
            set(payload["sequence"]["required_before_promotion"]), EXPECTED_NEXT_GATES
        )
        self.assertEqual(
            {entry["document_id"] for entry in payload["candidates"]}, EXPECTED_CANDIDATES
        )

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        categories = (
            ("REQUIRED_COMPLETED_STEPS", EXPECTED_COMPLETED_STEPS),
            ("REQUIRED_NEXT_GATES", EXPECTED_NEXT_GATES),
            ("CANDIDATE_IDS", EXPECTED_CANDIDATES),
            ("ALLOWED_L2_RESULTS", EXPECTED_L2_RESULTS),
        )
        for attribute, expected_values in categories:
            production_values = getattr(foundation_promotion_gate, attribute)
            self.assertEqual(production_values, frozenset(expected_values))
            for value in sorted(expected_values):
                with self.subTest(attribute=attribute, value=value), patch.object(
                    foundation_promotion_gate,
                    attribute,
                    production_values - {value},
                ):
                    self.assertIn(
                        FOUNDATION_PROMOTION_GATE_MAP_INVALID,
                        validate_foundation_promotion_gate(ROOT).errors,
                    )

        ordered_categories = (
            ("REQUIRED_COMPLETED_STEP_ORDER", EXPECTED_COMPLETED_STEP_ORDER),
            ("REQUIRED_NEXT_GATE_ORDER", EXPECTED_NEXT_GATE_ORDER),
        )
        for attribute, expected_values in ordered_categories:
            production_values = getattr(foundation_promotion_gate, attribute)
            self.assertEqual(production_values, expected_values)
            for value in expected_values:
                with self.subTest(attribute=attribute, value=value), patch.object(
                    foundation_promotion_gate,
                    attribute,
                    tuple(item for item in production_values if item != value),
                ):
                    self.assertIn(
                        FOUNDATION_PROMOTION_GATE_MAP_INVALID,
                        validate_foundation_promotion_gate(ROOT).errors,
                    )

    def test_each_candidate_requires_prior_selection_before_canonical(self) -> None:
        for document_id in sorted(EXPECTED_CANDIDATES):
            with self.subTest(document_id=document_id), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                entry = next(
                    item for item in self.payload(root)["candidates"] if item["document_id"] == document_id
                )
                primary = root / entry["primary"]
                text = primary.read_text(encoding="utf-8")
                text = text.replace("Status: Draft", "Status: Canonical", 1)
                text = text.replace("Version: 0.", "Version: 1.", 1)
                primary.write_text(text, encoding="utf-8")
                self.assertIn(
                    FOUNDATION_PROMOTION_GATE_SELECTION_REQUIRED,
                    validate_foundation_promotion_gate(root).errors,
                )

    def test_each_declared_dependency_and_l2_result_is_live(self) -> None:
        for document_id, dependencies in EXPECTED_DEPENDENCIES.items():
            for dependency in dependencies:
                with self.subTest(document_id=document_id, dependency=dependency), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    entry = next(
                        item for item in self.payload(root)["candidates"] if item["document_id"] == document_id
                    )
                    primary = root / entry["primary"]
                    text = primary.read_text(encoding="utf-8")
                    old = next(line for line in text.splitlines() if line.startswith("Depends-On:"))
                    values = [item.strip() for item in old.split(":", 1)[1].split(",")]
                    values.remove(dependency)
                    primary.write_text(
                        text.replace(old, "Depends-On: " + ", ".join(values), 1), encoding="utf-8"
                    )
                    self.assertIn(
                        FOUNDATION_PROMOTION_GATE_CANDIDATE_DRIFT,
                        validate_foundation_promotion_gate(root).errors,
                    )

        for document_id, dependency, new_status in (
            ("OCP-005", "OCP-004", "Draft"),
            ("OCP-006", "OCP-005", "Canonical"),
            ("OCP-010", "OCP-008", "Draft"),
        ):
            with self.subTest(document_id=document_id, l2_dependency=dependency), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                dependency_path = next((root / "docs").glob(f"{dependency[4:]}-*/README.md"))
                text = dependency_path.read_text(encoding="utf-8")
                old_status = next(line for line in text.splitlines() if line.startswith("Status:"))
                text = text.replace(old_status, f"Status: {new_status}", 1)
                dependency_path.write_text(text, encoding="utf-8")
                self.assertIn(
                    FOUNDATION_PROMOTION_GATE_L2_MISMATCH,
                    validate_foundation_promotion_gate(root).errors,
                )

    def test_candidate_document_and_concept_statuses_are_individually_live(self) -> None:
        for document_id in sorted(EXPECTED_CANDIDATES):
            for field, old, new in (
                ("document", "Status: Draft", "Status: Accepted"),
                ("concept", "Concept-Status: Accepted", "Concept-Status: Proposed"),
            ):
                with self.subTest(document_id=document_id, field=field), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    entry = next(
                        item for item in self.payload(root)["candidates"] if item["document_id"] == document_id
                    )
                    primary = root / entry["primary"]
                    text = primary.read_text(encoding="utf-8")
                    self.assertIn(old, text)
                    primary.write_text(text.replace(old, new, 1), encoding="utf-8")
                    self.assertIn(
                        FOUNDATION_PROMOTION_GATE_CANDIDATE_DRIFT,
                        validate_foundation_promotion_gate(root).errors,
                    )

    def test_completed_scope_cannot_regress_or_self_supply_selection(self) -> None:
        for mutation in ("regress_scope", "self_supply_selection"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                payload = self.payload(root)
                if mutation == "regress_scope":
                    payload["sequence"]["selected_next_scope_state"] = "absent"
                else:
                    payload["promotion_selections"] = ["OCP-010"]
                self.write_payload(root, payload)
                self.assertIn(
                    FOUNDATION_PROMOTION_GATE_MAP_INVALID,
                    validate_foundation_promotion_gate(root).errors,
                )


if __name__ == "__main__":
    unittest.main()
