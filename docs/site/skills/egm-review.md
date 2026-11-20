---
title: Review
description: Independently review an existing design with risk-based fresh-context coverage.
---

## What it does

Fresh reviewers read your design document and permitted source context without the earlier conversation. Coverage scales with concrete risk:

- `egm-design-critic` as the default baseline reviewer.
- Targeted specialists when risk warrants them (`egm-codebase-details`, `egm-implementation-readiness`, `egm-comprehension`, or `egm-inventive-catalyst` for technical contradictions and forced trade-offs).

## When to use it

Use Review when you already have a design document and want an independent read-only audit, or targeted corrections under an explicit mandate.

## What you get

Concise prioritized findings (`Blocker`, `Major`, `Nit`), verified coverage and limits returned directly in chat — without mandatory report files unless you ask for an export.

## Example

```text
/egm-review docs/designs/webhooks.md
```

## Full instructions

The assistant follows the [Review skill instructions](../../../skills/egm-review/SKILL.md) in the repository.
