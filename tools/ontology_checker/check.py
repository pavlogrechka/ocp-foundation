#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from ocp_checker import load_fixture, validate_fixture, validate_repository


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate OCP reference YAML fixtures.")
    parser.add_argument("path", nargs="?", default=str(Path(__file__).with_name("fixtures")))
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[2]),
        help="Repository root used for cross-document status checks.",
    )
    args = parser.parse_args()

    root = Path(args.path)
    files = sorted(root.rglob("*.yaml")) if root.is_dir() else [root]
    failures = 0

    for path in files:
        try:
            fixture = load_fixture(path)
            result = validate_fixture(fixture)
            expected = fixture.get("expected", {})
            expected_valid = bool(expected.get("valid"))
            expected_codes = set(expected.get("error_codes", []))
            actual_codes = set(result.errors)
            ok = result.valid == expected_valid and expected_codes == actual_codes
            case_id = fixture.get("case_id", path.name)
            print(
                f"{'PASS' if ok else 'FAIL'} {case_id} "
                f"valid={result.valid} errors={list(result.errors)}"
            )
        except (OSError, ValueError, yaml.YAMLError) as exc:
            ok = False
            print(f"FAIL {path}: {type(exc).__name__}: {exc}")
        failures += 0 if ok else 1

    repo_result = validate_repository(Path(args.repo_root))
    repo_ok = repo_result.valid
    print(
        f"{'PASS' if repo_ok else 'FAIL'} repository-status-sync "
        f"errors={list(repo_result.errors)}"
    )
    failures += 0 if repo_ok else 1

    print(f"Checked {len(files)} fixture(s) and repository status sync; failures={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
