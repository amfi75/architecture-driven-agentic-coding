# The method in detail

These pages explain ADAC's architecture and working practices in more detail. The [ADAC 2.3 core](../releases/2.3.0/core.md) contains the complete shared commitments; [model/task recommendations](../releases/2.3.0/recommendations.md) are adaptable advice. These pages are written for agents as well as developers. The recommended [repository-reading workflow](../SETUP.md) instructs the orchestrator to retrieve and read the six working guides before architecture and task planning when ADAC is selected. Consult the glossary as needed; workers receive guidance relevant to their assignments. The guides explain the core rather than add a separate set of commitments.

Start with requirements, assess whether meaningful modular decomposition helps, then derive architecture, interfaces and work packages. A leading agent orchestrates implementation, worker change requests, integration and verification. The delivery loop supports that architecture-driven work.

## Reading guide

| Page | What it explains |
| --- | --- |
| [Concept](concept.md) | The three goals, architectural decomposition and when ADAC is useful. |
| [Operating model](operating-model.md) | The complete path from requirements and initial planning to autonomous delivery and handoff. |
| [Components and public surfaces](public-surfaces.md) | Responsibilities, information hiding, dependencies and semantic interface contracts. |
| [Controlled parallel work](parallel-agent-workflow.md) | Readiness for fan-out, complete worker assignments, coordination and integration. |
| [Change requests](change-request-workflow.md) | How workers request interface, neighboring-component or scope changes, and how the orchestrator resolves them. |
| [Independent review](review-model.md) | Plan and result review, concrete evidence, correction and acceptance. |
| [Glossary](glossary.md) | Shared terms, including overall requirements, derived decisions and the orchestrator role. |

## Related practical guidance

Use [bootstrap](../bootstrap/README.md) to start in a new or existing repository and the [task-package template](../templates/task-package.md) for a worker assignment. The [loop guide](../docs/agent-loop.md) illustrates return paths; the [architecture foundations](../docs/architecture-foundations.md) explain the theoretical sources and their application to agents.

For the recommended direct-reading workflow, use the [agent reading guide](../SETUP.md). The [three-file release](../releases/2.3.0/README.md) provides a compact local reading option; copying and customization are optional. For current evidence and its limits, see [verification](../docs/verification.md).
