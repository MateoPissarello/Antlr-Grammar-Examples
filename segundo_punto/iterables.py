from antlr4 import *
from IterableOpsLexer import IterableOpsLexer
from IterableOpsParser import IterableOpsParser
from EvalVisitor import EvalVisitor


def main():
    input_stream = InputStream(
        input("Introduce una expresión: ")
    )  # Leer entrada del usuario
    lexer = IterableOpsLexer(input_stream)  # Crear lexer
    token_stream = CommonTokenStream(lexer)  # Crear flujo de tokens
    parser = IterableOpsParser(token_stream)  # Crear parser
    tree = parser.prog()  # Parsear la entrada

    visitor = EvalVisitor()  # Crear instancia del visitante
    visitor.visit(tree)  # Visitar el árbol de parseo


if __name__ == "__main__":
    main()
