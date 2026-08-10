from __future__ import annotations

from pathlib import Path
import shutil
import sys
import tempfile
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools/ontology_checker"))

from ocp_checker.accepted_snapshot import (  # noqa: E402
    ACCEPTED_SNAPSHOT_CONTENT_MISMATCH,
    ACCEPTED_SNAPSHOT_COVERAGE_MISMATCH,
    ACCEPTED_SNAPSHOT_DECLARATION_MISSING,
    ACCEPTED_SNAPSHOT_MISSING,
    ACCEPTED_SNAPSHOT_NAME_MISMATCH,
    ACCEPTED_SNAPSHOT_PRIMARY_INVALID,
    validate_accepted_snapshots,
)


EXPECTED = {
    "OCP-011": ("Accepted", "0.1.1", "1c293a9b58ddd3a14a73bc3e614e24fce9dfa0f458a968c44d2ac350d708ff3f", "current-accepted"),
    "OCP-012": ("Accepted", "0.1.0", "a397323ee69863790e55f1b548bce3946100797abe03b464d642e0261c76db55", "current-accepted"),
    "OCP-013": ("Accepted", "0.1.0", "64df2a408a70edbf40c27b1d9d294d04426e063506792f6dc1d95af658e6371b", "current-accepted"),
    "OCP-014": ("Accepted", "0.1.0", "022580c6731414a533736171c5cfc111ff311fd75adc0462cb7095697a7fd0ac", "current-accepted"),
    "OCP-015": ("Accepted", "0.1.0", "08f0d972c327a8572551821f66beb7675fad407cccda94f057eeb4780fc3826e", "current-accepted"),
    "OCP-016": ("Canonical", "0.1.0", "111e676ac750a2bfbe17d34fb1e8d2984af860fd38c856b824b4aff8c261c155", "retained-acceptance-evidence"),
    "OCP-017": ("Accepted", "0.1.0", "e3fc44295a8182eb97c3e39cd407daadc3434b49000b74fd4926cfa4e420cb28", "current-accepted"),
    "OCP-018": ("Accepted", "0.1.0", "7b60d478ac15ced656eaee2d6a7062ca1c0291e6dadc6dccae85787f700df077", "current-accepted"),
    "OCP-020": ("Accepted", "0.1.0", "05992f1006dee9c2dca137e6145f3c5c70ce57746bb0febb79a3ca9598146bb8", "current-accepted"),
}


class AcceptedSnapshotTests(unittest.TestCase):
    map_path = Path("architecture/accepted-document-snapshot-map.yaml")

    def payload(self) -> dict:
        return yaml.safe_load((ROOT / self.map_path).read_text(encoding="utf-8"))

    def entries(self) -> list[dict]:
        return self.payload()["entries"]

    def copy_inputs(self, destination: Path) -> None:
        paths = {self.map_path}
        paths.update(path.relative_to(ROOT) for path in (ROOT / "docs").glob("*/README.md"))
        for entry in self.entries():
            paths.add(Path(entry["snapshot"]))
        for relative_path in paths:
            target = destination / relative_path
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative_path, target)

    @staticmethod
    def write_payload(root: Path, payload: dict) -> None:
        (root / AcceptedSnapshotTests.map_path).write_text(
            yaml.safe_dump(payload, sort_keys=False), encoding="utf-8"
        )

    def test_repository_map_and_every_declared_element_are_exact(self) -> None:
        self.assertTrue(validate_accepted_snapshots(ROOT).valid)
        payload = self.payload()
        self.assertEqual(payload["required_retained_evidence"], ["OCP-016"])
        self.assertEqual(
            {
                entry["document_id"]: (
                    entry["current_status"],
                    entry["reviewed_version"],
                    entry["sha256"],
                    entry["basis"],
                )
                for entry in payload["entries"]
            },
            EXPECTED,
        )

    def test_acceptance_without_each_required_snapshot_is_rejected(self) -> None:
        for entry in self.entries():
            with self.subTest(document=entry["document_id"]), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                (root / entry["snapshot"]).unlink()
                self.assertIn(
                    ACCEPTED_SNAPSHOT_MISSING,
                    validate_accepted_snapshots(root).errors,
                )

    def test_each_mismatched_snapshot_name_is_rejected(self) -> None:
        for index, entry in enumerate(self.entries()):
            with self.subTest(document=entry["document_id"]), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                payload = self.payload()
                mutated = payload["entries"][index]
                original = root / mutated["snapshot"]
                wrong = original.with_name("reviewed-contract-v9.9.9.md")
                original.rename(wrong)
                mutated["snapshot"] = str(wrong.relative_to(root))
                self.write_payload(root, payload)
                self.assertIn(
                    ACCEPTED_SNAPSHOT_NAME_MISMATCH,
                    validate_accepted_snapshots(root).errors,
                )

    def test_each_mismatched_snapshot_content_is_rejected(self) -> None:
        for entry in self.entries():
            with self.subTest(document=entry["document_id"]), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                target = root / entry["snapshot"]
                target.write_bytes(target.read_bytes() + b"\nmutation-control\n")
                self.assertIn(
                    ACCEPTED_SNAPSHOT_CONTENT_MISMATCH,
                    validate_accepted_snapshots(root).errors,
                )

    def test_each_current_accepted_mapping_is_required(self) -> None:
        for index, entry in reversed(list(enumerate(self.entries()))):
            if entry["basis"] != "current-accepted":
                continue
            with self.subTest(document=entry["document_id"]), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                payload = self.payload()
                del payload["entries"][index]
                self.write_payload(root, payload)
                self.assertIn(
                    ACCEPTED_SNAPSHOT_COVERAGE_MISMATCH,
                    validate_accepted_snapshots(root).errors,
                )

    def test_each_primary_declaration_and_status_binding_is_required(self) -> None:
        for entry in self.entries():
            with self.subTest(document=entry["document_id"], field="declaration"), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                primary = root / entry["primary"]
                text = primary.read_text(encoding="utf-8")
                marker = f"]({Path(entry['snapshot']).name})"
                self.assertIn(marker, text)
                primary.write_text(text.replace(marker, "](removed-snapshot.md)"), encoding="utf-8")
                self.assertIn(
                    ACCEPTED_SNAPSHOT_DECLARATION_MISSING,
                    validate_accepted_snapshots(root).errors,
                )

            with self.subTest(document=entry["document_id"], field="status"), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                primary = root / entry["primary"]
                text = primary.read_text(encoding="utf-8")
                old = f"Status: {entry['current_status']}"
                primary.write_text(text.replace(old, "Status: Draft", 1), encoding="utf-8")
                self.assertIn(
                    ACCEPTED_SNAPSHOT_PRIMARY_INVALID,
                    validate_accepted_snapshots(root).errors,
                )


if __name__ == "__main__":
    unittest.main()
