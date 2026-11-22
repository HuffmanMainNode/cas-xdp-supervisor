# Definitions

- **Read-only audit:** Collection of local environment facts without changing host state.
- **Enforcement:** A component actively applying a defensive policy to traffic or host resources. An audit is not enforcement.
- **Unavailable:** A required capability is absent or unsupported. This state must not be reported as protected.
- **Compatibility manifest:** A repository-specific `COMPATIBILITY.json` instance validated against the shared JSON Schema.
- **Canonical contract:** The versioned engineering rules maintained in the private CAS-XDP master repository and copied byte-for-byte into each public repository.
- **Evidence tier:** A label describing the kind of verification actually performed. A tier is not a security certification.
- **Operator approval:** Explicit authorization tied to the exact displayed change plan. It cannot be implied by CLI invocation alone.
