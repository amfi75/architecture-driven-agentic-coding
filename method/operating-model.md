# Design depth and delivery

Apply the [core](../releases/2.4.0-dev.3/core.md); record consequential understanding during work rather than only at handoff.

## Understand enough to act

Start from the project entry point and relevant architecture/delivery sections. Use code, tests, contracts, history, configuration and observed behavior to bound plausible impact. Distinguish facts from assumptions. For an improvement, identify Delta / Preserve / Impact / Evidence, including characterization where relevant coverage is insufficient. Suitable existing architecture does not need redesign to satisfy a process.

## Investigate a consequential decision

A useful investigation identifies the decision, required behavior/quality, consequences of choosing poorly, existing solutions, alternatives, discriminating evidence, rationale and remaining verification. Research externally when needed; focused experiments answer specific authorized questions. Stop when a defensible choice is supported and remaining uncertainty has an evidence path.

For example, a context-selection design must fit intended conversation behavior and resource limits; merely exposing a storage API is insufficient. Research may be substantial where the problem warrants it, but collecting material without a decision criterion is not progress.

The orchestrator can investigate before selecting components. Component owners then investigate and design within assigned boundaries. If suitable capability is unavailable, retain the work at the orchestrator or report the gap; do not treat uncertainty as resolved or lower acceptance. Workers receive sufficiently established designs and return unresolved design questions to their owner.

## Iterate against the whole result

Integrate contributions and exercise representative intended-use scenarios. New dependencies or invariants update understanding, impact, preservation and evidence. Unsuitable design returns to affected architecture; recurring preservation failures or broad impact warrant reconsideration, not automatic refactoring. Only required changes to protected commitments reopen the user decision.

Update authoritative records and communicate affected decisions before dependent work resumes. Distinguish approved requirements, proposed deltas and implementation progress. On context loss, reload relevant records and reconcile discrepancies before continuing; a conversation summary is not the architectural source of truth.
