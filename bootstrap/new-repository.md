# Start in a new repository

1. Understand users, intended outcome, functional needs, quality goals, constraints, non-goals and observable acceptance. Record these overall requirements before choosing an architecture.
2. Assess whether meaningful modular responsibilities and interfaces justify ADAC. A small inseparable task needs ordinary proportionate work, not artificial layers.
3. Identify needed capabilities and their relationships; investigate consequential uncertainty. Derive a simple initial component/dependency map from behavior, quality and constraints. Explain the responsibilities and changeable decisions each component hides. A modular monolith is often sufficient; no deployment topology is prescribed.
4. Define affected interfaces, their providers/consumers, data, semantics, errors, invariants and compatibility. Resolve common decisions needed for dependent implementation, leaving unrelated details open.
5. Evaluate reuse and dependencies. Derive worker packages with purpose, behavior, quality, constraints, design discretion, scope, interface revision, readiness, acceptance and reporting. Assign research and design ownership for complex components; plan intended-use evidence. Assign integration and cross-cutting outcomes to the orchestrator.
6. Plan which contributions can proceed concurrently and which require sequencing. Avoid overlapping edits or competing contract revisions.
7. Independently review the complete plan for substantial work, repair blocking/high gaps and obtain the user's initial approval. Preserve the requirement revision and distinguish it from revisable design decisions.

This preparation may fit in a few concise records. Templates and archetypes are optional aids, not required scaffolding. Preparation alone is not approval to implement product behavior. After approval, follow the [autonomous operating model](../method/operating-model.md), including internal change requests and final independent review.
