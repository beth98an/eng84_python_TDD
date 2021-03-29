# Let's create tests to check if the code would be running without any errors

from simple_calc import SimpleCalc:
# importing the file and class where we would write our code
import unittest
#

class CalcTest(unittest.TestCase):
    calc = SimpleCalc()

    def test_add(self):
