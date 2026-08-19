#!/usr/bin/env python3
from __future__ import annotations

import argparse
import difflib
import os
import sys
from pathlib import Path

import yaml

from ocp_checker import load_fixture, validate_reference_fixture, validate_repository
from ocp_checker.artifact_governance import validate_artifact_governance, validate_process_audit
from ocp_checker.accepted_snapshot import validate_accepted_snapshots
from ocp_checker.concept_graph import validate_and_render_concept_graph
from ocp_checker.current_numeric_accounting import validate_current_numeric_accounting
from ocp_checker.consumer_need_discovery import validate_consumer_need_discovery
from ocp_checker.assignment_amendment_q2 import validate_assignment_amendment_q2
from ocp_checker.assignment_temporal_scope import validate_assignment_temporal_scope
from ocp_checker.assignment_consumer_compatibility import validate_assignment_consumer_compatibility
from ocp_checker.assignment_consumer_pressure import validate_assignment_consumer_pressure
from ocp_checker.assignment_norm_compatibility import validate_assignment_norm_compatibility
from ocp_checker.assignment_q3_lifecycle import validate_assignment_q3_lifecycle
from ocp_checker.assignment_q2_sufficiency import validate_assignment_q2_sufficiency
from ocp_checker.assignment_q9_sufficiency import validate_assignment_q9_sufficiency
from ocp_checker.assignment_stable_surface import validate_assignment_stable_surface
from ocp_checker.constraint_stable_surface import validate_constraint_stable_surface
from ocp_checker.constraint_q6_sufficiency import validate_constraint_q6_sufficiency
from ocp_checker.constraint_document_status_readiness import validate_constraint_document_status_readiness
from ocp_checker.event_stable_surface import validate_event_stable_surface
from ocp_checker.event_promotion_selection import validate_event_promotion_selection
from ocp_checker.event_lifecycle_promotion import validate_event_lifecycle_promotion
from ocp_checker.event_concept_canonicalization import validate_event_concept_canonicalization
from ocp_checker.foundation_promotion_gate import validate_foundation_promotion_gate
from ocp_checker.foundation_promotion_reassessment import validate_foundation_promotion_reassessment
from ocp_checker.open_question_sync import validate_open_question_sync
from ocp_checker.ocp024_acceptance import validate_ocp024_acceptance


def validate_any_fixture(fixture: dict):
    return validate_reference_fixture(fixture)


def resolve_context(requested: str) -> str:
    if requested in {"pr", "main"}:
        return requested
    event = os.environ.get("GITHUB_EVENT_NAME", "")
    ref = os.environ.get("GITHUB_REF", "")
    return "main" if event == "push" and ref == "refs/heads/main" else "pr"


