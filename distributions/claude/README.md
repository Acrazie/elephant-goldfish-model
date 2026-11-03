<!-- Modified by Acrazie on 2026-11-03 for the independent EGM fork. -->

> **Independent Acrazie fork.** Based on [Google's Elephant-Goldfish Model](https://github.com/google/elephant-goldfish-model), modified and maintained by Acrazie. Not published, endorsed or supported by Google. See [LICENSE](LICENSE) and [NOTICE](NOTICE).

<p align="center">
  <a href="https://github.com/Acrazie/elephant-goldfish-model"><img src="docs/assets/readme-header.svg" width="480" height="116" alt="Elephant-Goldfish Model"></a>
</p>

<p align="center">Design with an elephant. Review with a goldfish.</p>

<p align="center">
  <a href="#install">Install</a> &ensp;·&ensp;
  <a href="#try-your-first-design">Quickstart</a> &ensp;·&ensp;
  <a href="docs/getting_started.md">Documentation</a> &ensp;·&ensp;
  <a href="https://github.com/Acrazie/elephant-goldfish-model">Website</a>
</p>

<br>

The upstream EGM project designs specifications with deep-context agents and stress-tests them with independent reviewers. This fork adapts that workflow; it does not inherit upstream usage or native-verification claims.

**Elephant** holds your project context and drafts the specification. **Goldfish** reviewers examine the draft and referenced source material without the earlier conversation, helping expose unstated assumptions and blind spots. **You** make the architectural trade-offs and approve the specification before implementing.

Use it when a feature needs design decisions before implementation. For a small, clear bug fix, use your normal coding workflow.

## Install

Choose your coding agent. Install the complete plugin so its skills can read the reviewer prompts and document standards.

### Antigravity CLI

```sh
agy plugin install https://github.com/google/elephant-goldfish-model
```

For the **Antigravity App** and **Antigravity for IDEs** (Visual Studio Code extension), run `/plugin` or see the [installation instructions](docs/harnesses.md#antigravity-app-and-antigravity-for-ides).

### Claude Code

```sh
claude plugin marketplace add Acrazie/elephant-goldfish-model
claude plugin install egm@egm
```

### Codex

```sh
codex plugin marketplace add Acrazie/elephant-goldfish-model
codex plugin add egm@egm
```

Start a new session after installation. For **Claude Cowork** and **ChatGPT Work**, see the [setup guide](docs/harnesses.md).

## Try your first design

Start `egm-design` explicitly with an idea, agreed architecture, or existing document.
In Claude Code and Antigravity CLI use `/egm:egm-design`; in Codex select the skill.

```text
/egm-design Design webhook delivery for this project.
```

The plugin adapts the exploration, updates one useful design, coordinates independent
review and brings material decisions to you with recommendations. No manual sequence
of commands, duplicate drafts or compulsory per-stage reports. Ask for drafting only
when review is not part of your mandate. Approve the final design before requesting
implementation separately. See the [workflow guide](docs/getting_started.md).

## How it works

<table>
  <thead><tr><th align="left">Role</th><th align="left">Context</th><th align="left">Responsibility</th></tr></thead>
  <tbody>
    <tr valign="top"><td><strong>Elephant</strong></td><td>Your project, requirements, and earlier decisions</td><td>Explore the problem and draft the specification.</td></tr>
    <tr valign="top"><td><strong>Goldfish</strong></td><td>The document and its referenced source material, without the earlier conversation</td><td>Find missing assumptions, unclear requirements, and implementation risks.</td></tr>
    <tr valign="top"><td><strong>You</strong></td><td>The goals and constraints that matter</td><td>Resolve trade-offs, approve the design, and decide what to build.</td></tr>
  </tbody>
</table>

Goldfish reviews require fresh subagent contexts. If your agent cannot create them, EGM stops the review. A review does not replace tests or human judgment. See [supported environments and verification limits](docs/harnesses.md#support-status--contributing-other-harnesses).

## Choose a skill

| Skill | Purpose |
| --- | --- |
| [Design](skills/egm-design/SKILL.md) | Adaptive architectural design through independent review and human approval. |
| [Review](skills/egm-review/SKILL.md) | Independent review of an existing design, without edits unless authorized. |
| [Drift Report](skills/egm-drift-report/SKILL.md) | Compare documented commitments with current code. |
| [Bootstrap](skills/egm-bootstrap/SKILL.md) | Document a targeted gap for an identified reader. |

These are the four public commands. Exploration, drafting, resolution and review
iteration are internal capabilities. The former command names have been removed
without aliases. No existing user document is deleted or converted automatically.

## Learn more

- [Getting started](docs/getting_started.md): the workflow and project layout.
- [Setup](docs/harnesses.md): installation, agent capabilities, and known limits.
- [Architecture](https://github.com/google/elephant-goldfish-model/blob/main/docs/designs/architecture.md): how skills and reviewers fit together.
- [Testing](https://github.com/Acrazie/elephant-goldfish-model/blob/main/TESTING.md): checks, execution records, and verification limits.
- [Dave Rensin’s original essay](https://medium.com/@drensin/elephants-goldfish-and-the-new-golden-age-of-software-engineering-c33641a48874): the ideas behind EGM.

## Contribute

See the [accessibility statement](https://github.com/google/elephant-goldfish-model/blob/main/ACCESSIBILITY.md)
for accessibility goals, known limits, and how to report barriers.

Read [contributing](https://github.com/google/elephant-goldfish-model/blob/main/CONTRIBUTING.md) for PRs, [issues](https://github.com/google/elephant-goldfish-model/issues) for bugs, and [discussions](https://github.com/google/elephant-goldfish-model/discussions) for questions.

## License

[Apache 2.0](LICENSE). This is not an officially supported Google product.
