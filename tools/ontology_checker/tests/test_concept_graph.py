from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from ocp_checker.concept_graph import validate_and_render_concept_graph


REGISTRY = """# registry
| Concept | Status | Specification |
|---|---|---|
| Resource | Accepted | OCP-003 |
| Operation | Accepted | OCP-004 |
| Assignment | Accepted | OCP-005 |
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


class ConceptGraphTests(unittest.TestCase):
    def make_repo(
        self,
        dependencies: dict[str, list[str]],
        *,
        status: str = "Accepted",
        omit_declaration_for: str | None = None,
        omit_document_id_for: str | None = None,
        legacy_source: bool = False,
    ) -> Path:
        root = Path(tempfile.mkdtemp())
        write(root / "docs/000-operational-ontology/README.md", REGISTRY)

        for number, document_id, concept in (
            (3, "OCP-003", "Resource"),
            (4, "OCP-004", "Operation"),
            (5, "OCP-005", "Assignment"),
        ):
            document_line = (
                ""
                if concept == omit_document_id_for
                else f"Document-ID: {document_id}\n"
            )
            dependency_line = (
                ""
                if concept == omit_declaration_for
                else f"Concept-Depends-On: [{', '.join(dependencies[concept])}]\n"
            )
            concept_status = status if concept == "Assignment" else "Accepted"
            write(
                root / f"docs/{number:03d}-concept/README.md",
                "---\n"
                f"{document_line}"
                f"Defines-Concepts: {concept}\n"
                f"{dependency_line}"
                f"Concept-Status: {concept_status}\n"
                "---\n",
            )

        if legacy_source:
            write(
                root / "architecture/baselines/concept-dependencies.yaml",
                "concepts: {}\n",
            )
        write(
            root / "architecture/baselines/foundation-future-edges.yaml",
            "edges: []\n",
        )
        return root

    @staticmethod
    def valid_dependencies() -> dict[str, list[str]]:
        return {
            "Resource": [],
            "Operation": [],
            "Assignment": ["Resource", "Operation"],
        }

    def test_valid_graph_is_deterministic(self) -> None:
        root = self.make_repo(self.valid_dependencies())
        first = validate_and_render_concept_graph(root)
        second = validate_and_render_concept_graph(root)

        self.assertTrue(first.valid)
        self.assertEqual(first.rendered_map, second.rendered_map)
        self.assertIn("`Assignment → Operation`", first.rendered_map)

    def test_explicit_empty_dependency_declaration_is_required(self) -> None:
        root = self.make_repo(
            self.valid_dependencies(),
            omit_declaration_for="Resource",
        )
        result = validate_and_render_concept_graph(root)

        self.assertIn(
            "CONCEPT_GRAPH_DEPENDENCY_DECLARATION_MISSING",
            result.errors,
        )

    def test_legacy_source_is_rejected_after_migration(self) -> None:
        root = self.make_repo(self.valid_dependencies(), legacy_source=True)
        result = validate_and_render_concept_graph(root)

        self.assertIn(
            "CONCEPT_GRAPH_MULTIPLE_DEPENDENCY_SOURCES",
            result.errors,
        )

    def test_phantom_reference_is_rejected(self) -> None:
        dependencies = self.valid_dependencies()
        dependencies["Assignment"] = ["Phantom"]
        result = validate_and_render_concept_graph(self.make_repo(dependencies))

        self.assertIn("CONCEPT_GRAPH_PHANTOM_REFERENCE", result.errors)

    def test_cycle_is_rejected(self) -> None:
        dependencies = self.valid_dependencies()
        dependencies["Resource"] = ["Assignment"]
        dependencies["Assignment"] = ["Resource"]
        result = validate_and_render_concept_graph(self.make_repo(dependencies))

        self.assertIn("CONCEPT_GRAPH_CYCLE", result.errors)

    def test_under_review_is_allowed_in_pr_context(self) -> None:
        root = self.make_repo(
            self.valid_dependencies(),
            status="Under Review",
        )
        result = validate_and_render_concept_graph(root, context="pr")

        self.assertNotIn("MAIN_CONCEPT_UNDER_REVIEW", result.errors)

    def test_under_review_is_rejected_in_main_context(self) -> None:
        root = self.make_repo(
            self.valid_dependencies(),
            status="Under Review",
        )
        result = validate_and_render_concept_graph(root, context="main")

        self.assertIn("MAIN_CONCEPT_UNDER_REVIEW", result.errors)

    def test_defining_document_id_is_required(self) -> None:
        root = self.make_repo(
            self.valid_dependencies(),
            omit_document_id_for="Resource",
        )
        result = validate_and_render_concept_graph(root)

        self.assertIn("CONCEPT_GRAPH_DEFINING_DOCUMENT_MISSING", result.errors)


if __name__ == "__main__":
    unittest.main()
