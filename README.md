# cas-xdp-supervisor

Local operator-facing control plane for the CAS-XDP defensive component family.

## Responsibility

The supervisor is intended to provide read-only local host auditing, display reviewed defensive action plans, coordinate explicit operator approval, and expose a narrowly scoped MCP stdio JSON-RPC 2.0 interface. It is not a remote management service.

## Safety boundary

- Read-only inspection is the default.
- State changes must follow the seven-stage gate in [CONTRACT.md](CONTRACT.md), including a rollback snapshot prepared before approval and mutation.
- No remote exploitation, outbound scanning, brute force, counter-attack, or silent privileged mutation.
- An unavailable enforcement component must be reported as unavailable, not represented as protected.
- MCP tools and CLI flags will be documented and schema-versioned before being treated as stable.

## Current status

**Lifecycle: planned.** This repository is an initialized project baseline. No executable supervisor, CLI, MCP tool, or test suite has yet been verified. See [COMPATIBILITY.json](COMPATIBILITY.json) for explicit unverified targets.

## Development

The canonical shared engineering rules are in [CONTRACT.md](CONTRACT.md). The compatibility manifest is validated in CI. No hosted service, proprietary subscription, or mandatory external API is intended for core local operation.
