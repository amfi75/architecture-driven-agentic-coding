# Design rationale and contribution

ADAC exists to make architecture useful during agentic implementation: understand requirements, identify meaningful responsibilities, define interfaces, derive work and coordinate it through integration. Its goals are maintainability and quality, faster implementation through controlled parallelism, and autonomous completion.

## Restore architecture without restoring unnecessary rigidity

The early method included architecture discovery, component/interface records, bounded tasks, change requests and a coordinator delivery loop. During simplification, versions 2.0–2.2 reduced too much of this concrete guidance. The 2.2 candidate's emphasis on the loop obscured the architecture-driven decomposition that makes the method distinctive.

Version 2.3 restores those concepts from the last pre-2.0 method and updates their authority rules. The historical snapshot is a reconstruction source, not a claim that the old rules were all correct. The three-file package remains self-contained; richer bootstrap, contracts, task records and archetypes are optional and accessible.

## Requirements precede architecture

Functional needs, quality goals and binding constraints determine the architecture. A suitability decision prevents ADAC becoming overhead for every small task. Initial architecture and interfaces are part of the complete substantial-work plan, independently reviewed before the user's initial approval. This avoids asking the user to approve a plan whose important design is still absent.

## System understanding supports safe change

For substantial change, reason from requirements to architecture. For incremental change, reason from intended delta to preserved behavior. System understanding supports both. The orchestrator maintains that understanding as evidence changes; existing project or harness records retain what later work needs. ADAC adds no memory implementation.

A change fitting the architecture can still cause regressions. Explicit preservation and impact reasoning helps prevent a narrowly successful patch from silently changing other required behavior. Repeated boundary pressure warrants architectural reconsideration, not automatic refactoring, which can itself expand the regression surface.

## Ownership can span components

A leading agent may implement an approved outcome across authorized internal components. A blanket ban on cross-component owner work and one-agent-per-layer assignments would obstruct integration. Architectural responsibilities still matter; workers remain bounded by explicit derived requirements, contracts, scope and acceptance.

## Internal changes belong with the orchestrator

The orchestrator is the accountable agent role, not extra controller software. Workers can ask for interface changes, neighboring-component work or a revised assignment. The orchestrator evaluates alternatives, updates common contracts and tasks, and coordinates integration autonomously.

A design decision does not become an immutable user requirement simply because it appeared in a plan. The user decides again when overall requirements or binding constraints must change. Explicit compatibility, privacy, security or technology commitments remain protected. This distinction preserves autonomy without allowing agents to redefine success.

## Capabilities do not grant permissions

Model recommendations describe useful capabilities for orchestration, implementation and independent review. A stronger model does not expand a worker's scope or turn a reviewer into an implementer. Model names, when included, must be dated examples. The method does not require a router, Python interpreter, model assignment service or particular provider.

Text instructions are portable, transparent, easy to copy, version and inspect, and usable with existing project practices. These are practical advantages; they are not an enforcement guarantee. The host must provide the execution and review capabilities actually used.

## Review remains meaningful

Autonomy includes testing, observation, integration, independent review and remediation. Neither internal PASS reports nor theoretical citations establish better engineering outcomes by themselves. Acceptance must refer to the agreed result and actual evidence. Private project results are not public release evidence. Prior experiments do not certify the corrected method across all environments.

## Human and AI contribution

The maintainer defined and applied the method in practice, reports about six months of successful use, and challenged the loss of architecture-centered decomposition. He specified the restored priorities: requirements first, controlled fan-out, explicit interfaces, an agent orchestrator, derived worker requirements, internal change requests and autonomy within overall requirements. He also required advisory model guidance, clear speed benefits, private review before publication and no new demo work for this repair.

AI assisted repository/history inspection, research, drafting, diagrams, consistency checks and independent review. The correction is an AI-assisted implementation of those human decisions; it does not justify attributing every line of implementation or every test execution to the maintainer. The agent's earlier simplification went too far, and the maintainer identified the problem.

The [foundations](architecture-foundations.md) distinguish established theory from ADAC's agent-specific application. [Verification](verification.md) distinguishes practical experience, historical experiments and the checks performed for this correction.
