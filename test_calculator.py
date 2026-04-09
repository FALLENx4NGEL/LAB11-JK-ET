# https://github.com/FALLENx4NGEL/LAB11-JK-ET

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(5,8),13)
        self.assertEqual(add(0,0),0)
        self.assertEqual(add(-3,-5),-8)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(3,5),-2)
        self.assertEqual(subtract(5,3),2)
        self.assertEqual(subtract(0,0),0)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2,2),1)
        self.assertEqual(logarithm(2,4),.5)
        self.assertAlmostEqual(logarithm(8,2),3)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2,0)
        with self.assertRaises(ValueError):
            logarithm(3,1)
        with self.assertRaises(ValueError):
            logarithm(2,-2)
    def test_log_invalid_argument(self): # 1 assertion
        #  INPUT ERROR (MUST BE > 0)
        with self.assertRaises(ValueError):
            logarithm(0,2)
        with self.assertRaises(ValueError):
            logarithm(-1,2)
        with self.assertRaises(ValueError):
            logarithm(-5,10)


    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3,4),5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(8, 6), 10)

        with self.assertRaises(ValueError):
            hypotenuse(-4,5)

        with self.assertRaises(ValueError):
            hypotenuse(4,-5)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        self.assertEqual(square_root(4), 2.0)
        self.assertEqual(square_root(16), 4.0)
        self.assertEqual(square_root(81), 9.0)

        with self.assertRaises(ValueError):
            square_root(-4)

    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(6, 7), 42)
        self.assertEqual(mul(2, 2), 4)
        self.assertEqual(mul(2, 3), 6)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(10,2),5)
        self.assertAlmostEqual(div(9,3),3)
        self.assertAlmostEqual(div(4,2),2)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()

# Main has not been touched (  owo)b