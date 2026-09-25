# Glossary

- **Overall requirements / Delivery Contract:** the agreed outcome, behavior, quality, binding constraints, non-goals, acceptance and authority; preserve its approved revision.
- **Architecture:** component responsibilities, dependencies, interfaces and the reasons for their organization.
- **Component:** a coherent responsibility that hides internal decisions. It may be a module, part of a layer or a service; no deployment style is prescribed.
- **Layer:** an optional architectural organization by responsibility and dependency direction. It is not automatically an agent assignment.
- **Public surface / interface contract:** behavior and data a provider makes available to consumers across a boundary, including errors and relevant invariants. “Public” does not alone determine change authority.
- **Private internals:** decisions another component should not depend on directly.
- **Orchestrator / owner / coordinator:** the leading agent responsible for architecture, task coverage, coordination, change decisions, integration and completion; it may implement within authority.
- **Worker / sub-agent:** an agent following a bounded assignment with derived requirements and acceptance.
- **Reviewer:** an independent read-only evaluator of plan or result.
- **Derived requirement / decision:** behavior required of a component or a design/task choice derived from overall requirements. The orchestrator can revise it while preserving those requirements.
- **Task package:** the goal, architecture context, behavior, interfaces/revision, dependencies, edit scope, acceptance and reporting expected of a worker.
- **Change request:** a worker's request to the orchestrator to resolve an interface, neighboring-component or assignment problem.
- **Controlled fan-out:** simultaneous work on suitable assignments with coordinated dependencies, common contracts and integration ownership.
- **Binding constraint:** an actual agreed obligation, such as offline use, compatibility, privacy or a specified technology. It is not silently changeable as an implementation detail.
- **External unblock:** an action or access only the user can supply; it does not itself restart requirements planning.

For the complete rules, use [core 2.3.0](../releases/2.3.0/core.md).
