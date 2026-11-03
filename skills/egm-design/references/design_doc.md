<!-- Modified by Acrazie on 2026-11-03 for the independent EGM fork. -->

# Useful design content

This is content guidance, not a required heading layout. Keep a single maintained
source; update a relevant existing design rather than creating a duplicate.

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
