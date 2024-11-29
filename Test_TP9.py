from TP7 import *
import unittest

class TestMethods(unittest.TestCase):

    def test_init(self):
        frac1 = Fraction(34,58)
        self.assertEqual(frac1.numerator,17)
        self.assertEqual(frac1.denominator,29)

    def test_init_zero(self):
        with self.assertRaises(ValueError):
            Fraction(3,0)


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

    def test_as_mixed_number(self):
        frac1 = Fraction(7, 3)
        self.assertEqual(frac1.as_mixed_number(), "2 and 1/3")

        frac2 = Fraction(6, 3)
        self.assertEqual(frac2.as_mixed_number(), "2")

        frac3 = Fraction(1, 3)
        self.assertEqual(frac3.as_mixed_number(), "0 and 1/3")

        frac4 = Fraction(-7, 3)
        self.assertEqual(frac4.as_mixed_number(), "-3 and 2/3")

        frac5 = Fraction(-9, 3)
        self.assertEqual(frac5.as_mixed_number(), "-3")

        frac6 = Fraction(0, 3)
        self.assertEqual(frac6.as_mixed_number(), "0")

    def test_add(self):
        # Test addition de fractions avec le même dénominateur
        frac1 = Fraction(3, 5)
        frac2 = Fraction(2, 5)
        result = frac1 + frac2
        self.assertEqual(result.numerator, 1)

        # +0
        frac3 = Fraction(3, 4)
        frac4 = Fraction(0, 3)
        result2 = frac3 + frac4
        self.assertEqual(result2.numerator, 3)
        self.assertEqual(result2.denominator, 4)

        frac5 = Fraction(-1, 2)
        frac6 = Fraction(1, 4)
        result3 = frac5 + frac6
        self.assertEqual(result3.numerator, -1)
        self.assertEqual(result3.denominator, 4)

        with self.assertRaises(TypeError):
            frac1 + 4

    def test_mul(self):
        frac1 = Fraction(3, 4)
        frac2 = Fraction(0, 5)
        with self.assertRaises(ValueError):
            frac1 / frac2

        with self.assertRaises(TypeError):
            frac1 / 2

        frac3 = Fraction(3, 4)
        frac4 = Fraction(2, 5)
        result1 = frac3 / frac4
        self.assertEqual(result1.numerator, 15)
        self.assertEqual(result1.denominator, 8)

        frac5 = Fraction(3, 4)
        frac6 = Fraction(-2, 5)
        result2 = frac5 / frac6
        self.assertEqual(result2.numerator, -15)
        self.assertEqual(result2.denominator, 8)

        frac7 = Fraction(3, 4)
        frac8 = Fraction(-2, 5)
        result3 = frac7 / frac8
        self.assertEqual(result3.numerator, -15)
        self.assertEqual(result3.denominator, 8)

    def test_eq(self):
        frac1 = Fraction(2, 3)
        frac2 = Fraction(2, 3)
        self.assertTrue(frac1 == frac2)


        frac3 = Fraction(3, 4)
        self.assertFalse(frac1 == frac3)

        frac5 = Fraction(0, 5)
        frac6 = Fraction(0, 10)
        self.assertTrue(frac5 == frac6)

        frac7 = Fraction(-2, 3)
        self.assertFalse(frac1 == frac7)

        with self.assertRaises(TypeError):
            frac1.__eq__(4)

    def test_is_integer(self):
        frac1 = Fraction(8, 4)
        self.assertTrue(frac1.is_integer())

        frac2 = Fraction(3, 1)
        self.assertTrue(frac2.is_integer())

        frac3 = Fraction(5, 3)
        self.assertFalse(frac3.is_integer())

        frac4 = Fraction(-8, 4)
        self.assertTrue(frac4.is_integer())

    def test_is_proper(self):
        frac1 = Fraction(1, 2)
        self.assertTrue(frac1.is_proper())

        frac2 = Fraction(-2, 5)
        self.assertTrue(frac2.is_proper())

        frac3 = Fraction(5, 3)
        self.assertFalse(frac3.is_proper())

        frac4 = Fraction(1, 1)
        self.assertFalse(frac4.is_proper())

        frac5 = Fraction(-2, 2)
        self.assertFalse(frac5.is_proper())

        frac_zero = Fraction(0, 10)
        self.assertTrue(frac_zero.is_proper())

    def test_is_adjacent(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(3, 2)
        self.assertTrue(frac1.is_adjacent_to(frac2))

        frac3 = Fraction(-1, 3)
        frac4 = Fraction(5, 6)
        self.assertFalse(frac3.is_adjacent_to(frac4))

        frac1 = Fraction(1, 2)  # 1/2
        with self.assertRaises(TypeError):
            frac1.is_adjacent_to("Not a fraction")


if __name__ == '__main__':
    unittest.main()