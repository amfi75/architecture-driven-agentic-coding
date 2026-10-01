# Independent review and acceptance

The [core](../releases/2.4.0-dev.2/core.md) defines review independence, gates and verdicts. Review attempts to falsify delivery of the agreed result.

## Inputs

Supply the exact approved requirements/deltas, relevant architecture and interface decisions, assignments, evidence and actual changes. Initial review evaluates the proposed complete plan; final review evaluates the integrated outcome. Missing evidence must remain visible.

## Questions that expose gaps

- Do boundaries follow required behavior, quality, constraints and hidden decisions, rather than folders or agent availability?
- Were consequential uncertainties investigated? Do evidence and tradeoffs support the selected design? Are remaining unknowns being mistaken for resolved ones?
- Does every delegated component have purpose, derived requirements and accountable design ownership? Who covers integration and cross-cutting outcomes?
- Do interfaces agree on semantics, errors, invariants and compatibility? Has private coupling or a protected commitment been relabeled?
- Do observations exercise intended use and relevant preservation? Could an interface-correct scaffold still fail the user scenario?
- Did changed assumptions reach every affected owner and consumer? Were confirmed failures corrected and rechecked?

Ground each finding in a criterion, evidence, impact and remedy. Distinguish a defect from a new preference. Illustrative scenarios help investigate agreed behavior; they do not authorize added requirements.

Use the optional [review report](../templates/review-report.md). Missing review, missing evidence or failed integration cannot become PASS. Apply existing obligations and the core's proportionality; small local tasks do not automatically require the substantial-work gates.
