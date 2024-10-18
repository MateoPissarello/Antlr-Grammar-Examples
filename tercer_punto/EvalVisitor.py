import sympy as sp
from LaplaceParser import LaplaceParser
from LaplaceVisitor import LaplaceVisitor

# Definir variables simbólicas para SymPy
t, s = sp.symbols("t s")


class EvalVisitor(LaplaceVisitor):

    # Método para manejar 'L[funcion]'
    def visitLaplaceExpr(self, ctx: LaplaceParser.LaplaceExprContext):
        # Visitar la función dentro de los corchetes L[...]
        func = self.visit(ctx.functionExpr())
        # Calcular la transformada de Laplace usando SymPy
        laplace_transform = sp.laplace_transform(func, t, s, noconds=True)
        print(f"Transformada de Laplace: {laplace_transform}")
        return laplace_transform

    # Método para manejar funciones exponenciales (e^at)
    def visitExpExpr(self, ctx: LaplaceParser.ExpExprContext):
        # Obtener el número del exponente
        a = float(ctx.NUMBER().getText())
        # Retornar e^(a*t) como una expresión simbólica en SymPy
        return sp.exp(a * t)

    # Método para manejar funciones seno (sin(at))
    def visitSinExpr(self, ctx: LaplaceParser.SinExprContext):
        # Obtener la frecuencia 'a' del seno
        a = float(ctx.NUMBER().getText())
        # Retornar sin(a*t) como una expresión simbólica en SymPy
        return sp.sin(a * t)

    # Método para manejar funciones coseno (cos(at))
    def visitCosExpr(self, ctx: LaplaceParser.CosExprContext):
        # Obtener la frecuencia 'a' del coseno
        a = float(ctx.NUMBER().getText())
        # Retornar cos(a*t) como una expresión simbólica en SymPy
        return sp.cos(a * t)

    # Método para manejar expresiones polinómicas (t^n)
    def visitTExpr(self, ctx: LaplaceParser.TExprContext):
        # Obtener el exponente de t
        n = int(ctx.NUMBER().getText())
        # Retornar t^n como una expresión simbólica en SymPy
        return t**n
