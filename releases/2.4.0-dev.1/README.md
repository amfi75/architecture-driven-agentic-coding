# ADAC 2.4.0-dev.1

Development candidate for live project experimentation, not a stable release. A portable text method for architecture-driven agentic coding. Core 2.4.0-dev.1 and task/model recommendations 1.2.0 are separate: the [core](core.md) defines the method; [recommendations](recommendations.md) describe adaptable capability and working-practice advice.

## Three goals

1. Build maintainable, modular software with high quality through explicit responsibilities and interface contracts.
2. Accelerate implementation through controlled parallel work, coordinated and integrated by a leading agent.
3. Complete the agreed outcome autonomously, returning to the user for necessary changes to overall requirements or binding constraints.

## When to use it

Use ADAC where the requested work supports meaningful modular decomposition and manageable dependencies. Communication adapters, business logic, persistence and user interaction are possible responsibilities, not mandatory layers. A modular monolith can fit. Small local fixes and inseparable tasks usually need no ADAC setup. Decide from requirements before assigning agents.

## Five-minute start

Read these three files together at one fixed candidate revision: README.md, core.md and recommendations.md. Optionally copy them into a folder such as `adac/` for local use or customization. No installation, script, controller, model binding or private instructions are needed. The five minutes are for understanding and starting, not a promise about delivery duration.

Give the leading agent this prompt:

> Read this snapshot's core.md and consult recommendations.md for model/task guidance. My requested outcome is: [describe it]. First understand and clarify the requirements and success criteria; inspect the existing system. Decide whether meaningful modular boundaries make ADAC useful. If so, derive the initial architecture, responsibilities, interface contracts and dependent or independent work packages. Separate binding requirements from changeable implementation choices. For substantial work, independently review the full plan and present it for my initial approval. After approval, act as orchestrator: give workers derived requirements, interfaces, scope and acceptance criteria; coordinate their change requests; integrate and verify the complete result. Revise internal architecture and tasks autonomously. Return to me for necessary changes to overall requirements or binding constraints, or a targeted external action only I can perform. Finish with observable evidence and any required independent review. Keep small local work proportionate.

For changes fitting the existing architecture, use the core's [incremental-change guidance](core.md#changes-within-the-existing-architecture). The orchestrator maintains change-relevant understanding and checks both the intended delta and preservation; small changes do not acquire the substantial-work gates.

## How substantial work flows

START → understand requirements and the relevant system → decide suitability → architecture and interfaces → task assignments → initial independent plan review and user approval → orchestrator-led implementation (parallel where useful) → integration, verification and correction → independent final PASS against all requirements → END.

Workers send interface or scope requests to the orchestrator. It coordinates internal revisions and updates affected assignments before work resumes. Implementation errors loop to implementation; internal design problems loop to architecture/task planning. Only needed changes to overall requirements or binding constraints reopen the substantive user decision. A required login or access action is a targeted unblock. The [core](core.md) defines these routes fully.

## What an assignment contains

Give each worker its contribution to the overall result; required behavior and quality; relevant architecture and interface revision; inputs/outputs and dependencies; authorized edits; acceptance criteria and reporting expectations. The orchestrator owns uncovered cross-cutting work and integration. Passing every local task is not automatically passing the whole system.

A software interface contract defines data and behavior between components. The Delivery Contract records overall requirements and authority. Neither a draft architecture diagram nor a worker assignment automatically becomes an unchangeable user requirement.

## What successful use looks like

Requirements can be traced to component responsibilities and assignments. Workers can use agreed interfaces without depending on neighboring implementation details. Their questions reach an orchestrator able to coordinate changes. The integrated result satisfies the agreed behavior and quality, with actual evidence and independent review rather than unresolved failures.

## Version and limits

The 2.4 candidate extends 2.3 with explicit ownership of system understanding and proportionate reasoning about safe incremental change. The dev.1 designation separates this experimental revision from a stable release. The released 2.3 snapshot remains unchanged. Earlier pins remain authoritative until deliberately migrated. If a pinned version is missing, surface that issue; do not silently replace it. This text package supplies no runtime enforcement and assumes agents can follow the instructions and access authorized tools. Higher-priority instructions and permissions still apply. No comparative model benchmark is claimed.
