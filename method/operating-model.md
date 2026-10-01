# Design depth and delivery

Apply the [core](../releases/2.4.0-dev.2/core.md) with records proportionate to the decision.

## Build relevant understanding

Use code, tests, contracts, history, configuration and observed behavior to trace the affected flow. Separate verified facts from assumptions. For incremental work, identify the intended change and the behavior that must survive; use existing records for the core's Delta / Preserve / Impact / Evidence reasoning.

## Investigate a decision

A useful investigation states:

- decision and consequence of choosing poorly;
- required behavior, quality and constraints;
- existing implementation, reusable solutions and viable alternatives;
- evidence distinguishing the alternatives;
- selected approach, tradeoffs and remaining verification.

For example, a context-selection design must serve the agreed conversation behavior and resource limits. A storage API alone cannot establish that fit. Determine what evidence would discriminate approaches before collecting more material. Consult relevant primary documentation or research when local knowledge is insufficient; experiment only to answer a consequential unresolved question within authority.

The orchestrator may assign this investigation before deciding component boundaries. Once boundaries exist, delegate detailed design explicitly and retain system-level tradeoffs. If no suitable specialist is available, the orchestrator retains the work or reports missing capability rather than treating uncertainty as resolved.

## Keep design connected to delivery

Carry rationale and acceptance into assignments. Integrate coherent contributions and exercise representative intended-use scenarios. Findings may refine the design or expand relevant system understanding. Preserve the resulting decisions in existing project records; the core governs approvals, correction and completion.
