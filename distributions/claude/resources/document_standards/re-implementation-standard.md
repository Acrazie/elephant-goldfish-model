<!-- Modified by Acrazie on 2026-11-03 for the independent EGM fork. -->

# Source Contract Documentation Standard

Documentation helps its identified reader preserve important behavior and
non-obvious constraints. It is not a substitute for the source or a requirement
to reconstruct all implementation from prose.

Verify documented public interfaces, behavioral invariants, authorization, data
formats and important side effects against current source. Link to reliable
existing documentation and code instead of copying it. Include applicable failure
behavior, operational limits and real verification commands; distinguish a command
reference from proof that it ran.

Do not require private helpers, all algorithms, test infrastructure or every
symbol to be documented. An undocumented detail alone is not drift. Incorrect
claims about current behavior and missing material safeguards are defects.
