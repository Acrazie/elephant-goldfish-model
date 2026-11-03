<!-- Modified by Acrazie on 2026-11-03 for the independent EGM fork. -->

<!--
Copyright 2026 Google LLC.
SPDX-License-Identifier: Apache-2.0
-->

# Targeted documentation guidance

These are possible content elements, not mandatory sections or files. Use only
what serves the identified reader and is not already explained by a reliable source.

- Component responsibility and boundaries; link to existing architecture context.
- Public contracts and non-obvious invariants developers must preserve.
- Important side effects, authorization, failure or operational constraints.
- Verified source references and real verification commands, with execution limits.

Do not list every class or function, roll up a README for every ancestor directory,
copy code or repeat child documents. Preserve human-maintained content. Prefer
updating a useful source over creating another README, EGM.md, glossary or index.
