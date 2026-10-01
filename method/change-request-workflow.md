# Change requests

Use the [core](../releases/2.4.0-dev.2/core.md) to distinguish internal design decisions from binding commitments.

A request is warranted when the assignment cannot deliver its purpose using its declared scope and contracts. Send the orchestrator:

- the missing behavior or decision and why it matters;
- affected contracts, owners, consumers and dependent work;
- viable options, consequences and proposed checks.

Pause dependent work only. For example, an owner discovering that an event lacks required identity information can propose a contract change; it cannot independently redefine the event and neighboring consumers.

The orchestrator investigates alternatives and consults affected owners. For an internal revision, record the decision, distribute one updated contract and assignment, coordinate providers/consumers and repeat affected integration checks. A short existing task note suffices.

If preserving the agreed outcome, compatibility or another binding constraint is impossible, propose the precise requirement delta to the user before relying on it. An explicitly required technology remains binding; an agent-selected implementation can be revised internally. A document label cannot change that distinction.

Requests can arise during research, design, implementation or review. They feed the same correction loop rather than create another recurring approval phase.
