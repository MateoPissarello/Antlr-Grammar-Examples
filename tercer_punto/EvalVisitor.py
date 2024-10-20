import sympy as sp
from LaplaceParser import LaplaceParser
from LaplaceVisitor import LaplaceVisitor

# Definir variables simbólicas para SymPy
t, s = sp.symbols("t s")


class EvalVisitor(LaplaceVisitor):

    # Método para manejar 'L[funcion]'
    def visitLaplaceExpr(self, ctx: LaplaceParser.LaplaceExprContext):
        func = self.visit(
            ctx.expr()
        )  # Cambiado para usar expr en lugar de functionExpr
        laplace_transform = sp.laplace_transform(func, t, s, noconds=True)
        print(f"Transformada de Laplace: {self.format_result(laplace_transform)}")
        return laplace_transform

    # Método para manejar la suma de funciones
    def visitSumExpr(self, ctx: LaplaceParser.SumExprContext):
        result = self.visit(ctx.functionExpr(0))  # Obtener el primer término
        for i in range(1, len(ctx.functionExpr())):
            term = self.visit(ctx.functionExpr(i))
            if ctx.getChild(2 * i - 1).getText() == "+":
                result += term
            else:  # Debe ser '-'
                result -= term
        return result

    # Método para manejar funciones exponenciales (e^at)
    def visitExpExpr(self, ctx: LaplaceParser.ExpExprContext):
        a = float(ctx.NUMBER().getText())
        return sp.exp(a * t)

    # Método para manejar funciones seno (sin(at))
    def visitSinExpr(self, ctx: LaplaceParser.SinExprContext):
        a = float(ctx.NUMBER().getText())
        return sp.sin(a * t)

    # Método para manejar funciones coseno (cos(at))
    def visitCosExpr(self, ctx: LaplaceParser.CosExprContext):
        a = float(ctx.NUMBER().getText())
        return sp.cos(a * t)

    # Método para manejar expresiones polinómicas (t^n)
    def visitTExpr(self, ctx: LaplaceParser.TExprContext):
        n = int(ctx.NUMBER().getText())
        return t**n

    def format_result(self, result):
        """Formatea el resultado para que los enteros se representen sin decimales."""
        if isinstance(result, sp.Basic):
            simplified_result = result.simplify()  # simplifica la expresión
            return self.convert_to_int_if_needed(simplified_result)
        return self.convert_to_int_if_needed(result)

    # Método para manejar números
    def visitNumberExpr(self, ctx: LaplaceParser.NumberExprContext):
        return float(ctx.getText())  # Convertir el texto del número a float

    def convert_to_int_if_needed(self, expr):
        """Convierte expresiones que son números enteros a enteros en lugar de flotantes."""
        if expr.is_number:
            # Verificar si el número es entero y convertirlo
            if expr.is_integer:
                return int(expr)  # Devolver como un entero
            elif expr.is_real and expr == int(
                expr
            ):  # Verifica si es real y se puede representar como entero
                return int(expr)
        return expr
