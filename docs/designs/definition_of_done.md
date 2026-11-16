# Definition of Done for implementation handoffs

Status: proposed; human approval pending.

## Objective and scope

Make every design produced or updated by `egm-design` contain an explicit
**Definition of Done** that a separate implementation agent can use to determine
whether the approved contract is fulfilled, through PR delivery after human
validation. Success means the agent can distinguish work remaining from evidence
remaining and publication awaiting authorization without guessing from prose.

### Goals

- Turn the design's objectives, contracts and preserved invariants into observable
  acceptance criteria and corresponding verification evidence.
- Define implementation completion and PR delivery separately from design approval.
- Preserve human review, repository governance and EGM's design-only boundary.

### Non-Goals

- Implementing, committing or publishing within `egm-design`.
- Adding an implementation command, shipping automation, a new report or a schema.
- Requiring merge, deployment, exhaustive helper specifications or new tooling.
- Automatically rewriting existing designs outside the selected target.

## Current behavior and ownership

The [design skill](../../skills/egm-design/SKILL.md) already establishes success
criteria, contracts and expected verification. Its
[content guidance](../../skills/egm-design/references/design_doc.md) makes the
heading layout optional. Neither requires a dedicated delivery contract.
The [shared execution rules](../../resources/execution_instructions.md) prohibit
implementation and publication; design approval does not authorize either.
The [review procedure](../../resources/review-workflow.md) already owns independent
coverage and revision binding. Reuse those rules rather than duplicating review
or adding an execution engine.

## Proposed contract

Require a `Definition of Done` section in every canonical design created or
updated by `egm-design`, using the document's language. Keep other headings
adaptive. An existing equivalent section can be renamed and completed in place;
do not duplicate acceptance criteria or create a separate contract file.

For each in-scope objective and material contract/invariant, record an observable
acceptance criterion and the evidence needed to establish it. Include relevant
failure and regression cases, not merely the happy path. Specify actionable
checks and expected outcomes; defer reversible test implementation details.
Where tests cannot establish a criterion, name the manual or external evidence
and responsible validator. Derive criteria from agreed scope; a completion
checklist cannot introduce extra features or waive required safeguards.

Describe the handoff as three distinct gates:

1. **Design approved:** the exact design revision has completed its required
   independent coverage, resolved material decisions and received human approval.
   Drafting-only results remain explicitly unreviewed. This gate alone authorizes
   neither implementation nor publication.
2. **Implementation verified:** under a separate implementation mandate, all
   acceptance criteria are met within approved write boundaries, with actual
   verification after the final relevant changes. Record the checked source
   revision or content digest, commands or manual checks, observed outcomes and
   limits. Required checks that fail, are blocked or are not run prevent this
   gate. A genuine non-applicable check needs a rationale; changing a required
   criterion or accepting a material risk requires an explicit human decision
   and affected review revalidation, not silently checking it off.
3. **PR delivered:** after human review of the actual implementation and its
   evidence, testing and explicit publication approval, create or update the PR
   using repository rules and the required template. Record the verified PR URL
   and head revision. A local commit, push or PR link alone does not prove the
   implementation contract. Report pending or failed required remote checks;
   do not claim full delivery while those checks remain unresolved.

The default delivery endpoint is the PR, not merge or deployment. Repository
restrictions, contribution tracks, required issues/labels and design prerequisites
still apply. Missing permissions, credentials or human decisions mean blocked or
awaiting approval, not success. The implementation agent reports the highest gate
actually reached and remaining conditions. It must not stop at a plan or partial
implementation when authorized work remains, nor cross an approval boundary to
finish. Substantive design changes invalidate affected coverage and approvals;
implementation edits invalidate affected evidence and human validation before
publication. Reuse unchanged evidence only when its scope still applies.

## Implementation boundary

A separately authorized implementation may modify:

- `skills/egm-design/SKILL.md`: require the section and distinguish the three gates
  while retaining the design-only completion boundary.
- `skills/egm-design/references/design_doc.md`: own the detailed content guidance,
  referenced by the skill rather than repeated in full.
- `skills/egm-design/test_scenarios.yaml` and `skills/egm-design/TEST.md`: add focused
  native scenarios and verification instructions for the delivery contract.
- `tests/unit/test_adaptive_workflow.py`: add minimal static coverage for the new
  requirement and scenario presence without claiming behavioral proof.

No other runtime owner, dependency or public command needs to change. Update the
skill and its guidance together, then their tests. Existing unselected documents
remain unchanged; resumed selected designs acquire the section before a new
ready verdict, with affected coverage revalidated.

## Definition of Done

For the implementation of this proposal:

- A newly authored or resumed design contains the delivery section with explicit
  criteria, evidence and the three gates. Native scenarios inspect actual files
  and agent actions for both paths, not only the final response.
- A failing or unrun required check prevents verified completion. A changed source
  revision triggers affected revalidation. Native scenarios cover both cases.
- Design approval alone does not start implementation or publication. An
  implementation that passes local checks but lacks human validation waits before
  PR creation. Native scenarios check both approval boundaries.
- After human validation and explicit publication approval, a separately mandated
  implementation agent can deliver the PR and report its head and remote checks.
  Exercise this in an authorized disposable repository; absent authorization or
  capability, report this required evidence as not run, not passed.
- Run `pytest tests/unit` after the final implementation edits. Passing offline
  tests proves packaging/static constraints, not native agent behavior. Native
  runs require separate quota/installation authorization under the existing
  [behavioral verification instructions](../../skills/egm-design/TEST.md).
- Before publication, satisfy this repository's contribution track, issue/design
  prerequisites and [PR template](../../.github/PULL_REQUEST_TEMPLATE.md). Human
  accountability remains for the human to attest. No merge or deployment needed.

## Review and approval metadata

Digest domain: UTF-8 bytes before the `## Review and approval metadata` heading.
Reviewed body SHA-256:
`e0ffa1c76c5a69d88c4f2598d6a57574eca22062e6b8a6527bb0a48ac30b572f`.
Selected source baseline: local HEAD
`4a94df184ba4a0df53740777d7bdf10e7e3102f3`; selected sources were unmodified.
One fresh-context design critic completed the target, persona, feature-spec,
zoom-out and implementation-readiness standards, selected source rules and
scenario/testing owner reads. Coverage: fit, observable acceptance, approval and
publication boundaries, failure/resume behavior and implementation readiness.
No Blocker, Major or Nit findings. No material accepted risks or open decisions.
Limits: read-only design review, not implementation or native behavioral proof.
Fresh conversation isolation does not establish host instruction-file exclusion.
Human approval: granted on 2026-11-16 in this chat for the reviewed body
digest above. Implementation and publication remain separately authorized actions.

Current status: human-approved design; local implementation applied, native
behavioral verification outstanding. This supersedes the review-time status in
the design body without changing the approved contract.
Implementation and offline testing were separately authorized on 2026-11-16.
The human also authorized synchronizing the two generated copies under
`distributions/claude/skills/egm-design/` (`SKILL.md` and
`references/design_doc.md`), required by the existing packaging consistency test.
Offline verification: `uv run --offline --no-project --with pytest==8.3.5 --with
pyyaml==6.0.2 python -m pytest tests/unit`: 340 passed, 2 skipped. Skips are the
opt-in Copilot loader and Cursor bundle probes. `git diff --check` passed.
Six focused native delivery scenarios and separate implementation-leg instructions
were added; native quota/installations and disposable-remote publication were not
authorized or exercised. Those required behavioral checks remain not run, so full
implementation verification and PR delivery are not claimed. No commit or PR.
