# A repository link and a task

Give your coding agent this request, replacing the task description:

> Use ADAC from https://github.com/amfi75/architecture-driven-agentic-coding for this task: [describe the task]. Read SETUP.md, the core and the applicable method guides directly from one fixed repository revision before planning.

The [reading guide](../SETUP.md) tells the agent which documents to retrieve and read. It assesses suitability from the requirements, then reads the detailed method before architecture and task planning when ADAC is selected. Workers receive their task context and relevant instructions from the orchestrator.

Reading the documents provides context for the current session. For continued use across sessions, ask for a short pinned reference in the project's existing agent instructions. Reading from the repository needs no installation. Copying the documents is optional and useful for local access, offline use or customization.

For suitable work, use [existing repository](existing-repository.md) or [new repository](new-repository.md) planning guidance. Substantial work still needs the complete independently reviewed plan and initial user approval defined by the core. Reading the method does not authorize implementation by itself.
