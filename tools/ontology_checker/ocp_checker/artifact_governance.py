from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import subprocess
from typing import Any, Iterable

import yaml


ARTIFACT_ID_MISMATCH = "ARTIFACT_ID_MISMATCH"
ARTIFACT_STATUS_INVALID = "ARTIFACT_STATUS_INVALID"
ARTIFACT_METADATA_MISSING = "ARTIFACT_METADATA_MISSING"
ARTIFACT_TAXONOMY_INVALID = "ARTIFACT_TAXONOMY_INVALID"
BACKLOG_ID_DUPLICATE = "BACKLOG_ID_DUPLICATE"
AD_BACKLOG_REFERENCE_MISSING = "AD_BACKLOG_REFERENCE_MISSING"
AD_BACKLOG_STATUS_UNRESOLVED = "AD_BACKLOG_STATUS_UNRESOLVED"
PATTERN_REFERENCE_INVALID = "PATTERN_REFERENCE_INVALID"
PATTERN_REFERENCE_MISSING = "PATTERN_REFERENCE_MISSING"
PATTERN_VERSION_INVALID = "PATTERN_VERSION_INVALID"
PATTERN_VERSION_MISMATCH = "PATTERN_VERSION_MISMATCH"
PROCESS_HISTORY_AUDIT_FAILED = "PROCESS_HISTORY_AUDIT_FAILED"
PROCESS_HISTORY_NON_LINEAR = "PROCESS_HISTORY_NON_LINEAR"
PROCESS_HISTORY_SHALLOW = "PROCESS_HISTORY_SHALLOW"

GOVERNANCE_ERROR_CODES = frozenset(
    {
        ARTIFACT_ID_MISMATCH,
        ARTIFACT_STATUS_INVALID,
        ARTIFACT_METADATA_MISSING,
        ARTIFACT_TAXONOMY_INVALID,
        BACKLOG_ID_DUPLICATE,
        AD_BACKLOG_REFERENCE_MISSING,
        AD_BACKLOG_STATUS_UNRESOLVED,
        PATTERN_REFERENCE_INVALID,
        PATTERN_REFERENCE_MISSING,
        PATTERN_VERSION_INVALID,
        PATTERN_VERSION_MISMATCH,
        PROCESS_HISTORY_AUDIT_FAILED,
        PROCESS_HISTORY_NON_LINEAR,
        PROCESS_HISTORY_SHALLOW,
    }
)

SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
PATTERN_REF = re.compile(r"^(P-\d{3})@(\d+\.\d+\.\d+)$")
AB_REF = re.compile(r"\bAB-\d{3}\b")
COMMIT_SHA = re.compile(r"^[0-9a-f]{40}$")


@dataclass(frozen=True)
class GovernanceResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> GovernanceResult:
    return GovernanceResult(tuple(dict.fromkeys(errors)))


def _frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    loaded = yaml.safe_load(text[4:end])
    return loaded if isinstance(loaded, dict) else {}


