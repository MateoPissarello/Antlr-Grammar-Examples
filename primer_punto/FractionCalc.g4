grammar FractionCalc;

prog:
	stat+ EOF; 

stat:
	expr NEWLINE	# printExpr
	| NEWLINE		# blank ; 

expr:
	expr ('*' | '/') expr	# MulDiv
	| expr ('+' | '-') expr	# AddSub 
	| fraction				# fractionExpr 
	| '(' expr ')'			# parens ;

fraction: INT '/' INT;

INT: [0-9]+;

NEWLINE: '\r'? '\n';
WS: [ \t]+ -> skip; 