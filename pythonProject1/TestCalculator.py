import unittest
from Calculator import Calculator
class TestCalculator(unittest.TestCase):
    def SetUp(self):
        self.calculator = Calculator()
    def test_add(self):
        self.assertEqual(self.calculator.add(3,7), 10)
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(6,2), 4)
    def test_myltiply(self):
        self.assertEqual(self.calculator.myltiply(5,6), 30)
    def test_divide(self):
        self.assertEqual(self.calculator.divide(82,16), 5.125)
if __name__ == "__main__":
    unittest.main()


