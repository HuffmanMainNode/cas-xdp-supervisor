# CAS-XDP Public Roadmap

**Roadmap baseline:** 2026-11-22  
**Lifecycle:** Prototype suite  
**Status labels:** Complete, In progress, Pending, Deferred

This roadmap is a continuation plan, not a promise that unverified capabilities exist.

## Completed component milestones

- [x] Shared contract, compatibility schema, and five repository-specific manifests.
- [x] Read-only supervisor CLI with deterministic CI tests.
- [x] Offline artifact integrity/provenance and signature-verification prototype.
- [x] Sandbox-scoped POSIX inspection and gated reversible quarantine prototype.
- [x] Linux XDP IPv4 ingress primitive with verifier and isolated veth evidence.
- [x] Local-first HTTP canary with minimized JSONL events and optional STIX 2.1 export.
- [x] Public component release records and public project index.

## Phase 6: integration verification

<badge>Pending</badge>

- [ ] Resolve private master GitHub Actions runner assignment or use trusted Linux host.
- [ ] Run pinned clean-checkout audit against all five public repositories.
- [ ] Run auditor fixture tests and workbench tests.
- [ ] Execute the five allowlisted read-only component commands.
- [ ] Validate and archive integration report and evidence envelopes privately.
- [ ] Review results before any TIER-4 claim.

The previous private master Actions jobs failed before runner assignment. No integration test result was produced by those attempts. This is not recorded as a failing test suite.

## Interface stabilization

- [ ] Define native JSON result schemas for each CLI command intended for automation.
- [ ] Specify stable CLI argument and exit-code contracts.
- [ ] Establish a versioned common result envelope only after component-specific output is characterized.
- [ ] Add compatibility tests that use pinned real checkouts.
- [ ] Evaluate MCP stdio JSON-RPC only after tools, permissions, and schemas are specified.
- [ ] Preserve read-only defaults and explicit exclusion of mutation from orchestration.

## Component hardening

- [ ] Independent review of artifact trust-store lifecycle, revocation, and key rotation.
- [ ] Independent review of POSIX filesystem race handling and rollback semantics.
- [ ] Expand XDP kernel/driver test matrix and design a separately reviewed loader/map transaction.
- [ ] Review canary deployment, TLS/reverse-proxy, log rotation, retention, and multi-process coordination before any non-loopback use.
- [ ] Add supported platform statements only when backed by evidence.

## Release sequence

1. Re-clone and test each component at its documented source commit.
2. Review dependency locks, licenses, README instructions, and release records.
3. Publish independent component prototype tags/releases with exact source commit and evidence.
4. Complete Phase 6 and archive the private report.
5. Reassess whether an integrated prototype release is justified.
6. Conduct independent security review before production claims.

## Permanent exclusions

Remote exploitation, outbound scanning, brute force, retaliation, silent privileged mutation, invented threat attribution, and mandatory hosted services remain outside scope.
