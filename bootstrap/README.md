# Start work with ADAC

Give your coding agent the repository link and task using the prompt in the [main README](../README.md#use-adac-with-your-agent). It follows [SETUP.md](../SETUP.md) and reads the documents directly at one fixed revision. No copying into the project is needed; a local copy is also an option for offline use or customization. A short persistent project reference is optional for continued use across sessions.

The guides in this folder explain planning actual work. The [core](../releases/2.4.0-dev.1/core.md) defines the method and [method/](../method/README.md) explains its application. The [initial prompt](initial-prompt.md) is the same repository-reading entry point.

First understand the requested outcome and assess ADAC suitability. When selected, the orchestrator reads the detailed method guides before architecture and task planning. Then use [existing repository](existing-repository.md) or [new repository](new-repository.md) guidance. Templates and archetypes are practical references, not mandatory formats, layers or installed files.

## Useful planning outputs

Capture the overall requirements and acceptance, existing repository map, responsibilities and dependency map, affected interface contracts, uncertainties, work packages and integration/review plan. Optional [templates](../templates/project-intake.md) help when a compact single record would be insufficient. There is no required document layout or one-document-per-component rule.

Keep binding requirements distinct from derived architecture and task decisions. For substantial work, independently review the complete initial plan and obtain user approval before implementation. Reading the method or producing a plan does not grant product-change authority. After approval, the orchestrator works through implementation and correction without repeated phase approvals.

## Ready to implement?

A worker should be able to identify its derived behavior, overall requirement, relevant component interfaces, allowed changes, dependencies, verification and change-request recipient. The orchestrator should be able to explain whole-system coverage, why parallel assignments are independent and how they will be integrated.
