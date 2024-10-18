# Generated from IterableOps.g4 by ANTLR 4.13.2
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
        4,1,12,100,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,0,1,0,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,3,4,55,8,4,1,4,1,
        4,1,5,1,5,1,5,3,5,62,8,5,1,5,1,5,1,6,1,6,1,6,5,6,69,8,6,10,6,12,
        6,72,9,6,1,7,1,7,3,7,76,8,7,1,8,1,8,3,8,80,8,8,1,8,1,8,1,9,1,9,3,
        9,86,8,9,1,9,1,9,1,10,1,10,1,10,5,10,93,8,10,10,10,12,10,96,9,10,
        1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,1,1,0,8,10,
        96,0,25,1,0,0,0,2,33,1,0,0,0,4,35,1,0,0,0,6,43,1,0,0,0,8,51,1,0,
        0,0,10,58,1,0,0,0,12,65,1,0,0,0,14,75,1,0,0,0,16,77,1,0,0,0,18,83,
        1,0,0,0,20,89,1,0,0,0,22,97,1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,
        26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,29,1,0,0,0,29,30,5,
        0,0,1,30,1,1,0,0,0,31,34,3,4,2,0,32,34,3,6,3,0,33,31,1,0,0,0,33,
        32,1,0,0,0,34,3,1,0,0,0,35,36,5,1,0,0,36,37,5,2,0,0,37,38,3,8,4,
        0,38,39,5,3,0,0,39,40,3,14,7,0,40,41,5,4,0,0,41,42,5,11,0,0,42,5,
        1,0,0,0,43,44,5,5,0,0,44,45,5,2,0,0,45,46,3,10,5,0,46,47,5,3,0,0,
        47,48,3,14,7,0,48,49,5,4,0,0,49,50,5,11,0,0,50,7,1,0,0,0,51,52,5,
        8,0,0,52,54,5,2,0,0,53,55,3,12,6,0,54,53,1,0,0,0,54,55,1,0,0,0,55,
        56,1,0,0,0,56,57,5,4,0,0,57,9,1,0,0,0,58,59,5,8,0,0,59,61,5,2,0,
        0,60,62,3,12,6,0,61,60,1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,63,64,
        5,4,0,0,64,11,1,0,0,0,65,70,3,22,11,0,66,67,5,3,0,0,67,69,3,22,11,
        0,68,66,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,13,
        1,0,0,0,72,70,1,0,0,0,73,76,3,16,8,0,74,76,3,18,9,0,75,73,1,0,0,
        0,75,74,1,0,0,0,76,15,1,0,0,0,77,79,5,6,0,0,78,80,3,20,10,0,79,78,
        1,0,0,0,79,80,1,0,0,0,80,81,1,0,0,0,81,82,5,7,0,0,82,17,1,0,0,0,
        83,85,5,2,0,0,84,86,3,20,10,0,85,84,1,0,0,0,85,86,1,0,0,0,86,87,
        1,0,0,0,87,88,5,4,0,0,88,19,1,0,0,0,89,94,3,22,11,0,90,91,5,3,0,
        0,91,93,3,22,11,0,92,90,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,
        1,0,0,0,95,21,1,0,0,0,96,94,1,0,0,0,97,98,7,0,0,0,98,23,1,0,0,0,
        9,27,33,54,61,70,75,79,85,94
    ]

