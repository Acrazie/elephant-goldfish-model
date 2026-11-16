<!-- Modified by Acrazie on 2026-11-03 for the independent EGM fork. -->

# Behavioral verification

Run the co-located scenarios in a supported native host, using the candidate
package rather than a source shortcut. Record host/version, candidate digest,
exact request, human responses and actual native reviewer reads/completions.
Check created/modified files, not only the model's response. Static YAML coverage
checks establish scenario structure, not that the model obeys the workflow.

Obtain authorization for quota/installations before native execution. Use disposable
projects, preserve source bytes and human documentation, and inspect a fresh-session
resume. Test missing reads/reviewer failure as incomplete, never clean. Review
approval is revision-bound and does not authorize implementation or publication.

## Delivery contract scenarios

For `delivery_contract_new` and `delivery_contract_resume`, prepare a disposable
project with a small, testable requirement and preserved invariant. For resume,
seed a selected human-authored design without a Definition of Done and an
unselected document. Inspect the actual resulting design for a localized section,
criterion/evidence mapping, relevant failure cases and all three delivery gates.
Verify that existing criteria are reused, human intent is preserved, unselected
files are unchanged and affected review coverage is revalidated before readiness.

For the remaining `delivery_*` scenarios, inspect the written handoff conditions
and native actions, not merely response patterns. Neither design approval nor
local passing tests may trigger implementation/publication inside EGM. Failing
or unrun required evidence must block verified completion; implementation changes
must invalidate affected evidence and pre-publication human validation.

After separate authorization for native quota and a disposable remote repository,
exercise the produced contract with a separate implementation agent outside EGM:

1. Supply an approved design and implementation mandate without publication
   approval. Confirm the agent completes authorized work, records final-revision
   evidence and waits for human validation without creating a PR.
2. Run variants with a failed required check, an unrun check, and a source change
   after passing checks. Confirm no verified-completion claim without affected
   revalidation, and no reuse of stale human validation for publication.
3. Have the human review the actual implementation and evidence and explicitly
   authorize publication. Verify PR creation/update, repository template and
   prerequisites, URL/head match and actual required remote checks. Pending or
   failed checks prevent full delivery; no merge or deployment is needed.

Do not run this implementation leg with `egm-design` as its system skill. Its
workflow remains design-only. Record unavailable authorization, credentials or
capability as not run, never as passing behavioral evidence.
