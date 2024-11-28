from TP7 import *
import unittest

class TestMethods(unittest.TestCase):

    def test_init(self):
        frac1 = Fraction(34,58)
        self.assertEqual(frac1.numerator,17)
        self.assertEqual(frac1.denominator,29)


    def test_string(self):
        frac_big = Fraction(34,58)
        self.assertEqual(frac_big.__str__(),"17/29")
        frac2 = Fraction(1,4)
        self.assertEqual(frac2.__str__(), "1/4")
        frac3 = Fraction(-1,2)
        self.assertEqual(frac3.__str__(), "-1/2")
        frac4 = Fraction(4,4)
        self.assertEqual(frac4.__str__(), "1")
        frac5 = Fraction(1,-5)
        self.assertEqual(frac5.__str__(), "-1/5")
        frac6 = Fraction(-1,-2)
        self.assertEqual(frac6.__str__(), "1/2")
        frac7 = Fraction(0,10)
        self.assertEqual(frac7.__str__(), "0")




if __name__ == '__main__':
    unittest.main()