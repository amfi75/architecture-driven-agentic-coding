# CLI Tool Archetype

Use this archetype for command-line tools.

Treat command syntax, flags, exit codes, config files, and output formats as public surfaces. They are user-facing contracts even when no library API exists.


## Optional architecture aid

The adjacent [responsibility map](layers.yaml) is a design hypothesis. Derive boundaries from required capabilities, quality, constraints and the actual system; functions need not map one-to-one to components. No layer sequence, service topology or one-agent-per-layer assignment is prescribed.

Investigate consequential uncertainty and assign design ownership before dependent implementation. Use [core 2.4.0-dev.2](../../releases/2.4.0-dev.2/core.md) for contracts, bounded assignments, coordinated changes and integrated acceptance. The archetype adds no separate rules.
