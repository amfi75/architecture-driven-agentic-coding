# AI Agent System Archetype

Use this archetype for systems that plan, call tools, retrieve memory, and evaluate outputs.

Treat prompts, tool manifests, memory records, and evaluation reports as public surfaces. Agents must not silently change prompt input or output formats.


## Optional architecture aid

The adjacent [responsibility map](layers.yaml) is a design hypothesis. Derive boundaries from required capabilities, quality, constraints and the actual system; functions need not map one-to-one to components. No layer sequence, service topology or one-agent-per-layer assignment is prescribed.

Investigate consequential uncertainty and assign design ownership before dependent implementation. Use [core 2.4.0-dev.2](../../releases/2.4.0-dev.2/core.md) for contracts, bounded assignments, coordinated changes and integrated acceptance. The archetype adds no separate rules.
