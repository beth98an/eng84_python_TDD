# TDD - Test Driven Development
## Why should we use TDD
### What are the benefits of TDD


**Best Use Cases**
- We will use Pytest unittest in Python to implement TDD
- TDD is widely used and is the cheapest way to test the code or implement test driven development

**Best practises for TDD**
- write the smallest possible test case that matches what we need to program
- TDD cycle start with everything failing - `RED`
- Write code to pass the test `GREEN`
- Refactor the code for the next test `BLUE`
- this continues until all the test have successfully passed

|Method |   Checks that|   New in |
|:---|:---|:---|
|assertEqual(a, b)        | a == b              ||
|assertNotEqual(a, b)     |    a != b              ||  
|assertTrue(x)            |    bool(x) is True     ||  
|assertFalse(x)           |    bool(x) is False    ||  
|assertIs(a, b)           |    a is b             |3.1|
|assertIsNot(a, b)        |    a is not b          |3.1|
|assertIsNone(x)          |    x is None           |3.1|
|assertIsNotNone(x)       |    x is not None       |3.1|
|assertIn(a, b)           |    a in b              |3.1|
|assertNotIn(a, b)        |    a not in b         |3.1|
|assertIsInstance(a, b)   |    isinstance(a, b)    |3.2|
|assertNotIsInstance(a, b)|    not isinstance(a, b)|3.2| 


- Let's create a file called `test_unittest_simplecalc.py`
- Naming convention is extremely important 

- `python -m pytest` to run the test.
```
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
```
```
class SimpleCalc:

    def add(self, value1, value2):
        return value1 + value2
        # this function adds the values for value1 and value2 against the test we have in other class

    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        return value1 / value2
```
- Running the test with `python -m unittest discover -v`
```
python -m unittest discover -v
test_add (test_unittest_simplecalc.CalcTest) ... ok
test_divide (test_unittest_simplecalc.CalcTest) ... ok
test_multiply (test_unittest_simplecalc.CalcTest) ... ok
test_subtract (test_unittest_simplecalc.CalcTest) ... ok

----------------------------------------------------------------
------
Ran 4 tests in 0.005s

OK
```
