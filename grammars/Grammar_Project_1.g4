grammar Grammar_Project_1;

program: (programLine)*;

programLine: expression SEMICOLON;

expression: unaryExpression
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
    | LOGICAL_NOT expression
    | LPAREN expression RPAREN
    | INT;

unaryExpression: (PLUS | MINUS)? number
    | (PLUS MINUS)+ (PLUS)? number
    | (MINUS PLUS)+ (MINUS)? number;

number: INT;



LPAREN: '(';
RPAREN: ')';
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

WHITESPACE: [ \t\r\n]+ -> skip;