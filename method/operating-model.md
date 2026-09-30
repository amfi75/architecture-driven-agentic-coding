# Operating model

The [core](../releases/2.4.0-dev.1/core.md) defines authority. This guide explains the practical records and decisions.

## 1. Understand requirements and inspect the system

Capture the desired outcome, relevant behavior and quality, binding constraints, non-goals and observable acceptance criteria. Identify actual users and critical workflows. Resolve material ambiguity before deriving work. In an existing repository, use architecture documentation, code, contracts, tests, history, configuration and observable runtime behavior to establish the change-relevant understanding required by the core. Follow actual dependencies rather than treating folder names as architecture. Keep reasoning-critical findings in existing architecture, contract or decision records so later work can recover them.

Decide whether modular decomposition and explicit interfaces justify ADAC. Do not select it solely because the repository is large or agents are available.

## 2. Derive architecture and interfaces

Name each affected component's responsibility, decisions it hides, dependencies and contracts. Explain choices through functional needs and quality goals. Describe provider/consumer behavior, errors and invariants as well as data shape. Separate intended interfaces from accidental coupling.

Resolve the shared decisions necessary for dependent work; do not design every future detail up front. A component map, short decision notes and focused contract examples often suffice. Existing useful architecture should be reused.

For architecture-fitting changes with a meaningful regression surface, use the core's [Delta / Preserve / Impact / Evidence reasoning](../releases/2.4.0-dev.1/core.md#changes-within-the-existing-architecture) in the existing task or change record. Capture relevant pre-change behavior where executable coverage is insufficient. Reuse the current design unless the impact assessment shows that architectural decisions must be revisited; small incremental work does not require a new substantial-work plan.

## 3. Prepare the complete initial plan

Trace overall requirements to tasks, integration and verification. Record shared-file ownership, interface revisions and dependencies. Give each worker its derived requirements, scope, relevant contracts and acceptance. The orchestrator owns missing coverage and cross-cutting outcomes.

For substantial work, independently review this plan, including its initial architecture and interfaces, remediate blocking/high findings and obtain the user's initial approval. Preserve the agreed revision. Distinguish binding overall requirements from architecture and task decisions that can change internally.

## 4. Execute and coordinate

The orchestrator may implement directly, assign independent tasks concurrently and sequence dependent ones. Workers inspect context broadly but modify only their assigned scope. They use declared interfaces, report real verification results and send boundary problems to the orchestrator.

A request can ask for another component to change, a field to be added, an assignment to expand or an assumption to be revised. The orchestrator investigates, decides within overall requirements, updates contracts and assignments coherently, and coordinates affected workers. See [change requests](change-request-workflow.md).

## 5. Integrate, verify, review and correct

Check the actual combined result against the overall requirements, not just individual worker reports. Verify relevant contracts and full user workflows. For substantial work or where otherwise required, obtain independent read-only review; remedy confirmed findings and repeat affected checks. Local bugs return to implementation. Unsuitable internal designs return to architecture/interface/task planning under the orchestrator.

As new dependencies or effects emerge, update the existing change record and affected checks before claiming completion. Use the core's correction and architecture-return rules; missing delta or preservation evidence remains unfinished work.

Continue autonomously until the complete agreed result and required review pass. Failed tests never justify silently lowering acceptance criteria.

## 6. Escalate only the decision that requires it

A needed change to overall requirements or binding constraints returns to the user with the precise proposed delta and consequences. An internal architecture change or a revised worker assignment does not require human approval just because it appeared in a plan. An explicitly required technology, compatibility promise or privacy constraint remains binding.

A necessary login or physical action is a targeted external unblock. It is not a new planning cycle. Actual permissions remain applicable throughout.

## Handoff

Provide the implemented outcome, key architecture decisions, interface changes, verification evidence, any required independent verdict and deployment/publication state. Preserve project learning without changing global rules or other repositories without authority.
