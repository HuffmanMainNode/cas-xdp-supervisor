#!/usr/bin/env python3
"""Read-only local control-plane prototype for CAS-XDP.

This module intentionally performs no network access, privilege escalation, or
host mutation. It reports environment facts and verifies repository baseline
files. Enforcement and containment are not implemented here.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import sys
from pathlib import Path
from typing import Any, List, Optional

EXPECTED_REPOSITORY = "cas-xdp-supervisor"
EXPECTED_CONTRACT_BLOB = "cd04d1046df036894a5b68796fdc007d4ab7cc82"
EXPECTED_SCHEMA_BLOB = "e565766ca037479c441ce21dd866fbb8209d7615"
REQUIRED_MANIFEST_KEYS = {
    "schema_version", "project", "repository", "contract_version",
    "lifecycle_state", "capabilities", "negative_scope", "platforms",
    "dependencies", "interfaces", "verification",
}


def git_blob_sha1(data: bytes) -> str:
    """Return the Git object ID for a blob without invoking Git."""
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_manifest_shape(manifest: Any, expected_name: str = EXPECTED_REPOSITORY) -> list[str]:
    """Perform offline structural checks for this repository's manifest.

    Full JSON Schema Draft 2020-12 validation is performed by CI. This small
    standard-library check is deliberately described as a structural check,
    not as a general JSON Schema implementation.
    """
    errors: list[str] = []
    if not isinstance(manifest, dict):
        return ["manifest root must be a JSON object"]

    missing = REQUIRED_MANIFEST_KEYS - set(manifest)
    extra = set(manifest) - REQUIRED_MANIFEST_KEYS
    if missing:
        errors.append(f"missing top-level keys: {', '.join(sorted(missing))}")
    if extra:
        errors.append(f"unexpected top-level keys: {', '.join(sorted(extra))}")

    if manifest.get("schema_version") != "1.0":
        errors.append("schema_version must be '1.0'")
    if manifest.get("project") != "CAS-XDP":
        errors.append("project must be 'CAS-XDP'")
    if manifest.get("contract_version") != "1.0":
        errors.append("contract_version must be '1.0'")
    if manifest.get("lifecycle_state") not in {
        "planned", "prototype", "implemented", "verified", "released", "deprecated"
    }:
        errors.append("lifecycle_state is not a recognized value")

    repository = manifest.get("repository")
    if not isinstance(repository, dict):
        errors.append("repository must be an object")
    else:
        if repository.get("owner") != "HuffmanMainNode":
            errors.append("repository.owner must be 'HuffmanMainNode'")
        if repository.get("name") != expected_name:
            errors.append(f"repository.name must be {expected_name!r}")
        if repository.get("visibility") != "public":
            errors.append("repository.visibility must be 'public'")
        expected_url = f"https://github.com/HuffmanMainNode/{expected_name}"
        if repository.get("url") != expected_url:
            errors.append(f"repository.url must be {expected_url!r}")

    for key in ("capabilities", "negative_scope", "platforms", "interfaces"):
        if not isinstance(manifest.get(key), list):
            errors.append(f"{key} must be an array")

    dependencies = manifest.get("dependencies")
    if not isinstance(dependencies, dict):
        errors.append("dependencies must be an object")
    else:
        for key in ("build", "runtime", "optional"):
            if not isinstance(dependencies.get(key), list):
                errors.append(f"dependencies.{key} must be an array")

    verification = manifest.get("verification")
    if not isinstance(verification, dict):
        errors.append("verification must be an object")
    else:
        if verification.get("highest_evidence_tier") not in {
            "none", "TIER-1", "TIER-2", "TIER-3", "TIER-4", "TIER-5"
        }:
            errors.append("verification.highest_evidence_tier is invalid")
        if not isinstance(verification.get("claims"), list):
            errors.append("verification.claims must be an array")

    return errors


def collect_read_only_audit() -> dict[str, Any]:
    """Collect low-sensitivity runtime facts without changing host state."""
    if hasattr(os, "geteuid"):
        privilege_context = "root" if os.geteuid() == 0 else "unprivileged"
    else:
        privilege_context = "not_available"

    return {
        "mode": "read_only",
        "host_mutations_performed": False,
        "enforcement_status": "not_implemented",
        "environment": {
            "os_family": platform.system(),
            "kernel_release": platform.release(),
            "machine_architecture": platform.machine(),
            "python_version": platform.python_version(),
            "privilege_context": privilege_context,
        },
        "checks": [
            {
                "id": "runtime-observation",
                "status": "observed",
                "detail": "Runtime metadata collected using Python standard-library calls.",
            },
            {
                "id": "enforcement",
                "status": "not_implemented",
                "detail": "This prototype does not attach filters or alter host state.",
            },
        ],
    }


def verify_baseline(root: Path) -> dict[str, Any]:
    """Verify canonical file identities and the local compatibility manifest."""
    checks: list[dict[str, str]] = []
    failures: list[str] = []

    expected_files = (
        ("CONTRACT.md", EXPECTED_CONTRACT_BLOB),
        ("schemas/compatibility.schema.json", EXPECTED_SCHEMA_BLOB),
    )
    for relative, expected in expected_files:
        path = root / relative
        try:
            actual = git_blob_sha1(path.read_bytes())
        except OSError as exc:
            failures.append(f"{relative}: cannot read file: {exc}")
            checks.append({"file": relative, "status": "unavailable"})
            continue
        if actual != expected:
            failures.append(f"{relative}: canonical Git blob identity mismatch")
            checks.append({"file": relative, "status": "mismatch", "actual_blob": actual})
        else:
            checks.append({"file": relative, "status": "match", "actual_blob": actual})

    manifest_path = root / "COMPATIBILITY.json"
    try:
        manifest = read_json(manifest_path)
    except (OSError, json.JSONDecodeError) as exc:
        failures.append(f"COMPATIBILITY.json: cannot parse manifest: {exc}")
        checks.append({"file": "COMPATIBILITY.json", "status": "invalid"})
    else:
        manifest_errors = validate_manifest_shape(manifest)
        if manifest_errors:
            failures.extend(f"COMPATIBILITY.json: {item}" for item in manifest_errors)
            checks.append({"file": "COMPATIBILITY.json", "status": "invalid"})
        else:
            checks.append({"file": "COMPATIBILITY.json", "status": "structurally_valid"})

    return {
        "check": "repository_baseline",
        "success": not failures,
        "checks": checks,
        "errors": failures,
        "note": "Offline structural check only; CI performs full JSON Schema validation.",
    }


def _emit(payload: dict[str, Any], as_json: bool) -> None:
    if as_json:
        print(json.dumps(payload, indent=2, sort_keys=True))
        return
    for key, value in payload.items():
        print(f"{key}: {json.dumps(value, sort_keys=True) if isinstance(value, (dict, list)) else value}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cas-xdp-supervisor",
        description="Read-only local CAS-XDP supervisor prototype. No host changes are performed.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    status = subparsers.add_parser("status", help="show prototype and enforcement status")
    status.add_argument("--json", action="store_true", help="emit JSON")

    audit = subparsers.add_parser("audit", help="collect read-only local runtime metadata")
    audit.add_argument("--json", action="store_true", help="emit JSON")

    baseline = subparsers.add_parser("verify-baseline", help="verify local contract, schema, and manifest")
    baseline.add_argument("--root", type=Path, default=Path.cwd(), help="repository root (default: current directory)")

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "status":
        payload = {
            "project": "CAS-XDP",
            "component": EXPECTED_REPOSITORY,
            "lifecycle": "prototype",
            "enforcement_status": "not_implemented",
            "mutating_operations": "not_available",
            "network_access": "not_used",
        }
        _emit(payload, args.json)
        return 0

    if args.command == "audit":
        _emit(collect_read_only_audit(), args.json)
        return 0

    if args.command == "verify-baseline":
        result = verify_baseline(args.root.resolve())
        _emit(result, True)
        return 0 if result["success"] else 2

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
