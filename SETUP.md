# Read and apply ADAC

Give the agent the repository and task. No installer, skill or method copy is required. Reading the method is a read-only action; applying it to authorized work also establishes project records.

## Select one exact revision

1. Read the project's existing root `AGENTS.md` and honor its method pin. A missing or inaccessible pin is an unresolved dependency, not permission to substitute another version.
2. For a new unpinned project, use the latest stable release identified by the [main README](https://github.com/amfi75/architecture-driven-agentic-coding/tree/main). This branch contains **2.4.0-dev.3**, a candidate selected only by explicit request; current stable is **2.3.0**.
3. Resolve the selected reference to one exact commit and retrieve actual documents from that commit. Report the revision and documents read. A URL alone supplies no instructions. Do not mix core, guides or templates from different commits.
4. Read the selected core, understand the task and assess suitability. For this candidate, the [core](releases/2.4.0-dev.3/core.md) contains all requirements. If ADAC applies, use the [method index](method/README.md) to read explanations before the activities they cover. Read [capability advice](releases/2.4.0-dev.3/recommendations.md) when staffing or revising assignments.

Checking for an update reports availability; it does not change the project pin. An explicit upgrade follows [migration](docs/versioning-and-migration.md#deliberate-migration).

## Establish the project records

For selected, authorized ADAC work, retain existing equivalent architecture and delivery documents. Otherwise create `ARCHITECTURE.md` and `DELIVERY.md` using the [architecture](templates/architecture.md) and [delivery](templates/delivery.md) templates. Keep one authoritative account; link detailed contracts and records rather than copying them into multiple places. Do not create empty paperwork or invent missing architecture. Read-only evaluation and tasks that do not use ADAC do not require these writes.

Add this block to the project's root `AGENTS.md`, replacing placeholders with actual paths and a credential-free source. Preserve unrelated instructions; create the file if absent.

```text
ADAC source: <repository URL>
ADAC revision: <full commit ID>; core: <release/version>
Architecture: <authoritative document path>
Delivery: <authoritative document path>
Read the pinned core and these records before starting or resuming ADAC work.
Recover the approved agreement, relevant architecture and your authorized task.
Use only relevant sections; investigate discrepancies before affected changes.
Follow the method index at the same revision for applicable explanations.
Do not migrate the method or approved commitments without explicit authority.
```

The architecture record contains functional capabilities, relationships, software components, their mapping, responsibilities, dependencies, interfaces, rationale and constraints. Delivery separates exact approved commitments/approval history from changing assignments, progress and evidence. New work starts with proposed requirements; never label them approved until approval exists.

The orchestrator explicitly directs participating agents to the entry point; do not assume harness auto-discovery. Owners give workers bounded requirements, design, context, checks and a reporting route. Reopening a conversation or receiving a summary does not replace recovering current records. Independent reviewers receive the exact review baseline and remain read-only.

## Local copies and version changes

Copying the method is supported for offline access or customization. Preserve source revision, working links and identified local adaptations; the [standalone snapshot](releases/2.4.0-dev.3/README.md) is self-contained. Copying method files and maintaining project records are separate activities. Verify recorded source access and project paths; neither proves future agent compliance.

Follow the existing migration guide to upgrade or roll back. Global instruction changes require separate authority. Removing an ADAC reference does not authorize deleting the project's architectural knowledge or approval evidence. Maintainer scripts and the publication manifest are not installation requirements.
