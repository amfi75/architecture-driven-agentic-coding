# Architecture-Driven Agentic Coding

ADAC uses architecture to connect requirements to accountable implementation. Its goals are quality through meaningful modularity, speed through controlled parallel work and autonomous completion. The [core](../releases/2.4.0-dev.3/core.md) defines the rules.

The functional architecture describes capabilities and relationships. Software architecture allocates them to components while addressing quality, constraints and dependencies. The mapping is many-to-many. Boundaries hide consequential decisions, localize change and enable independent development; parallel assignments exploit those boundaries rather than dictate them.

The orchestrator maintains that system view and integrates the result. Component owners investigate difficult questions, design their contributions and retain accountability through integration. Workers execute bounded implementation tasks and return unresolved design questions to their owner. Shared-interface and cross-component decisions reach the orchestrator. Independent reviewers challenge the agreement and evidence without implementing corrections.

These responsibilities need suitable capabilities, not a fixed number of agents: the orchestrator can own components and owners can implement directly. Strong reasoning can be concentrated on research and design while well-defined implementation uses lighter models.

Project `AGENTS.md` identifies the method revision, architecture and delivery records. Those records preserve both design and authorized work across sessions. Updating and checking them during delivery prevents them becoming disconnected from the implementation.

New development establishes the architecture. Iterative changes reuse it where suitable, assess intended delta and preservation, and revisit affected boundaries when warranted. Both use one correction loop, not recurring user gates. ADAC is useful for meaningful modular coordination, including a modular monolith; local or inseparable tasks usually need ordinary proportionate work. Text is portable and inspectable, but instruction compliance depends on agents and host capabilities.
