# ADAC core 2.4.0-dev.3

Architecture-Driven Agentic Coding turns understood requirements into modular software and coordinated agent work. It pursues three objectives:

- **Software quality:** clear responsibilities and meaningful interfaces make software easier to maintain, adapt and reuse where useful.
- **Implementation speed:** architectural independence enables controlled parallel development of components or component groups.
- **Autonomous completion:** agents investigate, implement, evaluate and correct until the complete agreed outcome is achieved.

ADAC standardizes architecture records, ownership, coordination, evidence and continuity while leaving software design to engineering judgment. Its portable text specification requires no controller, router, interpreter, installation or particular provider. Agents follow its instructions; text does not enforce them. Higher-priority instructions, actual permissions and project pins apply. [Recommendations](recommendations.md) guide capability selection and working practices; they grant no authority. Use the project’s exact recorded revision consistently. Newer releases do not activate automatically. On an explicit upgrade request, compare revisions and local adaptations, resolve conflicts without weakening approved commitments, coordinate active agents, update affected records and verify the new pin. Preserve the previous reference and adaptations; reverting the method does not undo software changes.

## 1. Understand the outcome and the system

Understand intended use, behavior, quality, constraints, non-goals and observable acceptance before choosing components or agents. Resolve material requirements ambiguity with the user. The **Delivery Contract** records these overall requirements, authority, the exact approved revision and approved changes.

The **orchestrator** maintains system understanding and owns architecture, assignments, shared decisions, integration, cross-cutting requirements and the complete result. It may also implement within its authority.

For existing software, use and check available knowledge against relevant implementation and behavior. Trace affected responsibilities, dependencies, flows, contracts and invariants until plausible impact can reasonably be bounded and completion evidence identified. Investigate gaps before affected implementation; exhaustive repository understanding is unnecessary. Carry this understanding forward and update it throughout delivery.

Use ADAC where meaningful responsibilities and explicit interfaces support coordinated development with manageable dependencies. A modular monolith can qualify. Small local fixes, routine inspection and inseparable tasks usually need ordinary proportionate practices; size, folders or available agents alone do not justify ADAC.

For ADAC work, the project's root **`AGENTS.md` is the entry point**. It identifies the applicable ADAC version/source, the authoritative architecture and delivery documents. Reuse existing equivalent documents; otherwise create **`ARCHITECTURE.md`** and **`DELIVERY.md`**. Maintain one authoritative architectural account, linking detailed contracts rather than duplicating them. The delivery document separates approved requirements and approval history from mutable assignments, progress, unresolved decisions and evidence. Preserve the exact approved baseline and deltas as progress changes. Use the supplied standard templates for new records; in the standalone package, use the content requirements here. Retain equivalent existing records. Templates add no obligations. Preserve existing project instructions; the method itself need not be copied into the project.

The orchestrator ensures setup and delegation explicitly direct agents to this entry point; do not assume automatic discovery. On starting or resuming work, including after context compaction, read it and recover the relevant architecture, requirements, authorized assignment and current delivery state. Investigate discrepancies before affected work; conversation summaries alone are insufficient. Load the portions needed for the assignment, not the entire project history.

## 2. Establish or refine the architecture

Architecture gives work coherent boundaries. Derive them from required capabilities and behavior together with quality requirements, constraints and existing design. Functions need not map one-to-one to components; a component need not be a service, folder or layer.

The architecture document contains the **functional view and software architecture together with their mapping**: capabilities, relationships, allocation to components, rationale and constraints, including functions spanning components. The orchestrator owns consistency with requirements and implementation; component owners contribute findings and updates. Check affected records against implementation before changes. Distinguish agreed design from implemented state while work is underway.

Group cohesive responsibilities, hide changeable implementation decisions and limit coupling through meaningful interfaces. Favor boundaries that localize change, support maintenance and appropriate reuse, and allow components or groups to be developed independently. Justified design effort serves these goals; do not add speculative abstractions or universal portability without a relevant need. Record responsibilities, ownership, dependency direction and rationale.

Specify affected **interface contracts**: inputs, results, semantics, errors, invariants, compatibility and revisions. Include non-code surfaces such as events, CLI output, configuration and prompts. Distinguish intentional contracts from accidental access to private internals. Preserve suitable architecture; refine affected decisions as evidence develops.

Investigate consequential uncertainty before dependent implementation. The assigned owner frames the decision and criteria, examines existing solutions and established approaches, compares viable alternatives and records the rationale. Research externally when knowledge is missing; use focused experiments when needed and authorized. Stop when evidence supports a defensible choice and remaining uncertainty has a verification path. Routine work needs no study. The orchestrator retains boundary decisions and may delegate investigation. Do not lower acceptance to proceed.

**For incremental change**, identify **Delta**—intended behavior change; **Preserve**—relevant behavior that must remain; **Impact**—plausibly affected responsibilities, dependencies, contracts, invariants and workflows; and **Evidence**—checks of both change and preservation. Capture these proportionately in existing records, without a new template. A change can fit the architecture and still have significant regression risk. Characterize relevant behavior before modification when executable coverage is insufficient; revisit architecture only where warranted.

## 3. Organize accountable, parallel work

Derive assignments and acceptance from requirements and architecture. Exploit independent boundaries for parallel work; settle shared decisions, interface revisions, shared-artifact ownership and dependency readiness before concurrent implementation. Assign integration explicitly. There is no one-agent-per-layer rule.

A **component owner** is accountable for an assigned component or coherent component group: investigation, design, implementation, verification and its contribution through integration. It receives:

