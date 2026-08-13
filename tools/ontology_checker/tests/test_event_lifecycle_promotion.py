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

from ocp_checker import event_lifecycle_promotion  # noqa: E402
from ocp_checker.event_lifecycle_promotion import (  # noqa: E402
    EVENT_LIFECYCLE_PROMOTION_CONSUMER_DRIFT,
    EVENT_LIFECYCLE_PROMOTION_EVIDENCE_DRIFT,
    EVENT_LIFECYCLE_PROMOTION_GATE_DRIFT,
    EVENT_LIFECYCLE_PROMOTION_MAP_INVALID,
    EVENT_LIFECYCLE_PROMOTION_PRECONDITION_UNPROVED,
    EVENT_LIFECYCLE_PROMOTION_SUBJECT_DRIFT,
    validate_event_lifecycle_promotion,
)
from ocp_checker.event_promotion_selection import validate_event_promotion_selection  # noqa: E402
from ocp_checker.event_stable_surface import validate_event_stable_surface  # noqa: E402


class EventLifecyclePromotionTests(unittest.TestCase):
    map_path = Path("architecture/event-lifecycle-promotion.yaml")

    def copy_inputs(self, destination: Path) -> None:
        for relative in (
            self.map_path,
            Path("architecture/event-promotion-selection.yaml"),
            Path("architecture/event-stable-surface.yaml"),
            Path("architecture/foundation-promotion-gate.yaml"),
            Path("architecture/baselines/foundation-map.md"),
            Path("docs/010-event-concept/README.md"),
            Path("docs/011-outcome-assessment-record/README.md"),
            Path("docs/017-operation-lifecycle/README.md"),
            Path("tools/ontology_checker/rules.yaml"),
            Path("tools/ontology_checker/ocp_checker/event.py"),
            Path("tools/ontology_checker/fixtures/event/valid-integrated-scenario.yaml"),
            Path("tools/ontology_checker/fixtures/operation_lifecycle/valid-q3i-completed.yaml"),
        ):
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)
        for primary in (ROOT / "docs").glob("*/README.md"):
            target = destination / primary.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(primary, target)

    def payload(self, root: Path = ROOT) -> dict:
        return yaml.safe_load((root / self.map_path).read_text(encoding="utf-8"))

    def write_yaml(self, root: Path, relative: Path, payload: dict) -> None:
        (root / relative).write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")

    def test_repository_promotion_is_valid_and_all_preconditions_are_proved(self) -> None:
        result = validate_event_lifecycle_promotion(ROOT)
        self.assertTrue(result.valid, result.errors)
        payload = self.payload()
        self.assertEqual(
            {item["precondition_id"] for item in payload["promotion_preconditions"]},
            event_lifecycle_promotion.PRECONDITION_IDS,
        )

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        categories = (
            "MAP_KEYS", "GATE_KEYS", "SUBJECT_KEYS", "PRECONDITION_KEYS",
            "COMPATIBILITY_KEYS", "MIGRATION_KEYS", "ROLLBACK_KEYS", "EVIDENCE_KEYS",
            "PRECONDITION_IDS", "PROOF_IDS", "CONSUMER_IDS", "PRESERVED_REFS",
        )
        for attribute in categories:
            values = getattr(event_lifecycle_promotion, attribute)
            for value in sorted(values):
                with self.subTest(attribute=attribute, value=value), patch.object(
                    event_lifecycle_promotion, attribute, values - {value}
                ):
                    self.assertIn(
                        EVENT_LIFECYCLE_PROMOTION_MAP_INVALID,
                        validate_event_lifecycle_promotion(ROOT).errors,
                    )
        for precondition, proof in event_lifecycle_promotion.EXPECTED_PRECONDITIONS.items():
            mutated = dict(event_lifecycle_promotion.EXPECTED_PRECONDITIONS)
            mutated[precondition] = proof + "-mutated"
            with self.subTest(precondition=precondition), patch.object(
                event_lifecycle_promotion, "EXPECTED_PRECONDITIONS", mutated
            ):
                self.assertIn(
                    EVENT_LIFECYCLE_PROMOTION_PRECONDITION_UNPROVED,
                    validate_event_lifecycle_promotion(ROOT).errors,
                )
        for consumer_id, expected in event_lifecycle_promotion.EXPECTED_CONSUMERS.items():
            for index, value in enumerate(expected[:3]):
                mutated = dict(event_lifecycle_promotion.EXPECTED_CONSUMERS)
                changed = list(expected)
                changed[index] = str(value) + "-mutated"
                mutated[consumer_id] = tuple(changed)
                with self.subTest(consumer=consumer_id, value=value), patch.object(
                    event_lifecycle_promotion, "EXPECTED_CONSUMERS", mutated
                ):
                    self.assertIn(
                        EVENT_LIFECYCLE_PROMOTION_MAP_INVALID,
                        validate_event_lifecycle_promotion(ROOT).errors,
                    )

    def test_each_precondition_requires_independent_repository_evidence(self) -> None:
        payload = self.payload()
        for precondition, items in payload["evidence"].items():
            for item in items:
                for field in ("tokens", "absent_tokens"):
                    for token in item.get(field, []):
                        with self.subTest(precondition=precondition, field=field, token=token), tempfile.TemporaryDirectory() as tmp:
                            root = Path(tmp)
                            self.copy_inputs(root)
                            source = root / item["path"]
                            text = source.read_text(encoding="utf-8")
                            if field == "tokens":
                                self.assertIn(token, text)
                                text = text.replace(token, "MUTATED_PROMOTION_EVIDENCE")
                            else:
                                self.assertNotIn(token, text)
                                text += "\n" + token + "\n"
                            source.write_text(text, encoding="utf-8")
                            self.assertIn(
                                EVENT_LIFECYCLE_PROMOTION_EVIDENCE_DRIFT,
                                validate_event_lifecycle_promotion(root).errors,
                            )
                for edge in item.get("absent_current_edges", []):
                    with self.subTest(precondition=precondition, edge=edge), tempfile.TemporaryDirectory() as tmp:
                        root = Path(tmp)
                        self.copy_inputs(root)
                        source = root / item["path"]
                        text = source.read_text(encoding="utf-8")
                        marker = "## Current isolated defined Concepts"
                        source.write_text(text.replace(marker, f"- {edge}\n\n{marker}", 1), encoding="utf-8")
                        self.assertIn(
                            EVENT_LIFECYCLE_PROMOTION_EVIDENCE_DRIFT,
                            validate_event_lifecycle_promotion(root).errors,
                        )

    def test_declared_completion_without_each_proof_fails(self) -> None:
        for precondition in event_lifecycle_promotion.PRECONDITION_IDS:
            with self.subTest(precondition=precondition), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                payload = self.payload(root)
                item = next(value for value in payload["promotion_preconditions"] if value["precondition_id"] == precondition)
                item["status"] = "declared"
                self.write_yaml(root, self.map_path, payload)
                self.assertIn(
                    EVENT_LIFECYCLE_PROMOTION_PRECONDITION_UNPROVED,
                    validate_event_lifecycle_promotion(root).errors,
                )

    def test_each_accepted_consumer_binding_and_fixture_is_live(self) -> None:
        payload = self.payload()
        for consumer in payload["compatibility"]:
            for token in ["OCP-010", *consumer["preserved_refs"]]:
                with self.subTest(consumer=consumer["document_id"], token=token), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    source = root / consumer["primary"]
                    text = source.read_text(encoding="utf-8")
                    source.write_text(text.replace(token, "MUTATED_CONSUMER_TOKEN"), encoding="utf-8")
                    self.assertIn(
                        EVENT_LIFECYCLE_PROMOTION_CONSUMER_DRIFT,
                        validate_event_lifecycle_promotion(root).errors,
                    )

    def test_each_accepted_consumer_fixture_is_individually_live(self) -> None:
        for consumer_id, mutation in (
            ("OCP-011", ("conclusion: indeterminate", "conclusion: achieved")),
            ("OCP-017", ("provenance_ref: ACT-Q3I-ALPHA-T4", "provenance_ref: ''")),
        ):
            with self.subTest(consumer=consumer_id), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                consumer = next(item for item in self.payload(root)["compatibility"] if item["document_id"] == consumer_id)
                fixture = root / consumer["executable_fixture"]
                text = fixture.read_text(encoding="utf-8")
                old, new = mutation
                self.assertIn(old, text)
                fixture.write_text(text.replace(old, new, 1), encoding="utf-8")
                self.assertIn(
                    EVENT_LIFECYCLE_PROMOTION_CONSUMER_DRIFT,
                    validate_event_lifecycle_promotion(root).errors,
                )

    def test_promotion_requires_atomic_gate_and_canonical_subject(self) -> None:
        for mutation, expected in (
            ("draft_subject", EVENT_LIFECYCLE_PROMOTION_SUBJECT_DRIFT),
            ("unfinished_gate", EVENT_LIFECYCLE_PROMOTION_GATE_DRIFT),
        ):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                if mutation == "draft_subject":
                    source = root / "docs/010-event-concept/README.md"
                    text = source.read_text(encoding="utf-8")
                    source.write_text(text.replace("Status: Canonical", "Status: Draft", 1), encoding="utf-8")
                else:
                    gate_path = Path("architecture/foundation-promotion-gate.yaml")
                    gate = yaml.safe_load((root / gate_path).read_text(encoding="utf-8"))
                    gate["sequence"]["completed_steps"].remove("EVENT_LIFECYCLE_PROMOTION_ACT")
                    gate["sequence"]["required_before_promotion"] = ["EVENT_LIFECYCLE_PROMOTION_ACT"]
                    gate["sequence"]["selected_next_scope_state"] = "selected"
                    self.write_yaml(root, gate_path, gate)
                self.assertIn(expected, validate_event_lifecycle_promotion(root).errors)

    def test_historical_subject_state_survives_promotion_and_snapshot_tampering_fails(self) -> None:
        self.assertTrue(validate_event_stable_surface(ROOT).valid)
        self.assertTrue(validate_event_promotion_selection(ROOT).valid)
        for field in ("expected_version", "expected_status", "baseline_blob", "baseline_sha256"):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                map_path = Path("architecture/event-stable-surface.yaml")
                payload = yaml.safe_load((root / map_path).read_text(encoding="utf-8"))
                payload["subject"][field] = str(payload["subject"][field]) + "-mutated"
                self.write_yaml(root, map_path, payload)
                self.assertFalse(validate_event_stable_surface(root).valid)


if __name__ == "__main__":
    unittest.main()
