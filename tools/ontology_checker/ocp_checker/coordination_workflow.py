from __future__ import annotations

from typing import Any, Iterable

from ._common import nonempty, parse_time, result
from .checker import ValidationResult


COORDINATION_WORKFLOW_ERROR_CODES = frozenset(
    {
        "COORDINATION_PROPOSAL_INVALID",
        "COORDINATION_RESPONSE_INVALID",
        "COORDINATION_RECORD_DUPLICATE",
        "COORDINATION_REFERENCE_UNRESOLVED",
        "COORDINATION_RESPONDER_OUT_OF_SCOPE",
        "COORDINATION_SUPERSESSION_INVALID",
        "COORDINATION_FORBIDDEN_COUPLING",
        "COORDINATION_FIXTURE_INVALID",
    }
)

COORDINATION_WORKFLOW_DERIVATION_RULES = frozenset(
    {"derive_coordination_evidence"}
)

RULE_REF = "coordination-evidence@1"
PROPOSAL_KIND = "coordination-proposal@1"
RESPONSE_KIND = "coordination-response@1"
RESPONSE_KINDS = frozenset({"confirm", "decline", "withdraw"})
PROPOSAL_DISPOSITIONS = frozenset({"open", "withdrawn"})
OUTCOMES = frozenset({"positive", "negative", "withdrawal", "indeterminate"})
FORBIDDEN_COUPLING_KEYS = frozenset(
    {
        "authorization",
        "authorized",
        "approval",
        "selected",
        "selection",
        "reservation",
        "allocation",
        "assignment_mutation",
        "new_assignment",
        "permission",
    }
)


def _text(value: Any) -> str | None:
    return str(value).strip() if nonempty(value) else None


def _string_list(value: Any) -> list[str] | None:
    if not isinstance(value, list) or not value:
        return None
    values = [_text(item) for item in value]
    if any(item is None for item in values) or len(values) != len(set(values)):
        return None
    return [item for item in values if item is not None]


def _interval_valid(record: dict[str, Any]) -> bool:
    start = parse_time(record.get("effective_from"))
    end = parse_time(record.get("effective_until"))
    return start is not None and (end is None or start < end)


def _forbidden(record: dict[str, Any]) -> bool:
    return any(
        key in record and record.get(key) not in (None, False, "", [], {})
        for key in FORBIDDEN_COUPLING_KEYS
    )


def _proposal_payload(record: dict[str, Any]) -> tuple[Any, ...]:
    return (
        _text(record.get("context_ref")),
        tuple(sorted(record.get("invited_responder_refs") or [])),
        tuple(sorted(record.get("requirement_refs") or [])),
        tuple(sorted(record.get("visible_to_refs") or [])),
    )


def validate_coordination_proposal(record: dict[str, Any]) -> ValidationResult:
    invited = _string_list(record.get("invited_responder_refs"))
    visible = _string_list(record.get("visible_to_refs"))
    requirements = _string_list(record.get("requirement_refs"))
    errors: list[str] = []
    if (
        record.get("record_kind") != PROPOSAL_KIND
        or any(
            _text(record.get(field)) is None
            for field in (
                "proposal_record_id",
                "proposal_id",
                "revision",
                "publisher_ref",
                "context_ref",
                "provenance_ref",
            )
        )
        or invited is None
        or visible is None
        or requirements is None
        or not set(invited).issubset(visible)
        or record.get("disposition") not in PROPOSAL_DISPOSITIONS
        or not _interval_valid(record)
    ):
        errors.append("COORDINATION_PROPOSAL_INVALID")
    if _forbidden(record):
        errors.append("COORDINATION_FORBIDDEN_COUPLING")
    return result(errors)


def validate_coordination_response(record: dict[str, Any]) -> ValidationResult:
    errors: list[str] = []
    if (
        record.get("record_kind") != RESPONSE_KIND
        or any(
            _text(record.get(field)) is None
            for field in (
                "response_record_id",
                "proposal_ref",
                "responder_ref",
                "provenance_ref",
            )
        )
        or record.get("response_kind") not in RESPONSE_KINDS
        or not _interval_valid(record)
        or (record.get("response_kind") == "withdraw" and _text(record.get("supersedes_ref")) is None)
    ):
        errors.append("COORDINATION_RESPONSE_INVALID")
    if _forbidden(record):
        errors.append("COORDINATION_FORBIDDEN_COUPLING")
    return result(errors)


def _validate_lineage(
    records: list[dict[str, Any]], id_field: str, identity_fields: tuple[str, ...]
) -> list[str]:
    records = [item for item in records if isinstance(item, dict)]
    errors: list[str] = []
    index = {_text(item.get(id_field)): item for item in records}
    successors: dict[str, int] = {}
    for record in records:
        record_id = _text(record.get(id_field))
        parent_id = _text(record.get("supersedes_ref"))
        if parent_id is None:
            continue
        parent = index.get(parent_id)
        if (
            record_id is None
            or parent is None
            or parent_id == record_id
            or any(_text(parent.get(field)) != _text(record.get(field)) for field in identity_fields)
        ):
            errors.append("COORDINATION_SUPERSESSION_INVALID")
            continue
        successors[parent_id] = successors.get(parent_id, 0) + 1
    if any(count > 1 for count in successors.values()):
        errors.append("COORDINATION_SUPERSESSION_INVALID")

    for record in records:
        seen: set[str] = set()
        current = _text(record.get(id_field))
        while current is not None and current in index:
            if current in seen:
                errors.append("COORDINATION_SUPERSESSION_INVALID")
                break
            seen.add(current)
            current = _text(index[current].get("supersedes_ref"))
    return errors


