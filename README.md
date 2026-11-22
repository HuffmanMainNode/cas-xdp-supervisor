# cas-xdp-supervisor

Local operator-facing control plane for the CAS-XDP defensive component family.

## Current implementation

This repository now contains a **read-only Python prototype** with three commands:

- `status`: report component lifecycle and explicitly state that enforcement is not implemented.
- `audit`: collect low-sensitivity local runtime metadata without network access or host mutation.
- `verify-baseline`: verify the canonical contract/schema Git blob identities and perform structural checks on this repository's compatibility manifest.

Run from a clone:

```sh
python3 supervisor.py status
python3 supervisor.py audit --json
python3 supervisor.py verify-baseline
python3 -m unittest discover -v
```

## Safety boundary

- This prototype does not change host state, elevate privileges, attach packet filters, manage processes, or access the network.
- State-changing operations are not available. Any future containment workflow must follow the seven-stage gate in [CONTRACT.md](CONTRACT.md), including a rollback snapshot prepared before approval and mutation.
- No remote exploitation, outbound scanning, brute force, counter-attack, or silent privileged mutation.
- `XDP_PASS` is not fail-closed. Enforcement status must never be inferred from a successful audit.
- MCP stdio tools and stable CLI flags will be added only after their interfaces and schemas are specified and tested.

## Development

The core uses only the Python standard library. Full JSON Schema Draft 2020-12 validation is performed in CI using a pinned CI-only validator; the offline command performs a smaller structural check and does not claim to be a full JSON Schema engine.

```sh
make test
make verify
```

See [COMPATIBILITY.json](COMPATIBILITY.json) for planned platform targets and evidence status. No platform compatibility or enforcement capability is claimed as verified.
