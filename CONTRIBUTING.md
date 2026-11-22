# Contributing to CAS-XDP

Thanks for helping improve the CAS-XDP prototype family.

## Before opening a change

1. Identify the component repository that owns the behavior.
2. Read the root [CONTRACT.md](CONTRACT.md), [ARCHITECTURE.md](ARCHITECTURE.md), and [INTEROPERABILITY.md](INTEROPERABILITY.md).
3. Check the component's README, compatibility manifest, and prototype release record.
4. Open an issue or discussion for cross-component interface changes before implementing them.

## Required change quality

- Keep changes narrowly scoped and preserve independent cloneability.
- Add deterministic tests for new behavior and failure paths.
- Update schemas and compatibility manifests when interfaces or claims change.
- Document supported and unsupported platforms honestly.
- Include exact reproduction commands and evidence links.
- Avoid new runtime dependencies unless justified and explicitly declared.
- Never include credentials, private keys, tokens, personal data, or unredacted host telemetry.

## Safety requirements

- No remote exploitation, scanning, brute force, retaliation, or counter-attack.
- Default to read-only behavior.
- Any state-changing operation must follow the seven-stage approval and rollback gate in [CONTRACT.md](CONTRACT.md).
- Do not describe `XDP_PASS` as fail-closed.
- Do not claim an audit means enforcement is active.
- Do not label fixtures or synthetic tests as live operational evidence.

## Pull request checklist

- [ ] Scope and affected component are identified.
- [ ] Tests cover success and failure behavior.
- [ ] Documentation and compatibility manifest are updated.
- [ ] Dependency and license implications are documented.
- [ ] No secrets or private evidence are included.
- [ ] Evidence tier and limitations are accurately stated.
