# CAS-XDP Public Prototype Checkpoint

**Checkpoint date:** 2026-11-22  
**Public master:** `HuffmanMainNode/cas-xdp-supervisor`  
**Release stage:** `v0.1.0-prototype` candidate staging  
**Lifecycle:** Five independent public prototypes  
**Integration status:** Phase 6 pending; no combined runtime claim

## Closeout

The public documentation set is now established for the CAS-XDP prototype family. This repository is the public technical master and community-facing entry point, while retaining the read-only supervisor implementation. The four other public repositories retain their independent component identities and release records.

## Public documentation deposited

- [README.md](README.md): project and supervisor entry point.
- [PUBLIC-HANDOFF.md](PUBLIC-HANDOFF.md): public project handoff.
- [PROJECT-INDEX.md](PROJECT-INDEX.md): component map.
- [ARCHITECTURE.md](ARCHITECTURE.md): system shape and trust boundaries.
- [CONTRACT.md](CONTRACT.md): shared engineering contract.
- [schemas/compatibility.schema.json](schemas/compatibility.schema.json): shared compatibility schema.
- [COMPATIBILITY.json](COMPATIBILITY.json): supervisor manifest.
- [DEFINITIONS.md](DEFINITIONS.md) and [INVARIANT.md](INVARIANT.md): terms and guarantees.
- [INTEROPERABILITY.md](INTEROPERABILITY.md): actual interfaces and limitations.
- [ROADMAP.md](ROADMAP.md): next engineering sequence.
- [RELEASE-PLAN.md](RELEASE-PLAN.md): component publication requirements.
- [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md): community and security guidance.
- [PROTOTYPE-RELEASE.md](PROTOTYPE-RELEASE.md): supervisor implementation evidence and limitations.

The other four public components each contain their own `PROTOTYPE-RELEASE.md` and README link.

## Component evidence ceiling

| Component | Evidence ceiling | Release scope |
|---|---|---|
| Supervisor | TIER-2 | Read-only local audit and baseline checks |
| Threat index | TIER-2 | Offline digest, provenance, signature trust, revocation, local catalog |
| POSIX containment | TIER-2 | Explicit sandbox-scoped file containment |
| XDP ingress | TIER-3 | Linux XDP IPv4 ingress primitive and isolated veth test |
| HTTP canary | TIER-2 | Local canary, minimized events, optional STIX export |

These are component-level evidence ceilings, not a system-wide integration tier.

## Integration boundary

The five components do not yet form an automated runtime. The private master has a static pinned-repository auditor and a local read-only workbench prototype. The private Phase 6 workflow did not receive a GitHub Actions runner, so it did not execute its tests or integration audit. No passing integration report, TIER-4 claim, or production-readiness claim exists.

## Release staging

Candidate tag: `v0.1.0-prototype` per component.

No GitHub Releases or tags have been published in this checkpoint. Before publication, perform a clean clone at the exact intended source commit, run the component's documented test/build commands, verify license/dependencies and compatibility claims, and confirm the release record.

A combined CAS-XDP release remains deferred until Phase 6 actually passes. Production claims require separate security and operational validation.

## Next maintainer sequence

1. Run final clean-checkout tests for each public component.
2. Publish component-scoped prototype releases after review.
3. Resolve the private master Actions runner-assignment issue or run the documented Phase 6 local procedure on a trusted Linux host.
4. Archive raw test outputs and integration report privately.
5. Define stable versioned inter-component interfaces only after real command output and error behavior are characterized.
6. Update evidence tiers only from reproducible results.

## Closing point

The public project is now documented for independent adoption and future contribution. The private master retains the internal engineering record and verification machinery. The current development cycle is closed at the documented component-prototype checkpoint; the remaining integration work is explicitly staged for the next cycle.
