from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import yaml

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
    def make_repo(self, dependencies: dict, status: str = "Accepted", add_frontmatter_source: bool = False) -> Path:
        root = Path(tempfile.mkdtemp())
        write(root / "docs/000-operational-ontology/README.md", REGISTRY)
        for number, document, concept in (
            (3, "OCP-003", "Resource"),
            (4, "OCP-004", "Operation"),
            (5, "OCP-005", "Assignment"),
        ):
            concept_dependency = "\nConcept-Depends-On: Resource, Operation" if add_frontmatter_source and concept == "Assignment" else ""
            write(
                root / f"docs/{number:03d}-concept/README.md",
                f"---\nDocument-ID: {document}\nDefines-Concepts: {concept}\nConcept-Status: {status if concept == 'Assignment' else 'Accepted'}{concept_dependency}\n---\n",
            )
        write(
            root / "architecture/baselines/concept-dependencies.yaml",
            yaml.safe_dump({"concepts": dependencies}, sort_keys=False),
        )
        write(root / "architecture/baselines/foundation-future-edges.yaml", "edges: []\n")
        return root

    def valid_dependencies(self) -> dict:
        return {
            "Resource": {"defining_document": "OCP-003", "depends_on": []},
            "Operation": {"defining_document": "OCP-004", "depends_on": []},
            "Assignment": {"defining_document": "OCP-005", "depends_on": ["Resource", "Operation"]},
        }

    def test_valid_graph_is_deterministic(self) -> None:
        root = self.make_repo(self.valid_dependencies())
        first = validate_and_render_concept_graph(root)
        second = validate_and_render_concept_graph(root)
        self.assertTrue(first.valid)
        self.assertEqual(first.rendered_map, second.rendered_map)
        self.assertIn("`Assignment → Operation`", first.rendered_map)

    def test_phantom_reference_is_rejected(self) -> None:
        dependencies = self.valid_dependencies()
        dependencies["Assignment"]["depends_on"] = ["Phantom"]
        root = self.make_repo(dependencies)
        result = validate_and_render_concept_graph(root)
        self.assertIn("CONCEPT_GRAPH_PHANTOM_REFERENCE", result.errors)

    def test_cycle_is_rejected(self) -> None:
        dependencies = self.valid_dependencies()
        dependencies["Resource"]["depends_on"] = ["Assignment"]
        dependencies["Assignment"]["depends_on"] = ["Resource"]
        root = self.make_repo(dependencies)
        result = validate_and_render_concept_graph(root)
        self.assertIn("CONCEPT_GRAPH_CYCLE", result.errors)

    def test_under_review_is_allowed_in_pr_context(self) -> None:
        root = self.make_repo(self.valid_dependencies(), status="Under Review")
        result = validate_and_render_concept_graph(root, context="pr")
        self.assertNotIn("MAIN_CONCEPT_UNDER_REVIEW", result.errors)

    def test_under_review_is_rejected_in_main_context(self) -> None:
        root = self.make_repo(self.valid_dependencies(), status="Under Review")
        result = validate_and_render_concept_graph(root, context="main")
        self.assertIn("MAIN_CONCEPT_UNDER_REVIEW", result.errors)

    def test_staging_and_frontmatter_sources_cannot_coexist(self) -> None:
        root = self.make_repo(self.valid_dependencies(), add_frontmatter_source=True)
        result = validate_and_render_concept_graph(root)
        self.assertIn("CONCEPT_GRAPH_MULTIPLE_DEPENDENCY_SOURCES", result.errors)


if __name__ == "__main__":
    unittest.main()
