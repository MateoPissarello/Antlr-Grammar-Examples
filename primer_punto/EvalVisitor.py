from CustomFraction import CustomFraction
from FractionCalcParser import FractionCalcParser
from FractionCalcVisitor import FractionCalcVisitor


class EvalVisitor(FractionCalcVisitor):
    """
    EvalVisitor es una clase que extiende FractionCalcVisitor y se utiliza para evaluar expresiones aritméticas que involucran fracciones.
    Métodos:
        - visitProg(ctx: FractionCalcParser.ProgContext): Visita el nodo del programa y evalúa sus hijos.
        - visitPrintExpr(ctx: FractionCalcParser.PrintExprContext): Visita el nodo de impresión de expresión, evalúa la expresión y la imprime.
        - visitBlank(ctx: FractionCalcParser.BlankContext): Visita el nodo en blanco y no realiza ninguna acción.
        - visitParens(ctx: FractionCalcParser.ParensContext): Visita el nodo de paréntesis y evalúa la expresión dentro de los paréntesis.
        - visitMulDiv(ctx: FractionCalcParser.MulDivContext): Visita el nodo de multiplicación/división, evalúa las expresiones izquierda y derecha, y realiza la operación correspondiente.
        - visitAddSub(ctx: FractionCalcParser.AddSubContext): Visita el nodo de suma/resta, evalúa las expresiones izquierda y derecha, y realiza la operación correspondiente.
        - visitFractionExpr(ctx: FractionCalcParser.FractionExprContext): Visita el nodo de expresión de fracción, obtiene el numerador y el denominador, y retorna una fracción personalizada.
    """

    def visitProg(self, ctx: FractionCalcParser.ProgContext):
        """
        Visita el nodo 'Prog' en el árbol de análisis sintáctico.
        Args:
            ctx (FractionCalcParser.ProgContext): El contexto del nodo 'Prog'.
        Returns:
            El resultado de visitar los hijos del nodo 'Prog'.
        """

        return self.visitChildren(ctx)

    def visitPrintExpr(self, ctx: FractionCalcParser.PrintExprContext):
        """
        Visita el nodo de expresión de impresión y evalúa la expresión contenida.
        Args:
            ctx (FractionCalcParser.PrintExprContext): El contexto de la expresión de impresión.
        Returns:
            CustomFraction o cualquier otro tipo: El valor evaluado de la expresión.
        """

        value = self.visit(ctx.expr())
        if isinstance(value, CustomFraction):
            print(f"Resultado: {value}")
            print(f"Resultado simplificado: {value.simplify()}")
        else:
            print(f"Resultado: {value}")
        return value

    def visitBlank(self, ctx: FractionCalcParser.BlankContext):
        """
        Visita un nodo en blanco en el árbol de análisis.
        Este método se llama cuando se encuentra un nodo en blanco en el árbol de análisis
        generado por el parser de FractionCalc. No realiza ninguna acción y simplemente
        retorna None.
        Args:
            ctx (FractionCalcParser.BlankContext): El contexto del nodo en blanco.
        Returns:
            None: Siempre retorna None.
        """

        return None

    def visitParens(self, ctx: FractionCalcParser.ParensContext):
        """
        Visita el nodo de paréntesis en el árbol de análisis sintáctico.
        Args:
            ctx (FractionCalcParser.ParensContext): El contexto del nodo de paréntesis.
        Returns:
            El resultado de visitar la expresión dentro de los paréntesis.
        """

        return self.visit(ctx.expr())

    def visitMulDiv(self, ctx: FractionCalcParser.MulDivContext):
        """
        Visita los nodos de multiplicación y división en el árbol de análisis sintáctico.
        Args:
            ctx (FractionCalcParser.MulDivContext): El contexto del nodo actual en el árbol de análisis sintáctico.
        Returns:
            El resultado de la operación de multiplicación o división entre los dos operandos.
        """

        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if ctx.getChild(1).getText() == "*":
            return left * right
        elif ctx.getChild(1).getText() == "/":
            return left / right

    def visitAddSub(self, ctx: FractionCalcParser.AddSubContext):
        """
        Visita el nodo AddSub en el árbol de análisis y realiza la operación de suma o resta.
        Args:
            ctx (FractionCalcParser.AddSubContext): El contexto del nodo AddSub en el árbol de análisis.
        Returns:
            Fraction: El resultado de la operación de suma o resta entre las dos expresiones.
        """

        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if ctx.getChild(1).getText() == "+":
            return left + right
        elif ctx.getChild(1).getText() == "-":
            return left - right

    def visitFractionExpr(self, ctx: FractionCalcParser.FractionExprContext):
        """
        Visita una expresión de fracción y devuelve una instancia de CustomFraction.
        Args:
            ctx (FractionCalcParser.FractionExprContext): El contexto de la expresión de fracción.
        Returns:
            CustomFraction: Una instancia de CustomFraction con el numerador y denominador extraídos de la expresión.
        """

        numerator = int(ctx.fraction().INT(0).getText())
        denominator = int(ctx.fraction().INT(1).getText())
        return CustomFraction(numerator, denominator)
