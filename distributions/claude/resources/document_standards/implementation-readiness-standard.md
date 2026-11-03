<!-- Modified by Acrazie on 2026-11-03 for the independent EGM fork. -->

# Implementation Readiness Standard

A competent engineer or fresh session can implement the approved architectural
change without guessing material contracts, invariants, ownership or safeguards.
Internal local reversible implementation choices remain delegated; do not require
every private signature, helper or algorithmic detail to be predetermined.

## Target Scope & File Boundary

State the approved write boundary, using repository-relative paths for affected
owners and exact files when needed to prevent unrelated edits. Distinguish Create,
Modify and Delete where applicable. This is not an exhaustive directory inventory.
The implementation stage must not expand that boundary without authorization.

## Required evidence

- Resolved public behavior, data contracts, failure semantics and structural choices.
- Actionable changes and verification cases for success, failure and applicable
  security, compatibility, concurrency, migration and rollback risks.
- A safe order of changes where ordering matters, keeping intermediate states
  buildable/testable when applicable. Do not invent phases for a trivial change.
- Open material questions, verification limits and explicit accepted risks.

Reject consequential ambiguity or missing safeguards, not absent template headings.
A design is not ready while required coverage or material decisions remain open.
