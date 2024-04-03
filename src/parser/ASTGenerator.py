from src.antlr_files.GrammarParser import GrammarParser
from src.antlr_files.GrammarVisitor import GrammarVisitor as Visitor

from src.parser.AST import *
from src.parser.SymbolTable import SymbolTableTree, Symbol


class ASTGenerator(Visitor):

    def __init__(self):
        self.scope = SymbolTableTree()
        self.errors = []
        self.warnings = []
        self.node = None
        self.types = ['int', 'float', 'char']

    def get_highest_type(self, rval):
        if isinstance(rval, DerefNode):
            identifier = rval.identifier.value
            if self.scope.lookup(identifier):
                if isinstance(self.scope.lookup(identifier).type, str):
                    return self.scope.lookup(identifier).type
                return self.scope.lookup(identifier).type.type[0].value
        if isinstance(rval, IdentifierNode):
            identifier = rval.value
            if self.scope.lookup(identifier):
                if isinstance(self.scope.lookup(identifier).type, str):
                    return self.scope.lookup(identifier).type
                return self.scope.lookup(identifier).type.type[0].value
        if isinstance(rval, IntNode):
            return 'int'
        elif isinstance(rval, FloatNode):
            return 'float'
        elif isinstance(rval, CharNode):
            return 'char'
        elif isinstance(rval, Node):
            if isinstance(rval, AddrNode):
                identifier = rval.value.value
                if self.scope.lookup(identifier):
                    if isinstance(self.scope.lookup(identifier).type, str):
                        return self.scope.lookup(identifier).type
                    return self.scope.lookup(identifier).type.type[0].value
            type1 = self.get_highest_type(rval.children[0])
            type2 = self.get_highest_type(rval.children[len(rval.children) - 1])
            if type1 == 'float' or type2 == 'float':
                return float
            elif type1 == 'int' or type2 == 'int':
                return 'int'
            return 'char'

    def implicit_type_conversion(self, lvalType, rval):
        if isinstance(lvalType, PointerNode):
            lvalType = lvalType.type[0].value
        rvalType = self.get_highest_type(rval)
        if lvalType == 'int' and rvalType == 'float':
            self.warnings.append(f"line {rval.line}:{rval.pos} Implicit type conversion from float to int!")
        elif lvalType == 'char' and rvalType == 'float':
            self.warnings.append(f"line {rval.line}:{rval.pos} Implicit type conversion from float to char!")
        elif lvalType == 'char' and rvalType == 'int':
            self.warnings.append(f"line {rval.line}:{rval.pos} Implicit type conversion from int to char!")

    def visitProgram(self, ctx):
        children = []
        for line in ctx.getChildren():
            node = self.visit(line)
            if node is not None:
                if isinstance(node, list):
                    children.extend(node)
                else:
                    children.append(node)
        self.node = ProgramNode(ctx.start.line, ctx.start.column, children)
        return self

    def visitMain(self, ctx):
        children = []
        for line in ctx.getChildren():
            node = self.visit(line)
            if node is not None:
                if isinstance(node, list):
                    children.extend(node)
                else:
                    children.append(node)
        return MainNode(ctx.start.line, ctx.start.column, children)

    def visitScope(self, ctx):
        self.scope.open_scope()
        children = []
        for line in ctx.getChildren():
            node = self.visit(line)
            if node is not None:
                if isinstance(node, list):
                    children.extend(node)
                else:
                    children.append(node)
        self.scope.close_scope()
        return children

    def visitStatement(self, ctx):
        children = []
        for line in ctx.getChildren():
            if line.getText() == ";":
                pass
            else:
                child = self.visit(line)
                if isinstance(child, list):
                    children.extend(child)
                else:
                    children.append(child)
        if len(children) == 0:
            return None
        else:
            node = children[0]
            return node

    def visitVariables(self, ctx):
        children = []
        for line in ctx.getChildren():
            if line.getText() == ";":
                pass
            elif line.getText() == "=":
                children.append(line.getText())
            else:
                child = self.visit(line)
                if isinstance(child, list):
                    children.extend(child)
                else:
                    if child:
                        children.append(child)
        # Ends with type + identifier -> declaration.
        if (isinstance(children[len(children) - 2], TypeNode) or isinstance(children[len(children) - 2], PointerNode)) and isinstance(children[len(children) - 1], IdentifierNode):
            identifier = children[len(children) - 1].value
            var_type = children[len(children) - 2].value

            # Check if type is declared.
            if var_type not in self.types:
                if self.scope.lookup(var_type) is None:
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Type \'" + var_type + "\' not declared yet!")
                    return None
                elif not self.scope.lookup(var_type).typeDef:
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} \'" + var_type + "\' not declared as type!")
                    return None

            const = len(children) > 2

            if isinstance(children[len(children) - 2], PointerNode):
                var_type = children[len(children) - 2]
                const = len(children[0].type) > 1

            # Check if variable already declared in current scope.

            if self.scope.get_symbol(identifier) is not None:
                if self.scope.get_symbol(identifier).typeDef:
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} \'" + identifier + "\' is declared as type!")
                else:
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' already declared!")
                return None
            else:
                symbol = Symbol(name=identifier, varType=var_type, const=const)
                self.scope.add_symbol(symbol)
                node = DeclarationNode(ctx.start.line, ctx.start.column, children[:len(children) - 1], children[len(children) - 1])
                return node

        # assignment or definition
        if children.__contains__("="):
            node = children[children.index("=") + 1]
            if isinstance(node, IntNode) or isinstance(node, FloatNode):
                node = node.value
            identifier = children[children.index("=") - 1].value
            if isinstance(children[children.index("=") - 1], DerefNode):
                identifier = children[children.index("=") - 1].identifier.value
            # "=" is second character -> assignment and no definition.
            if children.index("=") == 1:
                if self.scope.lookup(identifier) is None:
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' not declared yet!")
                    return None
                if self.scope.lookup(identifier).const and isinstance(children[0], DerefNode):
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Pointer \'" + identifier + "\' is constant!")
                    return None
                lval = self.scope.lookup(identifier)
                rval = children[2]
                # Give warnings for implicit conversions.
                self.implicit_type_conversion(lval.type, rval)
                lvalPointer = 0
                rvalPointer = 0
                if isinstance(lval.type, PointerNode):
                    lvalPointer = int(lval.type.value)
                if isinstance(children[0], DerefNode):
                    if not self.scope.lookup(lval.name):
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + str(lval.name) + "\' not declared yet!")
                        return None
                    if not isinstance(self.scope.lookup(lval.name).type, PointerNode):
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Cannot dereference non-pointer type!")
                        return None
                    lvalPointer = int(self.scope.lookup(lval.name).type.value) - int(lval.type.value)
                rval = node
                if isinstance(rval, AddrNode) or isinstance(rval, IdentifierNode):
                    if isinstance(rval, AddrNode):
                        if not self.scope.lookup(rval.value.value):
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + rval.value.value + "\' not declared yet!")
                            return None
                        rvalType = self.scope.lookup(rval.value.value).type
                        if isinstance(rvalType, PointerNode):
                            rvalPointer = int(rvalType.value) + 1
                        else:
                            rvalPointer = 1
                    else:
                        if not self.scope.lookup(rval.value):
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + rval.value + "\' not declared yet!")
                            return None
                        rvalType = self.scope.lookup(rval.value).type
                        if isinstance(rvalType, PointerNode):
                            rvalPointer = int(rvalType.value)
                if isinstance(rval, DerefNode):
                    if not self.scope.lookup(rval.identifier.value):
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + rval.identifier.value + "\' not declared yet!")
                        return None
                    rvalType = self.scope.lookup(rval.identifier.value).type
                    if isinstance(rvalType, PointerNode):
                        rvalPointer = int(rvalType.value) - int(rval.value)
                    else:
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Cannot dereference non-pointer type!")
                        return None
                if lvalPointer != rvalPointer:
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Pointer type mismatch!")
                    return None
                # If variable is constant --> error. Otherwise set value.
                if self.scope.lookup(identifier).const and not isinstance(self.scope.lookup(identifier).type, PointerNode):
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' is constant!")
                    return None
                else:
                    self.scope.lookup(identifier).value = node
                    node = AssignmentNode(ctx.start.line, ctx.start.column, children[0], children[2])
                    return node
            else:
                # "=" is not second character -> definition.
                if self.scope.get_symbol(identifier) is not None:
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' already declared!")
                    return None
                else:
                    var_type = children[children.index("=") - 2].value
                    const = len(children) > 4
                    value = node
                    if isinstance(children[children.index("=") - 2], PointerNode):
                        var_type = children[children.index("=") - 2]
                        const = len(var_type.type) > 1
                    symbol = Symbol(name=identifier, varType=var_type, const=const)
                    lval = symbol
                    rval = children[len(children) - 1]
                    # Give warnings for implicit conversions.
                    self.implicit_type_conversion(var_type, rval)
                    lvalPointer = 0
                    rvalPointer = 0
                    if isinstance(lval.type, PointerNode):
                        lvalPointer = int(lval.type.value)
                    rval = node
                    if isinstance(rval, AddrNode) or isinstance(rval, IdentifierNode):
                        if isinstance(rval, AddrNode):
                            if not self.scope.get_symbol(rval.value.value):
                                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + rval.value.value + "\' not declared yet!")
                                return None
                            rvalType = self.scope.get_symbol(rval.value.value).type
                            if isinstance(rvalType, PointerNode):
                                rvalPointer = int(rvalType.value) + 1
                            else:
                                rvalPointer = 1
                        else:
                            if not self.scope.get_symbol(rval.value):
                                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + rval.value + "\' not declared yet!")
                                return None
                            rvalType = self.scope.get_symbol(rval.value).type
                            if isinstance(rvalType, PointerNode):
                                rvalPointer = int(rvalType.value)
                    elif isinstance(rval, DerefNode):
                        if not self.scope.get_symbol(rval.identifier.value):
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + rval.identifier.value + "\' not declared yet!")
                            return None
                        rvalType = self.scope.get_symbol(rval.identifier.value).type
                        if isinstance(rvalType, PointerNode):
                            rvalPointer = int(rvalType.value) - int(rval.value)
                        else:
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Cannot dereference non-pointer type!")
                            return None
                    if lvalPointer != rvalPointer:
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Pointer type mismatch!")
                        return None
                    self.scope.add_symbol(symbol)
                    node = DefinitionNode(ctx.start.line, ctx.start.column, children[:len(children) - 3], children[children.index("=") - 1], children[children.index("=") + 1])
                    return node

    def visitLvalue(self, ctx):
        children = []
        for line in ctx.getChildren():
            child = self.visit(line)
            if isinstance(child, list):
                children.extend(child)
            else:
                if child:
                    children.append(child)
        return children

    def visitIdentifier(self, ctx):
        node = IdentifierNode(ctx.getText(), ctx.start.line, ctx.start.column)
        return node

    def visitComment(self, ctx):
        node = CommentNode(ctx.getText(), ctx.start.line, ctx.start.column)
        return node

    def visitPostFixDecrement(self, ctx):
        identifier = ctx.getText()[:-2]
        if not self.scope.lookup(identifier):
            raise Exception("Variable \'" + identifier + "\' not declared yet!")
        node = PostFixNode(identifier, ctx.start.line, ctx.start.column, 'dec')
        return node

    def visitPostFixIncrement(self, ctx):
        identifier = ctx.getText()[:-2]
        if not self.scope.lookup(identifier):
            raise Exception("Variable \'" + identifier + "\' not declared yet!")
        node = PostFixNode(identifier, ctx.start.line, ctx.start.column, 'inc')
        return node

    def visitPreFixDecrement(self, ctx):
        identifier = ctx.getText()[2:]
        if not self.scope.lookup(identifier):
            raise Exception("Variable \'" + identifier + "\' not declared yet!")
        node = PreFixNode(identifier, ctx.start.line, ctx.start.column, 'dec')
        return node

    def visitPreFixIncrement(self, ctx):
        identifier = ctx.getText()[2:]
        if not self.scope.lookup(identifier):
            raise Exception("Variable \'" + identifier + "\' not declared yet!")
        node = PreFixNode(identifier, ctx.start.line, ctx.start.column, 'inc')
        return node

    def visitAddr(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)
        identifier = self.visit(children[1])
        if self.scope.lookup(identifier.value) is None:
            raise Exception("Variable \'" + identifier.value + "\' not declared yet!")
        node = AddrNode(identifier, ctx.start.line, ctx.start.column)
        return node

    def visitPointer(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)
        node = PointerNode(len(children) - 1, ctx.start.line, ctx.start.column, self.visit(children[0]))
        return node

    def visitDeref(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)
        identifier = self.visit(children[len(children) - 1])
        if self.scope.lookup(identifier.value) is None:
            raise Exception("Variable \'" + identifier.value + "\' not declared yet!")
        node = DerefNode(len(children) - 1, ctx.start.line, ctx.start.column, self.visit(children[len(children)-1]))
        return node

    def visitType(self, ctx):
        types = []
        for type in ctx.getChildren():
            types.append(TypeNode(type.getText(), ctx.start.line, ctx.start.column))
        return types

    def visitRvalue(self, ctx):
        lines = []
        for line in ctx.getChildren():
            lines.append(line)
        if len(lines) == 3:
            if str(lines[0]) == "(" and ")" == str(lines[2]):
                node = self.visit(lines[1])
                return node
            node = ProgramNode(0, 0)
            match str(lines[1]):
                case "/":
                    if not isinstance(self.visit(lines[2]).value, str) and int(self.visit(lines[2]).value) == 0:
                        raise Exception("Division by zero!")
                    node = DivNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "%":
                    node = ModNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "*":
                    node = MultNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "-":
                    node = MinusNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "+":
                    node = PlusNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case ">":
                    node = GTNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "<":
                    node = LTNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "==":
                    node = EQNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case ">=":
                    node = GTEQNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "<=":
                    node = LTEQNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "!=":
                    node = NEQNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "<<":
                    node = SLNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case ">>":
                    node = SRNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "&":
                    node = BitwiseAndNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "|":
                    node = BitwiseOrNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "^":
                    node = BitwiseXorNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "&&":
                    node = LogicalAndNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "||":
                    node = LogicalOrNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
            return node
        if len(lines) == 2:
            if str(lines[0]) == "!":
                node = LogicalNotNode(ctx.start.line, ctx.start.column, [self.visit(lines[1])])
                return node
        node = self.visitChildren(ctx)
        return node

    def visitLiteral(self, ctx):
        literal = ctx.getText()
        if literal.startswith("\'"):
            for i in literal:
                if i.isalnum():
                    node = CharNode(ord(i), ctx.start.line, ctx.start.column)
                    return node
        if float(literal) % 1 == 0:
            node = IntNode(ctx.getText(), ctx.start.line, ctx.start.column)
            return node
        node = FloatNode(ctx.getText(), ctx.start.line, ctx.start.column)
        return node

    def visitExplicitConversion(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)
        type = children[1].getText()
        node = ExplicitConversionNode(ctx.start.line, ctx.start.column, type)
        return node


    def visitPrintfStatement(self, ctx):
        children = []
        for line in ctx.getChildren():
            child = self.visit(line)
            if isinstance(child, list):
                children.extend(child)
            else:
                if child:
                    children.append(child)
        return PrintfNode(ctx.start.line, ctx.start.column, children)


    def visitFormatSpecifier(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)
        return FormatSpecifierNode(ctx.start.line, ctx.start.column, children[0].getText())


    def visitTypedef(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)

        name = children[2].getText()
        type = children[1].getText()

        if self.scope.get_symbol(name) is not None:
            if not self.scope.get_symbol(name).typeDef:
                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} \'" + name + "\' is declared a variable!")
                return None

        self.scope.add_symbol(Symbol(name=name, varType=type, typeDef=True, const=False))
        return TypedefNode(ctx.start.line, ctx.start.column, children[1].getText(), children[2].getText())
