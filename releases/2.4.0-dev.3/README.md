# ADAC 2.4.0-dev.3

Development candidate, not a stable release. Read [core 2.4.0-dev.3](core.md) at one fixed source revision for the complete method; use [capability recommendations 1.4.0](recommendations.md) when staffing work. These three files form a standalone snapshot; no required rule exists only in a guide or template.

## Use this candidate deliberately

> Apply ADAC 2.4.0-dev.3 to: [task]. Read its core at one exact source revision. Honor the project's existing pin unless I explicitly authorize migration. Understand requirements and assess suitability, then establish the project entry point and architectural/delivery records. Prepare the independently reviewed plan and obtain initial approval where substantial work requires it.

In the full repository, [SETUP.md](../../SETUP.md) explains retrieval and project records. Reading needs no installer or skill; copying the method is unnecessary but supported for offline use or customization. Project records are still required when applying ADAC. A standalone user can create them from the core's content requirements without downloading templates.

## Changes from dev.2

- Objectives lead into meaningful modularity and architectural independence for parallel work.
- A durable functional architecture maps capabilities to software components in the authoritative architecture document.
- `AGENTS.md` locates the exact method revision, architecture and delivery records. Agents recover authorized work and system understanding after context loss.
- Component owners retain research/design and integration accountability; bounded workers report to them. Capability advice distinguishes those responsibilities.
- Setup, templates, guides, diagrams and human explanations use the same conventions.
- Discovery of a newer release is separate from migration of a project.

## Migrating to dev.3

Follow the [migration procedure](../../docs/versioning-and-migration.md#deliberate-migration). Dev.3 requires these specific reconciliations:

1. Add the exact source/revision and record locations to the existing root `AGENTS.md`, preserving unrelated instructions. Create it if absent. Explicitly direct each participating agent to it.
2. Reuse equivalent architecture/delivery documents; otherwise create `ARCHITECTURE.md` and `DELIVERY.md`. Consolidate pointers, not competing architectural accounts. Preserve local material and approval history. Recover missing functional mappings from evidence; do not invent them.
3. Identify component owners separately from implementation workers. Carry forward current authority; revise reporting and assignments without assuming permission to launch extra agents.
4. Separate approved commitments from mutable progress. Record architecture and contract updates during work, with common revisions communicated before dependent work resumes.
5. Replace old copied templates only through reconciliation: architecture subsumes component/layer records; delivery subsumes intake/system-goal; task packages subsume agent/scope notes; the change-request guide contains the request format. Preserve project-specific content and evidence.

Previous 2.3.0, dev.1 and dev.2 snapshots remain unchanged. Switching instructions does not migrate product architecture, change approved requirements or activate a global default. Candidate checks are documented in [verification](../../docs/verification.md); no new demo, adoption experiment or benchmark is claimed.
