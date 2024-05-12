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

    def visit(self, node):
        method_name = "visit_" + node.__class__.__name__
        _visitor = getattr(self, method_name, self.generic_visit)
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
            self.code.append(f"s.s $f0, -{symbol.memAddress}($sp)")
            # Increment address by 4 bytes
            self.variableAddress += 4
        else:
            # Store 0 in variable
            self.code.append(f"li $t0, 0")
            # Save to memory
            self.code.append(f"sw $t0, -{symbol.memAddress}($sp)")
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
                self.code.append(f"s.s $f0, -{symbol.memAddress}($sp)")
                # Increment address by 4 bytes
                self.variableAddress += 4
            else:
                # Save to memory
                self.code.append(f"sw $t0, -{symbol.memAddress}($sp)")
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
                self.code.append(f"sw $t0, -{symbol.memAddress}($sp)")
            else:
                # Save to memory
                self.code.append(f"s.s $f0, -{symbol.memAddress}($sp)")
            # Increment address by 4 bytes
            self.variableAddress += 4
        elif isinstance(rvalue, list):
            address = rvalue[0]
            if var_type == 'char' or var_type == 'int':
                if self.get_highest_type(node.rvalue) == 'float':
                    # Load as float
                    self.code.append(f"l.s $f0, -{address}($sp)")
                    # Convert to int
                    self.code.append("cvt.w.s $f0, $f0")
                    # Move
                    self.code.append("mfc1 $t0, $f0")
                else:
                    # Load as int
                    self.code.append(f"lw $t0, -{address}($sp)")
                # Save to memory
                self.code.append(f"sw $t0, -{symbol.memAddress}($sp)")
                # Increment address by 4 bytes
                self.variableAddress += 4
            elif var_type == 'float':
                if self.get_highest_type(node.rvalue) != 'float':
                    # Load as int
                    self.code.append(f"lw $t0, -{address}($sp)")
                    # Move to $f0
                    self.code.append("mtc1 $t0, $f0")
                    # Convert to float
                    self.code.append("cvt.s.w $f0, $f0")
                else:
                    # Load as float
                    self.code.append(f"l.s $f0, -{address}($sp)")
                # Save to memory
                self.code.append(f"s.s $f0, -{symbol.memAddress}($sp)")
                # Increment address by 4 bytes
                self.variableAddress += 4

        if self.scope.get_symbol(name=node.lvalue.value) is None:
            self.scope.add_symbol(symbol)

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
                        self.code.append(f"s.s $f0, -{symbol.memAddress}($sp)")
                        # Increment address by 4 bytes
                        self.variableAddress += 4
                    else:
                        # Save to memory
                        self.code.append(f"sw $t0, -{symbol.memAddress}($sp)")
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
                        self.code.append(f"sw $t0, -{symbol.memAddress}($sp)")
                    else:
                        # Save to memory
                        self.code.append(f"s.s $f0, -{symbol.memAddress}($sp)")
                    # Increment address by 4 bytes
                    self.variableAddress += 4
                elif isinstance(rvalue, list):
                    address = rvalue[0]
                    if var_type == 'char' or var_type == 'int':
                        if self.get_highest_type(node.rvalue) == 'float':
                            # Load as float
                            self.code.append(f"l.s $f0, -{address}($sp)")
                            # Convert to int
                            self.code.append("cvt.w.s $f0, $f0")
                            # Move
                            self.code.append("mfc1 $t0, $f0")
                        else:
                            # Load as int
                            self.code.append(f"lw $t0, -{address}($sp)")
                        # Save to memory
                        self.code.append(f"sw $t0, -{symbol.memAddress}($sp)")
                        # Increment address by 4 bytes
                        self.variableAddress += 4
                    elif var_type == 'float':
                        if self.get_highest_type(node.rvalue) != 'float':
                            # Load as int
                            self.code.append(f"lw $t0, -{address}($sp)")
                            # Move to $f0
                            self.code.append("mtc1 $t0, $f0")
                            # Convert to float
                            self.code.append("cvt.s.w $f0, $f0")
                        else:
                            # Load as float
                            self.code.append(f"l.s $f0, -{address}($sp)")
                        # Save to memory
                        self.code.append(f"s.s $f0, -{symbol.memAddress}($sp)")
                        # Increment address by 4 bytes
                        self.variableAddress += 4

    def visit_IdentifierNode(self, node):
        symbol = self.scope.lookup(name=node.value)
        if symbol is not None:
            return [symbol.memAddress]

    def visit_PlusNode(self, node):
        # Assuming only integer addition for simplicity
        self.code.append(f"add $t0, {node.children[0].value}, {node.children[1].value}")

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
                    self.code.append(f"lw $t0, -{memAddress}($sp)")
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
                    self.code.append(f"l.s $f0, -{memAddress}($sp)")
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

    # def visit_UnaryOp(self, node):
    #    ...

    # def visit_BinaryOp(self, node, method):
    #    ...

    # def visit_MinusNode(self, node, children=[]):
    #    ...

    # def visit_MultNode(self, node, children=[]):
    #    ...

    # def visit_DivNode(self, node, children=[]):
    #    ...

    # def visit_ModNode(self, node, children=[]):
    #    ...

    # def visit_BitwiseAndNode(self, node, children=[]):
    #    ...

    # def visit_BitwiseOrNode(self, node, children=[]):
    #    ...

    # def visit_BitwiseXorNode(self, node, children=[]):
    #    ...

    # def visit_LogicalAndNode(self, node, children=[]):
    #    ...

    # def visit_LogicalOrNode(self, node, children=[]):
    #    ...

    # def visit_SRNode(self, node, children=[]):
    #    ...


    # def visit_SLNode(self, node, children=[]):
    #    ...

    # def visit_LTNode(self, node, children=[]):
    #    ...

    # def visit_GTNode(self, node, children=[]):
    #    ...

    # def visit_LTEQNode(self, node, children=[]):
    #    ...

    # def visit_GTEQNode(self, node, children=[]):
    #    ...

    # def visit_EQNode(self, node, children=[]):
    #    ...

    # def visit_NEQNode(self, node, children=[]):
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
