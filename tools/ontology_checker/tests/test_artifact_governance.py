from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker.artifact_governance import (  # noqa: E402
    AD_BACKLOG_STATUS_UNRESOLVED,
    ARTIFACT_ID_MISMATCH,
    ARTIFACT_STATUS_INVALID,
    BACKLOG_ID_DUPLICATE,
    PATTERN_REFERENCE_INVALID,
    PATTERN_REFERENCE_MISSING,
    PATTERN_VERSION_INVALID,
    PATTERN_VERSION_MISMATCH,
    PROCESS_HISTORY_AUDIT_FAILED,
    PROCESS_HISTORY_NON_LINEAR,
    PROCESS_HISTORY_SHALLOW,
    validate_artifact_governance,
    validate_process_audit,
)


TAXONOMY = """taxonomy_version: 0.4.0
artifact_classes:
  OCP:
    document_lifecycle: [Draft, Accepted]
    concept_lifecycle: [Proposed, Accepted]
  Pattern:
    lifecycle: [Draft, Accepted]
    version_format: semver
    invocation_version_policy: track-current
    version_change_requires_atomic_invoker_update: true
  AD:
    lifecycle: [Discovery, Under Review, Accepted]
  AB:
    lifecycle: [Open, Proposed, Discovery, Planned, Under Review, Resolved, Deferred, Rejected]
    active_states: [Open, Proposed, Discovery, Under Review]
commit_convention:
  merge_method: squash
  linear_history_required: true
  history_audit_scope: all_reachable_commits
  history_audit_requires_complete_history: true
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

    def assert_errors(self, root: Path, expected: set[str]) -> None:
        self.assertEqual(set(validate_artifact_governance(root).errors), expected)

    def test_valid_repository(self) -> None:
        self.assertTrue(validate_artifact_governance(self.make_repo()).valid)

    def test_invalid_class_status_is_rejected(self) -> None:
        root = self.make_repo()
        path = root / "backlog/architecture-backlog.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace("Resolved", "Partially Implemented"),
            encoding="utf-8",
        )
        self.assert_errors(root, {ARTIFACT_STATUS_INVALID})

    def test_id_must_match_repository_path(self) -> None:
        root = self.make_repo()
        path = root / "docs/001-sample/README.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace("OCP-001", "OCP-999"),
            encoding="utf-8",
        )
        self.assert_errors(root, {ARTIFACT_ID_MISMATCH})

    def test_accepted_ad_cannot_leave_referenced_backlog_active(self) -> None:
        root = self.make_repo()
        path = root / "backlog/architecture-backlog.md"
        path.write_text(path.read_text(encoding="utf-8").replace("Resolved", "Open"), encoding="utf-8")
        self.assert_errors(root, {AD_BACKLOG_STATUS_UNRESOLVED})

    def test_active_backlog_states_are_read_from_taxonomy(self) -> None:
        root = self.make_repo()
        taxonomy_path = root / "architecture/artifact-taxonomy.yaml"
        taxonomy = yaml.safe_load(taxonomy_path.read_text(encoding="utf-8"))
        taxonomy["artifact_classes"]["AB"]["active_states"] = ["Under Review"]
        taxonomy_path.write_text(yaml.safe_dump(taxonomy, sort_keys=False), encoding="utf-8")
        backlog_path = root / "backlog/architecture-backlog.md"
        backlog_path.write_text(
            backlog_path.read_text(encoding="utf-8").replace("Resolved", "Open"),
            encoding="utf-8",
        )
        self.assertTrue(validate_artifact_governance(root).valid)

    def test_duplicate_backlog_identifier_is_rejected(self) -> None:
        root = self.make_repo()
        path = root / "backlog/architecture-backlog.md"
        path.write_text(
            path.read_text(encoding="utf-8") + "| AB-001 | Duplicate | Resolved | AD-001 |\n",
            encoding="utf-8",
        )
        self.assert_errors(root, {BACKLOG_ID_DUPLICATE})

    def test_pattern_reference_format_is_rejected(self) -> None:
        root = self.make_repo()
        path = root / "docs/001-sample/README.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace("P-001@0.1.0", "P-001"),
            encoding="utf-8",
        )
        self.assert_errors(root, {PATTERN_REFERENCE_INVALID})

    def test_missing_pattern_is_rejected(self) -> None:
        root = self.make_repo()
        path = root / "docs/001-sample/README.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace("P-001@0.1.0", "P-999@0.1.0"),
            encoding="utf-8",
        )
        self.assert_errors(root, {PATTERN_REFERENCE_MISSING})

    def test_pattern_version_must_track_current(self) -> None:
        root = self.make_repo()
        path = root / "docs/001-sample/README.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace("P-001@0.1.0", "P-001@0.2.0"),
            encoding="utf-8",
        )
        self.assert_errors(root, {PATTERN_VERSION_MISMATCH})

    def test_pattern_version_must_be_semver(self) -> None:
        root = self.make_repo()
        path = root / "patterns/P-001-sample.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace("Version: 0.1.0", "Version: current"),
            encoding="utf-8",
        )
        self.assert_errors(root, {PATTERN_VERSION_INVALID})

    def git(self, root: Path, *args: str) -> None:
        env = os.environ.copy()
        env.update(
            {
                "GIT_AUTHOR_NAME": "OCP Test",
                "GIT_AUTHOR_EMAIL": "ocp@example.invalid",
                "GIT_COMMITTER_NAME": "OCP Test",
                "GIT_COMMITTER_EMAIL": "ocp@example.invalid",
            }
        )
        subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True, env=env)

    def make_git_repo(self) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "architecture").mkdir()
        (root / "architecture/artifact-taxonomy.yaml").write_text(TAXONOMY, encoding="utf-8")
        self.git(root, "init", "-b", "main")
        self.git(root, "add", ".")
        self.git(root, "commit", "-m", "initial")
        return root

    def test_process_audit_accepts_linear_complete_history(self) -> None:
        root = self.make_git_repo()
        self.assertTrue(validate_process_audit(root, context="main").valid)

    def test_process_audit_finds_merge_below_head(self) -> None:
        root = self.make_git_repo()
        self.git(root, "checkout", "-b", "feature")
        (root / "feature.txt").write_text("feature\n", encoding="utf-8")
        self.git(root, "add", "feature.txt")
        self.git(root, "commit", "-m", "feature")
        self.git(root, "checkout", "main")
        (root / "main.txt").write_text("main\n", encoding="utf-8")
        self.git(root, "add", "main.txt")
        self.git(root, "commit", "-m", "main")
        self.git(root, "merge", "--no-ff", "feature", "-m", "merge")
        (root / "after.txt").write_text("after\n", encoding="utf-8")
        self.git(root, "add", "after.txt")
        self.git(root, "commit", "-m", "after merge")
        self.assertEqual(
            set(validate_process_audit(root, context="main").errors),
            {PROCESS_HISTORY_NON_LINEAR},
        )

    def test_process_audit_rejects_shallow_history(self) -> None:
        origin = self.make_git_repo()
        (origin / "second.txt").write_text("second\n", encoding="utf-8")
        self.git(origin, "add", "second.txt")
        self.git(origin, "commit", "-m", "second")

        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        clone = Path(temp.name) / "clone"
        subprocess.run(
            ["git", "clone", "--depth", "1", origin.as_uri(), str(clone)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            set(validate_process_audit(clone, context="main").errors),
            {PROCESS_HISTORY_SHALLOW},
        )

    def test_process_audit_reports_infrastructure_failure(self) -> None:
        root = self.make_repo()
        self.assertEqual(
            set(validate_process_audit(root, context="main").errors),
            {PROCESS_HISTORY_AUDIT_FAILED},
        )


if __name__ == "__main__":
    unittest.main()
