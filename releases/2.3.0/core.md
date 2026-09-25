# ADAC core 2.3.0

Architecture-Driven Agentic Coding applies modular design, explicit interface contracts and architecture-centered iterative development to coding agents. Its goals are maintainable, modular software of high quality; faster implementation through controlled parallel work; and autonomous completion of the agreed outcome.

ADAC is a text method. Agents follow these instructions; there is no required controller, router, interpreter, installation or provider. Higher-priority instructions and actual permissions still apply. [Recommendations](recommendations.md) are adaptable advice, never additional authority. Existing project pins and approved requirements do not migrate automatically.

## Terms and responsibilities

- **Overall requirements:** the agreed outcome, required behavior and quality, binding constraints, non-goals and observable acceptance criteria. Include compatibility, privacy, security, cost or technology choices when they are actually binding. Preserve the exact agreed revision and approval record.
- **Delivery Contract:** the compact record of those overall requirements and authority. This organizational agreement differs from a software interface contract.
- **Architecture:** components, responsibilities, dependencies and the decisions that explain their organization. A component hides implementation decisions behind declared interfaces; it need not be a service, process or whole layer.
- **Interface contract:** what a provider and its consumers can assume: data shape, behavior, preconditions, results, errors, relevant invariants and compatibility. A CLI, event, fixture, file or prompt format may also be an interface.
- **Orchestrator / owner:** the leading agent accountable for architecture, coordination, integration and the entire outcome. It may also implement within its authorized scope. This is a role, not a required software service.
- **Worker / sub-agent:** an agent assigned derived requirements, interfaces, an edit scope and acceptance criteria. It reports boundary pressure to the orchestrator instead of expanding its own scope.
- **Reviewer:** an independent read-only evaluator. A separate human or fresh agent context may review; self-review or changing a model name alone does not establish independence.
- **Derived decision:** an architecture choice, internal interface or worker assignment selected to satisfy overall requirements. Merely including it in a plan does not make it a binding user requirement.

## 1. Understand requirements and choose whether ADAC fits

First understand the desired result and current system. Resolve material ambiguity with the user and record success criteria and binding constraints. Do not begin by assigning agents or selecting a layer template.

Choose ADAC when useful responsibilities can be separated through explicit interfaces and tasks can be developed and verified with manageable dependencies. Communication adapters, application logic, persistence and user interaction are possible responsibilities, not a prescribed architecture. A modular monolith can qualify. Inspect actual dependencies: separate directories alone do not establish independence.

A small local fix, an inseparable one-off task or routine inspection usually needs no ADAC setup. Project size and agent availability alone are insufficient. Use ordinary proportionate work practices instead; applicable project requirements still apply.

For suitable work, decide where parallel execution helps. Shared decisions may need coordination before otherwise independent packages begin. Some tasks will run serially. Do not distort the product architecture merely to occupy more agents.

## 2. Derive architecture, interfaces and a reviewed plan

Before the affected implementation or fan-out:

1. Understand and reuse the existing architecture where suitable; for new work, establish a proportionate initial design from requirements.
2. Name component responsibilities, what each owns, the changeable implementation decisions it hides, and allowed dependencies. Explain important choices and relevant alternatives using functional needs, quality goals and constraints.
3. Specify the affected interfaces: providers/consumers, inputs/outputs, semantics, errors, invariants and compatibility. Do not expose a private detail merely because another component currently depends on it; record accidental coupling and plan its treatment.
4. Derive tasks from the architecture and overall requirements. Identify dependencies, shared files and interface decisions. Explain which tasks can proceed independently and which must wait. Assign integration and cross-cutting requirements explicitly to the orchestrator.
5. Plan reuse, sequencing, relevant tests and observation of the complete user result. Keep overall requirements distinct from revisable implementation decisions.

These contents may fit in one short record; no fixed document layout or diagram count is required. Use enough architecture to support the affected work, not a complete frozen design of every future detail.

For substantial work, give an independent read-only reviewer the requirements, initial architecture, interfaces, task plan, evidence and acceptance criteria. The reviewer challenges whether the intended outcome can be delivered. Repair confirmed blocking/high gaps and re-review. Present the reviewed plan and requirements for the user's initial approval; record the approved revision before implementation. Missing review or approval remains an unmet gate, not permission to simulate it. Local tasks do not acquire these gates simply because ADAC files exist.

## 3. Give each worker a complete assignment

Every assignment contains:

- the goal and its relationship to overall requirements;
- the relevant architecture, expected behavior, quality and constraints;
- inputs, outputs, interface revision and dependency readiness;
- authorized components/files and excluded changes;
- acceptance criteria, required verification and what to report back.

