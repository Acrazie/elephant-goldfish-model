<!-- Modified by Acrazie on 2026-11-03 for the independent EGM fork. -->

# Independent review and resolution

This is the shared review procedure for design and standalone review. Read
`resources/execution_instructions.md` and the active host guide first. The primary
agent owns dispatch, synthesis, authorized corrections and integration; reviewers
are read-only. Do not add a supervisor layer or duplicate reviewers by default.

## 1. Bind the target and coverage

Read the actual target and any explicitly selected source context. Bind the
reviewed revision using a content digest or immutable revision, not line numbers
alone. Hash the substantive design body, excluding only the explicitly marked
review/approval metadata section; include all contracts, decisions and risk
premises. Record that digest domain so a new session can reproduce it. Updating
metadata alone does not invalidate coverage; substantive edits always do. Bind
selected source contracts to their inspected revision or digest as well. For an
uncommitted design, digests are sufficient; do not make a commit.
If the content changes during review, stop acceptance and invalidate the affected
coverage until the changed content is reviewed. Separate new proposed behavior
from claims about existing code.

Select the smallest complete coverage from concrete risks. The default is one
fresh reviewer reading `agents/design_critic.md` and the feature-spec, zoom-out
and implementation-readiness standards in `resources/document_standards/`.
It checks architectural fit, comprehension, contracts, failure behavior and
implementation readiness together, not five sequential stages. For an explicitly
early concept, mark implementation readiness as not assessed; do not claim ready.

Add only relevant independent specialists: `agents/codebase_details.md` for
uncertain source contracts; `agents/implementation_readiness.md` for migration,
data loss, compatibility or rollout risk; `agents/comprehension.md` when a
self-contained handoff is uncertain. Security-sensitive changes require explicit
security and authorization coverage by a capable reviewer. If that capability or
any required expertise is unavailable, report incomplete coverage rather than
silently omitting it. Structural or style review is not a mandatory separate pass.
Tell the user the intended coverage as part of the initial mandate, not a preset
selection gate. Respect host capacity and user-approved delegation/model budgets.

## 2. Dispatch directly in fresh contexts

Use the host's native fresh-context mechanism and read-only reviewer profiles.
Pass absolute paths to persona, target, selected standards and necessary source
reading list; pass objective and scope, but not the parent conversation, private
reasoning, memory or answers the document must explain. Do not resume an old
reviewer. Fresh conversation context does not prove exclusion of host instruction
files; retain the host guide's isolation limitations.

Each reviewer must read its persona, target and every supplied standard and return:

- The reviewed revision and scope, completed reads and material evidence limits.
- Concrete findings: severity (Blocker, Major, Nit), location, failure scenario,
  violated contract and supporting source evidence. Missing document detail is a
  finding only when it leaves a material decision, risk or verification ambiguous.
- Coverage completed and coverage not run. A timeout, inaccessible resource,
  failed required read or missing completion is **not run**, never zero findings.

Verify actual native completion/read evidence when exposed. Do not substitute
parent-authored status for tool evidence. If fresh review is unavailable, stop the
review and report the limitation. A same-context critique is not a Goldfish review.
Do not retry or widen delegation without an applicable budget.

## 3. Resolve within the mandate

Collect results in temporary structured returns or private host scratch, not
per-stage workspace files. Deduplicate findings by affected contract and scope.
Prioritize substantive failures; Nits and harmless template deviations do not
block. Correct local, reversible document defects only if edits are authorized.
For structural trade-offs, changed intent or accepted risks, present a recommended
decision and wait for the human. The reviewer never implements its own fixes.

Preserve settled decisions and accepted risks with their scope and rationale.
Do not reopen them without changed premises or new evidence. A claimed fix is
not a settled risk: independently check that the defect was actually removed.
Keep open material findings, decisions pending, required coverage, reviewed
revision and evidence limits in a compact review-state section of the canonical
design when writes are authorized. For a read-only review, return that state in
chat; if cross-session persistence is needed, ask for an authorized destination.

## 4. Targeted revalidation and stop

After corrections use targeted revalidation of affected contracts and regression
scope in a fresh context. If changes invalidate an architectural premise, include
all dependent contracts; do not call a local reread a full review. Do not require
two consecutive clean rounds or rerun unchanged lenses by default.

Stop when the planned coverage is complete and no unresolved, unarbitrated
Blocker or Major remains on the current content. Accepted risks require explicit
human decisions; neither a cap nor elapsed budget accepts them. If correction
and revalidation fail to converge, stop with open findings and ask the human.
No automatic retry loop or success after reviewer failure.

Present a concise final result: target/reviewed revision, coverage and failures,
open material findings, accepted risks and any missing validation. A changed
revision cannot inherit an old clean verdict. Preserve sufficient state for a
new session to avoid repeating settled decisions or assuming unreviewed edits
were accepted. A separate consolidated report is an explicit export, not a
default deliverable. Final design approval remains the human's responsibility.
