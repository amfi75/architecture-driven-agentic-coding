# Interface contract

Use this format when creating an interface record; link it from the authoritative architecture document. Retain equivalent existing contracts. Use enough detail for compatible independent work.

## Identity and purpose

- Name, revision and related requirement:
- Type: function, class, data object, event, CLI, database view, file convention, configuration, prompt, shared fixture or other:
- Owner/provider:
- Consumers and dependent tasks:

## Data and behavior

- Input and output shape:
- Preconditions:
- Success behavior and postconditions:
- Error cases and recovery expectations:
- Relevant invariants, identity, ordering and ownership:
- Valid and invalid examples:

## Dependencies and compatibility

- Public assumptions consumers may rely on:
- Private details consumers must not depend on:
- Compatibility obligations and their source:
- Binding user/external commitments versus derived internal decisions:
- Verification cases:

## Revision coordination

- Change decision and authority:
- Affected providers/consumers and current common revision:
- Integration checks and actual results:

Workers raise issues with their component owner; shared-interface changes go to the orchestrator. It can revise derived internal contracts while preserving overall requirements; binding commitments require the corresponding user decision. Update affected records and inform owners and workers before dependent work resumes.
