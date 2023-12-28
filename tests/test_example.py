import unittest
from ..src.fastwebgui.example import add_one


class AdditionTest(unittest.TestCase):
    def test_add_one(self) -> None:
        self.assertEqual(add_one(0), 1)
        self.assertEqual(add_one(-1), 0)
        self.assertEqual(add_one(99), 100)
