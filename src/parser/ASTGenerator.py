from src.antlr_files.Proj_2.Grammar_Project_2Parser import Grammar_Project_2Parser
from src.antlr_files.Proj_2.Grammar_Project_2Visitor import Grammar_Project_2Visitor as Visitor

from src.parser.AST import *
from src.parser.SymbolTable import SymbolTableTree, Symbol


def removeVariable(symbolTable, node):
    if isinstance(node, Node):
        children = [node]
        i = 0
        while i < len(children):
            for child in children[i].children:
                children.append(child)
            if isinstance(children[i], IdentifierNode):
                var = symbolTable.lookup(children[i].value)
                if var is None:
                    raise Exception("Variable \'" + children[i].value + "\' not declared!")
                if isinstance(var.value, int) or isinstance(var.value, str):
                    val = str(var.value).strip('\'')
                    if val.isalnum():
                        children[i].__class__ = IntNode
                        children[i].value = var.value
                        children[i].children = []
                    else:
                        children[i].__class__ = FloatNode
                        children[i].value = var.value
                        children[i].children = []
                else:
                    children[i].__class__ = type(var.value)
                    children[i].children = var.value.children
                    children[i].value = var.value
            i += 1
        a = 5
        pass


class ASTGenerator(Visitor):

    def __init__(self):
        self.scope = SymbolTableTree()

    def visitProgram(self, ctx):
        children = []
        for line in ctx.getChildren():
            node = self.visit(line)
            if node is not None:
                children.append(node)
        node = ProgramNode(ctx.start.line, ctx.start.column, children)
        return [node, self.scope]

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
            elif line.getText() == "=":
                children.append(line.getText())
            else:
                child = self.visit(line)
                if isinstance(child, list):
                    children.extend(child)
                else:
                    children.append(child)
        if len(children) >= 2:
            # Ends with type + identifier -> declaration.
            if isinstance(children[len(children) - 2], TypeNode) and isinstance(children[len(children) - 1], IdentifierNode):
                identifier = children[len(children) - 1].value
                var_type = children[len(children) - 2].value
                const = len(children) > 2

                # Check if variable already declared in current scope.
                if self.scope.get_symbol(identifier) is not None:
                    raise Exception("Variable \'" + identifier + "\' already declared!")
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
                # "=" is second character -> assignment and no definition.
                if children.index("=") == 1:
                    if self.scope.lookup(identifier) is None:
                        raise Exception("Variable \'" + identifier + "\' not declared yet!")
                    else:
                        # If variable is constant --> error. Otherwise set value.
                        if self.scope.lookup(identifier).const:
                            raise Exception("Variable \'" + identifier + "\' is constant!")
                        else:
                            self.scope.lookup(identifier).value = node
                            node = AssignmentNode(ctx.start.line, ctx.start.column, children[0], children[2])
                            return node
                else:
                    # "=" is not second character -> definition.
                    if self.scope.lookup(identifier) is not None:
                        raise Exception(
                            "Variable \'" + identifier + "\' already declared!")
                    else:
                        var_type = children[children.index("=") - 2].value
                        const = len(children) > 4
                        value = node
                        symbol = Symbol(name=identifier, varType=var_type, const=const, value=value)
                        self.scope.add_symbol(symbol)
                        node = DefinitionNode(ctx.start.line, ctx.start.column, children[:len(children)-3], children[children.index("=") - 1], children[children.index("=") + 1])
                        return node

        node = children[0]
        return node

    def visitLvalue(self, ctx):
        children = []
        for line in ctx.getChildren():
            child = self.visit(line)
            if isinstance(child, list):
                children.extend(child)
            else:
                children.append(child)
        return children

    def visitIdentifier(self, ctx):
        node = IdentifierNode(ctx.getText(), ctx.start.line, ctx.start.column)
        return node

    def visitPostfixDecrement(self, ctx):
        identifier = ctx.getText()[:-2]
        value = int(self.scope.lookup(identifier).value) - 1
        self.scope.lookup(identifier).value = value
        return IntNode(str(value), ctx.start.line, ctx.start.column)

    def visitPostfixIncrement(self, ctx):
        identifier = ctx.getText()[:-2]
        value = int(self.scope.lookup(identifier).value) + 1
        self.scope.lookup(identifier).value = value
        return IntNode(str(value), ctx.start.line, ctx.start.column)

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
        node = PointerNode(len(children) - 1, ctx.start.line, ctx.start.column)
        node.setType(self.visit(children[0]))
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
                    if int(self.visit(lines[2]).value) == 0:
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
                    node = BitwiseAndNode(ctx.start.line, ctx.start.column,
                                          [self.visit(lines[0]), self.visit(lines[2])])
                case "|":
                    node = BitwiseOrNode(ctx.start.line, ctx.start.column, [self.visit(lines[0]), self.visit(lines[2])])
                case "^":
                    node = BitwiseXorNode(ctx.start.line, ctx.start.column,
                                          [self.visit(lines[0]), self.visit(lines[2])])
                case "&&":
                    node = LogicalAndNode(ctx.start.line, ctx.start.column,
                                          [self.visit(lines[0]), self.visit(lines[2])])
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
                    literal = ord(i)
        if float(literal) % 1 == 0:
            node = IntNode(ctx.getText(), ctx.start.line, ctx.start.column)
            return node
        node = FloatNode(ctx.getText(), ctx.start.line, ctx.start.column)
        return node
