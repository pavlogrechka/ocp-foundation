from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker.artifact_governance import (  # noqa: E402
    AD_BACKLOG_STATUS_UNRESOLVED,
    ARTIFACT_ID_MISMATCH,
    ARTIFACT_STATUS_INVALID,
    PATTERN_VERSION_MISMATCH,
    _parent_count,
    validate_artifact_governance,
)


TAXONOMY = """taxonomy_version: 0.3.0
artifact_classes:
  OCP:
    document_lifecycle: [Draft, Accepted]
    concept_lifecycle: [Proposed, Accepted]
  Pattern:
    lifecycle: [Draft, Accepted]
  AD:
    lifecycle: [Discovery, Under Review, Accepted]
  AB:
    lifecycle: [Open, Planned, Under Review, Resolved, Deferred, Rejected]
"""


class ArtifactGovernanceTests(unittest.TestCase):
    def make_repo(self) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "architecture/discovery").mkdir(parents=True)
        (root / "backlog").mkdir()
        (root / "patterns").mkdir()
        (root / "docs/001-sample").mkdir(parents=True)
        (root / "architecture/artifact-taxonomy.yaml").write_text(TAXONOMY, encoding="utf-8")
        (root / "backlog/architecture-backlog.md").write_text(
            "| ID | Тема | Статус | Наступна дія |\n"
            "|---|---|---|---|\n"
            "| AB-001 | Sample | Resolved | AD-001 |\n",
            encoding="utf-8",
        )
        (root / "patterns/P-001-sample.md").write_text(
            "---\nPattern-ID: P-001\nVersion: 0.1.0\nStatus: Accepted\n---\n",
            encoding="utf-8",
        )
        (root / "docs/001-sample/README.md").write_text(
            "---\nDocument-ID: OCP-001\nStatus: Draft\nDefines-Concepts: Sample\n"
            "Concept-Status: Accepted\nUses-Patterns: P-001@0.1.0\n---\n",
            encoding="utf-8",
        )
        (root / "architecture/discovery/AD-001-sample.md").write_text(
            "---\nDecision-ID: AD-001\nStatus: Accepted\nApplies-To: AB-001\n---\n",
            encoding="utf-8",
        )
        return root

    def test_valid_repository(self) -> None:
        self.assertTrue(validate_artifact_governance(self.make_repo()).valid)

    def test_invalid_class_status_is_rejected(self) -> None:
        root = self.make_repo()
        path = root / "backlog/architecture-backlog.md"
        path.write_text(path.read_text(encoding="utf-8").replace("Resolved", "Partially Implemented"), encoding="utf-8")
        self.assertIn(ARTIFACT_STATUS_INVALID, validate_artifact_governance(root).errors)

    def test_id_must_match_repository_path(self) -> None:
        root = self.make_repo()
        path = root / "docs/001-sample/README.md"
        path.write_text(path.read_text(encoding="utf-8").replace("OCP-001", "OCP-999"), encoding="utf-8")
        self.assertIn(ARTIFACT_ID_MISMATCH, validate_artifact_governance(root).errors)

    def test_accepted_ad_cannot_leave_referenced_backlog_active(self) -> None:
        root = self.make_repo()
        path = root / "backlog/architecture-backlog.md"
        path.write_text(path.read_text(encoding="utf-8").replace("Resolved", "Open"), encoding="utf-8")
        self.assertIn(AD_BACKLOG_STATUS_UNRESOLVED, validate_artifact_governance(root).errors)

    def test_pattern_version_must_resolve_exactly(self) -> None:
        root = self.make_repo()
        path = root / "docs/001-sample/README.md"
        path.write_text(path.read_text(encoding="utf-8").replace("P-001@0.1.0", "P-001@0.2.0"), encoding="utf-8")
        self.assertIn(PATTERN_VERSION_MISMATCH, validate_artifact_governance(root).errors)

    def test_process_parent_count(self) -> None:
        self.assertEqual(_parent_count("abc parent"), 1)
        self.assertEqual(_parent_count("abc parent1 parent2"), 2)


if __name__ == "__main__":
    unittest.main()
