---
Document-ID: OCP-015
Title: Coordination Proposal and Response Record Contract
Version: 0.1.0
Status: Draft
Owner: Architecture Board
Depends-On: OCP-001, OCP-005, OCP-006, OCP-012, OCP-013, OCP-014, AD-009
Used-By: AB-058, Coordination workflows
Uses-Patterns: P-001@0.1.0
Last-Review: 2026-08-05
Review-After: External adversarial review and Architecture Board decision
---

# OCP-015 — Coordination Proposal and Response Record Contract

## 1. Людське пояснення

Цей Draft відповідає на вузьке запитання:

> Як дві незалежні вертикалі можуть зберегти доказ того, що одна опублікувала точну координаційну пропозицію, а інша її підтвердила, відхилила або відкликала свою відповідь — без передачі одна одній authority?

Пропозиція і відповідь є різними records. Автор пропозиції не може записати відповідь іншої вертикалі. Відповідач не може переписати пропозицію. Підтвердження означає лише attributable відповідь на exact revision; воно не є authorization, approval, selection, reservation або Assignment.

Наприклад, vertical `relay-ops` публікує proposal revision `PROP-7-R1`, що посилається на exact OCP-014 requirement. Vertical `airspace` окремо підтверджує цю revision. Якщо proposal змінюється на `PROP-7-R2`, попереднє підтвердження не переноситься автоматично. Якщо `airspace` відкликає відповідь, історичне підтвердження не зникає, але більше не є effective head.

## 2. Proposed mandate implemented by this Draft

OCP-015 реалізує запропонований AD-009A Outcome B:

1. immutable proposal revisions;
2. separate attributable response records;
3. exact participant, context, requirement, time and provenance binding;
4. history-preserving supersession;
5. deterministic fail-safe projection over exact record heads.

Draft не визначає production API, permission system або operational commitment.

## 3. Authority boundary

- Proposal publisher authoritative лише для факту, що він опублікував exact proposal revision із записаним payload і visibility envelope.
- Response issuer authoritative лише для факту, що він підтвердив, відхилив або відкликав власну відповідь щодо exact proposal revision.
- OCP-015 derivation authoritative лише для механічної projection стану evidence snapshot.
- OCP-014, OCP-013, OCP-012 та OCP-006 зберігають власні окремі authorities.

Жоден record або projection не встановлює authorization, approval, consensus, availability, Readiness, capacity, ranking, selection, reservation, allocation, replacement чи Assignment action.

Actor authentication and authorization залишаються зовнішнім contract. Нерозв'язаний actor або provenance не може дати production-authoritative positive projection. Reference fixtures використовують opaque actor references як заздалегідь зв'язані тестові inputs; checker перевіряє їхню наявність та exact equality, але не автентифікує actor.

## 4. P-001 invocation

OCP-015 invokes P-001 `0.1.0` twice. Both invocations select Module A — Temporal Effectivity and Module C — Supersession. Module B is not selected; no mutable lifecycle stage is authoritative.

### 4.1 CoordinationProposalRecord mapping

| P-001 element | OCP-015 mapping |
|---|---|
| Stable record identity | `proposal_record_id` |
| Owning specification | OCP-015 §§5–7 |
| Endpoints | `publisher_ref`, `invited_responder_refs[]`, `context_ref` |
| Governed kind | fixed `coordination-proposal@1` |
| Provenance | `provenance_ref` |
| Authority | exact proposal record and valid supersession graph |
| Module A | `[effective_from, effective_until)` |
| Module C | `supersedes_ref` within one `proposal_id` lineage |

### 4.2 CoordinationResponseRecord mapping

| P-001 element | OCP-015 mapping |
|---|---|
| Stable record identity | `response_record_id` |
| Owning specification | OCP-015 §§8–10 |
| Endpoints | `proposal_ref`, `responder_ref` |
| Governed kind | fixed `coordination-response@1` |
| Provenance | `provenance_ref` |
| Authority | responder-scoped exact response record and valid supersession graph |
| Module A | `[effective_from, effective_until)` |
| Module C | `supersedes_ref` for the same proposal and responder |

## 5. CoordinationProposalRecord

```text
CoordinationProposalRecord
- proposal_record_id
- record_kind: coordination-proposal@1
- proposal_id
- revision
- publisher_ref
- invited_responder_refs[]
- context_ref
- requirement_refs[]
- visible_to_refs[]
- disposition: open | withdrawn
- effective_from
- effective_until [optional]
- supersedes_ref [optional]
- provenance_ref
```

`proposal_record_id` identifies one immutable record. `proposal_id` identifies its lineage. `revision` is descriptive evidence and never selects authority by numeric maximum. A later revision is authoritative only through one valid acyclic `supersedes_ref` chain.

`requirement_refs[]` must use exact OCP-014/OCP-013 references. `visible_to_refs[]` states the publisher's evidence-distribution envelope; it is not a universal visibility policy and grants no permission.

`withdrawn` is a new proposal record that supersedes an open revision. It preserves the earlier record and cannot mutate an Assignment or revoke an external authorization.

## 6. Proposal invariants

