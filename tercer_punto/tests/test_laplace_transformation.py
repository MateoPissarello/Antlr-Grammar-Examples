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
        expected = 1 / (s - 2) + 1 / (s - 3)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
