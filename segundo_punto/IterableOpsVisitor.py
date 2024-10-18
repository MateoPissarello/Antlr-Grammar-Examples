# Generated from IterableOps.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .IterableOpsParser import IterableOpsParser
else:
    from IterableOpsParser import IterableOpsParser

# This class defines a complete generic visitor for a parse tree produced by IterableOpsParser.

class IterableOpsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IterableOpsParser#prog.
    def visitProg(self, ctx:IterableOpsParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableOpsParser#statement.
    def visitStatement(self, ctx:IterableOpsParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableOpsParser#mapStatement.
    def visitMapStatement(self, ctx:IterableOpsParser.MapStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableOpsParser#filterStatement.
    def visitFilterStatement(self, ctx:IterableOpsParser.FilterStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableOpsParser#functionCall.
    def visitFunctionCall(self, ctx:IterableOpsParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableOpsParser#conditionFunction.
    def visitConditionFunction(self, ctx:IterableOpsParser.ConditionFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableOpsParser#argumentList.
    def visitArgumentList(self, ctx:IterableOpsParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableOpsParser#iterable.
    def visitIterable(self, ctx:IterableOpsParser.IterableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableOpsParser#list.
    def visitList(self, ctx:IterableOpsParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableOpsParser#tuple.
    def visitTuple(self, ctx:IterableOpsParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableOpsParser#expressionList.
    def visitExpressionList(self, ctx:IterableOpsParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableOpsParser#expression.
    def visitExpression(self, ctx:IterableOpsParser.ExpressionContext):
        return self.visitChildren(ctx)



del IterableOpsParser