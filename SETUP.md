# Read and use ADAC from the repository

The recommended entry is a repository link and a task. Read the documents directly from that repository at one fixed revision. Do not install or copy ADAC into the target project by default. The filename SETUP.md is retained as the stable agent entry point; no installer, skill or runtime is required.

The [core](releases/2.3.0/core.md) defines the method. The detailed guides explain its practical application. Reading a link means retrieving and reading the actual document content, not assuming the link itself supplies the instructions.

## 1. Select an accessible, fixed revision

Use the supplied repository and honor any existing project pin or explicitly requested revision. Otherwise resolve the current source to one exact commit for this task and state it briefly. Read every method document from that same revision; a moving branch or version label alone is not a complete document pin.

Use revision-specific document links or the repository's read API with the agent's existing access. Verify that the retrieved content corresponds to the selected revision. Repository identity and stored references must not contain credentials. If access fails, report the specific access problem rather than claiming to have read the method. Do not invent content or silently substitute another version.

Existing project instructions, requirements and permissions remain authoritative. A method link does not authorize replacing a project pin, changing global configuration or starting unapproved product implementation.

## 2. Read the rules and the detailed method

First read [core 2.3.0](releases/2.3.0/core.md), understand the requested outcome and assess ADAC suitability. A local fix or inseparable task remains proportionate; the presence of an ADAC reference does not make every task an ADAC project.

When ADAC is selected, the orchestrator reads the following documents at the chosen revision **before architecture and task planning**:

- [Method overview](method/README.md)
- [Concept](method/concept.md)
- [Operating model](method/operating-model.md)
- [Components and public surfaces](method/public-surfaces.md)
- [Controlled parallel work](method/parallel-agent-workflow.md)
- [Change requests](method/change-request-workflow.md)
- [Independent review](method/review-model.md)

Use the [glossary](method/glossary.md) for terminology and consult [model/task recommendations](releases/2.3.0/recommendations.md) as adaptable advice. Use [existing-repository](bootstrap/existing-repository.md) or [new-repository](bootstrap/new-repository.md) planning guidance as applicable. Templates and archetypes are references to consult when useful, not files to install automatically.

Give each worker its derived requirements, architecture context, interface revision, scope, dependencies, acceptance and relevant method instructions. Do not assume sub-agents inherit the orchestrator's context or access. Supply the relevant text when needed so a worker need not independently fetch the whole repository. Workers request interface, neighboring-component and scope changes through the orchestrator.

For substantial work, independently review the complete initial plan and obtain user approval before implementation. Then integrate, verify, independently review and correct until the agreed result passes. Internal changes remain the orchestrator's responsibility within overall requirements; necessary changes to those requirements or binding constraints need user approval.

## 3. Distinguish this session from continued project use

For a one-off request, reading the documents is enough to establish the method context for this session. Do not create a local package or edit persistent instructions unless continued project use was requested. State the selected revision and which documents were actually read.

For continued use across sessions, add only a short pinned reference to the project's existing agent instructions, using the entry point the host actually loads. This records where future agents must read the method; it does not embed the method documents in the project. Preserve unrelated instructions and existing pins. Create a supported project instruction file only when its loading mechanism is known and the requested integration authorizes it.

A compact reference can follow this form. Replace placeholders with actual repository/revision links and verify them before saving:

```text
ADAC reference
Source: <repository URL without credentials>
Revision: <full commit ID>
Read <revision-specific SETUP.md URL> and the core before assessing ADAC
suitability. When ADAC is selected, retrieve and read the method guides
listed there before architecture/task planning; pass relevant instructions
to workers. Do not vendor ADAC or silently change this pin. Preserve the
project's requirements, permissions and existing approval gates.
```

Read back the entry and check its links. Report current-session reading and persistent integration separately. A link written to disk is not evidence that a future agent has read it, and a host without persistent instruction support must not be reported as configured for future sessions. No unperformed host/adoption test is implied.

## Access, offline use and updates

Direct reading requires repository access whenever the agent needs to load the pinned documents. If that is unavailable, explain the missing access. A local documentation snapshot is an **explicit offline alternative**, not an automatic fallback; agree that alternative with the user before copying anything. Retain the same revision and reading instructions if that alternative is chosen.

Changes upstream do not silently change the chosen revision. On an explicit update request, review the differences, preserve binding commitments and update only the relevant reference. To stop continued use, remove only the ADAC reference, not the rest of the project's instructions. Existing local copies from earlier setups are not deleted automatically. Global instructions and other projects require their own authority.

The [publication manifest](maintainer/public-files.txt) is for maintainers preparing this repository's release. It is not a list of files agents must copy into a project.
