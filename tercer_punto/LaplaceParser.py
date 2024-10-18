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
        4,1,11,45,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,3,0,17,8,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,3,2,28,
        8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,
        1,6,0,0,7,0,2,4,6,8,10,12,0,0,41,0,16,1,0,0,0,2,18,1,0,0,0,4,27,
        1,0,0,0,6,29,1,0,0,0,8,33,1,0,0,0,10,37,1,0,0,0,12,41,1,0,0,0,14,
        17,3,2,1,0,15,17,3,4,2,0,16,14,1,0,0,0,16,15,1,0,0,0,17,1,1,0,0,
        0,18,19,5,1,0,0,19,20,5,2,0,0,20,21,3,4,2,0,21,22,5,3,0,0,22,3,1,
        0,0,0,23,28,3,6,3,0,24,28,3,8,4,0,25,28,3,10,5,0,26,28,3,12,6,0,
        27,23,1,0,0,0,27,24,1,0,0,0,27,25,1,0,0,0,27,26,1,0,0,0,28,5,1,0,
        0,0,29,30,5,4,0,0,30,31,5,10,0,0,31,32,5,5,0,0,32,7,1,0,0,0,33,34,
        5,6,0,0,34,35,5,10,0,0,35,36,5,7,0,0,36,9,1,0,0,0,37,38,5,8,0,0,
        38,39,5,10,0,0,39,40,5,7,0,0,40,11,1,0,0,0,41,42,5,9,0,0,42,43,5,
        10,0,0,43,13,1,0,0,0,2,16,27
    ]

class LaplaceParser ( Parser ):

    grammarFileName = "Laplace.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'L'", "'['", "']'", "'e^'", "'t'", "'sin('", 
                     "'t)'", "'cos('", "'t^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "WS" ]

    RULE_expr = 0
    RULE_laplaceExpr = 1
    RULE_functionExpr = 2
    RULE_expExpr = 3
    RULE_sinExpr = 4
    RULE_cosExpr = 5
    RULE_tExpr = 6

    ruleNames =  [ "expr", "laplaceExpr", "functionExpr", "expExpr", "sinExpr", 
                   "cosExpr", "tExpr" ]

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
    NUMBER=10
    WS=11

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


        def functionExpr(self):
            return self.getTypedRuleContext(LaplaceParser.FunctionExprContext,0)


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
            self.state = 16
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.laplaceExpr()
                pass
            elif token in [4, 6, 8, 9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.functionExpr()
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

        def functionExpr(self):
            return self.getTypedRuleContext(LaplaceParser.FunctionExprContext,0)


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
            self.state = 18
            self.match(LaplaceParser.T__0)
            self.state = 19
            self.match(LaplaceParser.T__1)
            self.state = 20
            self.functionExpr()
            self.state = 21
            self.match(LaplaceParser.T__2)
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
        self.enterRule(localctx, 4, self.RULE_functionExpr)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.expExpr()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.sinExpr()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.cosExpr()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 26
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
        self.enterRule(localctx, 6, self.RULE_expExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(LaplaceParser.T__3)
            self.state = 30
            self.match(LaplaceParser.NUMBER)
            self.state = 31
            self.match(LaplaceParser.T__4)
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
        self.enterRule(localctx, 8, self.RULE_sinExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(LaplaceParser.T__5)
            self.state = 34
            self.match(LaplaceParser.NUMBER)
            self.state = 35
            self.match(LaplaceParser.T__6)
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
        self.enterRule(localctx, 10, self.RULE_cosExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(LaplaceParser.T__7)
            self.state = 38
            self.match(LaplaceParser.NUMBER)
            self.state = 39
            self.match(LaplaceParser.T__6)
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
        self.enterRule(localctx, 12, self.RULE_tExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(LaplaceParser.T__8)
            self.state = 42
            self.match(LaplaceParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





