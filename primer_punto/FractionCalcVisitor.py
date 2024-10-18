# Generated from FractionCalc.g4 by ANTLR 4.13.2
from antlr4 import *

if "." in __name__:
    from .FractionCalcParser import FractionCalcParser
else:
    from FractionCalcParser import FractionCalcParser

# This class defines a complete generic visitor for a parse tree produced by FractionCalcParser.


class FractionCalcVisitor(ParseTreeVisitor):
    # Visit a parse tree produced by FractionCalcParser#prog.
    def visitProg(self, ctx: FractionCalcParser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FractionCalcParser#printExpr.
    def visitPrintExpr(self, ctx: FractionCalcParser.PrintExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FractionCalcParser#blank.
    def visitBlank(self, ctx: FractionCalcParser.BlankContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FractionCalcParser#parens.
    def visitParens(self, ctx: FractionCalcParser.ParensContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FractionCalcParser#MulDiv.
    def visitMulDiv(self, ctx: FractionCalcParser.MulDivContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FractionCalcParser#AddSub.
    def visitAddSub(self, ctx: FractionCalcParser.AddSubContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FractionCalcParser#fractionExpr.
    def visitFractionExpr(self, ctx: FractionCalcParser.FractionExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FractionCalcParser#fraction.
    def visitFraction(self, ctx: FractionCalcParser.FractionContext):
        return self.visitChildren(ctx)


del FractionCalcParser
