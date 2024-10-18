from antlr4 import *
from FractionCalcLexer import FractionCalcLexer
from FractionCalcParser import FractionCalcParser
from EvalVisitor import EvalVisitor  # Importa el visitor personalizado


def main():
    input_stream = InputStream(input("Introduce una expresión: "))
    lexer = FractionCalcLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FractionCalcParser(stream)
    tree = parser.prog()

    visitor = EvalVisitor()
    visitor.visit(tree)


if __name__ == "__main__":
    main()
