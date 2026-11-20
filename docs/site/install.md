---
title: Install EGM
description: Choose your AI application and install the Acrazie EGM fork plugin.
---

## Claude Cowork

Open the plugin panel and add this marketplace:

```text
Acrazie/elephant-goldfish-model
```

## Command line

Run the commands for your application.

### Claude Code

```sh
claude plugin marketplace add Acrazie/elephant-goldfish-model
claude plugin install egm@egm
```

### Codex CLI

```sh
codex plugin marketplace add Acrazie/elephant-goldfish-model
codex plugin add egm@egm
```

### Antigravity

```sh
agy plugin install https://github.com/Acrazie/elephant-goldfish-model
```

## Before your first review

Install the whole plugin, not just the skills. Reviews need separate AI reviewers with fresh conversation contexts.

Cloud review support has limits. See [application support](https://github.com/Acrazie/elephant-goldfish-model/blob/main/docs/harnesses.md#support-status--contributing-other-harnesses) for details.

## Next step

Follow [Getting started](/getting-started) to design a feature or review an existing document.

Need help? Check the [installation guide](https://github.com/Acrazie/elephant-goldfish-model/blob/main/docs/harnesses.md#install) or [report an issue](https://github.com/Acrazie/elephant-goldfish-model/issues).
