class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num: int=0, den: int=1):
        """This builds a fraction based on some numerator and denominator.

            PRE : none
            POST : initialise les variables d'instances de l'object de classe Fraction, réduit la fraction au maximum et si le dénominateur est négatif, met le - au nominateur.
        """
        if den == 0:
            raise ValueError("Impossible de diviser par zéro")
        
        if den < 0:
            den = -den
            num = -num

        num_reduit = num
        den_reduit = den
        while den_reduit != 0:
            temp = num_reduit % den_reduit
            num_reduit = den_reduit
            den_reduit = temp

        self._num = num // num_reduit
        self._den = den // num_reduit
                

    @property
    def numerator(self):
        return self._num
    @property
    def denominator(self):
        return self._den

# ------------------ Textual representations ------------------

    def __str__(self) :
        """Return a textual representation of the reduced form of the fraction

        PRE : -
        POST : Retourne la fraction en chaine de caractère
        """
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return f"{self.numerator}/{self.denominator}"

    def as_mixed_number(self) :
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : -
        POST : Renvoie un entier et sa fraction restante
        Raise : ValueError si num < den 
        """
        if self.numerator < self.denominator:
            raise ValueError("le nominateur doit être plus grand que le dénominateur")
        if self.numerator % self.denominator == 0:
            return self.numerator // self.denominator
        else:
            integ = self.numerator - (self.numerator % self.denominator)
            frac = f"{self.numerator % self.denominator}/{self.denominator}"
            return f"{integ} et {frac}"


    
# ------------------ Operators overloading ------------------

    def __add__(self, other: object):
        """Overloading of the + operator for fractions

         PRE : -
         POST : Renvoie un nouvel objet issu de l'addition de notre object et de l'object other
         Raises : TypeError si other n'est pas un object de classe Fraction 
         """
        if not isinstance(other, Fraction):
            raise TypeError("other doit être un object de classe Fraction.")
        
        if self.denominator == other.denominator:
            new_num = self.numerator + other.numerator
            new_den = self.denominator
        else:
            new_num = (self.numerator * other.denominator) + (other.numerator * self.denominator)
            new_den = (self.denominator * other.denominator) + (other.denominator * self.denominator)  
        return Fraction(new_num,new_den)

    def __sub__(self, other: object):
        """Overloading of the - operator for fractions

        PRE : -
        POST : Renvoie un nouvel object issu de la soustraction de notre object et de l'object other
        Raises : TypeError si other n'est pas un object de classe Fraction 
        """
        if not isinstance(other, Fraction):
            raise TypeError("other doit être un object de classe Fraction.")
        
        if self.denominator == other.denominator:
            new_num = self.numerator - other.numerator
            new_den = self.denominator
        else:
            new_num = (self.numerator * other.denominator) - (other.numerator * self.denominator)
            new_den = self.denominator * other.denominator
        return Fraction(new_num,new_den)


    def __mul__(self, other: object):
        """Overloading of the * operator for fractions

        PRE : -
        POST : Renvoie un object issu de la multiplication de notre object et de l'objet other de class Fraction
        Raises : TypeError si other n'est pas un object de classe Fraction 
        """
        if not isinstance(other, Fraction):
            raise TypeError("other doit être un object de classe Fraction.")
        new_num = self.numerator * other.numerator
        new_den = self.denominator * self.denominator
        return Fraction(new_num,new_den)


    def __truediv__(self, other: object):
        """Overloading of the / operator for fractions

        PRE : -
        POST : Renvoie un object issu de la division de notre object et de l'objet other de class Fraction
        Raises : TypeError si other n'est pas un object de classe Fraction and ValueError si le numérateur de other est égale à 0
        """
        if not isinstance(other, Fraction):
            raise TypeError("other doit être un object de classe Fraction.")
        
        if other.numerator == 0:
            raise ValueError("Pas de division par 0")
        
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        return Fraction(new_num,new_den)


    def __pow__(self, other: int):
        """Overloading of the ** operator for fractions

        PRE : -
        POST : Renvoie un objet qui est la puissance other de notre object
        """  
        new_num = self.numerator ** other
        new_den = self.denominator ** other
        return Fraction(new_num,new_den)
    
    
    def __eq__(self, other: object) : 
        """Overloading of the == operator for fractions
        
        PRE : -
        POST : retourne True si les deux objects de class Fractions sont égaux
        Raises : TypeError si other n'est pas un object de classe Fraction and ValueError si le numérateur de other est égale à 0
        """
        if not isinstance(other, Fraction):
            raise TypeError("other doit être un object de classe Fraction.")
        if self.numerator == other.numerator and self.denominator == other.denominator:
            return True
        else:
            return False
        
    def __float__(self) :
        """Returns the decimal value of the fraction

        PRE : -
        POST : Retourne un float égal à la valeur de la fraction
        """
        return self.numerator / self.denominator
    
# TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)




# ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : -
        POST : Renvoie True si la fraction est égale à 0sinon renvoie False
        """
        if self.numerator == 0:
            return True
        else:
            return False
            


    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : -
        POST : Renvoie True si la Fraction est égale à un entier
        """
        if self.numerator % self.denominator == 0:
            return True
        else:
            return False
        

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : -
        POST : Renvoie True si la Fraction est égale à une valeur strictement en dessous de 1 
        """
        if abs(self.numerator) / abs(self.denominator) < 1:
            return True
        else:
            return False
        
    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : -
        POST : Renvoie True si le numérateur de notre object est égak à 1
        """
        if self.numerator == 1:
            return True
        else:
            return False

    def is_adjacent_to(self, other : object) :
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference is a unit fraction

        PRE : -
        POST : Retourne True si la valeur absolue de la différence entre 2 fractions est une  unité de fraction sinon false
        Raises : TypeError si other n'est pas un object de classe Fraction and ValueError si le numérateur de other est égale à 0
        """
        if not isinstance(other, Fraction):
            raise TypeError("other doit être un object de classe Fraction.") 
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        difference = Fraction(abs(new_num), new_den)
        return difference.numerator == 1 and difference.denominator != 0
    
f1 = Fraction(1,2)
f2 = Fraction(7,9)
f3 = Fraction(1,2)
f4 = Fraction(5,2)
f5 = Fraction(0,5)
f6 = Fraction(4,2)
f7 = Fraction(8,9)
if __name__ == "__main__":
    print(f1)
    print(f4.as_mixed_number())
    print(f1 + f2)
    print(f1 - f2)
    print(f1 * f2)
    print(f4 / f2)
    print(f1**4)
    print(f1 == f2)
    print(f1 == f3)
    print(f1.__float__())
    print(f5.is_zero())
    print(f4.is_zero())
    print(f6.is_integer())
    print(f1.is_proper())
    print(f6.is_proper())
    print(f1.is_unit())
    print(f2.is_adjacent_to(f7))



