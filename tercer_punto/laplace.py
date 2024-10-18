from antlr4 import *
from LaplaceLexer import LaplaceLexer
from LaplaceParser import LaplaceParser
from EvalVisitor import EvalVisitor


def main():
    # Ejemplo de entrada: L[e^2t]
    expression = InputStream(
        input(
            "Ingresa una función para calcular la transformada de Laplace (L[funcion]): "
        )
    )

    # Crear lexer y parser
    lexer = LaplaceLexer(expression)
    stream = CommonTokenStream(lexer)
    parser = LaplaceParser(stream)

    # Parsear la expresión
    tree = parser.expr()

    # Usar el visitor para procesar la expresión y calcular la transformada
    visitor = EvalVisitor()
    visitor.visit(tree)


if __name__ == "__main__":
    main()