def validate_coordination_workflow_dataset(
    proposals: Iterable[dict[str, Any]], responses: Iterable[dict[str, Any]]
) -> ValidationResult:
    proposal_entries = list(proposals)
    response_entries = list(responses)
    errors: list[str] = []
    for record in proposal_entries:
        if not isinstance(record, dict):
            errors.append("COORDINATION_PROPOSAL_INVALID")
        else:
            errors.extend(validate_coordination_proposal(record).errors)
    for record in response_entries:
        if not isinstance(record, dict):
            errors.append("COORDINATION_RESPONSE_INVALID")
        else:
            errors.extend(validate_coordination_response(record).errors)

    proposal_ids = [_text(item.get("proposal_record_id")) for item in proposal_entries if isinstance(item, dict)]
    response_ids = [_text(item.get("response_record_id")) for item in response_entries if isinstance(item, dict)]
    if len(proposal_ids) != len(set(proposal_ids)) or len(response_ids) != len(set(response_ids)):
        errors.append("COORDINATION_RECORD_DUPLICATE")

    proposal_index = {
        _text(item.get("proposal_record_id")): item
        for item in proposal_entries
        if isinstance(item, dict) and _text(item.get("proposal_record_id")) is not None
    }
    for proposal in proposal_entries:
        if not isinstance(proposal, dict) or proposal.get("disposition") != "withdrawn":
            continue
        parent = proposal_index.get(_text(proposal.get("supersedes_ref")))
        if parent is None or _proposal_payload(proposal) != _proposal_payload(parent):
            errors.append("COORDINATION_SUPERSESSION_INVALID")
    for response in response_entries:
        if not isinstance(response, dict):
            continue
        proposal = proposal_index.get(_text(response.get("proposal_ref")))
        if proposal is None:
            errors.append("COORDINATION_REFERENCE_UNRESOLVED")
        elif _text(response.get("responder_ref")) not in (proposal.get("invited_responder_refs") or []):
            errors.append("COORDINATION_RESPONDER_OUT_OF_SCOPE")

    errors.extend(
        _validate_lineage(proposal_entries, "proposal_record_id", ("proposal_id", "publisher_ref"))
    )
    errors.extend(
        _validate_lineage(response_entries, "response_record_id", ("proposal_ref", "responder_ref"))
    )
    return result(errors)


def _effective(record: dict[str, Any], at: Any) -> bool:
    moment = parse_time(at)
    start = parse_time(record.get("effective_from"))
    end = parse_time(record.get("effective_until"))
    return bool(moment is not None and start is not None and start <= moment and (end is None or moment < end))


def _heads(records: list[dict[str, Any]], id_field: str, at: Any) -> list[dict[str, Any]]:
    effective = [item for item in records if _effective(item, at)]
    superseded = {
        _text(item.get("supersedes_ref"))
        for item in effective
        if _text(item.get("supersedes_ref")) is not None
    }
    return [item for item in effective if _text(item.get(id_field)) not in superseded]


def derive_coordination_evidence(snapshot: dict[str, Any]) -> str:
    """Derive attributable agreement evidence, never authorization or execution."""
    if not isinstance(snapshot, dict) or snapshot.get("rule_ref") != RULE_REF:
        return "indeterminate"
    if _text(snapshot.get("snapshot_ref")) is None or _forbidden(snapshot):
        return "indeterminate"
    proposals = snapshot.get("proposals")
    responses = snapshot.get("responses")
    if not isinstance(proposals, list) or not isinstance(responses, list):
        return "indeterminate"
    if not validate_coordination_workflow_dataset(proposals, responses).valid:
        return "indeterminate"

    at = snapshot.get("evaluation_time")
    proposal_id = _text(snapshot.get("proposal_id"))
    if proposal_id is None:
        return "indeterminate"
    proposal_heads = _heads(
        [item for item in proposals if _text(item.get("proposal_id")) == proposal_id],
        "proposal_record_id",
        at,
    )
    if len(proposal_heads) != 1:
        return "indeterminate"
    proposal = proposal_heads[0]
    if proposal.get("disposition") == "withdrawn":
        return "withdrawal"

    outcomes: list[str] = []
    for responder in proposal["invited_responder_refs"]:
        candidates = [
            item
            for item in responses
            if item.get("proposal_ref") == proposal.get("proposal_record_id")
            and item.get("responder_ref") == responder
        ]
        heads = _heads(candidates, "response_record_id", at)
        if len(heads) != 1:
            return "indeterminate"
        outcomes.append(heads[0]["response_kind"])

    if outcomes and all(item == "confirm" for item in outcomes):
        return "positive"
    if "decline" in outcomes:
        return "negative"
    if outcomes and all(item == "withdraw" for item in outcomes):
        return "withdrawal"
    return "indeterminate"


def validate_coordination_workflow_fixture(fixture: dict[str, Any]) -> ValidationResult:
    cases = fixture.get("cases")
    if not isinstance(cases, dict) or not cases:
        return result(["COORDINATION_FIXTURE_INVALID"])
    errors: list[str] = []
    for case in cases.values():
        if (
            not isinstance(case, dict)
            or case.get("expected_outcome") not in OUTCOMES
            or not isinstance(case.get("snapshot"), dict)
        ):
            errors.append("COORDINATION_FIXTURE_INVALID")
            continue
        if derive_coordination_evidence(case["snapshot"]) != case["expected_outcome"]:
            errors.append("COORDINATION_FIXTURE_INVALID")
    return result(errors)
