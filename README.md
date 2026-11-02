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

## Ecosystem directory

This project is part of the [HuffmanRepositories public ecosystem](https://github.com/HuffmanRepositories/Huffman-Ecosystem-Root). Use the directory for project routing, human and AI onboarding, shared terminology, governance, and related workstreams. This repository's own README and specifications remain authoritative for its scope, maturity, and validation status.
