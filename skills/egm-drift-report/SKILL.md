---
name: egm-drift-report
license: Apache-2.0
disable-model-invocation: true
description: Compare documented architectural commitments with current code and return actionable differences, without requiring exhaustive documentation or a report file.
---

<!-- Modified by Acrazie on 2026-11-03 for the independent EGM fork. -->


# EGM Drift Check

When running in Codex or ChatGPT Work, first read [Codex integration](../../docs/codex.md).
In Claude Code or Cowork, read `${CLAUDE_PLUGIN_ROOT}/docs/claude.md` first.
Read and apply `resources/execution_instructions.md`.

Accept an explicitly selected document or directory and optional source scope.
Ask only if the target is absent or ambiguous. Read the relevant documents and
current source, not cached assumptions. Distinguish approved commitments, proposed
but unimplemented changes, superseded designs and descriptions of current behavior.
A proposed design is not automatically an implemented baseline; ask if its status
cannot be established before declaring a missing implementation a regression.

Compare only the contracts, invariants, boundaries and constraints the selected
documents actually commit to. Verify cited existing symbols; proposed Create paths
need not already exist. Undocumented code alone is not drift. Do not demand an
inventory of helpers, all logic or unrelated test infrastructure.

Report concrete discrepancies with document/source locations, observed behavior,
expected commitment and impact. Missing source access is a verification limit,
not proof of agreement. If no differences are established, say so with the checked
scope and limits. Recommend whether a discrepancy needs a human decision; do not
choose silently between changing intent and changing code.

Return concise results without a report file by default. Export only on explicit
request to an authorized destination. Never modify code or documentation as part
of the check. A separate mandate is required for document corrections; production
implementation remains outside EGM.
