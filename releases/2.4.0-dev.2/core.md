# ADAC core 2.4.0-dev.2

Architecture-Driven Agentic Coding turns understood requirements into modular software, explicit interfaces and coordinated agent work. Its goals are maintainable software of high quality, faster implementation through controlled parallelism, and autonomous completion of the agreed outcome.

This is a complete text specification: no controller, router, interpreter, installation or provider is required. Agents follow the rules; text does not enforce them. Higher-priority instructions, actual permissions and existing project pins apply. [Recommendations](recommendations.md) are advice, never authority. Upstream changes do not migrate projects automatically.

## Responsibilities and commitments

**Overall requirements** define the outcome, behavior, quality, binding constraints, non-goals and observable acceptance. The **Delivery Contract** records these requirements and authority, including the exact approved revision and subsequent approved deltas. A software **interface contract** instead defines provider/consumer obligations: inputs, results, semantics, errors, invariants and compatibility.

**Architecture** identifies responsibilities, hidden implementation decisions, dependencies and their rationale. A component need not be a service, folder or layer. **Derived decisions**—agent-chosen architecture, internal interfaces and assignments—remain revisable; appearing in a plan does not make them binding user requirements.

| Role | Accountability |
| --- | --- |
| Orchestrator | Maintains relevant system understanding; owns architecture, assignments, shared decisions, integration, cross-cutting requirements and the entire result. May implement within its authorized scope. |
| Worker / component owner | Delivers a bounded assignment. Component ownership includes assigned investigation, design, implementation and evidence; routine implementation may have narrower responsibility. Reports boundary pressure to the orchestrator. |
| Independent reviewer | Challenges design and completion against requirements, read-only. Use a separate human or fresh agent context; self-review or a model-name change alone is insufficient. |

Combine responsibilities where useful without compromising review independence. A role or stronger model never grants additional scope, delegation or tool permissions.

## 1. Understand and assess suitability

Understand intended use, required behavior, quality and constraints before choosing components or agents. Resolve material requirements ambiguity with the user. For existing systems, inspect affected responsibilities, dependencies, flows, contracts and invariants until plausible impact can reasonably be bounded and safe-completion evidence identified. Inspect further if insufficient; exhaustive repository understanding is unnecessary.

Use ADAC when meaningful responsibilities and explicit interfaces support manageable dependencies and coordinated development. A modular monolith can qualify. Small local fixes, routine inspection and inseparable tasks usually need ordinary proportionate practices. Size, separate directories or available agents do not establish suitability or independence.

## 2. Design and investigate

Before affected implementation or fan-out:

1. Identify needed capabilities, behavior and their relationships. Derive software boundaries from this functional understanding together with quality requirements, constraints and existing architecture. Reuse suitable design; functions need not map one-to-one to components. No separate functional-architecture document or completed phase is required.
2. Explain component responsibilities, ownership, hidden changeable decisions and allowed dependencies. Specify affected interface contracts and revisions, including non-code surfaces such as events, CLI output, configuration and prompt formats. Distinguish intentional interfaces from accidental coupling to private internals.
3. Derive work and acceptance from requirements and architecture. Assign shared artifacts and integration explicitly. Identify decisions and dependencies that must be resolved before independent work begins; parallelize only ready contributions.

**Investigate consequential uncertainty** affecting behavior, boundaries, quality or solution choice. The assigned owner frames the decision, criteria and evidence needed; inspects existing solutions and relevant established approaches; compares viable alternatives and records a concise rationale. Research externally when relevant knowledge is missing. Familiar routine work needs no study. Use focused experiments only when needed and authorized.

Stop investigation when evidence supports a defensible choice and remaining uncertainty has a verification path. Resolve critical unknowns before dependent implementation; do not lower acceptance to proceed. Investigation may precede component selection or recur during delivery. The orchestrator can delegate investigation while retaining boundary decisions. Refine affected design recursively, without freezing every future detail or adding human gates for internal design.

For substantial work, independently review the complete initial plan: requirements, architecture/interfaces, assignments, reuse, dependencies, sequencing, evidence and acceptance. Repair blocking/high gaps and re-review; obtain the user's approval and record its exact revision before implementation. Missing review or approval is an unmet gate. Small tasks do not acquire these gates merely because ADAC is referenced.

### Changes within the existing architecture

For meaningful regression risk, capture **Delta** (intended behavior change), **Preserve** (relevant behavior remaining unchanged), **Impact** (plausibly affected responsibilities, contracts and workflows), and **Evidence** (checks of change and preservation). Use existing task records, not a mandatory new template. Characterize relevant behavior before modification when executable coverage is insufficient. Reuse fitting architecture; substantial work and existing project obligations retain their gates.