class IterableOpsParser ( Parser ):

    grammarFileName = "IterableOps.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'MAP'", "'('", "','", "')'", "'FILTER'", 
                     "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IDENTIFIER", "INT", "STRING", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_mapStatement = 2
    RULE_filterStatement = 3
    RULE_functionCall = 4
    RULE_conditionFunction = 5
    RULE_argumentList = 6
    RULE_iterable = 7
    RULE_list = 8
    RULE_tuple = 9
    RULE_expressionList = 10
    RULE_expression = 11

    ruleNames =  [ "prog", "statement", "mapStatement", "filterStatement", 
                   "functionCall", "conditionFunction", "argumentList", 
                   "iterable", "list", "tuple", "expressionList", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    IDENTIFIER=8
    INT=9
    STRING=10
    NEWLINE=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(IterableOpsParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IterableOpsParser.StatementContext)
            else:
                return self.getTypedRuleContext(IterableOpsParser.StatementContext,i)


        def getRuleIndex(self):
            return IterableOpsParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = IterableOpsParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.statement()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==5):
                    break

            self.state = 29
            self.match(IterableOpsParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mapStatement(self):
            return self.getTypedRuleContext(IterableOpsParser.MapStatementContext,0)


        def filterStatement(self):
            return self.getTypedRuleContext(IterableOpsParser.FilterStatementContext,0)


        def getRuleIndex(self):
            return IterableOpsParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = IterableOpsParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.mapStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.filterStatement()
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


    class MapStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(IterableOpsParser.FunctionCallContext,0)


        def iterable(self):
            return self.getTypedRuleContext(IterableOpsParser.IterableContext,0)


        def NEWLINE(self):
            return self.getToken(IterableOpsParser.NEWLINE, 0)

        def getRuleIndex(self):
            return IterableOpsParser.RULE_mapStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapStatement" ):
                listener.enterMapStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapStatement" ):
                listener.exitMapStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapStatement" ):
                return visitor.visitMapStatement(self)
            else:
                return visitor.visitChildren(self)




    def mapStatement(self):

        localctx = IterableOpsParser.MapStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mapStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(IterableOpsParser.T__0)
            self.state = 36
            self.match(IterableOpsParser.T__1)
            self.state = 37
            self.functionCall()
            self.state = 38
            self.match(IterableOpsParser.T__2)
            self.state = 39
            self.iterable()
            self.state = 40
            self.match(IterableOpsParser.T__3)
            self.state = 41
            self.match(IterableOpsParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionFunction(self):
            return self.getTypedRuleContext(IterableOpsParser.ConditionFunctionContext,0)


        def iterable(self):
            return self.getTypedRuleContext(IterableOpsParser.IterableContext,0)


        def NEWLINE(self):
            return self.getToken(IterableOpsParser.NEWLINE, 0)

        def getRuleIndex(self):
            return IterableOpsParser.RULE_filterStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterStatement" ):
                listener.enterFilterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterStatement" ):
                listener.exitFilterStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterStatement" ):
                return visitor.visitFilterStatement(self)
            else:
                return visitor.visitChildren(self)




    def filterStatement(self):

        localctx = IterableOpsParser.FilterStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(IterableOpsParser.T__4)
            self.state = 44
            self.match(IterableOpsParser.T__1)
            self.state = 45
            self.conditionFunction()
            self.state = 46
            self.match(IterableOpsParser.T__2)
            self.state = 47
            self.iterable()
            self.state = 48
            self.match(IterableOpsParser.T__3)
            self.state = 49
            self.match(IterableOpsParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(IterableOpsParser.IDENTIFIER, 0)

        def argumentList(self):
            return self.getTypedRuleContext(IterableOpsParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return IterableOpsParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = IterableOpsParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(IterableOpsParser.IDENTIFIER)
            self.state = 52
            self.match(IterableOpsParser.T__1)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0):
                self.state = 53
                self.argumentList()


            self.state = 56
            self.match(IterableOpsParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(IterableOpsParser.IDENTIFIER, 0)

        def argumentList(self):
            return self.getTypedRuleContext(IterableOpsParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return IterableOpsParser.RULE_conditionFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionFunction" ):
                listener.enterConditionFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionFunction" ):
                listener.exitConditionFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionFunction" ):
                return visitor.visitConditionFunction(self)
            else:
                return visitor.visitChildren(self)




    def conditionFunction(self):

        localctx = IterableOpsParser.ConditionFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_conditionFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(IterableOpsParser.IDENTIFIER)
            self.state = 59
            self.match(IterableOpsParser.T__1)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0):
                self.state = 60
                self.argumentList()


            self.state = 63
            self.match(IterableOpsParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IterableOpsParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(IterableOpsParser.ExpressionContext,i)


        def getRuleIndex(self):
            return IterableOpsParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = IterableOpsParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.expression()
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 66
                self.match(IterableOpsParser.T__2)
                self.state = 67
                self.expression()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_(self):
            return self.getTypedRuleContext(IterableOpsParser.ListContext,0)


        def tuple_(self):
            return self.getTypedRuleContext(IterableOpsParser.TupleContext,0)


        def getRuleIndex(self):
            return IterableOpsParser.RULE_iterable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterable" ):
                listener.enterIterable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterable" ):
                listener.exitIterable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterable" ):
                return visitor.visitIterable(self)
            else:
                return visitor.visitChildren(self)




    def iterable(self):

        localctx = IterableOpsParser.IterableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_iterable)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.list_()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.tuple_()
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


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionList(self):
            return self.getTypedRuleContext(IterableOpsParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return IterableOpsParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = IterableOpsParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(IterableOpsParser.T__5)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0):
                self.state = 78
                self.expressionList()


            self.state = 81
            self.match(IterableOpsParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionList(self):
            return self.getTypedRuleContext(IterableOpsParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return IterableOpsParser.RULE_tuple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple" ):
                listener.enterTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple" ):
                listener.exitTuple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple" ):
                return visitor.visitTuple(self)
            else:
                return visitor.visitChildren(self)




    def tuple_(self):

        localctx = IterableOpsParser.TupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(IterableOpsParser.T__1)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0):
                self.state = 84
                self.expressionList()


            self.state = 87
            self.match(IterableOpsParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IterableOpsParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(IterableOpsParser.ExpressionContext,i)


        def getRuleIndex(self):
            return IterableOpsParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = IterableOpsParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.expression()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 90
                self.match(IterableOpsParser.T__2)
                self.state = 91
                self.expression()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(IterableOpsParser.IDENTIFIER, 0)

        def INT(self):
            return self.getToken(IterableOpsParser.INT, 0)

        def STRING(self):
            return self.getToken(IterableOpsParser.STRING, 0)

        def getRuleIndex(self):
            return IterableOpsParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = IterableOpsParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





