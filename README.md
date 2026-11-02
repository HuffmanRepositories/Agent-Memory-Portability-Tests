# Agent Memory Portability Tests

[Start here](START-HERE.md) · [Whitepaper](WHITEPAPER.md) · [AI agent guidance](AGENTS.md)


A neutral, synthetic test corpus for reviewing whether agent-memory export/import and migration workflows preserve meaning, metadata, and safety-relevant state.

**Status:** early draft / research prototype. Fixtures are illustrative; they are not a standard, certification suite, or claim of interoperability.

## Scope

Tests portability behaviors including provenance, timestamps, scope boundaries, retention/expiry, deletion tombstones, revision history, untrusted-memory labels, and explicit loss reporting.

This is a **test corpus and review aid**, not a memory protocol, universal schema, SDK, database, retrieval engine, vector store, MCP server, or certification program.

## Quick start

    python scripts/validate_fixtures.py
    python -m unittest discover -s tests -v

The validator checks fixture structure only. It does not test implementations, semantic preservation, security, or conformance.

All fixtures are synthetic. No user memory exports, secrets, or personal data are included.

See docs/fixture-format.md, docs/loss-taxonomy.md, docs/migration-review-checklist.md, and docs/fixture-status.md.
