from __future__ import annotations

import os
import re
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
    ARTIFACT_ID_DUPLICATE,
    ARTIFACT_ID_MISMATCH,
    ARTIFACT_STATUS_INVALID,
    ARTIFACT_VERSION_INVALID,
    BACKLOG_ID_DUPLICATE,
    CANONICAL_OCP_DEPENDENCY_PRECANONICAL,
    DEPENDENCY_REFERENCE_DUPLICATE,
    DEPENDENCY_REFERENCE_INVALID,
    DEPENDENCY_REFERENCE_MISSING,
    DEPENDENCY_SELF_REFERENCE,
    NORMATIVE_RULE_ID_DUPLICATE,
    NORMATIVE_RULE_INVALID,
    NORMATIVE_RULE_SOURCE_INVALID,
    NORMATIVE_RULE_SOURCE_MISSING,
    OCP_VERSION_LIFECYCLE_MISMATCH,
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


TAXONOMY = """taxonomy_version: 0.5.0
artifact_classes:
  OCP:
    document_lifecycle: [Draft, Accepted, Canonical]
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
reference_integrity:
  artifact_id_uniqueness_scope: [OCP, Pattern, AD, ADR, AB]
  dependency_metadata: Depends-On
  dependency_exact_resolution_required: true
  dependency_duplicates_forbidden: true
  dependency_self_reference_forbidden: true
  dependency_target_classes: [OCP, Pattern, AD, ADR, AB]
  normative_rule_manifest_glob: tools/ontology_checker/*rules.yaml
  normative_rule_ids_global_unique: true
  normative_rule_source_class: OCP
  normative_rule_default_kind: validation
  semantic_duplicate_detection: external-review
commit_convention:
  merge_method: squash
  linear_history_required: true
  history_audit_scope: post_baseline_reachable_commits
  history_audit_requires_complete_history: true
  history_audit_baseline: "0000000000000000000000000000000000000000"
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
            "---\nDocument-ID: OCP-001\nVersion: 0.1.0\nStatus: Draft\nDefines-Concepts: Sample\n"
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

    def add_metadata(self, path: Path, line: str) -> None:
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace("\n---\n", f"\n{line}\n---\n", 1), encoding="utf-8")

    def write_rule_manifest(
        self, root: Path, name: str, rule_id: str, source: str, kind: str = "validation"
    ) -> None:
        path = root / f"tools/ontology_checker/{name}-rules.yaml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            yaml.safe_dump(
                {"rules": [{"id": rule_id, "kind": kind, "source": source}]},
                sort_keys=False,
            ),
            encoding="utf-8",
        )

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

    def test_artifact_identifier_must_be_globally_unique(self) -> None:
        root = self.make_repo()
        duplicate = root / "docs/001-duplicate/README.md"
        duplicate.parent.mkdir()
        duplicate.write_text(
            "---\nDocument-ID: OCP-001\nVersion: 0.1.0\nStatus: Draft\n---\n",
            encoding="utf-8",
        )
        self.assert_errors(root, {ARTIFACT_ID_DUPLICATE})

    def test_pattern_identifier_must_be_globally_unique(self) -> None:
        root = self.make_repo()
        (root / "patterns/P-001-duplicate.md").write_text(
            "---\nPattern-ID: P-001\nVersion: 0.1.0\nStatus: Accepted\n---\n",
            encoding="utf-8",
        )
        self.assert_errors(root, {ARTIFACT_ID_DUPLICATE})

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

    def test_ocp_version_must_be_semver(self) -> None:
        root = self.make_repo()
        path = root / "docs/001-sample/README.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace("Version: 0.1.0", "Version: current"),
            encoding="utf-8",
        )
        self.assert_errors(root, {ARTIFACT_VERSION_INVALID})

    def test_precanonical_ocp_requires_zero_major_version(self) -> None:
        root = self.make_repo()
        path = root / "docs/001-sample/README.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace("Version: 0.1.0", "Version: 1.0.0"),
            encoding="utf-8",
        )
        self.assert_errors(root, {OCP_VERSION_LIFECYCLE_MISMATCH})

    def test_canonical_ocp_requires_nonzero_major_version(self) -> None:
        root = self.make_repo()
        path = root / "docs/001-sample/README.md"
        text = path.read_text(encoding="utf-8").replace("Status: Draft", "Status: Canonical")
        path.write_text(text, encoding="utf-8")
        self.assert_errors(root, {OCP_VERSION_LIFECYCLE_MISMATCH})

        path.write_text(text.replace("Version: 0.1.0", "Version: 1.0.0"), encoding="utf-8")
        self.assertTrue(validate_artifact_governance(root).valid)

    def test_canonical_ocp_cannot_depend_on_precanonical_ocp(self) -> None:
        root = self.make_repo()
        source = root / "docs/001-sample/README.md"
        text = source.read_text(encoding="utf-8")
        text = text.replace("Version: 0.1.0", "Version: 1.0.0")
        text = text.replace("Status: Draft", "Status: Canonical")
        source.write_text(text.replace("\n---\n", "\nDepends-On: OCP-002\n---\n", 1), encoding="utf-8")
        target = root / "docs/002-dependency/README.md"
        target.parent.mkdir()
        target.write_text(
            "---\nDocument-ID: OCP-002\nVersion: 0.1.0\nStatus: Draft\n---\n",
            encoding="utf-8",
        )
        self.assert_errors(root, {CANONICAL_OCP_DEPENDENCY_PRECANONICAL})

    def test_same_act_canonical_ocp_dependencies_satisfy_l2(self) -> None:
        root = self.make_repo()
        source = root / "docs/001-sample/README.md"
        text = source.read_text(encoding="utf-8")
        text = text.replace("Version: 0.1.0", "Version: 1.0.0")
        text = text.replace("Status: Draft", "Status: Canonical")
        source.write_text(text.replace("\n---\n", "\nDepends-On: OCP-002\n---\n", 1), encoding="utf-8")
        target = root / "docs/002-dependency/README.md"
        target.parent.mkdir()
        target.write_text(
            "---\nDocument-ID: OCP-002\nVersion: 1.0.0\nStatus: Canonical\n---\n",
            encoding="utf-8",
        )
        self.assertTrue(validate_artifact_governance(root).valid)

    def test_exact_dependencies_across_admitted_classes_are_accepted(self) -> None:
        root = self.make_repo()
        (root / "adr").mkdir()
        (root / "adr/ADR-000-sample.md").write_text("# ADR-000 — Sample\n", encoding="utf-8")
        self.add_metadata(
            root / "docs/001-sample/README.md",
            "Depends-On: P-001, AD-001, AB-001, ADR-000",
        )
        self.assertTrue(validate_artifact_governance(root).valid)

    def test_dependency_format_must_be_exact(self) -> None:
        root = self.make_repo()
        self.add_metadata(root / "docs/001-sample/README.md", "Depends-On: OCP-1")
        self.assert_errors(root, {DEPENDENCY_REFERENCE_INVALID})

    def test_dependency_target_must_resolve(self) -> None:
        root = self.make_repo()
        self.add_metadata(root / "docs/001-sample/README.md", "Depends-On: OCP-999")
        self.assert_errors(root, {DEPENDENCY_REFERENCE_MISSING})

    def test_dependency_list_cannot_repeat_a_target(self) -> None:
        root = self.make_repo()
        self.add_metadata(
            root / "architecture/discovery/AD-001-sample.md",
            "Depends-On: OCP-001, OCP-001",
        )
        self.assert_errors(root, {DEPENDENCY_REFERENCE_DUPLICATE})

    def test_dependency_cannot_reference_its_own_artifact(self) -> None:
        root = self.make_repo()
        self.add_metadata(root / "docs/001-sample/README.md", "Depends-On: OCP-001")
        self.assert_errors(root, {DEPENDENCY_SELF_REFERENCE})

    def test_normative_rule_identifiers_are_globally_unique(self) -> None:
        root = self.make_repo()
        self.write_rule_manifest(root, "first", "SAMPLE_RULE", "OCP-001 §1")
        self.write_rule_manifest(root, "second", "SAMPLE_RULE", "OCP-001 §2")
        self.assert_errors(root, {NORMATIVE_RULE_ID_DUPLICATE})

    def test_normative_rule_structure_is_validated(self) -> None:
        root = self.make_repo()
        self.write_rule_manifest(root, "sample", "bad-rule", "OCP-001 §1")
        self.assert_errors(root, {NORMATIVE_RULE_INVALID})

    def test_normative_rule_source_must_start_with_an_exact_ocp_id(self) -> None:
        root = self.make_repo()
        self.write_rule_manifest(root, "sample", "SAMPLE_RULE", "section 1")
        self.assert_errors(root, {NORMATIVE_RULE_SOURCE_INVALID})

    def test_normative_rule_source_ocp_must_resolve(self) -> None:
        root = self.make_repo()
        self.write_rule_manifest(root, "sample", "SAMPLE_RULE", "OCP-999 §1")
        self.assert_errors(root, {NORMATIVE_RULE_SOURCE_MISSING})

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

    def head(self, root: Path) -> str:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=root, check=True, capture_output=True, text=True
        ).stdout.strip()

    def set_history_baseline(self, root: Path, baseline: str) -> None:
        path = root / "architecture/artifact-taxonomy.yaml"
        text = path.read_text(encoding="utf-8")
        updated, count = re.subn(
            r'history_audit_baseline: \"?[0-9a-f]{40}\"?',
            f'history_audit_baseline: \"{baseline}\"',
            text,
            count=1,
        )
        self.assertEqual(count, 1)
        path.write_text(updated, encoding="utf-8")
        self.git(root, "add", str(path.relative_to(root)))
        self.git(root, "commit", "-m", "set history audit baseline")

    def create_merge(self, root: Path, name: str) -> str:
        self.git(root, "checkout", "-b", name)
        (root / f"{name}.txt").write_text(f"{name}\n", encoding="utf-8")
        self.git(root, "add", f"{name}.txt")
        self.git(root, "commit", "-m", name)
        self.git(root, "checkout", "main")
        marker = root / f"main-{name}.txt"
        marker.write_text(f"main {name}\n", encoding="utf-8")
        self.git(root, "add", marker.name)
        self.git(root, "commit", "-m", f"main before {name}")
        self.git(root, "merge", "--no-ff", name, "-m", f"merge {name}")
        return self.head(root)

    def test_process_audit_accepts_linear_history_after_baseline(self) -> None:
        root = self.make_git_repo()
        baseline = self.head(root)
        self.set_history_baseline(root, baseline)
        (root / "linear.txt").write_text("linear\n", encoding="utf-8")
        self.git(root, "add", "linear.txt")
        self.git(root, "commit", "-m", "linear after baseline")
        self.assertTrue(validate_process_audit(root, context="main").valid)

    def test_process_audit_accepts_legacy_merge_at_baseline(self) -> None:
        root = self.make_git_repo()
        legacy_merge = self.create_merge(root, "legacy-feature")
        self.set_history_baseline(root, legacy_merge)
        (root / "after-baseline.txt").write_text("linear\n", encoding="utf-8")
        self.git(root, "add", "after-baseline.txt")
        self.git(root, "commit", "-m", "linear after legacy baseline")
        self.assertTrue(validate_process_audit(root, context="main").valid)

    def test_process_audit_rejects_merge_after_baseline(self) -> None:
        root = self.make_git_repo()
        baseline = self.head(root)
        self.set_history_baseline(root, baseline)
        self.create_merge(root, "post-baseline-feature")
        (root / "after-merge.txt").write_text("after\n", encoding="utf-8")
        self.git(root, "add", "after-merge.txt")
        self.git(root, "commit", "-m", "after post-baseline merge")
        self.assertEqual(
            set(validate_process_audit(root, context="main").errors),
            {PROCESS_HISTORY_NON_LINEAR},
        )

    def test_process_audit_rejects_unreachable_baseline(self) -> None:
        root = self.make_git_repo()
        self.set_history_baseline(root, "f" * 40)
        self.assertEqual(
            set(validate_process_audit(root, context="main").errors),
            {PROCESS_HISTORY_AUDIT_FAILED},
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