- purpose, contribution to the complete result, functional and quality requirements, constraints and observable acceptance;
- relevant architecture, interface revisions, inputs, outputs and dependency readiness;
- authorized edits, exclusions, shared ownership and design discretion;
- investigation questions, checks, reporting and a change-request route to the orchestrator.

A **worker** executes a bounded task delegated by an owner where authorized. The owner supplies the relevant requirements, established design and interfaces, permitted edits, acceptance checks and reporting route. Workers inspect surrounding context, implement and verify within that scope, and report changed behavior/files, decisions, actual check results and unresolved questions to the owner. Return questions that invalidate the design or exceed the assignment to the owner; do not invent architectural answers, widen scope or restart parent planning. Delegation does not transfer the owner's accountability; the owner evaluates and integrates the contribution.

Match capability to responsibility: complex component ownership can require substantial reasoning and original research; well-defined worker tasks can use less costly models with sufficient implementation capability. Owners may implement directly when delegation adds no value. The orchestrator may also own components; roles do not require separate agents or one agent per component. Model recommendations are adaptable advice, not a mandatory router; stronger models do not expand authority or permissions.

The orchestrator checks whole-requirement coverage, including cross-cutting outcomes. At each delegation, supply relevant instructions and context explicitly rather than assuming inheritance. A file list is insufficient. Preserve review independence when combining responsibilities.

For substantial work, an **independent reviewer** challenges the complete initial plan: requirements, architecture/interfaces, assignments, reuse, dependencies, sequencing, evidence and acceptance. Review is read-only, using a separate human or fresh agent context; self-review or changing model names is insufficient. Resolve blocking/high findings and re-review, then obtain user approval and record the exact revision before implementation. Missing review or approval is an unmet gate. Small changes do not inherit these gates merely because ADAC is referenced.

## 4. Deliver and correct autonomously

After required approval, resolve dependencies, evaluate reuse, implement and integrate continuously. **Verify** contracts and specified behavior; **validate** the integrated result through representative intended-use scenarios derived from agreed requirements. Owners evidence their contributions; the orchestrator checks the complete user result. Scaffolds, local test counts or model agreement cannot substitute for this evidence.

Use findings to direct the next action:

| Finding | Action |
| --- | --- |
| Implementation defect or missing change/preservation evidence | Correct implementation or evidence and repeat affected checks. |
| Unknown dependency, invariant or effect | Expand system understanding; revise impact, preservation and evidence; continue. |
| Unsuitable design, interface or assignment | Revisit affected architectural decisions and coordinate dependent work. |
| Repeated broad impact, preservation failures or boundary pressure | Reconsider whether architecture localizes change; this does not automatically authorize refactoring. |
| Necessary change to agreed requirements or protected commitments | Follow the user-decision rule below before relying on it. |
| User-only access or physical action | Request that targeted unblock, then resume. |

Workers raise design or scope problems with their component owner. The owner resolves them within its assigned discretion; interface changes, neighboring work, access to other components' private internals or changes beyond its authority go to the orchestrator with the need, reasons, affected consumers/tasks, options and verification. Pause affected work while unrelated authorized work continues. The orchestrator consults affected owners, decides authorized internal changes and updates the authoritative architecture, affected contracts and delivery records coherently, including reasons, assignments and sequencing. Communicate the same revised decisions and contract revisions to affected owners and their workers before dependent work resumes; coordinate provider/consumer changes and repeat affected integration checks. Record new findings and progress as delivery proceeds so another context can resume reliably.

These iterations remain autonomous within the agreement. An increment passing does not complete a larger approved outcome, and revisiting internal design does not create another human gate.

## 5. Preserve the agreement

Agent-chosen architecture, internal interfaces and assignments are **derived decisions**, revisable within approved boundaries. Appearing in a plan does not itself make a decision binding. Internal coordination needs no per-field approval form.

Changes to overall requirements or binding architecture/technology, external commitments, compatibility, privacy, security or acceptance require explicit user approval. Propose the exact delta, reasons, alternatives, consequences and verification; preserve the original agreement and approved deltas and review affected planning. Pending or rejected deltas are unauthorized.

Check the commitment, not its location: do not weaken or relabel protected requirements as internal. Changing derived worker requirements alone need not change overall requirements. Failed checks never authorize reduced acceptance. ADAC grants no access, publication or cross-project authority.

## 6. Demonstrate completion and retain understanding

Completion requires the complete agreed outcome: **the intended delta is satisfied and relevant affected behavior is preserved**. Every required acceptance criterion and applicable independent final review must pass.

For substantial work or existing review obligations, provide the independent reviewer with the approved baseline/deltas, architecture/interfaces, actual changes and evidence. Check affected functional allocations and consistency between requirements, architectural records and implemented behavior. Challenge coverage, design tradeoffs, coupling, authority, plausible impact, preservation and intended-use results. Findings must identify concrete failures against the agreement; preferences or illustrative scenarios do not create requirements. Correct confirmed failures and obtain re-review. Repeat passing checks only when new changes, failures or unresolved concerns warrant it.

The substantial-work verdict records the baseline, approved deltas, requirement preservation, unauthorized changes and each criterion's evidence/result. **PASS** requires all criteria; demonstrated failure is **FAIL**; missing required evidence is **BLOCKED**. Neither FAIL nor BLOCKED is completion. Resolve requirement disagreements rather than declaring unilateral success.

Hand off results, consequential decisions, evidence, remaining limits and deployment/publication state. Ensure the architecture and delivery records reflect the verified result and retain understanding needed for subsequent work. No ADAC memory system is required. Retain useful project learning; changing ADAC, global rules or other projects requires separate authority.
