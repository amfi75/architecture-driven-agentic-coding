# Start in an existing repository

Understand the requested outcome and success criteria first. Inspect enough of the existing system to decide whether ADAC helps; do not impose a new architecture merely because these files exist.

## Inspection pass

Read the README, existing architecture and decision records, build/package files, source and tests, command entry points, configuration, exported modules, fixtures, prompts, schemas, events and CI/local verification commands.

Create a proportionate repository map naming important paths, responsibilities, commands and test locations. Infer boundaries from ownership and actual dependencies, not folder names alone. Mark uncertain inferences and use imports, calls, observable behavior, tests and existing documentation as evidence.

## Describe before changing

Identify intentional interfaces, private internals and accidental coupling separately. Include non-code contracts: CLI flags/output, configuration, messages, database views, file conventions, prompt formats and fixtures. Do not make a private helper public solely because another module imports it.

Record the affected architecture, interface semantics and known gaps. For example, if retrieval reads storage's private files directly, record the coupling and consider a declared storage interface. Do not silently rename modules or reorganize code during inspection.

## Plan from the requirements

Reuse suitable existing architecture. Explain any proposed changes and quality tradeoffs. Derive tasks with expected behavior, contracts/revisions, scope, dependencies and acceptance. Identify shared decisions to resolve before fan-out and explicitly assign integration and cross-cutting requirements to the orchestrator.

Distinguish binding constraints from revisable internal choices. Resolve material requirements ambiguity with the user; internal architecture uncertainty can be investigated by the orchestrator. Independently review the complete substantial-work plan and obtain initial approval before implementing it.

## Completion of preparation

The plan lets a reviewer distinguish intentional interfaces, private details, accidental coupling, uncertainty and safe task boundaries. Each worker knows where to send interface or scope requests. After approval, the orchestrator can revise internal decisions and assignments while preserving overall requirements. See [operating model](../method/operating-model.md).