def first_map_difference(committed: str, generated: str) -> str:
    diff = difflib.unified_diff(
        committed.splitlines(),
        generated.splitlines(),
        fromfile="committed/foundation-map.md",
        tofile="generated/foundation-map.md",
        lineterm="",
    )
    for line in diff:
        if line.startswith(("---", "+++", "@@")):
            continue
        return line
    return "content differs"


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate OCP reference YAML fixtures.")
    parser.add_argument("path", nargs="?", default=str(Path(__file__).with_name("fixtures")))
    parser.add_argument("--repo-root", default=str(Path(__file__).resolve().parents[2]))
    parser.add_argument("--context", choices=("auto", "pr", "main"), default="auto")
    args = parser.parse_args()

    context = resolve_context(args.context)
    root = Path(args.path)
    files = sorted(root.rglob("*.yaml")) if root.is_dir() else [root]
    failures = 0
    for path in files:
        try:
            fixture = load_fixture(path)
            result = validate_any_fixture(fixture)
            expected = fixture.get("expected", {})
            ok = result.valid == bool(expected.get("valid")) and set(result.errors) == set(expected.get("error_codes", []))
            print(f"{'PASS' if ok else 'FAIL'} {fixture.get('case_id', path.name)} valid={result.valid} errors={list(result.errors)}")
        except (OSError, ValueError, yaml.YAMLError) as exc:
            ok = False
            print(f"FAIL {path}: {type(exc).__name__}: {exc}")
        failures += 0 if ok else 1

    repo_root = Path(args.repo_root)
    repo_result = validate_repository(repo_root)
    print(f"{'PASS' if repo_result.valid else 'FAIL'} repository-status-sync errors={list(repo_result.errors)}")
    failures += 0 if repo_result.valid else 1

    artifact_result = validate_artifact_governance(repo_root)
    print(f"{'PASS' if artifact_result.valid else 'FAIL'} artifact-governance errors={list(artifact_result.errors)}")
    failures += 0 if artifact_result.valid else 1

    promotion_gate_result = validate_foundation_promotion_gate(repo_root)
    print(
        f"{'PASS' if promotion_gate_result.valid else 'FAIL'} "
        f"foundation-promotion-gate errors={list(promotion_gate_result.errors)}"
    )
    failures += 0 if promotion_gate_result.valid else 1

    reassessment_result = validate_foundation_promotion_reassessment(repo_root)
    print(
        f"{'PASS' if reassessment_result.valid else 'FAIL'} "
        f"foundation-promotion-reassessment errors={list(reassessment_result.errors)}"
    )
    failures += 0 if reassessment_result.valid else 1

    event_surface_result = validate_event_stable_surface(repo_root)
    print(
        f"{'PASS' if event_surface_result.valid else 'FAIL'} "
        f"event-stable-surface errors={list(event_surface_result.errors)}"
    )
    failures += 0 if event_surface_result.valid else 1

    assignment_surface_result = validate_assignment_stable_surface(repo_root)
    print(
        f"{'PASS' if assignment_surface_result.valid else 'FAIL'} "
        f"assignment-stable-surface errors={list(assignment_surface_result.errors)}"
    )
    failures += 0 if assignment_surface_result.valid else 1

    constraint_surface_result = validate_constraint_stable_surface(repo_root)
    print(
        f"{'PASS' if constraint_surface_result.valid else 'FAIL'} "
        f"constraint-stable-surface errors={list(constraint_surface_result.errors)}"
    )
    failures += 0 if constraint_surface_result.valid else 1

    constraint_q6_result = validate_constraint_q6_sufficiency(repo_root)
    print(
        f"{'PASS' if constraint_q6_result.valid else 'FAIL'} "
        f"constraint-q6-sufficiency errors={list(constraint_q6_result.errors)}"
    )
    failures += 0 if constraint_q6_result.valid else 1

    constraint_status_result = validate_constraint_document_status_readiness(repo_root)
    print(
        f"{'PASS' if constraint_status_result.valid else 'FAIL'} "
        f"constraint-document-status-readiness errors={list(constraint_status_result.errors)}"
    )
    failures += 0 if constraint_status_result.valid else 1

    assignment_amendment_result = validate_assignment_amendment_q2(repo_root)
    print(
        f"{'PASS' if assignment_amendment_result.valid else 'FAIL'} "
        f"assignment-amendment-q2 errors={list(assignment_amendment_result.errors)}"
    )
    failures += 0 if assignment_amendment_result.valid else 1

    assignment_temporal_scope_result = validate_assignment_temporal_scope(repo_root)
    print(
        f"{'PASS' if assignment_temporal_scope_result.valid else 'FAIL'} "
        f"assignment-temporal-scope errors={list(assignment_temporal_scope_result.errors)}"
    )
    failures += 0 if assignment_temporal_scope_result.valid else 1

    assignment_compatibility_result = validate_assignment_consumer_compatibility(repo_root)
    print(
        f"{'PASS' if assignment_compatibility_result.valid else 'FAIL'} "
        f"assignment-consumer-compatibility errors={list(assignment_compatibility_result.errors)}"
    )
    failures += 0 if assignment_compatibility_result.valid else 1

    assignment_pressure_result = validate_assignment_consumer_pressure(repo_root)
    print(
        f"{'PASS' if assignment_pressure_result.valid else 'FAIL'} "
        f"assignment-consumer-pressure errors={list(assignment_pressure_result.errors)}"
    )
    failures += 0 if assignment_pressure_result.valid else 1

    assignment_norm_result = validate_assignment_norm_compatibility(repo_root)
    print(
        f"{'PASS' if assignment_norm_result.valid else 'FAIL'} "
        f"assignment-norm-compatibility errors={list(assignment_norm_result.errors)}"
    )
    failures += 0 if assignment_norm_result.valid else 1

    assignment_q3_result = validate_assignment_q3_lifecycle(repo_root)
    print(
        f"{'PASS' if assignment_q3_result.valid else 'FAIL'} "
        f"assignment-q3-lifecycle errors={list(assignment_q3_result.errors)}"
    )
    failures += 0 if assignment_q3_result.valid else 1

    assignment_q2_sufficiency_result = validate_assignment_q2_sufficiency(repo_root)
    print(
        f"{'PASS' if assignment_q2_sufficiency_result.valid else 'FAIL'} "
        f"assignment-q2-sufficiency errors={list(assignment_q2_sufficiency_result.errors)}"
    )
    failures += 0 if assignment_q2_sufficiency_result.valid else 1

    assignment_q9_result = validate_assignment_q9_sufficiency(repo_root)
    print(
        f"{'PASS' if assignment_q9_result.valid else 'FAIL'} "
        f"assignment-q9-sufficiency errors={list(assignment_q9_result.errors)}"
    )
    failures += 0 if assignment_q9_result.valid else 1

    consumer_need_result = validate_consumer_need_discovery(repo_root)
    print(
        f"{'PASS' if consumer_need_result.valid else 'FAIL'} "
        f"consumer-need-discovery errors={list(consumer_need_result.errors)}"
    )
    failures += 0 if consumer_need_result.valid else 1

    ocp024_acceptance_result = validate_ocp024_acceptance(repo_root)
    print(
        f"{'PASS' if ocp024_acceptance_result.valid else 'FAIL'} "
        f"ocp024-acceptance errors={list(ocp024_acceptance_result.errors)}"
    )
    failures += 0 if ocp024_acceptance_result.valid else 1

    event_selection_result = validate_event_promotion_selection(repo_root)
    print(
        f"{'PASS' if event_selection_result.valid else 'FAIL'} "
        f"event-promotion-selection errors={list(event_selection_result.errors)}"
    )
    failures += 0 if event_selection_result.valid else 1

    event_promotion_result = validate_event_lifecycle_promotion(repo_root)
    print(
        f"{'PASS' if event_promotion_result.valid else 'FAIL'} "
        f"event-lifecycle-promotion errors={list(event_promotion_result.errors)}"
    )
    failures += 0 if event_promotion_result.valid else 1

    event_concept_result = validate_event_concept_canonicalization(repo_root)
    print(
        f"{'PASS' if event_concept_result.valid else 'FAIL'} "
        f"event-concept-canonicalization errors={list(event_concept_result.errors)}"
    )
    failures += 0 if event_concept_result.valid else 1

    question_sync_result = validate_open_question_sync(repo_root)
    print(
        f"{'PASS' if question_sync_result.valid else 'FAIL'} "
        f"open-question-resolution-sync errors={list(question_sync_result.errors)}"
    )
    failures += 0 if question_sync_result.valid else 1

    snapshot_result = validate_accepted_snapshots(repo_root)
    print(
        f"{'PASS' if snapshot_result.valid else 'FAIL'} "
        f"accepted-snapshot-governance errors={list(snapshot_result.errors)}"
    )
    failures += 0 if snapshot_result.valid else 1

    accounting_result = validate_current_numeric_accounting(repo_root)
    print(
        f"{'PASS' if accounting_result.valid else 'FAIL'} "
        f"current-numeric-accounting errors={list(accounting_result.errors)}"
    )
    failures += 0 if accounting_result.valid else 1

    process_result = validate_process_audit(repo_root, context=context)
    print(f"{'PASS' if process_result.valid else 'FAIL'} process-audit context={context} errors={list(process_result.errors)}")
    failures += 0 if process_result.valid else 1

    graph_result = validate_and_render_concept_graph(repo_root, context=context)
    print(f"{'PASS' if graph_result.valid else 'FAIL'} concept-graph context={context} errors={list(graph_result.errors)}")
    failures += 0 if graph_result.valid else 1

    generated_path = repo_root / "architecture/baselines/foundation-map.md"
    difference = ""
    try:
        committed = generated_path.read_text(encoding="utf-8")
        map_ok = committed == graph_result.rendered_map
        if not map_ok:
            difference = first_map_difference(committed, graph_result.rendered_map)
    except OSError as exc:
        map_ok = False
        difference = f"{type(exc).__name__}: {exc}"
    suffix = f" first_difference={difference!r}" if difference else ""
    print(f"{'PASS' if map_ok else 'FAIL'} foundation-map-drift{suffix}")
    failures += 0 if map_ok else 1

    print(
        f"Checked {len(files)} fixture(s), repository status, artifact governance, "
        f"foundation promotion gate, reassessment, Event, Assignment and Constraint stable-surface discovery, Constraint Q6 sufficiency and document-status readiness, "
        f"Assignment amendment-Q2 and temporal/partial-scope attempts, Accepted-consumer compatibility, pressure, norm compatibility, Q3 lifecycle and Q2/Q9 sufficiency, "
        f"consumer-need discovery, OCP-024 acceptance, "
        f"Event selection, lifecycle promotion and Concept canonicalization, "
        f"open-question resolution sync, accepted snapshot governance, current numeric accounting, process audit, "
        f"Concept graph and generated map; "
        f"failures={failures}"
    )
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
