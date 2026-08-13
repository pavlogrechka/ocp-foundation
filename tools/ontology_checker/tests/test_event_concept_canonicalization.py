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

from ocp_checker import event_concept_canonicalization  # noqa: E402
from ocp_checker.event_concept_canonicalization import (  # noqa: E402
    EVENT_CONCEPT_CANONICALIZATION_DEPENDENCY_UNSTABLE,
    EVENT_CONCEPT_CANONICALIZATION_EVIDENCE_INSUFFICIENT,
    EVENT_CONCEPT_CANONICALIZATION_HISTORY_REWRITTEN,
    EVENT_CONCEPT_CANONICALIZATION_MAP_INVALID,
    EVENT_CONCEPT_CANONICALIZATION_STATUS_DRIFT,
    validate_event_concept_canonicalization,
)


class EventConceptCanonicalizationTests(unittest.TestCase):
    map_path = Path("architecture/event-concept-canonicalization.yaml")

    def payload(self, root: Path = ROOT) -> dict:
        return yaml.safe_load((root / self.map_path).read_text(encoding="utf-8"))

    def copy_inputs(self, destination: Path) -> None:
        shutil.copytree(ROOT / "docs", destination / "docs")
        shutil.copytree(ROOT / "patterns", destination / "patterns")
        for relative in (
            self.map_path,
            Path("architecture/baselines/foundation-map.md"),
            Path("architecture/baselines/foundation-future-edges.yaml"),
            Path("architecture/event-lifecycle-promotion.yaml"),
            Path("architecture/foundation-promotion-gate.yaml"),
            Path("architecture/event-stable-surface.yaml"),
            Path("architecture/event-promotion-selection.yaml"),
            Path("architecture/foundation-promotion-reassessment.yaml"),
            Path("README.md"), Path("backlog/roadmap.md"), Path("backlog/architecture-backlog.md"),
            Path("tools/ontology_checker/rules.yaml"),
            Path("tools/ontology_checker/ocp_checker/event.py"),
            Path("tools/ontology_checker/fixtures/event/valid-integrated-scenario.yaml"),
            Path("tools/ontology_checker/fixtures/operation_lifecycle/valid-q3i-completed.yaml"),
        ):
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)

    def write_yaml(self, root: Path, relative: Path, payload: dict) -> None:
        (root / relative).write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")

    def test_repository_event_concept_canonicalization_is_valid(self) -> None:
        result = validate_event_concept_canonicalization(ROOT)
        self.assertTrue(result.valid, result.errors)

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        categories = (
            "MAP_KEYS", "GATE_KEYS", "BOARD_KEYS", "REQUIREMENT_KEYS", "DEPENDENCY_KEYS",
            "MACHINE_KEYS", "CARRIER_KEYS", "HISTORICAL_KEYS", "EVIDENCE_KEYS",
            "SEMANTIC_SURFACES", "FREEZE_BOUNDARY", "FORBIDDEN_IMPLICATIONS",
        )
        for attribute in categories:
            values = getattr(event_concept_canonicalization, attribute)
            for value in sorted(values):
                with self.subTest(attribute=attribute, value=value), patch.object(
                    event_concept_canonicalization, attribute, values - {value}
                ):
                    self.assertFalse(validate_event_concept_canonicalization(ROOT).valid)
        for attribute in (
            "DIRECT_OCP_DEPENDENCIES", "EXPECTED_CARRIERS", "CURRENT_TOKENS",
            "EXPECTED_HISTORICAL", "EXPECTED_EVIDENCE",
        ):
            value = getattr(event_concept_canonicalization, attribute)
            members = list(value)
            for member in members:
                mutated = copy.deepcopy(value)
                if isinstance(mutated, dict):
                    mutated.pop(member)
                else:
                    mutated = tuple(item for item in mutated if item != member)
                with self.subTest(attribute=attribute, member=member), patch.object(
                    event_concept_canonicalization, attribute, mutated
                ):
                    self.assertFalse(validate_event_concept_canonicalization(ROOT).valid)

    def test_each_current_status_carrier_is_live(self) -> None:
        for fpath, tokens in event_concept_canonicalization.CURRENT_TOKENS.items():
            for token in tokens:
                with self.subTest(fpath=fpath, token=token), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    source = root / fpath
                    text = source.read_text(encoding="utf-8")
                    self.assertIn(token, text)
                    source.write_text(text.replace(token, "MUTATED_CURRENT_STATUS"), encoding="utf-8")
                    self.assertIn(
                        EVENT_CONCEPT_CANONICALIZATION_STATUS_DRIFT,
                        validate_event_concept_canonicalization(root).errors,
                    )

    def test_each_stability_requirement_is_derived_from_live_metadata(self) -> None:
        for mutation in ("concept_dependency", "draft_ocp_dependency", "stale_pattern"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                if mutation == "concept_dependency":
                    source = root / "docs/010-event-concept/README.md"
                    source.write_text(source.read_text(encoding="utf-8").replace(
                        "Concept-Depends-On: []", "Concept-Depends-On: [Assignment]", 1
                    ), encoding="utf-8")
                elif mutation == "draft_ocp_dependency":
                    source = root / "docs/004-operation-concept/README.md"
                    source.write_text(source.read_text(encoding="utf-8").replace(
                        "Status: Canonical", "Status: Draft", 1
                    ), encoding="utf-8")
                else:
                    source = root / "patterns/P-001-identified-record-pattern.md"
                    source.write_text(source.read_text(encoding="utf-8").replace(
                        "Status: Accepted", "Status: Draft", 1
                    ), encoding="utf-8")
                self.assertIn(
                    EVENT_CONCEPT_CANONICALIZATION_DEPENDENCY_UNSTABLE,
                    validate_event_concept_canonicalization(root).errors,
                )

    def test_each_executable_evidence_token_and_fixture_is_live(self) -> None:
        for fpath, tokens in event_concept_canonicalization.EXPECTED_EVIDENCE.items():
            for token in tokens:
                with self.subTest(fpath=fpath, token=token), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    source = root / fpath
                    text = source.read_text(encoding="utf-8")
                    self.assertIn(token, text)
                    source.write_text(text.replace(token, "MUTATED_CANONICALIZATION_EVIDENCE"), encoding="utf-8")
                    self.assertIn(
                        EVENT_CONCEPT_CANONICALIZATION_EVIDENCE_INSUFFICIENT,
                        validate_event_concept_canonicalization(root).errors,
                    )

    def test_historical_baseline_witnesses_survive_and_rewrite_fails(self) -> None:
        for witness in self.payload()["historical_witnesses"]:
            with self.subTest(witness=witness["path"]), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                payload = self.payload(root)
                item = next(entry for entry in payload["historical_witnesses"] if entry["path"] == witness["path"])
                item["baseline"] = "0" * 40
                self.write_yaml(root, self.map_path, payload)
                self.assertIn(
                    EVENT_CONCEPT_CANONICALIZATION_HISTORY_REWRITTEN,
                    validate_event_concept_canonicalization(root).errors,
                )

    def test_unsynchronized_authoritative_representation_fails(self) -> None:
        for fpath, old in (
            ("docs/000-operational-ontology/README.md", "| Event | Canonical |"),
            ("docs/002-concept-taxonomy/README.md", "Event: Canonical"),
            ("docs/010-event-concept/README.md", "Concept-Status: Canonical"),
        ):
            with self.subTest(fpath=fpath), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                source = root / fpath
                source.write_text(source.read_text(encoding="utf-8").replace(old, old.replace("Canonical", "Accepted"), 1), encoding="utf-8")
                self.assertIn(
                    EVENT_CONCEPT_CANONICALIZATION_STATUS_DRIFT,
                    validate_event_concept_canonicalization(root).errors,
                )


if __name__ == "__main__":
    unittest.main()
