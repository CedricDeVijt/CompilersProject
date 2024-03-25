grammar Grammar_Project_3;

// parser rules
program: (main | typedefStatement | printfStatement | comment)*;

main: 'int' 'main' LPAREN RPAREN LBRACE statement* RBRACE;

statement: rvalue SEMICOLON
    | lvalue SEMICOLON
    | lvalue '=' rvalue SEMICOLON
    | lvalue '=' rvalueCast SEMICOLON
    | lvalue '=' rvalue SEMICOLON
    | postfixIncrement SEMICOLON
    | postfixDecrement SEMICOLON
    | printfStatement
    | comment;

printfStatement: 'printf' '(' formatSpecifier ',' ('var' | literal) ')' SEMICOLON;

formatSpecifier: '"%s"'
               | '"%d"'
               | '"%x"'
               | '"%f"'
               | '"%c"';

lvalue: identifier
    | type identifier
    | pointer identifier
    | deref;

rvalue: unaryExpression
    | identifier
    | deref
    | addr
    | LOGICAL_NOT rvalue
    | rvalue DIV rvalue
    | rvalue MOD rvalue
    | rvalue MULT rvalue
    | rvalue MINUS rvalue
    | rvalue PLUS rvalue
    | rvalue GREATER_THAN rvalue
    | rvalue LESS_THAN rvalue
    | rvalue GREATER_EQUAL rvalue
    | rvalue LESS_EQUAL rvalue
    | rvalue EQUALS rvalue
    | rvalue NOT_EQUAL rvalue
    | rvalue SHIFT_LEFT rvalue
    | rvalue SHIFT_RIGHT rvalue
    | rvalue BITWISE_AND rvalue
    | rvalue BITWISE_OR rvalue
    | rvalue BITWISE_XOR rvalue
    | rvalue LOGICAL_AND rvalue
    | rvalue LOGICAL_OR rvalue
    | LPAREN rvalue RPAREN;

rvalueCast:  LPAREN type RPAREN rvalue;

unaryExpression: (PLUS | MINUS)? literal
               | (PLUS MINUS)+ (PLUS)? literal
               | (MINUS PLUS)+ (MINUS)? literal;

literal: INT | FLOAT | CHAR;

pointer: type '*'+;

deref: '*'+ identifier;

addr: '&'+ identifier;

type: 'const'* ('int' | 'float' | 'char' | 'typedef');

typedefStatement: 'typedef' type IDENTIFIER SEMICOLON;

postfixIncrement: lvalue INCREMENT;

postfixDecrement: lvalue DECREMENT;

identifier: IDENTIFIER;
comment: COMMENT;


// lexer rules
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
CHAR : '\'' [a-zA-Z0-9] '\'' ;

WHITESPACE: [ \t\n\r]+ -> skip;

IDENTIFIER: [a-zA-Z] [a-zA-Z_0-9]*;

INCREMENT: '++';
DECREMENT: '--';

COMMENT: '//' ~[\r\n]*;