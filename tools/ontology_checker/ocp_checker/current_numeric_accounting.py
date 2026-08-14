from __future__ import annotations

import ast
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml


CURRENT_NUMERIC_ACCOUNTING_MAP_INVALID = "CURRENT_NUMERIC_ACCOUNTING_MAP_INVALID"
CURRENT_NUMERIC_ACCOUNTING_DRIFT = "CURRENT_NUMERIC_ACCOUNTING_DRIFT"

MAP_KEYS = frozenset({"schema_version", "rule_owner", "carrier", "claim_format", "metrics"})
METRIC_IDS = (
    "primary_ocp_document_status",
    "defining_concept_status",
    "governed_reviewed_snapshots",
    "p001_primary_invokers",
    "reference_suite",
)
DOCUMENT_STATUS_LABELS = frozenset({"Canonical", "Accepted", "Draft"})
CONCEPT_STATUS_LABELS = frozenset({"Canonical", "Accepted"})
SNAPSHOT_BASES = frozenset({"current-accepted", "retained-acceptance-evidence"})
P001_REF = "P-001@0.1.0"
MAP_PATH = Path("architecture/current-numeric-accounting.yaml")
SNAPSHOT_MAP_PATH = Path("architecture/accepted-document-snapshot-map.yaml")
CLAIM_FORMAT = (
    "- machine-derived current accounting: {ocp_total} primary OCP documents "
    "({ocp_canonical} Canonical / {ocp_accepted} Accepted / {ocp_draft} Draft); "
    "{concept_total} defined Concepts ({concept_canonical} Canonical / "
    "{concept_accepted} Accepted); {snapshot_total} governed reviewed snapshots "
    "({snapshot_current} current Accepted + {snapshot_retained} retained historical); "
    "{p001_invokers} P-001 primary invokers; {fixtures} non-sensitive fixtures; "
    "{tests} unit tests."
)


@dataclass(frozen=True)
class CurrentNumericAccountingResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> CurrentNumericAccountingResult:
    return CurrentNumericAccountingResult(tuple(dict.fromkeys(errors)))


def _frontmatter(fpath: Path) -> dict[str, Any] | None:
    try:
        text = fpath.read_text(encoding="utf-8")
    except OSError:
        return None
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    try:
        loaded = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None
    return loaded if isinstance(loaded, dict) else None


def _references(value: Any) -> tuple[str, ...]:
    if isinstance(value, list):
        return tuple(str(item).strip() for item in value if str(item).strip())
    if isinstance(value, str):
        return tuple(item.strip() for item in value.split(",") if item.strip())
    return ()


def _test_method_count(repo_root: Path) -> int:
    count = 0
    for fpath in sorted((repo_root / "tools/ontology_checker/tests").glob("test_*.py")):
        tree = ast.parse(fpath.read_text(encoding="utf-8"), filename=str(fpath))
        count += sum(
            isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and node.name.startswith("test_")
            for node in ast.walk(tree)
        )
    return count


def derive_current_numeric_accounting(repo_root: Path) -> dict[str, int]:
    metadata: list[dict[str, Any]] = []
    for primary in sorted((repo_root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
        item = _frontmatter(primary)
        if item is None or not isinstance(item.get("Document-ID"), str):
            raise ValueError(f"invalid primary OCP metadata: {primary}")
        metadata.append(item)

    document_counts = Counter(str(item.get("Status") or "") for item in metadata)
    concept_metadata = [item for item in metadata if item.get("Concept-Status") is not None]
    concept_counts = Counter(str(item.get("Concept-Status") or "") for item in concept_metadata)

    snapshot_payload = yaml.safe_load(
        (repo_root / SNAPSHOT_MAP_PATH).read_text(encoding="utf-8")
    )
    snapshot_entries = snapshot_payload.get("entries") if isinstance(snapshot_payload, dict) else None
    if not isinstance(snapshot_entries, list):
        raise ValueError("invalid accepted snapshot map")
    snapshot_counts = Counter(str(item.get("basis") or "") for item in snapshot_entries)

    return {
        "ocp_total": len(metadata),
        "ocp_canonical": document_counts["Canonical"],
        "ocp_accepted": document_counts["Accepted"],
        "ocp_draft": document_counts["Draft"],
        "concept_total": len(concept_metadata),
        "concept_canonical": concept_counts["Canonical"],
        "concept_accepted": concept_counts["Accepted"],
        "snapshot_total": len(snapshot_entries),
        "snapshot_current": snapshot_counts["current-accepted"],
        "snapshot_retained": snapshot_counts["retained-acceptance-evidence"],
        "p001_invokers": sum(
            P001_REF in _references(item.get("Uses-Patterns")) for item in metadata
        ),
        "fixtures": len(list((repo_root / "tools/ontology_checker/fixtures").rglob("*.yaml"))),
        "tests": _test_method_count(repo_root),
    }


def validate_current_numeric_accounting(repo_root: Path) -> CurrentNumericAccountingResult:
    errors: list[str] = []
    try:
        payload = yaml.safe_load((repo_root / MAP_PATH).read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return _result((CURRENT_NUMERIC_ACCOUNTING_MAP_INVALID,))

    if (
        not isinstance(payload, dict)
        or set(payload) != MAP_KEYS
        or payload.get("schema_version") != 1
        or payload.get("rule_owner") != "AD-034"
        or payload.get("carrier") != "README.md"
        or payload.get("claim_format") != CLAIM_FORMAT
        or tuple(payload.get("metrics") or ()) != METRIC_IDS
        or DOCUMENT_STATUS_LABELS != frozenset({"Canonical", "Accepted", "Draft"})
        or CONCEPT_STATUS_LABELS != frozenset({"Canonical", "Accepted"})
        or SNAPSHOT_BASES != frozenset({"current-accepted", "retained-acceptance-evidence"})
        or P001_REF != "P-001@0.1.0"
    ):
        errors.append(CURRENT_NUMERIC_ACCOUNTING_MAP_INVALID)

    try:
        counts = derive_current_numeric_accounting(repo_root)
        if (
            sum(counts[f"ocp_{label.lower()}"] for label in DOCUMENT_STATUS_LABELS)
            != counts["ocp_total"]
            or sum(counts[f"concept_{label.lower()}"] for label in CONCEPT_STATUS_LABELS)
            != counts["concept_total"]
            or sum(counts[f"snapshot_{'current' if basis == 'current-accepted' else 'retained'}"] for basis in SNAPSHOT_BASES)
            != counts["snapshot_total"]
        ):
            errors.append(CURRENT_NUMERIC_ACCOUNTING_DRIFT)
        carrier = repo_root / str(payload.get("carrier", ""))
        expected = CLAIM_FORMAT.format(**counts)
        if carrier.read_text(encoding="utf-8").splitlines().count(expected) != 1:
            errors.append(CURRENT_NUMERIC_ACCOUNTING_DRIFT)
    except (OSError, SyntaxError, ValueError, yaml.YAMLError):
        errors.append(CURRENT_NUMERIC_ACCOUNTING_MAP_INVALID)
    return _result(errors)
