# The delivery loop within architecture-driven work

The diagrams show the substantial-work flow. Architecture-fitting incremental work uses the core's [compact change guidance](../releases/2.4.0-dev.1/core.md#changes-within-the-existing-architecture) and proportionate review; it does not automatically enter the full planning gates.

The loop supports the architecture-driven method. First understand requirements and the relevant system, decide whether modular decomposition fits and derive architecture, interfaces and assignments. For substantial work, independently review this complete plan and obtain the user's initial approval. Only then enter implementation.

The main [workflow diagram](diagrams/workflow.svg) shows the starting point and completion. The diagram below expands the return paths. It is a representation of the instructions in [core 2.4.0-dev.1](../releases/2.4.0-dev.1/core.md), not an executable controller.

![Delivery and change-request return paths](diagrams/loop.svg)

## The return paths

| Observation | Recipient and next step | Human decision? |
| --- | --- | --- |
| Missing delta or preservation evidence; newly discovered impact | Orchestrator updates understanding, the change record and affected verification, correcting implementation where needed | No, if overall requirements are preserved |
| Local implementation defect | Orchestrator/assigned worker repairs implementation and repeats affected checks | No |
| Missing internal field or behavior; another component needs a change | Worker sends need, reasons, affected contracts/tasks, options and checks to the orchestrator | No, if overall requirements are preserved |
| Worker assignment is insufficient | Orchestrator revises scope or allocation and coordinates dependent work | No, if overall requirements are preserved |
| Shared-interface conflict or unsuitable internal design | Orchestrator revisits architecture/interfaces/tasks, distributes one current contract and resequences work before integration | No, if overall requirements are preserved |
| Required result, acceptance or binding constraint cannot be preserved | Orchestrator proposes exact requirement delta, alternatives and consequences; affected planning/review follows approval | Yes, before relying on the change |
| Login or physical action only the user can supply | Targeted unblock, then resume the interrupted step | Action/access only; not a new requirements cycle |
| All required criteria and independent review pass | Handoff complete result and evidence | Completion; no repeated phase gate |

A worker pauses only dependent work while a request is unresolved. It never expands its own authority. The orchestrator may implement directly and revise internal decisions without asking the user about every interface field. An explicitly required technology or compatibility promise cannot be relabeled as internal.

## Mapping to the actual instructions

- Core §§1–2: requirements, suitability, architecture/interfaces/assignments, independent initial plan review and approval.
- Core §§3–4: complete worker packages, common interface revision, requests to the orchestrator, updates to affected consumers and integration.
- Core §5: implement, observe, update understanding as evidence changes, verify, obtain required independent review, correct and repeat affected checks.
- Core “When the user must decide again”: overall-requirement changes, preserved authority and targeted external unblocks.
- Core “Completion and learning”: criterion-level evidence, independent final verdict and handoff; missing evidence is not completion.

Thus there are returns to implementation, to internal architecture/task planning, and to requirements when a user decision is necessary. The diagram's arrows summarize those normative instructions. Execution depends on instruction-following agents and their tools. See [verification](verification.md) for what has actually been checked, rather than assuming that drawing a loop establishes enforcement or empirical effectiveness.
