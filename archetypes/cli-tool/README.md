# CLI Tool Archetype

Use this archetype for command-line tools.

Treat command syntax, flags, exit codes, config files, and output formats as public surfaces. They are user-facing contracts even when no library API exists.


## Optional architecture aid

The adjacent [responsibility map](layers.yaml) is a design hypothesis. Derive boundaries from required capabilities, quality, constraints and the actual system; functions need not map one-to-one to components. No layer sequence, service topology or one-agent-per-layer assignment is prescribed.

Investigate consequential uncertainty and assign accountable component owners before dependent implementation. Owners may delegate bounded implementation to workers; workers report to their owner, and shared changes go to the orchestrator. Record the chosen functional/software mapping in the project architecture. Use [core 2.4.0-dev.3](../../releases/2.4.0-dev.3/core.md) for contracts, bounded assignments, coordinated changes and integrated acceptance. The archetype adds no separate rules.
