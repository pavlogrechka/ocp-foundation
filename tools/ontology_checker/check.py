#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from ocp_checker import load_fixture, validate_fixture


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate OCP reference YAML fixtures.")
    parser.add_argument("path", nargs="?", default=str(Path(__file__).with_name("fixtures")))
    args = parser.parse_args()

    root = Path(args.path)
    files = sorted(root.rglob("*.yaml")) if root.is_dir() else [root]
    failures = 0
    for path in files:
        fixture = load_fixture(path)
        result = validate_fixture(fixture)
        expected = fixture.get("expected", {})
        expected_valid = bool(expected.get("valid"))
        expected_codes = set(expected.get("error_codes", []))
        actual_codes = set(result.errors)
        ok = result.valid == expected_valid and expected_codes.issubset(actual_codes)
        print(f"{'PASS' if ok else 'FAIL'} {fixture.get('case_id', path.name)} valid={result.valid} errors={list(result.errors)}")
        failures += 0 if ok else 1

    print(f"Checked {len(files)} fixture(s); failures={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