def _legacy_ad_metadata(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    metadata: dict[str, Any] = {}
    heading = re.search(r"^#\s+(AD-\d{3})\b", text, flags=re.MULTILINE)
    if heading:
        metadata["Decision-ID"] = heading.group(1)
    for key in ("Status", "Applies-To"):
        match = re.search(rf"^-\s+{re.escape(key)}:\s*(.+?)\s*$", text, flags=re.MULTILINE)
        if match:
            metadata[key] = match.group(1)
    return metadata


def _metadata(path: Path, artifact_class: str) -> dict[str, Any]:
    data = _frontmatter(path)
    if not data and artifact_class == "AD":
        data = _legacy_ad_metadata(path)
    return data


def _backlog_rows(path: Path) -> tuple[dict[str, str], bool]:
    rows: dict[str, str] = {}
    duplicate = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 4 or not re.fullmatch(r"AB-\d{3}", cells[0]):
            continue
        if cells[0] in rows:
            duplicate = True
        rows[cells[0]] = cells[2]
    return rows, duplicate


def _status_set(class_spec: dict[str, Any], field: str = "lifecycle") -> set[str]:
    values = class_spec.get(field) or []
    return {str(item) for item in values} if isinstance(values, list) else set()


def _iter_invocations(value: Any) -> Iterable[str]:
    if value is None:
        return ()
    if isinstance(value, list):
        return (str(item).strip() for item in value if str(item).strip())
    return (item.strip() for item in str(value).split(",") if item.strip())


def _load_taxonomy(repo_root: Path) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    path = repo_root / "architecture/artifact-taxonomy.yaml"
    try:
        taxonomy = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return None, None
    if not isinstance(taxonomy, dict):
        return None, None
    classes = taxonomy.get("artifact_classes")
    if not isinstance(classes, dict):
        return None, None
    return taxonomy, classes


def validate_artifact_governance(repo_root: Path) -> GovernanceResult:
    errors: list[str] = []
    taxonomy, classes = _load_taxonomy(repo_root)
    if taxonomy is None or classes is None:
        return _result((ARTIFACT_TAXONOMY_INVALID,))

    backlog_path = repo_root / "backlog/architecture-backlog.md"
    ab_spec = classes.get("AB") or {}
    allowed_ab = _status_set(ab_spec)
    active_values = ab_spec.get("active_states")
    active_ab = {str(item) for item in active_values} if isinstance(active_values, list) else set()
    if not allowed_ab or not active_ab or not active_ab.issubset(allowed_ab):
        errors.append(ARTIFACT_TAXONOMY_INVALID)

    pattern_spec = classes.get("Pattern") or {}
    pattern_allowed = _status_set(pattern_spec)
    if (
        pattern_spec.get("version_format") != "semver"
        or pattern_spec.get("invocation_version_policy") != "track-current"
        or pattern_spec.get("version_change_requires_atomic_invoker_update") is not True
    ):
        errors.append(ARTIFACT_TAXONOMY_INVALID)

    commit_spec = taxonomy.get("commit_convention") or {}
    baseline = str(commit_spec.get("history_audit_baseline") or "")
    if (
        commit_spec.get("merge_method") != "squash"
        or commit_spec.get("linear_history_required") is not True
        or commit_spec.get("history_audit_scope") != "post_baseline_reachable_commits"
        or commit_spec.get("history_audit_requires_complete_history") is not True
        or not COMMIT_SHA.fullmatch(baseline)
    ):
        errors.append(ARTIFACT_TAXONOMY_INVALID)

    if not backlog_path.exists():
        errors.append(ARTIFACT_METADATA_MISSING)
        backlog: dict[str, str] = {}
    else:
        backlog, duplicate = _backlog_rows(backlog_path)
        if duplicate:
            errors.append(BACKLOG_ID_DUPLICATE)
        for status in backlog.values():
            if status not in allowed_ab:
                errors.append(ARTIFACT_STATUS_INVALID)

    pattern_ids: set[str] = set()
    pattern_versions: dict[str, str] = {}
    for path in sorted((repo_root / "patterns").glob("P-[0-9][0-9][0-9]-*.md")):
        metadata = _metadata(path, "Pattern")
        expected_id = "-".join(path.name.split("-", 2)[:2])
        actual = str(metadata.get("Pattern-ID") or "")
        if actual != expected_id:
            errors.append(ARTIFACT_ID_MISMATCH)
        if actual:
            pattern_ids.add(actual)

        status = str(metadata.get("Status") or "")
        version = str(metadata.get("Version") or "")
        if not status or not version:
            errors.append(ARTIFACT_METADATA_MISSING)
        if status and status not in pattern_allowed:
            errors.append(ARTIFACT_STATUS_INVALID)
        if version and not SEMVER.fullmatch(version):
            errors.append(PATTERN_VERSION_INVALID)
        elif actual and version:
            pattern_versions[actual] = version

    ocp_spec = classes.get("OCP") or {}
    document_allowed = _status_set(ocp_spec, "document_lifecycle")
    concept_allowed = _status_set(ocp_spec, "concept_lifecycle")
    for path in sorted((repo_root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
        metadata = _metadata(path, "OCP")
        expected_id = f"OCP-{path.parent.name[:3]}"
        if str(metadata.get("Document-ID") or "") != expected_id:
            errors.append(ARTIFACT_ID_MISMATCH)
        status = str(metadata.get("Status") or "")
        if not status:
            errors.append(ARTIFACT_METADATA_MISSING)
        elif status not in document_allowed:
            errors.append(ARTIFACT_STATUS_INVALID)
        if metadata.get("Defines-Concepts"):
            concept_status = str(metadata.get("Concept-Status") or "")
            if not concept_status:
                errors.append(ARTIFACT_METADATA_MISSING)
            elif concept_status not in concept_allowed:
                errors.append(ARTIFACT_STATUS_INVALID)

    ad_allowed = _status_set(classes.get("AD") or {})
    for path in sorted((repo_root / "architecture/discovery").glob("AD-[0-9][0-9][0-9]-*.md")):
        metadata = _metadata(path, "AD")
        expected_id = path.name[:6]
        if str(metadata.get("Decision-ID") or "") != expected_id:
            errors.append(ARTIFACT_ID_MISMATCH)
        status = str(metadata.get("Status") or "")
        if not status:
            errors.append(ARTIFACT_METADATA_MISSING)
        elif status not in ad_allowed:
            errors.append(ARTIFACT_STATUS_INVALID)
        if status == "Accepted":
            refs = set(AB_REF.findall(str(metadata.get("Applies-To") or "")))
            for ref in refs:
                if ref not in backlog:
                    errors.append(AD_BACKLOG_REFERENCE_MISSING)
                elif backlog[ref] in active_ab:
                    errors.append(AD_BACKLOG_STATUS_UNRESOLVED)

    for root in (repo_root / "docs", repo_root / "architecture", repo_root / "patterns"):
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.md")):
            metadata = _frontmatter(path)
            for invocation in _iter_invocations(metadata.get("Uses-Patterns")):
                match = PATTERN_REF.fullmatch(invocation)
                if not match:
                    errors.append(PATTERN_REFERENCE_INVALID)
                    continue
                pattern_id, version = match.groups()
                if pattern_id not in pattern_ids:
                    errors.append(PATTERN_REFERENCE_MISSING)
                elif pattern_id in pattern_versions and pattern_versions[pattern_id] != version:
                    errors.append(PATTERN_VERSION_MISMATCH)

    return _result(errors)


def _run_git(repo_root: Path, *args: str) -> subprocess.CompletedProcess[str] | None:
    try:
        return subprocess.run(
            ["git", *args],
            cwd=repo_root,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None


def validate_process_audit(repo_root: Path, context: str) -> GovernanceResult:
    if context != "main":
        return _result(())

    taxonomy, _ = _load_taxonomy(repo_root)
    commit_spec = taxonomy.get("commit_convention") if taxonomy else None
    baseline = str(commit_spec.get("history_audit_baseline") or "") if isinstance(commit_spec, dict) else ""
    if not isinstance(commit_spec, dict) or (
        commit_spec.get("linear_history_required") is not True
        or commit_spec.get("history_audit_scope") != "post_baseline_reachable_commits"
        or commit_spec.get("history_audit_requires_complete_history") is not True
        or not COMMIT_SHA.fullmatch(baseline)
    ):
        return _result((PROCESS_HISTORY_AUDIT_FAILED,))

    shallow = _run_git(repo_root, "rev-parse", "--is-shallow-repository")
    if shallow is None:
        return _result((PROCESS_HISTORY_AUDIT_FAILED,))
    shallow_value = shallow.stdout.strip().lower()
    if shallow_value == "true":
        return _result((PROCESS_HISTORY_SHALLOW,))
    if shallow_value != "false":
        return _result((PROCESS_HISTORY_AUDIT_FAILED,))

    ancestor = _run_git(repo_root, "merge-base", "--is-ancestor", baseline, "HEAD")
    if ancestor is None:
        return _result((PROCESS_HISTORY_AUDIT_FAILED,))

    merges = _run_git(repo_root, "rev-list", "--min-parents=2", f"{baseline}..HEAD")
    if merges is None:
        return _result((PROCESS_HISTORY_AUDIT_FAILED,))
    return _result((PROCESS_HISTORY_NON_LINEAR,)) if merges.stdout.strip() else _result(())
