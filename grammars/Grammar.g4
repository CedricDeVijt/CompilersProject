grammar Grammar;

// parser rules
program: (comment | (enumDeclaration SEMICOLON+) | (variable SEMICOLON+) | (typedef SEMICOLON+))* main (comment | (enumDeclaration SEMICOLON+) | variable | typedef)* EOF;

main: 'int' 'main' LPAREN RPAREN scope;

scope: LBRACE statement* RBRACE;

statement: rvalue SEMICOLON+
         | variable SEMICOLON+
         | comment
         | printfStatement SEMICOLON+
         | scope
         | conditional
         | whileLoop
         | forLoop
         | enumStatement SEMICOLON+
         | jumpStatement SEMICOLON+
         | switchStatement;

switchStatement: 'switch' LPAREN rvalue RPAREN LBRACE switchCase* RBRACE;

switchCase: 'case' literal COLON statement*
          | 'default' COLON statement*;

conditional: ifStatement elseIfStatement* elseStatement?;
ifStatement: 'if' LPAREN rvalue RPAREN scope;
elseIfStatement: 'else' 'if' LPAREN rvalue RPAREN scope;
elseStatement: 'else' scope;

whileLoop: 'while' LPAREN rvalue RPAREN scope;

forLoop: 'for' LPAREN forCondition RPAREN scope;
forInit: variable | rvalue;
forCondition: variable? SEMICOLON (rvalue conditionalExpression?)? SEMICOLON rvalue?;

printfStatement: 'printf' '(' formatSpecifier ',' (identifier | literal) ')';

formatSpecifier: '"%s"'
               | '"%d"'
               | '"%x"'
               | '"%f"'
               | '"%c"';


variable: lvalue '=' rvalue
         | lvalue
         | typedef;

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
      | rvalue SHIFT_LEFT rvalue
      | rvalue SHIFT_RIGHT rvalue
      | rvalue BITWISE_AND rvalue
      | rvalue BITWISE_OR rvalue
      | rvalue BITWISE_XOR rvalue
      | rvalue LOGICAL_AND rvalue
      | rvalue LOGICAL_OR rvalue
      | LPAREN rvalue RPAREN
      | explicitConversion
      | postFixIncrement
      | postFixDecrement
      | preFixIncrement
      | preFixDecrement
      | rvalue conditionalExpression
      | jumpStatement;

conditionalExpression: GREATER_THAN rvalue
                     | LESS_THAN rvalue
                     | GREATER_EQUAL rvalue
                     | LESS_EQUAL rvalue
                     | EQUALS rvalue
                     | NOT_EQUAL rvalue;

jumpStatement: 'break'
             | 'continue';

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

enumDeclaration: 'enum'  IDENTIFIER '{' IDENTIFIER (','  IDENTIFIER )*'}';

enumStatement: enumVariableDefinition
             | enumVariableDeclaration;

enumVariableDefinition: 'enum' IDENTIFIER IDENTIFIER '=' IDENTIFIER;
enumVariableDeclaration: 'enum' IDENTIFIER IDENTIFIER;

postFixIncrement: lvalue INCREMENT;
postFixDecrement: lvalue DECREMENT;

preFixIncrement: INCREMENT lvalue;
preFixDecrement: DECREMENT lvalue;

typedef: 'typedef' type IDENTIFIER;

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

COLON: ':';
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