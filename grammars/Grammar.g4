grammar Grammar;

program: (comment | declaration SEMICOLON+ | function)+ EOF;

declaration: enumDeclaration
           | structDefinition
           | variable
           | typedef
           | arrayStatement
           | enumStatement
           ;

scope: LBRACE statement* RBRACE;

statement: rvalue SEMICOLON+
         | variable SEMICOLON+
         | comment
         | printfStatement SEMICOLON+
         | scanfStatement SEMICOLON+
         | scope
         | conditional
         | whileLoop
         | forLoop
         | enumStatement SEMICOLON+
         | jumpStatement SEMICOLON+
         | function
         | switchStatement
         | arrayStatement SEMICOLON+
         | structStatement SEMICOLON+
         ;

function: (type | pointer) IDENTIFIER LPAREN functionParams? RPAREN scope
        | (type | pointer) IDENTIFIER LPAREN functionParams? RPAREN SEMICOLON
        ;

structDefinition: 'struct' IDENTIFIER '{' (((type identifier) | arrayDeclaration) SEMICOLON)* '}';

structStatement: structVariable
               | structVariableDefinition
               | structAssignment
               ;

structVariable: 'struct' IDENTIFIER IDENTIFIER;

structVariableDefinition: 'struct' IDENTIFIER IDENTIFIER '=' '{' (rvalue | structMember) (',' (rvalue | structMember))* '}';

structMember: IDENTIFIER '.' IDENTIFIER ('[' rvalue ']')*;

structAssignment: structMember '=' rvalue;

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

printfStatement: 'printf' '(' formatSpecifier (','( char | string | rvalue | structMember))* ')';
scanfStatement: 'scanf' '(' formatSpecifier (',' addr)* ')';

formatSpecifier: STRING;

char: CHAR;

string: STRING;

variable: lvalue '=' rvalue
         | lvalue
         | typedef
         ;

lvalue: identifier
      | type identifier
      | pointer identifier
      | deref
      | LPAREN lvalue RPAREN
      | arrayElement
      ;

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
      | rvalue EQUALS rvalue
      | rvalue NOT_EQUAL rvalue
      | rvalue LOGICAL_AND rvalue
      | rvalue LOGICAL_OR rvalue
      | rvalue GREATER_THAN rvalue
      | rvalue LESS_THAN rvalue
      | rvalue GREATER_EQUAL rvalue
      | rvalue LESS_EQUAL rvalue
      | (PLUS | MINUS)? LPAREN rvalue RPAREN
      | explicitConversion
      | postFixIncrement
      | postFixDecrement
      | preFixIncrement
      | preFixDecrement
      | functionCall
      | jumpStatement
      | arrayElement
      | string
      | structMember
      ;

jumpStatement: 'break'
             | 'continue'
             | 'return' rvalue?
             ;

unaryExpression: (PLUS | MINUS)? (literal | identifier | deref)
               | (PLUS MINUS)+ (PLUS)? (literal | identifier | deref)
               | (MINUS PLUS)+ (MINUS)? (literal | identifier | deref)
               ;

literal: INT
       | FLOAT
       | CHAR
       ;

explicitConversion: '(' + type + ')' rvalue;

pointer: type '*'+;

deref: '*'+ identifier;

addr: '&'+ (identifier | arrayElement);

enumDeclaration: 'enum'  IDENTIFIER '{' IDENTIFIER (','  IDENTIFIER )*'}';

enumStatement: enumVariableDefinition
             | enumVariableDeclaration
             ;

enumVariableDefinition: 'enum' IDENTIFIER IDENTIFIER '=' IDENTIFIER;
enumVariableDeclaration: 'enum' IDENTIFIER IDENTIFIER;

postFixIncrement: lvalue INCREMENT;
postFixDecrement: lvalue DECREMENT;

preFixIncrement: INCREMENT lvalue;
preFixDecrement: DECREMENT lvalue;

arrayStatement: arrayDeclaration
//              | arrayAssignment
              | arrayDefinition
              ;

arrayDeclaration: type identifier ('[' rvalue ']')+;
arrayAssignment: identifier ('[' rvalue ']')+ '=' (rvalue | array)
               | identifier '=' array
               ;
arrayDefinition: type identifier ('[' rvalue ']')+ '=' (array | string);

array: LBRACE (rvalue | array) (',' (rvalue | array))* RBRACE;

arrayElement: identifier ('[' rvalue ']')+;

typedef: 'typedef' type IDENTIFIER;

type: 'const'* ('int' | 'float' | 'char' | 'void' | IDENTIFIER);

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
COMMA: ',';
INT:  '0' | [1-9][0-9]*;
FLOAT: [0-9]+ ('.' [0-9]+)?;
CHAR : '\'' '\\'? (~["\r\n\t]) '\'' ;
STRING: '"' (~["\r\n\t])* '"';
WHITESPACE: [ \t\n\r]+ -> skip;

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

INCREMENT: '++';
DECREMENT: '--';

COMMENT: LINECOMMENT
       | BLOCKCOMMENT;

BLOCKCOMMENT: '/*' .*? '*/' -> skip;
LINECOMMENT: '//' ~[\r\n]* -> skip;
