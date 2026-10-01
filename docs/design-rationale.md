# Design rationale and contribution

ADAC makes architecture useful during agentic development: requirements lead to functional responsibilities, software boundaries and interfaces, then accountable work and integrated evidence. Its objectives are maintainable high-quality software, faster parallel implementation and autonomous completion.

## Architecture guides work

Versions 2.0–2.2 removed too much concrete architectural guidance during simplification. Version 2.3 restored architecture discovery, interfaces, bounded assignments and coordinated changes without restoring mandatory layers or restrictions on authorized end-to-end ownership.

Functional architecture explains needed capabilities and relationships. Software architecture allocates them while addressing quality, constraints and existing dependencies. The mapping is many-to-many. Cohesion, information hiding and limited coupling help localize change and create independence that can be exploited for parallel work. Useful abstraction can justify additional design effort; speculative generality does not follow from modularity alone.

## Continuity needs conventions

A durable architectural account lets agents inspect, share and recover decisions. Project `AGENTS.md` identifies the method revision and authoritative architecture/delivery records. Existing equivalent documents are reused; otherwise `ARCHITECTURE.md` and `DELIVERY.md` provide predictable locations. The functional view, software architecture and their mapping belong together, with links to detailed contracts instead of duplicate accounts.

This standardizes working conventions while preserving judgment over software design. The orchestrator keeps records consistent with requirements and implementation during delivery; review tests that consistency. Recovery after compaction includes current authorized work, not merely architectural prose. Explicit reading instructions avoid assuming every harness discovers the same files automatically.

## Separate design ownership from bounded execution

A component owner may need substantial domain reasoning, original research and alternative evaluation. A worker can execute a well-defined implementation task with lighter capability. The owner evaluates and integrates delegated work and remains accountable. Workers return unresolved design questions to their owner; cross-component decisions reach the orchestrator.

This distinction supports efficient capability allocation without requiring extra agents or a mandatory model hierarchy. The orchestrator can own components and owners can implement directly. Capability recommendations stay descriptive; model strength never grants scope or permissions.

## Iteration preserves the whole result

New development establishes architecture; improvements reuse suitable decisions. Delta / Preserve / Impact / Evidence makes regression obligations explicit even when a change fits existing boundaries. Discoveries update system understanding and affected evidence; recurring broad impact prompts architectural reasoning, not automatic refactoring.

Initial substantial work receives independent plan review and user approval. Afterward internal investigation, design refinement and correction proceed autonomously. Protected requirements, compatibility, privacy, security and acceptance remain subject to explicit user decisions. Component checks and interface-correct scaffolds cannot substitute for intended-use evidence of the complete result.

## Lightweight does not mean discretionary

The complete core states the requirements. Templates give new records a consistent structure; triggered guides explain application; capability advice helps staffing. These files reduce repeated invention without making every agent preload the entire repository. Version discovery and explicit migration preserve consistency across sessions and concurrent agents.

The method needs no controller, installer, interpreter or particular provider. Project records are persistent text, not an ADAC memory runtime. These properties support portability and inspection, but do not enforce agent compliance. Checks and internal PASS reports do not establish improved engineering outcomes by themselves.

## Human and AI contribution

The maintainer defined and applied ADAC, reports roughly six months of successful use, and identified the loss of architecture-centered decomposition. He specified requirements-first work, quality/modularity, parallel implementation, autonomy, clear interfaces, meaningful review and advisory model guidance. He requested research grounding and challenged shallow component implementations, loss of iterative continuity, ambiguous owner/worker roles and excessive discretion over working conventions.

AI assisted inspection, research, drafting, diagrams, checks and independent review. Dev.3 implements the subsequent human-directed clarification of records, roles, migration and public explanation. This does not attribute every implementation line or check to the maintainer. [Foundations](architecture-foundations.md) distinguish established theory from ADAC's application; [verification](verification.md) distinguishes practitioner experience from actual candidate checks. No private project example or new performance benchmark is part of this revision.
