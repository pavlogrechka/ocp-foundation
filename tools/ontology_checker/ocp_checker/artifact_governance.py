from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import subprocess
from typing import Any, Iterable

import yaml


ARTIFACT_ID_MISMATCH = "ARTIFACT_ID_MISMATCH"
ARTIFACT_ID_DUPLICATE = "ARTIFACT_ID_DUPLICATE"
ARTIFACT_STATUS_INVALID = "ARTIFACT_STATUS_INVALID"
ARTIFACT_VERSION_INVALID = "ARTIFACT_VERSION_INVALID"
OCP_VERSION_LIFECYCLE_MISMATCH = "OCP_VERSION_LIFECYCLE_MISMATCH"
CANONICAL_OCP_DEPENDENCY_PRECANONICAL = "CANONICAL_OCP_DEPENDENCY_PRECANONICAL"
ARTIFACT_METADATA_MISSING = "ARTIFACT_METADATA_MISSING"
ARTIFACT_TAXONOMY_INVALID = "ARTIFACT_TAXONOMY_INVALID"
BACKLOG_ID_DUPLICATE = "BACKLOG_ID_DUPLICATE"
DEPENDENCY_REFERENCE_DUPLICATE = "DEPENDENCY_REFERENCE_DUPLICATE"
DEPENDENCY_REFERENCE_INVALID = "DEPENDENCY_REFERENCE_INVALID"
DEPENDENCY_REFERENCE_MISSING = "DEPENDENCY_REFERENCE_MISSING"
DEPENDENCY_SELF_REFERENCE = "DEPENDENCY_SELF_REFERENCE"
AD_BACKLOG_REFERENCE_MISSING = "AD_BACKLOG_REFERENCE_MISSING"
AD_BACKLOG_STATUS_UNRESOLVED = "AD_BACKLOG_STATUS_UNRESOLVED"
PATTERN_REFERENCE_INVALID = "PATTERN_REFERENCE_INVALID"
PATTERN_REFERENCE_MISSING = "PATTERN_REFERENCE_MISSING"
PATTERN_VERSION_INVALID = "PATTERN_VERSION_INVALID"
PATTERN_VERSION_MISMATCH = "PATTERN_VERSION_MISMATCH"
NORMATIVE_RULE_ID_DUPLICATE = "NORMATIVE_RULE_ID_DUPLICATE"
NORMATIVE_RULE_INVALID = "NORMATIVE_RULE_INVALID"
NORMATIVE_RULE_SOURCE_INVALID = "NORMATIVE_RULE_SOURCE_INVALID"
NORMATIVE_RULE_SOURCE_MISSING = "NORMATIVE_RULE_SOURCE_MISSING"
PROCESS_HISTORY_AUDIT_FAILED = "PROCESS_HISTORY_AUDIT_FAILED"
PROCESS_HISTORY_NON_LINEAR = "PROCESS_HISTORY_NON_LINEAR"
PROCESS_HISTORY_SHALLOW = "PROCESS_HISTORY_SHALLOW"

GOVERNANCE_ERROR_CODES = frozenset(
    {
        ARTIFACT_ID_MISMATCH,
        ARTIFACT_ID_DUPLICATE,
        ARTIFACT_STATUS_INVALID,
        ARTIFACT_VERSION_INVALID,
        OCP_VERSION_LIFECYCLE_MISMATCH,
        CANONICAL_OCP_DEPENDENCY_PRECANONICAL,
        ARTIFACT_METADATA_MISSING,
        ARTIFACT_TAXONOMY_INVALID,
        BACKLOG_ID_DUPLICATE,
        DEPENDENCY_REFERENCE_DUPLICATE,
        DEPENDENCY_REFERENCE_INVALID,
        DEPENDENCY_REFERENCE_MISSING,
        DEPENDENCY_SELF_REFERENCE,
        AD_BACKLOG_REFERENCE_MISSING,
        AD_BACKLOG_STATUS_UNRESOLVED,
        PATTERN_REFERENCE_INVALID,
        PATTERN_REFERENCE_MISSING,
        PATTERN_VERSION_INVALID,
        PATTERN_VERSION_MISMATCH,
        NORMATIVE_RULE_ID_DUPLICATE,
        NORMATIVE_RULE_INVALID,
        NORMATIVE_RULE_SOURCE_INVALID,
        NORMATIVE_RULE_SOURCE_MISSING,
        PROCESS_HISTORY_AUDIT_FAILED,
        PROCESS_HISTORY_NON_LINEAR,
        PROCESS_HISTORY_SHALLOW,
    }
)

SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
PATTERN_REF = re.compile(r"^(P-\d{3})@(\d+\.\d+\.\d+)$")
DEPENDENCY_REF = re.compile(
    r"^(?:OCP|AD|P|AB|ADR)-\d{3}$|^ADR-DRAFT-\d{3}$"
)
ADR_PATH_ID = re.compile(r"^(ADR(?:-DRAFT)?-\d{3})(?:-|\.md$)")
RULE_ID = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")
RULE_SOURCE = re.compile(r"^(OCP-\d{3})(?:\s|$)")
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


def _register_artifact(
    registry: dict[str, list[Path]], artifact_id: str, path: Path
) -> None:
    if artifact_id:
        registry.setdefault(artifact_id, []).append(path)


def _validate_rule_manifests(
    repo_root: Path,
    manifest_glob: str,
    artifact_ids: set[str],
) -> tuple[str, ...]:
    errors: list[str] = []
    rule_ids: dict[str, list[Path]] = {}
    for path in sorted(repo_root.glob(manifest_glob)):
        try:
            manifest = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError):
            errors.append(NORMATIVE_RULE_INVALID)
            continue
        rules = manifest.get("rules") if isinstance(manifest, dict) else None
        if not isinstance(rules, list) or not rules:
            errors.append(NORMATIVE_RULE_INVALID)
            continue
        for rule in rules:
            if not isinstance(rule, dict):
                errors.append(NORMATIVE_RULE_INVALID)
                continue
            rule_id = str(rule.get("id") or "")
            kind = str(rule.get("kind") or "validation")
            source = str(rule.get("source") or "")
            if not RULE_ID.fullmatch(rule_id) or kind not in {"validation", "derivation"}:
                errors.append(NORMATIVE_RULE_INVALID)
            elif rule_id:
                rule_ids.setdefault(rule_id, []).append(path)

            source_match = RULE_SOURCE.match(source)
            if source_match is None:
                errors.append(NORMATIVE_RULE_SOURCE_INVALID)
            elif source_match.group(1) not in artifact_ids:
                errors.append(NORMATIVE_RULE_SOURCE_MISSING)

    if any(len(paths) > 1 for paths in rule_ids.values()):
        errors.append(NORMATIVE_RULE_ID_DUPLICATE)
    return tuple(errors)


