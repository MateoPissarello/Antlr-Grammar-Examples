# Generated from Laplace.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LaplaceParser import LaplaceParser
else:
    from LaplaceParser import LaplaceParser

# This class defines a complete listener for a parse tree produced by LaplaceParser.
class LaplaceListener(ParseTreeListener):

    # Enter a parse tree produced by LaplaceParser#expr.
    def enterExpr(self, ctx:LaplaceParser.ExprContext):
        pass

    # Exit a parse tree produced by LaplaceParser#expr.
    def exitExpr(self, ctx:LaplaceParser.ExprContext):
        pass


    # Enter a parse tree produced by LaplaceParser#laplaceExpr.
    def enterLaplaceExpr(self, ctx:LaplaceParser.LaplaceExprContext):
        pass

    # Exit a parse tree produced by LaplaceParser#laplaceExpr.
    def exitLaplaceExpr(self, ctx:LaplaceParser.LaplaceExprContext):
        pass


    # Enter a parse tree produced by LaplaceParser#sumExpr.
    def enterSumExpr(self, ctx:LaplaceParser.SumExprContext):
        pass

    # Exit a parse tree produced by LaplaceParser#sumExpr.
    def exitSumExpr(self, ctx:LaplaceParser.SumExprContext):
        pass


    # Enter a parse tree produced by LaplaceParser#functionExpr.
    def enterFunctionExpr(self, ctx:LaplaceParser.FunctionExprContext):
        pass

    # Exit a parse tree produced by LaplaceParser#functionExpr.
    def exitFunctionExpr(self, ctx:LaplaceParser.FunctionExprContext):
        pass


    # Enter a parse tree produced by LaplaceParser#expExpr.
    def enterExpExpr(self, ctx:LaplaceParser.ExpExprContext):
        pass

    # Exit a parse tree produced by LaplaceParser#expExpr.
    def exitExpExpr(self, ctx:LaplaceParser.ExpExprContext):
        pass


    # Enter a parse tree produced by LaplaceParser#sinExpr.
    def enterSinExpr(self, ctx:LaplaceParser.SinExprContext):
        pass

    # Exit a parse tree produced by LaplaceParser#sinExpr.
    def exitSinExpr(self, ctx:LaplaceParser.SinExprContext):
        pass


    # Enter a parse tree produced by LaplaceParser#cosExpr.
    def enterCosExpr(self, ctx:LaplaceParser.CosExprContext):
        pass

    # Exit a parse tree produced by LaplaceParser#cosExpr.
    def exitCosExpr(self, ctx:LaplaceParser.CosExprContext):
        pass


    # Enter a parse tree produced by LaplaceParser#tExpr.
    def enterTExpr(self, ctx:LaplaceParser.TExprContext):
        pass

    # Exit a parse tree produced by LaplaceParser#tExpr.
    def exitTExpr(self, ctx:LaplaceParser.TExprContext):
        pass



del LaplaceParser