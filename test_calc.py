import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_plus(self):
        self.assertEqual(self.calculator.doMath(4, 7, '+'), 11)
        self.assertEqual(self.calculator.doMath(0, 1, '+'), 1)

    def test_minus(self):
        self.assertEqual(self.calculator.doMath(7, 2, '-'), 5)

    def test_divide(self):
        self.assertEqual(self.calculator.doMath(8, 0, '/'), "ERROR: ZERO DIVISION")
        self.assertEqual(self.calculator.doMath(8, 2, '/'), 4)

    def test_multiply(self):
        self.assertEqual(self.calculator.doMath(7, 2, '*'), 14)
        self.assertEqual(self.calculator.doMath(7, 0, '*'), 0)

    def test_bracket_count(self):
        self.assertEqual(self.calculator.bracketChecker('(())'), True)
        self.assertEqual(self.calculator.bracketChecker('))(('), False)
    def test_to_polish(self):
        self.assertEqual(self.calculator.convert_to_polish('1+2-5*3'), ['1','2','+','5','3','*','-'])


if __name__ == "__main__":
  unittest.main()