def validate_artifact_governance(repo_root: Path) -> GovernanceResult:
    errors: list[str] = []
    taxonomy, classes = _load_taxonomy(repo_root)
    if taxonomy is None or classes is None:
        return _result((ARTIFACT_TAXONOMY_INVALID,))

    reference_spec = taxonomy.get("reference_integrity") or {}
    manifest_glob = str(reference_spec.get("normative_rule_manifest_glob") or "")
    if (
        reference_spec.get("artifact_id_uniqueness_scope")
        != ["OCP", "Pattern", "AD", "ADR", "AB"]
        or reference_spec.get("dependency_metadata") != "Depends-On"
        or reference_spec.get("dependency_exact_resolution_required") is not True
        or reference_spec.get("dependency_duplicates_forbidden") is not True
        or reference_spec.get("dependency_self_reference_forbidden") is not True
        or reference_spec.get("dependency_target_classes")
        != ["OCP", "Pattern", "AD", "ADR", "AB"]
        or manifest_glob != "tools/ontology_checker/*rules.yaml"
        or reference_spec.get("normative_rule_ids_global_unique") is not True
        or reference_spec.get("normative_rule_source_class") != "OCP"
        or reference_spec.get("normative_rule_default_kind") != "validation"
        or reference_spec.get("semantic_duplicate_detection") != "external-review"
    ):
        errors.append(ARTIFACT_TAXONOMY_INVALID)

    artifact_registry: dict[str, list[Path]] = {}
    dependencies: list[tuple[str, Any]] = []

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
        for backlog_id, status in backlog.items():
            _register_artifact(artifact_registry, backlog_id, backlog_path)
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
            _register_artifact(artifact_registry, actual, path)
            dependencies.append((actual, metadata.get("Depends-On")))

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
    ocp_statuses: dict[str, str] = {}
    ocp_dependencies: list[tuple[str, Any]] = []
    for path in sorted((repo_root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
        metadata = _metadata(path, "OCP")
        expected_id = f"OCP-{path.parent.name[:3]}"
        actual = str(metadata.get("Document-ID") or "")
        if actual != expected_id:
            errors.append(ARTIFACT_ID_MISMATCH)
        if actual:
            _register_artifact(artifact_registry, actual, path)
            dependencies.append((actual, metadata.get("Depends-On")))
            ocp_dependencies.append((actual, metadata.get("Depends-On")))
        status = str(metadata.get("Status") or "")
        if actual:
            ocp_statuses[actual] = status
        version = str(metadata.get("Version") or "")
        if not status:
            errors.append(ARTIFACT_METADATA_MISSING)
        elif status not in document_allowed:
            errors.append(ARTIFACT_STATUS_INVALID)
        if not version:
            errors.append(ARTIFACT_METADATA_MISSING)
        elif not SEMVER.fullmatch(version):
            errors.append(ARTIFACT_VERSION_INVALID)
        else:
            major = int(version.split(".", 1)[0])
            if status in {"Draft", "Accepted"} and major != 0:
                errors.append(OCP_VERSION_LIFECYCLE_MISMATCH)
            elif status == "Canonical" and major < 1:
                errors.append(OCP_VERSION_LIFECYCLE_MISMATCH)
        if metadata.get("Defines-Concepts"):
            concept_status = str(metadata.get("Concept-Status") or "")
            if not concept_status:
                errors.append(ARTIFACT_METADATA_MISSING)
            elif concept_status not in concept_allowed:
                errors.append(ARTIFACT_STATUS_INVALID)

    for source_id, value in ocp_dependencies:
        if ocp_statuses.get(source_id) != "Canonical" or value is None:
            continue
        for ref in _iter_invocations(value):
            if ref.startswith("OCP-") and ocp_statuses.get(ref) not in {None, "Canonical"}:
                errors.append(CANONICAL_OCP_DEPENDENCY_PRECANONICAL)

    ad_allowed = _status_set(classes.get("AD") or {})
    for path in sorted((repo_root / "architecture/discovery").glob("AD-[0-9][0-9][0-9]-*.md")):
        metadata = _metadata(path, "AD")
        expected_id = path.name[:6]
        actual = str(metadata.get("Decision-ID") or "")
        if actual != expected_id:
            errors.append(ARTIFACT_ID_MISMATCH)
        if actual:
            _register_artifact(artifact_registry, actual, path)
            dependencies.append((actual, metadata.get("Depends-On")))
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

    for path in sorted((repo_root / "adr").glob("ADR-*.md")):
        match = ADR_PATH_ID.match(path.name)
        if match is None:
            errors.append(ARTIFACT_ID_MISMATCH)
            continue
        artifact_id = match.group(1)
        _register_artifact(artifact_registry, artifact_id, path)
        metadata = _frontmatter(path)
        dependencies.append((artifact_id, metadata.get("Depends-On")))

    if any(len(paths) > 1 for paths in artifact_registry.values()):
        errors.append(ARTIFACT_ID_DUPLICATE)

    artifact_ids = set(artifact_registry)
    for source_id, value in dependencies:
        if value is None:
            continue
        refs = tuple(_iter_invocations(value))
        if not refs:
            errors.append(DEPENDENCY_REFERENCE_INVALID)
            continue
        if len(refs) != len(set(refs)):
            errors.append(DEPENDENCY_REFERENCE_DUPLICATE)
        for ref in refs:
            if not DEPENDENCY_REF.fullmatch(ref):
                errors.append(DEPENDENCY_REFERENCE_INVALID)
            elif ref == source_id:
                errors.append(DEPENDENCY_SELF_REFERENCE)
            elif ref not in artifact_ids:
                errors.append(DEPENDENCY_REFERENCE_MISSING)

    if manifest_glob == "tools/ontology_checker/*rules.yaml":
        errors.extend(
            _validate_rule_manifests(repo_root, manifest_glob, artifact_ids)
        )

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
