# Generated from FractionCalc.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,
        1,
        9,
        43,
        2,
        0,
        7,
        0,
        2,
        1,
        7,
        1,
        2,
        2,
        7,
        2,
        2,
        3,
        7,
        3,
        1,
        0,
        4,
        0,
        10,
        8,
        0,
        11,
        0,
        12,
        0,
        11,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        3,
        1,
        18,
        8,
        1,
        1,
        2,
        1,
        2,
        1,
        2,
        1,
        2,
        1,
        2,
        1,
        2,
        3,
        2,
        26,
        8,
        2,
        1,
        2,
        1,
        2,
        1,
        2,
        1,
        2,
        1,
        2,
        1,
        2,
        5,
        2,
        34,
        8,
        2,
        10,
        2,
        12,
        2,
        37,
        9,
        2,
        1,
        3,
        1,
        3,
        1,
        3,
        1,
        3,
        1,
        3,
        0,
        1,
        4,
        4,
        0,
        2,
        4,
        6,
        0,
        2,
        1,
        0,
        1,
        2,
        1,
        0,
        3,
        4,
        43,
        0,
        9,
        1,
        0,
        0,
        0,
        2,
        17,
        1,
        0,
        0,
        0,
        4,
        25,
        1,
        0,
        0,
        0,
        6,
        38,
        1,
        0,
        0,
        0,
        8,
        10,
        3,
        2,
        1,
        0,
        9,
        8,
        1,
        0,
        0,
        0,
        10,
        11,
        1,
        0,
        0,
        0,
        11,
        9,
        1,
        0,
        0,
        0,
        11,
        12,
        1,
        0,
        0,
        0,
        12,
        1,
        1,
        0,
        0,
        0,
        13,
        14,
        3,
        4,
        2,
        0,
        14,
        15,
        5,
        8,
        0,
        0,
        15,
        18,
        1,
        0,
        0,
        0,
        16,
        18,
        5,
        8,
        0,
        0,
        17,
        13,
        1,
        0,
        0,
        0,
        17,
        16,
        1,
        0,
        0,
        0,
        18,
        3,
        1,
        0,
        0,
        0,
        19,
        20,
        6,
        2,
        -1,
        0,
        20,
        26,
        3,
        6,
        3,
        0,
        21,
        22,
        5,
        5,
        0,
        0,
        22,
        23,
        3,
        4,
        2,
        0,
        23,
        24,
        5,
        6,
        0,
        0,
        24,
        26,
        1,
        0,
        0,
        0,
        25,
        19,
        1,
        0,
        0,
        0,
        25,
        21,
        1,
        0,
        0,
        0,
        26,
        35,
        1,
        0,
        0,
        0,
        27,
        28,
        10,
        4,
        0,
        0,
        28,
        29,
        7,
        0,
        0,
        0,
        29,
        34,
        3,
        4,
        2,
        5,
        30,
        31,
        10,
        3,
        0,
        0,
        31,
        32,
        7,
        1,
        0,
        0,
        32,
        34,
        3,
        4,
        2,
        4,
        33,
        27,
        1,
        0,
        0,
        0,
        33,
        30,
        1,
        0,
        0,
        0,
        34,
        37,
        1,
        0,
        0,
        0,
        35,
        33,
        1,
        0,
        0,
        0,
        35,
        36,
        1,
        0,
        0,
        0,
        36,
        5,
        1,
        0,
        0,
        0,
        37,
        35,
        1,
        0,
        0,
        0,
        38,
        39,
        5,
        7,
        0,
        0,
        39,
        40,
        5,
        2,
        0,
        0,
        40,
        41,
        5,
        7,
        0,
        0,
        41,
        7,
        1,
        0,
        0,
        0,
        5,
        11,
        17,
        25,
        33,
        35,
    ]


