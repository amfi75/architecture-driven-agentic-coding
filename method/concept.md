# Architecture-Driven Agentic Coding

ADAC connects requirements to architectural responsibilities, explicit interfaces and coordinated implementation. The [core](../releases/2.4.0-dev.2/core.md) defines the method.

Its three goals are maintainable modular software of high quality, faster implementation through controlled parallel work, and autonomous completion within agreed requirements.

Functional understanding describes the capabilities and behavior needed. Software architecture realizes them while addressing quality, constraints and existing dependencies. One function may involve several components; one component may support several functions. Choose boundaries that hide consequential implementation decisions and localize change. Work allocation follows those boundaries.

The orchestrator retains the whole-system view. A complex component assignment includes design and investigation as well as implementation; a routine coding assignment can be narrower. Explicit ownership avoids leaving design between tasks. Review challenges the integrated result.

A modular monolith can benefit. A local fix or inseparable task generally needs ordinary proportionate work. More agents and more folders do not establish useful independence.

ADAC uses readable, versionable text with no required runtime. Its portability does not guarantee every agent's compliance. Host capabilities determine available execution and review; missing required review remains unfinished work.
