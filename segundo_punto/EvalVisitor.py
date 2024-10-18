from antlr4 import *
from IterableOpsParser import IterableOpsParser
from IterableOpsVisitor import IterableOpsVisitor


class EvalVisitor(IterableOpsVisitor):

    def visitProg(self, ctx: IterableOpsParser.ProgContext):
        return self.visitChildren(ctx)

    def visitMapStatement(self, ctx: IterableOpsParser.MapStatementContext):
        function_name = ctx.functionCall().IDENTIFIER().getText()
        iterable_expr = ctx.iterable()

        # Evaluar el iterable
        iterable = self.visit(iterable_expr)
        result = self.map_function(function_name, iterable)
        print(f"Resultado de MAP: {result}")
        return result

    def visitFilterStatement(self, ctx: IterableOpsParser.FilterStatementContext):
        condition_function_name = ctx.conditionFunction().IDENTIFIER().getText()
        iterable_expr = ctx.iterable()

        iterable = self.visit(iterable_expr)
        result = self.filter_function(condition_function_name, iterable)
        print(f"Resultado de FILTER: {result}")
        return result

    def visitList(self, ctx: IterableOpsParser.ListContext):
        if ctx.expressionList():
            return [self.visit(expr) for expr in ctx.expressionList().expression()]
        return []

    def visitTuple(self, ctx: IterableOpsParser.TupleContext):
        if ctx.expressionList():
            return tuple(self.visit(expr) for expr in ctx.expressionList().expression())
        return ()

    def visitExpression(self, ctx: IterableOpsParser.ExpressionContext):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            # Aquí debes definir cómo obtener el valor de la variable, si corresponde
            return None  # Implementa lógica para manejar variables si es necesario

    def map_function(self, function_name, iterable):
        if function_name == "second_power":
            return [x * 2 for x in iterable]
        else:
            raise ValueError(f"Función '{function_name}' no definida")

    def filter_function(self, condition_function_name, iterable):
        if condition_function_name == "is_even":
            return [x for x in iterable if x % 2 == 0]
        else:
            raise ValueError(
                f"Función de condición '{condition_function_name}' no definida"
            )
