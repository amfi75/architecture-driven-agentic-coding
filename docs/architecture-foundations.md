# Architecture foundations

ADAC applies established software architecture ideas to coordinated coding agents. It does not claim to invent modularity or prove that agents always produce better software. The [core](../releases/2.3.0/core.md) is self-contained; these sources explain the design rationale rather than add required reading or hidden rules.

## Information hiding and meaningful modules

David Parnas's 1972 paper distinguishes decomposition around hidden design decisions from a division that simply follows processing steps. ADAC uses that principle when selecting responsibilities, private internals and declared dependencies. A directory or a horizontal layer is not automatically an independent work package. [Parnas, On the Criteria To Be Used in Decomposing Systems into Modules](https://doi.org/10.1145/361598.361623).

The agent-specific adaptation is to turn those boundaries into assignments and shared contracts. The paper does not prescribe coding-agent roles or establish an agent speedup.

## Requirements and quality drive architecture

The Software Engineering Institute's Attribute-Driven Design method derives architecture from requirements, including quality attributes, functionality and constraints, and refines the design iteratively. ADAC therefore starts with requirements, explains architectural choices through quality needs, and develops affected interfaces before dependent implementation. It does not require a complete frozen design before learning from code. [SEI, ADD Version 2.0](https://sei.cmu.edu/library/attribute-driven-design-add-version-20/) and [ADD collection](https://www.sei.cmu.edu/library/attribute-driven-design-method-collection/).

ADAC is a lightweight adaptation, not a claim to implement every ADD activity or provide ADD certification. The orchestrator can revise derived architecture while preserving the agreed overall requirements.

## Contracts describe behavior as well as shape

Bertrand Meyer's Design by Contract makes obligations and guarantees explicit through preconditions, postconditions and invariants. ADAC uses these ideas when describing component inputs, results, errors and invariants so separately developed contributions share expectations. [Eiffel, Design by Contract introduction](https://www.eiffel.com/values/design-by-contract/introduction/).

A Markdown interface description is not a formal proof or automatic runtime enforcement. ADAC's **Delivery Contract** is a separate organizational agreement about requirements, scope and acceptance; it should not be confused with a software interface contract.

## Multiple views and scenario-based integration

Philippe Kruchten's 1995 “4+1” model separates architectural concerns and uses scenarios to relate and validate the views. ADAC takes the practical lesson that a component map alone is insufficient: task allocation, dependencies, runtime interaction and user scenarios must agree. [Kruchten, The 4+1 View Model of Architecture](https://arxiv.org/pdf/2006.04975) (1995 paper, later author upload).

ADAC does not mandate five diagrams. It uses only the views needed for the task, and assigns integration and cross-cutting requirements explicitly to the orchestrator.

## Communication follows architecture

Melvin Conway's 1968 essay connects system structure with the communication structure of the organizations designing it. ADAC applies this as an analogy: worker responsibilities, declared interfaces and a direct change-request channel should support the intended architecture. The orchestrator maintains a whole-system view and coordinates shared changes. [Conway, How Do Committees Invent?](https://melconway.com/Home/Committees_Paper.html).

This is a design rationale for agent coordination, not empirical proof that Conway's observations transfer unchanged to AI agents. More agents alone do not establish useful parallelism.

## Decisions remain explainable as designs evolve

Michael Nygard's short architecture decision records capture context, decisions, status and consequences. ADAC uses proportionate decision notes to explain interface changes and design revisions without requiring a form for every field. Superseded decisions remain traceable. [Nygard, Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).

Parnas and Clements also distinguish a useful rational design explanation from the messy reality of discovery. ADAC preserves actual chronology and evidence while documenting the resulting rationale; it does not invent a linear success story. [Parnas and Clements, A Rational Design Process: How and Why to Fake It](https://jpaulgibson.synology.me/~jpaulgibson/TSP/Teaching/Teaching-ReadingMaterial/ParnasClements86.pdf).

The public description of ISO/IEC/IEEE 42010 provides broader context for architecture descriptions. ADAC makes no conformance claim; the full standard was not used as a normative checklist. [ISO/IEC/IEEE 42010:2022 overview](https://www.iso.org/standard/74393.html).

## What these foundations support

The sources explain why ADAC emphasizes requirements, information hiding, explicit contracts, coherent work allocation, iterative integration and preserved rationale. The orchestrator role, bounded agent packages, autonomous internal change decisions and read-only agent review are ADAC's application of those ideas.

Faster implementation through controlled parallel work is an explicit goal. The maintainer reports approximately six months of successful use including speed gains. That experience is distinct from both architectural theory and a controlled comparative study. See [verification and experience](verification.md) for the evidence boundary.
