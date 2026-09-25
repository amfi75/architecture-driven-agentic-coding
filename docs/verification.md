# Verification and practical experience — ADAC 2.3.0

This document records the verification scope for ADAC 2.3.0. Using this release does not automatically activate it in global agent instructions. Private project implementations, data and associated verification records are not part of this distribution.

## What has been checked

The method restores requirements-driven architecture, explicit interfaces, bounded worker assignments and orchestrator coordination. Verification covers method/documentation consistency, version and link checks, generic private-reference checks, visual inspection of the diagrams and banner, and independent read-only review against the agreed requirements.

Text review covers an additional internal field, a revised worker assignment, conflicting shared interfaces, an unsuitable internal design, dropping promised offline use, failed acceptance and a necessary login. These are checks of written rules, not simulated deliveries or adoption experiments.

The [repository-reading guide](../SETUP.md) is checked as documentation. No new agent adoption trial, demonstration, fixture or benchmark was performed for this correction. Static checks and independent review do not establish that every agent follows the method or that it is universally effective.

## Practical experience

The maintainer reports roughly six months of successful practical use, including faster implementation than single-agent work. Acceleration through controlled parallelism is an explicit goal alongside maintainability/quality and autonomous completion. No invented speedup ratio, controlled benchmark or project-specific measurement is claimed.

## Portability and limits

The method consists of Markdown instructions with no required provider, operating system or executable runtime. This is a property of the method, not a claim that every host or model has been tested. Direct repository reading depends on document access. Parallel execution, tool use and independent review depend on the agent host's capabilities and actual permissions.

Optional Python maintainer checks help maintain this repository; they are not needed to read or apply ADAC. A local documentation copy is optional and can support local access, offline use or customization. Reading in one session and configuring a reference for future sessions are different outcomes; neither is a claim of a completed cross-host adoption test.

See [maintaining](maintaining.md) for repository checks and [design rationale](design-rationale.md) for the human and AI contributions.
