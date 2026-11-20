---
title: Getting started
description: Try the method, choose an application, and start your first design.
---

## Start with the method

Read the [repository setup guide](https://github.com/Acrazie/elephant-goldfish-model/blob/main/docs/getting_started.md). It introduces the adaptive workflow and how Elephant and Goldfish contexts fit together.

## Choose an application

The plugin runs inside a supported AI application. [Install EGM](/install) in your application before your first project.

Review workflows require an application that can run isolated subagents. Cloud support remains partial. Check the installation guide for the current limits.

## Start with a software idea

Describe the problem, who it affects, and what you know using [Design](/skills/egm-design):

```text
/egm-design
Help students book a shared study space.
Help me design who needs access, how bookings work,
and what happens when two requests overlap.
```

The assistant clarifies material decisions with recommendations, writes one canonical design document with a `Definition of Done`, and coordinates fresh-context review before asking for your approval. See [drafting and review](/workflow).

## Review an existing document

Save the document as a file and run [Review](/skills/egm-review) for a read-only independent audit:

```text
/egm-review docs/designs/study-space-plan.md
```

Check the findings and decide which changes to authorize before implementation.
