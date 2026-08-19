from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools/ontology_checker"))

from ocp_checker import constraint_document_status_readiness as readiness  # noqa: E402
from ocp_checker.constraint_document_status_readiness import (  # noqa: E402
    CONSTRAINT_STATUS_READINESS_ASSESSMENT_DRIFT,
    CONSTRAINT_STATUS_READINESS_GATE_DRIFT,
    CONSTRAINT_STATUS_READINESS_NORM_DRIFT,
    CONSTRAINT_STATUS_READINESS_PRECEDENT_DRIFT,
    CONSTRAINT_STATUS_READINESS_SUBJECT_DRIFT,
    validate_constraint_document_status_readiness,
)


class ConstraintDocumentStatusReadinessTests(unittest.TestCase):
    map_path = Path("architecture/constraint-document-status-readiness.yaml")

    def payload(self, root: Path = ROOT) -> dict:
        return yaml.safe_load((root / self.map_path).read_text(encoding="utf-8"))

    def copy_inputs(self, destination: Path) -> None:
        paths = {
            self.map_path,
            Path("architecture/constraint-stable-surface.yaml"),
            Path("architecture/artifact-taxonomy.yaml"),
            readiness.GATE_PATH,
            Path("docs/016-core-boundary/reviewed-contract-v0.1.0.md"),
            Path("docs/006-constraint-concept/reviewed-contract-v0.3.2.md"),
            Path("architecture/constraint-document-acceptance.yaml"),
            Path("architecture/baselines/foundation-promotion-gate-pre-ocp006-acceptance.yaml"),
        }
        for source in sorted((ROOT / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
            paths.add(source.relative_to(ROOT))
        for relative in paths:
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)

    def write_payload(self, root: Path, payload: dict) -> None:
        (root / self.map_path).write_text(
            yaml.safe_dump(payload, sort_keys=False, allow_unicode=True), encoding="utf-8"
        )

    def test_repository_constraint_document_status_readiness_is_valid(self) -> None:
        self.assertTrue(validate_constraint_document_status_readiness(ROOT).valid)

    def test_derived_criterion_list_cannot_diverge_from_current_norm_text(self) -> None:
        payload = self.payload()
        evidence_rows = payload["governance_sweep"]["sources"] + payload["promotion_criteria"]
        for row in evidence_rows:
            for token in row["tokens"]:
                with self.subTest(source=row["source"], token=token), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    path = root / row["source"]
                    text = path.read_text(encoding="utf-8")
                    path.write_text(text.replace(token, "MUTATED-NORM", 1), encoding="utf-8")
                    self.assertIn(
                        CONSTRAINT_STATUS_READINESS_NORM_DRIFT,
                        validate_constraint_document_status_readiness(root).errors,
                    )

    def test_each_ocp006_criterion_assessment_cannot_change_without_basis(self) -> None:
        payload = self.payload()
        for index, row in enumerate(payload["promotion_criteria"]):
            with self.subTest(criterion=row["criterion_id"]), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                changed = self.payload(root)
                changed["promotion_criteria"][index]["ocp006_assessment"] = "satisfied"
                self.write_payload(root, changed)
                self.assertIn(
                    CONSTRAINT_STATUS_READINESS_ASSESSMENT_DRIFT,
                    validate_constraint_document_status_readiness(root).errors,
                )

    def test_normative_status_criteria_are_separate_from_discovery_practice(self) -> None:
        payload = self.payload()
        self.assertEqual(
            {row["axis"] for row in payload["norm_vs_practice"]["axes"]},
            readiness.PRACTICE_AXES,
        )
        self.assertTrue(all(
            row["kind"] == "discovery-practice-not-promotion-criterion"
            for row in payload["norm_vs_practice"]["axes"]
        ))
        self.assertNotIn(
            "open-question-count",
            {row["criterion_id"] for row in payload["promotion_criteria"]},
        )
        for row in payload["norm_vs_practice"]["axes"]:
            self.assertEqual(
                frozenset(row["norm_guard_terms"]),
                readiness.PRACTICE_NORM_GUARDS[row["axis"]],
            )
            for term in row["norm_guard_terms"]:
                with self.subTest(negative_norm_axis=row["axis"], term=term), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    path = root / "docs/001-ontology-governance/README.md"
                    path.write_text(
                        path.read_text(encoding="utf-8") + f"\n{term}\n",
                        encoding="utf-8",
                    )
                    self.assertIn(
                        CONSTRAINT_STATUS_READINESS_NORM_DRIFT,
                        validate_constraint_document_status_readiness(root).errors,
                    )

    def test_all_promoted_documents_are_swept_and_open_question_precedent_is_live(self) -> None:
        payload = self.payload()
        self.assertEqual(payload["precedent_sweep"]["promoted_document_count"], 23)
        self.assertEqual(
            {row["document_id"] for row in payload["precedent_sweep"]["carriers"]},
            set(readiness.PROMOTED_OPEN_CARRIERS),
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            path = root / "docs/011-outcome-assessment-record/README.md"
            path.write_text(path.read_text(encoding="utf-8") + "\n## 99. Open Questions\n\n1. Synthetic open question?\n", encoding="utf-8")
            self.assertIn(
                CONSTRAINT_STATUS_READINESS_PRECEDENT_DRIFT,
                validate_constraint_document_status_readiness(root).errors,
            )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            path = root / "docs/011-outcome-assessment-record/README.md"
            path.write_text(
                path.read_text(encoding="utf-8") + "\nA new semantic choice remains open.\n",
                encoding="utf-8",
            )
            self.assertIn(
                CONSTRAINT_STATUS_READINESS_PRECEDENT_DRIFT,
                validate_constraint_document_status_readiness(root).errors,
            )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            changed = self.payload(root)
            changed["precedent_sweep"]["interpretation"] = "open-question-closure-is-required"
            self.write_payload(root, changed)
            self.assertIn(
                CONSTRAINT_STATUS_READINESS_PRECEDENT_DRIFT,
                validate_constraint_document_status_readiness(root).errors,
            )

    def test_accepted_and_canonical_assessments_remain_distinct_and_l2_is_live(self) -> None:
        payload = self.payload()
        self.assertEqual(
            payload["result"]["accepted"],
            "normatively-possible-only-through-a-separate-complete-status-act",
        )
        self.assertEqual(
            payload["result"]["canonical"],
            "not-admissible-now-because-l2-fails-on-ocp005-draft",
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            path = root / readiness.ASSIGNMENT_PATH
            text = path.read_text(encoding="utf-8")
            path.write_text(text.replace("Status: Draft", "Status: Canonical", 1), encoding="utf-8")
            self.assertIn(
                CONSTRAINT_STATUS_READINESS_SUBJECT_DRIFT,
                validate_constraint_document_status_readiness(root).errors,
            )

    def test_discovery_preserves_subject_and_promotion_gate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            subject = root / "docs/006-constraint-concept/reviewed-contract-v0.3.2.md"
            subject.write_text(
                subject.read_text(encoding="utf-8").replace("Status: Draft", "Status: Canonical", 1),
                encoding="utf-8",
            )
            self.assertIn(
                CONSTRAINT_STATUS_READINESS_SUBJECT_DRIFT,
                validate_constraint_document_status_readiness(root).errors,
            )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            gate = root / readiness.GATE_PATH
            data = yaml.safe_load(gate.read_text(encoding="utf-8"))
            data["cycle_protocol"]["active_cycle_id"] = "CONSTRAINT_T7"
            gate.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
            self.assertIn(
                CONSTRAINT_STATUS_READINESS_GATE_DRIFT,
                validate_constraint_document_status_readiness(root).errors,
            )

    def test_baseline_anchors_are_full_chain(self) -> None:
        payload = self.payload()
        tree = subprocess.check_output(
            ["git", "ls-tree", "-r", payload["baseline"]], cwd=ROOT, text=True
        ).splitlines()
        reverse: dict[str, list[str]] = {}
        for line in tree:
            metadata, path = line.split("\t", 1)
            reverse.setdefault(metadata.split()[2], []).append(path)
        for item in payload["baseline_evidence_objects"]:
            with self.subTest(path=item["path"]):
                self.assertIn(item["path"], reverse.get(item["blob"], []))
                raw = subprocess.check_output(
                    ["git", "cat-file", "blob", item["blob"]], cwd=ROOT
                )
                self.assertEqual(hashlib.sha256(raw).hexdigest(), item["sha256"])
                self.assertTrue(all(token in raw.decode("utf-8") for token in item["state_tokens"]))

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        def scalar_paths(value, prefix=()):
            if isinstance(value, dict):
                for key, child in value.items():
                    yield from scalar_paths(child, prefix + (key,))
            elif isinstance(value, (list, tuple)):
                for index, child in enumerate(value):
                    yield from scalar_paths(child, prefix + (index,))
            else:
                yield prefix

        def mutate(value, path):
            if not path:
                if isinstance(value, bool):
                    return not value
                if isinstance(value, int):
                    return value + 1
                return f"MUTATED-{value}"
            part = path[0]
            rebuilt = copy.deepcopy(value)
            rebuilt[part] = mutate(value[part], path[1:])
            return rebuilt

        payload = self.payload()
        original_load = readiness._load
        for value_path in scalar_paths(payload):
            changed = mutate(payload, value_path)

            def changed_load(path: Path):
                return changed if path == ROOT / self.map_path else original_load(path)

            with self.subTest(value_path=value_path), patch.object(
                readiness, "_load", side_effect=changed_load
            ):
                self.assertFalse(validate_constraint_document_status_readiness(ROOT).valid)

        for name in (
            "EXPECTED_MAP_KEYS", "CRITERION_IDS", "PRACTICE_AXES", "GOVERNANCE_SOURCES", "FORBIDDEN_OUTCOMES",
        ):
            original = getattr(readiness, name)
            for value in sorted(original):
                with self.subTest(attribute=name, value=value), patch.object(
                    readiness, name, original - {value}
                ):
                    self.assertFalse(validate_constraint_document_status_readiness(ROOT).valid)
        for name in ("PROMOTED_OPEN_CARRIERS", "EXPECTED_ASSESSMENTS"):
            original = getattr(readiness, name)
            for key in sorted(original):
                changed = dict(original)
                del changed[key]
                with self.subTest(attribute=name, key=key), patch.object(readiness, name, changed):
                    self.assertFalse(validate_constraint_document_status_readiness(ROOT).valid)
        for name, changed in {
            "BASELINE": "MUTATED", "MAP_SHA256": "MUTATED", "SUBJECT_SHA256": "MUTATED",
            "EXPECTED_INTERPRETATION": "MUTATED",
            "OPEN_LEXICAL_VOCABULARY": tuple(reversed(readiness.OPEN_LEXICAL_VOCABULARY)),
            "EXPECTED_DEPENDENCIES": tuple(reversed(readiness.EXPECTED_DEPENDENCIES)),
        }.items():
            with self.subTest(attribute=name), patch.object(readiness, name, changed):
                self.assertFalse(validate_constraint_document_status_readiness(ROOT).valid)


if __name__ == "__main__":
    unittest.main()
