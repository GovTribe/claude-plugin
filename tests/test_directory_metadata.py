"""Offline checks for directory metadata and the credential-free diagnostic."""

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError

ROOT = Path(__file__).resolve().parents[1]


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validator = load_script("validate")
checker = load_script("check_mcp")


class DirectoryMetadataTest(unittest.TestCase):
    def test_existing_500_pixel_logo_cannot_be_used_as_the_directory_icon(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "plugin"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "dist", "__pycache__"))
            shutil.copyfile(root / "assets/govtribe-logo.png", root / "assets/govtribe-icon.png")
            with self.assertRaisesRegex(ValueError, "between 512 and 2048"):
                validator.validate(root)

    def test_missing_privacy_policy_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "plugin"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "dist", "__pycache__"))
            manifest = root / ".claude-plugin/plugin.json"
            value = json.loads(manifest.read_text())
            value.pop("privacyPolicyUrl")
            manifest.write_text(json.dumps(value))
            with self.assertRaisesRegex(ValueError, "privacy policy URL"):
                validator.validate(root)


class PublicDiagnosticTest(unittest.TestCase):
    def run_check(self, endpoint_response):
        responses = [
            io.BytesIO(b'{"resource":"https://govtribe.com/mcp","authorization_servers":["https://govtribe.com/mcp"]}'),
            io.BytesIO(b'{"issuer":"https://govtribe.com/mcp","code_challenge_methods_supported":["S256"],"authorization_endpoint":"https://govtribe.com/mcp/authorize","token_endpoint":"https://govtribe.com/mcp/token","registration_endpoint":"https://govtribe.com/mcp/register"}'),
            endpoint_response,
        ]
        opener = MagicMock()
        opener.open.side_effect = responses
        with patch.object(checker, "build_opener", return_value=opener), patch.object(sys, "argv", ["check_mcp.py"]), contextlib.redirect_stdout(io.StringIO()):
            checker.main()
        return opener

    def test_only_public_discovery_and_an_unauthenticated_initialize_are_sent(self):
        opener = self.run_check(HTTPError(checker.ENDPOINT, 401, "Unauthorized", {}, None))
        self.assertEqual(3, opener.open.call_count)
        request = opener.open.call_args_list[-1].args[0]
        self.assertEqual(checker.ENDPOINT, request.full_url)
        self.assertFalse(request.has_header("Authorization"))
        self.assertEqual("POST", request.get_method())
        self.assertEqual("initialize", json.loads(request.data)["method"])

    def test_a_successful_unauthenticated_request_is_not_treated_as_a_pass(self):
        with self.assertRaisesRegex(RuntimeError, "unauthenticated MCP request"):
            self.run_check(io.BytesIO(b'{}'))

    def test_the_removed_authenticated_option_does_not_make_any_request(self):
        with patch.object(checker, "build_opener") as build, patch.object(sys, "argv", ["check_mcp.py", "--authenticated"]), contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as result:
                checker.main()
        self.assertEqual(2, result.exception.code)
        build.assert_not_called()


if __name__ == "__main__":
    unittest.main()
