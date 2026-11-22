# CAS-XDP Release Plan

**Current release stage:** Component prototype staging  
**Candidate label:** `v0.1.0-prototype` per component  
**Publication status:** No GitHub Releases or tags have been published by this checkpoint.

## Release model

Each public repository is released independently. A release must identify:
- exact source commit;
- component scope and lifecycle;
- supported platform and toolchain evidence;
- dependency and build inputs;
- reproducible test commands and outcomes;
- evidence tier and direct evidence links;
- limitations and non-goals;
- artifact digest and signature where supported.

Do not create a single umbrella release that implies runtime integration.

## Candidate component set

| Repository | Candidate | Evidence ceiling |
|---|---|---|
| [cas-xdp-supervisor](https://github.com/HuffmanMainNode/cas-xdp-supervisor) | `v0.1.0-prototype` | TIER-2 |
| [cas-threat-index](https://github.com/HuffmanMainNode/cas-threat-index) | `v0.1.0-prototype` | TIER-2 |
| [posix-containment-kit](https://github.com/HuffmanMainNode/posix-containment-kit) | `v0.1.0-prototype` | TIER-2 |
| [xdp-ingress-primitives](https://github.com/HuffmanMainNode/xdp-ingress-primitives) | `v0.1.0-prototype` | TIER-3 |
| [canary-labyrinth-httpd](https://github.com/HuffmanMainNode/canary-labyrinth-httpd) | `v0.1.0-prototype` | TIER-2 |

Candidate labels do not establish that final clean-checkout review or release publication has occurred.

## Pre-publication checklist

- [ ] Clean clone at intended immutable source commit.
- [ ] Run the documented test and build commands.
- [ ] Confirm no uncommitted generated files or local secrets.
- [ ] Confirm license and dependency declarations.
- [ ] Confirm compatibility manifest matches actual tested scope.
- [ ] Confirm release notes match implementation and limitations.
- [ ] Record artifact digest and signing status.
- [ ] Publish the component tag and GitHub Release.
- [ ] Verify published tag resolves to the reviewed source commit.

## Integrated release gate

A combined CAS-XDP integration release is deferred until the private master Phase 6 audit, workbench tests, five read-only command checks, and evidence-envelope validation have actually executed and passed. Archive the report and evidence privately. A static/CLI integration pass is not production validation.

## Production gate

Production claims require independent security review, supported platform matrix, operational rollback testing, deployment/privacy review, and controlled real-environment validation.
