import unittest

from scripts.triage_environment import classify


class EnvironmentTriageTests(unittest.TestCase):
    def test_command_missing(self):
        self.assertEqual(classify("checksec: command not found"), "command_missing")

    def test_permission(self):
        self.assertEqual(classify("bash: ./chall: Permission denied"), "permission_denied")

    def test_architecture(self):
        self.assertEqual(classify("cannot execute binary file: Exec format error"), "architecture_mismatch")

    def test_dependency(self):
        self.assertEqual(classify("ModuleNotFoundError: No module named 'pwn'"), "dependency_missing")

    def test_network(self):
        self.assertEqual(classify("Connection refused"), "connection_refused")

    def test_unknown(self):
        self.assertEqual(classify("unexpected parser state"), "unknown")


if __name__ == "__main__":
    unittest.main()
