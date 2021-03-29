# Let's create tests to check if the code would be running without any errors

from simple_calc import SimpleCalc
# importing the file and class where we would write our code
import unittest
# importing unittest to inherit TestCase to create our tests against the code


class CalcTest(unittest.TestCase):
    calc = SimpleCalc()  # creating an object of our SimpleCalc class

    def test_add(self):  # Naming convention - using `test` in the name of our function will let
        # python interpreter know what needs to be tested
        self.assertEqual(self.calc.add(2, 4), 6)
        # this test is checking if 2 + 4 = 6 would be true if true test will pass

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
        # this test is checking if 4 - 2 = 2 would be true if true test will pass

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
        # this test is checking if 2 * 2 = 4 would be true if true test will pass

    def test_divide(self):
        self.assertEqual(self.calc.divide(15, 3), 5)
        # this test is checking if 15 / 3 = 5 would be true if true test will pass
