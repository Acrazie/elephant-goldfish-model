<!-- Modified by Acrazie on 2026-11-03 for the independent EGM fork. -->

# Using EGM

EGM designs architectural changes before implementation. For a small clear bug,
use your normal coding workflow. Install the complete plugin using the
[host setup guide](harnesses.md). EGM requires an explicit command; ordinary
conversation does not start it automatically.

## Start once

Select `egm-design` with an idea, an agreed architecture or an existing document.
In Claude Code and Antigravity CLI use `/egm:egm-design`; in Codex use the skill
picker. For example: “Design the separation of ingestion and processing in this
project.” Read the active host guide for exact invocation and support limits.

The agent inspects the project, clarifies only missing material decisions with
recommendations, and updates an existing relevant design or one canonical document.
It adapts to your starting point; no minimum interview, compulsory brief or repeated
section approvals. Say “draft only, no review” to limit the mandate to writing.

The initial mandate includes scope, delegated edits and review coverage. The agent
then coordinates independent fresh-context review and authorized corrections.
Only material choices or blocking ambiguity interrupt work. You approve the final
content; production implementation requires a separate mandate outside EGM.

## Four public commands

- [egm-design](../skills/egm-design/SKILL.md): adaptive design through review.
- [egm-review](../skills/egm-review/SKILL.md): independently review an existing
  document; read-only unless you authorize corrections.
- [egm-drift-report](../skills/egm-drift-report/SKILL.md): compare documented
  commitments with current source, without requiring every code detail in prose.
- [egm-bootstrap](../skills/egm-bootstrap/SKILL.md): targeted documentation for
  a demonstrated reader need, not a README for every directory.

Exploration, drafting, resolution and iteration are internal capabilities, not
separate public commands. This is a breaking command change without aliases.
Existing documents are not deleted or migrated automatically; explicitly select
one as input rather than relying on old automatic artifact discovery.

## Useful persistence

Keep decisions, affected contracts/invariants, scope, verification, relevant risks
and compact revision-bound review state. Do not create duplicate brief/draft/final
files, per-agent reports, empty sections or an index by default. Intermediate
findings are temporary; ask explicitly for a separate export when useful.

On a new session, pass the canonical document. The agent must verify current source
and review coverage rather than infer approval from a filename or old clean result.
Missing required reviewers or source access means incomplete verification.

[Execution rules](../resources/execution_instructions.md) and
[review procedure](../resources/review-workflow.md) own the detailed invariants.
See [testing and limits](https://github.com/google/elephant-goldfish-model/blob/main/TESTING.md); static checks are not model behavior proof.
