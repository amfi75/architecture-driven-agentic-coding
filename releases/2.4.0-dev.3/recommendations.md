# Task and capability recommendations 1.4.0

Advice for [ADAC core 2.4.0-dev.3](core.md). The core defines authority; these recommendations guide efficient staffing, not a compulsory router or automatic model assignment. Consult them when assigning roles or reconsidering inadequate results.

| Responsibility | Useful capabilities | Context to supply |
| --- | --- | --- |
| Orchestrator | Sustained system reasoning, architecture tradeoffs, coordination, integration and reliable tools. | Overall agreement, functional/software architecture, cross-cutting requirements and delivery state. |
| Component owner | Domain reasoning, critical research, alternative evaluation, design and intended-use validation. Complex components may require original research. | Purpose, quality goals, system fit, interfaces, design discretion and unresolved questions. |
| Worker | Reliable implementation, instruction following, relevant tools and interpreting checks. A lighter/faster model can suit a well-defined task. | Established design, bounded edits, contract revisions, acceptance and reporting route to the owner. |
| Independent reviewer | Challenging assumptions, tracing evidence and constructing concrete counterexamples in fresh read-only context. | Approved baseline/deltas, relevant architecture, actual changes and evidence. |

Match capability to difficulty, not lines of code. Concentrate demanding reasoning on consequential decisions; make those decisions explicit enough for bounded workers to implement. Owners evaluate and integrate worker results and retain accountability. They can implement directly when delegation costs more than it helps. An orchestrator can also own components; more agents do not resolve a shared design uncertainty.

Choose among available models using reasoning, tool reliability, relevant context capacity, latency and cost. If results are inadequate, improve context or decomposition, return unresolved design questions to the owner, or recommend a capability change through authorized controls. Do not invent identity, silently switch models, expand authority or weaken acceptance. A reviewer remains read-only.

Record model/version and reasoning settings when material to cost or reproducibility. Specific model names belong in dated advice with exact identifiers and sources, distinguishing documented capability from observed experience. Unknown models receive no automatic ranking or prohibition.
