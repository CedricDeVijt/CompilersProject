grammar Grammar;

program: (comment | (enumDeclaration SEMICOLON+) | (variable SEMICOLON+) | (typedef SEMICOLON+) | function)+ EOF;

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
         | arrayStatement SEMICOLON+
         | jumpStatement SEMICOLON+
         | function
         | switchStatement;

function: (type | pointer) IDENTIFIER LPAREN functionParams? RPAREN scope
        | (type | pointer) IDENTIFIER LPAREN functionParams? RPAREN SEMICOLON;

functionParams: (pointer | type) (addr | identifier)
      | functionParams COMMA functionParams;

functionCall: IDENTIFIER LPAREN callParams? RPAREN;

callParams: rvalue
          | callParams COMMA callParams;

switchStatement: 'switch' LPAREN rvalue RPAREN LBRACE switchCase* RBRACE;

switchCase: 'case' literal COLON statement*
          | 'default' COLON statement*;

conditional: ifStatement elseIfStatement* elseStatement?;
ifStatement: 'if' LPAREN rvalue RPAREN scope;
elseIfStatement: 'else' 'if' LPAREN rvalue RPAREN scope;
elseStatement: 'else' scope;

whileLoop: 'while' LPAREN rvalue RPAREN scope;

forLoop: 'for' LPAREN forCondition RPAREN scope;

forCondition: variable? SEMICOLON rvalue? SEMICOLON rvalue?;

printfStatement: 'printf' '(' formatSpecifier ',' (identifier | literal) ')';

formatSpecifier: '"%s"'
               | '"%d"'
               | '"%x"'
               | '"%f"'
               | '"%c"';


variable: lvalue '=' rvalue
         | lvalue
         | typedef
         | arrayDeclaration;

lvalue: identifier
      | type identifier
      | pointer identifier
      | deref
      | arrayElement;

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
      | functionCall
      | jumpStatement
      | arrayElement
      | arrayInitializer;

conditionalExpression: GREATER_THAN rvalue
                     | LESS_THAN rvalue
                     | GREATER_EQUAL rvalue
                     | LESS_EQUAL rvalue
                     | EQUALS rvalue
                     | NOT_EQUAL rvalue;

jumpStatement: 'break'
             | 'continue'
             | 'return' rvalue?;

unaryExpression: (PLUS | MINUS)? (literal | identifier | deref)
               | (PLUS MINUS)+ (PLUS)? (literal | identifier | deref)
               | (MINUS PLUS)+ (MINUS)? (literal | identifier | deref);

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

type: 'const'* ('int' | 'float' | 'char' | 'void' | IDENTIFIER);

identifier: IDENTIFIER;
comment: COMMENT;

arrayStatement: arrayDeclaration
              | arrayDefinition '=' rvalue;

arrayDeclaration: type IDENTIFIER ('[' INT ']')+;
arrayDefinition: type IDENTIFIER ('[' INT ']')+ '=' (arrayInitializer | identifier);

arrayInitializer: '{' (rvalue (',' rvalue)*)? '}';

arrayElement: identifier ('[' (rvalue | identifier) ']')+;

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
COMMA: ',';
INT:  '0' | [1-9][0-9]*;
FLOAT: [0-9]+ ('.' [0-9]+)?;
CHAR : '\'' '\\'? [a-zA-Z0-9] '\'' ;

WHITESPACE: [ \t\n\r]+ -> skip;

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

INCREMENT: '++';
DECREMENT: '--';

COMMENT: LINECOMMENT
       | BLOCKCOMMENT;

BLOCKCOMMENT: '/*' .*? '*/' -> skip;
LINECOMMENT: '//' ~[\r\n]* -> skip;
