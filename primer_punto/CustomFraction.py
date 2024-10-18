class CustomFraction:
    """
    Una clase para representar fracciones y realizar operaciones aritméticas con ellas.
    Atributos:
    ----------
    numerator : int
        El numerador de la fracción.
    denominator : int
        El denominador de la fracción.
    Métodos:
    --------
    __init__(self, numerator, denominator):
        Inicializa una nueva instancia de CustomFraction con el numerador y denominador dados.
    __str__(self):
        Devuelve una representación en cadena de la fracción en el formato "numerador/denominador".
    __add__(self, other):
        Suma dos fracciones y devuelve una nueva instancia de CustomFraction con el resultado.
    __sub__(self, other):
        Resta dos fracciones y devuelve una nueva instancia de CustomFraction con el resultado.
    __mul__(self, other):
        Multiplica dos fracciones y devuelve una nueva instancia de CustomFraction con el resultado.
    __truediv__(self, other):
        Divide dos fracciones y devuelve una nueva instancia de CustomFraction con el resultado.
    simplify(self):
        Simplifica la fracción actual y devuelve la instancia simplificada de CustomFraction.
    to_fraction(self):
        Convierte la fracción actual a una instancia de Fraction de la librería fractions.
    """

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = (
            self.numerator * other.denominator + other.numerator * self.denominator
        )
        new_denominator = self.denominator * other.denominator
        return CustomFraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = (
            self.numerator * other.denominator - other.numerator * self.denominator
        )
        new_denominator = self.denominator * other.denominator
        return CustomFraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return CustomFraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return CustomFraction(new_numerator, new_denominator)

    def simplify(self):
        # Método para simplificar la fracción manualmente, si lo deseas
        from math import gcd

        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // common_divisor
        self.denominator = self.denominator // common_divisor
        return self

    def to_fraction(self):

        from fractions import Fraction

        return Fraction(self.numerator, self.denominator)
