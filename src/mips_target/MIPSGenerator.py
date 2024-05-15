import struct

from src.parser.AST import *
from src.parser.SymbolTable import *

unary_ops = {'LogicalNotNode', 'BitwiseNotNode'}
binary_ops = {'DivNode', 'ModNode', 'MultNode', 'MinusNode', 'PlusNode', 'GTNode', 'LTNode', 'GTEQNode', 'LTEQNode',
              'EQNode', 'NEQNode', 'SLNode', 'SRNode', 'BitwiseAndNode', 'BitwiseOrNode', 'BitwiseXorNode',
              'LogicalAndNode', 'LogicalOrNode'}


class MIPSVisitor:
    def __init__(self, stdio=False):
        self.code = []
        self.data = []
        self.scope = SymbolTableTree()
        self.variableAddress = 0
        self.printf_string = 0
        self.scanf_string = 0
        self.enums = {}
        self.structs = {}
        self.break_blocks = []
        self.continue_blocks = []

    def __setattr__(self, name, value):
        if name == "variableAddress":
            self.__dict__["temporaryAddress"] = value
        self.__dict__[name] = value

    def visit(self, node):
        method_name = "visit_" + node.__class__.__name__
        _visitor = getattr(self, method_name, self.generic_visit)
        if node.__class__.__name__ in binary_ops:
            return self.visit_BinaryOp(node, _visitor)
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
        for child in node.children:
            self.visit(child)

    def visit_FunctionNode(self, node):
        self.scope.open_scope()
        self.code.append(f"{node.value}:")
        self.code.append(f"li $sp, 0x7ffffffc")
        for statement in node.body:
            self.code.append(f"# {statement.original}")
            self.visit(statement)
        self.scope.close_scope()

    def visit_ReturnNode(self, node):
        if isinstance(node.return_value, IntNode):
            self.code.append(f"li $v0, {int(node.return_value.value)}")
        elif isinstance(node.return_value, FloatNode):
            self.code.append(f"li $v0, {hex(struct.unpack('<I', struct.pack('<f', float(node.return_value.value)))[0])}")
        elif isinstance(node.return_value, CharNode):
            self.code.append(f"li $v0, {chr(node.return_value.value)}")
        elif isinstance(node.return_value, IdentifierNode):
            # TODO handle return value when it is an identifier
            ...

        self.code.append(f"jr $ra")

    def visit_DeclarationNode(self, node):
        var_type = self.get_highest_type(node.type[len(node.type) - 1])
        symbol = Symbol(node.lvalue.value, var_type, 'variable')
        symbol.memAddress = self.variableAddress
        if var_type == 'float':
            # Store 0 in variable
            self.code.append(f"li.s $f0, 0.0")
            # Save to memory
            self.code.append(f"s.s $f0, -{symbol.memAddress}($gp)")
            # Increment address by 4 bytes
            self.variableAddress += 4
        else:
            # Store 0 in variable
            self.code.append(f"li $t0, 0")
            # Save to memory
            self.code.append(f"sw $t0, -{symbol.memAddress}($gp)")
            # Increment address by 4 bytes
            self.variableAddress += 4

    def visit_DefinitionNode(self, node):
        var_type = self.get_highest_type(node.type[len(node.type) - 1])
        symbol = Symbol(node.lvalue.value, var_type, 'variable')
        symbol.memAddress = self.variableAddress
        rvalue = self.visit(node.rvalue)
        if isinstance(rvalue, str):
            rvalue = ord(rvalue)
        if isinstance(rvalue, int):
            # Load int
            self.code.append(f"li $t0, {rvalue}")
            if symbol.type == 'float':
                # Move to $f0
                self.code.append(f"mtc1 $t0, $f0")
                # Convert to float
                self.code.append(f"cvt.s.w $f0, $f0")
                # Save to memory
                self.code.append(f"s.s $f0, -{symbol.memAddress}($gp)")
                # Increment address by 4 bytes
                self.variableAddress += 4
            else:
                # Save to memory
                self.code.append(f"sw $t0, -{symbol.memAddress}($gp)")
                # Increment address by 4 bytes
                self.variableAddress += 4
        elif isinstance(rvalue, float):
            # Load float
            self.code.append(f"li.s $f0, {rvalue}")
            if symbol.type == 'int' or symbol.type == 'char':
                # Convert to int
                self.code.append("cvt.w.s $f0, $f0")
                # Move
                self.code.append("mfc1 $t0, $f0")
                # Save to memory
                self.code.append(f"sw $t0, -{symbol.memAddress}($gp)")
            else:
                # Save to memory
                self.code.append(f"s.s $f0, -{symbol.memAddress}($gp)")
            # Increment address by 4 bytes
            self.variableAddress += 4
        elif isinstance(rvalue, list):
            address = rvalue[0]
            if var_type == 'char' or var_type == 'int':
                if self.get_highest_type(node.rvalue) == 'float':
                    # Load as float
                    self.code.append(f"l.s $f0, -{address}($gp)")
                    # Convert to int
                    self.code.append("cvt.w.s $f0, $f0")
                    # Move
                    self.code.append("mfc1 $t0, $f0")
                else:
                    # Load as int
                    self.code.append(f"lw $t0, -{address}($gp)")
                # Save to memory
                self.code.append(f"sw $t0, -{symbol.memAddress}($gp)")
                # Increment address by 4 bytes
                self.variableAddress += 4
            elif var_type == 'float':
                if self.get_highest_type(node.rvalue) != 'float':
                    # Load as int
                    self.code.append(f"lw $t0, -{address}($gp)")
                    # Move to $f0
                    self.code.append("mtc1 $t0, $f0")
                    # Convert to float
                    self.code.append("cvt.s.w $f0, $f0")
                else:
                    # Load as float
                    self.code.append(f"l.s $f0, -{address}($gp)")
                # Save to memory
                self.code.append(f"s.s $f0, -{symbol.memAddress}($gp)")
                # Increment address by 4 bytes
                self.variableAddress += 4

        if self.scope.get_symbol(name=node.lvalue.value) is None:
            self.scope.add_symbol(symbol)

    def visit_ArrayDefinitionNode(self, node):
        var_type = node.type.value
        symbol = Symbol(node.lvalue.value, var_type, 'array')
        symbol.memAddress = self.variableAddress
        for i in node.rvalue.array:
            if var_type == 'float':
                # Store 0 in variable
                self.code.append(f"li.s $f0, 0.0")
                # Save to memory
                self.code.append(f"s.s $f0, -{symbol.memAddress}($gp)")
                # Increment address by 4 bytes
                self.variableAddress += 4
            else:
                # Store value in memory
                self.code.append(f"li $t0, {self.visit(i)}")
                # Save to memory
                self.code.append(f"sw $t0, -{symbol.memAddress}($gp)")
                # Increment address by 4 bytes
                self.variableAddress += 4


    def visit_AssignmentNode(self, node):
        if isinstance(node.lvalue, IdentifierNode):
            symbol = self.scope.lookup(name=node.lvalue.value)
            if symbol is not None:
                rvalue = self.visit(node.rvalue)
                var_type = self.get_highest_type(symbol.type)
                if isinstance(rvalue, str):
                    rvalue = ord(rvalue)
                if isinstance(rvalue, int):
                    # Load int
                    self.code.append(f"li $t0, {rvalue}")
                    if symbol.type == 'float':
                        # Move to $f0
                        self.code.append(f"mtc1 $t0, $f0")
                        # Convert to float
                        self.code.append(f"cvt.s.w $f0, $f0")
                        # Save to memory
                        self.code.append(f"s.s $f0, -{symbol.memAddress}($gp)")
                        # Increment address by 4 bytes
                        self.variableAddress += 4
                    else:
                        # Save to memory
                        self.code.append(f"sw $t0, -{symbol.memAddress}($gp)")
                        # Increment address by 4 bytes
                        self.variableAddress += 4
                elif isinstance(rvalue, float):
                    # Load float
                    self.code.append(f"li.s $f0, {rvalue}")
                    if symbol.type == 'int' or symbol.type == 'char':
                        # Convert to int
                        self.code.append("cvt.w.s $f0, $f0")
                        # Move
                        self.code.append("mfc1 $t0, $f0")
                        # Save to memory
                        self.code.append(f"sw $t0, -{symbol.memAddress}($gp)")
                    else:
                        # Save to memory
                        self.code.append(f"s.s $f0, -{symbol.memAddress}($gp)")
                    # Increment address by 4 bytes
                    self.variableAddress += 4
                elif isinstance(rvalue, list):
                    address = rvalue[0]
                    if var_type == 'char' or var_type == 'int':
                        if self.get_highest_type(node.rvalue) == 'float':
                            # Load as float
                            self.code.append(f"l.s $f0, -{address}($gp)")
                            # Convert to int
                            self.code.append("cvt.w.s $f0, $f0")
                            # Move
                            self.code.append("mfc1 $t0, $f0")
                        else:
                            # Load as int
                            self.code.append(f"lw $t0, -{address}($gp)")
                        # Save to memory
                        self.code.append(f"sw $t0, -{symbol.memAddress}($gp)")
                        # Increment address by 4 bytes
                        self.variableAddress += 4
                    elif var_type == 'float':
                        if self.get_highest_type(node.rvalue) != 'float':
                            # Load as int
                            self.code.append(f"lw $t0, -{address}($gp)")
                            # Move to $f0
                            self.code.append("mtc1 $t0, $f0")
                            # Convert to float
                            self.code.append("cvt.s.w $f0, $f0")
                        else:
                            # Load as float
                            self.code.append(f"l.s $f0, -{address}($gp)")
                        # Save to memory
                        self.code.append(f"s.s $f0, -{symbol.memAddress}($gp)")
                        # Increment address by 4 bytes
                        self.variableAddress += 4

    def visit_IdentifierNode(self, node):
        symbol = self.scope.lookup(name=node.value)
        if symbol is not None:
            return [symbol.memAddress]

    def visit_PrintfNode(self, node):
        args = []
        specifiers = node.specifier
        amtSpec = 0
        arguments = []
        i = 0
        while i < len(specifiers):
            if specifiers[i] == '%':
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
            elif isinstance(self.visit(arg), list):
                memAddress = self.visit(arg)[0]
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
            elif isinstance(self.visit(arg), str):
                self.data.append(f"printf_string_{self.printf_string}: .asciiz {self.visit(arg)}")
                self.code.append("li $v0, 4")
                self.code.append(f"la $a0, printf_string_{self.printf_string}")
                self.code.append("syscall")
                self.printf_string += 1
            elif isinstance(self.visit(arg), int):
                self.code.append("li $v0, 1")
                self.code.append(f"li $a0, {self.visit(arg)}")
                self.code.append("syscall")
            elif isinstance(self.visit(arg), float):
                self.code.append("li $v0, 2")
                self.code.append(f"li $t0, {hex(struct.unpack('<I', struct.pack('<f', self.visit(arg)))[0])}")
                self.code.append("mtc1 $t0, $f12")
                self.code.append("syscall")
            else:
                register = self.visit(arg)[0]
                if self.get_highest_type(arg) == 'char':
                    self.code.append(f"li $v0, 11")
                    self.code.append(f"move $a0, {register}")
                    self.code.append(f"syscall")
                elif self.get_highest_type(arg) == 'int':
                    self.code.append(f"li $v0, 1")
                    self.code.append(f"move $a0, {register}")
                    self.code.append(f"syscall")
                elif self.get_highest_type(arg) == 'float':
                    self.code.append(f"li $v0, 2")
                    self.code.append(f"mov.s $f12, {register}")
                    self.code.append(f"syscall")

    def visit_PreFixNode(self, node):
        symbol = self.scope.lookup(name=node.value.value)
        if node.op == 'inc':
            self.code.append(f"addi $t{symbol.int_reg}, $t{symbol.int_reg}, 1")
        elif node.op == 'dec':
            self.code.append(f"addi $t{symbol.int_reg}, $t{symbol.int_reg}, -1")

    def visit_PostFixNode(self, node):
        symbol = self.scope.lookup(name=node.value.value)
        # fix to post
        if node.op == 'inc':
            self.code.append(f"addi $t{symbol.int_reg}, $t{symbol.int_reg}, 1")
        elif node.op == 'dec':
            self.code.append(f"addi $t{symbol.int_reg}, $t{symbol.int_reg}, -1")

    def visit_ScopeNode(self, node):
        self.scope.open_scope()
        for statement in node.children:
            self.visit(statement)
        self.scope.close_scope()

    def visit_EnumNode(self, node):
        self.enums[node.enum_name] = node.enum_list

    # def visit_ScanfNode(self, node):
    #    ...
    #
    # def visit_FunctionCallNode(self, node):
    #    ...
    #
    # def visit_ArrayDefinitionNode(self, node):
    #    ...
    #
    # def visit_StructDefinitionNode(self, node):
    #    ...
    #
    # def visit_DeclarationNode(self, node):
    #    ...
    #
    # def visit_ArrayDeclarationNode(self, node):
    #    ...
    #
    # def visit_StructDeclarationNode(self, node):
    #    ...
    #
    # def visit_ArrayAssignmentNode(self, node):
    #    ...
    #
    # def visit_StructAssignmentNode(self, node):
    #    ...
    #

    # def visit_StringNode(self, node):
    #    ...

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
        elif isinstance(left, str) or isinstance(left, int):
            if isinstance(left, str):
                left = ord(left)
            # Load the value as an int
            self.code.append(f"li $t0, {left}")
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
        elif isinstance(right, str) or isinstance(right, int):
            if isinstance(right, str):
                right = ord(right)
            # Load the value as an int
            self.code.append(f"li $t1, {right}")
        elif isinstance(right, float):
            # Load the value as a float
            self.code.append(f"li.s $f1, {right}")

        return visitor(node)

    def visit_PlusNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Add
        if type1 == 'float' or type2 == 'float':
            self.code.append("add.s $f0, $f0, $f1")
            # Save to temporary address
            self.code.append(f"s.s $f0, -{self.temporaryAddress}($gp)")
        else:
            self.code.append("add $t0, $t0, $t1")
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.temporaryAddress}($gp)")
        # Increment temporary address
        self.temporaryAddress += 4
        # Return temporary address
        return [self.temporaryAddress - 4]

    def visit_MinusNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Subtract
        if type1 == 'float' or type2 == 'float':
            self.code.append("sub.s $f0, $f0, $f1")
            # Save to temporary address
            self.code.append(f"s.s $f0, -{self.temporaryAddress}($gp)")
        else:
            self.code.append("sub $t0, $t0, $t1")
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.temporaryAddress}($gp)")
        # Increment temporary address
        self.temporaryAddress += 4
        # Return temporary address
        return [self.temporaryAddress - 4]

    def visit_MultNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Mul
        if type1 == 'float' or type2 == 'float':
            self.code.append("mul.s $f0, $f0, $f1")
            # Save to temporary address
            self.code.append(f"s.s $f0, -{self.temporaryAddress}($gp)")
        else:
            self.code.append("mul $t0, $t0, $t1")
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.temporaryAddress}($gp)")
        # Increment temporary address
        self.temporaryAddress += 4
        # Return temporary address
        return [self.temporaryAddress - 4]

    def visit_DivNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Div
        if type1 == 'float' or type2 == 'float':
            self.code.append("div.s $f0, $f0, $f1")
            # Save to temporary address
            self.code.append(f"s.s $f0, -{self.temporaryAddress}($gp)")
        else:
            self.code.append("div $t0, $t0, $t1")
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.temporaryAddress}($gp)")
        # Increment temporary address
        self.temporaryAddress += 4
        # Return temporary address
        return [self.temporaryAddress - 4]

    def visit_ModNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Div
        self.code.append("div $t0, $t1")
        # Get remainder
        self.code.append("mfhi $t2")
        # Save to temporary address
        self.code.append(f"sw $t2, -{self.temporaryAddress}($gp)")
        # Increment temporary address
        self.temporaryAddress += 4
        # Return temporary address
        return [self.temporaryAddress - 4]

    def visit_BitwiseAndNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # And
        self.code.append("and $t0, $t0, $t1")
        # Save to temporary address
        self.code.append(f"sw $t0, -{self.temporaryAddress}($gp)")
        # Increment temporary address
        self.temporaryAddress += 4
        # Return temporary address
        return [self.temporaryAddress - 4]

    def visit_BitwiseOrNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Or
        self.code.append("or $t0, $t0, $t1")
        # Save to temporary address
        self.code.append(f"sw $t0, -{self.temporaryAddress}($gp)")
        # Increment temporary address
        self.temporaryAddress += 4
        # Return temporary address
        return [self.temporaryAddress - 4]

    def visit_BitwiseXorNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Xor
        self.code.append("xor $t0, $t0, $t1")
        # Save to temporary address
        self.code.append(f"sw $t0, -{self.temporaryAddress}($gp)")
        # Increment temporary address
        self.temporaryAddress += 4
        # Return temporary address
        return [self.temporaryAddress - 4]

    def visit_LogicalAndNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # And
        if type1 == 'float' or type2 == 'float':
            # Load 0 into $f2
            self.code.append("li.s $f2, 0.0")
            # Load 1 into $f3
            self.code.append("li.s $f3, 1.0")
            # Check if $f0 == 0
            self.code.append("c.eq.s $f0, $f2")
            # Put 0.0 in $f4 if c.eq.s returned true
            self.code.append("movt.s $f4, $f2, 1")
            # Put 1.0 in $f4 if c.eq.s returned false
            self.code.append("movf.s $f4, $f3, 1")

            # Check if $f1 == 0
            self.code.append("c.eq.s $f1, $f2")
            # Put 0.0 in $f4 if c.eq.s returned true
            self.code.append("movt.s $f5, $f2, 1")
            # Put 1.0 in $f4 if c.eq.s returned false
            self.code.append("movf.s $f5, $f3, 1")

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
            self.code.append(f"s.s $f0, -{self.temporaryAddress}($gp)")
        else:
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.temporaryAddress}($gp)")
        # Increment temporary address
        self.temporaryAddress += 4
        # Return temporary address
        return [self.temporaryAddress - 4]

    def visit_LogicalOrNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Or
        if type1 == 'float' or type2 == 'float':
            # Load 0 into $f2
            self.code.append("li.s $f2, 0.0")
            # Load 1 into $f3
            self.code.append("li.s $f3, 1.0")
            # Check if $f0 == 0
            self.code.append("c.eq.s $f0, $f2")
            # Put 0.0 in $f4 if c.lt.s returned true
            self.code.append("movt.s $f4, $f2, 1")
            # Put 1.0 in $f4 if c.lt.s returned false
            self.code.append("movf.s $f4, $f3, 1")

            # Check if $f1 == 0
            self.code.append("c.eq.s $f1, $f2")
            # Put 0.0 in $f4 if c.lt.s returned true
            self.code.append("movt.s $f5, $f2, 1")
            # Put 1.0 in $f4 if c.lt.s returned false
            self.code.append("movf.s $f5, $f3, 1")

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
            self.code.append(f"s.s $f0, -{self.temporaryAddress}($gp)")
        else:
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.temporaryAddress}($gp)")
        # Increment temporary address
        self.temporaryAddress += 4
        # Return temporary address
        return [self.temporaryAddress - 4]

    def visit_LogicalNotNode(self, node):
        type1 = self.get_highest_type(node.children[0])

        # Not
        if type1 == 'float':
            # Load 0 into $f1
            self.code.append("li.s $f1, 0.0")
            # Load 1 into $f2
            self.code.append("li.s $f2, 1.0")
            # Check if $f0 == 0
            self.code.append("c.eq.s $f0, $f1")
            # Put 0.0 in $f3 if c.lt.s returned true
            self.code.append("movt.s $f3, $f1, 1")
            # Put 1.0 in $f3 if c.lt.s returned false
            self.code.append("movf.s $f3, $f2, 1")
        else:
            # Check if $t0 is 0
            self.code.append("slt $t1, $t0, $zero")
            self.code.append("slt $t2, $zero, $t0")
            # 0 if $t0 is 0
            self.code.append("or $t0, $t1, $t2")

            # And
            self.code.append("and $t0, $t0, $t1")

        if type1 == 'float':
            # Save to temporary address
            self.code.append(f"s.s $f0, -{self.temporaryAddress}($gp)")
        else:
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.temporaryAddress}($gp)")
        # Increment temporary address
        self.temporaryAddress += 4
        # Return temporary address
        return [self.temporaryAddress - 4]

    def visit_LTNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Less than
        if type1 == 'float' or type2 == 'float':
            # Load 0 into $f2
            self.code.append("li.s $f2, 0.0")
            # Load 1 into $f3
            self.code.append("li.s $f3, 1.0")
            # Check if $f0 < $f1
            self.code.append("c.lt.s $f0, $f1")
            # Put 0.0 in $f0 if c.lt.s returned true
            self.code.append("movt.s $f0, $f3, 1")
            # Put 1.0 in $f0 if c.lt.s returned false
            self.code.append("movf.s $f0, $f2, 1")
        else:
            # Check if $t0 < $t1
            self.code.append("slt $t0, $t0, $t1")

        if type1 == 'float' or type2 == 'float':
            # Save to temporary address
            self.code.append(f"s.s $f0, -{self.temporaryAddress}($gp)")
        else:
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.temporaryAddress}($gp)")
        # Increment temporary address
        self.temporaryAddress += 4
        # Return temporary address
        return [self.temporaryAddress - 4]

    def visit_GTNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Greater than
        if type1 == 'float' or type2 == 'float':
            # Load 0 into $f2
            self.code.append("li.s $f2, 0.0")
            # Load 1 into $f3
            self.code.append("li.s $f3, 1.0")
            # Check if $f1 <= $f0
            self.code.append("c.le.s $f1, $f0")
            # Put 0.0 in $f0 if c.le.s returned true
            self.code.append("movt.s $f0, $f3, 0")
            # Put 1.0 in $f0 if c.le.s returned false
            self.code.append("movf.s $f0, $f2, 0")
        else:
            # Check if $t1 < $t0
            self.code.append("slt $t0, $t1, $t0")


        if type1 == 'float' or type2 == 'float':
            # Save to temporary address
            self.code.append(f"s.s $f0, -{self.temporaryAddress}($gp)")
        else:
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.temporaryAddress}($gp)")
        # Increment temporary address
        self.temporaryAddress += 4
        # Return temporary address
        return [self.temporaryAddress - 4]

    def visit_EQNode(self, node):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])

        # Equals
        if type1 == 'float' or type2 == 'float':
            # Load 0 into $f2
            self.code.append("li.s $f2, 0.0")
            # Load 1 into $f3
            self.code.append("li.s $f3, 1.0")
            # Check if $f0 == $f1
            self.code.append("c.eq.s $f0, $f1")
            # Put 1.0 in $f0 if c.eq.s returned true
            self.code.append("movt.s $f0, $f3, 1")
            # Put 0.0 in $f0 if c.eq.s returned false
            self.code.append("movf.s $f0, $f2, 1")
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
            self.code.append(f"s.s $f0, -{self.temporaryAddress}($gp)")
        else:
            # Save to temporary address
            self.code.append(f"sw $t0, -{self.temporaryAddress}($gp)")
        # Increment temporary address
        self.temporaryAddress += 4
        # Return temporary address
        return [self.temporaryAddress - 4]

    # def visit_LTEQNode(self, node):
    #    ...

    # def visit_GTEQNode(self, node):
    #    ...

    # def visit_EQNode(self, node):
    #    ...

    # def visit_NEQNode(self, node):
    #    ...

    # def visit_IdentifierNode(self, node):
    #    ...

    # def visit_AddrNode(self, node):
    #    ...

    # def visit_DerefNode(self, node):
    #    ...

    # def visit_ExplicitConversionNode(self, node):
    #    ...

    # def visit_TypedefNode(self, node):
    #    pass

    # def visit_IfStatementNode(self, node):
    #    ...

    # def visit_WhileLoopNode(self, node):
    #    ...

    # def visit_BreakNode(self, node):
    #     ...


    def visit_CommentNode(self, node):
        self.code.append(f"#{node.value[2:]}")

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