1. Identity, kind, lineage, publisher, context, responders, effectivity and provenance are required.
2. Invited responders and visible recipients are exact, non-empty and unique.
3. Every invited responder must be included in the proposal visibility envelope.
4. Exact requirement references are non-empty and unique.
5. A superseding revision keeps `proposal_id` and `publisher_ref` unchanged; a withdrawal also preserves context, invited responders, requirements and visibility of the record it withdraws.
6. Supersession is one-to-one, acyclic and cannot target self.
7. An invalid interval, missing provenance or unresolved endpoint fails closed.
8. Record order, revision number and newest timestamp never choose the head.

## 7. Effective proposal head

At time `t`, `proposal_head(records, proposal_id, t)` returns one effective leaf of a valid supersession chain or no authoritative head. Zero heads, multiple leaves, broken references, cycles or invalid records yield `indeterminate`.

A withdrawn head yields the distinct projection `withdrawal`. It does not erase prior proposal or response evidence.

## 8. CoordinationResponseRecord

```text
CoordinationResponseRecord
- response_record_id
- record_kind: coordination-response@1
- proposal_ref
- responder_ref
- response_kind: confirm | decline | withdraw
- effective_from
- effective_until [optional]
- supersedes_ref [optional]
- provenance_ref
```

`proposal_ref` binds one exact proposal record, not a proposal lineage alias or latest revision. `responder_ref` must be invited by that proposal revision. `withdraw` is valid only when it supersedes the same responder's earlier response to the same proposal revision.

Changing proposal, responder or response author requires a new lineage; it cannot be hidden inside supersession.

## 9. Response invariants

1. Identity, kind, exact proposal, responder, response kind, effectivity and provenance are required.
2. Response kind is governed by the closed vocabulary above.
3. Supersession keeps both `proposal_ref` and `responder_ref` unchanged.
4. One response may supersede at most one earlier response and may itself have at most one valid successor.
5. Conflicting leaf responses for one proposal and responder yield `indeterminate`; timestamp, order and count do not resolve them.
6. A response from a non-invited or non-visible responder is out of scope and fails closed.
7. Confirmation cannot contain authorization, selection, reservation or Assignment directives.

## 10. Coordination evidence projection

```text
derive_coordination_evidence(proposals, responses, proposal_id, evaluation_time)
```

returns:

- `positive` — one effective open proposal head exists and every invited responder has one effective `confirm` head for that exact revision;
- `negative` — one effective open proposal head exists and at least one invited responder has one effective `decline` head, with no ambiguous required response;
- `withdrawal` — the proposal head is withdrawn, or every otherwise-resolvable response state for the open proposal is superseded by its issuer's valid `withdraw` head;
- `indeterminate` — required evidence is missing, stale, conflicting, unresolved, out of scope, cross-revision, malformed or coupled to forbidden authority.

`positive` means only “the required attributable confirmations are present for this exact evidence snapshot.” It is not permission, consensus, selection or commitment. `negative` means only that an attributable decline is present; it is not a prohibition or durable claim about a Resource.

## 11. Replay and change

The projection binds exact proposal and response record ids, evaluation time and rule version `coordination-evidence@1`. A proposal revision, response supersession, expiry or rule version change creates a new evaluation context. Historical projections are not rewritten.

The same exact valid snapshot and rule version must replay the same result regardless of record order.

## 12. Executable evidence

The reference fixture covers:

1. two invited verticals confirming one exact proposal (`positive`);
2. one attributable decline (`negative`);
3. missing, stale, conflicting and cross-revision responses (`indeterminate`);
4. proposal withdrawal and response withdrawal (`withdrawal`);
5. proposal revision without silent confirmation carry-forward;
6. visibility without permission;
7. confirmation without authorization, selection or Assignment mutation;
8. record-order independence and exact replay.

Executable evidence implements this contract but is not its normative owner or a production authority.

## 13. Explicit evidence gap

Core does not yet define actor authentication, delegation, signature validation or a universal vertical identity type. OCP-015 therefore requires exact governed actor and provenance references from a separately accepted profile before production use. The reference checker can reject missing or mismatched references, but cannot prove that an opaque reference resolves to an authenticated actor. Implementations may not infer authority from labels, Organization names, caller identity or service accounts.

## 14. Explicitly not defined

OCP-015 does not define negotiation, consensus, arbitration, conflict resolution, permission, universal visibility, command, approval, availability, Readiness, capacity, ranking, selection, reservation, allocation, replacement, Assignment amendment, notification delivery, UI, transport, production storage, a new fundamental Concept or a Concept graph edge.

## 15. External review questions

Fable should try to falsify whether:

1. proposal and response records truly preserve independent authority;
2. the P-001 invocations are complete rather than partial;
3. visibility remains evidence distribution rather than permission;
4. positive and negative projections stay narrow and non-authorizing;
5. withdrawal preserves history and cannot rewrite another actor's record;
6. conflicts and cross-revision responses fail closed without timestamp, order or count authority;
7. the actor-identity gap is explicit enough to prevent a false production-positive path;
8. rejected alternatives received outcome-fair evidence obligations; and
9. the conceptual contract remains understandable without checker code.

## 16. Draft status

Revision `0.1.0` is a Draft for external adversarial review. It creates no production workflow authority. Acceptance requires exact-head Fable approval, Codex adjudication, green CI and separate explicit Pavlo/Architecture Board authorization before squash merge.
