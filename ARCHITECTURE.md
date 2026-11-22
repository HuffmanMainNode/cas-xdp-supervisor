# CAS-XDP Public Architecture

**Architecture version:** 1.0  
**Lifecycle:** Prototype suite  
**Authority:** The shared engineering contract in [CONTRACT.md](CONTRACT.md)

## System shape

CAS-XDP is a family of independently cloneable defensive components. It is not a single remote service, hosted control plane, or automatically integrated runtime. The five components can be adopted independently; cross-component automation remains a future, evidence-gated milestone.

```text
                    Operator / Local Agent
                             |
                    cas-xdp-supervisor
                    /        |         \
                   /         |          \
          cas-threat-index  posix-kit   canary-httpd
                                  \
                             xdp-primitives
```

This is a conceptual responsibility map, not a runtime call graph. The current components do not invoke one another.

## Component responsibilities

| Component | Responsibility | Current boundary |
|---|---|---|
| [cas-xdp-supervisor](https://github.com/HuffmanMainNode/cas-xdp-supervisor) | Read-only local status, audit, and baseline verification | No enforcement, mutation, or network access |
| [cas-threat-index](https://github.com/HuffmanMainNode/cas-threat-index) | Artifact digest, provenance, signature trust, revocation, and local catalog | No artifact execution; trust roots are explicit and local |
| [posix-containment-kit](https://github.com/HuffmanMainNode/posix-containment-kit) | Sandbox-scoped inspection, quarantine, and separately approved restore | No system-wide containment or privilege escalation |
| [xdp-ingress-primitives](https://github.com/HuffmanMainNode/xdp-ingress-primitives) | Minimal Linux XDP IPv4 ingress filter | Exact-source drop primitive; no production loader or map updater |
| [canary-labyrinth-httpd](https://github.com/HuffmanMainNode/canary-labyrinth-httpd) | Local HTTP canary and privacy-minimized event log | Loopback-first; no remote scanning or invented attribution |

## Trust boundaries

1. The operator remains the authority for host state changes.
2. The supervisor performs read-only local reporting and baseline checks.
3. The threat index separates byte integrity from publisher identity and trust.
4. The POSIX kit is confined to an explicitly initialized sandbox and its staged approval procedure.
5. XDP behavior is limited to its explicit ingress program. `XDP_PASS` passes traffic to the normal networking stack and is not fail-closed.
6. The canary observes only requests delivered to its controlled endpoints. It does not scan remote systems.
7. The private project-control archive is not a runtime secret store and is not part of public operation.

## Shared contract and compatibility

Every public component carries a byte-identical [CONTRACT.md](CONTRACT.md) and a repository-specific `COMPATIBILITY.json` validated against [schemas/compatibility.schema.json](schemas/compatibility.schema.json). The contract defines negative scope, provenance, permission boundaries, explicit failure behavior, evidence tiers, interfaces, and reproducible release expectations.

The compatibility manifest is an instance, not a schema. A manifest claim marked verified must cite reproducible evidence. Planned or unverified capabilities must remain labelled accordingly.

## Integration reality

The public components are separate prototypes. Their command surfaces and data models are component-specific. No public document should imply that an automated pipeline, swarm, common runtime API, or end-to-end enforcement flow is already operating.

The private master contains an offline pin auditor and a local read-only workbench prototype. Its Phase 6 workflow has not yet produced a passing integration report. The workbench is not a public service and does not expose state-changing operations.

## Build sequence

1. Preserve each component's independent cloneability and tests.
2. Complete clean-checkout verification at the pinned source revisions.
3. Complete the private cross-repository static audit and read-only command checks.
4. Define versioned native-output schemas and stable inter-component interfaces before adding automation.
5. Review any future state-changing action independently, including approval and rollback.
6. Publish versioned component releases with exact source commits, evidence, dependencies, and limitations.

## Non-goals

Remote exploitation, outbound scanning, brute force, counter-attack, retaliation, silent privileged mutation, mandatory hosted services, and fabricated operational evidence are outside scope.
