<!-- Modified by Acrazie on 2026-11-03 for the independent EGM fork. -->

# Useful design content

Only the Definition of Done section is required; keep other headings adaptive.
Keep a single maintained source; update a relevant existing design rather than
creating a duplicate.

Keep information needed to decide, preserve a non-obvious constraint, verify the
change or resume safely. Usually this means:

- The problem, desired outcome, success criteria and meaningful scope boundaries.
- Affected public behavior, contracts, invariants and integration ownership.
- Structural decisions and why; real rejected alternatives only when the trade-off
  helps a future reader. No invented options to satisfy a rubric.
- Actionable change boundaries and expected verification, including failure paths.
  Name exact write boundaries when needed to prevent adjacent implementation
  edits; a directory inventory or recipe for every private helper is not required.
- Unresolved material questions and risks, plus migration/rollback or other
  safeguards where applicable. Do not imply optional security validation.
- Review state: content revision, scope/coverage, incomplete reviews, open material
  findings, accepted risks and decisions awaiting the human. Preserve intent
  approved earlier so later edits cannot silently replace it.

Use verified references to existing source and documentation. Distinguish current
behavior from proposed changes; absent proposed files are not broken references.
Diagrams, glossaries, indexes, extra resources and sections are conditional on
actual reader need. Omit empty sections, repeated summaries, speculative future
work, process transcripts and exhaustive descriptions already available in code.

A plan is ready when material contracts and decisions are resolved and verification
is actionable, not when it eliminates every local implementation choice. Record
status honestly: draft, reviewed with limits, or human-approved for a specific
revision. Approval is not authorization to implement or publish.

## Definition of Done

Include this section, translated into the document's language, when creating or
updating a design. Complete or rename an equivalent existing section rather than
duplicating criteria. On resume, add missing content before a new ready verdict
and revalidate affected review coverage. Do not rewrite unselected designs.

For each in-scope objective and material contract or preserved invariant, define
an observable acceptance criterion, actionable checks and expected outcomes.
Include relevant failure and regression cases. Where automated tests cannot
establish a criterion, name the manual or external evidence and responsible
validator. Reference existing criteria rather than repeating them. Do not add
scope or waive safeguards through this checklist.

Separate the delivery gates for the implementation agent:

- **Design approved:** required independent coverage and material decisions are
  complete, and the human has approved the exact revision. Drafting-only work
  remains unreviewed. Neither implementation nor publication is authorized.
- **Implementation verified:** under a separate mandate, all criteria are met
  within approved write boundaries. Record actual checks after the final relevant
  edits, source revision or digest, observed outcomes and limits. Failed, blocked
  or unrun required checks prevent this gate; justify genuinely non-applicable
  checks. Changing a criterion or accepting a material risk requires an explicit
  human decision and affected review revalidation, not a silent waiver.
- **PR delivered:** after human review of the actual implementation and evidence,
  testing and explicit publication approval, create or update the PR under
  repository rules and its required template. Record the verified URL and head
  revision. Report required remote checks; pending or failed checks prevent full
  delivery. A commit, push or PR link alone does not prove the contract.

The default endpoint is the PR, not merge or deployment. Preserve contribution
tracks, issue/label requirements and design prerequisites. Missing permissions,
credentials or human decisions mean blocked or awaiting approval, not success.
Report the highest gate reached and remaining conditions. Continue authorized
work until its criteria are satisfied; do not stop at a plan or partial work,
and do not cross an approval boundary to finish. Substantive design changes
invalidate affected review coverage and approvals; implementation edits invalidate
affected evidence and human validation before publication. Reuse unchanged
evidence only while its scope still applies. These handoff conditions do not
change EGM's design-only boundary.
