# Components and public surfaces

A component boundary assigns responsibility and hides implementation decisions. A public surface is an interface another component or external consumer relies on; it need not be internet-facing. The [core](../releases/2.4.0-dev.3/core.md) determines change authority.

## Connect functions and components

The authoritative architecture document records capabilities, relationships, component allocations and rationale. Trace needed behavior, then consider quality, shared state, dependencies and likely change. One capability may cross components; one component may support several capabilities. A processing step need not become a module.

Prefer cohesive responsibilities and useful abstractions that limit coupling and localize change. A storage boundary can hide representation while supporting several capabilities. Specify required portability from actual needs, rather than assuming every backend must be supported. Record allowed dependencies, private internals and observed accidental coupling separately.

## Describe the interface

Use the [interface format](../templates/contract.md) for a new contract. Capture provider/consumers, purpose, revision, inputs/results, semantics, errors, invariants, relevant ordering/ownership and compatibility. Examples can clarify obligations. Events, files, configuration, CLI output, database views, prompts and fixtures can all be contracts.

Link detailed contracts from the architecture instead of maintaining duplicate definitions. Inspect discrepancies between records and implementation before affected work; mark intended changes separately from implemented status. Use enough detail for compatible independent work without documenting every internal function.

Component owners retain design responsibility. Workers raise questions to their owner; shared contract changes use the [coordination route](change-request-workflow.md). Protected external commitments remain protected regardless of file names.
