# Versioning and migration

## Available versus selected

The [main README](https://github.com/amfi75/architecture-driven-agentic-coding/tree/main) is the stable discovery entry point; current stable is **2.3.0**. This branch contains candidate **2.4.0-dev.3**, with recommendations **1.4.0**. Candidates are explicit opt-ins, not automatic replacements for stable releases.

A project uses the exact commit recorded in its root `AGENTS.md`. New unpinned use resolves the stable entry point unless a candidate is explicitly requested. Checking availability does not change a pin. Read core, advice, guides and templates from the same commit; do not combine a pinned core with newer guides. Report an inaccessible or missing pin rather than silently substituting content. See [setup](../SETUP.md).

Core obligations and advisory recommendations have separate versions; advice cannot change authority. Updating any selected package revision is deliberate, including advice-only updates. Existing project adaptations remain identifiable alongside their source. Historical snapshots are immutable; a branch name alone is not a reproducible method pin.

## Deliberate migration

An explicit upgrade request authorizes assessing and applying a compatible method migration. It does not authorize altering approved product commitments or global instructions.

1. **Establish source and target.** Read the current pin, exact target commit, both methods, target release notes and local adaptations. Record the prior reference and preserve the existing records/adaptations for rollback.
2. **Assess the project impact.** Compare obligations, records, roles, reporting routes and approval/review rules. Identify active assignments and architecture or approval information that is missing or inconsistent. Recover missing information from evidence rather than fabricating it.
3. **Resolve conflicts.** Preserve approved requirements, permissions, compatibility and acceptance. Propose any necessary protected delta explicitly; unresolved or rejected conflicts block the affected migration. Preserve legitimate local adaptations and explain reconciliations. Do not rewrite product architecture merely to fit a method template.
4. **Coordinate the transition.** Stop issuing affected assignments and pause dependent work at a recoverable point. Record current progress. Reconcile project records and instructions, preserving approval history. Ensure active owners, workers and reviewers will use the same target revision; restart/rebrief contexts that cannot reliably adopt it. Do not mix old and new rules during coordinated work.
5. **Verify and activate.** Check accessible pinned documents, record paths, role routes, approved-baseline preservation and consistency of changed instructions. Apply required project review proportionately. Only after conflicts are resolved and preparation is verified, switch the `AGENTS.md` pin, record authorization and the source-to-target change, and rebrief participating agents before resuming.

Use the current delivery record to preserve migration decisions and evidence; no migration runtime, skill, additional contract type or mandatory new file is needed. A migration that changes binding commitments retains the existing explicit approval rules. The [dev.3 notes](../releases/2.4.0-dev.3/README.md#migrating-to-dev3) list its record and role changes.

## Rollback

Restore the preserved method reference and reconcile affected instructions/records, coordinating active agents as for an upgrade. Preserve architectural knowledge, project adaptations and approval evidence. Verify the restored pin and reporting paths before resuming. A method rollback does not revert software changes, undo approved requirements or justify weakening acceptance. Global defaults and other projects remain unchanged unless separately authorized.

## History and provenance

Versions 2.0–2.2 simplified away too much architectural guidance. Version 2.3 restored requirements-driven architecture, interfaces and controlled fan-out while preserving autonomous internal changes. Dev.1 made system understanding and safe incremental change explicit; dev.2 clarified design investigation and compacted reading; dev.3 adds durable conventions and distinct owner/worker responsibilities.

The private source history and excluded project evidence remain outside this distribution. Released 2.3.0 and the dev.1/dev.2 snapshots remain unchanged. Copies for offline access or customization retain exact source revision and identified adaptations; no local copy is removed or migrated automatically.
