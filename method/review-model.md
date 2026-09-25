# Independent review and acceptance

Review checks whether architecture and implementation deliver the agreed outcome. It is not a compliance score for paperwork. The [core](../releases/2.3.0/core.md) governs the gates.

## Independence and inputs

For substantial work, use an independent read-only reviewer before initial plan approval and at final acceptance. A fresh agent context or a separate human can provide independence. The implementing orchestrator's own checks are useful but are not independent review; merely switching model names does not establish it.

Provide the requirements and exact approved revision/deltas, relevant architecture and interface decisions, task assignments, actual changes and evidence. Plan review includes the initial architecture, interfaces, sequencing, integration and observable acceptance. Repair confirmed blocking/high gaps and re-review before presenting the initial plan for user approval.

## Review questions

1. Does the decomposition follow requirements and meaningful responsibilities? Are important alternatives and quality tradeoffs understood?
2. Do interfaces describe behavior, errors and invariants, with compatible assumptions across providers and consumers?
3. Are private internals respected, dependencies controlled and changes within authority? Was a protected commitment silently reclassified?
4. Do worker assignments cover derived requirements, scope, dependencies and acceptance? Who owns integration and cross-cutting needs?
5. Does the complete behavior satisfy acceptance? Inspect actual outputs and relevant adversarial cases, not only test counts or worker claims.
6. Were reuse and external dependencies handled proportionately? Are real limitations and missing evidence visible?
7. Did internal change requests reach the orchestrator and all affected consumers receive the same contract revision?
8. Are confirmed findings corrected and affected checks repeated? Are claims of completion or publication supported?

A reviewer must not introduce personal preferences, speculative risks or future productization as new requirements. Findings need a criterion, concrete evidence, impact and remediation. Scope can be inspected from the diff; no scope checker or interpreter is required to use ADAC.

## Verdict and correction

Record baseline, approved deltas, requirement preservation, unauthorized changes, each criterion's PASS/FAIL/BLOCKED evidence and overall verdict. Missing required evidence is BLOCKED; a demonstrated required failure is FAIL. PASS requires all required criteria. Neither missing independent review nor incomplete integration may become a passed gate.

The orchestrator repairs implementation defects and revises unsuitable internal designs autonomously, then obtains affected re-review. A necessary overall-requirement change goes to the user. Resolve factual or requirements disagreements with evidence rather than unilaterally declaring success.

A [review report](../templates/review-report.md) is optional. Keep project lessons without assuming authority to change ADAC, global policies or other repositories.
