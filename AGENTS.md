# Working in this repository

The [ADAC 2.3 core](releases/2.3.0/core.md) defines the method; [model/task recommendations](releases/2.3.0/recommendations.md) are advisory. Preserve the current approved task contract and any explicit project pin.

Start with requirements. Use ADAC for meaningful modular work, not merely because multiple agents are available. The leading agent orchestrates architecture, bounded worker assignments, change requests and integration; it may also implement. Workers stay within their assignments; independent reviewers remain read-only.

For substantial engineering, independently review the full initial plan and obtain user approval before implementation. Afterward revise internal architecture, interfaces and assignments autonomously while preserving overall requirements and binding constraints. Return to the user for needed changes to those requirements, not every internal decision. Existing permissions and external unblocks still apply.

Preserve immutable releases, historical evidence and unrelated work. This repair is method/documentation work: no new demo, adoption experiment or benchmark, and no alteration of existing demo code/tests. Use relevant existing maintainer checks; they are not prerequisites to adopting ADAC. Private records and historical tooling are outside the public package. Publication and global activation require their own authority.
