![ADAC — Architecture-Driven Agentic Coding: modular architecture with defined interfaces](docs/assets/adac-banner.png)

# Architecture-Driven Agentic Coding

**Turn understood requirements into modular software, coordinated parallel work and an autonomously completed result.**

ADAC is a lightweight, text-only method for coding agents. A leading agent acts as orchestrator: it derives an architecture and explicit interfaces from the requirements, assigns bounded work, handles questions and changes, and integrates the result.

## Why ADAC?

1. **Build maintainable, modular software with high quality.** Clear responsibilities and explicit contracts help contain change, avoid unintended coupling and make component behavior and integration reviewable.
2. **Accelerate implementation through controlled parallel work.** Agents develop suitably independent contributions at the same time. The orchestrator coordinates dependencies, interface revisions and integration so parallel progress serves a coherent system.
3. **Finish the agreed result as autonomously as possible.** Agents implement, verify and correct continuously. The orchestrator resolves internal issues and revises the architecture or tasks as needed; the user decides again when overall requirements or binding constraints must change.

The method is readable and versionable, with no required controller, Python runtime, executable installer, provider or agent harness. Model-choice guidance stays advisory. The maintainer reports successful practical use over approximately six months, including faster implementation than single-agent work; this is practitioner experience, not a quantified comparative study.

## When does it help?

Use ADAC for work that supports meaningful modular responsibilities and defined interfaces: for example communication adapters, application logic, storage and user interaction. These are examples, not required layers or separate services. Architecture should fit the requirements, and work allocation should fit the architecture.

A local bug fix, typo or inseparable one-off task usually does not justify this coordination. More files or available agents alone are not reasons to use it. A shared-interface decision may need serial coordination before independent implementation can proceed.

For substantial change, reason from requirements to architecture. For incremental change, reason from intended delta to preserved behavior. The orchestrator maintains change-relevant system understanding throughout both; see [changes within the existing architecture](releases/2.4.0-dev.1/core.md#changes-within-the-existing-architecture).

## From requirements to a complete result

The diagram shows substantial architecture-driven work. Architecture-fitting incremental changes follow the compact guidance above with proportionate review.

![ADAC: requirements, architecture, orchestrator, parallel work and integration](docs/diagrams/workflow.svg)

Text equivalent: **START → requirements and system understanding → suitability → architecture/interfaces/tasks → independent plan review and initial user approval → orchestrator-led implementation → integration, verification and independent review → END.** Work can be parallel or serial according to dependencies. Failed checks trigger correction; internal design issues return to the orchestrator. Needed changes to overall requirements return to the user. The [loop and change-request guide](docs/agent-loop.md) shows these return paths.

The orchestrator is an agent role, not a software controller. It can implement as well as coordinate. Workers request interface or scope changes from it; they do not silently edit neighboring modules. Independent reviewers remain read-only.

## Use ADAC with your agent

Give your coding agent the repository link and your task:

> Use the ADAC 2.4 development candidate from https://github.com/amfi75/architecture-driven-agentic-coding/tree/adac-2.4-system-understanding for this task: [describe the task]. Resolve this branch to one fixed commit and read SETUP.md, the core and the applicable method guides from that commit before planning. Preserve any existing project pin unless I explicitly request migration.

The agent follows the **[reading guide](SETUP.md)**: it loads the actual documents, understands the requirements and checks whether ADAC fits. When it does, the orchestrator reads the detailed architecture and coordination guides before planning and gives workers the relevant instructions. A link alone does not mean its contents have been read.

For continued use across sessions, ask the agent to add a short pinned repository reference to your existing project instructions. With this approach, the method documents stay in the ADAC repository. For a one-off task, no persistent project change is needed.

You do not need to select files, run a command or install a skill. Direct reading needs repository access. You can also copy the documents into your project for local access, offline use or customization; copying is optional. The [core](releases/2.4.0-dev.1/core.md), [recommendations](releases/2.4.0-dev.1/recommendations.md) and **[method in detail](method/README.md)** provide the rules and practical guidance. The standalone [three-file snapshot](releases/2.4.0-dev.1/README.md) provides a compact local reading option.

## Foundations and guidance

ADAC applies established principles of modular design, information hiding, interface contracts and architecture-centered iterative development to coding agents. Read the [architecture foundations](docs/architecture-foundations.md) for sources, the specific ADAC interpretation and its limits. The [design rationale](docs/design-rationale.md) explains choices and human/AI contribution.

The [model-selection recommendations](releases/2.4.0-dev.1/recommendations.md) cover orchestration, implementation and review. They require no automatic router and do not grant permissions.

See [verification and experience](docs/verification.md) for the actual scope of evidence. This distribution contains the method, its guidance and repository support files; private project implementations and their evidence are excluded.

## Version and publication

This branch exercises **ADAC 2.4.0-dev.1**, with candidate core 2.4.0-dev.1 and recommendations 1.2.0. The released [ADAC 2.3.0 snapshot](releases/2.3.0/README.md) remains immutable; `main` remains the stable entry point. Existing projects and global installations do not migrate automatically. See [migration and rollback](docs/versioning-and-migration.md).

[MIT license](LICENSE) · [Provenance](NOTICE.md) · [Contributing](CONTRIBUTING.md) · [Optional maintainer checks](docs/maintaining.md)
