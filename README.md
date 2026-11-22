# CAS-XDP Public Master and Supervisor

**Project:** CAS-XDP  
**Role:** Public master and read-only supervisor component  
**Lifecycle:** Prototype suite  
**License:** MIT for this repository; other component repositories retain their existing licenses.

CAS-XDP is a family of independently cloneable defensive prototypes for local artifact trust, bounded file containment, ingress filtering primitives, and privacy-minimized canary telemetry. This repository is the community-facing technical master and also contains the read-only supervisor implementation. It is not a hosted control plane or a claim that all components already operate as one runtime.

## Start here

| Document | Purpose |
|---|---|
| [PUBLIC-HANDOFF.md](PUBLIC-HANDOFF.md) | Public project handoff and contributor starting sequence |
| [PROJECT-INDEX.md](PROJECT-INDEX.md) | Map of all five public components |
| [ARCHITECTURE.md](ARCHITECTURE.md) | System shape, trust boundaries, build sequence |
| [CONTRACT.md](CONTRACT.md) | Shared engineering contract and non-negotiable invariants |
| [DEFINITIONS.md](DEFINITIONS.md) | Shared terminology |
| [INVARIANT.md](INVARIANT.md) | Supervisor-specific guarantees |
| [INTEROPERABILITY.md](INTEROPERABILITY.md) | Actual interfaces and integration limits |
| [ROADMAP.md](ROADMAP.md) | Remaining engineering milestones |
| [RELEASE-PLAN.md](RELEASE-PLAN.md) | Component prototype release criteria |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution and review requirements |
| [PROTOTYPE-RELEASE.md](PROTOTYPE-RELEASE.md) | Supervisor implementation scope and evidence |

## Public component family

- [cas-xdp-supervisor](https://github.com/HuffmanMainNode/cas-xdp-supervisor): read-only lifecycle and local baseline audit.
- [cas-threat-index](https://github.com/HuffmanMainNode/cas-threat-index): offline artifact digest, provenance, signature trust, revocation, and local catalog.
- [posix-containment-kit](https://github.com/HuffmanMainNode/posix-containment-kit): sandbox-scoped file inspection, quarantine, and separately approved restore.
- [xdp-ingress-primitives](https://github.com/HuffmanMainNode/xdp-ingress-primitives): minimal Linux XDP IPv4 ingress filtering primitive.
- [canary-labyrinth-httpd](https://github.com/HuffmanMainNode/canary-labyrinth-httpd): local HTTP canary, minimized JSONL events, optional STIX 2.1 export.

## Supervisor implementation

This repository contains a **read-only Python prototype** with three commands:

- `status`: report component lifecycle and explicitly state that enforcement is not implemented.
- `audit`: collect low-sensitivity local runtime metadata without network access or host mutation.
- `verify-baseline`: verify canonical contract/schema Git blob identities and perform structural checks on this repository's compatibility manifest.

Run from a clone:

```sh
python3 supervisor.py status
python3 supervisor.py audit --json
python3 supervisor.py verify-baseline
python3 -m unittest discover -v
```

## Safety boundary

- The supervisor does not change host state, elevate privileges, attach packet filters, manage processes, or access the network.
- State-changing operations are not available in this prototype.
- Any future containment workflow must follow the seven-stage gate in [CONTRACT.md](CONTRACT.md), including a rollback snapshot prepared before approval and mutation.
- No remote exploitation, outbound scanning, brute force, counter-attack, or silent privileged mutation.
- `XDP_PASS` is pass-through to the normal networking stack, not fail-closed.
- A successful audit does not prove that enforcement is active.
- MCP stdio tools and stable cross-component interfaces will be added only after their contracts and schemas are specified and tested.

## Verification

The recorded supervisor CI run passed six deterministic tests and compatibility checks across Python 3.9 through 3.13 on Ubuntu 24.04. This is TIER-2 evidence for the supervisor prototype, not evidence of kernel enforcement, host mutation, MCP server behavior, cross-repository runtime integration, or non-Ubuntu compatibility.

See [PROTOTYPE-RELEASE.md](PROTOTYPE-RELEASE.md) for the source commit, evidence link, exact scope, and limitations.

See [CHECKPOINT.md](CHECKPOINT.md) for the dated prototype closeout and continuation gates.

## Project integration status

The five public components remain independent prototypes. The private project-control master contains the offline integration auditor and local read-only workbench. The Phase 6 integration workflow has not yet produced a passing report because the private master Actions jobs failed before runner assignment. No TIER-4 integration or production claim is made.

## Governance and project boundaries

- Each repository retains its own identity, license, dependencies, and evidence record.
- The shared contract and compatibility schema are byte-identical across public components.
- Core local operation does not require a hosted service, subscription, or mandatory API key.
- Private project-control evidence and internal workbench artifacts remain outside this public repository.
- Platform and operational claims must be backed by reproducible evidence.
