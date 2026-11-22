# CAS-XDP Public Project Index

This page is the public navigation point for the CAS-XDP prototype family. It is documentation only. The repository hosting this index remains the **read-only supervisor component**, not a combined runtime or central hosted service.

## Project purpose

CAS-XDP is a collection of independently cloneable defensive prototypes exploring local artifact trust, bounded file containment, ingress filtering primitives, and privacy-minimized canary telemetry. Each component has its own lifecycle, interfaces, evidence, and limitations.

## Component map

| Component | Responsibility | Lifecycle | Evidence |
|---|---|---|---|
| [cas-xdp-supervisor](https://github.com/HuffmanMainNode/cas-xdp-supervisor) | Read-only lifecycle and local baseline audit | Prototype | TIER-2 |
| [cas-threat-index](https://github.com/HuffmanMainNode/cas-threat-index) | Offline artifact integrity, provenance, signature trust, revocation, local catalog | Prototype | TIER-2 |
| [posix-containment-kit](https://github.com/HuffmanMainNode/posix-containment-kit) | Sandbox-scoped file inspection, quarantine, and separately approved restore | Prototype | TIER-2 |
| [xdp-ingress-primitives](https://github.com/HuffmanMainNode/xdp-ingress-primitives) | Minimal Linux XDP IPv4 ingress filtering primitive | Prototype | TIER-3 |
| [canary-labyrinth-httpd](https://github.com/HuffmanMainNode/canary-labyrinth-httpd) | Local HTTP canary, minimized JSONL events, optional STIX 2.1 export | Prototype | TIER-2 |

## Prototype entry points

- [Supervisor prototype release record](PROTOTYPE-RELEASE.md)
- [Threat index prototype release record](https://github.com/HuffmanMainNode/cas-threat-index/blob/main/PROTOTYPE-RELEASE.md)
- [POSIX containment prototype release record](https://github.com/HuffmanMainNode/posix-containment-kit/blob/main/PROTOTYPE-RELEASE.md)
- [XDP ingress prototype release record](https://github.com/HuffmanMainNode/xdp-ingress-primitives/blob/main/PROTOTYPE-RELEASE.md)
- [HTTP canary prototype release record](https://github.com/HuffmanMainNode/canary-labyrinth-httpd/blob/main/PROTOTYPE-RELEASE.md)

## Integration status

The components are independently usable prototypes. A private integration auditor and read-only workbench have been implemented, but cross-repository execution has not yet produced a passing integration report. Do not treat the family as one integrated runtime.

## Safety and scope

- No remote exploitation, outbound scanning, brute force, retaliation, or silent privileged mutation.
- No required hosted service, subscription, or mandatory API key for core local operation.
- XDP `XDP_PASS` is pass-through to the normal networking stack, not fail-closed.
- Containment is restricted to an explicitly initialized sandbox.
- Artifact signature trust depends on explicit local trust roots.
- Public exposure and production deployment are not claimed.

## Next shared milestone

Complete and archive the pinned cross-repository audit and read-only workbench run on a trusted Linux host. Then review component-specific security limitations and prepare versioned prototype tags. A passing static/CLI integration gate will not, by itself, establish production readiness.
