"""
tests/test_calculator.py — Unit tests for the calculator module.
4 test cases, run with: python -m pytest tests/ -v
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.calculator import add, subtract, multiply, divide, power, is_even  # noqa: E402


class TestAddition(unittest.TestCase):
    """Test Case 1 — Addition"""

    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_zero(self):
        self.assertEqual(add(0, 100), 100)

    def test_add_floats(self):
        self.assertAlmostEqual(add(1.1, 2.2), 3.3, places=5)


class TestSubtraction(unittest.TestCase):
    """Test Case 2 — Subtraction"""

    def test_subtract_positive(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_subtract_negative_result(self):
        self.assertEqual(subtract(2, 8), -6)

    def test_subtract_zero(self):
        self.assertEqual(subtract(7, 0), 7)


class TestMultiplicationAndDivision(unittest.TestCase):
    """Test Case 3 — Multiplication & Division"""

    def test_multiply_positive(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(999, 0), 0)

    def test_divide_exact(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_divide_float_result(self):
        self.assertAlmostEqual(divide(7, 3), 2.3333, places=3)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError) as ctx:
            divide(10, 0)
        self.assertIn("zero", str(ctx.exception).lower())


class TestUtilityFunctions(unittest.TestCase):
    """Test Case 4 — Power and utility functions"""

    def test_power_positive(self):
        self.assertEqual(power(2, 8), 256)

    def test_power_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)

    def test_is_even_true(self):
        self.assertTrue(is_even(4))

    def test_is_even_false(self):
        self.assertFalse(is_even(7))

    def test_is_even_zero(self):
        self.assertTrue(is_even(0))


if __name__ == "__main__":
    unittest.main(verbosity=2)
