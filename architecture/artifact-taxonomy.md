# OCP Foundation Artifact Taxonomy

This document explains the machine-readable taxonomy in `architecture/artifact-taxonomy.yaml`.

## Governing rule

Artifact prefix does not by itself determine authority. Each class has an explicit normative level, lifecycle, numbering authority, repository location and review lane.

## Normative levels

- `binding` — directly governs dependent artifacts.
- `binding-when-invoked` — optional to adopt, but binding for an artifact that declares the invocation in metadata.
- `advisory` — implementation or guidance that does not redefine normative semantics.
- `record` — evidence, status accounting or backlog history.

## OCP dual status axes

An OCP specification carries two independent status axes when it defines a Concept:

- `Document Status` describes the maturity of the document artifact;
- `Concept Status` describes the maturity of the Concept defined by that document.

The machine-readable taxonomy therefore declares separate `document_lifecycle` and `concept_lifecycle` fields for the OCP class. A checker must not collapse these into one status value.

## Decision registries

### AD — active decision class

All new architecture decisions and discovery cycles use `AD-NNN` under `architecture/discovery/`.

AD resolves architecture choices that govern one or more future artifacts. Binding AD artifacts require external review before Architecture Board acceptance.

### ADR — historical registry

The `adr/` registry is frozen for new identifiers. Existing ADR artifacts remain binding according to their status, and `ADR-DRAFT-007` completes its existing lifecycle there. New decisions are not split between AD and ADR.

### AB — Board accounting record

AB entries track questions, planned actions and Board resolutions. They are records, not independent normative definitions. A resolved AB entry points to the artifact that defines the decision.

For accepted AD decision-accounting checks, the machine-readable `AB.active_states` set is authoritative:

```yaml
active_states: [Open, Proposed, Discovery, Under Review]
```

An accepted AD may not leave an explicitly referenced AB entry in one of those active states. `Deferred`, `Planned`, `Resolved` and `Rejected` remain lifecycle values but are not classified as active for this synchronization rule.

## Patterns

Patterns live under `patterns/` and are `binding-when-invoked`.

An artifact invokes a pattern using frontmatter such as:

```yaml
Uses-Patterns: P-001@0.1.0
```

Invocation means that the artifact must satisfy every Required Element and every obligation of the optional modules it selects. Domain semantics remain in the invoking artifact.

Pattern versions use semantic-version syntax. Invocation follows the machine-readable `track-current` policy: every `Uses-Patterns` value must equal the current version declared by the referenced Pattern. A PR that changes a Pattern version must atomically update every invoker and route each affected normative artifact through its required review lane.

This policy prevents silent semantic drift between a Pattern and accepted invokers. Historical pinning is not claimed by the current repository model because historical Pattern versions are not materialized as separately resolvable artifacts.

## Review records

Review artifacts are records rather than normative definitions. Their lifecycle is `Draft → Final`, but a dedicated status field is optional for existing review files. When absent, the committed review record is interpreted as `Final` unless the file explicitly states that it is provisional.

This compatibility rule avoids retroactively invalidating the existing review archive while still giving future tooling a defined lifecycle.

## Review lane

Artifacts whose taxonomy class is `binding` or `binding-when-invoked` require:

1. a dedicated branch and draft pull request;
2. external adversarial review before Board acceptance;
3. explicit Architecture Board resolution;
4. squash merge after required checks pass.

Review records, backlog bookkeeping and status-only changes dictated by an already accepted lifecycle do not recursively require review of the review itself.

## Enforcement boundary

Repository tooling validates metadata, references, declared Pattern versions and committed evidence. GitHub Rulesets or branch protection are the preventive authority for squash-only merge and required checks.

The post-factum process audit requires complete Git history and inspects every merge commit reachable from `HEAD`. A shallow repository is an audit failure, not a successful result. Pull-request merge refs are not audited as repository history because the process audit is enabled only in `main` context.
