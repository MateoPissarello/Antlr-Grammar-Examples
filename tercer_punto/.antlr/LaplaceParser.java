// Generated from /home/pissarello-dev/Documentos/Code/univerity/semestre-v/lpt/Antlr-Grammar-Examples/tercer_punto/Laplace.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class LaplaceParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		NUMBER=10, WS=11;
	public static final int
		RULE_expr = 0, RULE_laplaceExpr = 1, RULE_functionExpr = 2, RULE_expExpr = 3, 
		RULE_sinExpr = 4, RULE_cosExpr = 5, RULE_tExpr = 6;
	private static String[] makeRuleNames() {
		return new String[] {
			"expr", "laplaceExpr", "functionExpr", "expExpr", "sinExpr", "cosExpr", 
			"tExpr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'L'", "'['", "']'", "'e^'", "'t'", "'sin('", "'t)'", "'cos('", 
			"'t^'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, "NUMBER", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Laplace.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public LaplaceParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public LaplaceExprContext laplaceExpr() {
			return getRuleContext(LaplaceExprContext.class,0);
		}
		public FunctionExprContext functionExpr() {
			return getRuleContext(FunctionExprContext.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_expr);
		try {
			setState(16);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				enterOuterAlt(_localctx, 1);
				{
				setState(14);
				laplaceExpr();
				}
				break;
			case T__3:
			case T__5:
			case T__7:
			case T__8:
				enterOuterAlt(_localctx, 2);
				{
				setState(15);
				functionExpr();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LaplaceExprContext extends ParserRuleContext {
		public FunctionExprContext functionExpr() {
			return getRuleContext(FunctionExprContext.class,0);
		}
		public LaplaceExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_laplaceExpr; }
	}

	public final LaplaceExprContext laplaceExpr() throws RecognitionException {
		LaplaceExprContext _localctx = new LaplaceExprContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_laplaceExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(18);
			match(T__0);
			setState(19);
			match(T__1);
			setState(20);
			functionExpr();
			setState(21);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionExprContext extends ParserRuleContext {
		public ExpExprContext expExpr() {
			return getRuleContext(ExpExprContext.class,0);
		}
		public SinExprContext sinExpr() {
			return getRuleContext(SinExprContext.class,0);
		}
		public CosExprContext cosExpr() {
			return getRuleContext(CosExprContext.class,0);
		}
		public TExprContext tExpr() {
			return getRuleContext(TExprContext.class,0);
		}
		public FunctionExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionExpr; }
	}

	public final FunctionExprContext functionExpr() throws RecognitionException {
		FunctionExprContext _localctx = new FunctionExprContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_functionExpr);
		try {
			setState(27);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
				enterOuterAlt(_localctx, 1);
				{
				setState(23);
				expExpr();
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 2);
				{
				setState(24);
				sinExpr();
				}
				break;
			case T__7:
				enterOuterAlt(_localctx, 3);
				{
				setState(25);
				cosExpr();
				}
				break;
			case T__8:
				enterOuterAlt(_localctx, 4);
				{
				setState(26);
				tExpr();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpExprContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(LaplaceParser.NUMBER, 0); }
		public ExpExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expExpr; }
	}

	public final ExpExprContext expExpr() throws RecognitionException {
		ExpExprContext _localctx = new ExpExprContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_expExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(29);
			match(T__3);
			setState(30);
			match(NUMBER);
			setState(31);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SinExprContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(LaplaceParser.NUMBER, 0); }
		public SinExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sinExpr; }
	}

	public final SinExprContext sinExpr() throws RecognitionException {
		SinExprContext _localctx = new SinExprContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_sinExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			match(T__5);
			setState(34);
			match(NUMBER);
			setState(35);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CosExprContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(LaplaceParser.NUMBER, 0); }
		public CosExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cosExpr; }
	}

	public final CosExprContext cosExpr() throws RecognitionException {
		CosExprContext _localctx = new CosExprContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_cosExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(37);
			match(T__7);
			setState(38);
			match(NUMBER);
			setState(39);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TExprContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(LaplaceParser.NUMBER, 0); }
		public TExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tExpr; }
	}

	public final TExprContext tExpr() throws RecognitionException {
		TExprContext _localctx = new TExprContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_tExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(41);
			match(T__8);
			setState(42);
			match(NUMBER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u000b-\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0001\u0000\u0001\u0000\u0003"+
		"\u0000\u0011\b\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002\u001c"+
		"\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0000\u0000\u0007"+
		"\u0000\u0002\u0004\u0006\b\n\f\u0000\u0000)\u0000\u0010\u0001\u0000\u0000"+
		"\u0000\u0002\u0012\u0001\u0000\u0000\u0000\u0004\u001b\u0001\u0000\u0000"+
		"\u0000\u0006\u001d\u0001\u0000\u0000\u0000\b!\u0001\u0000\u0000\u0000"+
		"\n%\u0001\u0000\u0000\u0000\f)\u0001\u0000\u0000\u0000\u000e\u0011\u0003"+
		"\u0002\u0001\u0000\u000f\u0011\u0003\u0004\u0002\u0000\u0010\u000e\u0001"+
		"\u0000\u0000\u0000\u0010\u000f\u0001\u0000\u0000\u0000\u0011\u0001\u0001"+
		"\u0000\u0000\u0000\u0012\u0013\u0005\u0001\u0000\u0000\u0013\u0014\u0005"+
		"\u0002\u0000\u0000\u0014\u0015\u0003\u0004\u0002\u0000\u0015\u0016\u0005"+
		"\u0003\u0000\u0000\u0016\u0003\u0001\u0000\u0000\u0000\u0017\u001c\u0003"+
		"\u0006\u0003\u0000\u0018\u001c\u0003\b\u0004\u0000\u0019\u001c\u0003\n"+
		"\u0005\u0000\u001a\u001c\u0003\f\u0006\u0000\u001b\u0017\u0001\u0000\u0000"+
		"\u0000\u001b\u0018\u0001\u0000\u0000\u0000\u001b\u0019\u0001\u0000\u0000"+
		"\u0000\u001b\u001a\u0001\u0000\u0000\u0000\u001c\u0005\u0001\u0000\u0000"+
		"\u0000\u001d\u001e\u0005\u0004\u0000\u0000\u001e\u001f\u0005\n\u0000\u0000"+
		"\u001f \u0005\u0005\u0000\u0000 \u0007\u0001\u0000\u0000\u0000!\"\u0005"+
		"\u0006\u0000\u0000\"#\u0005\n\u0000\u0000#$\u0005\u0007\u0000\u0000$\t"+
		"\u0001\u0000\u0000\u0000%&\u0005\b\u0000\u0000&\'\u0005\n\u0000\u0000"+
		"\'(\u0005\u0007\u0000\u0000(\u000b\u0001\u0000\u0000\u0000)*\u0005\t\u0000"+
		"\u0000*+\u0005\n\u0000\u0000+\r\u0001\u0000\u0000\u0000\u0002\u0010\u001b";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}