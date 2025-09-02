import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 3, 5)

    def test_subtraction(self):
        self.assertEqual(10 - 4, 6)

if __name__ == "__main__":
    unittest.main()
