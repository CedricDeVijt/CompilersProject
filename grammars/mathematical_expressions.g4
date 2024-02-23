grammar mathematical_expressions;

// Lexer rules
INTEGER : [0-9]+ ('.' [0-9]+)?;
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

// Parser rules
expression : logicalExpression SEMICOLON;
logicalExpression : equalityExpression ((AND | OR) equalityExpression)*;
equalityExpression : relationalExpression ((EQ | NEQ | GTE | LTE) relationalExpression)*;
relationalExpression : additiveExpression ((GT | LT) additiveExpression)*;
additiveExpression : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*;
multiplicativeExpression : unaryExpression ((MULTIPLY | DIVIDE | MODULO) unaryExpression)*;
unaryExpression : (PLUS | MINUS | NOT | BIT_NOT) unaryExpression
                | primaryExpression;
primaryExpression : INTEGER
                  | LPAREN expression RPAREN;
