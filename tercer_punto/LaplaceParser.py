# Generated from Laplace.g4 by ANTLR 4.13.2
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
        4,1,13,60,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,3,0,22,8,0,1,1,1,1,1,1,1,1,1,1,1,2,
        1,2,1,2,5,2,32,8,2,10,2,12,2,35,9,2,1,3,1,3,1,3,1,3,3,3,41,8,3,1,
        4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,
        8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,1,1,0,4,5,56,0,21,1,0,0,0,2,
        23,1,0,0,0,4,28,1,0,0,0,6,40,1,0,0,0,8,42,1,0,0,0,10,44,1,0,0,0,
        12,48,1,0,0,0,14,52,1,0,0,0,16,56,1,0,0,0,18,22,3,2,1,0,19,22,3,
        4,2,0,20,22,3,8,4,0,21,18,1,0,0,0,21,19,1,0,0,0,21,20,1,0,0,0,22,
        1,1,0,0,0,23,24,5,1,0,0,24,25,5,2,0,0,25,26,3,0,0,0,26,27,5,3,0,
        0,27,3,1,0,0,0,28,33,3,6,3,0,29,30,7,0,0,0,30,32,3,6,3,0,31,29,1,
        0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,5,1,0,0,0,35,
        33,1,0,0,0,36,41,3,10,5,0,37,41,3,12,6,0,38,41,3,14,7,0,39,41,3,
        16,8,0,40,36,1,0,0,0,40,37,1,0,0,0,40,38,1,0,0,0,40,39,1,0,0,0,41,
        7,1,0,0,0,42,43,5,12,0,0,43,9,1,0,0,0,44,45,5,6,0,0,45,46,5,12,0,
        0,46,47,5,7,0,0,47,11,1,0,0,0,48,49,5,8,0,0,49,50,5,12,0,0,50,51,
        5,9,0,0,51,13,1,0,0,0,52,53,5,10,0,0,53,54,5,12,0,0,54,55,5,9,0,
        0,55,15,1,0,0,0,56,57,5,11,0,0,57,58,5,12,0,0,58,17,1,0,0,0,3,21,
        33,40
    ]

