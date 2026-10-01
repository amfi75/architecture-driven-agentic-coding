# Independent review and acceptance

The [core](../releases/2.4.0-dev.3/core.md) defines independence, gates and verdicts. Review attempts to falsify delivery of the agreed result; it remains read-only.

Supply the exact approved requirements/deltas, relevant architectural record and interfaces, assignments, actual changes and evidence. Initial review examines the complete plan; final review examines the integrated outcome. Use the [review format](../templates/review-report.md) for a new record.

## Questions that expose gaps

- Do functional/software mappings and boundaries follow behavior, quality, constraints and hidden decisions rather than folders or available agents?
- Do architectural records agree with implementation and distinguish proposed decisions from implemented state? Can relevant work resume from the entry point and delivery records?
- Were consequential uncertainties investigated with defensible alternatives and evidence? Are unresolved questions being presented as settled?
- Does each component have an accountable owner? Do bounded workers have established requirements/design and the right reporting route? Who evaluates their output, integrates it and covers cross-cutting outcomes?
- Do contracts agree on semantics, errors, invariants and compatibility? Have private coupling or protected commitments been relabeled?
- Is the claimed impact plausible beyond edited files? Do observations establish intended use, the requested delta and relevant preservation, rather than only scaffold or interface correctness?
- Did current decisions reach affected owners and workers before dependent work resumed? Were confirmed failures corrected and rechecked?

Ground findings in requirements, evidence, impact and remedy. Preferences and illustrative scenarios do not create new acceptance requirements. Missing required review/evidence or failed integration cannot become PASS. Apply existing obligations proportionately; local tasks do not automatically inherit substantial-work gates.