## 3. Delegate complete, bounded work

Give each worker:

- purpose and contribution to the overall result and end-to-end behavior;
- derived functional/quality requirements, constraints and observable acceptance;
- relevant architecture, interfaces/revisions, inputs/outputs and dependency readiness;
- authorized edits, exclusions, shared ownership and design discretion;
- investigation questions where needed, required checks, reporting and change-request route.

The orchestrator checks whole-requirement coverage, including cross-cutting outcomes. Supply relevant method instructions and context explicitly; do not assume inheritance or require the whole conversation. A file list is insufficient. Preserve recoverable decisions and evidence in existing project records.

Workers read surrounding context, use declared interfaces, and design, implement and verify within their assignments. They report decisions, changed behavior/files, actual check results, interface effects and unresolved questions. A component owner remains responsible for its contribution through integration; narrower implementation assignments do not leave design unowned. Workers do not independently widen scope or restart parent planning.

## 4. Coordinate changes

Before concurrent implementation, establish common interface revisions, shared-artifact ownership and dependency readiness. There is no one-agent-per-layer rule.

When an interface lacks needed behavior, neighboring work is required, private internals would be needed or the assignment is insufficient, the worker sends the orchestrator the need, reasons, affected consumers/tasks, options and verification. Pause affected work; unrelated authorized work continues.

The orchestrator checks alternatives against overall requirements, consults affected owners, and decides internal changes. Record the reason; revise architecture, contracts, assignments or sequencing coherently before dependent work resumes. Give affected workers the same updated contract, coordinate provider/consumer changes, integrate and repeat affected checks. A brief existing record suffices; no per-field form or routine human approval is required.

## 5. Deliver, validate and correct

After required approval, resolve dependencies, evaluate reuse, implement and integrate continuously. **Verify** contracts and specified behavior; **validate** the integrated result against intended use through representative scenarios derived from agreed requirements. Component evidence must support its contribution; the orchestrator checks the complete user result. Local test counts, scaffolds or model agreement cannot substitute for this evidence.

For substantial work or existing review obligations, give an independent reviewer the approved baseline/deltas, relevant architecture/interfaces, actual changes and evidence. Challenge requirement coverage, design tradeoffs, coupling, authority, preservation and intended-use evidence. Findings must identify concrete failures against the agreement; preferences and illustrative scenarios do not create requirements. Correct confirmed failures, repeat affected checks and obtain re-review. Do not repeat passing work without a new change, failure or unresolved concern.

| Finding | Return path |
| --- | --- |
| Implementation defect or missing delta/preservation evidence | Correct implementation or evidence, then verify again. |
| Unknown dependency, invariant or effect | Update system understanding, impact, preservation and evidence; continue affected work. |
| Unsuitable design or material responsibility/interface/dependency change | Orchestrator revisits architecture, investigation and assignments; coordinates dependent work. |
| Repeated broad impact or boundary pressure | Reconsider whether architecture localizes change; this does not itself authorize refactoring. |
| Necessary change to overall requirements or binding constraints | Obtain the user decision below before relying on it. |
| Login, access or physical action only the user can provide | Request that targeted unblock; resume the interrupted phase. |

Internal correction and replanning remain autonomous within the agreement. Preserve new understanding and consequential decisions for subsequent work.

## When the user must decide again

Propose the exact required delta, reasons, alternatives, consequences and verification. Obtain explicit approval, preserve the original agreement and approved changes, and review affected planning. Pending or rejected changes are unauthorized.

Binding architecture/technology, external commitments, compatibility, privacy, security or acceptance cannot be weakened or relabeled internal. Check the agreement, not the file containing a promise. Changing derived worker requirements alone is not a user-requirement change. A failed check never authorizes reduced acceptance. ADAC grants no access, publication or cross-project authority.

## Completion and learning

Complete only when every required criterion and applicable independent final review passes. The substantial-work verdict records baseline, approved deltas, requirement preservation, unauthorized changes, each criterion's evidence/result and overall outcome: **PASS** requires all criteria; demonstrated failure is **FAIL**; missing required evidence is **BLOCKED**. Neither FAIL nor BLOCKED is completion. Resolve requirement disagreements rather than declaring unilateral success.

Hand off the result, consequential design/interface decisions, evidence, remaining limits and deployment/publication state. Retain useful learning in the project; changing ADAC, global rules or other projects requires separate authority.

**START → understand → assess suitability → design/investigate → review initial plan → user approval → coordinate delivery and correction → integrated evidence and required independent PASS → END.** Apply substantial-work gates proportionately; use the return paths above throughout.
