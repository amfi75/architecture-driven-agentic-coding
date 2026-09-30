# Task and capability recommendations 1.2.0

Compatible with ADAC core 2.4.0-dev.1. These model-selection and working-practice recommendations are advisory. They do not route requests automatically, select a compulsory profile or alter permission. Read the [core](core.md) for the method and roles.

## Match capability to responsibility

| Assignment | Useful capabilities | Recommendation |
| --- | --- | --- |
| Orchestrator, requirements and architecture | Sustained reasoning across dependencies; recognizing ambiguity; evaluating alternatives; reliable tool use and integration | Use an available model that can hold the system context and follow through. Supply requirements, architecture rationale, interface contracts and evidence, not just a list of subtasks. |
| Bounded implementation | Reliable editing and instruction following; relevant language/domain knowledge; ability to run and interpret checks | Use a model appropriate to the package's difficulty. A smaller or faster model can suit well-specified routine work; consequential or ambiguous tasks may need stronger reasoning. Keep the same acceptance criteria. |
| Interface change and integration | Cross-component reasoning, compatibility analysis and diagnosis | Keep responsibility with the orchestrator. Consult affected workers, revise contracts and check the whole result. Escalate model capability as needed through the available authorized controls, not by widening a worker's scope. |
| Independent review | Challenging assumptions, tracing evidence to requirements, finding concrete counterexamples | Use a suitably capable reviewer in fresh context with read-only authority. Give it the agreed requirements, interfaces, diff and actual results. A different model name alone does not make a review independent. |

## Apply the advice without a router

1. Understand the task, role, relevant context and risks.
2. Choose among models actually available in the user's harness, considering reasoning, tool reliability, context capacity, latency and cost.
3. Provide the assignment and a checkable result. Adapt the amount of guidance to observed performance and task ambiguity.
4. If performance is insufficient, improve the context or assignment, or recommend a model change. Do not invent identity, silently switch models, or weaken requirements to match a model's limits.

Record the model/version and reasoning setting when they matter to reproducibility, cost or a material change. No binding manifest, interpreter, resolver or model-selection form is required. Unknown models are not prohibited and receive no automatic capability ranking.

Specific model names may be supplied in a dated project recommendation with the exact identifier, source and whether the recommendation is based on documentation or local experience. This portable edition deliberately makes no provider-specific ranking. The capability guidance is usable with any provider; actual availability and suitability must be checked in the task environment.

## Control parallelism

The purpose of parallel work is faster progress on genuinely separable contributions. Start only ready packages with compatible interfaces and manageable coordination needs. Adding workers to coupled work can create rework. The orchestrator can combine or resequence assignments and implement parts itself. Availability of more agents is not a reason to split the architecture.

Retain an accessible architecture map and shared contracts while giving each worker only the relevant working context. Never use reduced context to hide requirements it must satisfy. Give workers an explicit route to ask for interface or scope changes.

Authority stays fixed: workers remain bounded, reviewers remain read-only, and the orchestrator preserves overall requirements. None of this advice overrides an explicit project pin, higher-priority instruction or user/tool permission.
