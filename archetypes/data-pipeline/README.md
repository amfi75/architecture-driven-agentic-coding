# Data Pipeline Archetype

Use this archetype for batch or streaming data movement.

Declare source records, normalized records, sink commands, and log events before assigning agents. Most unsafe coupling appears when transform code depends on source-specific internals.


## Optional architecture aid

The adjacent [responsibility map](layers.yaml) is a design hypothesis. Derive boundaries from required capabilities, quality, constraints and the actual system; functions need not map one-to-one to components. No layer sequence, service topology or one-agent-per-layer assignment is prescribed.

Investigate consequential uncertainty and assign accountable component owners before dependent implementation. Owners may delegate bounded implementation to workers; workers report to their owner, and shared changes go to the orchestrator. Record the chosen functional/software mapping in the project architecture. Use [core 2.4.0-dev.3](../../releases/2.4.0-dev.3/core.md) for contracts, bounded assignments, coordinated changes and integrated acceptance. The archetype adds no separate rules.
