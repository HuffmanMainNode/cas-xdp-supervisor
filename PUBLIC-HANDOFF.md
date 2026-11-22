# CAS-XDP Public Handoff

**Checkpoint:** 2026-11-22  
**Audience:** Contributors, reviewers, researchers, and future maintainers

## What exists

CAS-XDP currently consists of five independently cloneable public prototypes. The public master is this repository, `cas-xdp-supervisor`, and serves as the community-facing technical entry point for the family. It also contains the read-only supervisor implementation described in [PROTOTYPE-RELEASE.md](PROTOTYPE-RELEASE.md).

The private project-control master remains the canonical location for internal evidence, detailed engineering continuity, integration reports, and private workbench implementation. Private materials are intentionally not reproduced here.

## Start here

1. Read [README.md](README.md) for the public entry point.
2. Read [ARCHITECTURE.md](ARCHITECTURE.md) for system boundaries.
3. Read [CONTRACT.md](CONTRACT.md) for shared invariants.
4. Read [DEFINITIONS.md](DEFINITIONS.md) and [INVARIANT.md](INVARIANT.md) for terminology and supervisor guarantees.
5. Read [INTEROPERABILITY.md](INTEROPERABILITY.md) before building integrations.
6. Read [PROJECT-INDEX.md](PROJECT-INDEX.md) for the five component map.
7. Read [ROADMAP.md](ROADMAP.md) and [RELEASE-PLAN.md](RELEASE-PLAN.md) for next milestones.
8. Read each component's `PROTOTYPE-RELEASE.md` before using it.

## Current system status

The five components have independent implementation and CI evidence. They are not yet a unified runtime. The private Phase 6 auditor and workbench have not produced a passing archived integration report because the private master Actions jobs did not receive runners. No TIER-4 integration or production claim is made.

## Contributor rules

- Preserve the shared contract and repository-specific compatibility manifests.
- Do not change the license of an initialized repository without explicit maintainer approval.
- Keep changes component-scoped and include tests.
- Never claim platform support or behavior without reproducible evidence.
- Keep secrets, private keys, unredacted host data, and private integration evidence out of public commits.
- Any state-changing behavior must implement the seven-stage approval and rollback gate in the contract.
- Keep the default behavior read-only wherever possible.

## Next maintainer checkpoint

Complete the component release checklist, then finish the private Phase 6 audit. Stabilize versioned interfaces only after tests characterize current native outputs. Do not add a central hosted service or mandatory third-party dependency.
