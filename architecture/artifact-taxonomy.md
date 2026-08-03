# OCP Foundation Artifact Taxonomy

This document explains the machine-readable taxonomy in `architecture/artifact-taxonomy.yaml`.

## Governing rule

Artifact prefix does not by itself determine authority. Each class has an explicit normative level, lifecycle, numbering authority, repository location and review lane.

## Normative levels

- `binding` — directly governs dependent artifacts.
- `binding-when-invoked` — optional to adopt, but binding for an artifact that declares the invocation in metadata.
- `advisory` — implementation or guidance that does not redefine normative semantics.
- `record` — evidence, status accounting or backlog history.

## Decision registries

### AD — active decision class

All new architecture decisions and discovery cycles use `AD-NNN` under `architecture/discovery/`.

AD resolves architecture choices that govern one or more future artifacts. Binding AD artifacts require external review before Architecture Board acceptance.

### ADR — historical registry

The `adr/` registry is frozen for new identifiers. Existing ADR artifacts remain binding according to their status, and `ADR-DRAFT-007` completes its existing lifecycle there. New decisions are not split between AD and ADR.

### AB — Board accounting record

AB entries track questions, planned actions and Board resolutions. They are records, not independent normative definitions. A resolved AB entry points to the artifact that defines the decision.

## Patterns

Patterns live under `patterns/` and are `binding-when-invoked`.

An artifact invokes a pattern using frontmatter such as:

```yaml
Uses-Patterns: P-001@0.1.0
```

Invocation means that the artifact must satisfy every Required Element and every obligation of the optional modules it selects. Domain semantics remain in the invoking artifact.

Pattern changes require versioning and the same external-review lane as other normative artifacts because they may affect every invoker.

## Review lane

Artifacts whose taxonomy class is `binding` or `binding-when-invoked` require:

1. a dedicated branch and draft pull request;
2. external adversarial review before Board acceptance;
3. explicit Architecture Board resolution;
4. squash merge after required checks pass.

Review records, backlog bookkeeping and status-only changes dictated by an already accepted lifecycle do not recursively require review of the review itself.

## Enforcement boundary

Repository tooling can validate metadata, references, declared pattern versions and committed evidence. It can audit merge history after the fact. GitHub Rulesets or branch protection are the preventive authority for squash-only merge and required checks.
