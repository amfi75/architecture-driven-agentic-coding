# Controlled parallel work

Architecture enables independent contributions; coordination keeps them compatible. Apply the [core](../releases/2.4.0-dev.3/core.md) and use [assignment formats](../templates/task-package.md) when creating assignments.

## Separate ownership from implementation

The orchestrator assigns component owners purpose, derived behavior/quality, interfaces, design discretion, research questions and acceptance. Owners turn defensible designs into bounded worker tasks where delegation is useful and authorized. Workers receive established decisions, permitted changes, checks and a reporting route to the owner. Delegation does not transfer the owner's design or integration accountability.

Owners can implement directly, cover coherent component groups, or be the orchestrator itself. No extra agent hierarchy or one-agent-per-layer arrangement is required. The orchestrator checks cross-cutting outcomes and requirements not covered by individual assignments.

## Check readiness

Confirm shared decisions, common interface revisions, dependency order, shared-artifact ownership and integration evidence before concurrent implementation. Separate paths do not guarantee independent semantics. Resolve shared uncertainty before dependent implementation. Work allocation follows meaningful architecture rather than available agent count.

Supply relevant sections of `AGENTS.md`, architecture and delivery records at each delegation; do not assume context inheritance. Preserve current assignments and decisions so replacement contexts can resume without the entire conversation.

## Coordinate and integrate

Workers report evidence and design/scope problems to their owner. Owners resolve assigned internal questions and escalate interface, neighboring-component or authority changes to the orchestrator. Updated contracts and records reach affected owners and workers before dependent work resumes. Owners evaluate and integrate worker output; the orchestrator evaluates the complete result.

Worktrees isolate files, not shared ports, databases or services. Use the host's available execution capabilities; serial delivery is possible when parallel execution is unavailable. Record actual mode rather than claim concurrency. Independent review still requires independence.
