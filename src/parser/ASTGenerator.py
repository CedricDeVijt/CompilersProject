import copy

from src.antlr_files.GrammarParser import GrammarParser as Parser, GrammarParser
from src.antlr_files.GrammarVisitor import GrammarVisitor as Visitor

from src.parser.AST import *
from src.parser.dotGenerator import expandExpression
from src.parser.SymbolTable import SymbolTableTree, Symbol


def matching_params(type1, type2):
    # Amount of params
    if len(type1) != len(type2):
        return False
    for i in range(0, len(type1)):
        # Check if both are identifier or both are by reference
        if type(type1[i][1]) != type(type2[i][1]):
            return False
        # Ignore identifier
        type_1 = type1[i][0]
        type_2 = type2[i][0]
        # If types are different --> different params, except if list.
        if (isinstance(type_1, TypeNode) or isinstance(type_1, list)) and isinstance(type_2, PointerNode):
            return False
        if (isinstance(type_2, TypeNode) or isinstance(type_2, list)) and isinstance(type_1, PointerNode):
            return False
        if isinstance(type_1, PointerNode):
            # Check depth of pointer
            if type_1.value != type_2.value:
                return False
            # Check values of type (ignore const)
            if isinstance(type_1.type, list) and isinstance(type_2.type, list):
                if type_1.type[len(type_1.type) - 1].value != type_2.type[len(type_2.type) - 1].value:
                    return False
            elif isinstance(type_1.type, list):
                if type_1.type[len(type_1.type) - 1].value != type_2.type.value:
                    return False
            elif isinstance(type_2.type, list):
                if type_1.type.value != type_2.type[len(type_2.type) - 1].value:
                    return False
            else:
                if type_1.type.value != type_2.type.value:
                    return False
        elif isinstance(type_1, list) and isinstance(type_2, list):
            if type_1[len(type_1) - 1].value != type_2[len(type_2) - 1].value:
                return False
        elif isinstance(type_1, list):
            if type_1[len(type_1) - 1].value != type_2.value:
                return False
        elif isinstance(type_2, list):
            if type_1.value != type_2[len(type_2) - 1].value:
                return False
        else:
            if type_1.value != type_2.value:
                return False
    return True


