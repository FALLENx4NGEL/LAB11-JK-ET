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
        self.assertLessEqual(self.a, 0, 'Domain Error: A must be greater than 1!')

    def test_hypotenuse(self): # 3 assertions
        self.assertGreater(self.a, 0, 'hmmst')
        self.assertGreater(self.b, 0, 'hmmst')
        self.assertGreater(hypotenuse(self.a, self.b), 0, 'hmmst')

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        self.assertRaises(self, ValueError, 'Cannot take a square root of a negative value!')


    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(6,7), 43)
        self.assertEqual(mul(2,2), 4)
        self.assertEqual(mul(2,3), 6)

    def test_divide(self): # 3 assertions
        try:
             div(self.a,self.b)
        except ZeroDivisionError:
            print('Invalid Argument')
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()

# Main has not been touched (  owo)b