# https://github.com/FALLENx4NGEL/LAB11-JK-ET

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        #  INPUT ERROR (MUST BE > 0)
        with self.assertRaises(ZeroDivisionError):
            log(5, 5)
            log(9,10)
            log(4, 20)


    def test_hypotenuse(self): # 3 assertions
        with self.assertRaises(ZeroDivisionError):
            hypotenuse(4,9)
            hypotenuse(8, 5)
            hypotenuse(8, 7)

        with self.assertRaises(ValueError):
            hypotenuse(4,5)
            hypotenuse(6,7)
            hypotenuse(4,21)

        with self.assertRaises(TypeError):
            hypotenuse(5, 10)
            hypotenuse(6, 7)
            hypotenuse(4, 21)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ValueError):
            square_root(4)
            square_root(16)
            square_root(81)


    def test_multiply(self): # 3 assertions
        with self.assertRaises(ValueError):
            self.assertEqual(mul(6, 7), 42)
            self.assertEqual(mul(2, 2), 4)
            self.assertEqual(mul(2, 3), 6)
        with self.assertRaises(TypeError):
            self.assertEqual(mul(6, 7), 42)
            self.assertEqual(mul(2, 2), 4)
            self.assertEqual(mul(2, 3), 6)
        with self.assertRaises(OverflowError):
            self.assertEqual(mul(6, 7), 42)
            self.assertEqual(mul(2, 2), 4)
            self.assertEqual(mul(2, 3), 6)



    def test_divide(self): # 3 assertions
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(div(42,7), 6)
            self.assertEqual(div(2, 2), 1)
            self.assertEqual(div(5, 5), 1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()

# Main has not been touched (  owo)b