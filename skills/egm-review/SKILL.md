---
name: egm-review
license: Apache-2.0
disable-model-invocation: true
description: Independently review an existing design with risk-based fresh-context coverage, without starting a new design or editing without a mandate.
---

<!-- Modified by Acrazie on 2026-11-03 for the independent EGM fork. -->


# EGM Review

When running in Codex or ChatGPT Work, first read [Codex integration](../../docs/codex.md).
In Claude Code or Cowork, read `${CLAUDE_PLUGIN_ROOT}/docs/claude.md` first.
Read and apply `resources/execution_instructions.md` and
`resources/review-workflow.md`; the latter owns dispatch, findings, correction
authority, revalidation, persistence and stop conditions.

Accept a target file and optional review scope or selected reading list. If the
target is missing or ambiguous, ask for it; do not guess from old artifacts.
Read the target and identify the smallest complete risk coverage. A document
need not use fixed headings or feature/implementation line-range splits.
Review an explicitly selected early concept as such, without claiming readiness.

The default mandate is read-only review. Return concise findings in chat without
a report file. Do not write a new design, update status, fix findings or persist
review state without authorization. If the user authorized corrections, perform
only those within the mandate and follow the shared revalidation procedure.
Export a separate report only on explicit request to a confirmed destination.

Do not request a preset, per-stage approval or permission to continue after an
unchanged mechanical transition. Ask only for material decisions or missing
authority. Preserve reviewer failure and fresh-context limitations in the result.
