from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class ConceptGraphResult:
    errors: tuple[str, ...]
    rendered_map: str

    @property
    def valid(self) -> bool:
        return not self.errors


def _read_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    loaded = yaml.safe_load(text[4:end])
    return loaded if isinstance(loaded, dict) else {}


def _ontology_registry(path: Path) -> dict[str, str]:
    rows: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0] in {"Concept", "---"} or set(cells[0]) == {"-"}:
            continue
        rows[cells[0]] = cells[1]
    return rows


def _load_yaml(path: Path) -> dict[str, Any]:
    loaded = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(loaded, dict):
        raise ValueError(f"{path} must contain a mapping")
    return loaded


def _has_cycle(graph: dict[str, set[str]]) -> bool:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for target in sorted(graph.get(node, set())):
            if visit(target):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    return any(visit(node) for node in sorted(graph))


def _render_map(registry: dict[str, str], graph: dict[str, set[str]], future: dict[str, Any]) -> str:
    lines = [
        "# Foundation Concept Map",
        "",
        "> GENERATED FILE. Current-state sections are derived from OCP-000 and the governed Concept dependency record.",
        "> Future intent is rendered from `foundation-future-edges.yaml` and is not a current dependency.",
        "",
        "## Registered Concepts",
        "",
        "| Concept | Status |",
        "|---|---|",
    ]
    for concept, status in sorted(registry.items()):
        lines.append(f"| {concept} | {status} |")

    lines.extend(["", "## Current normative dependencies", ""])
    current_edges = [(source, target) for source, targets in graph.items() for target in targets]
    if current_edges:
        for source, target in sorted(current_edges):
            lines.append(f"- `{source} → {target}`")
    else:
        lines.append("- None.")

    lines.extend(["", "## Current isolated defined Concepts", ""])
    connected = {item for edge in current_edges for item in edge}
    defined = set(graph)
    isolated = sorted(defined - connected)
    for concept in isolated:
        lines.append(f"- `{concept}`")

    lines.extend(["", "## Future intent — non-normative", ""])
    for edge in future.get("edges", []):
        source = edge.get("from")
        target = edge.get("to")
        basis = edge.get("basis")
        style = " (dashed)" if edge.get("style") == "dashed" else ""
        lines.append(f"- `{source} ⇢ {target}`{style} — {basis}")
    lines.append("")
    return "\n".join(lines)


def validate_and_render_concept_graph(repo_root: Path, context: str = "pr") -> ConceptGraphResult:
    if context not in {"pr", "main"}:
        raise ValueError("context must be 'pr' or 'main'")

    errors: list[str] = []
    registry_path = repo_root / "docs/000-operational-ontology/README.md"
    dependency_path = repo_root / "architecture/baselines/concept-dependencies.yaml"
    future_path = repo_root / "architecture/baselines/foundation-future-edges.yaml"

    if not registry_path.exists():
        return ConceptGraphResult(("CONCEPT_GRAPH_REGISTRY_MISSING",), "")
    if not dependency_path.exists():
        return ConceptGraphResult(("CONCEPT_GRAPH_DEPENDENCY_SOURCE_MISSING",), "")
    if not future_path.exists():
        return ConceptGraphResult(("CONCEPT_GRAPH_FUTURE_SOURCE_MISSING",), "")

    registry = _ontology_registry(registry_path)
    dependencies = _load_yaml(dependency_path).get("concepts") or {}
    future = _load_yaml(future_path)
    if not isinstance(dependencies, dict):
        return ConceptGraphResult(("CONCEPT_GRAPH_DEPENDENCY_SOURCE_INVALID",), "")

    defining_documents: list[tuple[Path, dict[str, Any]]] = []
    has_frontmatter_dependency_source = False
    for path in sorted((repo_root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
        metadata = _read_frontmatter(path)
        defining_documents.append((path, metadata))
        if "Concept-Depends-On" in metadata:
            has_frontmatter_dependency_source = True

    if dependency_path.exists() and has_frontmatter_dependency_source:
        errors.append("CONCEPT_GRAPH_MULTIPLE_DEPENDENCY_SOURCES")

    graph: dict[str, set[str]] = {}
    for concept, entry in dependencies.items():
        if concept not in registry:
            errors.append("CONCEPT_GRAPH_UNREGISTERED_NODE")
        if not isinstance(entry, dict):
            errors.append("CONCEPT_GRAPH_DEPENDENCY_ENTRY_INVALID")
            continue
        targets = entry.get("depends_on") or []
        if not isinstance(targets, list):
            errors.append("CONCEPT_GRAPH_DEPENDENCY_ENTRY_INVALID")
            continue
        graph[str(concept)] = {str(target) for target in targets}
        for target in targets:
            if target not in registry:
                errors.append("CONCEPT_GRAPH_PHANTOM_REFERENCE")

    if _has_cycle(graph):
        errors.append("CONCEPT_GRAPH_CYCLE")

    for _, metadata in defining_documents:
        names = metadata.get("Defines-Concepts")
        status = metadata.get("Concept-Status")
        if not names:
            continue
        if context == "main" and status == "Under Review":
            errors.append("MAIN_CONCEPT_UNDER_REVIEW")

    for concept, entry in dependencies.items():
        expected_document = str(entry.get("defining_document", "")) if isinstance(entry, dict) else ""
        found = False
        for _, metadata in defining_documents:
            names = [item.strip() for item in str(metadata.get("Defines-Concepts", "")).split(",") if item.strip()]
            if concept in names and metadata.get("Document-ID") == expected_document:
                found = True
                break
        if not found:
            errors.append("CONCEPT_GRAPH_DEFINING_DOCUMENT_MISSING")

    rendered = _render_map(registry, graph, future)
    return ConceptGraphResult(tuple(dict.fromkeys(errors)), rendered)
