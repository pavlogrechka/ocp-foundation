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
    OPEN_QUESTION_SYNC_BACKLOG_INVALID,
    validate_open_question_sync,
)


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

    def test_resolved_backlog_status_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            target = root / self.backlog_path
            text = target.read_text(encoding="utf-8")
            text = text.replace(
                "| AB-025 | Reservation / Allocation як окремий Concept | Resolved |",
                "| AB-025 | Reservation / Allocation як окремий Concept | Open |",
                1,
            )
            target.write_text(text, encoding="utf-8")
            result = validate_open_question_sync(root)
            self.assertIn(OPEN_QUESTION_SYNC_BACKLOG_INVALID, result.errors)


if __name__ == "__main__":
    unittest.main()
