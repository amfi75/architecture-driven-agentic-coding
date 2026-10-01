# Controlled parallel work

Architecture makes simultaneous contributions coherent. Apply the [core](../releases/2.4.0-dev.2/core.md) to select ready packages with compatible interfaces and manageable dependencies.

## Allocate responsibility before files

A component owner receives the component's purpose, derived behavior and quality, design discretion, investigation needs and acceptance. A routine implementer can receive a narrower established design. Neither assignment creates additional authority. Keep design ownership explicit when implementation is split.

Use the optional [task package](../templates/task-package.md). A message with the same information works. Include enough surrounding system context to reason about integration, without copying the entire orchestration history. The orchestrator retains cross-cutting outcomes and uncovered requirements.

## Check readiness

Confirm common interface revisions, dependency order, shared-file ownership and integration evidence. Separate paths do not guarantee independent semantics. Resolve a shared decision serially before parallel implementation when necessary. Do not select boundaries merely to employ available agents.

## Coordinate and integrate

Workers report actual decisions, outcomes and boundary pressure. The orchestrator resolves competing assumptions, updates affected assignments and integrates throughout delivery. A component owner follows its contribution through integration; passing local checks is insufficient for whole-system acceptance.

Worktrees are optional and do not isolate shared ports, databases or services. Serial delivery remains possible when concurrency is unavailable; report the actual execution mode. Independent review still needs independence.
