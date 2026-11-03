---
name: egm-bootstrap
license: Apache-2.0
disable-model-invocation: true
description: Create or update targeted architectural documentation only for an identified reader need, preserving existing content without mirroring every directory or symbol.
---

<!-- Modified by Acrazie on 2026-11-03 for the independent EGM fork. -->


# EGM Targeted Documentation

When running in Codex or ChatGPT Work, first read [Codex integration](../../docs/codex.md).
In Claude Code or Cowork, read `${CLAUDE_PLUGIN_ROOT}/docs/claude.md` first.
Read and apply `resources/execution_instructions.md`.

## Scope and safety

Require a target path and reader need. Inspect existing documentation before
proposing a new file. A root path is not permission to generate a README for every
directory. Propose the smallest useful document set and confirm write destinations
in the initial mandate. Never modify production source, stage, commit or install.
Preserve human content and confirm destructive replacement rather than rewriting
whole files. Follow the host guide for destinations outside the workspace.

Discover only the selected scope. Do not follow symlink directories or walk
outside the authorized root. Exclude generated, dependency, hidden/system and
test-only trees unless expressly relevant; respect .gitignore and .egmignore.
If discovery exceeds 15 directories without an already explicit full-tree mandate,
ask to narrow or authorize that scope before continuing. Scope expansion is a real
permission decision, not approval at every mechanical transition.

Default to sequential authoring with no worker swarm. If independently authorized
workers are required, bound their count and non-overlapping write paths before
dispatch; no worker-spawns-worker. Delegate only within available host capacity
and approved model/resource budgets. If native fresh-context review is unavailable,
label any inline source check honestly; never call it independent Goldfish review.

Temporary status and logs belong in private host scratch or `mktemp -d`, never a
fixed, shared path. If neither exists, skip them. Do not write process reports in
the project. Do not create alternate contracts or an index merely to fill a tree.

## Author and verify

1. Read the real source and relevant build/test manifests. Determine which
   responsibilities, non-obvious invariants, interfaces or operational constraints
   a reader cannot reliably infer from existing documentation and code.
2. Update the relevant existing document where possible. Create a new targeted
   document only for a demonstrated gap. Use [content guidance](references/templates.md)
   conditionally, not a required template or exhaustive symbol catalog.
3. Reference stable source locations rather than copying private implementation.
   Do not invent behavior, symbols, test commands or assurance. Mark unverified
   claims and commands as such. Never run project commands without an applicable
   execution mandate; naming a command is not proof that it passes.
4. Verify factual claims against current source, local links and preserved human
   content. Missing access is a limit. Independent review, if authorized, follows
   `resources/review-workflow.md`; otherwise report a source check, not approval.
5. Return changed paths, reader value and verification limits briefly. Offer no
   automatic drift scan or additional documentation wave. No changes is a valid
   outcome when existing sources already satisfy the reader need.
