---
Decision-ID: AD-050
Title: Constraint Bounded Stable-Surface Discovery
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: AD-025, AD-026, AD-027, OCP-001, OCP-005, OCP-006, OCP-016
Applies-To: Constraint bounded stable-surface discovery
Review-After: Separately mandated Constraint lifecycle act; this discovery creates no selection, freeze, promotion cycle or question-resolution authority
---

# AD-050 — Constraint Bounded Stable-Surface Discovery

## 1. Result and authority boundary

The full current OCP-006 question inventory contains twelve numbered entries: eight open and four resolved. Applying one predeclared criterion produces five bounded stable candidates, eight moving surfaces and exactly one whole-document blocker, `EVALUATION_CURRENTNESS_UNRESOLVED`, bound to Q6. Q2, Q7, Q11 and Q12 are local after a bounded freeze; Q1, Q8 and Q10 are outside that bounded surface under current negative owner boundaries. Q3/Q4/Q5/Q9 are resolved by AD-027/AD-027/AD-025/AD-026 and are excluded from the open set.

This is discovery, not a freeze or lifecycle decision. It does not edit OCP-006, close a question, select Constraint, establish readiness, start a promotion cycle, change OCP-005 or its blockers, create a Concept or alter the registry, taxonomy or graph. Even if the bounded surface later proves acceptable, transition authority requires a separate mandate.

## 2. Gate-first result

Before choosing the AD plus machine-readable witness form, the result was tested against OCP-016 G4. A question-classification evidence map and drift validator do not create a positive-capable rule, result or profile and perform no activation. G4 therefore does not apply to this act. The bounded candidate cannot approve or activate itself.

## 3. Criterion fixed before application

AD-050 reuses the current AD-035 vocabulary rather than inventing a Constraint-specific one:

- `blocks-whole-document-freeze`: every permitted answer can change a declared property inside the named bounded kernel;
- `local-after-bounded-freeze`: a named kernel remains invariant under every permitted answer, while the answer is confined to a named moving surface;
- `outside-bounded-surface`: an existing owner/non-authority boundary keeps the question outside the kernel; and
- `outside-open-set`: a resolved numbered entry, retained historically but excluded from the current open inventory.

If none applies, the checker requires a vocabulary-gap report before an extension. Classification reasoning is explicitly `analytical`; the source tokens, question state and closed-question acts are observational and executable.

## 4. Complete question enumeration

| Q | State | Classification | Operational reason |
|---|---|---|---|
| Q1 Conflict object/aggregation | open | outside-bounded-surface | §13 already freezes violation as not automatically Conflict; a future Conflict owner can change without moving that boundary |
| Q2 expression language | open | local-after-bounded-freeze | versioned predicate/input binding is fixed while execution syntax remains technology-local |
| Q3 precedence/override/exception | resolved by AD-027 | outside-open-set | current negative application-order/override boundary |
| Q4 contextual waiver | resolved by AD-027 | outside-open-set | current negative waiver boundary |
| Q5 quantity/unit/demand/capacity inputs | resolved by AD-025 | outside-open-set | exact input contract selected; positive capacity remains gated |
| Q6 dynamic-input evaluation currentness | open | blocks-whole-document-freeze | without the expiry/currentness rule, the same record may or may not feed effective result and admissibility |
| Q7 stored versus reproducible blocking evaluations | open | local-after-bounded-freeze | §11 already admits either carrier under the same exact version/context/snapshot result binding |
| Q8 Operation authorization | open | outside-bounded-surface | §§12/14.5 freeze the non-authorization boundary; another owner may define authorization |
| Q9 Reservation object form | resolved by AD-026 | outside-open-set | current negative establishment boundary |
| Q10 Readiness/availability handoff | open | outside-bounded-surface | §17.10 already denies derivation from one violation without a separate accepted rule |
| Q11 Constraint-kind taxonomy | open | local-after-bounded-freeze | §14 labels patterns non-canonical; predicate/enforcement semantics do not require a kind taxonomy |
| Q12 domain relation expression | open | local-after-bounded-freeze | opaque target scope plus versioned predicate/input binding can freeze while domain relation language remains external |

The “all open questions block” outcome was tested independently: it fails because Q2/Q7/Q11/Q12 each have a named invariant kernel, while Q1/Q8/Q10 have already-declared owner boundaries. The “none block” outcome also fails: Q6 directly controls whether an evaluation is current enough to participate in the document's own effective-result/admissibility derivation.

## 5. Bounded candidate and moving work

The candidate surface is limited to:

1. Constraint identity, semantic-change/new-identity and explicit supersession boundaries;
2. minimum structure, transition-history lifecycle and prospective temporal effectivity;
3. evaluation context/applicability/result/admissibility shape, excluding unresolved dynamic-input currentness;
4. fail-safe non-satisfaction plus non-authorization/non-Conflict boundaries; and
5. target-scope non-inheritance and explicit, traceable propagation.

Moving work remains expression language, evaluation currentness, storage/reproduction policy, kind taxonomy, domain relation language and three external-owner handoffs. Only currentness blocks a whole-document freeze. This finding neither establishes freeze readiness nor remedies OCP-006's Draft OCP-005 dependency floor.

## 6. Executable evidence

`architecture/constraint-stable-surface.yaml` records the exact question text/state, classification basis, invariant/moving surfaces, closure acts, stable candidates, one blocker and forbidden outcomes. `constraint_stable_surface.py` re-enumerates the numbered OCP-006 section, verifies strikeout state, closure-act status/tokens, every evidence token, exact subject metadata and unchanged promotion-gate guard.

Mutation tests separately fail when the body/open inventory diverges and when a classification changes without its basis changing. Every exported defensive vocabulary value and every scalar in the expected question/evidence projections is removed or mutated individually. No fixture is added or changed.

## 7. Version, migration and rollback

AD-050 begins at `0.1.0 / Discovery`: it introduces a new evidence artifact, not Constraint semantics. The witness begins at schema 1 because it introduces a new evidence language; checker support has no OCP SemVer. OCP-006 remains byte-identical at `0.3.2 / Draft`, so no document migration exists.

Rollback is atomic removal of AD-050, its witness, checker module/tests and current README/roadmap/checker-guide projections. Partial rollback is invalid because prose without executable question/classification binding would overstate evidence. Historical objects and every `baseline_*` witness remain byte-identical.
