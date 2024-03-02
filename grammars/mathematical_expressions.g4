grammar mathematical_expressions;

// Lexer Rules
INTEGER : [0-9]+;
PLUS : '+';
MINUS : '-';
MULTIPLY : '*';
DIVIDE : '/';
MODULO : '%';
GT : '>';
LT : '<';
EQ : '==';
GTE : '>=';
LTE : '<=';
NEQ : '!=';
AND : '&&';
OR : '||';
NOT : '!';
LSHIFT : '<<';
RSHIFT : '>>';
BIT_AND : '&';
BIT_OR : '|';
BIT_NOT : '~';
BIT_XOR : '^';
LPAREN : '(';
RPAREN : ')';
SEMICOLON : ';';
WS: [ \n\t\r]+ -> skip;

// Parser Rules
start
    : (programLine)*
    ;

programLine
    : expression SEMICOLON
    ;

expression
    : expression GT expression
    | expression LT expression
    | expression EQ expression
    | expression GTE expression
    | expression LTE expression
    | expression NEQ expression
    | expression AND expression
    | expression OR expression
    | NOT expression
    | expression LSHIFT expression
    | expression RSHIFT expression
    | expression BIT_AND expression
    | expression BIT_OR expression
    | expression BIT_XOR expression
    | BIT_NOT expression
    | operation
    ;
operation
    : operation PLUS operation
    | operation MINUS operation
    | term
    ;

term
    : LPAREN expression RPAREN
    | term MULTIPLY term
    | term DIVIDE term
    | term MODULO term
    | MINUS? INTEGER
    ;