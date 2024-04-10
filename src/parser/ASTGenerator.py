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

    def get_pointer_size(self, node):
        size = []
        if isinstance(node, DerefNode):
            identifier = node.identifier.value
            if self.scope.lookup(identifier):
                if isinstance(self.scope.lookup(identifier).type, PointerNode):
                    if int(self.scope.lookup(identifier).type.value) - 1 != 0:
                        size.append(int(self.scope.lookup(identifier).type.value) - int(node.value))
        elif isinstance(node, IdentifierNode):
            identifier = node.value
            if self.scope.lookup(identifier):
                if isinstance(self.scope.lookup(identifier).type, PointerNode):
                    size.append(int(self.scope.lookup(identifier).type.value))
        elif isinstance(node, AddrNode):
            identifier = node.value.value
            if self.scope.lookup(identifier):
                if isinstance(self.scope.lookup(identifier).type, PointerNode):
                    size.append(int(self.scope.lookup(identifier).type.value) + 1)
                else:
                    size.append(1)
        elif isinstance(node, CharNode) or isinstance(node, IntNode) or isinstance(node, FloatNode) or isinstance(node, str) or isinstance(node, int):
            return []
        elif isinstance(node, EQNode) or isinstance(node, NEQNode) or isinstance(node, LTEQNode) or isinstance(node, GTEQNode):
            return []
        else:
            for child in node.children:
                list = self.get_pointer_size(child)
                if len(list) != 0:
                    size.extend(list)
        return size

    def get_highest_type(self, rval):
        if isinstance(rval, DerefNode):
            identifier = rval.identifier.value
            if self.scope.lookup(identifier):
                if isinstance(self.scope.lookup(identifier).type, str):
                    return self.scope.lookup(identifier).type
                return self.scope.lookup(identifier).type.type[0].value
        elif isinstance(rval, IdentifierNode):
            identifier = rval.value
            if self.scope.lookup(identifier):
                if isinstance(self.scope.lookup(identifier).type, str):
                    return self.scope.lookup(identifier).type
                return self.scope.lookup(identifier).type.type[0].value
        elif isinstance(rval, IntNode):
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
            if isinstance(rval, ExplicitConversionNode):
                return type
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
        self.node = ProgramNode(line=ctx.start.line, pos=ctx.start.column, original=None, children=children)
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
        node = MainNode(line=ctx.start.line, pos=ctx.start.column, original="int main()", children=children)
        return node

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
                    if isinstance(child, IdentifierNode):
                        if self.scope.lookup(child.value) is None:
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + child.value + "\' not declared yet!")
                        else:
                            if self.scope.lookup(child.value).typeDef:
                                self.warnings.append("line {ctx.start.line}:{ctx.start.column} \'" + child.value + "\' useless type name in empty declaration!")
                    children.append(child)
        if len(children) == 0:
            return None
        else:
            return children

    def visitVariable(self, ctx):
        children = []
        original = ""
        for line in ctx.getChildren():
            if line.getText() == ";":
                pass
            elif line.getText() == "=":
                children.append(line.getText())
                original += "= "
            else:
                child = self.visit(line)
                if isinstance(child, list):
                    children.extend(child)
                    for item in child:
                        original += f"{item.original} "
                else:
                    if child is not None:
                        if isinstance(child, TypedefNode):
                            return child
                        children.append(child)
                        original += f"{child.original} "

        # Ends with type + identifier -> declaration.
        if (isinstance(children[len(children) - 2], TypeNode) or isinstance(children[len(children) - 2], PointerNode)) and isinstance(children[len(children) - 1], IdentifierNode):
            identifier = children[len(children) - 1].value
            var_type = children[len(children) - 2].value

            if isinstance(children[len(children) - 2], PointerNode):
                var_type = children[len(children) - 2].type[len(children[len(children) - 2].type) - 1].value

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
                node = DeclarationNode(line=ctx.start.line, pos=ctx.start.column, original=original, type=children[:len(children) - 1], lvalue=children[len(children) - 1])
                return node

        # assignment or definition
        if children.__contains__("="):
            node = children[children.index("=") + 1]
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
                if isinstance(children[0], DerefNode):
                    if not isinstance(self.scope.lookup(lval.name).type, PointerNode):
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Cannot dereference non-pointer type!")
                        return None
                rval = node
                if isinstance(rval, AddrNode) or isinstance(rval, IdentifierNode):
                    if isinstance(rval, AddrNode):
                        if not self.scope.lookup(rval.value.value):
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + rval.value.value + "\' not declared yet!")
                            return None
                    else:
                        if not self.scope.lookup(rval.value):
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + rval.value + "\' not declared yet!")
                            return None
                if isinstance(rval, DerefNode):
                    if not self.scope.lookup(rval.identifier.value):
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + rval.identifier.value + "\' not declared yet!")
                        return None
                    rvalType = self.scope.lookup(rval.identifier.value).type
                    if not isinstance(rvalType, PointerNode):
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Cannot dereference non-pointer type!")
                        return None
                # If variable is constant --> error. Otherwise set value.
                if self.scope.lookup(identifier).const and not isinstance(self.scope.lookup(identifier).type, PointerNode):
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' is constant!")
                    return None
                else:
                    self.implicit_type_conversion(lval.type, rval)
                    rval_ptr = self.get_pointer_size(rval)
                    lval_ptr = 0
                    var_type = self.scope.lookup(identifier).type
                    if isinstance(var_type, PointerNode):
                        lval_ptr = var_type.value
                    if len(rval_ptr) > 1:
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Invalid operands!")
                        return None
                    if len(rval_ptr):
                        if int(rval_ptr[0]) != int(lval_ptr):
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Pointer type mismatch!")
                            return None
                    self.scope.lookup(identifier).value = node
                    node = AssignmentNode(line=ctx.start.line, pos=ctx.start.column, original=original, lvalue=children[0], rvalue=children[2])
                    return node
            else:
                # "=" is not second character -> definition.
                identifier = children[children.index('=') - 1].value
                var_type = children[children.index('=') - 2].value

                if isinstance(children[children.index('=') - 2], PointerNode):
                    var_type = children[children.index('=') - 2].type[len(children[children.index('=') - 2].type) - 1].value

                # Check if type is declared.
                if var_type not in self.types:
                    if self.scope.lookup(var_type) is None:
                        self.errors.append(
                            f"line {ctx.start.line}:{ctx.start.column} Type \'" + var_type + "\' not declared yet!")
                        return None
                    elif not self.scope.lookup(var_type).typeDef:
                        self.errors.append(
                            f"line {ctx.start.line}:{ctx.start.column} \'" + var_type + "\' not declared as type!")
                        return None
                if self.scope.get_symbol(identifier) is not None:
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' already declared!")
                    return None
                else:
                    var_type = children[children.index("=") - 2].value
                    const = len(children) > 4
                    if isinstance(children[children.index("=") - 2], PointerNode):
                        var_type = children[children.index("=") - 2]
                        const = len(var_type.type) > 1
                    symbol = Symbol(name=identifier, varType=var_type, const=const)
                    lval = symbol
                    rval = children[len(children) - 1]
                    # Give warnings for implicit conversions.
                    rval = node
                    if isinstance(rval, AddrNode) or isinstance(rval, IdentifierNode):
                        if isinstance(rval, AddrNode):
                            if not self.scope.get_symbol(rval.value.value):
                                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + rval.value.value + "\' not declared yet!")
                                return None
                        else:
                            if not self.scope.get_symbol(rval.value):
                                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + rval.value + "\' not declared yet!")
                                return None
                            rvalType = self.scope.get_symbol(rval.value).type
                    elif isinstance(rval, DerefNode):
                        if not self.scope.get_symbol(rval.identifier.value):
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + rval.identifier.value + "\' not declared yet!")
                            return None
                        rvalType = self.scope.get_symbol(rval.identifier.value).type
                        if not isinstance(rvalType, PointerNode):
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Cannot dereference non-pointer type!")
                            return None
                    self.scope.add_symbol(symbol)
                    self.implicit_type_conversion(var_type, rval)
                    rval_ptr = self.get_pointer_size(rval)
                    lval_ptr = 0
                    if isinstance(var_type, PointerNode):
                        lval_ptr = var_type.value
                    if len(rval_ptr) > 1:
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Invalid operands!")
                        return None
                    if len(rval_ptr):
                        if int(rval_ptr[0]) != int(lval_ptr):
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Pointer type mismatch!")
                            return None
                    if lval_ptr != 0 and rval_ptr == []:
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Pointer type mismatch!")
                        return None
                    node = DefinitionNode(line=ctx.start.line, pos=ctx.start.column, original=original, type=children[:len(children) - 3], lvalue=children[children.index("=") - 1], rvalue=children[children.index("=") + 1])
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
        node = IdentifierNode(value=ctx.getText(), line=ctx.start.line, pos=ctx.start.column, original=ctx.getText())
        return node

    def visitConditional(self, ctx):
        children = []
        for line in ctx.getChildren():
            child = self.visit(line)
            if isinstance(child, list):
                children.extend(child)
            else:
                if child:
                    children.append(child)
        return children

    def visitIfStatement(self, ctx):
        children = []
        for line in ctx.getChildren():
            child = self.visit(line)
            if isinstance(child, list):
                children.extend(child)
            else:
                if child:
                    children.append(child)
        original = f"if ({children[0].original})" + "{}"
        node = IfStatementNode(line=ctx.start.line, pos=ctx.start.column, original=original, condition=children[0], body=children[1:])
        return node

    def visitElseIfStatement(self, ctx):
        children = []
        for line in ctx.getChildren():
            child = self.visit(line)
            if isinstance(child, list):
                children.extend(child)
            else:
                if child:
                    children.append(child)
        original = f"else if ({children[0].original})" + "{}"
        node = ElseIfStatementNode(line=ctx.start.line, pos=ctx.start.column, original=original, condition=children[0], body=children[1:])
        return node

    def visitElseStatement(self, ctx):
        children = []
        for line in ctx.getChildren():
            child = self.visit(line)
            if isinstance(child, list):
                children.extend(child)
            else:
                if child:
                    children.append(child)
        original = "else {}"
        node = ElseStatementNode(line=ctx.start.line, pos=ctx.start.column, original=original, body=children)
        return node

    def visitComment(self, ctx):

        node = CommentNode(ctx.getText(), line=ctx.start.line, pos=ctx.start.column, original="")
        return node

    def visitPostFixDecrement(self, ctx):
        identifier = ctx.getText()[:-2]
        if not self.scope.lookup(identifier):
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' not declared yet!")
            return None
        original = f"{identifier}--"
        node = PostFixNode(value=identifier, line=ctx.start.line, pos=ctx.start.column, original=original, op='dec')
        return node

    def visitPostFixIncrement(self, ctx):
        identifier = ctx.getText()[:-2]
        if not self.scope.lookup(identifier):
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' not declared yet!")
            return None
        original = f"{identifier}++"
        node = PostFixNode(value=identifier, line=ctx.start.line, pos=ctx.start.column, original=original, op='inc')
        return node

    def visitPreFixDecrement(self, ctx):
        identifier = ctx.getText()[2:]
        if not self.scope.lookup(identifier):
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' not declared yet!")
            return None
        original = f"--{identifier}"
        node = PreFixNode(value=identifier, line=ctx.start.line, pos=ctx.start.column, original=original, op='dec')
        return node

    def visitPreFixIncrement(self, ctx):
        identifier = ctx.getText()[2:]
        if not self.scope.lookup(identifier):
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' not declared yet!")
            return None
        original = f"++{identifier}"
        node = PreFixNode(value=identifier, line=ctx.start.line, pos=ctx.start.column, original=original, op='inc')
        return node

    def visitAddr(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)
        identifier = self.visit(children[1])
        if self.scope.lookup(identifier.value) is None:
            raise Exception("Variable \'" + identifier.value + "\' not declared yet!")
        original = ""
        node = AddrNode(value=identifier, line=ctx.start.line, pos=ctx.start.column, original=original)
        return node

    def visitPointer(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)
        original = ""
        for type in self.visit(children[0]):
            original += f"{type.original} "
        original += "*" * (len(children) - 1)
        node = PointerNode(value=len(children) - 1, line=ctx.start.line, pos=ctx.start.column, original=original, type=self.visit(children[0]))
        return node

    def visitDeref(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)
        identifier = self.visit(children[len(children) - 1])
        if self.scope.lookup(identifier.value) is None:
            raise Exception("Variable \'" + identifier.value + "\' not declared yet!")
        original = "*" * (len(children) - 1)
        original += f"{identifier.original}"
        node = DerefNode(value=len(children) - 1, line=ctx.start.line, pos=ctx.start.column, original=original, identifier=identifier)
        return node

    def visitType(self, ctx):
        types = []
        for type in ctx.getChildren():
            types.append(TypeNode(value=type.getText(), line=ctx.start.line, pos=ctx.start.column, original=type.getText()))
        return types

    def visitRvalue(self, ctx):
        lines = []
        for line in ctx.getChildren():
            lines.append(line)
        original = ""
        if len(lines) == 3:
            node = ProgramNode(line=0, pos=0, original="")
            if str(lines[0]) == "(" and ")" == str(lines[2]):
                node = self.visit(lines[1])
                node.original = f"({node.original})"
                return node
            original = f"{lines[0].getText()} {lines[1].getText()} {lines[2].getText()}"
            match str(lines[1]):
                case "/":
                    if not isinstance(self.visit(lines[2]).value, str) and int(self.visit(lines[2]).value) == 0:
                        raise Exception("Division by zero!")
                    node = DivNode(line=ctx.start.line, pos=ctx.start.column, original=original, children=[self.visit(lines[0]), self.visit(lines[2])])
                case "%":
                    node = ModNode(line=ctx.start.line, pos=ctx.start.column, original=original, children=[self.visit(lines[0]), self.visit(lines[2])])
                case "*":
                    node = MultNode(line=ctx.start.line, pos=ctx.start.column, original=original, children=[self.visit(lines[0]), self.visit(lines[2])])
                case "-":
                    node = MinusNode(line=ctx.start.line, pos=ctx.start.column, original=original, children=[self.visit(lines[0]), self.visit(lines[2])])
                case "+":
                    node = PlusNode(line=ctx.start.line, pos=ctx.start.column, original=original, children=[self.visit(lines[0]), self.visit(lines[2])])
                case "<<":
                    node = SLNode(line=ctx.start.line, pos=ctx.start.column, original=original, children=[self.visit(lines[0]), self.visit(lines[2])])
                case ">>":
                    node = SRNode(line=ctx.start.line, pos=ctx.start.column, original=original, children=[self.visit(lines[0]), self.visit(lines[2])])
                case "&":
                    node = BitwiseAndNode(line=ctx.start.line, pos=ctx.start.column, original=original, children=[self.visit(lines[0]), self.visit(lines[2])])
                case "|":
                    node = BitwiseOrNode(line=ctx.start.line, pos=ctx.start.column, original=original, children=[self.visit(lines[0]), self.visit(lines[2])])
                case "^":
                    node = BitwiseXorNode(line=ctx.start.line, pos=ctx.start.column, original=original, children=[self.visit(lines[0]), self.visit(lines[2])])
                case "&&":
                    node = LogicalAndNode(line=ctx.start.line, pos=ctx.start.column, original=original, children=[self.visit(lines[0]), self.visit(lines[2])])
                case "||":
                    node = LogicalOrNode(line=ctx.start.line, pos=ctx.start.column, original=original, children=[self.visit(lines[0]), self.visit(lines[2])])
            if isinstance(node.children[0], IdentifierNode):
                identifier = node.children[0].value
                if self.scope.lookup(identifier) is None:
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' not declared yet!")
                    return node
                if self.scope.lookup(identifier).typeDef:
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} \'" + identifier + "\' is declared as type!")
                    return node
            if isinstance(node.children[1], IdentifierNode):
                identifier = node.children[1].value
                if self.scope.lookup(identifier) is None:
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' not declared yet!")
                    return node
                if self.scope.lookup(identifier).typeDef:
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} \'" + identifier + "\' is declared as type!")
                    return node
            return node
        if len(lines) == 2:
            original = f"{lines[0].getText()} {lines[1].getText()}"
            if str(lines[0]) == "!":
                node = LogicalNotNode(line=ctx.start.line, pos=ctx.start.column, original=original, children=[self.visit(lines[1])])
            elif str(lines[0]) == "~":
                node = BitwiseNotNode(line=ctx.start.line, pos=ctx.start.column, original=original, children=[self.visit(lines[1])])
            else:
                node = self.visit(lines[1])
                original = f"{lines[0].getText()} {node.original}"
                node.original = original
                node.children[0] = self.visit(lines[0])
                return node
            if isinstance(node.children[0], IdentifierNode):
                identifier = lines[1].getText()
                if self.scope.lookup(identifier) is None:
                    self.errors.append(
                        f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' not declared yet!")
                    return node
                if self.scope.lookup(identifier).typeDef:
                    self.errors.append(
                        f"line {ctx.start.line}:{ctx.start.column} \'" + identifier + "\' is declared as type!")
                    return node
            return node
        node = self.visitChildren(ctx)
        if len(lines) == 1:
            negatives = 0
            for child in lines[0].children:
                if child.getText() == "-":
                    negatives += 1
            if negatives % 2:
                node.value = - int(node.value)
        return node

    def visitConditionalExpression(self, ctx):
        children = []
        node = ProgramNode
        for line in ctx.getChildren():
            children.append(line)
        original = f"{children[0].getText()} {self.visit(children[1]).original}"
        match children[0].getText():
            case ">":
                node = GTNode(line=ctx.start.line, pos=ctx.start.column, original=original, children=[self.visit(children[1]), self.visit(children[1])])
            case "<":
                node = LTNode(line=ctx.start.line, pos=ctx.start.column, original=original, children=[self.visit(children[1]), self.visit(children[1])])
            case "==":
                node = EQNode(line=ctx.start.line, pos=ctx.start.column, original=original, children=[self.visit(children[1]), self.visit(children[1])])
            case ">=":
                node = GTEQNode(line=ctx.start.line, pos=ctx.start.column, original=original, children=[self.visit(children[1]), self.visit(children[1])])
            case "<=":
                node = LTEQNode(line=ctx.start.line, pos=ctx.start.column, original=original, children=[self.visit(children[1]), self.visit(children[1])])
            case "!=":
                node = NEQNode(line=ctx.start.line, pos=ctx.start.column, original=original, children=[self.visit(children[1]), self.visit(children[1])])
        return node

    def visitLiteral(self, ctx):
        literal = ctx.getText()
        if literal.startswith("\'"):
            for i in literal:
                if i.isalnum():
                    node = CharNode(value=str(ord(i)), line=ctx.start.line, pos=ctx.start.column, original=ctx.getText())
                    return node
        elif '.' in literal:
            node = FloatNode(value=ctx.getText(), line=ctx.start.line, pos=ctx.start.column, original=ctx.getText())
        elif literal.isdigit():
            node = IntNode(value=ctx.getText(), line=ctx.start.line, pos=ctx.start.column, original=ctx.getText())
        return node

    def visitExplicitConversion(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)
        type = children[1].getText()
        original = f"({type}) {children[len(children) - 1].getText()}"
        node = ExplicitConversionNode(line=ctx.start.line, pos=ctx.start.column, original=original, type=type, rval=self.visit(children[len(children) - 1]))
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
        original = f"printf({children[0].original}, {children[1].original})"
        node = PrintfNode(line=ctx.start.line, pos=ctx.start.column, original=original, specifier=children[0].specifier, node=children[1])
        if self.scope.lookup(node.node.value) is None:
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + node.node.value + "\' not declared yet!")
            return ProgramNode(line=0, pos=0, original="")
        if self.scope.lookup(node.node.value).typeDef:
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} \'" + node.node.value + "\' is declared as type!")
            return ProgramNode(line=0, pos=0, original="")
        return node

    def visitFormatSpecifier(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)
        original = f"{children[0].getText()}"
        return FormatSpecifierNode(line=ctx.start.line, pos=ctx.start.column, original=original, specifier=children[0].getText())

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
        original = ""
        return TypedefNode(line=ctx.start.line, pos=ctx.start.column, original=original, type=children[1].getText(), identifier=children[2].getText())

    def visitWhileLoop(self, ctx):
        children = []
        for child in ctx.getChildren():
            child = self.visit(child)
            if child is not None:
                if isinstance(child, list):
                    children.extend(child)
                else:
                    children.append(child)
        original = f"while ({children[0].original}) " + "{}"
        node = WhileLoopNode(line=ctx.start.line, pos=ctx.start.column, original=original, condition=children[0], body=children[1:])
        return node

    def visitForLoop(self, ctx):
        self.scope.open_scope()
        children = []
        for child in ctx.getChildren():
            child = self.visit(child)
            if child is not None:
                if isinstance(child, list):
                    children.extend(child)
                else:
                    children.append(child)
        body = children[3:]
        if children[2] is not None:
            body.append(children[2])
        original = ""
        condition = IntNode('1', line=ctx.start.line, pos=ctx.start.column, original='1')
        if children[1] is not None:
            condition = children[1]
        original = "for ("
        if children[0] is not None:
            original += f"{children[0].original}; "
        else:
            original += "; "
        if not isinstance(condition, IntNode):
            original += f"{condition.original}; "
        else:
            original += "; "
        if children[2] is not None:
            original += f"{children[2].original}) " + "{}"
        else:
            original += ") {}"
        node = WhileLoopNode(line=ctx.start.line, pos=ctx.start.column, original=original, condition=condition, body=body)
        self.scope.close_scope()
        return node if children[0] is None else [children[0], node]

    def visitForCondition(self, ctx):
        children = []
        i = 0
        for child in ctx.getChildren():
            text = child.getText()
            child = self.visit(child)
            if child is None:
                if text == ';':
                    if i == len(children):
                        children.append(None)
                    i += 1
                    continue
            if isinstance(child, list):
                children.extend(child)
            else:
                children.append(child)
        if len(children) < 3:
            children.append(None)
        return children

    def visitJumpStatement(self, ctx):
        name = ctx.getText()
        match name:
            case 'break':
                return BreakNode(line=ctx.start.line, pos=ctx.start.column, original="break")
            case 'continue':
                return ContinueNode(line=ctx.start.line, pos=ctx.start.column, original="continue")

    def visitSwitchStatement(self, ctx):
        children = []
        for child in ctx.getChildren():
            child = self.visit(child)
            if child is not None:
                if isinstance(child, list):
                    children.extend(child)
                else:
                    children.append(child)
        rval = children[0]
        cases = children[1:]
        ifNodes = []
        # Count default cases
        i = 0
        defaultNodes = []
        for case in cases:
            if case.condition == 'Default':
                defaultNodes.insert(0, i)
            i += 1
        # Multiple default cases.
        if len(defaultNodes) > 1:
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Multiple default cases in switch statement!")
        # Put default cases at back.
        for index in defaultNodes:
            case = cases[index]
            cases.remove(case)
            cases.append(case)
        # Check for duplicate cases.
        for case1 in cases:
            for case2 in cases:
                if case1 != case2:
                    if case1.condition != 'Default' and case2.condition != 'Default':
                        if case1.condition.value == case2.condition.value:
                            self.errors.append(f"line {case1.line}:{case1.pos} Duplicate cases in switch statement!")
        # Make if statements
        if len(cases) == 0:
            return None
        not_default_condition = None
        condition_since_break = None
        for case in cases:
            original = ""
            if case.condition == 'Default':
                defaultCondition = IntNode(value='1', line=case.line, pos=case.pos, original='1')
                if not_default_condition is not None:
                    original = f"(! {not_default_condition.original})"
                    not_default_condition = LogicalNotNode(case.line, case.pos, original=original, children=[not_default_condition])
                    original = f"({not_default_condition.original} && {defaultCondition.original})"
                    defaultCondition = LogicalAndNode(case.line, case.pos, original=original, children=[not_default_condition, defaultCondition])
                    original = f"default:"
                ifNode = IfStatementNode(line=case.line, pos=case.pos, original=original, condition=defaultCondition, body=case.children)
                ifNodes.append(ifNode)
            else:
                if condition_since_break is None:
                    original = f"({rval.original} == {case.condition.original})"
                    condition_since_break = EQNode(line=case.line, pos=case.pos, original=original, children=[rval, case.condition])
                    original = f"case {case.condition.original}:"
                else:
                    original = f"({rval.original} == {case.condition.original})"
                    case_condition = EQNode(line=case.line, pos=case.pos, original=original, children=[rval, case.condition])
                    original = f"({condition_since_break.original} || {case_condition.original})"
                    condition_since_break = LogicalOrNode(line=case.line, pos=case.pos, original=original, children=[condition_since_break, case_condition])
                    original = f"case {case.condition.original}:"
                ifNodes.append(IfStatementNode(line=case.line, pos=case.pos, original=original, condition=condition_since_break, body=case.children))
                for child in case.children:
                    # If break found, set condition to case condition.
                    if isinstance(child, BreakNode):
                        if not_default_condition is None:
                            not_default_condition = condition_since_break
                        else:
                            not_default_condition = LogicalAndNode(line=case.line, pos=case.pos, original=original, children=[not_default_condition, condition_since_break])
                        condition_since_break = None
                        break
        # Remove code after break.
        for case in cases:
            delete = False
            for child in case.children:
                if delete:
                    case.children.remove(child)
                if isinstance(child, BreakNode):
                    delete = True
                    case.children.remove(child)

        return ifNodes

    def visitSwitchCase(self, ctx):
        children = []
        for child in ctx.getChildren():
            child = self.visit(child)
            if child is not None:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, DeclarationNode) or isinstance(item, DefinitionNode):
                            self.scope.remove_symbol(item.lvalue.value)
                            self.errors.append(f"line {item.line}:{item.pos} Cannot declare variable in switch case!")
                        else:
                            children.append(item)
                else:
                    if isinstance(child, DeclarationNode) or isinstance(child, DefinitionNode):
                        self.scope.remove_symbol(child)
                        self.errors.append(f"line {child.line}:{child.pos} Cannot declare variable in switch case!")
                    else:
                        children.append(child)
        original = ""
        if len(children) == 0:
            return CaseNode(line=ctx.start.line, pos=ctx.start.column, original=original, condition="Default")
        if isinstance(children[0], CharNode) or isinstance(children[0], IntNode) or isinstance(children[0], FloatNode):
            return CaseNode(line=ctx.start.line, pos=ctx.start.column, original=original, condition=children[0], children=children[1:])
        return CaseNode(line=ctx.start.line, pos=ctx.start.column, original=original, condition="Default", children=children)
