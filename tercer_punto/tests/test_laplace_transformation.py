import sys
import os

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import sympy as sp
from antlr4 import *
from LaplaceLexer import LaplaceLexer
from LaplaceParser import LaplaceParser
from EvalVisitor import EvalVisitor

# Definir las variables simbólicas globalmente para SymPy
t, s = sp.symbols("t s")


class TestLaplaceTransform(unittest.TestCase):

    def evaluate(self, expression):
        lexer = LaplaceLexer(InputStream(expression))
        stream = CommonTokenStream(lexer)
        parser = LaplaceParser(stream)
        tree = parser.expr()
        visitor = EvalVisitor()
        return visitor.visit(tree)

    def test_number(self):
        result = self.evaluate("L[3]")
        expected = 3.0 / s
        self.assertEqual(result, expected)

    def test_exp(self):
        result = self.evaluate("L[e^2t]")
        expected = 1 / (s - 2.0)
        self.assertEqual(result, expected)

    def test_sin(self):
        result = self.evaluate("L[sin(3t)]")
        expected = 3.0 / (s**2 + 9.0)
        self.assertEqual(result, expected)

    def test_cos(self):
        result = self.evaluate("L[cos(4t)]")
        expected = s / (s**2 + 16.0)
        self.assertEqual(result, expected)

    def test_t_squared(self):
        result = self.evaluate("L[t^2]")
        expected = 2 / s**3
        self.assertEqual(result, expected)

    def test_exp_combined(self):
        result = self.evaluate("L[e^(2t) + e^(3t)]")
        expected = 1 / (s - 2.0) + 1 / (s - 3.0)
        self.assertEqual(result, expected)

    # Nuevas pruebas añadidas
    def test_sin_combined(self):
        result = self.evaluate("L[sin(1t) + sin(2t)]")
        expected = 1 / (s**2 + 1.0) + 2.0 / (s**2 + 4.0)
        self.assertEqual(result, expected)

    def test_cos_combined(self):
        result = self.evaluate("L[cos(1t) + cos(3t)]")
        expected = s / (s**2 + 1.0) + s / (s**2 + 9.0)
        self.assertEqual(result, expected)

    def test_exp_and_sin(self):
        result = self.evaluate("L[e^(2t) * sin(3t)]")
        expected = 3.0 / ((s - 2.0) ** 2 + 9.0)
        self.assertEqual(result, expected)

    def test_exp_and_cos(self):
        result = self.evaluate("L[e^(3t) * cos(2t)]")
        expected = (s - 3.0) / ((s - 3.0) ** 2 + 4.0)
        self.assertEqual(result, expected)

    def test_t_cubed(self):
        result = self.evaluate("L[t^3]")
        expected = 6 / s**4
        self.assertEqual(result, expected)

    def test_sin_combined_with_coefficient(self):
        result = self.evaluate("L[5 * sin(4t)]")
        expected = 5 * 4.0 / (s**2 + 16.0)
        self.assertEqual(result, expected)

    def test_exp_minus(self):
        result = self.evaluate("L[e^(2t) - e^(3t)]")
        expected = 1 / (s - 2.0) - 1 / (s - 3.0)
        self.assertEqual(result, expected)

    def test_t_and_exp_combined(self):
        result = self.evaluate("L[t * e^(4t)]")
        expected = 1 / (s - 4.0) ** 2
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