class LaplaceParser ( Parser ):

    grammarFileName = "Laplace.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'L'", "'['", "']'", "'+'", "'-'", "'e^'", 
                     "'t'", "'sin('", "'t)'", "'cos('", "'t^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "WS" ]

    RULE_expr = 0
    RULE_laplaceExpr = 1
    RULE_sumExpr = 2
    RULE_functionExpr = 3
    RULE_numberExpr = 4
    RULE_expExpr = 5
    RULE_sinExpr = 6
    RULE_cosExpr = 7
    RULE_tExpr = 8

    ruleNames =  [ "expr", "laplaceExpr", "sumExpr", "functionExpr", "numberExpr", 
                   "expExpr", "sinExpr", "cosExpr", "tExpr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    NUMBER=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def laplaceExpr(self):
            return self.getTypedRuleContext(LaplaceParser.LaplaceExprContext,0)


        def sumExpr(self):
            return self.getTypedRuleContext(LaplaceParser.SumExprContext,0)


        def numberExpr(self):
            return self.getTypedRuleContext(LaplaceParser.NumberExprContext,0)


        def getRuleIndex(self):
            return LaplaceParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = LaplaceParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.laplaceExpr()
                pass
            elif token in [6, 8, 10, 11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.sumExpr()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 20
                self.numberExpr()
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


    class LaplaceExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LaplaceParser.ExprContext,0)


        def getRuleIndex(self):
            return LaplaceParser.RULE_laplaceExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLaplaceExpr" ):
                listener.enterLaplaceExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLaplaceExpr" ):
                listener.exitLaplaceExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLaplaceExpr" ):
                return visitor.visitLaplaceExpr(self)
            else:
                return visitor.visitChildren(self)




    def laplaceExpr(self):

        localctx = LaplaceParser.LaplaceExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_laplaceExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(LaplaceParser.T__0)
            self.state = 24
            self.match(LaplaceParser.T__1)
            self.state = 25
            self.expr()
            self.state = 26
            self.match(LaplaceParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SumExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LaplaceParser.FunctionExprContext)
            else:
                return self.getTypedRuleContext(LaplaceParser.FunctionExprContext,i)


        def getRuleIndex(self):
            return LaplaceParser.RULE_sumExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumExpr" ):
                listener.enterSumExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumExpr" ):
                listener.exitSumExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumExpr" ):
                return visitor.visitSumExpr(self)
            else:
                return visitor.visitChildren(self)




    def sumExpr(self):

        localctx = LaplaceParser.SumExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sumExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.functionExpr()
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4 or _la==5:
                self.state = 29
                _la = self._input.LA(1)
                if not(_la==4 or _la==5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 30
                self.functionExpr()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expExpr(self):
            return self.getTypedRuleContext(LaplaceParser.ExpExprContext,0)


        def sinExpr(self):
            return self.getTypedRuleContext(LaplaceParser.SinExprContext,0)


        def cosExpr(self):
            return self.getTypedRuleContext(LaplaceParser.CosExprContext,0)


        def tExpr(self):
            return self.getTypedRuleContext(LaplaceParser.TExprContext,0)


        def getRuleIndex(self):
            return LaplaceParser.RULE_functionExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionExpr" ):
                listener.enterFunctionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionExpr" ):
                listener.exitFunctionExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionExpr" ):
                return visitor.visitFunctionExpr(self)
            else:
                return visitor.visitChildren(self)




    def functionExpr(self):

        localctx = LaplaceParser.FunctionExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functionExpr)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.expExpr()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.sinExpr()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.cosExpr()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 39
                self.tExpr()
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


    class NumberExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(LaplaceParser.NUMBER, 0)

        def getRuleIndex(self):
            return LaplaceParser.RULE_numberExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)




    def numberExpr(self):

        localctx = LaplaceParser.NumberExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_numberExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(LaplaceParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(LaplaceParser.NUMBER, 0)

        def getRuleIndex(self):
            return LaplaceParser.RULE_expExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpExpr" ):
                listener.enterExpExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpExpr" ):
                listener.exitExpExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpExpr" ):
                return visitor.visitExpExpr(self)
            else:
                return visitor.visitChildren(self)




    def expExpr(self):

        localctx = LaplaceParser.ExpExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(LaplaceParser.T__5)
            self.state = 45
            self.match(LaplaceParser.NUMBER)
            self.state = 46
            self.match(LaplaceParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SinExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(LaplaceParser.NUMBER, 0)

        def getRuleIndex(self):
            return LaplaceParser.RULE_sinExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinExpr" ):
                listener.enterSinExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinExpr" ):
                listener.exitSinExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinExpr" ):
                return visitor.visitSinExpr(self)
            else:
                return visitor.visitChildren(self)




    def sinExpr(self):

        localctx = LaplaceParser.SinExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_sinExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(LaplaceParser.T__7)
            self.state = 49
            self.match(LaplaceParser.NUMBER)
            self.state = 50
            self.match(LaplaceParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CosExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(LaplaceParser.NUMBER, 0)

        def getRuleIndex(self):
            return LaplaceParser.RULE_cosExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCosExpr" ):
                listener.enterCosExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCosExpr" ):
                listener.exitCosExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCosExpr" ):
                return visitor.visitCosExpr(self)
            else:
                return visitor.visitChildren(self)




    def cosExpr(self):

        localctx = LaplaceParser.CosExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cosExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(LaplaceParser.T__9)
            self.state = 53
            self.match(LaplaceParser.NUMBER)
            self.state = 54
            self.match(LaplaceParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(LaplaceParser.NUMBER, 0)

        def getRuleIndex(self):
            return LaplaceParser.RULE_tExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTExpr" ):
                listener.enterTExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTExpr" ):
                listener.exitTExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTExpr" ):
                return visitor.visitTExpr(self)
            else:
                return visitor.visitChildren(self)




    def tExpr(self):

        localctx = LaplaceParser.TExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_tExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(LaplaceParser.T__10)
            self.state = 57
            self.match(LaplaceParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





