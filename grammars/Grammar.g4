grammar Grammar;

// parser rules
program: (comment | variables | typedef)* main (comment | variables | typedef)* EOF;

main: 'int' 'main' LPAREN RPAREN scope;

scope: LBRACE statement* RBRACE;

statement: rvalue SEMICOLON+
         | variables
         | postFixIncrement SEMICOLON+
         | postFixDecrement SEMICOLON+
         | preFixIncrement SEMICOLON+
         | preFixDecrement SEMICOLON+
         | comment
         | printfStatement
         | scope
         |typedef;


printfStatement: 'printf' '(' formatSpecifier ',' (identifier | literal) ')' SEMICOLON;

formatSpecifier: '"%s"'
               | '"%d"'
               | '"%x"'
               | '"%f"'
               | '"%c"';


variables: lvalue '=' rvalue SEMICOLON+
         | lvalue SEMICOLON+;

lvalue: identifier
      | type identifier
      | pointer identifier
      | deref;

rvalue: unaryExpression
      | identifier
      | deref
      | addr
      | LOGICAL_NOT rvalue
      | BITWISE_NOT rvalue
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
      | LPAREN rvalue RPAREN
      | explicitConversion;

unaryExpression: (PLUS | MINUS)? literal
               | (PLUS MINUS)+ (PLUS)? literal
               | (MINUS PLUS)+ (MINUS)? literal;

literal: INT
       | FLOAT
       | CHAR;

explicitConversion: '(' + type + ')' rvalue;

pointer: type '*'+;

deref: '*'+ identifier;

addr: '&'+ identifier;



postFixIncrement: lvalue INCREMENT;
postFixDecrement: lvalue DECREMENT;

preFixIncrement: INCREMENT lvalue;
preFixDecrement: DECREMENT lvalue;

typedef: 'typedef' type IDENTIFIER SEMICOLON;

type: 'const'* ('int' | 'float' | 'char' | IDENTIFIER);

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
BITWISE_NOT: '~';
LOGICAL_AND: '&&';
LOGICAL_OR: '||';
LOGICAL_NOT: '!';

SEMICOLON: ';';
INT:  '0' | [1-9][0-9]*;
FLOAT: [0-9]+ ('.' [0-9]+)?;
CHAR : '\'' [a-zA-Z0-9] '\'' ;

WHITESPACE: [ \t\n\r]+ -> skip;

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

INCREMENT: '++';
DECREMENT: '--';

COMMENT: LINECOMMENT
       | BLOCKCOMMENT;

BLOCKCOMMENT: '/*' .*? '*/' -> skip;
LINECOMMENT: '//' ~[\r\n]* -> skip;