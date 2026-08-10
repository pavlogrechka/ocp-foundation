from __future__ import annotations

from pathlib import Path
import shutil
import sys
import tempfile
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools/ontology_checker"))

from ocp_checker.open_question_sync import (  # noqa: E402
    OPEN_QUESTION_RESOLUTION_MISSING,
    OPEN_QUESTION_RESOLUTION_REFERENCE_MISSING,
    OPEN_QUESTION_SYNC_BACKLOG_INVALID,
    validate_open_question_sync,
)


EXPECTED_AB_BINDINGS = {
    "QSYNC-001": ("AB-059",),
    "QSYNC-002": ("AB-059",),
    "QSYNC-003": ("AB-036",),
    "QSYNC-004": ("AB-037",),
    "QSYNC-005": ("AB-025",),
    "QSYNC-006": ("AB-025",),
    "QSYNC-007": ("AB-025", "AB-037"),
    "QSYNC-008": ("AB-036",),
    "QSYNC-009": ("AB-036",),
    "QSYNC-010": ("AB-037",),
    "QSYNC-011": ("AB-025",),
    "QSYNC-012": ("AB-056",),
}


class OpenQuestionSyncTests(unittest.TestCase):
    map_path = Path("architecture/open-question-resolution-map.yaml")
    backlog_path = Path("backlog/architecture-backlog.md")

    def entries(self) -> list[dict]:
        payload = yaml.safe_load((ROOT / self.map_path).read_text(encoding="utf-8"))
        return payload["entries"]

    def copy_inputs(self, destination: Path) -> None:
        paths = {self.map_path, self.backlog_path}
        paths.update(Path(entry["document"]) for entry in self.entries())
        for relative_path in paths:
            target = destination / relative_path
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative_path, target)

    def test_repository_resolution_map_is_valid(self) -> None:
        self.assertTrue(validate_open_question_sync(ROOT).valid)
        self.assertEqual(
            {entry["id"]: tuple(entry["ab_ids"]) for entry in self.entries()},
            EXPECTED_AB_BINDINGS,
        )

    def test_every_declared_question_is_individually_enforced(self) -> None:
        for entry in self.entries():
            with self.subTest(entry=entry["id"]), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                target = root / entry["document"]
                marker = f"~~{entry['question']}~~"
                text = target.read_text(encoding="utf-8")
                self.assertEqual(text.count(marker), 1)
                target.write_text(text.replace(marker, entry["question"], 1), encoding="utf-8")
                result = validate_open_question_sync(root)
                self.assertIn(OPEN_QUESTION_RESOLUTION_MISSING, result.errors)

            with self.subTest(entry=entry["id"], field="resolution_ref"), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                target = root / entry["document"]
                text = target.read_text(encoding="utf-8")
                marker = f"~~{entry['question']}~~"
                lines = text.splitlines(keepends=True)
                matching_indexes = [index for index, line in enumerate(lines) if marker in line]
                self.assertEqual(len(matching_indexes), 1)
                index = matching_indexes[0]
                self.assertIn(entry["resolution_ref"], lines[index])
                lines[index] = lines[index].replace(
                    entry["resolution_ref"], "REMOVED-RESOLUTION-REF", 1
                )
                target.write_text("".join(lines), encoding="utf-8")
                result = validate_open_question_sync(root)
                self.assertIn(OPEN_QUESTION_RESOLUTION_REFERENCE_MISSING, result.errors)

    def test_resolved_backlog_status_is_required(self) -> None:
        for ab_id in sorted({ab_id for values in EXPECTED_AB_BINDINGS.values() for ab_id in values}):
            with self.subTest(ab_id=ab_id), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                target = root / self.backlog_path
                text = target.read_text(encoding="utf-8")
                old = next(line for line in text.splitlines() if line.startswith(f"| {ab_id} "))
                self.assertIn("| Resolved |", old)
                target.write_text(
                    text.replace(old, old.replace("| Resolved |", "| Open |"), 1),
                    encoding="utf-8",
                )
                result = validate_open_question_sync(root)
                self.assertIn(OPEN_QUESTION_SYNC_BACKLOG_INVALID, result.errors)


if __name__ == "__main__":
    unittest.main()
