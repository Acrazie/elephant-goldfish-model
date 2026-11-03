<!-- Modified by Acrazie on 2026-11-03 for the independent EGM fork. -->

<!--
Copyright 2026 Google LLC.
SPDX-License-Identifier: Apache-2.0
-->

# Claude Code integration

The current interface has four public commands and follows the
[shared execution rules](../resources/execution_instructions.md) and
[adaptive review procedure](../resources/review-workflow.md). Historical loader
and workflow results below describe their recorded revisions, not validation
of this breaking workflow change. Native behavior must be reverified.

Use Claude Code 2.1.271 or later for `omitClaudeMd` support. Older versions
must not be treated as verified Goldfish isolation environments.

## Invocation and resources

```sh
claude plugin marketplace add Acrazie/elephant-goldfish-model
claude plugin install egm@egm
```

Enable the installed plugin with `claude plugin enable egm@egm`.
Start explicitly with `/egm:egm-design`, `/egm:egm-review`,
`/egm:egm-drift-report`, or `/egm:egm-bootstrap`. The design command coordinates
its internal capabilities without requiring additional public invocations.
Give inline feedback on the canonical design or request changes in chat. Initial
scope, material choices and final approval remain human; section gates do not.

The `Skill` tool may refuse user-invocable-only skills. Read the selected
`SKILL.md` and shared resources in the main context; do not invoke internal
phases as additional public skills. Dispatch reviewers directly and collect
native completion/read evidence. Do not require per-stage workspace reports.

If the user's prompt or agent instructions file (`CLAUDE.md` or `AGENTS.md`)
has a line `EGM artifact directory: <path>`, use it for the canonical design and
explicitly requested exports. Resolve relative paths against the working directory.
If a path from an instructions file resolves outside the working directory,
after following symbolic links, ask the user to confirm it before creating the
folder or writing there. If they decline or no one can confirm, use the working
directory and say why. Intermediate findings belong in temporary returns or
private scratch, not extra workspace artifacts.

## Claude Code Warning: Default agents/ folder is ignored

In Claude Code (`/plugin` > Errors), you may see the following advisory warning:

```text
Default agents/ folder is ignored because the manifest sets "agents"
```

This specific advisory is expected with EGM's explicit adapter list. It does not
mean the registered adapters failed to load; investigate other errors separately.

EGM maintains two agent directories:
1. `agents/`: Contains canonical, harness-agnostic reviewer persona markdown prompts loaded by Antigravity and other harnesses.
2. `.claude-plugin/agents/`: Contains Claude Code adapters. Reviewer adapters use
   `omitClaudeMd: true` and `tools: [Read, Grep, Glob]`; the synthesizer and bootstrap
   orchestrator have their own tool lists, described below.

Because `.claude-plugin/plugin.json` explicitly lists the adapters in `"agents"`,
Claude Code skips auto-loading the root `agents/` folder. The shared personas do
not declare Claude's read-only tool restrictions. Auto-loading them instead would
lose the adapter-specific restrictions; available tools would still be subject to
the host's permissions. Registering both copies would also duplicate reviewer
names. Keep the explicit adapter list rather than removing it to silence this notice.

## Reviewer isolation

Spawn a new native Agent of the plugin's registered reviewer type for each
independent review, for example `egm:egm-zoom-out`. Do not fork the conversation
or resume a previous reviewer. Provide only the task, target, persona/standard
paths, and explicitly supplied Goldfish context; do not copy parent deliberation.

Claude adapters in `.claude-plugin/agents/` declare `tools: [Read, Grep, Glob]`,
`model: inherit`, and `omitClaudeMd: true`. Each adapter reads its canonical
persona from `agents/` through `${CLAUDE_PLUGIN_ROOT}`. Keep Claude tool names
out of shared persona frontmatter: other hosts can interpret `tools` themselves.
Reviewers cannot edit files or run shell commands, and no persistent `memory`
is configured. The synthesizer adapter declares
`tools: [Read, Grep, Glob, Write]` for optional result normalization and
explicit exports, not nested orchestration. It cannot spawn reviewers. Tool lists
cannot restrict Write to specific paths; destination restrictions remain
instructions, not a filesystem sandbox. When using this optional adapter, name
the authorized destination in its task. The primary agent resolves symlinks and
confirms outside-workspace paths before dispatch. Never pass an unconfirmed
instruction-file override to a child.
The bootstrap orchestrator adapter routes to the canonical targeted-documentation
skill. Its Bash and edit tools remain subject to ordinary host permissions;
configuration alone is not a filesystem or network sandbox.
Reviewers cannot open URLs. Do not pass documentation URLs in
`GoldfishContext` to Claude reviewers: save the raw page as a file in the
workspace and pass that path instead.

Normal subagents exclude parent conversation history. `omitClaudeMd` additionally
excludes user/project/local instruction files, but managed policies still apply.
This is context and tool isolation, not filesystem isolation: reviewers can read
accessible files. Pass any required review constraints explicitly and keep
unrelated history, logs, and memory out of the review task.

For local testing, load a uniquely named copy with `claude --plugin-dir <copy>`
to avoid confusion with an already installed `egm` plugin. Validate it with
`claude plugin validate <copy>/.claude-plugin/plugin.json`.

## Claude Cowork

Claude Cowork uses the same `.claude-plugin` package as Claude Code.
Install the plugin from claude.ai/plugins or the Cowork plugin panel via marketplace `google/elephant-goldfish-model`.
For a candidate package, Customize > Plugins > Add plugin > Upload plugin
accepts a ZIP containing the Claude manifest, adapters, and shared runtime files.
Install it and choose **Try in chat**. Record whether the resulting task runs
locally or in the cloud; the tested desktop surface used cloud tasks.
Verify resource resolution and reviewer tools in the actual Cowork session.
Installation alone does not establish that Claude Code's subagent settings or
`${CLAUDE_PLUGIN_ROOT}` substitution work on that surface.
Local testing with `claude --plugin-dir` is supported in Claude Code only.

References: [plugin paths](https://code.claude.com/docs/en/plugins-reference),
[skill invocation](https://code.claude.com/docs/en/skills), and
[subagent context and tools](https://code.claude.com/docs/en/sub-agents).
