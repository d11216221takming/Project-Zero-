import unittest
from safe_division import safe_division

class TestSafeDivision(unittest.TestCase):
    def test_normal_division(self):
        self.assertEqual(safe_division(10, 2), 5)
        self.assertAlmostEqual(safe_division(7, 3), 7/3)

    def test_division_by_zero(self):
        self.assertIsNone(safe_division(5, 0))
        self.assertIsNone(safe_division(0, 0))

    def test_zero_numerator(self):
        self.assertEqual(safe_division(0, 5), 0)

    def test_negative_numbers(self):
        self.assertEqual(safe_division(-10, 2), -5)
        self.assertEqual(safe_division(10, -2), -5)
        self.assertEqual(safe_division(-10, -2), 5)

if __name__ == '__main__':
    unittest.main()