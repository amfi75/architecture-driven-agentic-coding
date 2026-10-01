# Task and capability recommendations 1.3.0

Compatible with ADAC core 2.4.0-dev.2. Advice is adaptable; the [core](core.md) defines authority. No automatic routing, compulsory profile or model assignment is supplied.

| Assignment | Useful capabilities and context |
| --- | --- |
| Orchestration and architecture | Sustained reasoning across requirements, dependencies and tradeoffs; maintaining system understanding; integration and reliable tools. Supply the overall agreement and relevant evidence. |
| Component design and investigation | Domain understanding, critical source evaluation, comparison of alternatives, recursive design, uncertainty recognition and intended-use validation. Supply purpose, quality expectations, system fit and explicit design discretion. Match capability to design difficulty, not anticipated lines of code. |
| Bounded implementation | Reliable editing, instruction following, domain/tool knowledge and interpreting checks. A faster/smaller model may suit a well-understood task; consequential ambiguity can require stronger reasoning. |
| Contract change and integration | Cross-component reasoning and compatibility analysis. Keep system-wide decisions with the orchestrator and consult affected owners. |
| Independent review | Challenging assumptions, tracing evidence and finding concrete counterexamples, in fresh read-only context. |

Choose among models actually available, considering reasoning, tool reliability, relevant context capacity, latency and cost. If results are inadequate, improve context or assignment, or recommend a capability change through authorized controls. Do not invent model identity, silently switch models or weaken acceptance. Role names and model capability never expand scope; a worker remains bounded and a reviewer read-only.

Record model/version and reasoning settings when material to reproducibility or cost. Specific model names belong in dated project advice with exact identifiers, sources and a distinction between documentation and observed experience. Unknown models receive no automatic ranking or prohibition.

Retain an accessible architecture map and contracts. Give workers the relevant subset with enough purpose and context to avoid local optimization at the system's expense. Combine roles or run serially when appropriate; extra workers cannot repair an unresolved shared design decision. Component ownership requires the ability to reason about design, or an explicit design assignment retained by the orchestrator.
