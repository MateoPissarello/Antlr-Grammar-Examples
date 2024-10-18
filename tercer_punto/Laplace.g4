grammar Laplace;

/*
 * Parser rules
 */

expr: laplaceExpr | functionExpr;

laplaceExpr: 'L' '[' functionExpr ']';

functionExpr: expExpr | sinExpr | cosExpr | tExpr;

expExpr: 'e^' NUMBER 't';

sinExpr: 'sin(' NUMBER 't)';

cosExpr: 'cos(' NUMBER 't)';

tExpr: 't^' NUMBER;

/*
 * Lexer rules
 */

NUMBER:
	[0-9]+ ('.' [0-9]+)?; // Reconoce números enteros y decimales
WS: [ \t\r\n]+ -> skip; // Ignora espacios en blanco