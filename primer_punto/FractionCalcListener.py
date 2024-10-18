# Generated from FractionCalc.g4 by ANTLR 4.13.2
from antlr4 import *

if "." in __name__:
    from .FractionCalcParser import FractionCalcParser
else:
    from FractionCalcParser import FractionCalcParser


# This class defines a complete listener for a parse tree produced by FractionCalcParser.
class FractionCalcListener(ParseTreeListener):
    # Enter a parse tree produced by FractionCalcParser#prog.
    def enterProg(self, ctx: FractionCalcParser.ProgContext):
        pass

    # Exit a parse tree produced by FractionCalcParser#prog.
    def exitProg(self, ctx: FractionCalcParser.ProgContext):
        pass

    # Enter a parse tree produced by FractionCalcParser#printExpr.
    def enterPrintExpr(self, ctx: FractionCalcParser.PrintExprContext):
        pass

    # Exit a parse tree produced by FractionCalcParser#printExpr.
    def exitPrintExpr(self, ctx: FractionCalcParser.PrintExprContext):
        pass

    # Enter a parse tree produced by FractionCalcParser#blank.
    def enterBlank(self, ctx: FractionCalcParser.BlankContext):
        pass

    # Exit a parse tree produced by FractionCalcParser#blank.
    def exitBlank(self, ctx: FractionCalcParser.BlankContext):
        pass

    # Enter a parse tree produced by FractionCalcParser#parens.
    def enterParens(self, ctx: FractionCalcParser.ParensContext):
        pass

    # Exit a parse tree produced by FractionCalcParser#parens.
    def exitParens(self, ctx: FractionCalcParser.ParensContext):
        pass

    # Enter a parse tree produced by FractionCalcParser#MulDiv.
    def enterMulDiv(self, ctx: FractionCalcParser.MulDivContext):
        pass

    # Exit a parse tree produced by FractionCalcParser#MulDiv.
    def exitMulDiv(self, ctx: FractionCalcParser.MulDivContext):
        pass

    # Enter a parse tree produced by FractionCalcParser#AddSub.
    def enterAddSub(self, ctx: FractionCalcParser.AddSubContext):
        pass

    # Exit a parse tree produced by FractionCalcParser#AddSub.
    def exitAddSub(self, ctx: FractionCalcParser.AddSubContext):
        pass

    # Enter a parse tree produced by FractionCalcParser#fractionExpr.
    def enterFractionExpr(self, ctx: FractionCalcParser.FractionExprContext):
        pass

    # Exit a parse tree produced by FractionCalcParser#fractionExpr.
    def exitFractionExpr(self, ctx: FractionCalcParser.FractionExprContext):
        pass

    # Enter a parse tree produced by FractionCalcParser#fraction.
    def enterFraction(self, ctx: FractionCalcParser.FractionContext):
        pass

    # Exit a parse tree produced by FractionCalcParser#fraction.
    def exitFraction(self, ctx: FractionCalcParser.FractionContext):
        pass


del FractionCalcParser