The orchestrator checks that all overall requirements are covered, including integration and cross-cutting properties. A list of files is not a task specification. No separate human approval is needed for each derived package.

Workers read enough surrounding context to understand their contribution, use declared interfaces, and avoid relying on neighboring private internals. They implement and verify within their assignments. They report changed behavior/files, checks and actual results, interface impact and unresolved questions. A stronger model does not widen scope.

## 4. Coordinate change requests and parallel work

Before concurrent work, establish a common interface revision, clear ownership of shared artifacts and readiness of dependencies. There is no mandatory one-agent-per-layer mapping. Parallel workers must not make incompatible assumptions about the same interface.

A worker requests a change when a required field or behavior is absent, another component must change, private internals would be needed, or its assignment is insufficient. It sends the orchestrator the exact need, why the existing contract fails, affected consumers/packages, proposed options and relevant verification. Pause the affected work; unrelated authorized work can continue.

The orchestrator then:

1. Checks the request against overall requirements and alternatives; consults affected workers as needed.
2. Decides internally when only derived decisions change. It may revise architecture, internal interfaces, assignments or sequencing, or perform the integration itself.
3. Records the decision and updates the shared interface/assignment before dependent implementation proceeds. A concise note in the task or change record is enough; no mandatory per-field form.
4. Makes affected workers use the same updated contract; pauses or resequences conflicting work and updates consumers and checks coherently.
5. Integrates results and repeats affected contract and end-to-end verification.

A worker cannot approve its own expanded authority. The orchestrator does not forward routine internal problems to the user without investigating a solution.

## 5. Continue the autonomous delivery and quality loop

After initial approval, resolve dependencies, evaluate reuse, implement, integrate, observe actual behavior and run the required checks. Diagnose failures and correct them. A code defect returns to implementation; an unsuitable internal design returns to architecture/interface/task planning under the orchestrator. Neither creates a new human approval gate while overall requirements remain satisfied.

Give an independent reviewer the agreed baseline, approved requirement changes, relevant architecture and interfaces, actual changes and evidence. The reviewer tests claims against acceptance and architecture, including whether passing components work together. It must not turn preferences into new requirements. Correct confirmed failures, repeat affected verification and obtain independent re-review. Do not repeat passing work without a new change, failure or unresolved concern.

Continue until every required criterion is met and the substantial-work final review passes. A usable complete result matters: test counts, documentation compliance or model agreement do not replace observed behavior. Report absent evidence as blocked, never passed.

## When the user must decide again

The substantive return to the user is a needed change to overall requirements or binding constraints: for example dropping offline operation, weakening agreed compatibility or relaxing acceptance. Propose the exact delta, reason, alternatives, consequences and verification; obtain explicit approval before relying on it. Review the affected plan and preserve the original agreement and approved changes. Pending or rejected changes are not authorized.

An explicitly required architecture or technology is a binding constraint; an agent-chosen implementation choice is not automatically one. Check the agreement and existing obligations rather than relabeling a protected promise as internal. Changing a worker's derived requirements is not itself a change to the user's overall requirements. Do not treat a failed check as permission to lower them.

Actual permissions remain in force. A login, physical action or access grant only the user can supply is a targeted external unblock, not a new architectural approval cycle. Resume the interrupted work afterward. This method cannot grant access, publication or cross-project authority that the task does not provide.

## Completion and learning

For substantial work, the independent final verdict identifies baseline, approved deltas, requirement preservation, any unauthorized change, each criterion's PASS/FAIL/BLOCKED result, actual outcome and an overall verdict. PASS requires every required criterion to be satisfied; missing evidence is BLOCKED and a demonstrated required failure is FAIL. Neither is completion. Resolve disagreements about requirements rather than declaring unilateral success.

Hand off the working result, relevant architecture/interface decisions, verification, remaining limits and publication/deployment state. Preserve useful decisions and lessons in the project. Improvements to this method, global instructions or other projects require their own authority; learning does not silently change them.

## Flow in plain text

START → understand requirements → assess suitability → derive architecture, interfaces and assignments → independently review the initial plan → user approves → orchestrator coordinates implementation (parallel where useful) → integrate, verify, independently review and correct → all requirements met → END.

Plan-review gaps stay in planning. Worker change requests go to the orchestrator. In-scope design problems return to internal planning; implementation failures return to implementation. A necessary overall-requirement change returns to the user and affected planning/review. External unblocks resume the interrupted phase. No executable controller is supplied.
