class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0 , den=1 ):
        """This builds a fraction based on some numerator and denominator.

            PRE : none
            POST : initialise les variables d'instances de l'object de classe Fraction, réduit la fraction au maximum et si le dénominateur est négatif, met le - au nominateur.
        """
        if den == 0:
            raise ValueError("Impossible de diviser par zéro")
        i = 0
        while i < 1:
            if den % num == 0 and num != 1:
                num = num/num
                den = den/num
            elif num % den == 0 and den != 1:
                num = num/den
                den = den/den
            else:
                i += 1
        self._num = num
        self._den = den
                

    @property
    def numerator(self):
        return self._num
    @property
    def denominator(self):
        return self._den

# ------------------ Textual representations ------------------

    def __str__(self) :
        """Return a textual representation of the reduced form of the fraction

        PRE : none
        POST : Retourne la fraction en chaine de caractère
        """
        return f"{self._num}/{self._den}"

    def as_mixed_number(self) :
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : -
        POST : Renvoie un entier et sa fraction restante
        Raise : ValueError si num < den 
        """
        if self._num < self._den:
            raise ValueError("le nominateur est plus grand que le dénominateur")
        if self._num % self._den == 0:
            return self._num / self._den
        else:
            integ = self._num - (self._num % self._den)
            frac = f"{self._num % self._den}/{self._den}"
            return f"{integ},{frac}"


    
# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : ?
         POST : ?
         """
        pass


    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : ?
        POST : ?
        """
        pass


    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : ?
        POST : ?
        """
        pass


    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : ?
        POST : ?
        """
        pass


    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : ?
        POST : ?
        """
        pass
    
    
    def __eq__(self, other) : 
        """Overloading of the == operator for fractions
        
        PRE : ?
        POST : ? 
        
        """
        
    def __float__(self) :
        """Returns the decimal value of the fraction

        PRE : ?
        POST : ?
        """
        pass
    
# TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)




# ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : ?
        POST : ?
        """
        pass


    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : ?
        POST : ?
        """
        pass

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : ?
        POST : ?
        """

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : ?
        POST : ?
        """
        pass

    def is_adjacent_to(self, other) :
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference is a unit fraction

        PRE : ?
        POST : ?
        """
        pass

