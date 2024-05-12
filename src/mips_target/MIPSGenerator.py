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
        self.printf_string = 0
        self.scanf_string = 0
        self.float_reg = 0
        self.int_reg = 0
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
            self.visit(statement)
        self.scope.close_scope()

    def visit_ReturnNode(self, node):
        self.code.append(f"jr $ra")

    def visit_DefinitionNode(self, node):
        symbol = Symbol(node.lvalue.value, self.get_highest_type(node.rvalue), 'variable')
        if self.scope.get_symbol(name=node.lvalue.value) is None:
            self.scope.add_symbol(symbol)

        if symbol.type == 'float':
            self.code.append(f"li.s $f{self.float_reg}, {self.visit(node.rvalue)}")
            symbol.varname = f'$f{self.float_reg}'
            self.float_reg += 1
            return
        if symbol.type == 'int':
            self.code.append(f"li $t{self.int_reg}, {self.visit(node.rvalue)}")
            symbol.varname = f'$t{self.int_reg}'
            self.int_reg += 1
            return
        if symbol.type == 'char':
            self.code.append(f"li $t{self.int_reg}, {ord(self.visit(node.rvalue))}")
            symbol.varname = f'$t{self.int_reg}'
            self.int_reg += 1
            return

    def visit_AssignmentNode(self, node):
        # Assuming only integer assignments for simplicity
        self.code.append(f"li $t0, {node.rvalue.value}")
        self.code.append(f"sw $t0, {node.lvalue.value}")

    def visit_IdentifierNode(self, node):
        symbol = self.scope.lookup(name=node.value)
        if symbol is not None:
            return [symbol.varname]

    def visit_PlusNode(self, node):
        # Assuming only integer addition for simplicity
        self.code.append(f"add $t0, {node.children[0].value}, {node.children[1].value}")

    def visit_PrintfNode(self, node):
        args = []
        specifiers = node.specifier
        amtSpec = 0
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
            elif isinstance(self.visit(arg), str):
                self.data.append(f"printf_string_{self.printf_string}: .asciiz {self.visit(arg)}")
                self.code.append(f"li $v0, 4")
                self.code.append(f"la $a0, printf_string_{self.printf_string}")
                self.code.append(f"syscall")
                self.printf_string += 1
            elif isinstance(self.visit(arg), int):
                self.code.append(f"li $v0, 1")
                self.code.append(f"li $a0, {self.visit(arg)}")
                self.code.append(f"syscall")
            elif isinstance(self.visit(arg), float):
                self.code.append(f"li $v0, 2")
                self.code.append(f"li $t0, {hex(struct.unpack('<I', struct.pack('<f', self.visit(arg)))[0])}")
                self.code.append(f"mtc1 $t0, $f12")
                self.code.append(f"syscall")
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

    # def visit_ScanfNode(self, node):
    #    ...
    #
    # def visit_FunctionCallNode(self, node):
    #    ...
    #
    # def visit_DefinitionNode(self, node):
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
    # def visit_PostFixNode(self, node):
    #    ...
    #
    # def visit_PreFixNode(self, node):
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
