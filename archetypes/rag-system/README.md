# RAG System Archetype

Use this archetype for retrieval-augmented generation systems.

Declare document, index, retrieval, prompt, and answer contracts explicitly. Prompt formats and test fixtures are public surfaces when other layers depend on them.


## Optional architecture aid

First understand requirements and assess whether modular decomposition makes ADAC useful. The adjacent [responsibility map](layers.yaml) is a starting hypothesis, not a required layer sequence or one-agent-per-layer assignment. Adapt it to functional needs, quality goals and the existing system. A modular monolith is sufficient where appropriate.

Define provider/consumer behavior, errors and relevant invariants before dependent work. The orchestrator derives bounded assignments, coordinates shared decisions and integrates the outcome; it may implement itself. Parallelize suitable independent tasks and sequence shared dependencies. Workers request interface, neighboring-module or scope changes through the orchestrator. Derived internal changes can be decided there; overall-requirement or binding-constraint changes return to the user. Follow [core 2.4.0-dev.1](../../releases/2.4.0-dev.1/core.md).
