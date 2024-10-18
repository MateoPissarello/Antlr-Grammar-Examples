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
        4,1,13,55,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,3,0,19,8,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,
        29,8,2,10,2,12,2,32,9,2,1,3,1,3,1,3,1,3,3,3,38,8,3,1,4,1,4,1,4,1,
        4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,0,0,8,0,2,4,6,
        8,10,12,14,0,1,1,0,4,5,51,0,18,1,0,0,0,2,20,1,0,0,0,4,25,1,0,0,0,
        6,37,1,0,0,0,8,39,1,0,0,0,10,43,1,0,0,0,12,47,1,0,0,0,14,51,1,0,
        0,0,16,19,3,2,1,0,17,19,3,4,2,0,18,16,1,0,0,0,18,17,1,0,0,0,19,1,
        1,0,0,0,20,21,5,1,0,0,21,22,5,2,0,0,22,23,3,0,0,0,23,24,5,3,0,0,
        24,3,1,0,0,0,25,30,3,6,3,0,26,27,7,0,0,0,27,29,3,6,3,0,28,26,1,0,
        0,0,29,32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,5,1,0,0,0,32,30,
        1,0,0,0,33,38,3,8,4,0,34,38,3,10,5,0,35,38,3,12,6,0,36,38,3,14,7,
        0,37,33,1,0,0,0,37,34,1,0,0,0,37,35,1,0,0,0,37,36,1,0,0,0,38,7,1,
        0,0,0,39,40,5,6,0,0,40,41,5,12,0,0,41,42,5,7,0,0,42,9,1,0,0,0,43,
        44,5,8,0,0,44,45,5,12,0,0,45,46,5,9,0,0,46,11,1,0,0,0,47,48,5,10,
        0,0,48,49,5,12,0,0,49,50,5,9,0,0,50,13,1,0,0,0,51,52,5,11,0,0,52,
        53,5,12,0,0,53,15,1,0,0,0,3,18,30,37
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
    RULE_expExpr = 4
    RULE_sinExpr = 5
    RULE_cosExpr = 6
    RULE_tExpr = 7

    ruleNames =  [ "expr", "laplaceExpr", "sumExpr", "functionExpr", "expExpr", 
                   "sinExpr", "cosExpr", "tExpr" ]

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
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.laplaceExpr()
                pass
            elif token in [6, 8, 10, 11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.sumExpr()
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
            self.state = 20
            self.match(LaplaceParser.T__0)
            self.state = 21
            self.match(LaplaceParser.T__1)
            self.state = 22
            self.expr()
            self.state = 23
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
            self.state = 25
            self.functionExpr()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4 or _la==5:
                self.state = 26
                _la = self._input.LA(1)
                if not(_la==4 or _la==5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 27
                self.functionExpr()
                self.state = 32
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
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.expExpr()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.sinExpr()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.cosExpr()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 36
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
        self.enterRule(localctx, 8, self.RULE_expExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(LaplaceParser.T__5)
            self.state = 40
            self.match(LaplaceParser.NUMBER)
            self.state = 41
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
        self.enterRule(localctx, 10, self.RULE_sinExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(LaplaceParser.T__7)
            self.state = 44
            self.match(LaplaceParser.NUMBER)
            self.state = 45
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
        self.enterRule(localctx, 12, self.RULE_cosExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(LaplaceParser.T__9)
            self.state = 48
            self.match(LaplaceParser.NUMBER)
            self.state = 49
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
        self.enterRule(localctx, 14, self.RULE_tExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(LaplaceParser.T__10)
            self.state = 52
            self.match(LaplaceParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





