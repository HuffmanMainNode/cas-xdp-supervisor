import json
import unittest
from pathlib import Path

import supervisor


ROOT = Path(__file__).resolve().parents[1]


class SupervisorTests(unittest.TestCase):
    def test_git_blob_identity_matches_contract(self):
        data = (ROOT / "CONTRACT.md").read_bytes()
        self.assertEqual(supervisor.git_blob_sha1(data), supervisor.EXPECTED_CONTRACT_BLOB)

    def test_manifest_is_structurally_valid(self):
        manifest = supervisor.read_json(ROOT / "COMPATIBILITY.json")
        self.assertEqual(supervisor.validate_manifest_shape(manifest), [])

    def test_manifest_rejects_wrong_repository_identity(self):
        manifest = supervisor.read_json(ROOT / "COMPATIBILITY.json")
        manifest["repository"]["name"] = "some-other-repo"
        errors = supervisor.validate_manifest_shape(manifest)
        self.assertTrue(any("repository.name" in item for item in errors))

    def test_manifest_rejects_missing_required_key(self):
        manifest = supervisor.read_json(ROOT / "COMPATIBILITY.json")
        del manifest["negative_scope"]
        errors = supervisor.validate_manifest_shape(manifest)
        self.assertTrue(any("negative_scope" in item for item in errors))

    def test_baseline_verification_passes_for_checkout(self):
        result = supervisor.verify_baseline(ROOT)
        self.assertTrue(result["success"], result["errors"])

    def test_audit_is_read_only_and_does_not_claim_enforcement(self):
        result = supervisor.collect_read_only_audit()
        self.assertEqual(result["mode"], "read_only")
        self.assertFalse(result["host_mutations_performed"])
        self.assertEqual(result["enforcement_status"], "not_implemented")


if __name__ == "__main__":
    unittest.main()
