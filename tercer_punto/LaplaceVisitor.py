# Generated from Laplace.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LaplaceParser import LaplaceParser
else:
    from LaplaceParser import LaplaceParser

# This class defines a complete generic visitor for a parse tree produced by LaplaceParser.

class LaplaceVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LaplaceParser#expr.
    def visitExpr(self, ctx:LaplaceParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#laplaceExpr.
    def visitLaplaceExpr(self, ctx:LaplaceParser.LaplaceExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#sumExpr.
    def visitSumExpr(self, ctx:LaplaceParser.SumExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#functionExpr.
    def visitFunctionExpr(self, ctx:LaplaceParser.FunctionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#numberExpr.
    def visitNumberExpr(self, ctx:LaplaceParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#expExpr.
    def visitExpExpr(self, ctx:LaplaceParser.ExpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#sinExpr.
    def visitSinExpr(self, ctx:LaplaceParser.SinExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#cosExpr.
    def visitCosExpr(self, ctx:LaplaceParser.CosExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#tExpr.
    def visitTExpr(self, ctx:LaplaceParser.TExprContext):
        return self.visitChildren(ctx)



del LaplaceParser