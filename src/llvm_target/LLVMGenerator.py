import platform

from llvmlite import ir

from src.parser.AST import *
from src.parser.SymbolTable import *
from src.parser.ASTGenerator import matching_params

unary_ops = {'LogicalNotNode', 'BitwiseNotNode'}
binary_ops = {'DivNode', 'ModNode', 'MultNode', 'MinusNode', 'PlusNode', 'GTNode', 'LTNode', 'GTEQNode', 'LTEQNode', 'EQNode', 'NEQNode', 'SLNode', 'SRNode', 'BitwiseAndNode', 'BitwiseOrNode', 'BitwiseXorNode', 'LogicalAndNode', 'LogicalOrNode'}


class LLVMVisitor:
    def __init__(self, stdio=False):
        self.builder = None
        self.scope = SymbolTableTree()
        self.module = ir.Module()
        self.module.triple = f"{platform.machine()}-pc-{platform.system().lower()}"
        self.printf_string = 0
        self.scanf_string = 0
        self.enums = {}
        self.break_blocks = []
        self.continue_blocks = []
        self.global_var = 0
        self.structs = {}

        # Add printf and scanf function
        if stdio:

            # Printf

            function_type = ir.FunctionType(ir.IntType(32), [ir.PointerType(ir.IntType(8))], var_arg=True)
            function = ir.Function(self.module, function_type, name='printf')
            self.builder = function

            # Scanf

            function_type = ir.FunctionType(ir.IntType(32), [ir.PointerType(ir.IntType(8))], var_arg=True)
            function = ir.Function(self.module, function_type, name='scanf')
            self.builder = function

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
            size.append(node.value)
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

    def get_highest_type(self, rval):
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
        symbols = self.scope.lookup(identifier)
        if symbols:
            if isinstance(symbols.type, str):
                return symbols.type
            if isinstance(symbols.type, PointerNode):
                if isinstance(symbols.type.type, list):
                    var_type = symbols.type.type[len(symbols.type.type) - 1].value
                else:
                    var_type = symbols.type.type.value
                if var_type == 'char' and symbols.type.value == 1:
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
        for child in node.children:
            if isinstance(child, StringNode):
                child.value = child.value.strip('"')
                child.value = child.value + "\00"
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

        # Call Printf Function.
        args = [self.builder.bitcast(format_string_global, ir.PointerType(ir.IntType(8)))]
        for arg in node.children:
            if isinstance(arg, StringNode):
                self.printf_string += 1
            if isinstance(arg, DerefNode):
                arg = self.visit(arg)
                arg = self.builder.load(arg)
            else:
                arg = self.visit(arg)
            if arg.type == ir.FloatType():
                # Convert to double
                arg = self.builder.fpext(arg, ir.DoubleType())

            args.append(arg)
        self.builder.call(self.module.get_global('printf'), args)
        self.printf_string += 1

    def visit_ScanfNode(self, node):
        specifier = node.specifier
        specifier += '\00'
        # Create Global Variable For Format String.
        c_string_type = ir.ArrayType(ir.IntType(8), len(specifier))
        format_string_global = ir.GlobalVariable(self.module, c_string_type, name=f'scanf_string_{self.scanf_string}')
        format_string_global.global_constant = True
        format_string_global.initializer = ir.Constant(c_string_type, bytearray(specifier, 'utf8'))

        # Call Scanf Function.
        args = [self.builder.bitcast(format_string_global, ir.PointerType(ir.IntType(8)))]
        for arg in node.children:
            arg = self.visit(arg)
            args.append(arg)
        self.builder.call(self.module.get_global('scanf'), args)
        self.scanf_string += 1

    def visit_FunctionNode(self, node):
        # Add symbol if not exist
        const = False
        if isinstance(node.type, PointerNode):
            const = isinstance(node.type.type, list)
        else:
            const = isinstance(node.type, list)
        symbol = Symbol(name=node.value, var_type=node.type, symbol_type='function', const=const, params=node.params)
        symbol.original = str(self.global_var)
        if node.value == 'main' and len(node.params) == 0:
            original = 'main'
        else:
            original = str(self.global_var)
            self.global_var += 1
        symbols = self.scope.get_symbol(name=node.value) if self.scope.get_symbol(name=node.value) is not None else []
        if isinstance(symbols, Symbol):
            symbols = [symbols]
        if len(symbols) != 0:
            for symb in symbols:
                if symb.symbol_type != 'function':
                    return
                elif not symb.defined:
                    continue
                elif len(symbol.params) == len(symb.params):
                    if matching_params(symb.params, node.params):
                        if symb.defined == symbol.defined:
                            return
        self.scope.add_symbol(symbol)
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
            symbol = Symbol(name=param_name, var_type=param_type, const=const, symbol_type='variable', defined=True, params=None)
            symbols = self.scope.get_symbol(name=param_name)
            if not symbols:
                self.scope.add_symbol(symbol)
        # Arguments.
        arg_types = []
        arg_names = []
        symbols = []
        for param in node.params:
            if isinstance(param, list):
                param_type = param[len(param) - 2]
                param_name = param[len(param) - 1]
                if isinstance(param_name, IdentifierNode):
                    param_name = param_name.value
                arg_names.append(param_name)
                symbol = Symbol(name=param_name, var_type=param_type)
                symbols.append(symbol)
                if isinstance(param_type, TypeNode):
                    if param_type.value == 'char':
                        arg_types.append(ir.IntType(8))
                    elif param_type.value == 'int':
                        arg_types.append(ir.IntType(32))
                    elif param_type.value == 'float':
                        arg_types.append(ir.FloatType())
                elif isinstance(param_type, PointerNode):
                    ...

        # Function type.
        function_type = ir.FunctionType(ir.VoidType(), arg_types)
        func_type = node.type
        if isinstance(func_type, list):
            func_type = func_type[len(func_type) - 1]
        if isinstance(func_type, TypeNode):
            if func_type.value == 'char':
                function_type = ir.FunctionType(ir.IntType(8), arg_types)
            elif func_type.value == 'int':
                function_type = ir.FunctionType(ir.IntType(32), arg_types)
            elif func_type.value == 'float':
                function_type = ir.FunctionType(ir.FloatType(), arg_types)
            elif func_type.value == 'void':
                function_type = ir.FunctionType(ir.VoidType(), arg_types)
        elif isinstance(func_type, PointerNode):
            ...
        function = ir.Function(self.module, function_type, name=original)

        entry_block = function.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(entry_block)

        for arg_name in arg_names:
            # Update symbol alloca
            symbol = self.scope.get_symbol(name=arg_name)
            if isinstance(symbol, Symbol):
                alloca = self.builder.alloca(function.args[arg_names.index(arg_name)].type)
                self.builder.store(function.args[arg_names.index(arg_name)], alloca)
                symbol.alloca = alloca

        # Add return statement if last instruction is IfStatementNode
        if len(node.body) != 0 and isinstance(node.body[len(node.body) - 1], IfStatementNode):
            original = 'return'
            func_type = self.get_highest_type(node.type)
            if func_type == 'void':
                ret_val = None
            elif func_type == 'char':
                ret_val = CharNode(line=0, column=0, original='0', value='0')
            elif func_type == 'int':
                ret_val = IntNode(line=0, column=0, original='0', value='0')
            elif func_type == 'float':
                ret_val = FloatNode(line=0, column=0, original='0', value='0')
            ret_node = ReturnNode(line=0, column=0, original=original, ret_val=ret_val)
            node.body.append(ret_node)

        # Visit function body
        for statement in node.body:
            self.builder.comment(statement.original.replace('\n', '\\n'))
            self.visit(statement)

        # Close scope.
        self.scope.close_scope()

    def visit_FunctionCallNode(self, node):
        args = []
        for arg in node.arguments:
            if isinstance(arg, DerefNode):
                arg = self.visit(arg)
                arg = self.builder.load(arg)
            else:
                arg = self.visit(arg)
            args.append(arg)
        symbols = self.scope.lookup(name=node.value) if self.scope.lookup(name=node.value) is not None else []
        if isinstance(symbols, Symbol):
            symbols = [symbols]
        found = False
        for symbol in symbols:
            similar = True
            params = symbol.params
            if len(node.arguments) != len(params):
                continue
            for i in range(0, len(params)):
                type1 = self.get_highest_type(params[i][0])
                type2 = self.get_highest_type(node.arguments[i])
                if type1 != type2:
                    similar = False
                lval = self.get_pointer_size(params[i][0], by_ref=True)
                rval = self.get_pointer_size(node.arguments[i])
                error = False
                if len(lval) != len(rval):
                    similar = False
                else:
                    for i in range(0, len(lval)):
                        if lval[i] != rval[i]:
                            if not error:
                                similar = False
            if similar:
                a = self.module.get_global(symbol.original)
                return self.builder.call(self.module.get_global(symbol.original), args)

    def visit_ifStatementNode(self, node):
        # open scope
        self.scope.open_scope()
        # close scope
        self.scope.close_scope()

    def get_array_type(self, node, c_type):
        if not isinstance(node.array[0], ArrayNode):
            length = len(node.array)
            if c_type == 'int':
                return ir.ArrayType(ir.IntType(32), length)
            elif c_type == 'float':
                return ir.ArrayType(ir.FloatType(), length)
            elif c_type == 'char':
                return ir.ArrayType(ir.IntType(8), length)
        else:
            return ir.ArrayType(self.get_array_type(node.array[0], c_type), len(node.array))

    def create_multi_dimensional_list(self, dimensions):
        if not dimensions:
            return 0
        else:
            return [self.create_multi_dimensional_list(dimensions[1:]) for _ in range(dimensions[0])]

    # for declaration
    def get_array_type_dec(self, zero_list, c_type):
        if not isinstance(zero_list[0], list):
            length = len(zero_list)
            if c_type == 'int':
                return ir.ArrayType(ir.IntType(32), length)
            elif c_type == 'float':
                return ir.ArrayType(ir.FloatType(), length)
            elif c_type == 'char':
                return ir.ArrayType(ir.IntType(8), length)
        else:
            return ir.ArrayType(self.get_array_type_dec(zero_list[0], c_type), len(zero_list))

    def initialize_array(self, node, c_type):
        # initialize array on zeros
        if isinstance(node.array[0], ArrayNode):
            array_constants = []
            for i in range(len(node.array)):
                array_constants.append(self.initialize_array(node.array[i], c_type))
            return array_constants
        else:
            array_constants = []
            for i in range(len(node.array)):
                if c_type == 'int':
                    array_constants.append(ir.Constant(ir.IntType(32), 0))
                elif c_type == 'float':
                    array_constants.append(ir.Constant(ir.FloatType(), 0))
                elif c_type == 'char':
                    array_constants.append(ir.Constant(ir.IntType(8), 0))
            return array_constants

    def initialize_array_dec(self, zero_list, c_type):
        # initialize array on zeros
        if isinstance(zero_list[0], list):
            array_constants = []
            for i in range(len(zero_list)):
                array_constants.append(self.initialize_array_dec(zero_list[i], c_type))
            return array_constants
        else:
            array_constants = []
            for i in range(len(zero_list)):
                if c_type == 'int':
                    array_constants.append(ir.Constant(ir.IntType(32), 0))
                elif c_type == 'float':
                    array_constants.append(ir.Constant(ir.FloatType(), 0))
                elif c_type == 'char':
                    array_constants.append(ir.Constant(ir.IntType(8), 0))
            return array_constants

    def assign_array_values(self, node, array_ptr):
        if not isinstance(node, ArrayNode):
            self.builder.store(self.visit(node), array_ptr)
            return
        elif isinstance(node.array[0], ArrayNode):
            for i in range(len(node.array)):
                ptr = self.builder.gep(array_ptr, [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), i)])
                self.assign_array_values(node.array[i], ptr)
            return
        else:
            for i in range(len(node.array)):
                ptr = self.builder.gep(array_ptr, [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), i)])
                self.builder.store(self.visit(node.array[i]), ptr)

    def visit_DefinitionNode(self, node):
        # definition vars
        var_name = node.lvalue.value
        rvalue = self.visit(node.rvalue)
        if isinstance(node.rvalue, DerefNode):
            rvalue = self.builder.load(rvalue)
        enum = False
        # if regular type
        if isinstance(node.type, list):
            var_type = self.get_highest_type(node.type[len(node.type) - 1])
            symbol = Symbol(name=var_name, var_type=node.type[len(node.type) - 1])
        # if enum
        else:
            var_type = 'int'
            symbol = Symbol(name=var_name, var_type=var_type)
            enum = True

        if not enum and isinstance(node.type[0], PointerNode):
            if var_type == 'float':
                pointer_type = ir.PointerType(ir.FloatType())
            elif var_type == 'int':
                pointer_type = ir.PointerType(ir.IntType(32))
            elif var_type == 'char':
                pointer_type = ir.PointerType(ir.IntType(8))
            for i in range(0, int(node.type[0].value) - 1):
                pointer_type = ir.PointerType(pointer_type)
            var_ptr = ir.GlobalVariable(self.module, ir.PointerType(pointer_type), name=str(self.global_var))
            self.global_var += 1
            var_ptr.linkage = 'internal'
            var_ptr.initializer = None

            symbol.alloca = var_ptr
            if self.scope.get_symbol(name=var_name) is None:
                self.scope.add_symbol(symbol)

            rvalue = self.builder.inttoptr(rvalue, pointer_type)

            alloca = self.builder.alloca(pointer_type)

            self.builder.store(rvalue, alloca)

            # loaded = self.builder.load(rvalue)
            return self.builder.store(alloca, symbol.alloca)

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

        var_ptr = ir.GlobalVariable(self.module, rvalue.type, name=str(self.global_var))
        self.global_var += 1
        var_ptr.linkage = 'internal'
        var_ptr.initializer = None
        symbol.alloca = var_ptr
        if self.scope.get_symbol(name=var_name) is None:
            self.scope.add_symbol(symbol)
        if self.scope.is_global():
            var_ptr.initializer = rvalue
            return
        return self.builder.store(rvalue, var_ptr)

    def visit_ArrayDefinitionNode(self, node):
        # definition vars
        var_name = node.lvalue.value
        c_type = node.type.value
        array_types = self.get_array_type(node.rvalue, c_type)
        array_ptr = self.builder.alloca(array_types, name=var_name)
        array_constants = self.initialize_array(node.rvalue, c_type)
        rvalue = ir.Constant(array_types, array_constants)
        # create and store symbol for symbol table
        symbol = Symbol(name=var_name, var_type=array_types)
        symbol.alloca = array_ptr
        if self.scope.get_symbol(name=var_name) is None:
            self.scope.add_symbol(symbol)
        # store the zero array
        self.builder.store(rvalue, array_ptr)
        # assign the values
        self.assign_array_values(node.rvalue, array_ptr)
        return

    def visit_DeclarationNode(self, node):
        # Get the type and name of the variable being declared
        var_name = node.lvalue.value
        var_type = self.get_highest_type(node.type[len(node.type) - 1])
        if isinstance(node.type[0], PointerNode):
            if var_type == 'float':
                rvalue = ir.PointerType(ir.FloatType())
            elif var_type == 'int':
                rvalue = ir.PointerType(ir.IntType(32))
            elif var_type == 'char':
                rvalue = ir.PointerType(ir.IntType(8))
            else:
                raise Exception("WTF")
            for i in range(0, int(node.type[0].value)):
                rvalue = ir.PointerType(rvalue)
            rvalue = ir.Constant(rvalue, None)
        elif var_type == 'float':
            rvalue = ir.Constant(ir.FloatType(), None)
        elif var_type == 'int':
            rvalue = ir.Constant(ir.IntType(32), None)
        elif var_type == 'char':
            rvalue = ir.Constant(ir.IntType(8), None)
        else:
            raise Exception("WTF")
        var_ptr = ir.GlobalVariable(self.module, rvalue.type, name=str(self.global_var))
        self.global_var += 1
        var_ptr.linkage = 'internal'
        var_ptr.initializer = rvalue
        # Add to symbol table
        symbol = Symbol(name=var_name, var_type=node.type[len(node.type) - 1])
        symbol.alloca = var_ptr
        if self.scope.get_symbol(name=var_name) is None:
            self.scope.add_symbol(symbol)
        return var_ptr

    def visit_ArrayDeclarationNode(self, node):
        # Get the type and name of the variable being declared
        var_name = node.lvalue.value
        c_type = self.get_highest_type(node.type)
        dimensions = node.size
        array_types = self.get_array_type_dec(self.create_multi_dimensional_list(dimensions), c_type)
        array_ptr = self.builder.alloca(array_types, name=var_name)
        array_constants = self.initialize_array_dec(self.create_multi_dimensional_list(dimensions), c_type)
        rvalue = ir.Constant(array_types, array_constants)
        symbol = Symbol(name=var_name, var_type=array_types)
        symbol.alloca = array_ptr
        symbol.dimensions = dimensions
        if self.scope.get_symbol(name=var_name) is None:
            self.scope.add_symbol(symbol)
        # store the zero array
        self.builder.store(rvalue, array_ptr)
        return

    def visit_StructDeclarationNode(self, node):
        var_name = node.lvalue.value
        struct_type = self.structs[node.type.value][0]
        struct_ptr = self.builder.alloca(struct_type, name=var_name)
        symbol = Symbol(name=var_name, var_type=struct_type)
        symbol.alloca = struct_ptr
        symbol.vars = self.structs[node.type.value][1]
        if self.scope.get_symbol(name=var_name) is None:
            self.scope.add_symbol(symbol)
        return

    def visit_AssignmentNode(self, node):
        var_name = node.lvalue
        if isinstance(var_name, IdentifierNode):
            var_name = var_name.value
        elif isinstance(var_name, DerefNode):
            var_name = var_name.identifier.value
        symbol = self.scope.lookup(name=var_name)
        var_type = self.get_highest_type(symbol.type)
        rvalue = self.visit(node.rvalue)
        if isinstance(node.rvalue, DerefNode):
            rvalue = self.builder.load(rvalue)
        # Pointer
        if isinstance(symbol.type, PointerNode):
            # Change value of pointer.
            if isinstance(node.lvalue, DerefNode):
                pointee = self.visit(node.lvalue)
                alloca = self.builder.alloca(pointee.type.pointee)
                self.builder.store(rvalue, pointee)
                return
            # Change value of pointer.
            rvalue = self.builder.inttoptr(rvalue, symbol.alloca.type.pointee.pointee)

            alloca = self.builder.alloca(symbol.alloca.type.pointee.pointee)

            self.builder.store(rvalue, alloca)

            # loaded = self.builder.load(rvalue)
            return self.builder.store(alloca, symbol.alloca)

        # Convert value if needed.
        if rvalue.type != ir.FloatType() and var_type == 'float':
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
        symbol = self.scope.lookup(name=var_name)
        if self.scope.is_global():
            symbol.alloca.initializer = rvalue
            return
        self.builder.store(rvalue, symbol.alloca)

    def visit_ArrayAssignmentNode(self, node):
        # array assignment
        array_symbol = self.scope.lookup(name=node.lvalue.value)
        ptr = array_symbol.alloca
        if isinstance(node.lvalue, ArrayIdentifierNode):
            index = node.lvalue.indices
            for i in index:
                ptr = self.builder.gep(ptr, [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), i)])
        self.assign_array_values(node.rvalue, ptr)
        return

    def visit_StructAssignmentNode(self, node):
        # get pointer to struct
        symbol = self.scope.lookup(name=node.lvalue.struct_var_name)
        struct_ptr = symbol.alloca
        # get index of variable in struct
        vars = symbol.vars
        var_name = node.lvalue.struct_member_name
        index = vars.index(var_name)
        self.builder.store(self.visit(node.rvalue), self.builder.gep(struct_ptr, [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), index)]))
        return

    def visit_PostFixNode(self, node):
        symbol = self.scope.lookup(name=node.value)
        if isinstance(symbol, Symbol):
            value = 1
            if node.op == 'dec':
                value = -1
            # Pointer
            if isinstance(symbol.type, PointerNode):
                if symbol.alloca.type == ir.PointerType(ir.PointerType(ir.PointerType(ir.IntType(32)))):
                    value *= 4
                elif symbol.alloca.type == ir.PointerType(ir.PointerType(ir.PointerType(ir.FloatType()))):
                    value *= 8
                index = ir.Constant(ir.IntType(64), value)
                original_pointer = self.builder.load(symbol.alloca)
                original_pointer = self.builder.load(original_pointer)
                pointer_as_int = self.builder.ptrtoint(original_pointer, ir.IntType(64))
                new_pointer_as_int = self.builder.add(pointer_as_int, index)
                new_pointer = self.builder.inttoptr(new_pointer_as_int, symbol.alloca.type.pointee.pointee)
                self.builder.store(new_pointer, self.builder.load(symbol.alloca))
                return original_pointer
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
                if symbol.alloca.type == ir.PointerType(ir.PointerType(ir.PointerType(ir.IntType(32)))):
                    value *= 4
                elif symbol.alloca.type == ir.PointerType(ir.PointerType(ir.PointerType(ir.FloatType()))):
                    value *= 8
                index = ir.Constant(ir.IntType(64), value)
                pointer = self.builder.load(symbol.alloca)
                pointer_as_int = self.builder.ptrtoint(pointer, ir.IntType(64))
                new_pointer_as_int = self.builder.add(pointer_as_int, index)
                new_pointer = self.builder.inttoptr(new_pointer_as_int, symbol.alloca.type.pointee)
                self.builder.store(new_pointer, symbol.alloca)
                return new_pointer
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
            elif value.type == ir.IntType(8) or value.type == ir.IntType(32):
                val = self.builder.sext(value, ir.IntType(64))
            else:
                return self.builder.ptrtoint(value, ir.IntType(64))
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
            result = self.builder.zext(result, ir.IntType(32))
            return self.builder.sitofp(result, ir.FloatType())
        else:
            result = self.builder.icmp_signed("==", child, ir.Constant(child.type, 0))
            if child.type == ir.IntType(8):
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
        if isinstance(node.children[0], DerefNode):
            child1 = self.builder.load(child1)
        child2 = self.visit(node.children[1])
        if isinstance(node.children[1], DerefNode):
            child2 = self.builder.load(child2)
        pointer = False
        if child1.type != ir.IntType(8) and child1.type != ir.IntType(32) and child1.type != ir.FloatType():
            pointer = True
        if child2.type != ir.IntType(8) and child2.type != ir.IntType(32) and child2.type != ir.FloatType():
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
        return self.builder.load(self.scope.lookup(name=node.value).alloca)

    def visit_AddrNode(self, node):
        alloca = self.scope.lookup(name=node.value.value).alloca
        ptr_int = self.builder.ptrtoint(alloca, ir.IntType(64))
        return ptr_int

    def visit_DerefNode(self, node):
        alloca = self.scope.lookup(name=node.identifier.value).alloca
        pointer = self.builder.load(alloca)
        loaded = self.builder.load(pointer)
        for i in range(0, int(self.scope.lookup(name=node.identifier.value).type.value) - 1):
            loaded = self.builder.load(loaded)
        return loaded

    def get_DerefNodePointee(self, node):
        alloca = self.scope.lookup(name=node.identifier.value).alloca
        loaded = self.builder.load(alloca)
        for i in range(0, int(self.scope.lookup(name=node.identifier.value).type.value) - 1):
            loaded = self.builder.load(loaded)
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

    def visit_IfStatementNode(self, node):
        # Generate code for the condition
        condition = self.visit(node.condition)
        if isinstance(node.condition, DerefNode):
            condition = self.builder.load(condition)

        if condition.type != ir.IntType(1):
            condition = self.builder.icmp_signed('!=', condition, ir.Constant(ir.IntType(32), 0))

        # Create blocks for the if body and for after the if statement
        if_body_block = self.builder.function.append_basic_block(name='if.body')
        after_if_block = self.builder.function.append_basic_block(name='after.if')

        # Insert a conditional branch instruction
        self.builder.cbranch(condition, if_body_block, after_if_block)

        # Generate code for the if body
        self.builder.position_at_start(if_body_block)

        # body is a scope
        self.visit(node.body[0])

        if not self.builder.block.is_terminated:
            self.builder.branch(after_if_block)

        # Continue with the block after the if statement
        self.builder.position_at_start(after_if_block)

    def visit_WhileLoopNode(self, node):
        # Create blocks for the loop condition, loop body, and after the loop
        condition_block = self.builder.function.append_basic_block(name='while.cond')
        body_block = self.builder.function.append_basic_block(name='while.body')
        after_loop_block = self.builder.function.append_basic_block(name='after.while')

        # Push the after_loop_block to the break_blocks stack
        self.break_blocks.append(after_loop_block)

        # Push the condition_block to the continue_blocks stack
        self.continue_blocks.append(condition_block)

        # Generate code for the loop condition and set builder's position to the condition block
        self.builder.branch(condition_block)
        self.builder.position_at_start(condition_block)
        condition = self.visit(node.condition)

        if condition.type != ir.IntType(1):
            condition = self.builder.icmp_signed('!=', condition, ir.Constant(ir.IntType(32), 0))

        self.builder.cbranch(condition, body_block, after_loop_block)

        # Generate code for the loop body and set builder's position to the body block
        self.builder.position_at_start(body_block)
        for statement in node.body:
            self.visit(statement)
        self.builder.branch(condition_block)

        # Pop the after_loop_block from the break_blocks stack
        self.break_blocks.pop()

        # Continue with the block after the loop
        self.builder.position_at_start(after_loop_block)

        # Set builder's position to the block after the loop
        self.builder.position_at_start(after_loop_block)

    def visit_BreakNode(self, node):
        # Get the nearest loop end block from the break_blocks stack
        if self.break_blocks:
            break_block = self.break_blocks[-1]
            self.builder.branch(break_block)
        else:
            raise Exception("Invalid break statement. It should be inside a loop.")

    def visit_ContinueNode(self, node):
        # Get the nearest loop condition block from the continue_blocks stack
        if self.continue_blocks:
            continue_block = self.continue_blocks[-1]
            self.builder.branch(continue_block)
        else:
            raise Exception("Invalid continue statement. It should be inside a loop.")

    def visit_EnumNode(self, node):
        self.enums[node.enum_name] = node.enum_list

    def visit_ScopeNode(self, node):
        self.scope.open_scope()
        for statement in node.children:
            self.visit(statement)
        self.scope.close_scope()

    def visit_ArrayNode(self, node):
        pass

    def visit_ArrayIdentifierNode(self, node):
        # array index to retrieve
        index = node.indices

        array_symbol = self.scope.get_symbol(name=node.value)
        # Get pointer to original array
        ptr = array_symbol.alloca
        # Use gep to get a pointer to the specific element in the array
        for i in index:
            ptr = self.builder.gep(ptr, [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), i)])
        # Load and return the value from the pointer
        return self.builder.load(ptr)

    def visit_StructNode(self, node):
        struct_name = node.struct_name
        # get all types
        struct_types = []
        for i in node.struct_members:
            if self.get_highest_type(i.type) == 'int':
                struct_types.append(ir.IntType(32))
            elif self.get_highest_type(i.type) == 'float':
                struct_types.append(ir.FloatType())
            elif self.get_highest_type(i.type) == 'char':
                struct_types.append(ir.IntType(8))
        struct_type = ir.LiteralStructType(struct_types)
        struct_vars = []
        for i in node.struct_members:
            struct_vars.append(i.lvalue.value)

        # save struct with name and type
        self.structs[struct_name] = [struct_type, struct_vars]

    def visit_StructMemberNode(self, node):
        symbol = self.scope.get_symbol(name=node.struct_var_name)
        struct_ptr = symbol.alloca
        vars = symbol.vars
        index = vars.index(node.struct_member_name)
        struct_ptr = self.builder.gep(struct_ptr, [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), index)])
        return self.builder.load(struct_ptr)
