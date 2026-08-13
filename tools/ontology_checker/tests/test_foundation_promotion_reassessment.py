from __future__ import annotations

from pathlib import Path
from unittest.mock import patch
import copy
import shutil
import sys
import tempfile
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools/ontology_checker"))

from ocp_checker import foundation_promotion_reassessment  # noqa: E402
from ocp_checker.foundation_promotion_reassessment import (  # noqa: E402
    FOUNDATION_REASSESSMENT_EVIDENCE_DRIFT,
    FOUNDATION_REASSESSMENT_GATE_STATE_INVALID,
    FOUNDATION_REASSESSMENT_L2_MISMATCH,
    FOUNDATION_REASSESSMENT_MAP_INVALID,
    FOUNDATION_REASSESSMENT_SELECTION_FORBIDDEN,
    validate_foundation_promotion_reassessment,
)


class FoundationPromotionReassessmentTests(unittest.TestCase):
    map_path = Path("architecture/foundation-promotion-reassessment.yaml")
    gate_path = Path("architecture/foundation-promotion-gate.yaml")

    def copy_inputs(self, destination: Path) -> None:
        shutil.copytree(ROOT / "docs", destination / "docs")
        for relative in (self.map_path, self.gate_path):
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)

    def payload(self, root: Path = ROOT) -> dict:
        return yaml.safe_load((root / self.map_path).read_text(encoding="utf-8"))

    def write_yaml(self, root: Path, relative: Path, payload: dict) -> None:
        (root / relative).write_text(
            yaml.safe_dump(payload, sort_keys=False), encoding="utf-8"
        )

    def test_repository_reassessment_is_valid_and_machine_distinct(self) -> None:
        self.assertTrue(validate_foundation_promotion_reassessment(ROOT).valid)
        evidence = self.payload()["baseline_gate_state"]
        self.assertIn("POST_DISCOVERY_REASSESSMENT", evidence["completed_steps"])
        self.assertEqual(
            evidence["required_before_promotion"], ["CANDIDATE_BOARD_SELECTION"]
        )
        self.assertEqual(evidence["promotion_selections"], [])

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        categories = (
            "CRITERION_IDS", "CANDIDATE_IDS", "OPTION_IDS", "L2_RESULTS", "BLOCKER_IDS",
            "COST_IDS", "UNLOCK_IDS", "MISSING_IDS", "OPTION_RESULTS", "RECOMMENDATION_VALUES",
            "MAP_KEYS", "L2_KEYS", "OPTION_KEYS", "EVIDENCE_KEYS",
        )
        for attribute in categories:
            production_values = getattr(foundation_promotion_reassessment, attribute)
            for value in sorted(production_values):
                with self.subTest(attribute=attribute, value=value), patch.object(
                    foundation_promotion_reassessment,
                    attribute,
                    production_values - {value},
                ):
                    self.assertIn(
                        FOUNDATION_REASSESSMENT_MAP_INVALID,
                        validate_foundation_promotion_reassessment(ROOT).errors,
                    )

        for value in foundation_promotion_reassessment.CRITERION_ORDER:
            with self.subTest(attribute="CRITERION_ORDER", value=value), patch.object(
                foundation_promotion_reassessment,
                "CRITERION_ORDER",
                tuple(item for item in foundation_promotion_reassessment.CRITERION_ORDER if item != value),
            ):
                self.assertIn(
                    FOUNDATION_REASSESSMENT_MAP_INVALID,
                    validate_foundation_promotion_reassessment(ROOT).errors,
                )

        for document_id, expected in foundation_promotion_reassessment.EXPECTED_L2.items():
            dependencies, result, blockers = expected
            mutated = dict(foundation_promotion_reassessment.EXPECTED_L2)
            mutated[document_id] = (dependencies, result + "-mutated", blockers)
            with self.subTest(document_id=document_id, l2_result=result), patch.object(
                foundation_promotion_reassessment, "EXPECTED_L2", mutated
            ):
                self.assertIn(
                    FOUNDATION_REASSESSMENT_L2_MISMATCH,
                    validate_foundation_promotion_reassessment(ROOT).errors,
                )
            for dependency in dependencies:
                mutated = dict(foundation_promotion_reassessment.EXPECTED_L2)
                mutated[document_id] = (
                    tuple(item for item in dependencies if item != dependency), result, blockers
                )
                with self.subTest(document_id=document_id, dependency=dependency), patch.object(
                    foundation_promotion_reassessment, "EXPECTED_L2", mutated
                ):
                    self.assertIn(
                        FOUNDATION_REASSESSMENT_L2_MISMATCH,
                        validate_foundation_promotion_reassessment(ROOT).errors,
                    )
            for blocker in blockers:
                mutated = dict(foundation_promotion_reassessment.EXPECTED_L2)
                mutated[document_id] = (
                    dependencies, result, tuple(item for item in blockers if item != blocker)
                )
                with self.subTest(document_id=document_id, l2_blocker=blocker), patch.object(
                    foundation_promotion_reassessment, "EXPECTED_L2", mutated
                ):
                    self.assertIn(
                        FOUNDATION_REASSESSMENT_L2_MISMATCH,
                        validate_foundation_promotion_reassessment(ROOT).errors,
                    )

        for option_id, expected in foundation_promotion_reassessment.EXPECTED_OPTIONS.items():
            for index, value in enumerate(expected):
                values = value if isinstance(value, tuple) else (value,)
                for item in values:
                    mutated = copy.deepcopy(foundation_promotion_reassessment.EXPECTED_OPTIONS)
                    changed = list(expected)
                    if isinstance(value, tuple):
                        changed[index] = tuple(member for member in value if member != item)
                    else:
                        changed[index] = str(item) + "-mutated"
                    mutated[option_id] = tuple(changed)
                    with self.subTest(option_id=option_id, field=index, value=item), patch.object(
                        foundation_promotion_reassessment, "EXPECTED_OPTIONS", mutated
                    ):
                        self.assertIn(
                            FOUNDATION_REASSESSMENT_MAP_INVALID,
                            validate_foundation_promotion_reassessment(ROOT).errors,
                        )

        for blocker_id, evidence in foundation_promotion_reassessment.EXPECTED_EVIDENCE.items():
            for item_index, (source, tokens) in enumerate(evidence):
                mutated = copy.deepcopy(foundation_promotion_reassessment.EXPECTED_EVIDENCE)
                changed_items = list(evidence)
                changed_items[item_index] = (source + "-mutated", tokens)
                mutated[blocker_id] = tuple(changed_items)
                with self.subTest(blocker_id=blocker_id, source=source), patch.object(
                    foundation_promotion_reassessment, "EXPECTED_EVIDENCE", mutated
                ):
                    self.assertIn(
                        FOUNDATION_REASSESSMENT_MAP_INVALID,
                        validate_foundation_promotion_reassessment(ROOT).errors,
                    )
                for token in tokens:
                    mutated = copy.deepcopy(foundation_promotion_reassessment.EXPECTED_EVIDENCE)
                    changed_items = list(evidence)
                    changed_items[item_index] = (
                        source, tuple(value for value in tokens if value != token)
                    )
                    mutated[blocker_id] = tuple(changed_items)
                    with self.subTest(blocker_id=blocker_id, token=token), patch.object(
                        foundation_promotion_reassessment, "EXPECTED_EVIDENCE", mutated
                    ):
                        self.assertIn(
                            FOUNDATION_REASSESSMENT_MAP_INVALID,
                            validate_foundation_promotion_reassessment(ROOT).errors,
                        )

    def test_l2_is_derived_from_live_metadata_not_gate_claims(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            primary = root / "docs/004-operation-concept/README.md"
            text = primary.read_text(encoding="utf-8")
            primary.write_text(text.replace("Status: Canonical", "Status: Draft", 1), encoding="utf-8")
            self.assertIn(
                FOUNDATION_REASSESSMENT_L2_MISMATCH,
                validate_foundation_promotion_reassessment(root).errors,
            )

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            reassessment = self.payload(root)
            entry = next(item for item in reassessment["live_l2"] if item["document_id"] == "OCP-010")
            entry["result"] = "fail"
            entry["blockers"] = ["OCP-008"]
            self.write_yaml(root, self.map_path, reassessment)
            self.assertIn(
                FOUNDATION_REASSESSMENT_L2_MISMATCH,
                validate_foundation_promotion_reassessment(root).errors,
            )

    def test_each_historical_evidence_token_is_snapshot_live(self) -> None:
        payload = self.payload()
        for blocker_id, items in payload["evidence"].items():
            for evidence in items:
                for token in evidence["tokens"]:
                    with self.subTest(blocker_id=blocker_id, token=token), tempfile.TemporaryDirectory() as tmp:
                        root = Path(tmp)
                        self.copy_inputs(root)
                        snapshot = self.payload(root)
                        item = next(value for value in snapshot["evidence"][blocker_id] if value["path"] == evidence["path"])
                        item["tokens"].remove(token)
                        self.write_yaml(root, self.map_path, snapshot)
                        self.assertIn(FOUNDATION_REASSESSMENT_MAP_INVALID, validate_foundation_promotion_reassessment(root).errors)

    def test_reassessment_cannot_self_supply_selection(self) -> None:
        for mutation in ("name_selection", "claim_authority"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                payload = self.payload(root)
                if mutation == "name_selection":
                    payload["recommendation"]["selected_candidates"] = ["OCP-010"]
                else:
                    payload["recommendation"]["selection_authority"] = True
                self.write_yaml(root, self.map_path, payload)
                expected_error = FOUNDATION_REASSESSMENT_SELECTION_FORBIDDEN
                self.assertIn(
                    expected_error,
                    validate_foundation_promotion_reassessment(root).errors,
                )


if __name__ == "__main__":
    unittest.main()
