# Component or layer responsibility

The filename is retained for familiarity. A component need not be a horizontal layer or a separate service. This optional record describes architecture, not a mandatory agent assignment.

- Name and related requirements:
- Responsibility and quality goals:
- Owns:
- Does not own:
- Implementation decisions hidden behind interfaces:
- Public surfaces, providers/consumers and revisions:
- Private internals:
- Allowed dependencies:
- Prohibited dependencies and reasons:
- Known accidental coupling or uncertainty:
- Key design alternatives and rationale:
- Component and integration verification:

The orchestrator derives work packages from these responsibilities and their dependencies. It may implement across authorized internal components; workers remain bounded by their assignments.
