#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from ocp_checker import load_fixture, validate_fixture, validate_repository
from ocp_checker.organization import validate_organization, validate_organization_relationship


def validate_any_fixture(fixture: dict):
    concept = fixture.get("concept")
    entity = fixture.get("entity") or {}
    if concept == "Organization":
        return validate_organization(entity)
    if concept == "OrganizationRelationshipRecord":
        return validate_organization_relationship(entity)
    return validate_fixture(fixture)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate OCP reference YAML fixtures.")
    parser.add_argument("path", nargs="?", default=str(Path(__file__).with_name("fixtures")))
    parser.add_argument("--repo-root", default=str(Path(__file__).resolve().parents[2]))
    args = parser.parse_args()

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

    repo_result = validate_repository(Path(args.repo_root))
    print(f"{'PASS' if repo_result.valid else 'FAIL'} repository-status-sync errors={list(repo_result.errors)}")
    failures += 0 if repo_result.valid else 1
    print(f"Checked {len(files)} fixture(s) and repository status sync; failures={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
