# Migration Review Checklist

- [ ] Synthetic data only.
- [ ] Source and target versions identified when known.
- [ ] Identity/provenance retained or loss reported.
- [ ] Event, created, updated, and import times not conflated.
- [ ] Ownership/audience/tenant/project scope does not widen.
- [ ] Retention/expiry and deletion/tombstone semantics survive.
- [ ] Revision history/conflicts retained or loss reported.
- [ ] Confidence/source/trust labels not silently changed.
- [ ] Untrusted content is not elevated to trusted instruction.
- [ ] Unsupported fields/payloads have explicit loss reports.
- [ ] Observed results identify system/version/configuration/date.
- [ ] No certification or comprehensive security claim implied.
