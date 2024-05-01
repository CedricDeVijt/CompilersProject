import platform

from llvmlite import ir

from src.parser.AST import *
from src.parser.SymbolTable import *

unary_ops = {'LogicalNotNode', 'BitwiseNotNode'}
binary_ops = {'DivNode', 'ModNode', 'MultNode', 'MinusNode', 'PlusNode', 'GTNode', 'LTNode', 'GTEQNode', 'LTEQNode', 'EQNode', 'NEQNode', 'SLNode', 'SRNode', 'BitwiseAndNode', 'BitwiseOrNode', 'BitwiseXorNode', 'LogicalAndNode', 'LogicalOrNode'}


class LLVMVisitor:
    def __init__(self, stdio=False):
        self.builder = None
        self.scope = SymbolTableTree()
        self.module = ir.Module()
        self.module.triple = f"{platform.machine()}-pc-{platform.system().lower()}"
        self.printf_string = 0
        self.enums = {}
        self.break_blocks = []  # Stack to keep track of the nearest loop end block

        # Add printf and scanf function
        if stdio:
            function_type = ir.FunctionType(ir.IntType(32), [ir.PointerType(ir.IntType(8))], var_arg=True)
            function = ir.Function(self.module, function_type, name='printf')

            self.builder = function

    def get_highest_type(self, rval):
        type_check_dict = {
            DerefNode: lambda rval: self.lookup_and_get_type(rval.identifier.value),
            IdentifierNode: lambda rval: self.lookup_and_get_type(rval.value),
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
        symbols = self.scope.lookup(identifier)
        if symbols:
            if isinstance(symbols.type, str):
                return symbols.type
            if isinstance(symbols.type, PointerNode):
                if isinstance(symbols.type.type, list):
                    return symbols.type.type[len(symbols.type.type) - 1].value
                return symbols.type.type.value
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

                similar = all(self.get_highest_type(param[0]) == self.get_highest_type(arg) for param, arg in zip(symbol.params, rval.arguments))
                if similar:
                    return self.get_highest_type(symbol.type)
        return 'char'

    def visit(self, node):
        if node.__class__.__name__ in unary_ops:
            return self.visit_UnaryOp(node)
        if node.__class__.__name__ in binary_ops:
            return self.visit_BinaryOp(node, f"visit_{node.__class__.__name__}")
        method_name = "visit_" + node.__class__.__name__
        _visitor = getattr(self, method_name, self.generic_visit)
        return _visitor(node)

    def generic_visit(self, node):
        raise Exception(f"No visit_{node.__class__.__name__} method defined")

    @staticmethod
    def create_entry_block_allocation(function, var_name):
        builder = ir.IRBuilder(function.append_basic_block(name="entry"))
        return builder.alloca(ir.IntType(32), name=var_name)

    def visit_ProgramNode(self, node):
        for child in node.children:
            self.visit(child)

    def visit_PrintfNode(self, node):
        specifier = node.specifier
        specifier += '\00'
        j = 0
        while j < len(specifier) - 1:
            if specifier[j] == '\\':
                next_symbol = specifier[j + 1]
                if next_symbol == '\\':
                    specifier = specifier[:j] + '\\' + specifier[j + 2:]
                elif next_symbol == 'n':
                    specifier = specifier[:j] + '\n' + specifier[j + 2:]
                elif next_symbol == 't':
                    specifier = specifier[:j] + '\t' + specifier[j + 2:]
                elif next_symbol == '\'':
                    specifier = specifier[:j] + '\'' + specifier[j + 2:]
                elif next_symbol == '\"':
                    specifier = specifier[:j] + '\"' + specifier[j + 2:]
            j += 1
        # Create Global Variable For Format String.
        c_string_type = ir.ArrayType(ir.IntType(8), len(specifier))
        format_string_global = ir.GlobalVariable(self.module, c_string_type, name=f'printf_string_{self.printf_string}')
        format_string_global.global_constant = True
        format_string_global.initializer = ir.Constant(c_string_type, bytearray(specifier, 'utf8'))
        self.printf_string += 1

        # Call Printf Function.
        args = [self.builder.bitcast(format_string_global, ir.PointerType(ir.IntType(8)))]
        for arg in node.children:
            if isinstance(arg, StringNode):
                self.printf_string += 1
            arg = self.visit(arg)
            if arg.type == ir.FloatType():
                # Convert to double
                arg = self.builder.fpext(arg, ir.DoubleType())
            args.append(arg)
        self.builder.call(self.module.get_global('printf'), args)
        self.printf_string += 1

    def visit_FunctionNode(self, node):
        # Open new scope.
        self.scope.open_scope()
        # Add params
        for param in node.params:
            param_type = param[0]
            param_name = param[1]
            const = False
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
            symbol = Symbol(name=param_name, var_type=param_type, const=const, symbol_type='variable', defined=True,
                            params=None)
            #symbol.alloca =
            symbol = Symbol(name=param_name, var_type=param_type, const=const, symbol_type='variable', defined=True, params=None)
            symbols = self.scope.get_symbol(name=param_name)
            if not symbols:
                self.scope.add_symbol(symbol)
        # Arguments.
        args = []
        for param in node.params:
            if isinstance(param, list):
                param_type = param[len(param) - 2]
                if isinstance(param_type, TypeNode):
                    if param_type.value == 'char':
                        args.append(ir.IntType(8))
                    elif param_type.value == 'int':
                        args.append(ir.IntType(32))
                    elif param_type.value == 'float':
                        args.append(ir.FloatType())
                    elif param_type.value == 'void':
                        args.append(ir.VoidType())
                elif isinstance(param_type, PointerNode):
                    ...
        # Function type.
        function_type = ir.FunctionType(ir.VoidType(), args)
        func_type = node.type
        if isinstance(func_type, list):
            func_type = func_type[len(func_type) - 1]
        if isinstance(func_type, TypeNode):
            if func_type.value == 'char':
                function_type = ir.FunctionType(ir.IntType(8), args)
            elif func_type.value == 'int':
                function_type = ir.FunctionType(ir.IntType(32), args)
            elif func_type.value == 'float':
                function_type = ir.FunctionType(ir.FloatType(), args)
            elif func_type.value == 'void':
                function_type = ir.FunctionType(ir.VoidType(), args)
        elif isinstance(func_type, PointerNode):
            ...
        function = ir.Function(self.module, function_type, name=node.value)


        entry_block = function.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(entry_block)

        # Visit function body
        for statement in node.body:
            self.builder.comment(statement.original.replace('\n', ''))
            self.visit(statement)

        # Close scope.
        self.scope.close_scope()

    def visit_FunctionCallNode(self, node):
        args = []
        for arg in node.arguments:
            args.append(self.visit(arg))
        return self.builder.call(self.module.get_global(node.value), args)

    def visit_ifStatementNode(self, node):
        # open scope
        self.scope.open_scope()
        # close scope
        self.scope.close_scope()

    def visit_DefinitionNode(self, node):
        # definition vars
        var_name = node.lvalue.value
        rvalue = self.visit(node.rvalue)
        enum = False
        if isinstance(node.type, list):
            var_type = self.get_highest_type(node.type[len(node.type) - 1])
            symbol = Symbol(name=var_name, var_type=node.type[len(node.type) - 1])
        else:
            var_type = 'int'
            symbol = Symbol(name=var_name, var_type=var_type)
            enum = True
        if not enum and isinstance(node.type[0], PointerNode):
            if var_type == 'float':
                rvalue = self.builder.inttoptr(rvalue, ir.PointerType(ir.FloatType))
            elif var_type == 'int':
                rvalue = self.builder.inttoptr(rvalue, ir.PointerType(ir.IntType(32)))
            elif var_type == 'char':
                rvalue = self.builder.inttoptr(rvalue, ir.PointerType(ir.IntType(8)))
            var_ptr = self.builder.alloca(rvalue.type)
            symbol.alloca = var_ptr
            if self.scope.get_symbol(name=var_name) is None:
                self.scope.add_symbol(symbol)
            return self.builder.store(rvalue, var_ptr)
        # Not a Pointer
        if not enum and rvalue.type != ir.FloatType() and var_type == 'float':
            if rvalue.type == ir.IntType(8):
                rvalue = self.builder.fptosi(rvalue, ir.IntType(32))
            rvalue = self.builder.sitofp(rvalue, ir.FloatType())
        elif rvalue.type != ir.IntType(32) and var_type == 'int':
            if rvalue.type == ir.FloatType():
                rvalue = self.builder.fptosi(rvalue, ir.IntType(32))
            else:
                rvalue = self.builder.sext(rvalue, ir.IntType(32))
        elif rvalue.type != ir.IntType(8) and var_type == 'char':
            if rvalue.type == ir.FloatType():
                rvalue = self.builder.fptosi(rvalue, ir.IntType(32))
            rvalue = self.builder.trunc(rvalue, ir.IntType(8))

        var_ptr = self.builder.alloca(rvalue.type)
        symbol.alloca = var_ptr
        if self.scope.get_symbol(name=var_name) is None:
            self.scope.add_symbol(symbol)
        return self.builder.store(rvalue, var_ptr)

    def visit_DeclarationNode(self, node):
        # Get the type and name of the variable being declared
        var_name = node.lvalue.value
        var_type = self.get_highest_type(node.type[len(node.type) - 1])
        if isinstance(node.type[0], PointerNode):
            if var_type == 'float':
                value = ir.Constant(ir.PointerType(ir.FloatType()), None)
            elif var_type == 'int':
                value = ir.Constant(ir.PointerType(ir.IntType(32)), None)
            elif var_type == 'char':
                value = ir.Constant(ir.PointerType(ir.IntType(8)), None)
        elif var_type == 'float':
            value = ir.Constant(ir.FloatType(), 0)
        elif var_type == 'int':
            value = ir.Constant(ir.IntType(32), 0)
        elif var_type == 'char':
            value = ir.Constant(ir.IntType(8), 0)
        var_ptr = self.builder.alloca(value.type)
        self.builder.store(value, var_ptr)
        # Add to symbol table
        symbol = Symbol(name=var_name, var_type=node.type[len(node.type) - 1])
        symbol.alloca = var_ptr
        symbol.pointer = False
        if isinstance(node.type[len(node.type) - 1], PointerNode):
            symbol.pointer = True
        if self.scope.get_symbol(name=var_name) is None:
            self.scope.add_symbol(symbol)
        return var_ptr

    def visit_AssignmentNode(self, node):
        var_name = node.lvalue
        if isinstance(var_name, IdentifierNode):
            var_name = var_name.value
        elif isinstance(var_name, DerefNode):
            var_name = var_name.identifier.value
        symbol = self.scope.lookup(name=var_name)
        var_type = self.get_highest_type(symbol.type)
        value = self.visit(node.rvalue)
        # Pointer
        if isinstance(symbol.type, PointerNode):
            pointer = self.builder.inttoptr(value, symbol.alloca.type)
            loaded = self.builder.load(pointer)
            return self.builder.store(loaded, symbol.alloca)
        # Convert value if needed.
        if value.type != ir.FloatType() and var_type == 'float':
            if value.type == ir.IntType(8):
                value = self.builder.fptosi(value, ir.IntType(32))
            value = self.builder.sitofp(value, ir.FloatType())
        elif value.type != ir.IntType(32) and var_type == 'int':
            if value.type == ir.FloatType():
                value = self.builder.fptosi(value, ir.IntType(32))
            else:
                value = self.builder.sext(value, ir.IntType(32))
        elif value.type != ir.IntType(8) and var_type == 'char':
            if value.type == ir.FloatType():
                value = self.builder.fptosi(value, ir.IntType(32))
            value = self.builder.trunc(value, ir.IntType(8))
        symbol = self.scope.lookup(name=var_name)
        self.builder.store(value, symbol.alloca)

    def visit_PostFixNode(self, node):
        symbol = self.scope.lookup(name=node.value)
        if isinstance(symbol, Symbol):
            value = 1
            if node.op == 'dec':
                value = -1
            # Pointer
            if isinstance(symbol.type, PointerNode):
                index = ir.Constant(ir.IntType(64), value)
                address = self.builder.ptrtoint(symbol.alloca, ir.IntType(64))
                address = self.builder.add(address, index)
                pointer = self.builder.inttoptr(address, symbol.alloca.type)
                loaded = self.builder.load(pointer)
                return self.builder.store(loaded, symbol.alloca)
            # Do operation
            var_type = self.get_highest_type(symbol.type)
            original = self.builder.load(symbol.alloca)
            if var_type == 'float':
                value = self.builder.fadd(original, ir.Constant(ir.FloatType(), value))
            elif var_type == 'int':
                value = self.builder.add(original, ir.Constant(ir.IntType(32), value))
            else:
                value = self.builder.add(original, ir.Constant(ir.IntType(8), value))
            self.builder.store(value, symbol.alloca)
            return original

    def visit_PreFixNode(self, node):
        symbol = self.scope.lookup(name=node.value)
        if isinstance(symbol, Symbol):
            value = 1
            if node.op == 'dec':
                value = -1
            # Pointer
            if isinstance(symbol.type, PointerNode):
                index = ir.Constant(ir.IntType(8), value)
                loaded = self.builder.load(symbol.alloca)
                gep = self.builder.gep(loaded, [index])
                return self.builder.store(gep, symbol.alloca)
            # Do operation
            var_type = self.get_highest_type(symbol.type)
            original = self.builder.load(symbol.alloca)
            if var_type == 'float':
                value = self.builder.fadd(original, ir.Constant(ir.FloatType(), value))
            elif var_type == 'int':
                value = self.builder.add(original, ir.Constant(ir.IntType(32), value))
            else:
                value = self.builder.add(original, ir.Constant(ir.IntType(8), value))
            self.builder.store(value, symbol.alloca)
            return self.builder.load(symbol.alloca)

    def convert(self, var_type, node):    # var_type = cType in string: 'int'    value = value: 10)
        if var_type == "int":
            if isinstance(node, IntNode):
                return ir.Constant(ir.IntType(32), node.value)
            elif isinstance(node, FloatNode):
                return ir.Constant(ir.IntType(32), int(float(node.value)))
            elif isinstance(node, CharNode):
                return ir.Constant(ir.IntType(32), node.value)
        elif var_type == "float":
            if isinstance(node, IntNode):
                return ir.Constant(ir.FloatType(), float(node.value))
            elif isinstance(node, FloatNode):
                return ir.Constant(ir.FloatType(), float(node.value))
            elif isinstance(node, CharNode):
                return ir.Constant(ir.FloatType(), float(ord(node.value)))
        elif var_type == "char":
            if isinstance(node, IntNode):
                return ir.Constant(ir.IntType(8), node.value)
            elif isinstance(node, FloatNode):
                return ir.Constant(ir.IntType(8), float(node.value))
            elif isinstance(node, CharNode):
                return ir.Constant(ir.IntType(8), node.value)
        return self.visit(node)

    def convertLLVMtype(self, ast_type, value, pointer=False):
        if value.type == ir.IntType(64):
            return value
        if pointer:
            if value.type == ir.FloatType():
                val = self.builder.fptosi(value, ir.IntType(64))
            else:
                val = self.builder.sext(value, ir.IntType(64))
            bytes_size = 0
            if ast_type == 'float':
                bytes_size = 8
            elif ast_type == 'int':
                bytes_size = 4
            elif ast_type == 'char':
                bytes_size = 1
            val = self.builder.mul(val, ir.Constant(ir.IntType(64), bytes_size))
            return val
        if ast_type == "int":
            if value.type == ir.IntType(32):
                return value
            elif value.type == ir.FloatType():
                return self.builder.fptosi(value, ir.IntType(32))
            elif value.type == ir.IntType(8):
                return self.builder.sext(value, ir.IntType(32))
        elif ast_type == "float":
            if value.type == ir.IntType(32):
                return self.builder.sitofp(value, ir.FloatType())
            elif value.type == ir.FloatType():
                return value
            elif value.type == ir.IntType(8):
                return self.builder.sitofp(value, ir.FloatType())
        elif ast_type == "char":
            if value.type == ir.IntType(32):
                return self.builder.trunc(value, ir.IntType(8))
            elif value.type == ir.FloatType():
                return self.builder.trunc(self.builder.fptosi(value, ir.IntType(32)), ir.IntType(8))
            elif value.type == ir.IntType(8):
                return value

    def visit_ReturnNode(self, node):
        if node.return_value is not None:
            value = self.visit(node.return_value)
            self.builder.ret(value)
        else:
            self.builder.ret_void()

    def visit_IntNode(self, node):
        return ir.Constant(ir.IntType(32), int(node.value))

    def visit_CharNode(self, node):
        return ir.Constant(ir.IntType(8), node.value)

    def visit_FloatNode(self, node):
        return ir.Constant(ir.FloatType(), float(node.value))

    def visit_StringNode(self, node):
        c_string_type = ir.ArrayType(ir.IntType(8), len(node.value))
        string_global = ir.GlobalVariable(self.module, c_string_type, name=f'string_{self.printf_string}')
        string_global.global_constant = True
        string_global.initializer = ir.Constant(c_string_type, bytearray(node.value, 'utf8'))
        self.printf_string += 1
        return self.builder.bitcast(string_global, ir.PointerType(ir.IntType(8)))

    def visit_UnaryOp(self, node):
        child = self.visit(node.children[0])
        if isinstance(node, BitwiseNotNode):
            return self.builder.not_(child)

        if child.type == ir.FloatType():
            result = self.builder.fcmp_ordered("==", child, ir.Constant(child.type, 0))
        else:
            result = self.builder.icmp_signed("==", child, ir.Constant(child.type, 0))
        if child.type == ir.FloatType():
            result = self.builder.zext(child, ir.IntType(32))
            return self.builder.sitofp(result, ir.FloatType())
        elif child.type == ir.IntType(8):
            return self.builder.zext(result, ir.IntType(8))
        else:
            return self.builder.zext(result, ir.IntType(32))

    def visit_BinaryOp(self, node, method):
        type1 = self.get_highest_type(node.children[0])
        type2 = self.get_highest_type(node.children[1])
        var_type = 'char'
        if 'float' in [type1, type2]:
            var_type = 'float'
        elif 'int' in [type1, type2]:
            var_type = 'int'
        child1 = self.visit(node.children[0])
        child2 = self.visit(node.children[1])
        pointer = False
        if child1.type == ir.IntType(64):
            pointer = True
        if child1.type == ir.IntType(64):
            pointer = True
        if child1.type == ir.IntType(64):
            pointer = True
        if child2.type == ir.IntType(64):
            pointer = True
        if child2.type == ir.IntType(64):
            pointer = True
        if child2.type == ir.IntType(64):
            pointer = True
        child1 = self.convertLLVMtype(var_type, child1, pointer)
        child2 = self.convertLLVMtype(var_type, child2, pointer)
        _visitor = getattr(self, method, self.generic_visit)
        return _visitor(node, [child1, child2])

    def visit_PlusNode(self, node, children=[]):
        left = children[0]
        right = children[1]

        if left.type == ir.FloatType():
            return self.builder.fadd(left, right)
        return self.builder.add(left, right)

    def visit_MinusNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        if left.type == ir.FloatType():
            return self.builder.fsub(left, right)
        return self.builder.sub(left, right, name="tmp")

    def visit_MultNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        if left.type == ir.FloatType():
            return self.builder.fmul(left, right)
        return self.builder.mul(left, right)

    def visit_DivNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        if left.type == ir.FloatType():
            return self.builder.fdiv(left, right)
        return self.builder.sdiv(left, right)

    def visit_ModNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.srem(left, right)

    def visit_BitwiseAndNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.and_(left, right)

    def visit_BitwiseOrNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.or_(left, right)

    def visit_BitwiseXorNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.xor(left, right)

    def visit_LogicalAndNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        if left.type == ir.FloatType():
            left = self.builder.fcmp_ordered("!=", left, ir.Constant(left.type, 0))
        else:
            left = self.builder.icmp_signed("!=", left, ir.Constant(left.type, 0))
        if right.type == ir.FloatType():
            right = self.builder.fcmp_ordered("!=", right, ir.Constant(right.type, 0))
        else:
            right = self.builder.icmp_signed("!=", right, ir.Constant(right.type, 0))
        result = self.builder.icmp_unsigned("==", left, right)
        result = self.builder.icmp_unsigned("==", left, result)
        if left.type == ir.IntType(8):
            return self.builder.zext(result, ir.IntType(8))
        else:
            result = self.builder.zext(result, ir.IntType(32))
            if left.type == ir.FloatType():
                return self.builder.sitofp(result, ir.FloatType())
            return result

    def visit_LogicalOrNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        if left.type == ir.FloatType():
            left = self.builder.fcmp_ordered("!=", left, ir.Constant(left.type, 0))
        else:
            left = self.builder.icmp_signed("!=", left, ir.Constant(left.type, 0))
        if right.type == ir.FloatType():
            right = self.builder.fcmp_ordered("!=", right, ir.Constant(right.type, 0))
        else:
            right = self.builder.icmp_signed("!=", right, ir.Constant(right.type, 0))
        result = self.builder.or_(left, right)
        if left.type == ir.IntType(8):
            return self.builder.zext(result, ir.IntType(8))
        else:
            result = self.builder.zext(result, ir.IntType(32))
            if left.type == ir.FloatType():
                return self.builder.sitofp(result, ir.FloatType())
            return result

    def visit_SRNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.ashr(left, right)

    def visit_SLNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        return self.builder.shl(left, right)

    def visit_LTNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        if left.type == ir.FloatType():
            result = self.builder.fcmp_ordered("<", left, right)
            result = self.builder.zext(result, ir.IntType(32))
            return self.builder.sitofp(result, ir.FloatType())
        else:
            result = self.builder.icmp_signed("<", left, right)
        if left.type == ir.IntType(8):
            return self.builder.zext(result, ir.IntType(8))
        else:
            return self.builder.zext(result, ir.IntType(32))

    def visit_GTNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        if left.type == ir.FloatType():
            result = self.builder.fcmp_ordered(">", left, right)
            result = self.builder.zext(result, ir.IntType(32))
            return self.builder.sitofp(result, ir.FloatType())
        else:
            result = self.builder.icmp_signed(">", left, right)
        if left.type == ir.IntType(8):
            return self.builder.zext(result, ir.IntType(8))
        else:
            return self.builder.zext(result, ir.IntType(32))

    def visit_LTEQNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        if left.type == ir.FloatType():
            result = self.builder.fcmp_ordered("<=", left, right)
            result = self.builder.zext(result, ir.IntType(32))
            return self.builder.sitofp(result, ir.FloatType())
        else:
            result = self.builder.icmp_signed("<=", left, right)
        if left.type == ir.IntType(8):
            return self.builder.zext(result, ir.IntType(8))
        else:
            return self.builder.zext(result, ir.IntType(32))

    def visit_GTEQNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        if left.type == ir.FloatType():
            result = self.builder.fcmp_ordered(">=", left, right)
            result = self.builder.zext(result, ir.IntType(32))
            return self.builder.sitofp(result, ir.FloatType())
        else:
            result = self.builder.icmp_signed(">=", left, right)
        if left.type == ir.IntType(8):
            return self.builder.zext(result, ir.IntType(8))
        else:
            return self.builder.zext(result, ir.IntType(32))

    def visit_EQNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        if left.type == ir.FloatType():
            result = self.builder.fcmp_ordered("==", left, right)
            result = self.builder.zext(result, ir.IntType(32))
            return self.builder.sitofp(result, ir.FloatType())
        else:
            result = self.builder.icmp_signed("==", left, right)
        if left.type == ir.IntType(8):
            return self.builder.zext(result, ir.IntType(8))
        else:
            return self.builder.zext(result, ir.IntType(32))

    def visit_NEQNode(self, node, children=[]):
        left = children[0]
        right = children[1]
        if left.type == ir.FloatType():
            result = self.builder.fcmp_ordered("!=", left, right)
            result = self.builder.zext(result, ir.IntType(32))
            return self.builder.sitofp(result, ir.FloatType())
        else:
            result = self.builder.icmp_signed("!=", left, right)
        if left.type == ir.IntType(8):
            return self.builder.zext(result, ir.IntType(8))
        else:
            return self.builder.zext(result, ir.IntType(32))

    def visit_IdentifierNode(self, node):
        # Load the value from the alloca
        return self.builder.load(self.scope.get_symbol(name=node.value).alloca)

    def visit_AddrNode(self, node):
        alloca = self.scope.get_symbol(name=node.value.value).alloca
        ptr_int = self.builder.ptrtoint(alloca, ir.IntType(64))
        return ptr_int

    def visit_DerefNode(self, node):
        alloca = self.scope.get_symbol(name=node.identifier.value).alloca
        loaded = self.builder.load(alloca)
        return loaded

    def visit_ExplicitConversionNode(self, node):
        value = self.visit(node.rvalue)
        if node.type == 'int':
            if value.type == ir.FloatType():
                return self.builder.fptosi(value, ir.IntType(32))
            return self.builder.sext(value, ir.IntType(32))
        elif node.type == 'float':
            if value.type == ir.IntType(32):
                return self.builder.sitofp(value, ir.FloatType())
            return self.builder.fptosi(value, ir.FloatType())
        elif node.type == 'char':
            if value.type == ir.FloatType():
                return self.builder.fptosi(value, ir.IntType(8))
            return self.builder.trunc(value, ir.IntType(8))

    def visit_CommentNode(self, node):
        pass

    def visit_TypedefNode(self, node):
        pass

    def visit_EnumNode(self, node):
        self.enums[node.enum_name] = node.enum_list
