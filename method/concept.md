# Architecture-Driven Agentic Coding

ADAC starts with the desired software outcome. It turns requirements into components with clear responsibilities and explicit interfaces, then uses those boundaries to coordinate agents. The [core 2.4.0-dev.1](../releases/2.4.0-dev.1/core.md) contains the shared commitments; these pages expand them with optional working aids.

## Three goals

- Maintainable, modular software with high quality: hide internal decisions, control dependencies and verify both component behavior and integration.
- Faster implementation through controlled parallel work: assign independent contributions against agreed interfaces, coordinate shared decisions and integrate continuously.
- Autonomous completion: the orchestrator solves internal problems, adjusts the design and keeps working until the agreed acceptance criteria are met.

## Architecture enables the work allocation

A component is a responsibility with an interface, not necessarily a folder, service or horizontal layer. Requirements and quality goals determine the decomposition. Information hiding reduces how much one worker must know about another's implementation. Contracts make assumptions explicit enough to develop and test compatible contributions.

The orchestrator preserves a view of the whole system. It covers cross-cutting concerns, coordinates dependencies and owns integration. Workers receive derived requirements and bounded authority. An independent reviewer checks the result rather than helping implement it.

An owner may implement across internal components within the approved scope. This does not remove architecture boundaries: the same component responsibilities, interfaces and acceptance apply. There is no requirement to assign one agent to every layer.

## Proportionate use

Choose ADAC when meaningful modular responsibilities and verifiable interfaces support the work. A modular monolith can qualify. A small local change or inseparable task normally does not need the setup. Do not manufacture boundaries to occupy agents. Temporary shared-interface work can be coordinated serially within an otherwise parallel project.

## Text, not a controller

The three-file package requires no executable router, Python package or provider integration. Instructions are inspectable, portable, adaptable to the existing repository and easy to version. Agents and their harness must still follow them; text alone does not enforce edit isolation or supply missing capabilities. Tool availability determines whether parallel execution and independent review are possible. Missing required review cannot be relabeled as success.

See [operating model](operating-model.md), [parallel work](parallel-agent-workflow.md) and [theoretical foundations](../docs/architecture-foundations.md).
