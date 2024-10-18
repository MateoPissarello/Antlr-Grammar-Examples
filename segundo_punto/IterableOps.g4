grammar IterableOps;

// Regla principal
prog: statement+ EOF;

// Declaraciones
statement
    : mapStatement
    | filterStatement
    ;

// Declaración de MAP
mapStatement
    : 'MAP' '(' functionCall ',' iterable ')' NEWLINE
    ;

// Declaración de FILTER
filterStatement
    : 'FILTER' '(' conditionFunction ',' iterable ')' NEWLINE
    ;

// Llamada a una función
functionCall
    : IDENTIFIER '(' argumentList? ')'
    ;

// Llamada a una función de condición
conditionFunction
    : IDENTIFIER '(' argumentList? ')'
    ;

// Lista de argumentos
argumentList
    : expression (',' expression)*
    ;

// Objetos iterables (puede ser lista o tupla)
iterable
    : list | tuple
    ;

// Definición de lista
list
    : '[' expressionList? ']'   // Lista con corchetes
    ;

// Definición de tupla
tuple
    : '(' expressionList? ')'    // Tupla con paréntesis
    ;

// Lista de expresiones
expressionList
    : expression (',' expression)*
    ;

// Expresiones
expression
    : IDENTIFIER   // Variable
    | INT          // Número entero
    | STRING       // Cadena de texto
    ;

// Tokens
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*; // Identificadores
INT: [0-9]+;                         // Números enteros
STRING: '"' .*? '"';                 // Cadenas de texto
NEWLINE: '\r'? '\n' -> skip;         // Nueva línea
WS: [ \t]+ -> skip;                   // Espacios en blanco
