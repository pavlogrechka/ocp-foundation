from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Iterable

from .checker import ValidationResult


def result(errors: Iterable[str]) -> ValidationResult:
    return ValidationResult(tuple(dict.fromkeys(errors)))


def nonempty(value: Any) -> bool:
    return value is not None and bool(str(value).strip())


def parse_time(value: Any) -> datetime | None:
    if isinstance(value, datetime):
        parsed = value
    elif isinstance(value, str) and value.strip():
        try:
            parsed = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
        except ValueError:
            return None
    else:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def signature(history: list[dict[str, Any]]) -> tuple[tuple[str, str], ...]:
    return tuple((str(item.get("from_stage")), str(item.get("to_stage"))) for item in history)


def transition(history: list[dict[str, Any]], source: str, target: str) -> dict[str, Any] | None:
    matches = [item for item in history if item.get("from_stage") == source and item.get("to_stage") == target]
    return matches[0] if len(matches) == 1 else None


def times_non_decreasing(history: list[dict[str, Any]]) -> bool:
    times = [parse_time(item.get("occurred_at")) for item in history]
    return all(item is not None for item in times) and all(a <= b for a, b in zip(times, times[1:]))


def projection_mismatches(entity: dict[str, Any], projection: dict[str, Any], prefix: str) -> list[str]:
    return [
        f"{prefix}_{field.upper()}_MISMATCH"
        for field, expected in projection.items()
        if field in entity and entity[field] != expected
    ]
