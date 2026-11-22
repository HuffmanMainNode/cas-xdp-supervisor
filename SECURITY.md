# Security Policy

## Scope

This project is currently a read-only local prototype. It does not implement enforcement, containment, remote management, network scanning, or privileged operations.

## Reporting

Report suspected vulnerabilities privately to the repository owner through GitHub's security reporting mechanism where enabled. Do not publish exploit details in an issue before maintainers have had an opportunity to assess the report.

## Safe-use guarantees and limitations

- Current commands do not intentionally mutate host state or open network connections.
- Environment metadata is printed locally; review output before sharing it.
- The baseline checker verifies local repository files only. It does not authenticate external publishers or prove that an artifact is safe.
- No production-security or host-protection guarantee is made.
- Future state-changing functionality must implement the full staged approval and rollback requirements in [CONTRACT.md](CONTRACT.md).
