grammar Grammar_Project_2;

program: main;

main: TYPE 'main' LPAREN RPAREN LBRACE statement+ RBRACE;

statement: expression SEMICOLON;


expression: unaryExpression
    | LOGICAL_NOT expression
    | expression DIV expression
    | expression MOD expression
    | expression MULT expression
    | expression MINUS expression
    | expression PLUS expression
    | expression GREATER_THAN expression
    | expression LESS_THAN expression
    | expression GREATER_EQUAL expression
    | expression LESS_EQUAL expression
    | expression EQUALS expression
    | expression NOT_EQUAL expression
    | expression SHIFT_LEFT expression
    | expression SHIFT_RIGHT expression
    | expression BITWISE_AND expression
    | expression BITWISE_OR expression
    | expression BITWISE_XOR expression
    | expression LOGICAL_AND expression
    | expression LOGICAL_OR expression
    | LPAREN expression RPAREN
    | INT
    | variable;

variable: TYPE CHAR;


unaryExpression: (PLUS | MINUS)? literal
    | (PLUS MINUS)+ (PLUS)? literal
    | (MINUS PLUS)+ (MINUS)? literal;

literal: INT | FLOAT | CHAR;

TYPE: 'int' | 'const' | 'char' | 'float';


LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
GREATER_THAN: '>';
LESS_THAN: '<';
GREATER_EQUAL: '>=';
LESS_EQUAL: '<=';
EQUALS: '==';
NOT_EQUAL: '!=';
SHIFT_LEFT: '<<';
SHIFT_RIGHT: '>>';
BITWISE_AND: '&';
BITWISE_OR: '|';
BITWISE_XOR: '^';
LOGICAL_AND: '&&';
LOGICAL_OR: '||';
LOGICAL_NOT: '!';

SEMICOLON: ';';
INT: [0-9]+;
FLOAT: [0-9]+ ('.' [0-9]+)?;
CHAR: [a-zA-Z0-9];

WHITESPACE: [ \t\r\n]+ -> skip;
