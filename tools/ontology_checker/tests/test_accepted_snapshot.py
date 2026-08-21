from __future__ import annotations

from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools/ontology_checker"))

from ocp_checker import accepted_snapshot  # noqa: E402
from ocp_checker.accepted_snapshot import (  # noqa: E402
    ACCEPTED_SNAPSHOT_CONTENT_MISMATCH,
    ACCEPTED_SNAPSHOT_COVERAGE_MISMATCH,
    ACCEPTED_SNAPSHOT_DECLARATION_MISSING,
    ACCEPTED_SNAPSHOT_MAP_INVALID,
    ACCEPTED_SNAPSHOT_MISSING,
    ACCEPTED_SNAPSHOT_NAME_MISMATCH,
    ACCEPTED_SNAPSHOT_PRIMARY_INVALID,
    validate_accepted_snapshots,
)


EXPECTED = {
    "OCP-005": (
        "docs/005-assignment-concept/README.md",
        "Canonical",
        "0.3.0",
        "docs/005-assignment-concept/reviewed-contract-v0.3.0.md",
        "de84c9dafdb6126ff68a3a33218a344ddc250cf1a28e63c91407fd416e7e161b",
        "retained-acceptance-evidence",
    ),
    "OCP-006": (
        "docs/006-constraint-concept/README.md",
        "Accepted",
        "0.3.2",
        "docs/006-constraint-concept/reviewed-contract-v0.3.2.md",
        "0472d8ce4b15a8c64d58151ee7f706b450b930f708f6f0a7a40bdd87914b3b10",
        "current-accepted",
    ),
    "OCP-011": (
        "docs/011-outcome-assessment-record/README.md",
        "Accepted",
        "0.1.1",
        "docs/011-outcome-assessment-record/reviewed-contract-v0.1.1.md",
        "1c293a9b58ddd3a14a73bc3e614e24fce9dfa0f458a968c44d2ac350d708ff3f",
        "current-accepted",
    ),
    "OCP-012": (
        "docs/012-capability-claim-record/README.md",
        "Accepted",
        "0.1.0",
        "docs/012-capability-claim-record/reviewed-contract-v0.1.0.md",
        "a397323ee69863790e55f1b548bce3946100797abe03b464d642e0261c76db55",
        "current-accepted",
    ),
    "OCP-013": (
        "docs/013-resource-interchangeability/README.md",
        "Accepted",
        "0.1.0",
        "docs/013-resource-interchangeability/reviewed-contract-v0.1.0.md",
        "64df2a408a70edbf40c27b1d9d294d04426e063506792f6dc1d95af658e6371b",
        "current-accepted",
    ),
    "OCP-014": (
        "docs/014-coordination-profile/README.md",
        "Accepted",
        "0.1.0",
        "docs/014-coordination-profile/reviewed-contract-v0.1.0.md",
        "022580c6731414a533736171c5cfc111ff311fd75adc0462cb7095697a7fd0ac",
        "current-accepted",
    ),
    "OCP-015": (
        "docs/015-coordination-workflow/README.md",
        "Accepted",
        "0.1.0",
        "docs/015-coordination-workflow/reviewed-contract-v0.1.0.md",
        "08f0d972c327a8572551821f66beb7675fad407cccda94f057eeb4780fc3826e",
        "current-accepted",
    ),
    "OCP-016": (
        "docs/016-core-boundary/README.md",
        "Canonical",
        "0.1.0",
        "docs/016-core-boundary/reviewed-contract-v0.1.0.md",
        "111e676ac750a2bfbe17d34fb1e8d2984af860fd38c856b824b4aff8c261c155",
        "retained-acceptance-evidence",
    ),
    "OCP-017": (
        "docs/017-operation-lifecycle/README.md",
        "Accepted",
        "0.1.0",
        "docs/017-operation-lifecycle/reviewed-contract-v0.1.0.md",
        "e3fc44295a8182eb97c3e39cd407daadc3434b49000b74fd4926cfa4e420cb28",
        "current-accepted",
    ),
    "OCP-018": (
        "docs/018-operation-authorization-source/README.md",
        "Accepted",
        "0.1.0",
        "docs/018-operation-authorization-source/reviewed-contract-v0.1.0.md",
        "7b60d478ac15ced656eaee2d6a7062ca1c0291e6dadc6dccae85787f700df077",
        "current-accepted",
    ),
    "OCP-019": (
        "docs/019-conflict-derivation-boundary/README.md",
        "Accepted",
        "0.1.0",
        "docs/019-conflict-derivation-boundary/reviewed-contract-v0.1.0.md",
        "8689327a770eecccd40a7d43dd147659c24eb2e1dc0cd117dfe3e75114676bec",
        "current-accepted",
    ),
    "OCP-020": (
        "docs/020-quantitative-constraint-input/README.md",
        "Accepted",
        "0.1.0",
        "docs/020-quantitative-constraint-input/reviewed-contract-v0.1.0.md",
        "05992f1006dee9c2dca137e6145f3c5c70ce57746bb0febb79a3ca9598146bb8",
        "current-accepted",
    ),
    "OCP-021": (
        "docs/021-reservation-allocation-boundary/README.md",
        "Accepted",
        "0.1.0",
        "docs/021-reservation-allocation-boundary/reviewed-contract-v0.1.0.md",
        "85cdc7e3bb5281a6b2fe0af4d11b31bc47040b762de5786a0a8a10c2e000f683",
        "current-accepted",
    ),
    "OCP-022": (
        "docs/022-order-authorization-boundary/README.md",
        "Accepted",
        "0.1.0",
        "docs/022-order-authorization-boundary/reviewed-contract-v0.1.0.md",
        "8e2562153738d140510d21742b9c50ee8d37588ecbfe2a3221ae79f04268a60a",
        "current-accepted",
    ),
    "OCP-023": (
        "docs/023-resource-occupancy/README.md",
        "Accepted",
        "0.1.0",
        "docs/023-resource-occupancy/reviewed-contract-v0.1.0.md",
        "c8a765053c3bd398eba18508c080f15dbe49a784565faa59bb8a88d266d872d4",
        "current-accepted",
    ),
    "OCP-024": (
        "docs/024-completeness-evaluator/README.md",
        "Accepted",
        "0.1.0",
        "docs/024-completeness-evaluator/reviewed-contract-v0.1.0.md",
        "0c77e0527ec3adf9ed7cf5bbd32e0a63e55a1c3780f007d35a0ef2630cc18753",
        "current-accepted",
    ),
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
        self.assertEqual(payload["required_retained_evidence"], ["OCP-005", "OCP-016"])
        self.assertEqual(
            {
                entry["document_id"]: (
                    entry["primary"],
                    entry["current_status"],
                    entry["reviewed_version"],
                    entry["snapshot"],
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

    def test_each_mapping_and_new_acceptance_are_required(self) -> None:
        for index, entry in reversed(list(enumerate(self.entries()))):
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

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            new_acceptance = root / "docs/010-event-concept/README.md"
            text = new_acceptance.read_text(encoding="utf-8")
            new_acceptance.write_text(
                text.replace("Status: Canonical", "Status: Accepted", 1), encoding="utf-8"
            )
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

    def test_new_accepted_boundaries_preserve_exact_reviewed_bodies(self) -> None:
        markers = {
            "OCP-005": 27,
            "OCP-006": 30,
            "OCP-019": 15,
            "OCP-021": 15,
            "OCP-022": 15,
            "OCP-023": 11,
        }
        for document_id, section in markers.items():
            with self.subTest(document=document_id):
                entry = next(
                    item for item in self.entries() if item["document_id"] == document_id
                )
                primary = (ROOT / entry["primary"]).read_bytes().split(b"\n---\n", 1)[1]
                snapshot = (ROOT / entry["snapshot"]).read_bytes().split(b"\n---\n", 1)[1]
                marker = (
                    f"\n## {section}. Accepted authority and incorporated reviewed body\n"
                    .encode("utf-8")
                )
                self.assertTrue(primary.startswith(snapshot + marker))

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        for attribute in ("ENTRY_KEYS", "BASES"):
            values = getattr(accepted_snapshot, attribute)
            for value in sorted(values):
                with self.subTest(attribute=attribute, value=value), patch.object(
                    accepted_snapshot, attribute, values - {value}
                ):
                    self.assertIn(
                        ACCEPTED_SNAPSHOT_MAP_INVALID,
                        validate_accepted_snapshots(ROOT).errors,
                    )


if __name__ == "__main__":
    unittest.main()
