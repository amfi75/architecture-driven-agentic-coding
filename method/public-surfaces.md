# Components and public surfaces

A public surface is an interface another component or external consumer may rely on. “Public” here describes a dependency boundary; it does not necessarily mean internet-facing or immutable. Use the [core's](../releases/2.3.0/core.md) distinction between overall requirements and derived decisions to determine change authority.

## Discover the actual interfaces

Look beyond functions and classes. Interfaces include data objects, messages and events, CLI flags/output/exit codes, configuration keys, database views, file conventions, prompt formats and shared fixtures. Record the owner/provider and consumers. A private helper imported elsewhere is evidence of coupling, not automatically an intentional contract.

For each affected interface describe:

- purpose and relevant requirement;
- inputs, outputs and their shape;
- preconditions, success behavior and failure behavior;
- relevant invariants, ordering, identity and ownership;
- compatibility obligations and verification examples;
- current revision and affected providers/consumers.

Use only details relevant to the work. Do not turn every internal function into a cross-component contract.

## Hide decisions likely to change

A storage component might expose record lookup while hiding file layout and indexing. A protocol adapter might expose normalized messages while hiding transport parsing. This lets implementation vary without forcing consumers to understand private details.

Define allowed dependencies explicitly. If two components need the same decision, choose an owner or a shared contract and coordinate it. Merely dividing code into directories does not create independent work.

## Change authority

A worker reports interface pressure to the orchestrator before changing shared assumptions or exceeding its assignment. The orchestrator may revise a derived internal interface and the affected assignments while preserving overall requirements. It updates providers, consumers and verification together, distributing the same revision to all affected workers.

Existing external commitments and explicitly agreed compatibility, technology, privacy or security requirements cannot be reclassified as internal. A required change to those commitments needs the user's decision. See [change requests](change-request-workflow.md) and the optional [contract record](../templates/contract.md).
