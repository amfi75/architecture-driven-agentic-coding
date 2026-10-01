# Read ADAC from the repository

Give the agent the repository link and your task. No installer, skill or local copy is required. Copying remains useful for offline access or customization.

## Select and read one revision

Honor an existing project pin. Otherwise resolve the requested source to an exact commit; this candidate is **2.4.0-dev.2** on `adac-2.4-system-understanding`. Retrieve actual document contents from that same commit and report the revision and documents read. A link alone supplies no instructions. If access fails or a pinned release is missing, report it; do not invent content or silently substitute a version.

Read the [core](releases/2.4.0-dev.2/core.md), understand the task and assess suitability. When ADAC applies, read the [method index](method/README.md) and the guides triggered by the work before the affected decisions. The core contains all shared commitments; guides explain their application. Consult [capability advice](releases/2.4.0-dev.2/recommendations.md) when useful. Workers receive relevant instructions and a complete bounded assignment from the orchestrator, without assumed context inheritance.

## Continued use and local copies

Session reading requires no persistent change. For continued use, when authorized, add a short reference to the project's existing agent instructions using an entry point the host actually loads:

```text
ADAC source: <credential-free repository URL>
Revision: <full commit ID>
Read <revision-specific SETUP.md URL> and its core. When ADAC fits,
use the method index to read relevant guides before affected decisions.
Preserve project requirements, permissions and pins; migrate only on request.
```

Verify saved links and distinguish session reading from persistent configuration. Neither proves future agent compliance. Local copies retain source revision, working relative links and identified adaptations. On an explicit update, review differences before changing the reference; removing ADAC means removing only its reference. Preserve unrelated instructions and copies. Global changes need their own authority.

The [standalone release](releases/2.4.0-dev.2/README.md) is another reading option. The [publication manifest](maintainer/public-files.txt) is maintainer tooling, not an installation list.
