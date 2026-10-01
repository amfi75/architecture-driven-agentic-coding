# Start in a new repository

Use [setup](../SETUP.md) for revision selection and project records, then apply the [core](../releases/2.4.0-dev.3/core.md).

1. Understand users, intended use, functional and quality requirements, constraints, non-goals and observable acceptance. Resolve material requirements ambiguity before choosing components.
2. Assess ADAC suitability. For selected work, establish `AGENTS.md` and the architecture/delivery records. Mark initial requirements as proposed until the required approval is recorded.
3. Identify capabilities and relationships; investigate consequential uncertainty. Derive component boundaries from behavior, quality, constraints, hidden decisions and manageable dependencies. Record the functional/software mapping and rationale.
4. Define affected interfaces and common revisions. Resolve shared decisions before dependent implementation while leaving unrelated details open. Consider reusable solutions and dependencies.
5. Assign component owners and integration responsibility. Owners handle required research/design and derive bounded worker tasks when delegation is useful and authorized. Include purpose, requirements, scope, interfaces, readiness, checks and reporting routes.
6. Plan concurrent contributions and necessary sequencing. The orchestrator covers cross-cutting requirements; owners retain accountability through integration.
7. For substantial work, independently review the complete plan, remediate blocking/high findings and obtain initial approval. Preserve its exact requirements baseline separately from changing progress.

Then use the shared delivery/correction loop and maintain records as evidence develops. Establishing the initial architecture does not freeze every future detail or impose separate approvals for internal refinement.
