# https://github.com/FALLENx4NGEL/LAB11-JK-ET

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######## Partner 1
    def test_subtract(self):  # 3 assertions
        with self.assertRaises(TypeError):
            subtract("x", 1)
        with self.assertRaises(TypeError):
            subtract(None, 5)
        with self.assertRaises(TypeError):
            subtract([1, 2], 3)

    def test_log_invalid_argument(self):  # 1 assertion
        # logarithm input (value) MUST BE > 0
        with self.assertRaises(ValueError):
            logarithm(-5, 10)  # negative value is invalid input

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)  # 3-4-5 triangle
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)  # 5-12-13 triangle
        with self.assertRaises(ValueError):
            hypotenuse(-1, 4)  # negative side is invalid

    def test_sqrt(self):  # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        self.assertAlmostEqual(square_root(4), 2.0)
        self.assertAlmostEqual(square_root(16), 4.0)
        with self.assertRaises(ValueError):
            square_root(-9)

    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(6, 7), 42)
        self.assertEqual(mul(2, 2), 4)
        self.assertEqual(mul(2, 3), 6)

    def test_divide(self):  # 3 assertions
        try:
            div(10, 85)
        except ZeroDivisionError:
            print('Invalid Argument')

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_add(self):
        with self.assertRaises(TypeError):
            add("a", 1)
        with self.assertRaises(TypeError):
            add(None, 5)
        with self.assertRaises(TypeError):
            add([1, 2], 3)

    def test_logarithm(self):  # 3 assertions
        with self.assertRaises(ValueError):
            logarithm(-1, 10)  # negative value
        with self.assertRaises(ValueError):
            logarithm(0, 10)  # zero value
        with self.assertRaises(ValueError):
            logarithm(10, -1)  # negative base

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, 1)  # base of 1 is invalid

    ######## Partner 1

    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()

# Main has not been touched (  owo)b