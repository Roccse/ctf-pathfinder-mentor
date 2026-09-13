import unittest

from scripts.session_router import choose_level


class SessionRouterTests(unittest.TestCase):
    def test_default_l1(self):
        self.assertEqual(choose_level(0), "L1")

    def test_unclear_and_one_attempt_l2(self):
        self.assertEqual(choose_level(0, says_unclear=True), "L2")
        self.assertEqual(choose_level(1), "L2")

    def test_two_attempts_l3(self):
        self.assertEqual(choose_level(2), "L3")

    def test_l4_requires_request_or_insistence(self):
        self.assertEqual(choose_level(3), "L3")
        self.assertEqual(choose_level(3, answer_requested=True), "L4")
        self.assertEqual(choose_level(0, answer_insisted=True), "L4")

    def test_solved(self):
        self.assertEqual(choose_level(3, answer_requested=True, solved=True), "SOLVED")

    def test_negative_attempts(self):
        with self.assertRaises(ValueError):
            choose_level(-1)


if __name__ == "__main__":
    unittest.main()
