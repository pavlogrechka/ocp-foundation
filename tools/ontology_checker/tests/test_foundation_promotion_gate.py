from __future__ import annotations

import copy
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

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
from ocp_checker.event_promotion_selection import validate_event_promotion_selection  # noqa: E402
from ocp_checker.event_stable_surface import validate_event_stable_surface  # noqa: E402
from ocp_checker.foundation_promotion_reassessment import (  # noqa: E402
    validate_foundation_promotion_reassessment,
)


EXPECTED_STEPS = (
    "CANDIDATE_BOARD_SELECTION", "DOCUMENT_PROMOTION", "CONCEPT_CANONICALIZATION",
)
EXPECTED_CANDIDATES = {"OCP-005", "OCP-006", "OCP-010"}
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
            copied = destination / primary.relative_to(ROOT)
            copied.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(primary, copied)

    def write_payload(self, root: Path, payload: dict) -> None:
        (root / self.gate_path).write_text(
            yaml.safe_dump(payload, sort_keys=False), encoding="utf-8"
        )

    def mutate_subject_status(self, root: Path, document_id: str, document: str, concept: str) -> None:
        payload = self.payload(root)
        entry = next(item for item in payload["candidates"] if item["document_id"] == document_id)
        primary = root / entry["primary"]
        text = primary.read_text(encoding="utf-8")
        old_document = next(line for line in text.splitlines() if line.startswith("Status:"))
        old_concept = next(line for line in text.splitlines() if line.startswith("Concept-Status:"))
        primary.write_text(
            text.replace(old_document, f"Status: {document}", 1).replace(
                old_concept, f"Concept-Status: {concept}", 1
            ), encoding="utf-8",
        )
        entry["expected_document_status"] = document
        entry["expected_concept_status"] = concept
        self.write_payload(root, payload)

    def append_assignment_cycle(self, root: Path, states: tuple[str, str, str]) -> None:
        payload = self.payload(root)
        steps = dict(zip(EXPECTED_STEPS, states))
        cycle = {
            "cycle_id": "ASSIGNMENT_T6", "candidate_id": "OCP-005", "slot": "T6",
            "steps": steps,
            "evidence": {
                step: f"SYNTHETIC_{step}_ACT"
                for step, state in steps.items() if state == "completed"
            },
        }
        existing = next(
            (index for index, row in enumerate(payload["cycles"]) if row["candidate_id"] == "OCP-005"),
            None,
        )
        if existing is None:
            payload["cycles"].append(cycle)
        else:
            payload["cycles"][existing] = cycle
        payload["cycle_protocol"]["active_cycle_id"] = (
            None if all(state == "completed" for state in states) else "ASSIGNMENT_T6"
        )
        self.write_payload(root, payload)

    def test_repository_records_completed_event_and_active_assignment_selection_cycle(self) -> None:
        result = validate_foundation_promotion_gate(ROOT)
        self.assertTrue(result.valid, result.errors)
        payload = self.payload()
        self.assertEqual(payload["schema_version"], 5)
        self.assertEqual(payload["cycle_protocol"]["active_cycle_id"], "ASSIGNMENT_T6")
        self.assertEqual([item["candidate_id"] for item in payload["cycles"]], ["OCP-010", "OCP-005"])
        self.assertEqual(
            tuple(payload["cycles"][1]["steps"].values()),
            ("completed", "completed", "pending"),
        )
        self.assertEqual(set(payload["candidates"][0]), foundation_promotion_gate.CANDIDATE_KEYS)

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        categories = (
            "STEP_STATES", "CANDIDATE_IDS", "ALLOWED_L2_RESULTS", "ALLOWED_STATUS_PAIRS",
            "SLOT_IDS", "MAP_KEYS", "PROTOCOL_KEYS", "CYCLE_KEYS", "CANDIDATE_KEYS",
        )
        for attribute in categories:
            values = getattr(foundation_promotion_gate, attribute)
            for value in sorted(values, key=str):
                with self.subTest(attribute=attribute, value=value), patch.object(
                    foundation_promotion_gate, attribute, values - {value}
                ):
                    self.assertFalse(validate_foundation_promotion_gate(ROOT).valid)
        for value in EXPECTED_STEPS:
            with self.subTest(attribute="CYCLE_STEPS", value=value), patch.object(
                foundation_promotion_gate,
                "CYCLE_STEPS",
                tuple(item for item in EXPECTED_STEPS if item != value),
            ):
                self.assertFalse(validate_foundation_promotion_gate(ROOT).valid)

    def assert_assignment_cycle_reachable(
        self, states: tuple[str, str, str], document: str, concept: str
    ) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            if document == "Canonical":
                self.mutate_subject_status(root, "OCP-005", document, concept)
                payload = self.payload(root)
                constraint = next(
                    item for item in payload["candidates"] if item["document_id"] == "OCP-006"
                )
                constraint["expected_l2"] = "pass"
                constraint["l2_blockers"] = []
                self.write_payload(root, payload)
            self.append_assignment_cycle(root, states)
            result = validate_foundation_promotion_gate(root)
            self.assertTrue(result.valid, result.errors)

    def test_current_cycle_document_promoted_state_is_reachable_without_code_change(self) -> None:
        self.assert_assignment_cycle_reachable(
            ("completed", "completed", "pending"), "Canonical", "Accepted"
        )

    def test_next_cycle_document_promoted_state_is_reachable_without_code_change(self) -> None:
        self.assert_assignment_cycle_reachable(
            ("completed", "completed", "pending"), "Canonical", "Accepted"
        )

    def test_next_cycle_fully_completed_state_is_reachable_without_code_change(self) -> None:
        self.assert_assignment_cycle_reachable(
            ("completed", "completed", "completed"), "Canonical", "Canonical"
        )

    def test_historical_event_witnesses_remain_valid(self) -> None:
        self.assertTrue(validate_event_stable_surface(ROOT).valid)
        self.assertTrue(validate_foundation_promotion_reassessment(ROOT).valid)
        self.assertTrue(validate_event_promotion_selection(ROOT).valid)

    def test_skipping_any_next_cycle_step_fails(self) -> None:
        attacks = (
            ("pending", "completed", "pending"),
            ("completed", "pending", "completed"),
            ("pending", "completed", "completed"),
        )
        for states in attacks:
            with self.subTest(states=states), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                self.append_assignment_cycle(root, states)
                errors = validate_foundation_promotion_gate(root).errors
                self.assertTrue(
                    FOUNDATION_PROMOTION_GATE_MAP_INVALID in errors
                    or FOUNDATION_PROMOTION_GATE_SELECTION_REQUIRED in errors,
                    errors,
                )

    def test_only_last_cycle_may_be_active_and_active_id_is_exact(self) -> None:
        for mutation in ("missing_active", "two_incomplete", "completed_marked_active"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                self.append_assignment_cycle(root, ("completed", "pending", "pending"))
                payload = self.payload(root)
                if mutation == "missing_active":
                    payload["cycle_protocol"]["active_cycle_id"] = None
                elif mutation == "two_incomplete":
                    payload["cycles"][0]["steps"]["CONCEPT_CANONICALIZATION"] = "pending"
                    payload["cycles"][0]["evidence"].pop("CONCEPT_CANONICALIZATION")
                else:
                    payload["cycle_protocol"]["active_cycle_id"] = "EVENT_T6"
                self.write_payload(root, payload)
                self.assertIn(
                    FOUNDATION_PROMOTION_GATE_MAP_INVALID,
                    validate_foundation_promotion_gate(root).errors,
                )

    def test_unselected_canonical_candidate_still_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            payload = self.payload(root)
            payload["cycles"] = [row for row in payload["cycles"] if row["candidate_id"] != "OCP-005"]
            payload["cycle_protocol"]["active_cycle_id"] = None
            self.write_payload(root, payload)
            self.mutate_subject_status(root, "OCP-005", "Canonical", "Accepted")
            payload = self.payload(root)
            constraint = next(item for item in payload["candidates"] if item["document_id"] == "OCP-006")
            constraint["expected_l2"] = "pass"
            constraint["l2_blockers"] = []
            self.write_payload(root, payload)
            self.assertIn(
                FOUNDATION_PROMOTION_GATE_SELECTION_REQUIRED,
                validate_foundation_promotion_gate(root).errors,
            )

    def test_selected_candidate_still_requires_live_l2_pass(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            payload = self.payload(root)
            payload["cycles"] = [row for row in payload["cycles"] if row["candidate_id"] != "OCP-005"]
            payload["cycles"].append({
                "cycle_id": "CONSTRAINT_T7", "candidate_id": "OCP-006", "slot": "T7",
                "steps": dict(zip(EXPECTED_STEPS, ("completed", "pending", "pending"))),
                "evidence": {"CANDIDATE_BOARD_SELECTION": "SYNTHETIC_SELECTION_ACT"},
            })
            payload["cycle_protocol"]["active_cycle_id"] = "CONSTRAINT_T7"
            self.mutate_subject_status(root, "OCP-005", "Accepted", "Accepted")
            payload = self.payload(root)
            assignment = next(item for item in payload["candidates"] if item["document_id"] == "OCP-005")
            assignment["expected_document_status"] = "Accepted"
            constraint = next(item for item in payload["candidates"] if item["document_id"] == "OCP-006")
            constraint["expected_l2"] = "pass"
            constraint["l2_blockers"] = []
            self.write_payload(root, payload)
            self.assertIn(
                FOUNDATION_PROMOTION_GATE_L2_MISMATCH,
                validate_foundation_promotion_gate(root).errors,
            )

    def test_each_declared_dependency_and_status_is_live(self) -> None:
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


if __name__ == "__main__":
    unittest.main()