class ASTGenerator(Visitor):

    def __init__(self):
        self.scope = SymbolTableTree()
        self.errors = []
        self.warnings = []
        self.node = None
        self.has_main = False
        self.types = ['int', 'float', 'char']

    def get_pointer_size(self, node, by_ref=False):
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
                    if by_ref:
                        size.append(int(self.scope.lookup(identifier).type.value))
                    else:
                        size.append(int(self.scope.lookup(identifier).type.value) + 1)
                else:
                    size.append(1)
        elif isinstance(node, PointerNode):
            size.append(int(node.value))
        elif isinstance(node, CharNode) or isinstance(node, IntNode) or isinstance(node, FloatNode) or isinstance(node, str) or isinstance(node, int):
            return []
        elif isinstance(node, EQNode) or isinstance(node, NEQNode) or isinstance(node, LTEQNode) or isinstance(node, GTEQNode):
            return []
        elif isinstance(node, StringNode):
            return [1]
        else:
            for child in node.children:
                plist = self.get_pointer_size(child)
                if len(plist) != 0:
                    size.extend(plist)
        return size

    def get_highest_type(self, rval: Node):
        type_check_dict = {
            DerefNode: lambda rval: self.lookup_and_get_type(rval.identifier.value),
            IdentifierNode: lambda rval: self.lookup_and_get_type(rval.value),
            AddrNode: lambda rval: self.lookup_and_get_type(rval.value.value),
            CharNode: lambda rval: 'char',
            IntNode: lambda rval: 'int',
            FloatNode: lambda rval: 'float',
            StringNode: lambda rval: 'string',
            Node: self.handle_node_type
        }
        for key, value in type_check_dict.items():
            if isinstance(rval, key):
                return value(rval)

        if rval in ['char', 'int', 'float']:
            return rval

        return 'char'

    def lookup_and_get_type(self, identifier):
        if isinstance(identifier, IdentifierNode):
            identifier = identifier.value
        if isinstance(identifier, ArrayIdentifierNode):
            identifier = identifier.value
        if isinstance(identifier, DerefNode):
            identifier = identifier.identifier.value
        symbols = self.scope.lookup(identifier)
        if symbols:
            if isinstance(symbols.type, str):
                return symbols.type
            if isinstance(symbols.type, PointerNode):
                if isinstance(symbols.type.type, list):
                    var_type = symbols.type.type[len(symbols.type.type) - 1].value
                else:
                    var_type = symbols.type.type.value
                if var_type == 'char' and int(symbols.type.value) == 1:
                    return 'string'
                return var_type
            if symbols.symbol_type == 'array' and symbols.type.value == 'char':
                return 'string'
            return symbols.type.value

    def handle_node_type(self, rval):
        if isinstance(rval, PointerNode):
            if isinstance(rval.type, list):
                return rval.type[len(rval.type) - 1].value
            return self.get_highest_type(rval.type)
        if isinstance(rval, AddrNode):
            return self.lookup_and_get_type(rval.value.value)
        if isinstance(rval, ExplicitConversionNode):
            return rval.type
        if isinstance(rval, (PreFixNode, PostFixNode)):
            return self.lookup_and_get_type(rval.value)
        if isinstance(rval, FunctionCallNode):
            return self.handle_function_call(rval)
        if isinstance(rval, TypeNode):
            if rval.value in ['char', 'int', 'float']:
                return rval.value
            symbols = self.scope.lookup(rval.value)
            if symbols is not None and isinstance(symbols, Symbol):
                return self.get_highest_type(symbols.type)
        if isinstance(rval, ArrayIdentifierNode):
            return self.lookup_and_get_type(rval.value)
        if isinstance(rval, StructMemberNode):
            return self.get_highest_type(rval.type)
        type1 = self.get_highest_type(rval.children[0]) if not isinstance(rval, ProgramNode) else 'char'
        type2 = self.get_highest_type(rval.children[-1]) if not isinstance(rval, ProgramNode) else 'char'
        if 'float' in [type1, type2]:
            return 'float'
        elif 'int' in [type1, type2]:
            return 'int'
        return 'char'

    def handle_function_call(self, rval):
        symbols = self.scope.lookup(rval.value) if self.scope.lookup(rval.value) is not None else []
        if isinstance(symbols, Symbol):
            symbols = [symbols]
        for symbol in symbols:
            if len(symbol.params) != len(rval.arguments):
                continue

            similar = all(self.get_highest_type(param[0]) == self.get_highest_type(arg) for param, arg in zip(symbol.params, rval.arguments))
            if similar:
                return self.get_highest_type(symbol.type)
        return 'char'

    def implicit_type_conversion(self, lvalType, rval):
        def check_type_and_lookup(type_value):
            while type_value not in ['char', 'int', 'float', 'string']:
                if isinstance(type_value, TypeNode):
                    type_value = type_value.value
                elif isinstance(type_value, PointerNode):
                    type_value = type_value.type[-1].value if isinstance(type_value.type,
                                                                         list) else type_value.type.value
                elif isinstance(type_value, list):
                    type_value = type_value[-1].value
                if self.scope.lookup(type_value) is not None and self.scope.lookup(type_value).symbol_type == 'typeDef':
                    type_value = self.scope.lookup(type_value).type
            return type_value

        lvalType = check_type_and_lookup(lvalType)
        rvalType = self.get_highest_type(rval)
        rvalType = check_type_and_lookup(rvalType)

        if lvalType == rvalType:
            return
        elif lvalType == 'int' and rvalType == 'float':
            self.warnings.append(f"line {rval.line}:{rval.column} Implicit type conversion from float to int!")
        elif lvalType == 'char' and rvalType == 'float':
            self.warnings.append(f"line {rval.line}:{rval.column} Implicit type conversion from float to char!")
        elif lvalType == 'char' and rvalType == 'int':
            self.warnings.append(f"line {rval.line}:{rval.column} Implicit type conversion from int to char!")
        elif lvalType == 'char' and rvalType == 'string':
            pass

    def contains_node(self, node, node_type):
        if isinstance(node, node_type):
            return True

        children = node.body if isinstance(node, IfStatementNode) else node.children
        for child in children:
            if self.contains_node(child, node_type):
                return True

        return False

    def set_valid(self, node, node_type):
        if node is None:
            return
        if isinstance(node, node_type):
            node.valid = True
        if isinstance(node, IfStatementNode):
            for child in node.body[0].children:
                self.set_valid(child, node_type)
        elif isinstance(node, FunctionNode) or isinstance(node, WhileLoopNode):
            for child in node.body:
                self.set_valid(child, node_type)
        else:
            for child in node.children:
                self.set_valid(child, node_type)

    def remove_type(self, node, node_type):
        delete = []
        if isinstance(node, IfStatementNode) or isinstance(node, FunctionNode) or isinstance(node, WhileLoopNode):
            for child in node.body:
                if isinstance(child, node_type):
                    delete.append(child)
                self.remove_type(child, node_type)
            for child in delete:
                node.body.remove(child)
        else:
            for child in node.children:
                if isinstance(child, node_type):
                    delete.append(child)
                self.remove_type(child, node_type)
            for child in delete:
                node.children.remove(child)

    def place_node_before_type(self, node1, node2, node_type):
        node2 = copy.deepcopy(node2)
        if isinstance(node1, IfStatementNode):
            for child in node1.body[0].children:
                if isinstance(child, node_type):
                    index = node1.body[0].children.index(child)
                    node1.body[0].children.insert(index, node2)
                    break
                else:
                    self.place_node_before_type(child, node2, node_type)
        else:
            for child in node1.children:
                if isinstance(child, node_type):
                    index = node1.children.index(child)
                    node1.body.insert(index, node2)
                    break
                else:
                    self.place_node_before_type(child, node2, node_type)

    def check_validity(self, node):
        if node is None:
            return
        if isinstance(node, IfStatementNode):
            for child in node.body[0].children:
                self.check_validity(child)
        elif isinstance(node, FunctionNode) or isinstance(node, WhileLoopNode):
            for child in node.body:
                self.check_validity(child)
        for child in node.children:
            self.check_validity(child)
        if hasattr(node, 'valid'):
            if not node.valid:
                self.errors.append(f"line {node.line}:{node.column} {node.value} is not in it's respective while/switch statement or in a function.")

    def remove_unused_children(self, children: list):
        # check in current scope which variables are not used. (remove them)
        unused_children = []
        for child in children:
            if isinstance(child, DeclarationNode) or isinstance(child, DefinitionNode):
                # find symbol in scope
                symbol = self.scope.lookup(child.lvalue.value, remove_unused=True)
                if symbol is not None and not symbol.used:
                    unused_children.append(child)
        for child in unused_children:
            children.remove(child)

    def check_returns(self, node, func_type):
        if node is None:
            return
        if isinstance(node, IfStatementNode):
            for child in node.body[0].children:
                self.check_returns(child, func_type)

        elif isinstance(node, WhileLoopNode):
            for child in node.body:
                self.check_returns(child, func_type)
        for child in node.children:
            self.check_returns(child, func_type)
        if isinstance(node, ReturnNode):
            if node.return_type != func_type:
                self.errors.append(f"line {node.line}:{node.column} Return type does not match function type!")

    def checkArraySizes(self, array: ArrayNode, sizes: list):
        if not isinstance(array, ArrayNode):
            return False

        if len(array.array) != sizes[0]:
            return False

        for element in array.array:
            if isinstance(element, ArrayNode):
                if len(sizes) == 0:
                    return False
                if self.checkArraySizes(element, sizes[1:]):
                    continue
                else:
                    return False

        return True

    def checkArrayTypes(self, array: ArrayNode, type_node: TypeNode):
        type = self.get_highest_type(type_node)

        for element in array.array:
            if isinstance(element, ArrayNode):
                if not self.checkArrayTypes(element, type_node):
                    return False
            else:
                if type != self.get_highest_type(element):
                    return False

        return True

    def visitProgram(self, ctx):
        children = []
        for line in ctx.getChildren():
            node = self.visit(line)
            if node is not None:
                if isinstance(node, list):
                    children.extend(node)
                else:
                    children.append(node)

        self.remove_unused_children(children)

        self.node = ProgramNode(line=ctx.start.line, column=ctx.start.column, original=None, children=children)
        self.check_validity(self.node)
        return self

    def visitFunction(self, ctx):
        children = []
        return_type = None
        if ctx.getChild(0).getText() == "void":
            return_type = TypeNode(value="void", line=ctx.start.line, column=ctx.start.column, original="void")
        else:
            return_type = self.visit(ctx.getChild(0))
        name = ctx.getChild(1).getText()
        if isinstance(return_type, TypeNode):
            original = f"{return_type.value} {name}("
        else:
            original = ''
            for ret_type in return_type:
                original += f"{ret_type.original} "
            original += f"{name}("
        defined = ctx.getChild(ctx.getChildCount() - 1).getText() != ";"
        const = isinstance(return_type.type, list) if isinstance(return_type, PointerNode) else isinstance(return_type, list)
        params = [] if ctx.getChild(3).getText() == ")" else self.visit(ctx.getChild(3))
        # Reorder params.
        new_params = []
        if len(params) != 0:
            while isinstance(params, list):
                left = params[0]
                right = params[1]
                if isinstance(right, list):
                    param_name = right[1]
                    param_type = right[0]
                else:
                    param_name = right
                    param_type = left
                new_params.insert(0, [param_type, param_name])
                params = left
        params = new_params

        symbol = Symbol(name=name, var_type=return_type, symbol_type='function', defined=defined, const=const, params=params)
        # Check if function exists already.
        symbols = self.scope.get_symbol(name=name) if self.scope.get_symbol(name=name) is not None else []
        if isinstance(symbols, Symbol):
            symbols = [symbols]
        if len(symbols) != 0:
            for symb in symbols:
                if symb.symbol_type != 'function':
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} {name} already declared as {symb.symbol_type}")
                    return None
                elif not symb.defined:
                    continue
                elif len(symbol.params) == len(symb.params):
                    if matching_params(symb.params, params):
                        if symb.defined == symbol.defined:
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} {name} has already been defined")
                            return None
        self.scope.add_symbol(symbol)
        # Add parameters to function scope, before scope is opened.
        # Open a new scope and lock opening a scope for 1x open scope. visiting the scope part of this function will close it.
        # (Only needed if there are params)
        if ctx.getChild(ctx.getChildCount() - 1).getText() != ";":
            self.scope.open_scope()
            self.scope.lock_scope()
        # Add params
        for param in params:
            param_type = param[0]
            param_name = param[1]
            const = False
            if params.index(param) == 0:
                original += f"{param_type.original} {param_name.original}"
            else:
                original += f", {param_type.original} {param_name.original}"
            # Get name
            if isinstance(param_name, IdentifierNode):
                param_name = param_name.value
            elif isinstance(param_name, AddrNode):
                param_name = param_name.value.value
            # Get type
            if isinstance(param_type, PointerNode):
                param_type = param_type.type
            if isinstance(param_type, list):
                const = True
                param_type = param_type[len(param_type) - 1]
            param_type = param_type.value
            symbol = Symbol(name=param_name, var_type=param_type, const=const, symbol_type='variable', defined=True, params=None)
            symbols = self.scope.get_symbol(name=param_name)
            if not symbols:
                self.scope.add_symbol(symbol)
            else:
                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} parameter {param_name} already exists!")
        if isinstance(return_type, TypeNode) and return_type.value == 'int' and name == 'main' and len(params) == 0:
            self.has_main = True
        body = [] if ctx.getChild(ctx.getChildCount() - 1).getText() == ";" else self.visit(ctx.getChild(ctx.getChildCount() - 1))
        body = body.children if isinstance(body, ScopeNode) else body
        original += ")" if body != [] else ") {}"
        node = FunctionNode(value=name, line=ctx.start.line, column=ctx.start.column, original=original, return_type=return_type, params=params, body=body, children=children)
        # Return nodes are valid in function.
        self.set_valid(node, ReturnNode)
        # Check if return types match function type.
        for child in body:
            self.check_returns(child, return_type.value)
        # Close scope after function body.
        if ctx.getChild(ctx.getChildCount() - 1).getText() != ";":
            self.scope.close_scope(ignore=False)
        return node

    def visitFunctionParams(self, ctx):
        children = []
        for line in ctx.getChildren():
            child = self.visit(line)
            if child is not None:
                if isinstance(child, list) and len(child) == 1:
                    child = child[0]
                children.append(child)
        return children

    def visitFunctionCall(self, ctx):
        name = ctx.getChild(0).getText()
        args = self.visit(ctx.getChild(2)) if ctx.getChildCount() == 4 else []
        if not isinstance(args, list):
            args = [args] if args is not None else []
        # reorder arguments
        new_args = []
        if len(args) != 0:
            while isinstance(args, list):
                if len(args) == 1:
                    args = args[0]
                    break
                new_args.insert(0, args[1])
                args = args[0]
            new_args.insert(0, args)
        args = new_args
        original = f"{name}()"
        # Check if function with name and param types exists.
        symbols = self.scope.lookup(name=name) if self.scope.lookup(name=name) is not None else []
        if isinstance(symbols, Symbol):
            symbols = [symbols]
        found = False
        for symbol in symbols:
            similar = True
            params = symbol.params
            if len(args) != len(params):
                continue
            for i in range(0, len(params)):
                type1 = self.get_highest_type(params[i][0])
                type2 = self.get_highest_type(args[i])
                if type1 != type2:
                    similar = False
                    continue
                lval = self.get_pointer_size(params[i][0], by_ref=True)
                rval = self.get_pointer_size(args[i])
                error = False
                if len(lval) != len(rval):
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} function call to function that doesn't exist!")
                else:
                    for i in range(0, len(lval)):
                        if lval[i] != rval[i]:
                            if not error:
                                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} function call to function that doesn't exist!")
                                error = True
            if similar:
                found = True
        if not found:
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} function call to function that doesn't exist!")
        return FunctionCallNode(value=name, line=ctx.start.line, column=ctx.start.column, original=original, arguments=args)

    def visitCallParams(self, ctx):
        children = []
        for line in ctx.getChildren():
            child = self.visit(line)
            if child is not None:
                if isinstance(child, list) and len(child) == 1:
                    child = child[0]
                children.append(child)
        return children

    def visitScope(self, ctx):
        self.scope.open_scope()
        children = []
        stop = False
        for line in ctx.getChildren():
            if stop:
                break
            if line.getChildCount() == 2:
                if isinstance(line.getChild(0), Parser.RvalueContext):
                    if isinstance(line.getChild(0).getChild(0), Parser.JumpStatementContext):
                        stop = True
            node = self.visit(line)
            if node is not None:
                if isinstance(node, list):
                    children.extend(node)
                else:
                    children.append(node)

        self.remove_unused_children(children)

        self.scope.close_scope()
        node = ScopeNode(line=ctx.start.line, column=ctx.start.column, original="", children=children)
        return node

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
                    if child is None:
                        return None
                    if isinstance(child, IdentifierNode):
                        if self.scope.lookup(child.value) is None:
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + child.value + "\' not declared yet!")
                        else:
                            if self.scope.lookup(child.value).symbol_type == 'typeDef':
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
                    for item in child:
                        if isinstance(item, TypeNode):
                            if item.value != 'const':
                                item.value = self.get_highest_type(item)
                        children.append(item)
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
                if isinstance(children[len(children) - 2].type, list):
                    var_type = children[len(children) - 2].type[len(children[len(children) - 2].type) - 1].value
                else:
                    var_type = children[len(children) - 2].type.value

            const = len(children) > 2

            if isinstance(children[len(children) - 2], PointerNode):
                var_type = children[len(children) - 2]
                const = isinstance(children[0].type, list)

            # Check if variable already declared in current scope.
            if self.scope.get_symbol(identifier) is not None or identifier in self.scope.get_enum_values():
                if identifier in self.scope.get_all_enum_values():
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' already declared!")
                    return None
                if self.scope.get_symbol(identifier).symbol_type == 'typeDef':
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} \'" + identifier + "\' is declared as type!")
                    return None
                if self.scope.get_symbol(identifier).symbol_type == 'function':
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} \'" + identifier + "\' is declared as function!")
                    return None
                if not self.scope.is_global():
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' already declared!")
                    return None


            symbol = Symbol(name=identifier, var_type=var_type, const=const, symbol_type='variable')
            if self.scope.is_global():
                symbol.defined = False
            if self.scope.get_symbol(name=symbol.name) is None:
                self.scope.add_symbol(symbol=symbol)
            node = DeclarationNode(line=ctx.start.line, column=ctx.start.column, original=original, type=children[:len(children) - 1], lvalue=children[len(children) - 1])
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
                if self.scope.lookup(identifier).defined and self.scope.is_global():
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' already declared!")
                    return None
                lval = self.scope.lookup(identifier)
                if isinstance(children[0], DerefNode):
                    if not isinstance(self.scope.lookup(lval.name).type, PointerNode):
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Cannot dereference non-pointer type!")
                        return None
                if lval.symbol_type == 'enum':
                    enum_type = lval.type
                    if isinstance(node, IdentifierNode):
                        value = node.value
                        if value not in self.scope.get_enum_values_of_enum(enum_type):
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Enum value \'" + value + "\' not declared!")
                            return None

                        # get index of value in enum
                        index = self.scope.get_enum_values_of_enum(enum_type).index(value)
                        rval_node = IntNode(line=ctx.start.line, column=ctx.start.column, original=original, value=index)

                        node = AssignmentNode(line=ctx.start.line, column=ctx.start.column, original=original, lvalue=children[0], rvalue=rval_node)
                        return node
                    else:
                        if isinstance(node, IntNode):
                            if int(node.value) >= len(self.scope.get_enum_values_of_enum(enum_type.original)):
                                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Enum value \'" + str(node.value) + "\' not declared!")
                                return None
                        else:
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Enum value \'" + str(node.value) + "\' not declared!")
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
                        if isinstance(children[0], DerefNode):
                            lval_ptr = str(int(lval_ptr) - int(children[0].value))
                    if len(rval_ptr) > 1:
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Invalid operands!")
                        return None
                    if len(rval_ptr):
                        if int(rval_ptr[0]) != int(lval_ptr):
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Pointer type mismatch!")
                            return None
                    if lval.symbol_type == 'array':
                        return self.visitArrayAssignmentFromCTX(ctx=ctx)
                    self.scope.lookup(identifier).defined = True
                    node = AssignmentNode(line=ctx.start.line, column=ctx.start.column, original=original, lvalue=children[0], rvalue=children[2])
                    return node
            else:
                # "=" is not second character -> definition.
                identifier = children[children.index('=') - 1].value
                var_type = children[children.index('=') - 2].value

                if isinstance(children[children.index('=') - 2], PointerNode):
                    if isinstance(children[children.index('=') - 2].type, list):
                        var_type = children[children.index('=') - 2].type[len(children[children.index('=') - 2].type) - 1].value
                    else:
                        var_type = children[children.index('=') - 2].type.value

                # Check if type is declared.
                if var_type not in self.types:
                    if self.scope.lookup(var_type) is None:
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Type \'" + var_type + "\' not declared yet!")
                        return None
                    elif not self.scope.lookup(var_type).symbol_type == 'typeDef':
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} \'" + var_type + "\' not declared as type!")
                        return None
                if self.scope.get_symbol(identifier) is not None or identifier in self.scope.get_enum_values():
                    if identifier in self.scope.get_all_enum_values():
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' already declared!")
                        return None
                    if self.scope.get_symbol(identifier).symbol_type == 'typeDef':
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} \'" + identifier + "\' is declared as type!")
                        return None
                    if self.scope.get_symbol(identifier).symbol_type == 'function':
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} \'" + identifier + "\' is declared as function!")
                        return None
                    if self.scope.is_global() and self.scope.get_symbol(identifier).defined:
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' already declared!")
                        return None
                    if not self.scope.is_global():
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' already declared!")
                        return None
                var_type = children[children.index("=") - 2].value
                const = len(children) > 4
                if isinstance(children[children.index("=") - 2], PointerNode):
                    var_type = children[children.index("=") - 2]
                    const = isinstance(var_type.type, list)
                symbol = Symbol(name=identifier, var_type=var_type, const=const, symbol_type='variable')
                lval = symbol
                rval = children[len(children) - 1]
                # Give warnings for implicit conversions.
                rval = node
                if isinstance(rval, StringNode):
                    if not isinstance(lval.type, PointerNode):
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Cannot assign string to non-char-pointer type!")
                        return None
                    if lval.type.type.value != "char" or int(lval.type.value) != 1:
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Cannot assign string to non-char-pointer type!")
                        return None
                elif isinstance(rval, AddrNode) or isinstance(rval, IdentifierNode):
                    if isinstance(rval, AddrNode):
                        if not self.scope.lookup(rval.value.value):
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + rval.value.value + "\' not declared yet!")
                            return None
                    else:
                        if not self.scope.lookup(rval.value):
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + rval.value + "\' not declared yet!")
                            return None
                        rvalType = self.scope.lookup(rval.value).type
                elif isinstance(rval, DerefNode):
                    if not self.scope.lookup(rval.identifier.value):
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + rval.identifier.value + "\' not declared yet!")
                        return None
                    rvalType = self.scope.lookup(rval.identifier.value).type
                    if not isinstance(rvalType, PointerNode):
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Cannot dereference non-pointer type!")
                        return None
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
                if self.scope.get_symbol(symbol.name) is None:
                    self.scope.add_symbol(symbol=symbol)
                else:
                    self.scope.get_symbol(symbol.name).defined = True
                self.implicit_type_conversion(var_type, rval)

                # if rvalue is a string
                if isinstance(rval, StringNode):
                    node = ArrayDefinitionNode(line=ctx.start.line, column=ctx.start.column, original=original, type=var_type, lvalue=children[len(children) - 3], rvalue=rval, size=[len(rval.value)])
                    return node
                node = DefinitionNode(line=ctx.start.line, column=ctx.start.column, original=original, type=children[:len(children) - 3], lvalue=children[children.index("=") - 1], rvalue=children[children.index("=") + 1])
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
        node = IdentifierNode(value=ctx.getText(), line=ctx.start.line, column=ctx.start.column, original=ctx.getText())
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
        condition = None
        original_condition = None
        original = None
        for child in children:
            if isinstance(child, IfStatementNode):
                condition = child.condition
                original_condition = condition
                condition.original = f"({condition.original})"
            elif isinstance(child, ElseIfStatementNode):
                original = f"(! {condition.original})"
                new_condition = LogicalNotNode(line=child.line, column=child.column, original=original, children=[condition])
                original = f"({new_condition.original} && {child.original})"
                new_condition = LogicalAndNode(line=child.line, column=child.column, original=original, children=[new_condition, child.condition])
                original = f"({condition.original} || {child.condition.original})"
                condition = LogicalOrNode(line=child.line, column=child.column, original=original, children=[condition, child.condition])
                child.condition = new_condition
                child.__class__ = IfStatementNode
            elif isinstance(child, ElseStatementNode):
                original = f"(! {condition.original})"
                condition = LogicalNotNode(line=child.line, column=child.column, original=original, children=[condition])
                child.__class__ = IfStatementNode
                child.condition = condition
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
        node = IfStatementNode(line=ctx.start.line, column=ctx.start.column, original=original, condition=children[0], body=children[1:])
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
        original = f"else if({children[0].original})" + "{}"
        node = ElseIfStatementNode(line=ctx.start.line, column=ctx.start.column, original=original, condition=children[0], body=children[1:])
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
        node = ElseStatementNode(line=ctx.start.line, column=ctx.start.column, original=original, body=children)
        return node

    def visitComment(self, ctx):
        node = CommentNode(ctx.getText(), line=ctx.start.line, column=ctx.start.column, original=ctx.getText())
        return node

    def visitPostFixDecrement(self, ctx):
        variable = self.visit(ctx.getChild(0))[0]
        if isinstance(variable, IdentifierNode):
            identifier = variable.value
        elif isinstance(variable, DerefNode):
            identifier = variable.identifier.value
        elif isinstance(variable, ArrayIdentifierNode):
            identifier = variable.value
        if not self.scope.lookup(identifier):
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' not declared yet!")
        original = f"{identifier}--"
        node = PostFixNode(value=variable, line=ctx.start.line, column=ctx.start.column, original=original, op='dec')
        return node

    def visitPostFixIncrement(self, ctx):
        variable = self.visit(ctx.getChild(0))[0]
        if isinstance(variable, IdentifierNode):
            identifier = variable.value
        elif isinstance(variable, DerefNode):
            identifier = variable.identifier.value
        elif isinstance(variable, ArrayIdentifierNode):
            identifier = variable.value
        if not self.scope.lookup(identifier):
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' not declared yet!")
        original = f"{identifier}++"
        node = PostFixNode(value=variable, line=ctx.start.line, column=ctx.start.column, original=original, op='inc')
        return node

    def visitPreFixDecrement(self, ctx):
        variable = self.visit(ctx.getChild(1))[0]
        if isinstance(variable, IdentifierNode):
            identifier = variable.value
        elif isinstance(variable, DerefNode):
            identifier = variable.identifier.value
        elif isinstance(variable, ArrayIdentifierNode):
            identifier = variable.value
        if not self.scope.lookup(identifier):
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' not declared yet!")
        original = f"--{identifier}"
        node = PreFixNode(value=variable, line=ctx.start.line, column=ctx.start.column, original=original, op='dec')
        return node

    def visitPreFixIncrement(self, ctx):
        variable = self.visit(ctx.getChild(1))[0]
        if isinstance(variable, IdentifierNode):
            identifier = variable.value
        elif isinstance(variable, DerefNode):
            identifier = variable.identifier.value
        elif isinstance(variable, ArrayIdentifierNode):
            identifier = variable.value
        if not self.scope.lookup(identifier):
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' not declared yet!")
        original = f"++{identifier}"
        node = PreFixNode(value=variable, line=ctx.start.line, column=ctx.start.column, original=original, op='inc')
        return node

    def visitAddr(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)
        identifier = self.visit(children[1])
        original = f"&{identifier.original}"
        node = AddrNode(value=identifier, line=ctx.start.line, column=ctx.start.column, original=original)
        return node

    def visitPointer(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)
        original = ""
        types = self.visit(children[0])
        if not isinstance(types, list):
            types = [types]
        for type in types:
            original += f"{type.original} "
        original += "*" * (len(children) - 1)
        type = types[0] if len(types) == 1 else types
        node = PointerNode(value=len(children) - 1, line=ctx.start.line, column=ctx.start.column, original=original, type=type)
        return node

    def visitDeref(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)
        identifier = self.visit(children[len(children) - 1])
        if self.scope.lookup(identifier.value) is None:
            self.errors.append("Variable \'" + identifier.value + "\' not declared yet!")
        original = "*" * (len(children) - 1)
        original += f"{identifier.original}"
        node = DerefNode(value=len(children) - 1, line=ctx.start.line, column=ctx.start.column, original=original, identifier=identifier)
        return node

    def visitType(self, ctx):
        types = []
        for type in ctx.getChildren():
            types.append(TypeNode(value=type.getText(), line=ctx.start.line, column=ctx.start.column, original=type.getText()))
        return types if len(types) != 1 else types[0]

    def visitRvalue(self, ctx):
        lines = []
        for line in ctx.getChildren():
            lines.append(line)
        original = ""
        if len(lines) == 4:
            node = self.visit(lines[2])

            if isinstance(node, IntNode) or isinstance(node, CharNode):
                if lines[0].getText() == "-":
                    node.value = - int(node.value)
            elif isinstance(node, FloatNode):
                if lines[0].getText() == "-":
                    node.value = - float(node.value)
            else :
                if lines[0].getText() == "-":
                    node.value = "-" + node.value


            node.original = f"{lines[0].getText} ({node.original})"

        if len(lines) == 3:
            node = ProgramNode(line=0, column=0, original=None)
            if str(lines[0]) == "(" and ")" == str(lines[2]):
                node = self.visit(lines[1])
                node.original = f"({node.original})"
                return node
            original = f"{lines[0].getText()} {lines[1].getText()} {lines[2].getText()}"
            child0 = self.visit(lines[0])
            child2 = self.visit(lines[2])
            if isinstance(child0, IdentifierNode):
                if self.scope.lookup(child0.value) is None:
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + child0.value + "\' not declared yet!")
                    return node
                if self.scope.lookup(child0.value).symbol_type not in ['variable', 'enum']:
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + child0.value + "\' not declared yet!")
                    return node
            if isinstance(child2, IdentifierNode):
                if self.scope.lookup(child2.value) is None:
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + child2.value + "\' not declared yet!")
                    return node
                if self.scope.lookup(child2.value).symbol_type != 'variable' and self.scope.lookup(child2.value).symbol_type != 'enum':
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + child2.value + "\' not declared yet!")
                    return node
            match str(lines[1]):
                case "/":
                    if not isinstance(self.visit(lines[2]).value, str) and int(self.visit(lines[2]).value) == 0:
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Division by zero!")
                    node = DivNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[child0, child2])
                case "%":
                    type0 = self.get_highest_type(child0)
                    type2 = self.get_highest_type(child2)
                    if type0 == 'float' or type2 == 'float':
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Invalid operands!")
                    node = ModNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[child0, child2])
                case "*":
                    node = MultNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[child0, child2])
                case "-":
                    node = MinusNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[child0, child2])
                case "+":
                    node = PlusNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[child0, child2])
                case "<<":
                    type0 = self.get_highest_type(child0)
                    type2 = self.get_highest_type(child2)
                    if type0 == 'float' or type2 == 'float':
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Invalid operands!")
                    node = SLNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[child0, child2])
                case ">>":
                    type0 = self.get_highest_type(child0)
                    type2 = self.get_highest_type(child2)
                    if type0 == 'float' or type2 == 'float':
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Invalid operands!")
                    node = SRNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[child0, child2])
                case "&":
                    type0 = self.get_highest_type(child0)
                    type2 = self.get_highest_type(child2)
                    if type0 == 'float' or type2 == 'float':
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Invalid operands!")
                    node = BitwiseAndNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[child0, child2])
                case "|":
                    type0 = self.get_highest_type(child0)
                    type2 = self.get_highest_type(child2)
                    if type0 == 'float' or type2 == 'float':
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Invalid operands!")
                    node = BitwiseOrNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[child0, child2])
                case "^":
                    type0 = self.get_highest_type(child0)
                    type2 = self.get_highest_type(child2)
                    if type0 == 'float' or type2 == 'float':
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Invalid operands!")
                    node = BitwiseXorNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[child0, child2])
                case "&&":
                    node = LogicalAndNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[child0, child2])
                case "||":
                    node = LogicalOrNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[child0, child2])
                case ">":
                    node = GTNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[child0, child2])
                case "<":
                    node = LTNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[child0, child2])
                case "==":
                    node = EQNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[child0, child2])
                case ">=":
                    node = GTEQNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[child0, child2])
                case "<=":
                    node = LTEQNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[child0, child2])
                case "!=":
                    node = NEQNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[child0, child2])
            if isinstance(node.children[0], IdentifierNode):
                identifier = node.children[0].value
                if self.scope.lookup(identifier) is None:
                    if identifier not in self.scope.get_all_enum_values():
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' not declared yet!")
                        return node
                    else:
                        node.children[0] = IntNode(value=self.scope.get_index_of_enum_value(identifier), line=ctx.start.line, column=ctx.start.column, original=identifier)
                        return node
                if self.scope.lookup(identifier).symbol_type == 'typeDef':
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} \'" + identifier + "\' is declared as type!")
                    return node
            if isinstance(node.children[1], IdentifierNode):
                identifier = node.children[1].value
                if self.scope.lookup(identifier) is None:
                    if identifier not in self.scope.get_all_enum_values():
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' not declared yet!")
                        return node
                    else:
                        node.children[1] = IntNode(value=self.scope.get_index_of_enum_value(identifier), line=ctx.start.line, column=ctx.start.column, original=identifier)
                        return node
                if self.scope.lookup(identifier).symbol_type == 'typeDef':
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} \'" + identifier + "\' is declared as type!")
                    return node
            return node
        if len(lines) == 2:
            original = f"{lines[0].getText()} {lines[1].getText()}"
            child0 = self.visit(lines[1])
            if isinstance(child0, IdentifierNode):
                if self.scope.lookup(child0.value) is None:
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + child0.value + "\' not declared yet!")
                    return child0
                if self.scope.lookup(child0.value).symbol_type != 'variable':
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + child0.value + "\' not declared yet!")
                    return child0
            if str(lines[0]) == "!":
                node = LogicalNotNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[child0])
            elif str(lines[0]) == "~":
                node = BitwiseNotNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[child0])
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
                if self.scope.lookup(identifier).symbol_type == 'typeDef':
                    self.errors.append(
                        f"line {ctx.start.line}:{ctx.start.column} \'" + identifier + "\' is declared as type!")
                    return node
            return node
        if len(lines) == 1:
            node = self.visit(lines[0])
            negatives = 0
            original = ""
            for child in lines[0].children:
                if child.getText() == "-" or child.getText() == "+":
                    original += f"{child.getText()}"
                if child.getText() == "-":
                    negatives += 1
            node.original = f"{original}{node.original}"
            if negatives % 2:
                if isinstance(node, DerefNode):
                    node.identifier.value = f"-{node.identifier.value}"
                else:
                    node.value = f"-{node.value}"
        if isinstance(node, IdentifierNode):
            if self.scope.get_index_of_enum_value(node.value) is not None:
                node = IntNode(value=self.scope.get_index_of_enum_value(node.value), line=ctx.start.line, column=ctx.start.column, original=node.value)
        return node

    def visitConditionalExpression(self, ctx):
        children = []
        node = ProgramNode(line=0, column=0, original=None)
        for line in ctx.getChildren():
            children.append(line)
        original = f"{children[0].getText()} {self.visit(children[1]).original}"
        match children[0].getText():
            case ">":
                node = GTNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[self.visit(children[1]), self.visit(children[1])])
            case "<":
                node = LTNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[self.visit(children[1]), self.visit(children[1])])
            case "==":
                node = EQNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[self.visit(children[1]), self.visit(children[1])])
            case ">=":
                node = GTEQNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[self.visit(children[1]), self.visit(children[1])])
            case "<=":
                node = LTEQNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[self.visit(children[1]), self.visit(children[1])])
            case "!=":
                node = NEQNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[self.visit(children[1]), self.visit(children[1])])
        return node

    def visitLiteral(self, ctx):
        literal = ctx.getText()
        node = ProgramNode(line=0, column=0, original=None)
        if literal.startswith("\'"):
            literal = literal.strip("\'")
            node = CharNode(value=str(ord(literal)), line=ctx.start.line, column=ctx.start.column, original=literal)
        elif '.' in literal:
            node = FloatNode(value=ctx.getText(), line=ctx.start.line, column=ctx.start.column, original=ctx.getText())
        elif literal.isdigit():
            node = IntNode(value=ctx.getText(), line=ctx.start.line, column=ctx.start.column, original=ctx.getText())
        return node

    def visitString(self, ctx):
        node = StringNode(value=ctx.getText(), line=ctx.start.line, column=ctx.start.column, original=ctx.getText())
        return node

    def visitChar(self, ctx):
        node = CharNode(value=ord(ctx.getText().strip("\'")), line=ctx.start.line, column=ctx.start.column, original=ctx.getText())
        return node

    def visitExplicitConversion(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)
        type = children[1].getText()
        original = f"({type}) {children[len(children) - 1].getText()}"
        typeNode = TypeNode(value=type, line=ctx.start.line, column=ctx.start.column, original=type)
        type = self.get_highest_type(typeNode)

        rval = self.visit(children[len(children) - 1])
        if isinstance(rval, IdentifierNode):
            self.scope.lookup(rval.value)

        node = ExplicitConversionNode(line=ctx.start.line, column=ctx.start.column, original=original, type=type, rvalue=rval)
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
        original = f"printf({children[0].original}"
        for i in range(1, len(children)):
            original += f", {children[i].original}"
        original += ")"
        # Count amount of specifiers
        specifiers = 0
        children[0].specifier = children[0].specifier.replace('\"', '')
        copy_specifier = children[0].specifier
        i = 0
        while i < len(copy_specifier):
            if i == len(copy_specifier):
                break
            if copy_specifier[i] == '%':
                if len(copy_specifier) - 1 == i:
                    copy_specifier = copy_specifier[:i] + copy_specifier[i + 1:]
                    continue
                char = copy_specifier[i + 1]
                if char == 'd' or char == 'x' or char == 's' or char == 'f' or char == 'c' or char == '%':
                    specifiers += 1
                    if char == '%':
                        specifiers -= 1
                        i += 2
                        continue
                    if specifiers > len(children) - 1:
                        self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Too few arguments for format string!")
                        return None
                    if isinstance(children[specifiers], StructMemberNode):
                        format_type = self.get_highest_type(children[specifiers].type)
                    else:
                        format_type = self.get_highest_type(children[specifiers])
                    if format_type is None:
                        if isinstance(children[specifiers], IdentifierNode):
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + children[specifiers].value + "\' not declared yet!")
                        else:
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + children[specifiers].identifier.value + "\' not declared yet!")
                        return None
                    if char == 'd' and format_type != 'int':
                        self.warnings.append(f"line {ctx.start.line}:{ctx.start.column} use of %{char} but got {format_type}")
                    if char == 'x' and format_type != 'int':
                        self.warnings.append(f"line {ctx.start.line}:{ctx.start.column} use of %{char} but got {format_type}")
                    elif char == 's' and format_type != 'string':
                        self.warnings.append(f"line {ctx.start.line}:{ctx.start.column} use of %s but got {format_type}")
                    elif char == 'f' and format_type != 'float':
                        self.warnings.append(f"line {ctx.start.line}:{ctx.start.column} use of %f but got {format_type}")
                    elif char == 'c' and format_type != 'char':
                        self.warnings.append(f"line {ctx.start.line}:{ctx.start.column} use of %c but got {format_type}")
                else:
                    copy_specifier = copy_specifier[:i] + copy_specifier[i + 1:]
                    continue
            i += 1
        children[0].specifier = copy_specifier
        if specifiers < len(children) - 1:
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Too many arguments for format string!")
            return None
        original = f"printf(\"{children[0].specifier}\""
        for i in range(1, len(children)):
            original += f", {children[i].original}"
        original += ")"
        node = PrintfNode(line=ctx.start.line, column=ctx.start.column, original=original, specifier=children[0].specifier, children=children[1:])
        if len(children) == 1:
            return node
        if isinstance(children[1], IdentifierNode) or isinstance(children[1], DerefNode):
            identifier = ''
            if isinstance(children[1], IdentifierNode):
                identifier = children[1].value
            else:
                identifier = children[1].identifier.value
            if self.scope.lookup(identifier) is None:
                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' not declared yet!")
                return ProgramNode(line=0, column=0, original=None)
            if self.scope.lookup(identifier).symbol_type == 'typeDef':
                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} \'" + identifier + "\' is declared as type!")
                return ProgramNode(line=0, column=0, original=None)
        return node

    def visitFormatSpecifier(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)
        original = f"{children[0].getText()}"
        return FormatSpecifierNode(line=ctx.start.line, column=ctx.start.column, original=original, specifier=children[0].getText())

    def visitTypedef(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)

        name = children[2].getText()
        type = children[1].getText()

        if self.scope.get_symbol(name) is not None:
            if self.scope.get_symbol(name).symbol_type == 'variable':
                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} \'" + name + "\' is declared a variable!")
                return None
            if self.scope.get_symbol(name).symbol_type == 'function':
                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} \'" + name + "\' is declared a function!")
                return None

        self.scope.add_symbol(Symbol(name=name, var_type=type, symbol_type='typeDef', const=False))
        original = f"typedef {children[1].getText()} {children[2].getText()}"
        return TypedefNode(line=ctx.start.line, column=ctx.start.column, original=original, type=children[1].getText(), identifier=children[2].getText())

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
        whilenode = WhileLoopNode(line=ctx.start.line, column=ctx.start.column, original=original, condition=children[0], body=children[1:])
        node = ScopeNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[whilenode])
        # Continue and break are valid.
        self.set_valid(whilenode, BreakNode)
        self.set_valid(whilenode, ContinueNode)
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
        original = ""
        condition = IntNode('1', line=ctx.start.line, column=ctx.start.column, original='1')
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

        whilenode = WhileLoopNode(line=ctx.start.line, column=ctx.start.column, original=original, condition=condition, body=body)
        node = ScopeNode(line=ctx.start.line, column=ctx.start.column, original=original, children=[whilenode])
        # Continue and break are valid.
        self.set_valid(node, BreakNode)
        self.set_valid(node, ContinueNode)
        if children[2] is not None:
            for child in node.children[0].body:
                self.place_node_before_type(child, children[2], BreakNode)
                self.place_node_before_type(child, children[2], ReturnNode)
                self.place_node_before_type(child, children[2], ContinueNode)
            if not isinstance(node.children[0].body[len(node.children[0].body) - 1], BreakNode) and not isinstance(node.children[0].body[len(node.children[0].body) - 1], ReturnNode) and not isinstance(node.children[0].body[len(node.children[0].body) - 1], ContinueNode):
                node.children[0].body.append(children[2])
            else:
                node.children[0].body.insert(len(node.children[0].body) - 1, children[2])
        self.scope.close_scope()
        return node if children[0] is None else [ScopeNode(line=ctx.start.line, column=ctx.start.column, original=original, children = [children[0], node])]

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
        name = ctx.getChild(0).getText()
        match name:
            case 'break':
                return BreakNode(line=ctx.start.line, column=ctx.start.column, original="break")
            case 'continue':
                return ContinueNode(line=ctx.start.line, column=ctx.start.column, original="continue")
            case 'return':
                original = "return"
                ret_val = None
                if ctx.getChildCount() == 2:
                    ret_val = self.visit(ctx.getChild(1))
                    original += f" {expandExpression(ret_val)}"
                node = ReturnNode(line=ctx.start.line, column=ctx.start.column, original=original, ret_val=ret_val)
                node.return_type = self.get_highest_type(node.return_value)
                if node.return_value is None:
                    node.return_type = 'void'
                return node

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

        if isinstance(rval, IdentifierNode):
            symbol = self.scope.lookup(rval.value)
            if symbol is None:
                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + rval.value + "\' not declared yet!")

        elif isinstance(rval, DerefNode):
            symbol = self.scope.lookup(rval.identifier.value)
            if symbol is None:
                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + rval.identifier.value + "\' not declared yet!")

        elif isinstance(rval, ArrayIdentifierNode):
            symbol = self.scope.lookup(rval.value)
            if symbol is None:
                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + rval.value + "\' not declared yet!")

        elif isinstance(rval, (StructDefinitionNode, StructMemberNode)):
            symbol = self.scope.lookup(rval.lvalue.value)
            if symbol is None:
                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + rval.identifier.value + "\' not declared yet!")

        elif isinstance(rval, FunctionCallNode):
            symbol = self.scope.lookup(rval.value)
            if symbol is None:
                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + rval.identifier.value + "\' not declared yet!")

        elif isinstance(rval, AddrNode):
            symbol = self.scope.lookup(rval.value.value)
            if symbol is None:
                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + rval.value.value + "\' not declared yet!")

        else:
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Invalid switch statement!")


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
                            self.errors.append(f"line {case1.line}:{case1.column} Duplicate cases in switch statement!")
        # Make if statements
        if len(cases) == 0:
            return None
        not_default_condition = None
        condition_since_break = None
        for case in cases:
            original = ""
            if case.condition == 'Default':
                if not_default_condition is not None:
                    original = f"(! {not_default_condition.original})"
                    not_default_condition = LogicalNotNode(case.line, case.column, original=original, children=[not_default_condition])
                    if condition_since_break is not None:
                        not_default_condition = LogicalOrNode(line=case.line, column=case.column, original=f"({condition_since_break.original} || {not_default_condition.original})", children=[condition_since_break, not_default_condition])
                    original = f"default:"
                ifNode = IfStatementNode(line=case.line, column=case.column, original=original, condition=not_default_condition, body=case.children)
                ifNodes.append(ifNode)
            else:
                if condition_since_break is None:
                    original = f"({rval.original} == {case.condition.original})"
                    condition_since_break = EQNode(line=case.line, column=case.column, original=original, children=[rval, case.condition])
                    original = f"case {case.condition.original}:"
                else:
                    original = f"({rval.original} == {case.condition.original})"
                    case_condition = EQNode(line=case.line, column=case.column, original=original, children=[rval, case.condition])
                    original = f"({condition_since_break.original} || {case_condition.original})"
                    condition_since_break = LogicalOrNode(line=case.line, column=case.column, original=original, children=[condition_since_break, case_condition])
                    original = f"case {case.condition.original}:"
                if not_default_condition is None:
                    original = f"({rval.original} == {case.condition.original})"
                    not_default_condition = EQNode(line=case.line, column=case.column, original=original, children=[rval, case.condition])
                else:
                    original = f"({rval.original} == {case.condition.original})"
                    new_condition = EQNode(line=case.line, column=case.column, original=original, children=[rval, case.condition])
                    original = f"({not_default_condition.original} || {original})"
                    not_default_condition = LogicalOrNode(line=case.line, column=case.column, original=original, children=[not_default_condition, new_condition])
                ifNodes.append(IfStatementNode(line=case.line, column=case.column, original=original, condition=condition_since_break, body=case.children))
                for child in case.children:
                    # If break found, set condition to case condition.
                    if self.contains_node(child, BreakNode):
                        condition_since_break = None
                        break

        # Remove breaks
        for case in cases:
            self.remove_type(case, BreakNode)
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
                            self.errors.append(f"line {item.line}:{item.column} Cannot declare variable in switch case!")
                        else:
                            children.append(item)
                else:
                    if isinstance(child, DeclarationNode) or isinstance(child, DefinitionNode):
                        self.scope.remove_symbol(child)
                        self.errors.append(f"line {child.line}:{child.column} Cannot declare variable in switch case!")
                    else:
                        children.append(child)
        original = ""
        if len(children) == 0:
            original = "default:"
            return CaseNode(line=ctx.start.line, column=ctx.start.column, original=original, condition="Default")
        if isinstance(children[0], CharNode) or isinstance(children[0], IntNode) or isinstance(children[0], FloatNode):
            original = f"case {children[0]}:"
            return CaseNode(line=ctx.start.line, column=ctx.start.column, original=original, condition=children[0], children=children[1:])
        return CaseNode(line=ctx.start.line, column=ctx.start.column, original=original, condition="Default", children=children)

    def visitEnumDeclaration(self, ctx):
        enum_name = ctx.children[1].getText()
        enum_list = []

        original = f"enum {enum_name} " + "{"
        for i in range(3, len(ctx.children)-1):
            if ctx.children[i].getText() == ",":
                continue
            enum_list.append(ctx.children[i].getText())
            original += f"{ctx.children[i].getText()}, "
        original = original[:-2] + "}"

        # Check if enum value in list is unique
        if len(enum_list) != len(set(enum_list)):
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Enum values must be unique!")
            return None

        for enum_value in enum_list:
            if enum_value in self.scope.get_all_enum_values():
                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Enum value \'{enum_value}\' already declared!")
                return None

        # Check if enum is already declared as symbol
        for enum_value in self.scope.get_all_symbols():
            if enum_value in self.scope.get_all_symbols():
                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Enum value \'{enum_value.name}\' already declared!")
                return None

        self.scope.add_enum(enum_name, enum_list)

        return EnumNode(line=ctx.start.line, pos=ctx.start.column, original=original, enum_name=enum_name, enum_list=enum_list)

    def visitEnumStatement(self, ctx):
        return self.visit(ctx.children[0])

    def visitEnumVariableDeclaration(self, ctx):
        enum_type_name = ctx.children[1].getText()
        enum_var_name = ctx.children[2].getText()

        # Check if enum type is declared
        if enum_type_name not in self.scope.get_all_enums():
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Enum type \'{enum_type_name}\' not declared!")
            return None

        # Check if variable is already declared
        if enum_var_name in self.scope.get_all_symbols():
            self.errors.append(
                f"line {ctx.start.line}:{ctx.start.column} Variable \'{enum_var_name}\' already declared!")
            return None

        # Add symbol to scope
        self.scope.add_symbol(Symbol(name=enum_var_name, var_type=TypeNode(value='int', line=ctx.start.line, column=ctx.start.column, original=enum_type_name), symbol_type='enum'))

        # Create definition node
        type = TypeNode(value=enum_type_name, line=ctx.start.line, column=ctx.start.column, original=enum_type_name)
        lvalue = IdentifierNode(value=enum_var_name, line=ctx.start.line, column=ctx.start.column, original=enum_var_name)

        original = f"{enum_type_name} {enum_var_name}"

        return DeclarationNode(line=ctx.start.line, column=ctx.start.column, original=original, type=[type], lvalue=lvalue)

    def visitEnumVariableDefinition(self, ctx):
        enum_type_name = ctx.children[1].getText()
        enum_var_name = ctx.children[2].getText()
        enum_value = ctx.children[4].getText()

        # Check if enum type is declared
        if enum_type_name not in self.scope.get_all_enums():
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Enum type \'{enum_type_name}\' not declared!")
            return None

        # Check if variable is already declared
        if enum_var_name in self.scope.get_all_symbols():
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'{enum_var_name}\' already declared!")
            return None

        # Check if enum value is declared
        if enum_value not in self.scope.get_all_enum_values():
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Enum value \'{enum_value}\' not declared!")
            return None

        # Add symbol to scope
        self.scope.add_symbol(Symbol(name=enum_var_name, var_type=TypeNode(value='int', line=ctx.start.line, column=ctx.start.column, original=enum_type_name), symbol_type='enum'))

        # Create definition node
        type = TypeNode(value=enum_type_name, line=ctx.start.line, column=ctx.start.column, original=enum_type_name)
        lvalue = IdentifierNode(value=enum_var_name, line=ctx.start.line, column=ctx.start.column, original=enum_var_name)

        # get the index of the enum value using get_enum_values
        enum_value_index = self.scope.get_all_enum_values().index(enum_value)

        rvalue = IntNode(value=enum_value_index, line=ctx.start.line, column=ctx.start.column, original=enum_value)

        return DefinitionNode(line=ctx.start.line, column=ctx.start.column, original=ctx.getText(), type=[type], lvalue=lvalue, rvalue=rvalue)

    def visitArrayStatement(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitArrayDeclaration(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)

        typeNode = self.visit(children[0])
        identifier = children[1].getText()

        # Get array sizes
        arraySizes = []
        for child in children[2:]:
            if child.getText() == "[":
                continue
            if child.getText() == "]":
                continue
            node = self.visit(child)
            if not isinstance(node, (IntNode, CharNode)):
                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Invalid array declaration!")
                return None

            arraySizes.append(int(node.value))

        # Add symbol to scope
        if self.scope.get_symbol(identifier):
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' already declared!")
            return None
        self.scope.add_symbol(Symbol(name=identifier, var_type=typeNode, symbol_type='array', arraySizes=arraySizes))

        # Create declaration node
        original = f"{typeNode.original} {identifier}"
        lvalue = IdentifierNode(value=identifier, line=ctx.start.line, column=ctx.start.column, original=original)
        original = f"{typeNode.original} {identifier} ["
        for size in arraySizes:
            original += f"{size}]["
        original = original[:-2] + "]"
        return ArrayDeclarationNode(line=ctx.start.line, column=ctx.start.column, original=original, type=typeNode, lvalue=lvalue, size=arraySizes)

    def visitArrayDefinition(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)

        type_node = self.visit(children[0])
        identifier = children[1].getText()
        rvalue = self.visit(children[-1])

        if isinstance(rvalue, ArrayNode):
            # Get array sizes
            array_sizes = []
            for child in children[2:-2]:
                if child.getText() == "[":
                    continue
                if child.getText() == "]":
                    continue

                node = self.visit(child)
                if not isinstance(node, (IntNode, CharNode)):
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Invalid array definition!")
                    return None

                array_sizes.append(int(node.value))

            # Check if array is valid with the given sizes
            if not self.checkArraySizes(rvalue, array_sizes):
                self.errors.append("The size of the array does not match the given sizes.")

            # Check if elements of array are the same type as the type node
            if not self.checkArrayTypes(rvalue, type_node):
                self.errors.append("The elements of the array are not the same type as the type node.")

            # Add symbol to scope
            if self.scope.get_symbol(identifier):
                self.errors.append(
                    f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' already declared!")
                return None
            self.scope.add_symbol(
                Symbol(name=identifier, var_type=type_node, symbol_type='array', arraySizes=array_sizes))

            # Create definition node
            lvalue = IdentifierNode(value=identifier, line=ctx.start.line, column=ctx.start.column, original=identifier)
            return ArrayDefinitionNode(line=ctx.start.line, column=ctx.start.column, original=ctx.getText(), type=type_node, lvalue=lvalue, rvalue=rvalue, size=array_sizes)

        elif isinstance(rvalue, StringNode):
            # Check if type is char
            if type_node.value != 'char':
                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} String must be of type char!")
                return None

            # Remove quotes from string
            rvalue.value = rvalue.value[1:-1]

            # Add symbol to scope
            if self.scope.get_symbol(identifier):
                self.errors.append(
                    f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' already declared!")
                return None
            self.scope.add_symbol(
                Symbol(name=identifier, var_type=type_node, symbol_type='array', arraySizes=[len(rvalue.value)]))

            # Create definition node
            lvalue = IdentifierNode(value=identifier, line=ctx.start.line, column=ctx.start.column, original=identifier)
            original = f"{type_node.original} {identifier} [{len(rvalue.value)}] = {rvalue.original}"
            return ArrayDefinitionNode(line=ctx.start.line, column=ctx.start.column, original=original, type=type_node, lvalue=lvalue, rvalue=rvalue, size=[len(rvalue.value)])

        else:
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Invalid array or string definition!")
            return None

    def visitArrayAssignment(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)

        identifier = children[0].getText()
        array_node = self.visit(children[-1])

        # Check if array is valid with the given sizes
        id_node = self.scope.lookup(identifier)
        if id_node is None:
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' not declared yet!")
            return None
        if id_node.symbol_type != 'array':
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' is not an array!")
            return None

        # Get array sizes
        array_sizes = []
        for child in children[2:-2]:
            if child.getText() == "[":
                continue
            if child.getText() == "]":
                continue
            if isinstance(child, Parser.RvalueContext):
                array_sizes.append(self.visit(child))
            else:
                array_sizes.append(int(child.getText()))

        symbol_array_sizes = id_node.arraySizes

        # Check if array sizes are correct
        if len(array_sizes) == 0:
            # Full array assignment
            if self.checkArraySizes(array_node, symbol_array_sizes):
                if not self.checkArrayTypes(array_node, id_node.type):
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Array type mismatch!")
                    return None
                lvalue = IdentifierNode(value=id_node.name, line=ctx.start.line, column=ctx.start.column, original=identifier)
                return ArrayAssignmentNode(line=ctx.start.line, column=ctx.start.column, original=ctx.getText(), lvalue=lvalue, rvalue=array_node)
            else:
                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Array size mismatch!")
                return None
        else:
            if not isinstance(array_node, ArrayNode):
                lvalue = ArrayIdentifierNode(identifier=id_node, line=ctx.start.line, column=ctx.start.column, original=identifier, indices=array_sizes)
                return ArrayAssignmentNode(line=ctx.start.line, column=ctx.start.column, original=ctx.getText(), lvalue=lvalue, rvalue=array_node)
            else:
                # If array is an array node, it is an array
                if not self.checkArraySizes(array_node, symbol_array_sizes[len(array_sizes):]):
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Array size mismatch!")
                    return None
                # Check if array types are the same
                if not self.checkArrayTypes(array_node, id_node.type):
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Array type mismatch!")
                    return None

                # Create assignment node
                lvalue = ArrayIdentifierNode(identifier=id_node, line=ctx.start.line, column=ctx.start.column, original=identifier, indices=array_sizes)
                return ArrayAssignmentNode(line=ctx.start.line, column=ctx.start.column, original=ctx.getText(), lvalue=lvalue, rvalue=array_node)

    def visitArrayAssignmentFromCTX(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)

        lvalue = self.visit(children[0])[0]

        identifier = lvalue.value
        array_node = self.visit(children[-1])

        # Check if array is valid with the given sizes
        id_node = self.scope.lookup(identifier)
        if id_node is None:
            self.errors.append(
                f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' not declared yet!")
            return None
        if id_node.symbol_type != 'array':
            self.errors.append(
                f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' is not an array!")
            return None

        # Get array sizes
        array_sizes = []
        for index in lvalue.indices:
            array_sizes.append(index.value)
        symbol_array_sizes = id_node.arraySizes

        # Check if array sizes are correct
        if len(array_sizes) == 0:
            # Full array assignment
            if self.checkArraySizes(array_node, symbol_array_sizes):
                if not self.checkArrayTypes(array_node, id_node.type):
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Array type mismatch!")
                    return None
                lvalue = IdentifierNode(value=id_node.name, line=ctx.start.line, column=ctx.start.column,
                                        original=identifier)
                return ArrayAssignmentNode(line=ctx.start.line, column=ctx.start.column, original=ctx.getText(),
                                           lvalue=lvalue, rvalue=array_node)
            else:
                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Array size mismatch!")
                return None
        else:
            # Partial array assignment
            if not isinstance(array_node, ArrayNode):
                return ArrayAssignmentNode(line=ctx.start.line, column=ctx.start.column, original=ctx.getText(),
                                           lvalue=lvalue, rvalue=array_node)
            else:
                # If array is an array node, it is an array
                if not self.checkArraySizes(array_node, symbol_array_sizes[len(array_sizes):]):
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Array size mismatch!")
                    return None
                # Check if array types are the same
                if not self.checkArrayTypes(array_node, id_node.type):
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Array type mismatch!")
                    return None

                # Create assignment node
                return ArrayAssignmentNode(line=ctx.start.line, column=ctx.start.column, original=ctx.getText(),
                                           lvalue=lvalue, rvalue=array_node)

    def visitArray(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)

        array = []

        for child in children:
            if child.getText() == "{":
                continue
            if child.getText() == "}":
                continue
            if child.getText() == ",":
                continue
            if isinstance(child, Parser.ArrayContext):
                array.append(self.visit(child))
                continue
            array.append(self.visit(child))

        return ArrayNode(line=ctx.start.line, column=ctx.start.column, original=ctx.getText(), array=array)

    def visitArrayElement(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)

        identifier = children[0].getText()
        id_node = self.scope.lookup(identifier)

        if id_node is None:
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' not declared yet!")
            return None

        if id_node.symbol_type != 'array':
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' is not an array!")
            return None

        array_sizes = []

        for child in children[2:]:
            if child.getText() == "[":
                continue
            if child.getText() == "]":
                continue
            if isinstance(child, Parser.RvalueContext):
                array_sizes.append(self.visit(child))
            else:
                array_sizes.append(int(child.getText()))

        # check if array sizes are correct
        if len(array_sizes) != len(id_node.arraySizes):
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Array size mismatch!")
            return None

        for i in range(len(id_node.arraySizes)):
            if isinstance(array_sizes[i], (IntNode, CharNode)):
                if int(array_sizes[i].value) >= id_node.arraySizes[i]:
                    self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Array index out of bounds!")
                    return ArrayIdentifierNode(identifier=id_node, line=ctx.start.line, column=ctx.start.column, original=identifier, indices=array_sizes)

        original = f"{identifier}["
        for size in array_sizes:
            original += f"{size.value}]"
        return ArrayIdentifierNode(identifier=id_node, line=ctx.start.line, column=ctx.start.column, original=original, indices=array_sizes)

    def visitStructDefinition(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)

        struct_name = children[1].getText()
        struct_members = []

        for i in range(len(children)):
            if children[i].getText() in ["{", "}", ";", "struct", struct_name]:
                continue
            if isinstance(children[i], Parser.TypeContext) and isinstance(children[i+1], Parser.IdentifierContext):
                struct_members.append([self.visit(children[i]), self.visit(children[i+1])])
            elif isinstance(children[i], Parser.ArrayDeclarationContext):
                struct_members.append(self.visit(children[i]))

        for i in range(len(struct_members)):
            if isinstance(struct_members[i], list):
                original = f"{struct_members[i][0].original} {struct_members[i][1].original}"
                struct_members[i] = DeclarationNode(line=struct_members[i][0].line, column=struct_members[i][0].column, original=original, type=struct_members[i][0], lvalue=struct_members[i][1])


        # Check if struct members are unique
        member_set = set([])
        for struct_member in struct_members:
            member_set.add(struct_member.lvalue.value)
        if len(member_set) != len(struct_members):
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Struct members must be unique!")
            return None

        # Check if struct is already declared
        if self.scope.get_struct(struct_name):
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Struct \'{struct_name}\' already declared!")
            return None

        self.scope.add_struct(struct_name, struct_members)

        # Create struct node
        original = f"struct {struct_name} " + "{"
        for member in struct_members:
            original += f"{member.original}, "
        original = original[:-2] + "}"
        return StructNode(line=ctx.start.line, column=ctx.start.column, original=original, struct_name=struct_name, struct_members=struct_members)

    def visitStructStatement(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitStructVariable(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)

        struct_type_name = children[1].getText()
        struct_var_name = children[2].getText()

        # Check if struct type is declared
        if self.scope.get_struct(struct_type_name) is None:
            self.errors.append(
                f"line {ctx.start.line}:{ctx.start.column} Struct type \'{struct_type_name}\' not declared!")
            return None

        # Check if variable is already declared
        if self.scope.get_symbol(struct_var_name):
            self.errors.append(
                f"line {ctx.start.line}:{ctx.start.column} Variable \'{struct_var_name}\' already declared!")
            return None

        # Add symbol to scope
        type_node = TypeNode(value=struct_type_name, line=ctx.start.line, column=ctx.start.column,
                             original=struct_type_name)
        symbol = Symbol(name=struct_var_name, var_type=type_node, symbol_type='struct')
        self.scope.add_symbol(symbol)

        # Create declaration node
        original = f"{struct_type_name} {struct_var_name}"
        lvalue = IdentifierNode(value=struct_var_name, line=ctx.start.line, column=ctx.start.column,
                                original=struct_var_name)
        return StructDeclarationNode(line=ctx.start.line, column=ctx.start.column, original=original, type=type_node,
                                     lvalue=lvalue)

    def visitStructVariableDefinition(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)

        struct_type_name = children[1].getText()
        struct_var_name = children[2].getText()

        # Check if struct type is declared
        if self.scope.get_struct(struct_type_name) is None:
            self.errors.append(
                f"line {ctx.start.line}:{ctx.start.column} Struct type \'{struct_type_name}\' not declared!")
            return None

        # Check if variable is already declared
        if self.scope.get_symbol(struct_var_name):
            self.errors.append(
                f"line {ctx.start.line}:{ctx.start.column} Variable \'{struct_var_name}\' already declared!")
            return None

        # Add symbol to scope
        type_node = TypeNode(value=struct_type_name, line=ctx.start.line, column=ctx.start.column,
                             original=struct_type_name)
        symbol = Symbol(name=struct_var_name, var_type=type_node, symbol_type='struct')
        self.scope.add_symbol(symbol)

        # get struct members
        def_members = []
        for i in range(5, len(children)-1, 2):
            def_members.append(self.visit(children[i]))

        # Check if all values of the struct are assigned
        struct_members = self.scope.get_struct(struct_type_name)
        if len(struct_members) != len(def_members):
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Not all struct members are assigned!")
            return None

        for i in range(len(struct_members)):
            if self.get_highest_type(def_members[i]) != self.get_highest_type(struct_members[i].type):
                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Struct member \'{struct_members[i].lvalue.value}\' type mismatch!")
                return None

        # Create definition node
        original = f"{struct_type_name} {struct_var_name} " + "{"
        for member in def_members:
            original += f"{member.original}, "
        original = original[:-2] + "}"

        lvalue = IdentifierNode(value=struct_var_name, line=ctx.start.line, column=ctx.start.column, original=struct_var_name)

        return StructDefinitionNode(line=ctx.start.line, column=ctx.start.column, original=original, type=type_node, lvalue=lvalue, rvalue=def_members)

    def visitStructAssignment(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)

        lvalue = self.visit(children[0])
        rvalue = self.visit(children[-1])

        # check if left and right value are the same value
        if self.get_highest_type(lvalue.type) != self.get_highest_type(rvalue):
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Type mismatch!")
            return None

        return StructAssignmentNode(line=ctx.start.line, column=ctx.start.column, original=ctx.getText(), lvalue=lvalue, rvalue=rvalue)

    def visitStructMember(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)

        struct_var_name = children[0].getText()

        # Check if struct variable is declared
        struct_var_node = self.scope.get_symbol(struct_var_name)
        if struct_var_node is None:
            self.errors.append(
                f"line {ctx.start.line}:{ctx.start.column} Variable \'{struct_var_name}\' not declared yet!")
            return None

        # Check if struct variable is a struct
        if struct_var_node.symbol_type != 'struct':
            self.errors.append(
                f"line {ctx.start.line}:{ctx.start.column} Variable \'{struct_var_name}\' is not a struct!")
            return None

        # Check if struct member is declared
        struct_member_name = children[2].getText()
        if not self.scope.does_struct_contain_member(struct_var_node.type.value, struct_member_name):
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Struct member \'{struct_member_name}\' not declared!")
            return None

        member_type = self.scope.get_struct_member_type(struct_var_node.type.value, struct_member_name)


        if len(children) == 3:
            original = f"{struct_var_name}.{struct_member_name}"
            return StructMemberNode(line=ctx.start.line, column=ctx.start.column, original=original,
                                    struct_var_name=struct_var_name, struct_member_name=struct_member_name,
                                    type=member_type)
        else:
            array_sizes = []
            for child in children[3:]:
                if child.getText() == "[":
                    continue
                if child.getText() == "]":
                    continue
                array_sizes.append(int(child.getText()))

            original = f"{struct_var_name}.{struct_member_name}["
            for size in array_sizes:
                original += f"{size}]"

            return StructMemberNode(line=ctx.start.line, column=ctx.start.column, original=original,
                                    struct_var_name=struct_var_name, struct_member_name=struct_member_name,
                                    type=member_type, array_size=array_sizes)

    def visitStructPostFixDecrement(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)

        struct_member = self.visit(children[0])

        return StructPostFixNode(line=ctx.start.line, column=ctx.start.column, original=ctx.getText(), struct_member=struct_member, op="dec")

    def visitStructPostFixIncrement(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)

        struct_member = self.visit(children[0])

        return StructPostFixNode(line=ctx.start.line, column=ctx.start.column, original=ctx.getText(), struct_member=struct_member, op="inc")


    def visitStructPreFixDecrement(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)

        struct_member = self.visit(children[1])

        return StructPreFixNode(line=ctx.start.line, column=ctx.start.column, original=ctx.getText(), struct_member=struct_member, op="dec")

    def visitStructPreFixIncrement(self, ctx):
        children = []
        for line in ctx.getChildren():
            children.append(line)

        struct_member = self.visit(children[1])

        return StructPreFixNode(line=ctx.start.line, column=ctx.start.column, original=ctx.getText(), struct_member=struct_member, op="inc")




    def visitScanfStatement(self, ctx):
        children = []
        for line in ctx.getChildren():
            child = self.visit(line)
            if isinstance(child, list):
                children.extend(child)
            else:
                if child:
                    children.append(child)
        # Count amount of specifiers
        specifiers = 0
        children[0].specifier = children[0].specifier.replace('\"', '')
        copy_specifier = children[0].specifier
        i = 0
        while i < len(copy_specifier):
            if i == len(copy_specifier):
                break
            if copy_specifier[i] == '%':
                original_i = i
                i += 1
                if copy_specifier[i] == '%':
                    i += 1
                    continue
                while i != len(copy_specifier):
                    if copy_specifier[i] in ['d', 'x', 'f', 'c', 's']:
                        specifiers += 1
                        if specifiers > len(children) - 1:
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Too few arguments for format string!")
                            return None
                        if not isinstance(children[specifiers], AddrNode):
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Scanf argument is not an address to a variable!")
                            return None
                        format_type = self.get_highest_type(children[specifiers])
                        symbol = self.scope.lookup(name=children[specifiers].value.value)
                        if not isinstance(symbol, Symbol):
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'{children[specifiers].value.value}\' not declared yet!")
                            return None
                        if isinstance(symbol.type, PointerNode):
                            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Variable \'{children[specifiers].value.value}\' is a pointer!")
                        # Check if variable is same type as specifier
                        if copy_specifier[i] == 'd':
                            if format_type != 'int':
                                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Use of %d but not an int!")
                        if copy_specifier[i] == 'x':
                            if format_type != 'int':
                                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Use of %x but not an int!")
                        if copy_specifier[i] == 'f':
                            if format_type != 'float':
                                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Use of %f but not a float!")
                        if copy_specifier[i] == 'c':
                            if format_type != 'char':
                                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Use of %c but not a char!")
                        if copy_specifier[i] == 's':
                            if format_type != 'string':
                                self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Use of %s but not a string!")
                        i += 1
                        continue
                    if copy_specifier[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        i += 1
                        continue
                    i -= 1
                    if copy_specifier[i] == '%':
                        # Remove current i
                        copy_specifier = copy_specifier[:original_i] + copy_specifier[original_i+1:]
                        i -= 1
                    break
                if i == len(copy_specifier) and copy_specifier[i - 1] == '%':
                    copy_specifier = copy_specifier[:i-1]
            i += 1
        children[0].specifier = copy_specifier
        if specifiers < len(children) - 1:
            self.errors.append(f"line {ctx.start.line}:{ctx.start.column} Too many arguments for format string!")
            return None
        original = f"scanf(\"{children[0].specifier}\""
        for i in range(1, len(children)):
            original += f", {children[i].original}"
        original += ")"
        node = ScanfNode(line=ctx.start.line, column=ctx.start.column, original=original, specifier=children[0].specifier, children=children[1:])
        if len(children) == 1:
            return node
        if isinstance(children[1], IdentifierNode) or isinstance(children[1], DerefNode):
            identifier = ''
            if isinstance(children[1], IdentifierNode):
                identifier = children[1].value
            else:
                identifier = children[1].identifier.value
            if self.scope.lookup(identifier) is None:
                self.errors.append(
                    f"line {ctx.start.line}:{ctx.start.column} Variable \'" + identifier + "\' not declared yet!")
                return ProgramNode(line=0, column=0, original=None)
            if self.scope.lookup(identifier).symbol_type == 'typeDef':
                self.errors.append(
                    f"line {ctx.start.line}:{ctx.start.column} \'" + identifier + "\' is declared as type!")
                return ProgramNode(line=0, column=0, original=None)
        return node
