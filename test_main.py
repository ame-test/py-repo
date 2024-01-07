import unittest

from main import add

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(add(1, 2), 3)

    def test_main_zero_case(self):
        self.assertEqual(add(0, 0), 0)