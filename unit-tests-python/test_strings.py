import unittest

class TestStrings(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("rain".upper(), "RAIN")

    def test_isdigit(self):
        self.assertFalse("rain".isdigit())

if __name__ == "__main__":
    unittest.main()
