from TP7 import *
import unittest

class TestMethods(unittest.TestCase):

    def test_init(self):
        frac1 = Fraction(34,58)
        self.assertEqual(frac1.numerator,17)
        self.assertEqual(frac1.denominator,29)


   # def test_string(self):


if __name__ == '__main__':
    unittest.main()