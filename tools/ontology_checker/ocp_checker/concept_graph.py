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


def _render_map(
    registry: dict[str, str],
    graph: dict[str, set[str]],
    future: dict[str, Any],
) -> str:
    lines = [
        "# Foundation Concept Map",
        "",
        "> GENERATED FILE. Current-state sections are derived from OCP-000 and defining-document `Concept-Depends-On` metadata.",
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
    current_edges = [
        (source, target)
        for source, targets in graph.items()
        for target in targets
    ]
    if current_edges:
        for source, target in sorted(current_edges):
            lines.append(f"- `{source} → {target}`")
    else:
        lines.append("- None.")

    lines.extend(["", "## Current isolated defined Concepts", ""])
    connected = {item for edge in current_edges for item in edge}
    for concept in sorted(set(graph) - connected):
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


def validate_and_render_concept_graph(
    repo_root: Path,
    context: str = "pr",
) -> ConceptGraphResult:
    if context not in {"pr", "main"}:
        raise ValueError("context must be 'pr' or 'main'")

    errors: list[str] = []
    registry_path = repo_root / "docs/000-operational-ontology/README.md"
    legacy_dependency_path = (
        repo_root / "architecture/baselines/concept-dependencies.yaml"
    )
    future_path = repo_root / "architecture/baselines/foundation-future-edges.yaml"

    if not registry_path.exists():
        return ConceptGraphResult(("CONCEPT_GRAPH_REGISTRY_MISSING",), "")
    if not future_path.exists():
        return ConceptGraphResult(("CONCEPT_GRAPH_FUTURE_SOURCE_MISSING",), "")

    registry = _ontology_registry(registry_path)
    future = _load_yaml(future_path)
    if legacy_dependency_path.exists():
        errors.append("CONCEPT_GRAPH_MULTIPLE_DEPENDENCY_SOURCES")

    graph: dict[str, set[str]] = {}
    defining_documents: dict[str, str] = {}

    for path in sorted((repo_root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
        metadata = _read_frontmatter(path)
        names = [
            item.strip()
            for item in str(metadata.get("Defines-Concepts", "")).split(",")
            if item.strip()
        ]
        if not names:
            continue

        document_id = metadata.get("Document-ID")
        if not isinstance(document_id, str) or not document_id.strip():
            errors.append("CONCEPT_GRAPH_DEFINING_DOCUMENT_MISSING")

        if "Concept-Depends-On" not in metadata:
            errors.append("CONCEPT_GRAPH_DEPENDENCY_DECLARATION_MISSING")
            continue

        targets = metadata.get("Concept-Depends-On")
        if not isinstance(targets, list):
            errors.append("CONCEPT_GRAPH_DEPENDENCY_DECLARATION_INVALID")
            continue

        for concept in names:
            if concept not in registry:
                errors.append("CONCEPT_GRAPH_UNREGISTERED_NODE")
            if concept in defining_documents:
                errors.append("CONCEPT_GRAPH_MULTIPLE_DEFINING_DOCUMENTS")
            elif isinstance(document_id, str):
                defining_documents[concept] = document_id

            graph[concept] = {str(target) for target in targets}
            for target in targets:
                if target not in registry:
                    errors.append("CONCEPT_GRAPH_PHANTOM_REFERENCE")

        if context == "main" and metadata.get("Concept-Status") == "Under Review":
            errors.append("MAIN_CONCEPT_UNDER_REVIEW")

    if _has_cycle(graph):
        errors.append("CONCEPT_GRAPH_CYCLE")

    rendered = _render_map(registry, graph, future)
    return ConceptGraphResult(tuple(dict.fromkeys(errors)), rendered)
