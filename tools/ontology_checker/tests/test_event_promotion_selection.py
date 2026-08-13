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

from ocp_checker import event_promotion_selection  # noqa: E402
from ocp_checker.event_promotion_selection import (  # noqa: E402
    EVENT_PROMOTION_SELECTION_CONSUMER_DRIFT,
    EVENT_PROMOTION_SELECTION_EVIDENCE_DRIFT,
    EVENT_PROMOTION_SELECTION_GATE_DRIFT,
    EVENT_PROMOTION_SELECTION_MAP_INVALID,
    EVENT_PROMOTION_SELECTION_SUBJECT_DRIFT,
    validate_event_promotion_selection,
)
from ocp_checker.event_stable_surface import validate_event_stable_surface  # noqa: E402
from ocp_checker.foundation_promotion_reassessment import validate_foundation_promotion_reassessment  # noqa: E402


class EventPromotionSelectionTests(unittest.TestCase):
    map_path = Path("architecture/event-promotion-selection.yaml")
    gate_path = Path("architecture/foundation-promotion-gate.yaml")

    def copy_inputs(self, destination: Path) -> None:
        shutil.copytree(ROOT / "docs", destination / "docs")
        for relative in (
            self.map_path,
            self.gate_path,
            Path("architecture/foundation-promotion-reassessment.yaml"),
            Path("architecture/event-stable-surface.yaml"),
            Path("tools/ontology_checker/rules.yaml"),
            Path("tools/ontology_checker/ocp_checker/event.py"),
        ):
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)

    def payload(self, root: Path = ROOT) -> dict:
        return yaml.safe_load((root / self.map_path).read_text(encoding="utf-8"))

    def write_yaml(self, root: Path, relative: Path, payload: dict) -> None:
        (root / relative).write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")

    def test_repository_historical_selection_is_valid_after_promotion(self) -> None:
        self.assertTrue(validate_event_promotion_selection(ROOT).valid)
        payload = self.payload()
        self.assertEqual(payload["selected_unit"]["document_id"], "OCP-010")
        self.assertEqual(payload["selected_unit"]["expected_status"], "Draft")
        gate = yaml.safe_load((ROOT / self.gate_path).read_text(encoding="utf-8"))
        event_cycle = next(item for item in gate["cycles"] if item["candidate_id"] == "OCP-010")
        self.assertEqual(event_cycle["steps"]["CANDIDATE_BOARD_SELECTION"], "completed")
        self.assertEqual(event_cycle["steps"]["DOCUMENT_PROMOTION"], "completed")

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        categories = (
            "MAP_KEYS", "SELECTED_UNIT_KEYS", "COMPATIBILITY_KEYS", "CONSUMER_KEYS",
            "BLOCKER_KEYS", "MIGRATION_KEYS", "ROLLBACK_KEYS", "WITNESS_KEYS",
            "EVIDENCE_KEYS", "CONSUMER_IDS", "BLOCKER_IDS", "TREATMENTS",
            "PROMOTION_EFFECTS", "PRECONDITIONS", "DEPENDENCY_CRITERIA",
            "EXECUTABLE_LOCATIONS", "DESCRIPTIVE_LOCATIONS",
        )
        for attribute in categories:
            values = getattr(event_promotion_selection, attribute)
            for value in sorted(values):
                with self.subTest(attribute=attribute, value=value), patch.object(
                    event_promotion_selection, attribute, values - {value}
                ):
                    self.assertIn(
                        EVENT_PROMOTION_SELECTION_MAP_INVALID,
                        validate_event_promotion_selection(ROOT).errors,
                    )
        for blocker_id, expected in event_promotion_selection.EXPECTED_BLOCKERS.items():
            for index, value in enumerate(expected):
                mutated = dict(event_promotion_selection.EXPECTED_BLOCKERS)
                changed = list(expected)
                changed[index] = value + "-mutated"
                mutated[blocker_id] = tuple(changed)
                with self.subTest(blocker_id=blocker_id, value=value), patch.object(
                    event_promotion_selection, "EXPECTED_BLOCKERS", mutated
                ):
                    self.assertIn(EVENT_PROMOTION_SELECTION_MAP_INVALID, validate_event_promotion_selection(ROOT).errors)
        for consumer_id, expected in event_promotion_selection.EXPECTED_CONSUMERS.items():
            for index, value in enumerate(expected[:3]):
                mutated = dict(event_promotion_selection.EXPECTED_CONSUMERS)
                changed = list(expected)
                changed[index] = str(value) + "-mutated"
                mutated[consumer_id] = tuple(changed)
                with self.subTest(consumer_id=consumer_id, value=value), patch.object(
                    event_promotion_selection, "EXPECTED_CONSUMERS", mutated
                ):
                    self.assertIn(EVENT_PROMOTION_SELECTION_MAP_INVALID, validate_event_promotion_selection(ROOT).errors)
            for ref in expected[3]:
                mutated = dict(event_promotion_selection.EXPECTED_CONSUMERS)
                mutated[consumer_id] = (*expected[:3], tuple(item for item in expected[3] if item != ref))
                with self.subTest(consumer_id=consumer_id, ref=ref), patch.object(
                    event_promotion_selection, "EXPECTED_CONSUMERS", mutated
                ):
                    self.assertIn(EVENT_PROMOTION_SELECTION_MAP_INVALID, validate_event_promotion_selection(ROOT).errors)
        for blocker_id, items in event_promotion_selection.EXPECTED_EVIDENCE.items():
            for item_index, (path, tokens) in enumerate(items):
                for token in tokens:
                    mutated = copy.deepcopy(event_promotion_selection.EXPECTED_EVIDENCE)
                    changed = list(items)
                    changed[item_index] = (path, tuple(item for item in tokens if item != token))
                    mutated[blocker_id] = tuple(changed)
                    with self.subTest(blocker_id=blocker_id, token=token), patch.object(
                        event_promotion_selection, "EXPECTED_EVIDENCE", mutated
                    ):
                        self.assertIn(EVENT_PROMOTION_SELECTION_MAP_INVALID, validate_event_promotion_selection(ROOT).errors)

    def test_every_baseline_subject_and_evidence_object_value_is_individually_live(self) -> None:
        for key, value in self.payload()["baseline_subject_state"].items():
            with self.subTest(subject_key=key), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                payload = self.payload(root)
                payload["baseline_subject_state"][key] = str(value) + "-mutated"
                self.write_yaml(root, self.map_path, payload)
                self.assertIn(
                    EVENT_PROMOTION_SELECTION_SUBJECT_DRIFT,
                    validate_event_promotion_selection(root).errors,
                )
        for item_index, item in enumerate(self.payload()["baseline_evidence_objects"]):
            for key in ("path", "blob", "sha256"):
                with self.subTest(item=item_index, key=key), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    payload = self.payload(root)
                    payload["baseline_evidence_objects"][item_index][key] = item[key] + "-mutated"
                    self.write_yaml(root, self.map_path, payload)
                    self.assertIn(
                        EVENT_PROMOTION_SELECTION_EVIDENCE_DRIFT,
                        validate_event_promotion_selection(root).errors,
                    )

    def test_historical_selection_gate_and_subject_are_not_live(self) -> None:
        for mutation, expected_error in (
            ("remove_selection", EVENT_PROMOTION_SELECTION_GATE_DRIFT),
            ("remove_promotion_gate", EVENT_PROMOTION_SELECTION_GATE_DRIFT),
            ("promote_subject", EVENT_PROMOTION_SELECTION_SUBJECT_DRIFT),
        ):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                if mutation == "promote_subject":
                    path = root / "docs/010-event-concept/README.md"
                    path.write_text(path.read_text(encoding="utf-8").replace("Status: Draft", "Status: Canonical", 1), encoding="utf-8")
                else:
                    gate = yaml.safe_load((root / self.gate_path).read_text(encoding="utf-8"))
                    if mutation == "remove_selection":
                        event_cycle = next(
                            item for item in gate["cycles"] if item["candidate_id"] == "OCP-010"
                        )
                        event_cycle["steps"]["CANDIDATE_BOARD_SELECTION"] = "pending"
                        event_cycle["evidence"].pop("CANDIDATE_BOARD_SELECTION")
                    else:
                        event_cycle = next(
                            item for item in gate["cycles"] if item["candidate_id"] == "OCP-010"
                        )
                        event_cycle["steps"]["DOCUMENT_PROMOTION"] = "pending"
                        event_cycle["evidence"].pop("DOCUMENT_PROMOTION")
                    self.write_yaml(root, self.gate_path, gate)
                self.assertNotIn(expected_error, validate_event_promotion_selection(root).errors)

    def test_consumers_remain_live_and_blocker_evidence_is_historical(self) -> None:
        payload = self.payload()
        for consumer in payload["compatibility"]["consumers"]:
            for token in ["OCP-010", *consumer["preserved_refs"]]:
                with self.subTest(consumer=consumer["document_id"], token=token), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    path = root / consumer["primary"]
                    text = path.read_text(encoding="utf-8")
                    if token == "OCP-010":
                        line = next(value for value in text.splitlines() if value.startswith("Depends-On:"))
                        path.write_text(text.replace(line, line.replace("OCP-010", "OCP-099"), 1), encoding="utf-8")
                    else:
                        path.write_text(text.replace(token, token.replace("@", "-mutated@")), encoding="utf-8")
                        self.assertNotIn(token, path.read_text(encoding="utf-8"))
                    self.assertIn(EVENT_PROMOTION_SELECTION_CONSUMER_DRIFT, validate_event_promotion_selection(root).errors)
        for blocker_id, evidence in payload["evidence"].items():
            for item in evidence:
                for token in item["tokens"]:
                    with self.subTest(blocker_id=blocker_id, token=token), tempfile.TemporaryDirectory() as tmp:
                        root = Path(tmp)
                        self.copy_inputs(root)
                        path = root / item["path"]
                        path.write_text(path.read_text(encoding="utf-8").replace(token, "MUTATED_EVIDENCE"), encoding="utf-8")
                        self.assertNotIn(EVENT_PROMOTION_SELECTION_EVIDENCE_DRIFT, validate_event_promotion_selection(root).errors)

    def test_baseline_bound_history_survives_live_selection_and_rejected_live_model_breaks(self) -> None:
        self.assertTrue(validate_foundation_promotion_reassessment(ROOT).valid)
        self.assertTrue(validate_event_stable_surface(ROOT).valid)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            reassessment = yaml.safe_load((root / "architecture/foundation-promotion-reassessment.yaml").read_text(encoding="utf-8"))
            reassessment["evidence"]["BOARD_SELECTION_ABSENT"] = [{
                "path": "architecture/foundation-promotion-gate.yaml",
                "tokens": ["CANDIDATE_BOARD_SELECTION", "promotion_selections: []"],
            }]
            self.write_yaml(root, Path("architecture/foundation-promotion-reassessment.yaml"), reassessment)
            self.assertIn(
                "FOUNDATION_REASSESSMENT_MAP_INVALID",
                validate_foundation_promotion_reassessment(root).errors,
            )


if __name__ == "__main__":
    unittest.main()
