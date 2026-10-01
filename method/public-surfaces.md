# Components and public surfaces

A component boundary assigns responsibility and hides implementation decisions. A public surface is an interface another component or external consumer relies on; it need not be internet-facing. The [core](../releases/2.4.0-dev.2/core.md) determines change authority.

## From functions to boundaries

Trace needed behavior across the system, then consider quality, shared state, dependencies and likely changes. Avoid turning each processing step into a module automatically. A storage boundary can hide representation and indexing while serving several capabilities. A functional view explains what happens; the component view explains who owns the decisions that realize it.

## Describe the dependency

For an affected interface, capture provider/consumers, purpose, inputs/results, preconditions, errors, invariants, ordering or ownership where relevant, compatibility and revision. Include observable examples where they clarify semantics.

Look beyond functions: events, files, configuration, CLI output, database views, prompts and fixtures can all be contracts. A private helper imported elsewhere reveals coupling, not necessarily an intentional interface. Distinguish actual dependencies from desired ones before changing either.

Use enough detail to coordinate independent work without exposing every internal function. Shared design decisions need a clear owner. Coordinate changes through the [change-request guide](change-request-workflow.md); binding external commitments remain protected even when files are labeled internal.
