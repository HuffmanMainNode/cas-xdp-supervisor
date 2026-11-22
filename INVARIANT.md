# Supervisor Invariants

1. Default behavior is read-only.
2. No network connections are made by the current prototype.
3. No privilege escalation or host mutation is available.
4. An audit result never implies that a firewall, XDP program, or other enforcement mechanism is active.
5. Missing, mismatched, or malformed baseline files produce a non-zero verification result.
6. The offline baseline checker is a structural checker, not a full JSON Schema validator.
7. No unsupported platform or kernel is described as verified.
8. Future mutating workflows must bind explicit approval to an unchanged plan and prepare rollback state before applying changes.
