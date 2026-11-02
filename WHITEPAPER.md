# Agent Memory Portability: Preserving Meaning Across Systems

**Author:** Robert Huffman  
**Status:** Research whitepaper, version 0.1

## Abstract

Agent Memory Portability Tests (P10) is a synthetic corpus for examining what happens when agent memory is exported, imported, or migrated between systems. The project focuses on preserving meaning, provenance, scope, and safety-relevant metadata—not on defining a universal memory protocol.

## Problem statement

Memory migration can silently lose timestamps, source attribution, confidence, scope, retention rules, deletion state, revision history, trust labels, or embedding information. A migration that copies text but drops its context can change how a future system interprets that memory.

## Approach

P10 organizes synthetic cases around portability loss categories. Each case describes the source state, transformation, target state, expected preservation or explicit loss, and review rationale. The corpus emphasizes provenance, event time, procedural version, confidence, scope boundaries, retention, tombstones, revision conflicts, untrusted memory, and embedding loss.

## How to use P10

Read [START-HERE.md](START-HERE.md), [docs/loss-taxonomy.md](docs/loss-taxonomy.md), and [docs/migration-review-checklist.md](docs/migration-review-checklist.md). Inspect existing cases in [fixtures/cases/](fixtures/cases/). Run python scripts/validate_fixtures.py and python -m unittest discover -s tests -v.

## Privacy and limitations

All fixtures must remain synthetic. Never submit real memory exports, personal data, secrets, or customer records. Passing the validator does not prove semantic preservation, privacy, deletion, or security in a real implementation.

## Outlook

A mature portability practice should make data loss explicit, preserve provenance, and allow people to inspect and correct migration outcomes. The corpus is a review aid, not a claim that these properties are solved.

— Robert Huffman