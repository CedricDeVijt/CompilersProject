import struct

from src.parser.AST import *
from src.parser.SymbolTable import *

unary_ops = {'LogicalNotNode', 'BitwiseNotNode'}
binary_ops = {'DivNode', 'ModNode', 'MultNode', 'MinusNode', 'PlusNode', 'GTNode', 'LTNode', 'GTEQNode', 'LTEQNode',
              'EQNode', 'NEQNode', 'SLNode', 'SRNode', 'BitwiseAndNode', 'BitwiseOrNode', 'BitwiseXorNode',
              'LogicalAndNode', 'LogicalOrNode'}
literals = {'IntNode', 'FloatNode', 'CharNode', 'StringNode'}


class MIPSVisitor:
    def __init__(self, stdio=False):
        self.global_code = []
        self.code = []
        self.data = []
        self.scope = SymbolTableTree()
        self.variableAddress = 0
        self.printf_string = 0
        self.scanf_string = 0
        self.function = 0
        self.enums = {}
        self.structs = {}
        self.break_blocks = []
        self.continue_blocks = []
        self.if_count = 0
        self.while_count = 0

    def visit(self, node, return_address=0):
        method_name = "visit_" + node.__class__.__name__
        _visitor = getattr(self, method_name, self.generic_visit)
        if node.__class__.__name__ in binary_ops:
            return self.visit_BinaryOp(node, _visitor)
        if node.__class__.__name__ in unary_ops:
            return self.visit_UnaryOp(node, _visitor)
        if isinstance(node, ReturnNode) or isinstance(node, IfStatementNode) or isinstance(node, WhileLoopNode) or isinstance(node, ScopeNode):
            return _visitor(node, return_address)
        return _visitor(node)

    def generic_visit(self, node):
        raise Exception(f"No visit_{node.__class__.__name__} method")

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
                if isinstance(self.scope.lookup(identifier).type[0], PointerNode):
                    size.append(int(self.scope.lookup(identifier).type[0].value))
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
        elif isinstance(node, CharNode) or isinstance(node, IntNode) or isinstance(node, FloatNode) or isinstance(node,
                                                                                                                  str) or isinstance(
            node, int):
            return []
        elif isinstance(node, EQNode) or isinstance(node, NEQNode) or isinstance(node, LTEQNode) or isinstance(node,
                                                                                                               GTEQNode):
            return []
        elif isinstance(node, StringNode):
            return [1]
        else:
            for child in node.children:
                plist = self.get_pointer_size(child)
                if len(plist) != 0:
                    size.extend(plist)
        return size

    def get_highest_type(self, rval):
        type_check_dict = {
            DerefNode: lambda rval: self.lookup_and_get_type(rval.identifier.value),
            IdentifierNode: lambda rval: self.lookup_and_get_type(rval.value),
            AddrNode: lambda rval: self.lookup_and_get_type(rval.value.value),
            CharNode: lambda rval: 'char',
            IntNode: lambda rval: 'int',
            FloatNode: lambda rval: 'float',
            StringNode: lambda rval: 'string',
            Node: self.handle_node_type,
            str: lambda rval: rval,
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
            return self.get_highest_type(symbols.type[len(symbols.type) - 1])

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
        type1 = self.get_highest_type(rval.children[0])
        type2 = self.get_highest_type(rval.children[-1])
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

            similar = all(self.get_highest_type(param[0]) == self.get_highest_type(arg) for param, arg in
                          zip(symbol.params, rval.arguments))
            if similar:
                return self.get_highest_type(symbol.type)
        return 'char'

    def visit_ProgramNode(self, node):
        a = 5
        for child in node.children:
            self.visit(child)

    def visit_FunctionNode(self, node):
        func_name = f'function_{self.function}'
        if node.value == 'main' and len(node.params) == 0:
            self.code.append("main:")
            # Actually jump to main
            self.code.append(f"jal {func_name}")
            # Print exit code
            if self.get_highest_type(node.type) == 'void':
                pass
            else:
                # Copy exit code to $t0
                self.code.append("move $t0, $v0")
                # Print newline
                self.code.append("li $v0, 11")
                self.code.append("li $a0, 10")
                self.code.append("syscall")
                # Print actual exit code
                self.code.append("move $a0, $t0")
                if self.get_highest_type(node.type) == 'float':
                    self.code.append("li $v0, 2")
                else:
                    self.code.append("li $v0, 1")
                self.code.append("syscall")
            # Exit program
            self.code.append("li $v0, 10")
            self.code.append("syscall")
        # Increment function name
        self.function += 1
        # Add function label
        self.code.append(f"{func_name}:")
        # Add function to scope
        func_symbol = Symbol(name=node.value, var_type=node.type, symbol_type='function', params=node.params)
        func_symbol.mips_name = func_name
        func_symbol.return_address = self.variableAddress
        # Increment address by 4 bytes
        self.variableAddress += 4
        self.scope.add_symbol(func_symbol)
        # Open function scope
        self.scope.open_scope()
        # Define $sp in main
        if node.value == 'main' and len(node.params) == 0:
            self.code.append(f"li $sp, 0x7ffffffc")
        # Add arguments to scope where function is defined (easier to access)
        for param in node.params:
            # Get type of param
            var_type = self.get_highest_type(param[0])
            # Make symbol
            symbol = Symbol(param[1].value, var_type, 'variable')
            # Set address to param
            symbol.memAddress = self.variableAddress
            # Set address to param of func_symbol
            if not hasattr(func_symbol, 'paramsAddresses'):
                func_symbol.paramsAddresses = []
            func_symbol.paramsAddresses.append(self.variableAddress)
            # Increment address by 4 bytes
            self.variableAddress += 4
            # Add param to scope
            if self.scope.get_symbol(name=symbol.name) is None:
                self.scope.add_symbol(symbol)
        for statement in node.body:
            if not isinstance(statement, CommentNode) and not isinstance(statement, ScopeNode):
                # Add comment for code
                self.code.append(f"# {statement.original}")
            self.visit(statement, func_symbol.return_address)
        # Close function scope
        self.scope.close_scope()

    def visit_FunctionCallNode(self, node):
        # Get matching function
        symbols = self.scope.lookup(name=node.value)
        if isinstance(symbols, Symbol):
            symbols = [symbols]
        if not isinstance(symbols, list):
            return
        for symbol in symbols:
            if len(symbol.params) != len(node.arguments):
                continue
            similar = all(self.get_highest_type(param[0]) == self.get_highest_type(arg) for param, arg in zip(symbol.params, node.arguments))
            if similar:
                symbols = symbol
                break

        # Save previous arguments to stack
        # for i in range(0, len(node.arguments)):
        #     self.code.append(f"lw $t0, -{symbols.paramsAddresses[i]}($gp)")
        #     self.code.append("sub $sp, $sp, 4")
        #     self.code.append("sw $t0, 0($sp)")
        # Load arguments into their addresses
        for arg in node.arguments:
            arg_type = self.get_highest_type(arg)
            if self.get_pointer_size(arg) == [] or arg_type != 'float':
                if isinstance(self.visit(arg), list):
                    self.code.append(f"lw $t0, -{self.visit(arg)[0]}($gp)")
                    self.code.append(f"sw $t0, -{symbols.paramsAddresses[node.arguments.index(arg)]}($gp)")
                else:
                    self.code.append(f"li $t0, {self.visit(arg)}")
                    self.code.append(f"sw $t0, -{symbols.paramsAddresses[node.arguments.index(arg)]}($gp)")
            else:
                if isinstance(self.visit(arg), list):
                    self.code.append(f"l.s $f0, -{self.visit(arg)[0]}($gp)")
                    self.code.append(f"s.s $f0, -{symbols.paramsAddresses[node.arguments.index(arg)]}($gp)")
                else:
                    self.code.append(f"li.s $f0, {self.visit(arg)}")
                    self.code.append(f"s.s $f0, -{symbols.paramsAddresses[node.arguments.index(arg)]}($gp)")
        # Save $ra to stack
        self.code.append("sub $sp, $sp, 4")
        self.code.append("sw $ra, 0($sp)")
        # Jump to function
        self.code.append(f"jal {symbols.mips_name}")
        # Restore $ra from stack
        self.code.append("lw $ra, 0($sp)")
        self.code.append("add $sp, $sp, 4")
        # Restore arguments from stack
        # for i in range(len(node.arguments), 0, -1):
        #     self.code.append(f"lw $t0, 0($sp)")
        #     self.code.append("add $sp, $sp, 4")
        #     self.code.append(f"sw $t0, -{symbols.paramsAddresses[node.arguments.index(arg)]}($gp)")
        # Return return value
        return [symbols.return_address]

    def visit_ReturnNode(self, node, return_address):
        if node.return_type != 'void':
            address = self.visit(node.return_value)
            # Save to return address.
            if isinstance(address, float):
                self.code.append(f"li.s $f0, {address}")
            elif isinstance(address, str) or isinstance(address, int):
                if isinstance(address, str):
                    address = ord(address)
                self.code.append(f"li $t0, {address}")
            elif self.get_highest_type(node.return_value) == 'float':
                self.code.append(f"l.s $f0, -{address[0]}($gp)")
            else:
                self.code.append(f"lw $t0, -{address[0]}($gp)")
            # Save to address
            if self.get_highest_type(node.return_value) == 'float':
                self.code.append(f"s.s $f0, -{return_address}($gp)")
                self.code.append("mov.s $v0, $f0")
            else:
                self.code.append(f"sw $t0, -{return_address}($gp)")
                self.code.append("move $v0, $t0")
        self.code.append(f"jr $ra")

    def visit_DeclarationNode(self, node):
        code = []
        var_type = self.get_highest_type(node.type[len(node.type) - 1])
        symbol = Symbol(node.lvalue.value, node.type, 'variable')
        symbol.memAddress = self.variableAddress
        # Increment address by 4 bytes
        self.variableAddress += 4
        if self.scope.get_symbol(name=node.lvalue.value) is None:
            self.scope.add_symbol(symbol)

        if var_type == 'float':
            # Store 0 in variable
            code.append(f"li.s $f0, 0.0")
            # Save to memory
            code.append(f"s.s $f0, -{symbol.memAddress}($gp)")
        else:
            # Store 0 in variable
            code.append(f"li $t0, 0")
            # Save to memory
            code.append(f"sw $t0, -{symbol.memAddress}($gp)")

        if self.scope.is_global():
            self.global_code.extend(code)
        else:
            self.code.extend(code)

        if self.scope.get_symbol(name=symbol.name) is None:
            self.scope.add_symbol(symbol)

    def visit_ArrayDeclarationNode(self, node):
        var_type = node.type.value
        # create and save symbol
        symbol = Symbol(node.lvalue.value, var_type, 'array')
        symbol.memAddress = self.variableAddress
        # Increment address by 4 bytes
        self.variableAddress += 4
        symbol.dimensions = node.size
        if self.scope.get_symbol(name=node.lvalue.value) is None:
            self.scope.add_symbol(symbol)

        # create zero array
        self.assignZeroArray(self.create_multi_dimensional_list(node.size), var_type)

    def visit_StructDeclarationNode(self, node):
        code = []
        struct_name = node.type.value
        symbol = Symbol(node.lvalue.value, node.type, 'struct')
        symbol.struct_name = struct_name
        symbol.memAddress = self.variableAddress
        # Increment address by 4 bytes
        self.variableAddress += 4
        if self.scope.get_symbol(name=node.lvalue.value) is None:
            self.scope.add_symbol(symbol)

        for i in self.structs[struct_name][0]:
            if i == 'int' or i == 'char':
                code.append(f"li $t0, 0")
                code.append(f"sw $t0, -{self.variableAddress}($gp)")
            elif i == 'float':
                code.append(f"li.s $f0, 0.0")
                code.append(f"s.s $f0, -{self.variableAddress}($gp)")

        if self.scope.is_global():
            self.global_code.extend(code)
        else:
            self.code.extend(code)

    def visit_StructDefinitionNode(self, node):
        code = []
        struct_name = node.type.value
        symbol = Symbol(node.lvalue.value, node.type, 'struct')
        symbol.struct_name = struct_name
        symbol.memAddress = self.variableAddress
        if self.scope.get_symbol(name=node.lvalue.value) is None:
            self.scope.add_symbol(symbol)

        for i in range(len(self.structs[struct_name][0])):
            if self.structs[struct_name][0][i] == 'int':
                code.append(f"li $t0, {self.visit(node.rvalue[i])}")
                code.append(f"sw $t0, -{self.variableAddress}($gp)")
                self.variableAddress += 4
            elif self.structs[struct_name][0][i] == 'float':
                code.append(f"li.s $f0, {self.visit(node.rvalue[i])}")
                code.append(f"s.s $f0, -{self.variableAddress}($gp)")
                self.variableAddress += 4
            elif self.structs[struct_name][0][i] == 'char':
                code.append(f"li $t0, {ord(self.visit(node.rvalue[i]))}")
                code.append(f"sw $t0, -{self.variableAddress}($gp)")
                self.variableAddress += 4

        if self.scope.is_global():
            self.global_code.extend(code)
        else:
            self.code.extend(code)

    def visit_DefinitionNode(self, node):
        code = []
        node_type = node.type
        if not isinstance(node_type, list):
            node_type = [node_type]
        var_type = self.get_highest_type(node_type[len(node_type) - 1])
        symbol = Symbol(node.lvalue.value, node.type, 'variable')
        symbol.memAddress = self.variableAddress
        # Increment address by 4 bytes
        self.variableAddress += 4
        rvalue = self.visit(node.rvalue)
        if isinstance(rvalue, str):
            rvalue = ord(rvalue)
        if isinstance(rvalue, int):
            # Load int
            code.append(f"li $t0, {rvalue}")

            if self.get_highest_type(symbol.type[len(symbol.type) - 1]) == 'float':
                # Move to $f0
                code.append(f"mtc1 $t0, $f0")
                # Convert to float
                code.append(f"cvt.s.w $f0, $f0")
                # Save to memory
                code.append(f"s.s $f0, -{symbol.memAddress}($gp)")
                # Increment address by 4 bytes
            else:
                # Save to memory
                code.append(f"sw $t0, -{symbol.memAddress}($gp)")
        elif isinstance(rvalue, float):
            # Load float
            code.append(f"li.s $f0, {rvalue}")

            if self.get_highest_type(symbol.type[len(symbol.type) - 1]) == 'int' or self.get_highest_type(symbol.type[len(symbol.type) - 1]) == 'char':
                # Convert to int
                code.append("cvt.w.s $f0, $f0")
                # Move
                code.append("mfc1 $t0, $f0")
                # Save to memory
                code.append(f"sw $t0, -{symbol.memAddress}($gp)")
            else:
                # Save to memory
                code.append(f"s.s $f0, -{symbol.memAddress}($gp)")
        elif isinstance(rvalue, list):
            address = rvalue[0]
            if var_type == 'char' or var_type == 'int':
                if self.get_highest_type(node.rvalue) == 'float':
                    # Load as float
                    code.append(f"l.s $f0, -{address}($gp)")
                    # Convert to int
                    code.append("cvt.w.s $f0, $f0")
                    # Move
                    code.append("mfc1 $t0, $f0")
                else:
                    # Load as int
                    code.append(f"lw $t0, -{address}($gp)")
                # Save to memory
                code.append(f"sw $t0, -{symbol.memAddress}($gp)")
            elif var_type == 'float':
                if self.get_highest_type(node.rvalue) != 'float':
                    # Load as int
                    code.append(f"lw $t0, -{address}($gp)")
                    # Move to $f0
                    code.append("mtc1 $t0, $f0")
                    # Convert to float
                    code.append("cvt.s.w $f0, $f0")
                else:
                    # Load as float
                    code.append(f"l.s $f0, -{address}($gp)")
                # Save to memory
                code.append(f"s.s $f0, -{symbol.memAddress}($gp)")

        if self.scope.is_global():
            self.global_code.extend(code)
        else:
            self.code.extend(code)

        if self.scope.get_symbol(name=node.lvalue.value) is None:
            self.scope.add_symbol(symbol)

    def assignArrayElement(self, node, var_type):
        code = []
        # recursive method to assign array elements to memory
        if isinstance(node.array[0], ArrayNode):
            for i in node.array:
                self.assignArrayElement(i, var_type)
        else:
            for i in node.array:
                if var_type == 'float':
                    # Store 0 in variable
                    code.append(f"li.s $f0, {self.visit(i)}")
                    # Save to memory
                    code.append(f"s.s $f0, -{self.variableAddress}($gp)")
                    # Increment address by 4 bytes
                    self.variableAddress += 4
                else:
                    # Store value in memory
                    if var_type == 'char':
                        code.append(f"li $t0, {ord(self.visit(i))}")
                    else:
                        code.append(f"li $t0, {self.visit(i)}")
                    # Save to memory
                    code.append(f"sw $t0, -{self.variableAddress}($gp)")
                    # Increment address by 4 bytes
                    self.variableAddress += 4

        if self.scope.is_global():
            self.global_code.extend(code)
        else:
            self.code.extend(code)

    def create_multi_dimensional_list(self, dimensions):
        if not dimensions:
            return 0
        else:
            return [self.create_multi_dimensional_list(dimensions[1:]) for _ in range(dimensions[0])]

    def assignZeroArray(self, dimensions, var_type):
        code = []
        # recursive method to assign array elements to memory
        if not isinstance(dimensions[0], list):
            for i in dimensions:
                if var_type == 'float':
                    # Store 0 in variable
                    code.append(f"li.s $f0, 0.0")
                    # Save to memory
                    code.append(f"s.s $f0, -{self.variableAddress}($gp)")
                    # Increment address by 4 bytes
                    self.variableAddress += 4
                else:
                    # Store 0 in variable
                    code.append(f"li $t0, 0")
                    # Save to memory
                    code.append(f"sw $t0, -{self.variableAddress}($gp)")
                    # Increment address by 4 bytes
                    self.variableAddress += 4
        else:
            for i in dimensions:
                self.assignZeroArray(i, var_type)

        if self.scope.is_global():
            self.global_code.extend(code)
        else:
            self.code.extend(code)

    def visit_ArrayDefinitionNode(self, node):
        var_type = node.type.value
        # create and save symbol
        symbol = Symbol(node.lvalue.value, var_type, 'array')
        symbol.memAddress = self.variableAddress
        # Increment address by 4 bytes
        self.variableAddress += 4
        symbol.dimensions = node.size
        if self.scope.get_symbol(name=node.lvalue.value) is None:
            self.scope.add_symbol(symbol)

        # load values in array to memory
        self.assignArrayElement(node.rvalue, var_type)

    def visit_AssignmentNode(self, node):
        code = []
        if isinstance(node.lvalue, IdentifierNode):
            symbol = self.scope.lookup(name=node.lvalue.value)
            if symbol is not None:
                rvalue = self.visit(node.rvalue)
                var_type = self.get_highest_type(symbol.type)
                if isinstance(rvalue, str):
                    rvalue = ord(rvalue)
                if isinstance(rvalue, int):
                    # Load int
                    code.append(f"li $t0, {rvalue}")

                    if self.get_highest_type(symbol.type[len(symbol.type) - 1]) == 'float':
                        # Move to $f0
                        code.append(f"mtc1 $t0, $f0")
                        # Convert to float
                        code.append(f"cvt.s.w $f0, $f0")
                        # Save to memory
                        code.append(f"s.s $f0, -{symbol.memAddress}($gp)")
                    else:
                        # Save to memory
                        code.append(f"sw $t0, -{symbol.memAddress}($gp)")
                elif isinstance(rvalue, float):
                    # Load float
                    code.append(f"li.s $f0, {rvalue}")

                    if self.get_highest_type(symbol.type[len(symbol.type) - 1]) == 'int' or self.get_highest_type(symbol.type[len(symbol.type) - 1]) == 'char':
                        # Convert to int
                        code.append("cvt.w.s $f0, $f0")
                        # Move
                        code.append("mfc1 $t0, $f0")
                        # Save to memory
                        code.append(f"sw $t0, -{symbol.memAddress}($gp)")
                    else:
                        # Save to memory
                        code.append(f"s.s $f0, -{symbol.memAddress}($gp)")
                elif isinstance(rvalue, list):
                    address = rvalue[0]
                    if var_type == 'char' or var_type == 'int':
                        if self.get_highest_type(node.rvalue) == 'float':
                            # Load as float
                            code.append(f"l.s $f0, -{address}($gp)")
                            # Convert to int
                            code.append("cvt.w.s $f0, $f0")
                            # Move
                            code.append("mfc1 $t0, $f0")
                        else:
                            # Load as int
                            code.append(f"lw $t0, -{address}($gp)")
                        # Save to memory
                        code.append(f"sw $t0, -{symbol.memAddress}($gp)")
                    elif var_type == 'float':
                        if self.get_highest_type(node.rvalue) != 'float':
                            # Load as int
                            code.append(f"lw $t0, -{address}($gp)")
                            # Move to $f0
                            code.append("mtc1 $t0, $f0")
                            # Convert to float
                            code.append("cvt.s.w $f0, $f0")
                        else:
                            # Load as float
                            code.append(f"l.s $f0, -{address}($gp)")
                        # Save to memory
                        code.append(f"s.s $f0, -{symbol.memAddress}($gp)")
        elif isinstance(node.lvalue, DerefNode):
            symbol = self.scope.lookup(name=node.lvalue.identifier.value)
            if symbol is not None:
                lvalue = self.return_DerefNodeAddress(node.lvalue)
                # Load address
                code.append(f"lw $t1, -{lvalue[0]}($gp)")
                rvalue = self.visit(node.rvalue)

                var_type = self.get_highest_type(symbol.type[len(symbol.type) - 1])
                if isinstance(rvalue, str):
                    rvalue = ord(rvalue)
                if isinstance(rvalue, int):
                    # Load int
                    code.append(f"li $t0, {rvalue}")

                    if self.get_highest_type(symbol.type[len(symbol.type) - 1]) == 'float':
                        # Move to $f0
                        code.append(f"mtc1 $t0, $f0")
                        # Convert to float
                        code.append(f"cvt.s.w $f0, $f0")
                        # Save to memory
                        code.append(f"s.s $f0, 0($t1)")
                    else:
                        # Save to memory
                        code.append("sw $t0, 0($t1)")
                elif isinstance(rvalue, float):
                    # Load float
                    code.append(f"li.s $f0, {rvalue}")

                    if self.get_highest_type(symbol.type[len(symbol.type) - 1]) == 'int' or self.get_highest_type(symbol.type[len(symbol.type) - 1]) == 'char':
                        # Convert to int
                        code.append("cvt.w.s $f0, $f0")
                        # Move
                        code.append("mfc1 $t0, $f0")
                        # Save to memory
                        code.append("sw $t0, 0($t1)")
                    else:
                        # Save to memory
                        code.append("s.s $f0, 0($t1)")
                elif isinstance(rvalue, list):
                    address = rvalue[0]
                    if len(self.get_pointer_size(node.rvalue)) != 0:
                        # Put address in $t0
                        code.append(f"sub $t0, $gp, {address}")
                        # Save to memory
                        code.append(f"sw, $t0, -{symbol.memAddress}($gp)")
                    elif var_type == 'char' or var_type == 'int':
                        if self.get_highest_type(node.rvalue) == 'float':
                            # Load as float
                            code.append(f"l.s $f0, -{address}($gp)")
                            # Convert to int
                            code.append("cvt.w.s $f0, $f0")
                            # Move
                            code.append("mfc1 $t0, $f0")
                        else:
                            # Load as int
                            code.append(f"lw $t0, -{address}($gp)")
                        # Save to memory
                        code.append(f"sw $t0, -{symbol.memAddress}($gp)")
                    elif var_type == 'float':
                        if self.get_highest_type(node.rvalue) != 'float':
                            # Load as int
                            code.append(f"lw $t0, -{address}($gp)")
                            # Move to $f0
                            code.append("mtc1 $t0, $f0")
                            # Convert to float
                            code.append("cvt.s.w $f0, $f0")
                        else:
                            # Load as float
                            code.append(f"l.s $f0, -{address}($gp)")
                        # Save to memory
                        code.append(f"s.s $f0, -{symbol.memAddress}($gp)")

        if self.scope.is_global():
            self.global_code.extend(code)
        else:
            self.code.extend(code)

    def visit_ArrayAssignmentNode(self, node):
        code = []
        symbol = self.scope.lookup(name=node.lvalue.value)
        dimensions = symbol.dimensions
        address = symbol.memAddress
        for i in range(len(node.lvalue.indices)):
            add = self.visit(node.lvalue.indices[i])
            for j in range(i + 1, len(dimensions)):
                add *= dimensions[j]
            address += add * 4

        if symbol.type == 'float':
            # Store 0 in variable
            code.append(f"li.s $f0, {self.visit(node.rvalue)}")
            # Save to memory
            code.append(f"s.s $f0, -{address}($gp)")
        else:
            # Store value in memory
            if symbol.type == 'char':
                code.append(f"li $t0, {ord(self.visit(node.rvalue))}")
            else:
                code.append(f"li $t0, {self.visit(node.rvalue)}")
            # Save to memory
            code.append(f"sw $t0, -{address}($gp)")

        if self.scope.is_global():
            self.global_code.extend(code)
        else:
            self.code.extend(code)

    def visit_StructAssignmentNode(self, node):
        code = []
        struct_var_name = node.lvalue.struct_var_name
        symbol = self.scope.lookup(name=struct_var_name)
        struct_name = symbol.struct_name
        types = self.structs[struct_name][0]
        vars = self.structs[struct_name][1]
        index = vars.index(node.lvalue.struct_member_name)
        address = symbol.memAddress + index * 4
        type = types[index]

        if isinstance(node.rvalue, IntNode):
            code.append(f"li $t0, {self.visit(node.rvalue)}")
            code.append(f"sw $t0, -{address}($gp)")
        elif isinstance(node.rvalue, FloatNode):
            code.append(f"li.s $f0, {self.visit(node.rvalue)}")
            code.append(f"s.s $f0, -{address}($gp)")
        elif isinstance(node.rvalue, CharNode):
            code.append(f"li $t0, {ord(self.visit(node.rvalue))}")
            code.append(f"sw $t0, -{address}($gp)")
        else:
            if type == 'float':
                code.append(f"l.s $f0, -{self.visit(node.rvalue)[0]}($gp)")
                code.append(f"s.s $f0, -{address}($gp)")
            else:
                code.append(f"lw $t0, -{self.visit(node.rvalue)[0]}($gp)")
                code.append(f"sw $t0, -{address}($gp)")

        if self.scope.is_global():
            self.global_code.extend(code)
        else:
            self.code.extend(code)

    def visit_IdentifierNode(self, node):
        symbol = self.scope.lookup(name=node.value)
        if symbol is not None:
            if node.value.count('-') % 2 == 1:
                if self.get_highest_type(node) == 'float':
                    # Load from memory
                    self.code.append(f"l.s $f0, -{symbol.memAddress}($gp)")
                    # Negate
                    self.code.append("neg.s $f0, $f0")
                    # Save to memory
                    self.code.append(f"s.s $f0, -{self.variableAddress}($gp)")
                    # Increment self.variableAddress
                    self.variableAddress += 4
                    return [self.variableAddress - 4]
                # Load value
                self.code.append(f"lw $t0, -{symbol.memAddress}($gp)")
                # Negate
                self.code.append("neg $t0, $t0")
                # Save to memory
                self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
                # Increment self.variableAddress
                self.variableAddress += 4
                return [self.variableAddress - 4]
            return [symbol.memAddress]

    def visit_AddrNode(self, node):
        symbol = self.scope.lookup(name=node.value.value)
        if symbol is not None:
            # Subtract memAddress from $gp
            self.code.append(f"sub $t0, $gp, {symbol.memAddress}")
            # Save to memory
            self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
            # Increment self.variableAddress
            self.variableAddress += 4
            return [self.variableAddress - 4]

    def visit_DerefNode(self, node):
        symbol = self.scope.lookup(name=node.identifier.value)
        if symbol is not None:
            # Subtract memAddress from $gp
            self.code.append(f"sub $t0, $gp, {symbol.memAddress}")
            # Load from address
            self.code.append(f"lw $t0, 0($t0)")
            for i in range(0, int(node.value)):
                self.code.append(f"lw $t0, 0($t0)")
            # Store in memory
            self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
            # Increment self.variableAddress
            self.variableAddress += 4
            return [self.variableAddress - 4]

    def return_DerefNodeAddress(self, node):
        symbol = self.scope.lookup(name=node.identifier.value)
        if symbol is not None:
            # Load memAddress to register
            self.code.append(f"li $t0, {symbol.memAddress}")
            # Subtract $t0 from $gp
            self.code.append("sub $t0, $gp, $t0")
            # Load from address
            self.code.append(f"lw $t0, -{symbol.memAddress}($gp)")
            for i in range(0, int(node.value) - 1):
                self.code.append(f"lw $t0, 0($t0)")
            # Store in memory
            self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
            # Increment self.variableAddress
            self.variableAddress += 4
            return [self.variableAddress - 4]

    def visit_ArrayIdentifierNode(self, node):
        symbol = self.scope.lookup(name=node.value)
        dimensions = symbol.dimensions
        address = symbol.memAddress
        for i in range(len(node.indices)):
            add = self.visit(node.indices[i])
            for j in range(i+1, len(dimensions)):
                add *= dimensions[j]
            address += add * 4
        return address

    def visit_PrintfNode(self, node):
        args = []
        specifiers = node.specifier
        amtSpec = 0
        arguments = []
        i = 0
        while i < len(specifiers):
            if specifiers[i] == '%':
                if len(specifiers[:i]) != 0:
                    args.append(specifiers[:i])
                    specifiers = specifiers[i:]
                i = 0
                nextChar = specifiers[1]
                if nextChar == '%':
                    i += 1
                    continue
                args.append(node.children[amtSpec])
                amtSpec += 1
                specifiers = specifiers[2:]
                i = 0
                continue
            if len(specifiers) == i + 1:
                if len(specifiers) != 0:
                    args.append(specifiers)
                break
            i += 1
        for arg in args:
            if isinstance(arg, str):
                self.data.append(f"printf_string_{self.printf_string}: .asciiz \"{arg}\"")
                self.code.append(f"li $v0, 4")
                self.code.append(f"la $a0, printf_string_{self.printf_string}")
                self.code.append(f"syscall")
                self.printf_string += 1
                continue
            visited_arg = self.visit(arg)
            if isinstance(visited_arg, list):
                memAddress = visited_arg[0]
                if self.get_highest_type(arg) == 'char' or self.get_highest_type(arg) == 'int':
                    # Load from memory
                    self.code.append(f"lw $t0, -{memAddress}($gp)")
                    # Put in $a0
                    self.code.append(f"move $a0, $t0")
                    if self.get_highest_type(arg) == 'char':
                        # Print string
                        self.code.append("li $v0, 11")
                    else:
                        # Print int
                        self.code.append("li $v0, 1")
                    self.code.append("syscall")
                elif self.get_highest_type(arg) == 'float':
                    # Load from memory
                    self.code.append(f"l.s $f0, -{memAddress}($gp)")
                    # Move float to $f12
                    self.code.append("mov.s $f12, $f0")
                    # Print float
                    self.code.append("li $v0, 2")
                    self.code.append("syscall")
            elif isinstance(visited_arg, str):
                self.data.append(f"printf_string_{self.printf_string}: .asciiz {visited_arg}")
                self.code.append("li $v0, 4")
                self.code.append(f"la $a0, printf_string_{self.printf_string}")
                self.code.append("syscall")
                self.printf_string += 1
            elif isinstance(visited_arg, int) and not isinstance(arg, ArrayIdentifierNode) and not isinstance(arg, StructMemberNode):
                self.code.append("li $v0, 1")
                self.code.append(f"li $a0, {visited_arg}")
                self.code.append("syscall")
            elif isinstance(visited_arg, float):
                self.code.append("li $v0, 2")
                self.code.append(f"li $t0, {hex(struct.unpack('<I', struct.pack('<f', visited_arg))[0])}")
                self.code.append("mtc1 $t0, $f12")
                self.code.append("syscall")
            elif isinstance(arg, ArrayIdentifierNode):
                symbol = self.scope.lookup(name=arg.value)
                var_type = symbol.type
                memAddress = visited_arg
                if var_type == 'char' or var_type == 'int':
                    # Load from memory
                    self.code.append(f"lw $t0, -{memAddress}($gp)")
                    # Put in $a0
                    self.code.append(f"move $a0, $t0")
                    if var_type == 'char':
                        # Print string
                        self.code.append("li $v0, 11")
                    else:
                        self.code.append("li $v0, 1")
                    self.code.append("syscall")
                elif var_type == 'float':
                    # Load from memory
                    self.code.append(f"l.s $f0, -{memAddress}($gp)")
                    # Move float to $f12
                    self.code.append("mov.s $f12, $f0")
                    # Print float
                    self.code.append("li $v0, 2")
                    self.code.append("syscall")
            elif isinstance(arg, StructMemberNode):
                var_type = arg.type.value
                memAddress = self.visit(arg)
                if var_type == 'char' or var_type == 'int':
                    # Load from memory
                    self.code.append(f"lw $t0, -{memAddress}($gp)")
                    # Put in $a0
                    self.code.append(f"move $a0, $t0")
                    if var_type == 'char':
                        # Print string
                        self.code.append("li $v0, 11")
                    else:
                        self.code.append("li $v0, 1")
                    self.code.append("syscall")
                elif var_type == 'float':
                    # Load from memory
                    self.code.append(f"l.s $f0, -{memAddress}($gp)")
                    # Move float to $f12
                    self.code.append("mov.s $f12, $f0")
                    # Print float
                    self.code.append("li $v0, 2")
                    self.code.append("syscall")

    def visit_PreFixNode(self, node):
        if isinstance(node.value, DerefNode):
            address = self.return_DerefNodeAddress(node.value)[0]
        else:
            address = self.visit(node.value)[0]
        value = 1
        if node.op == 'dec':
            value = -1
        # If pointer or not a float
        if len(self.get_pointer_size(node.value)) != 0 or self.get_highest_type(node.value) != 'float':
            # Load value
            self.code.append(f"lw $t0, -{address}($gp)")
            if len(self.get_pointer_size(node.value)) != 0:
                # Multiply by 4 so we inc/dec by 4 bytes since it is a pointer
                # Also multiply by -1 since we save from high to low
                value *= -4
            if isinstance(node.value, DerefNode):
                # Save address
                self.code.append("move $t1, $t0")
                # Load value
                self.code.append("lw $t0, 0($t0)")
            # Add value
            self.code.append(f"add $t0, $t0, {value}")
            # Save to memory
            if isinstance(node.value, DerefNode):
                self.code.append("sw $t0, 0($t1)")
                self.code.append(f"sw $t0, -{address}($gp)")
            else:
                self.code.append(f"sw $t0, -{address}($gp)")
            # Return
            return [address]
        # Load value
        self.code.append(f"l.s $f0, -{address}($gp)")
        # Add value
        self.code.append(f"fadd $f0, $f0, {value}")
        # Save to memory
        self.code.append(f"s.s $f0, -{address}($gp)")
        # Return
        return [address]

    def visit_PostFixNode(self, node):
        if isinstance(node.value, DerefNode):
            address = self.return_DerefNodeAddress(node.value)[0]
        else:
            address = self.visit(node.value)[0]
        value = 1
        if node.op == 'dec':
            value = -1
        # If pointer or not a float
        if len(self.get_pointer_size(node.value)) != 0 or self.get_highest_type(node.value) != 'float':
            # Load value
            self.code.append(f"lw $t0, -{address}($gp)")
            if len(self.get_pointer_size(node.value)) != 0:
                # Multiply by 4 so we inc/dec by 4 bytes since it is a pointer
                # Also multiply by -1 since we save from high to low
                value *= -4
            if isinstance(node.value, DerefNode):
                # Save address
                self.code.append("move $t1, $t0")
                # Load value
                self.code.append("lw $t0, 0($t0)")
            # Save to temporary memory
            self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
            # Increment temporary memory
            self.variableAddress += 4
            # Add value
            self.code.append(f"add $t0, $t0, {value}")
            # Save to memory
            if isinstance(node.value, DerefNode):
                self.code.append("sw $t0, 0($t1)")
            else:
                self.code.append(f"sw $t0, -{address}($gp)")
            # Return
            return [self.variableAddress - 4]
        # Load value
        self.code.append(f"l.s $f0, -{address}($gp)")
        # Save to temporary memory
        self.code.append(f"s.s $f0, -{self.variableAddress}($gp)")
        # Increment temporary memory
        self.variableAddress += 4
        # Add value
        self.code.append(f"fadd $f0, $f0, {value}")
        # Save to memory
        self.code.append(f"s.s $f0, -{address}($gp)")
        # Return
        return [self.variableAddress - 4]

    def visit_ScopeNode(self, node, return_address):
        self.scope.open_scope()
        for statement in node.children:
            if not isinstance(statement, CommentNode):
                self.code.append(f"# {statement.original}")
            self.visit(statement, return_address)
        self.scope.close_scope()

    def visit_EnumNode(self, node):
        self.enums[node.enum_name] = node.enum_list

    def visit_BinaryOp(self, node, visitor):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])
        left = self.visit(node.children[0])
        right = self.visit(node.children[1])

        # Left
        if isinstance(left, list):
            address = left[0]
            if type1 == 'char' or type1 == 'int':
                # Load the value as an int
                self.code.append(f"lw $t0, -{address}($gp)")
                if type2 == 'float':
                    # Move to $f0
                    self.code.append("mtc1 $t0, $f0")
                    # Convert to float
                    self.code.append("cvt.s.w $f0, $f0")
            else:
                # Load the value as a float
                self.code.append(f"l.s $f0, -{address}($gp)")
        elif isinstance(left, str) or isinstance(left, int):
            if isinstance(left, str):
                left = ord(left)
            # Load the value as an int
            self.code.append(f"li $t0, {left}")
            if type2 == 'float':
                # Move to $f0
                self.code.append("mtc1 $t0, $f0")
                # Convert to float
                self.code.append("cvt.s.w $f0, $f0")
        elif isinstance(left, float):
            # Load the value as a float
            self.code.append(f"li.s $f0, {left}")

        # Right
        if isinstance(right, list):
            address = right[0]
            if type2 == 'char' or type2 == 'int':
                # Load the value as an int
                self.code.append(f"lw $t1, -{address}($gp)")
                if type1 == 'float':
                    # Move to $f1
                    self.code.append("mtc1 $t1, $f1")
                    # Convert to float
                    self.code.append("cvt.s.w $f1, $f1")
            else:
                # Load the value as a float
                self.code.append(f"l.s $f1 -{address}($gp)")
        elif isinstance(right, str) or isinstance(right, int):
            if isinstance(right, str):
                right = ord(right)
            # Load the value as an int
            self.code.append(f"li $t1, {right}")
            if type1 == 'float':
                # Move to $f1
                self.code.append("mtc1 $t1, $f1")
                # Convert to float
                self.code.append("cvt.s.w $f1, $f1")
        elif isinstance(right, float):
            # Load the value as a float
            self.code.append(f"li.s $f1, {right}")

        return visitor(node)

    def visit_UnaryOp(self, node, visitor):
        type1 = self.get_highest_type(node.children[0])
        child = self.visit(node.children[0])

        # Left
        if isinstance(child, list):
            address = child[0]
            if type1 == 'char' or type1 == 'int':
                # Load the value as an int
                self.code.append(f"lw $t0, -{address}($gp)")
        elif isinstance(child, str) or isinstance(child, int):
            if isinstance(child, str):
                child = ord(child)
            # Load the value as an int
            self.code.append(f"li $t0, {child}")
        elif isinstance(child, float):
            # Load the value as a float
            self.code.append(f"li.s $f0, {child}")

        return visitor(node)

    def visit_PlusNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Add
        if type1 == 'float' or type2 == 'float':
            self.code.append("add.s $f0, $f0, $f1")
            # Save to temporary address
            self.code.append(f"s.s $f0, -{self.variableAddress}($gp)")
        else:
            self.code.append("add $t0, $t0, $t1")
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
        # Increment temporary address
        self.variableAddress += 4
        # Return temporary address
        return [self.variableAddress - 4]

    def visit_MinusNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Subtract
        if type1 == 'float' or type2 == 'float':
            self.code.append("sub.s $f0, $f0, $f1")
            # Save to temporary address
            self.code.append(f"s.s $f0, -{self.variableAddress}($gp)")
        else:
            self.code.append("sub $t0, $t0, $t1")
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
        # Increment temporary address
        self.variableAddress += 4
        # Return temporary address
        return [self.variableAddress - 4]

    def visit_MultNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Mul
        if type1 == 'float' or type2 == 'float':
            self.code.append("mul.s $f0, $f0, $f1")
            # Save to temporary address
            self.code.append(f"s.s $f0, -{self.variableAddress}($gp)")
        else:
            self.code.append("mul $t0, $t0, $t1")
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
        # Increment temporary address
        self.variableAddress += 4
        # Return temporary address
        return [self.variableAddress - 4]

    def visit_DivNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Div
        if type1 == 'float' or type2 == 'float':
            self.code.append("div.s $f0, $f0, $f1")
            # Save to temporary address
            self.code.append(f"s.s $f0, -{self.variableAddress}($gp)")
        else:
            self.code.append("div $t0, $t0, $t1")
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
        # Increment temporary address
        self.variableAddress += 4
        # Return temporary address
        return [self.variableAddress - 4]

    def visit_ModNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Div
        self.code.append("div $t0, $t1")
        # Get remainder
        self.code.append("mfhi $t2")
        # Save to temporary address
        self.code.append(f"sw $t2, -{self.variableAddress}($gp)")
        # Increment temporary address
        self.variableAddress += 4
        # Return temporary address
        return [self.variableAddress - 4]

    def visit_BitwiseAndNode(self, node):
        # And
        self.code.append("and $t0, $t0, $t1")
        # Save to temporary address
        self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
        # Increment temporary address
        self.variableAddress += 4
        # Return temporary address
        return [self.variableAddress - 4]

    def visit_BitwiseOrNode(self, node):
        # Or
        self.code.append("or $t0, $t0, $t1")
        # Save to temporary address
        self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
        # Increment temporary address
        self.variableAddress += 4
        # Return temporary address
        return [self.variableAddress - 4]

    def visit_BitwiseXorNode(self, node):
        # Xor
        self.code.append("xor $t0, $t0, $t1")
        # Save to temporary address
        self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
        # Increment temporary address
        self.variableAddress += 4
        # Return temporary address
        return [self.variableAddress - 4]

    def visit_BitwiseNotNode(self, node):
        # Not
        self.code.append("not $t0, $t0")
        # Save to temporary address
        self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
        # Increment temporary address
        self.variableAddress += 4
        # Return temporary address
        return [self.variableAddress - 4]

    def visit_LogicalAndNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # And
        if type1 == 'float' or type2 == 'float':
            # Check if $f0 == 0
            self.code.append("c.eq.s $f0, $f2")
            # Load FCCR into $t0
            self.code.append("cfc1 $t0, $25")
            # Negate $t0
            self.code.append("xori $t0, $t0, 1")
            # Move to $f0
            self.code.append("mtc1 $t0, $f0")
            # Convert to float
            self.code.append("cvt.s.w $f0, $f0")

            # Check if $f1 == 0
            self.code.append("c.eq.s $f1, $f2")
            # Load FCCR into $t0
            self.code.append("cfc1 $t0, $25")
            # Negate $t0
            self.code.append("xori $t0, $t0, 1")
            # Move to $f0
            self.code.append("mtc1 $t0, $f1")
            # Convert to float
            self.code.append("cvt.s.w $f1, $f1")

            # Convert to integers
            self.code.append("cvt.w.s $f4, $f4")
            self.code.append("cvt.w.s $f5, $f5")
            # Move to $t0 and $t1
            self.code.append("mfc1 $t0, $f4")
            self.code.append("mfc1 $t1, $f5")
            # And
            self.code.append("and $t0, $t0, $t1")
            # Move to $f0
            self.code.append("mtc1 $t0, $f0")
            # Convert to float
            self.code.append("cvt.s.w $f0, $f0")
        else:
            # Check if $t0 is 0
            self.code.append("slt $t2, $t0, $zero")
            self.code.append("slt $t3, $zero, $t0")
            # 0 if $t0 is 0
            self.code.append("or $t0, $t2, $t3")

            # Check if $t1 is 0
            self.code.append("slt $t2, $t1, $zero")
            self.code.append("slt $t3, $zero, $t1")
            # 0 if $t1 is 0
            self.code.append("or $t1, $t2, $t3")

            # And
            self.code.append("and $t0, $t0, $t1")

        if type1 == 'float' or type2 == 'float':
            # Save to temporary address
            self.code.append(f"s.s $f0, -{self.variableAddress}($gp)")
        else:
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
        # Increment temporary address
        self.variableAddress += 4
        # Return temporary address
        return [self.variableAddress - 4]

    def visit_LogicalOrNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Or
        if type1 == 'float' or type2 == 'float':
            # Check if $f0 == 0
            self.code.append("c.eq.s $f0, $f2")
            # Load FCCR into $t0
            self.code.append("cfc1 $t0, $25")
            # Negate $t0
            self.code.append("xori $t0, $t0, 1")
            # Move to $f0
            self.code.append("mtc1 $t0, $f0")
            # Convert to float
            self.code.append("cvt.s.w $f0, $f0")

            # Check if $f1 == 0
            self.code.append("c.eq.s $f1, $f2")
            # Load FCCR into $t0
            self.code.append("cfc1 $t0, $25")
            # Negate $t0
            self.code.append("xori $t0, $t0, 1")
            # Move to $f0
            self.code.append("mtc1 $t0, $f1")
            # Convert to float
            self.code.append("cvt.s.w $f1, $f1")

            # Convert to integers
            self.code.append("cvt.w.s $f4, $f4")
            self.code.append("cvt.w.s $f5, $f5")
            # Move to $t0 and $t1
            self.code.append("mfc1 $t0, $f4")
            self.code.append("mfc1 $t1, $f5")
            # Or
            self.code.append("or $t0, $t0, $t1")
            # Move to $f0
            self.code.append("mtc1 $t0, $f0")
            # Convert to float
            self.code.append("cvt.s.w $f0, $f0")
        else:
            # Check if $t0 is 0
            self.code.append("slt $t2, $t0, $zero")
            self.code.append("slt $t3, $zero, $t0")
            # 0 if $t0 is 0
            self.code.append("or $t0, $t2, $t3")

            # Check if $t1 is 0
            self.code.append("slt $t2, $t1, $zero")
            self.code.append("slt $t3, $zero, $t1")
            # 0 if $t1 is 0
            self.code.append("or $t1, $t2, $t3")

            # Or
            self.code.append("or $t0, $t0, $t1")

        if type1 == 'float' or type2 == 'float':
            # Save to temporary address
            self.code.append(f"s.s $f0, -{self.variableAddress}($gp)")
        else:
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
        # Increment temporary address
        self.variableAddress += 4
        # Return temporary address
        return [self.variableAddress - 4]

    def visit_LogicalNotNode(self, node):
        type1 = self.get_highest_type(node.children[0])

        # Not
        if type1 == 'float':
            # Check if $f0 == 0
            self.code.append("c.eq.s $f0, $f1")
            # Load FCCR into $t0
            self.code.append("cfc1 $t0, $25")
            # Negate $t0
            self.code.append("xori $t0, $t0, 1")
            # Move to $f0
            self.code.append("mtc1 $t0, $f0")
            # Convert to float
            self.code.append("cvt.s.w $f0, $f0")
        else:
            # Check if $t0 == 0?
            self.code.append("seq $t0, $t0, $zero")

        if type1 == 'float':
            # Save to temporary address
            self.code.append(f"s.s $f0, -{self.variableAddress}($gp)")
        else:
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
        # Increment temporary address
        self.variableAddress += 4
        # Return temporary address
        return [self.variableAddress - 4]

    def visit_LTNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Less than
        if type1 == 'float' or type2 == 'float':
            # Check if $f0 < $f1
            self.code.append("c.lt.s $f0, $f1")
            # Load FCCR into $t0
            self.code.append("cfc1 $t0, $25")
            # Move to $f0
            self.code.append("mtc1 $t0, $f0")
            # Convert to float
            self.code.append("cvt.s.w $f0, $f0")
        else:
            # Check if $t0 < $t1
            self.code.append("slt $t0, $t0, $t1")

        if type1 == 'float' or type2 == 'float':
            # Save to temporary address
            self.code.append(f"s.s $f0, -{self.variableAddress}($gp)")
        else:
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
        # Increment temporary address
        self.variableAddress += 4
        # Return temporary address
        return [self.variableAddress - 4]

    def visit_GTNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Greater than
        if type1 == 'float' or type2 == 'float':
            # Check if $f1 <= $f0 aka $f0 > $f1
            self.code.append("c.le.s $f1, $f0")
            # Load FCCR into $t0
            self.code.append("cfc1 $t0, $25")
            # Move to $f0
            self.code.append("mtc1 $t0, $f0")
            # Convert to float
            self.code.append("cvt.s.w $f0, $f0")
        else:
            # Check if $t0 < $t1
            self.code.append("slt $t2, $t0, $t1")
            # Check if $t0 == $t1
            self.code.append("seq $t3, $t0, $t1")
            # Check if $t2 or $t3 is true
            self.code.append("or $t0, $t2, $t3")
            # Negate $t0
            self.code.append("xori $t0, $t0, 1")

        if type1 == 'float' or type2 == 'float':
            # Save to temporary address
            self.code.append(f"s.s $f0, -{self.variableAddress}($gp)")
        else:
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
        # Increment temporary address
        self.variableAddress += 4
        # Return temporary address
        return [self.variableAddress - 4]

    def visit_EQNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Equals
        if type1 == 'float' or type2 == 'float':
            # Check if $f0 == $f1
            self.code.append("c.eq.s $f0, $f1")
            # Load FCCR into $t0
            self.code.append("cfc1 $t0, $25")
            # Move to $f0
            self.code.append("mtc1 $t0, $f0")
            # Convert to float
            self.code.append("cvt.s.w $f0, $f0")
        else:
            # Check if $t0 == $t1
            self.code.append("seq $t0, $t0, $t1")

        if type1 == 'float' or type2 == 'float':
            # Save to temporary address
            self.code.append(f"s.s $f0, -{self.variableAddress}($gp)")
        else:
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
        # Increment temporary address
        self.variableAddress += 4
        # Return temporary address
        return [self.variableAddress - 4]

    def visit_NEQNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Not equals
        if type1 == 'float' or type2 == 'float':
            # Check if $f0 == $f1
            self.code.append("c.eq.s $f0, $f1")
            # Load FCCR into $t0
            self.code.append("cfc1 $t0, $25")
            # Negate $t0
            self.code.append("xori $t0, $t0, 1")
            # Move to $f0
            self.code.append("mtc1 $t0, $f0")
            # Convert to float
            self.code.append("cvt.s.w $f0, $f0")
        else:
            # Check if $t0 == $t1
            self.code.append("seq $t0, $t0, $t1")
            # Negate $t0
            self.code.append("xori $t0, $t0, 1")

        if type1 == 'float' or type2 == 'float':
            # Save to temporary address
            self.code.append(f"s.s $f0, -{self.variableAddress}($gp)")
        else:
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
        # Increment temporary address
        self.variableAddress += 4
        # Return temporary address
        return [self.variableAddress - 4]

    def visit_LTEQNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Less than or equals
        if type1 == 'float' or type2 == 'float':
            # Check if $f0 < $f1
            self.code.append("c.lt.s $f0, $f1")
            # Load FCCR into $t0
            self.code.append("cfc1 $t0, $25")
            # Check if $f0 == $f1
            self.code.append("c.eq.s $f0, $f1")
            # Load FCCR into $t1
            self.code.append("cfc1 $t1, $25")
            # Or of $t0 and $t1
            self.code.append("or $t0, $t0, $t1")
            # Move to $f0
            self.code.append("mtc1 $t0, $f0")
            # Convert to float
            self.code.append("cvt.s.w $f0, $f0")
        else:
            # Check if $t0 < $t1
            self.code.append("slt $t2, $t0, $t1")
            # Check if $t0 == $t1
            self.code.append("seq $t3, $t0, $t1")
            # Or of $t2 and $t3
            self.code.append("or $t0, $t2, $t3")

        if type1 == 'float' or type2 == 'float':
            # Save to temporary address
            self.code.append(f"s.s $f0, -{self.variableAddress}($gp)")
        else:
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
        # Increment temporary address
        self.variableAddress += 4
        # Return temporary address
        return [self.variableAddress - 4]

    def visit_GTEQNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Greater than
        if type1 == 'float' or type2 == 'float':
            # Check if $f1 <= $f0 aka $f0 > $f1
            self.code.append("c.lt.s $f1, $f0")
            # Load FCCR into $t0
            self.code.append("cfc1 $t0, $25")
            # Negate $t0
            self.code.append("xori $t0, $t0, 1")
            # Move to $f0
            self.code.append("mtc1 $t0, $f0")
            # Convert to float
            self.code.append("cvt.s.w $f0, $f0")
        else:
            # Check if $t0 < $t1
            self.code.append("slt $t0, $t0, $t1")
            # Negate $t0
            self.code.append("xori $t0, $t0, 1")

        if type1 == 'float' or type2 == 'float':
            # Save to temporary address
            self.code.append(f"s.s $f0, -{self.variableAddress}($gp)")
        else:
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
        # Increment temporary address
        self.variableAddress += 4
        # Return temporary address
        return [self.variableAddress - 4]

    def visit_CommentNode(self, node):
        endline = '\n'
        backslash = '\\'
        self.code.append(f"#{node.value.strip().replace(endline, f'{backslash}n ')}")

    def visit_SLNode(self, node):
        # Perform the shift operation
        self.code.append("sll $t0, $t0, $t1")

        # Save to temporary address
        self.code.append(f"sw $t0, -{self.variableAddress}($gp)")

        # Increment temporary address
        self.variableAddress += 4

        # Return temporary address
        return [self.variableAddress - 4]

    def visit_SRNode(self, node):
        # Perform the shift operation
        self.code.append("sra $t0, $t0, $t1")

        # Save to temporary address
        self.code.append(f"sw $t0, -{self.variableAddress}($gp)")

        # Increment temporary address
        self.variableAddress += 4

        # Return temporary address
        return [self.variableAddress - 4]

    def visit_ExplicitConversionNode(self, node):
        # Visit the child node
        child = self.visit(node.rvalue)

        if self.get_highest_type(node.rvalue) == 'float':
            # Load from memory
            self.code.append(f"l.s $f0, -{child[0]}($gp)")
            if node.type == 'float':
                # Save to address
                self.code.append(f"s.s $f0, -{self.variableAddress}($gp)")
            else:
                # Convert to int
                self.code.append("cvt.w.s $f0, $f0")
                # Move to $t0
                self.code.append("mfc1 $t0, $f0")
                # Save to address
                self.code.append(f"sw $t0, -{self.variableAddress}($gp)")
        else:
            # Load from memory
            self.code.append(f"lw $t0, -{child[0]}($gp)")
            if node.type == 'float':
                # Move to $f0
                self.code.append("mtc1 $t0, $f0")
                # Convert to float
                self.code.append("cvt.s.w $f0, $f0")
                # Save to address
                self.code.append(f"s.s $f0, -{self.variableAddress}($gp)")
            else:
                # Save to address
                self.code.append(f"sw $t0, -{self.variableAddress}($gp)")

        # Increment temporary address
        self.variableAddress += 4

        # Return temporary address
        return [self.variableAddress - 4]

    def visit_IfStatementNode(self, node, return_address):
        # Create unique labels for this if block
        end_label = f"endif_{self.if_count}"
        self.if_count += 1

        # Condition
        address = self.visit(node.condition)
        if isinstance(address, list):
            if self.get_highest_type(node.condition) == 'float':
                # Load into $f0
                self.code.append(f"s.s $f0, -{address[0]}($gp)")
                # Convert to integer
                self.code.append("cvt.w.s $f0, $f0")
                # Move to $t0
                self.code.append("mfc1 $t0, $f0")
            else:
                # Load into $t0
                self.code.append(f"lw $t0, -{address[0]}($gp)")
        elif isinstance(address, float):
            # Load into $f0
            self.code.append(f"li.s $f0, {address}")
            # Convert to integer
            self.code.append("cvt.w.s $f0, $f0")
            # Move to $t0
            self.code.append("mfc1 $t0, $f0")
        else:
            # Load into $t0
            self.code.append(f"li $t0, {address}")

        # Check if $t0 is true
        self.code.append(f"beq $t0, $zero, {end_label}")

        # Visit the if block
        for statement in node.body:
            self.visit(statement, return_address)

        # Jump to the end
        self.code.append(f"j {end_label}")

        # End of the if block
        self.code.append(f"{end_label}:")

    def visit_WhileLoopNode(self, node, return_address):
        # Create unique labels for this while loop
        start_label = f"while_{self.while_count}"
        end_label = f"endwhile_{self.while_count}"
        continue_label = f"continue_{self.while_count}"

        # Increment the while loop count for the next loop
        self.while_count += 1

        # Start of the while loop
        self.code.append(f"{start_label}:")

        # Condition
        address = self.visit(node.condition)
        if isinstance(address, list):
            if self.get_highest_type(node.condition) == 'float':
                # Load into $f0
                self.code.append(f"s.s $f0, -{address[0]}($gp)")
                # Convert to integer
                self.code.append("cvt.w.s $f0, $f0")
                # Move to $t0
                self.code.append("mfc1 $t0, $f0")
            else:
                # Load into $t0
                self.code.append(f"lw $t0, -{address[0]}($gp)")
        elif isinstance(address, float):
            # Load into $f0
            self.code.append(f"li.s $f0, {address}")
            # Convert to integer
            self.code.append("cvt.w.s $f0, $f0")
            # Move to $t0
            self.code.append("mfc1 $t0, $f0")
        else:
            # Load into $t0
            self.code.append(f"li $t0, {address}")

        # Assume the condition result is in $t0, compare it to zero
        self.code.append(f"beq $t0, $zero, {end_label}")

        # Visit the body of the while loop
        for statement in node.body:
            self.visit(statement, return_address)

        # Label for continue statement to jump to
        self.code.append(f"{continue_label}:")

        # Jump to the start to recheck the condition
        self.code.append(f"j {start_label}")

        # End of the while loop
        self.code.append(f"{end_label}:")

    def visit_BreakNode(self, node):
        # Use the current while_count to jump to the correct endwhile label
        end_label = f"endwhile_{self.while_count - 1}"
        self.code.append(f"j {end_label}")

    def visit_ContinueNode(self, node):
        # Use the current while_count to jump to the correct continue label
        continue_label = f"continue_{self.while_count - 1}"
        self.code.append(f"j {continue_label}")

    def visit_StructNode(self, node):
        struct_name = node.struct_name
        # get all types
        struct_types = []
        for i in node.struct_members:
            if self.get_highest_type(i.type) == 'int':
                struct_types.append('int')
            elif self.get_highest_type(i.type) == 'float':
                struct_types.append('float')
            elif self.get_highest_type(i.type) == 'char':
                struct_types.append('char')

        struct_vars = []
        for i in node.struct_members:
            struct_vars.append(i.lvalue.value)

        # save struct with name and type
        self.structs[struct_name] = [struct_types, struct_vars]

    def visit_StructMemberNode(self, node):
        symbol = self.scope.get_symbol(name=node.struct_var_name)
        index = self.structs[symbol.struct_name][1].index(node.struct_member_name)
        adress = symbol.memAddress + index * 4
        return adress

    @staticmethod
    def visit_IntNode(node):
        return int(node.value)

    @staticmethod
    def visit_CharNode(node):
        return chr(int(node.value))

    @staticmethod
    def visit_FloatNode(node):
        return float(node.value)

    @staticmethod
    def visit_StringNode(node):
        return node.value


# PASS

    def visit_TypedefNode(self, node):
        pass