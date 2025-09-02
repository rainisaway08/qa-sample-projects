import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(4, 5), 20)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(5, 0)

if __name__ == '__main__':
    unittest.main()
