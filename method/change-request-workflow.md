# Change requests and autonomous decisions

A change request is a focused message about a boundary problem. It need not be a ticket or form. It routes a worker's discovery to the orchestrator while preserving the [overall requirements](../releases/2.4.0-dev.1/core.md).

## When a worker sends a request

Examples include a missing field, insufficient error behavior, a needed change in another component, a prompt/fixture format mismatch, reliance on private internals or an assignment that cannot satisfy its acceptance criteria.

Send:

- the unmet derived requirement and why the current interface or assignment is insufficient;
- affected components, contracts, consumers and tasks;
- a proposed change or alternatives;
- compatibility, quality and integration consequences;
- the checks needed after the change.

Do not silently extend scope or make unilateral shared-interface changes. Pause the dependent portion; continue unrelated authorized work.

## Orchestrator decision

First investigate whether the need can be met under the current contract. Consult affected workers. If a derived internal decision must change, the orchestrator may decide, record it concisely, revise contracts and tasks and coordinate implementation. Deliver the same current revision to every affected worker. Sequence conflicting changes and repeat affected integration checks.

For example, adding an internal record field can be approved and coordinated by the orchestrator when it preserves overall requirements. A task may be expanded to cover its consumer as well. Neither decision needs the user solely because the old field list or task appeared in the approved plan.

## Return to the user

If the proposed solution requires changing the agreed outcome, acceptance or a binding constraint, present that exact delta, rationale, alternatives and consequences for explicit approval before relying on it. For example, dropping promised offline operation or breaking agreed external compatibility is not an internal refactor. Existing protected obligations cannot be relabeled to avoid this decision.

A rejected or unanswered request leaves the original requirements in force. A failed test is a reason to repair or propose a delta, never authority to weaken acceptance. Review affected planning after an approved requirements change.

A required user login is a targeted unblock, not a requirement change. Resume the interrupted work afterward.

## Close the request

Record the decision, authority basis, affected contract/task revision, implementation ownership and actual verification. The orchestrator closes the request when the dependent work is integrated and checked. See the optional [change-request record](../templates/change-request.md).
