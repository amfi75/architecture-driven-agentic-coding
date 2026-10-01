# Assignment

Use this format for new assignments in the delivery record or a linked task record. Choose the section dictated by the role: orchestrator assigns component ownership; the accountable owner assigns bounded worker implementation where delegation is authorized. An orchestrator acting as owner can assign workers directly.

## Shared assignment context

- Role, named assignee, assigning owner and reporting recipient:
- Purpose, contribution to the complete result and related overall requirements:
- Derived behavior/quality, constraints and observable acceptance:
- Relevant `AGENTS.md`, architecture and delivery sections; exact method revision:
- Contracts/revisions, providers/consumers, inputs/results, errors and invariants:
- Permitted edits, exclusions, shared-artifact ownership and design discretion:
- Dependencies/readiness, integration owner and required checks:

A path list alone is not a complete assignment. Give enough purpose and surrounding context without copying the entire conversation.

## Component-owner assignment

- Component or coherent group and its functional/software mapping:
- Investigation questions, criteria, existing solutions, alternatives and evidence:
- Design responsibilities, rationale, research stopping condition and remaining validation:
- Proposed worker tasks, retained decisions and integration/preservation evidence:

The owner retains accountability through integration, including evaluating delegated results. Decisions within its discretion remain autonomous; interface/cross-component/authority changes go to the orchestrator.

## Worker implementation task

- Established design and implementation outcome:
- Decisions already settled; bounded implementation discretion:
- Actual checks to perform and evidence to return:

Implement and verify within scope. Report design-invalidating questions or insufficient scope to the owner; pause affected work and continue unrelated authorized work. Do not independently redesign architecture, restart parent planning or broaden permissions.

## Result and continuity

Report decisions, changed behavior/files, actual check results, intended-use/preservation evidence, interface effects, unresolved questions and next actions. Record progress so another authorized context can resume. Neither worker success nor delegation transfers whole-system acceptance or authority to accept new limitations.
