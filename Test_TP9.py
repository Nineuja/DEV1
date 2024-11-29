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
        # Cas où le numérateur est plus grand que le dénominateur (cas standard)
        frac1 = Fraction(7, 3)  # 7/3 -> 2 and 1/3
        self.assertEqual(frac1.as_mixed_number(), "2 and 1/3")

        # Cas où le numérateur est divisible par le dénominateur
        frac2 = Fraction(6, 3)  # 6/3 -> 2
        self.assertEqual(frac2.as_mixed_number(), "2")

        # Cas où le numérateur est plus petit que le dénominateur (fraction propre)
        frac3 = Fraction(1, 3)  # 1/3 -> doit renvoyer "0" car il n'y a pas de partie entière
        self.assertEqual(frac3.as_mixed_number(), "0")

        # Cas avec fraction négative où le numérateur est plus grand que le dénominateur
        frac4 = Fraction(-7, 3)  # -7/3 -> -2 and -1/3
        self.assertEqual(frac4.as_mixed_number(), "-2 and -1/3")

        # Cas avec fraction négative et divisible (entier)
        frac5 = Fraction(-9, 3)  # -9/3 -> -3
        self.assertEqual(frac5.as_mixed_number(), "-3")

        # Cas de fraction positive et divisible (entier)
        frac6 = Fraction(9, 3)  # 9/3 -> 3
        self.assertEqual(frac6.as_mixed_number(), "3")

        # Cas avec une fraction simplifiée
        frac7 = Fraction(34, 58)  # 34/58 simplifié à 17/29
        self.assertEqual(frac7.as_mixed_number(), "0")

        # Cas avec une fraction négative simplifiée
        frac8 = Fraction(-34, 58)  # -34/58 simplifié à -17/29
        self.assertEqual(frac8.as_mixed_number(), "0")

        # Cas avec fraction positive où la partie fractionnelle est plus petite que l'entier
        frac9 = Fraction(15, 8)  # 15/8 -> 1 and 7/8
        self.assertEqual(frac9.as_mixed_number(), "1 and 7/8")

        # Cas avec numérateur égal à zéro
        frac10 = Fraction(0, 5)  # 0/5 -> 0
        self.assertEqual(frac10.as_mixed_number(), "0")

if __name__ == '__main__':
    unittest.main()