# CAS-XDP Interoperability

**Review status:** Initial interface inventory complete. Runtime interoperability is not implemented.

## Component interface inventory

| Component | Current CLI surface | Machine-readable output | State-changing operations |
|---|---|---|---|
| Supervisor | `status`, `audit`, `verify-baseline` | JSON for status/audit and baseline verification | None |
| Threat index | `digest`, `validate`, `verify`, `register`, `list` | JSON | `register` writes local SQLite catalog |
| POSIX containment | `init-root`, `inspect`, `prepare`, `show`, `approve`, `apply`, `verify`, `record`, `prepare-rollback` | JSON | Initialization, preparation, approval, apply, recording, rollback preparation; apply moves sandbox file |
| XDP ingress | `validate`, `compile` | JSON | None; compile is preview-only |
| HTTP canary | `serve`, `validate-log`, `export-stix` | JSON for validation/export; serve prints startup text | Serve opens listener and appends events; export writes STIX file |

Confirm exact flags with each component's current CLI help before scripting against it. Do not infer undocumented options.

## Existing data contracts

- Shared compatibility manifest: root `COMPATIBILITY.json`, validated against the Draft 2020-12 schema.
- Threat index: signed artifact provenance record and local trust-store schemas.
- POSIX containment: versioned plan, approval, record, and rollback snapshot references.
- XDP: versioned exact-source IPv4 ingress rule schema and deterministic map preview.
- Canary: versioned privacy-minimized event schema and STIX 2.1 bundle output.

## Current interoperability reality

The components do not import or invoke one another. Their CLIs emit JSON, but result structures are component-specific. There is no shared machine-readable command-result envelope across the public components.

The private master has an offline auditor that checks immutable pins, common contract/schema identity, manifest identity, and evidence claims. That static audit does not prove runtime command compatibility. Its local workbench is a private prototype and has not yet produced an archived successful integration run.

Do not describe the repositories as a functioning swarm, integrated control plane, or end-to-end security product.

## Safe manual composition points

1. **Baseline:** supervisor verifies local contract/schema identity and its compatibility manifest.
2. **Artifact trust:** threat index digests and verifies a local artifact against provenance and explicit trust roots. Registration is a separate local write.
3. **Sandbox inspection:** POSIX inspect/show/verify are read-only. Quarantine and restore remain sandbox-scoped and gated by explicit approval and rollback.
4. **Ingress preview:** XDP validate/compile produce a deterministic map preview; they do not load or update a map.
5. **Canary evidence:** canary validate-log reads local JSONL. STIX export writes a new local bundle. A listener must not be started automatically by an orchestrator.

These are manual boundaries, not an automated pipeline.

## Required interface work before automation

- Define versioned schemas for native command results.
- Specify exit-code semantics and error categories.
- Define source identity and immutable pin propagation.
- Define time, provenance, and evidence-envelope semantics.
- Specify explicit permission scopes and user approval for any mutating command.
- Add compatibility tests against real pinned component checkouts.
- Retain a default-deny command allowlist; do not accept arbitrary shell strings.

## Explicit non-claims

No runtime cross-repository calls, automated response orchestration, distributed agent coordination, public hosted service, production security coverage, or TIER-4/TIER-5 evidence is claimed.
