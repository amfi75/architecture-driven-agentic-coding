# Controlled parallel work

Parallelism is an explicit means of accelerating implementation. Architecture provides the responsibilities and interfaces that make simultaneous contributions coherent. The [core](../releases/2.4.0-dev.1/core.md) defines the authority rules.

## Readiness for fan-out

Before assigning dependent implementation, the orchestrator establishes:

1. Shared requirements and the affected architecture/interfaces.
2. Complete worker assignments with derived behavior, constraints, scope and acceptance.
3. A dependency order and common interface revision.
4. Ownership of shared files and decisions, plus an integration and verification plan.

Independence means compatible assumptions and manageable dependencies, not just non-overlapping paths. Two separate modules that disagree about message semantics are not ready for independent implementation. Conversely, a single module may contain independent tasks when their shared contracts are stable.

## Assign work to responsibilities

Use bounded tasks that fit meaningful responsibilities. An agent need not own an entire horizontal layer. The orchestrator can implement across its authorized internal components and retain integration work. Use serial coordination for a shared decision, then resume independent work.

An assignment includes the link to overall requirements, architecture context, expected behavior/quality, contracts and revisions, allowed changes, dependencies, acceptance and reporting. Workers do not replan the whole project or choose a new method independently.

## Coordinate questions and changes

Workers send interface, neighboring-component and scope needs to the orchestrator. Pause only affected work. The orchestrator evaluates alternatives, consults affected workers, updates the common contract and assignments, and prevents conflicting implementations. A worker cannot widen its own authority. Internal adjustments do not create a human approval gate; overall-requirement changes do.

## Integrate throughout delivery

Integrate coherent contributions, test their interaction and check cross-cutting requirements. A worker's passing tests do not establish whole-system acceptance. Independent review examines contracts, coupling, scope and the actual user result. Correct findings and repeat affected checks until completion.

Separate worktrees or tools may help isolate files, but they are optional host facilities. They do not isolate shared services, ports or databases. If agent concurrency is unavailable, the same work can run serially; do not claim a parallel run occurred. Independent review remains independent.
