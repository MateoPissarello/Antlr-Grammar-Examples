grammar Laplace;

// Parser rules
expr: laplaceExpr | sumExpr | numberExpr;

laplaceExpr: 'L' '[' expr ']';

// Permitir expresiones combinadas
sumExpr: functionExpr (('+' | '-') functionExpr)*;

// Definir las funciones
functionExpr: expExpr | sinExpr | cosExpr | tExpr;


numberExpr: NUMBER;
expExpr: 'e^' NUMBER 't';
sinExpr: 'sin(' NUMBER 't)';
cosExpr: 'cos(' NUMBER 't)';
tExpr: 't^' NUMBER;

// Lexer rules
NUMBER:
	[0-9]+ ('.' [0-9]+)?; // Reconoce números enteros y decimales
WS: [ \t\r\n]+ -> skip; // Ignora espacios en blanco