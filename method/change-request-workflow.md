# Change requests

The [core](../releases/2.4.0-dev.3/core.md) distinguishes derived decisions from protected commitments. Requests feed the existing correction loop; they do not create another approval phase.

Workers raise design-invalidating questions or insufficient scope with their component owner. The owner resolves issues within assigned discretion. Interface changes, neighboring-component work, private-internal access or changes beyond that discretion go to the orchestrator. If the orchestrator also owns the component, the route is direct.

## Request format

Use a concise message and preserve its consequential decision in the delivery record:

- requester, accountable owner and decision recipient;
- unmet behavior/requirement, current assignment or contract revision and reason;
- affected components, consumers and dependent tasks;
- proposed change, alternatives, compatibility/quality consequences and checks;
- dependent work paused and unrelated authorized work continuing.

For example, missing event identity may require a shared contract revision. A worker reports it to the owner rather than silently changing the event and consumers.

## Decision and coordination

The orchestrator consults affected owners and checks alternatives against the agreement. Record the decision, rationale, authority basis, affected contract/architecture/task revisions, owners, sequencing, recipients and verification. Communicate common revisions before dependent work resumes; coordinate providers/consumers and repeat affected integration checks. An existing task note suffices; no separate per-field form is required.

If the required result, compatibility or another binding commitment cannot be preserved, propose the exact delta, alternatives and consequences to the user. Preserve approval history and update affected planning only after approval. Pending or rejected deltas are unauthorized. An agent-chosen technology may be revised internally; an explicitly required technology cannot be relabeled internal.

Close the request with actual evidence and updated records. Research, implementation and review can all reveal further questions; route them according to responsibility and authority.
