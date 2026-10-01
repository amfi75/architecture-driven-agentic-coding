# Architecture

Use for a new `ARCHITECTURE.md`; retain an equivalent existing document. This is the authoritative architectural account identified in `AGENTS.md`. The orchestrator maintains it with component-owner contributions. Keep affected sections current during delivery and distinguish intended design from implemented state.

## Purpose and functional architecture

- Related requirements and quality goals:
- Capabilities and their relationships; important end-to-end flows:
- Constraints, invariants and evidence for existing behavior:

| Capability / responsibility | Realizing components | Relationships / flow | Relevant acceptance |
| --- | --- | --- | --- |
| | | | |

Mappings can be many-to-many; functions do not dictate component boundaries alone.

## Software architecture and ownership

For each relevant component or coherent group, record:

- Responsibility, owner, scope and exclusions:
- Changeable decisions hidden behind its boundary:
- Allowed dependencies, prohibited dependencies and rationale:
- Interfaces/revisions, providers/consumers and links to detailed contracts:
- Private internals, observed accidental coupling and unresolved uncertainty:
- Design alternatives, selected rationale and quality/maintenance tradeoffs:
- Integration contribution, validation and implementation status:

## Decisions and evolution

Record consequential decisions with affected requirements, components, contracts, rationale and verification. Link the approved delivery baseline; distinguish binding constraints from derived design. Before dependent work resumes, reconcile affected records and communicate revisions. Keep uncertainties explicit; do not turn an inferred boundary into a verified fact.
