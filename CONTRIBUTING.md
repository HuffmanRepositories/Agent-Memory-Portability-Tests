# Contributing

- Synthetic data only. Never submit personal memory exports, credentials, secrets, or real user data.
- Keep fixtures implementation-neutral and cite public documentation for claims.
- Distinguish expected behavior from observed behavior.
- Do not claim conformance without reproducible system-under-test evidence and review.
- Report loss or ambiguity explicitly rather than silently normalizing it away.

To add a fixture: copy docs/fixture-template.json, assign a unique MP-NNN ID, describe expected outcomes and loss labels, update docs/fixture-status.md, run validator/tests, then submit a PR.