class FractionCalcParser(Parser):
    grammarFileName = "FractionCalc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'*'", "'/'", "'+'", "'-'", "'('", "')'"]

    symbolicNames = [
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "INT",
        "NEWLINE",
        "WS",
    ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_fraction = 3

    ruleNames = ["prog", "stat", "expr", "fraction"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    INT = 7
    NEWLINE = 8
    WS = 9

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache
        )
        self._predicates = None

    class ProgContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(FractionCalcParser.StatContext)
            else:
                return self.getTypedRuleContext(FractionCalcParser.StatContext, i)

        def getRuleIndex(self):
            return FractionCalcParser.RULE_prog

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterProg"):
                listener.enterProg(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitProg"):
                listener.exitProg(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitProg"):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)

    def prog(self):
        localctx = FractionCalcParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.stat()
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3F) == 0 and ((1 << _la) & 416) != 0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return FractionCalcParser.RULE_stat

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class BlankContext(StatContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a FractionCalcParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(FractionCalcParser.NEWLINE, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBlank"):
                listener.enterBlank(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBlank"):
                listener.exitBlank(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBlank"):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)

    class PrintExprContext(StatContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a FractionCalcParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(FractionCalcParser.ExprContext, 0)

        def NEWLINE(self):
            return self.getToken(FractionCalcParser.NEWLINE, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterPrintExpr"):
                listener.enterPrintExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitPrintExpr"):
                listener.exitPrintExpr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitPrintExpr"):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)

    def stat(self):
        localctx = FractionCalcParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 7]:
                localctx = FractionCalcParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.expr(0)
                self.state = 14
                self.match(FractionCalcParser.NEWLINE)
                pass
            elif token in [8]:
                localctx = FractionCalcParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(FractionCalcParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return FractionCalcParser.RULE_expr

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class ParensContext(ExprContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a FractionCalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(FractionCalcParser.ExprContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterParens"):
                listener.enterParens(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitParens"):
                listener.exitParens(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitParens"):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)

    class MulDivContext(ExprContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a FractionCalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(FractionCalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(FractionCalcParser.ExprContext, i)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterMulDiv"):
                listener.enterMulDiv(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitMulDiv"):
                listener.exitMulDiv(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMulDiv"):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)

    class AddSubContext(ExprContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a FractionCalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(FractionCalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(FractionCalcParser.ExprContext, i)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAddSub"):
                listener.enterAddSub(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAddSub"):
                listener.exitAddSub(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAddSub"):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)

    class FractionExprContext(ExprContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a FractionCalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fraction(self):
            return self.getTypedRuleContext(FractionCalcParser.FractionContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFractionExpr"):
                listener.enterFractionExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFractionExpr"):
                listener.exitFractionExpr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitFractionExpr"):
                return visitor.visitFractionExpr(self)
            else:
                return visitor.visitChildren(self)

    def expr(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = FractionCalcParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = FractionCalcParser.FractionExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 20
                self.fraction()
                pass
            elif token in [5]:
                localctx = FractionCalcParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 21
                self.match(FractionCalcParser.T__4)
                self.state = 22
                self.expr(0)
                self.state = 23
                self.match(FractionCalcParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 4, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 33
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 3, self._ctx)
                    if la_ == 1:
                        localctx = FractionCalcParser.MulDivContext(
                            self,
                            FractionCalcParser.ExprContext(
                                self, _parentctx, _parentState
                            ),
                        )
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_expr
                        )
                        self.state = 27
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 4)"
                            )
                        self.state = 28
                        _la = self._input.LA(1)
                        if not (_la == 1 or _la == 2):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 29
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = FractionCalcParser.AddSubContext(
                            self,
                            FractionCalcParser.ExprContext(
                                self, _parentctx, _parentState
                            ),
                        )
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_expr
                        )
                        self.state = 30
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 3)"
                            )
                        self.state = 31
                        _la = self._input.LA(1)
                        if not (_la == 3 or _la == 4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 32
                        self.expr(4)
                        pass

                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 4, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class FractionContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i: int = None):
            if i is None:
                return self.getTokens(FractionCalcParser.INT)
            else:
                return self.getToken(FractionCalcParser.INT, i)

        def getRuleIndex(self):
            return FractionCalcParser.RULE_fraction

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFraction"):
                listener.enterFraction(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFraction"):
                listener.exitFraction(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitFraction"):
                return visitor.visitFraction(self)
            else:
                return visitor.visitChildren(self)

    def fraction(self):
        localctx = FractionCalcParser.FractionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_fraction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(FractionCalcParser.INT)
            self.state = 39
            self.match(FractionCalcParser.T__1)
            self.state = 40
            self.match(FractionCalcParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx: ExprContext, predIndex: int):
        if predIndex == 0:
            return self.precpred(self._ctx, 4)

        if predIndex == 1:
            return self.precpred(self._ctx, 3)
