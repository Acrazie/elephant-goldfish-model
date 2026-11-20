---
title: Drafting and review
description: How context, independent review, and human decisions fit together.
---

This page describes the adaptive software design workflow in this fork.

## Develop the design with context

The Elephant is the drafting assistant. Give it the project background, constraints, existing documents, and unresolved questions.

Use [Design](/skills/egm-design) to start from an idea, an agreed architecture, or an existing document. The assistant adapts exploration, maintains one canonical design document with a `Definition of Done`, and brings only material decisions to you with recommendations.

## Review without the earlier conversation

Reviews use independent AI reviewers and additional model tokens. Coverage scales with risk rather than running a fixed multi-stage loop.

The Goldfish reviewers start fresh. They receive the design document and permitted supporting material, including relevant source code for software work. They do not inherit the conversation that led to the design.

Use [Design](/skills/egm-design) to coordinate independent review and authorized corrections in one workflow, or [Review](/skills/egm-review) to audit an existing document read-only. “Fresh” refers to the reviewers’ conversation context; it does not mean they must work without evidence.

## Resolve findings and approve

Read the findings, check them against the project, and decide what to change. You approve the exact design revision before authorizing implementation separately.

## Start where you need to

You can review a document you already have without starting a new design.

For software work, [Document a codebase](/skills/egm-bootstrap) creates or updates targeted documentation for a demonstrated reader need. [Check for drift](/skills/egm-drift-report) compares checked-in documents with live source code after implementation.
