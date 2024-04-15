class Symbol:
    def __init__(self, name, var_type, const=False, symbol_type='variable', defined=True, params=None):
        self.name = name
        self.const = const
        self.type = var_type
        self.symbol_type = symbol_type
        self.defined = defined
        self.params = params if params is not None else []


class SymbolTable:
    def __init__(self):
        self.symbols = []
        self.enums = {}

    def add_symbol(self, symbol):
        for existing_symbol in self.symbols:
            if symbol.name == existing_symbol.name:
                if existing_symbol.symbol_type == 'function' and symbol.symbol_type == 'function' and existing_symbol.defined:
                    self.symbols.append(symbol)
                    return None
                raise Exception("Variable already exists")
        self.symbols.append(symbol)
        return None

    def add_enum(self, name, enum_list):
        if name in self.enums:
            raise Exception(f"Enum {name} already exists in the table")
        else:
            self.enums[name] = enum_list

    def remove_symbol(self, symbol):
        for symb in self.symbols:
            if symbol == symb.name:
                del self.symbols[self.symbols.index(symb)]
                return
        raise Exception(f"Symbol {symbol} does not exist in the table")

    def get_symbol(self, name) -> list:
        symbols = []
        if name.startswith('-'):
            name = name[1:]
        for symbol in self.symbols:
            if symbol.name == name:
                symbols.append(symbol)
        if len(symbols) > 1:
            return symbols
        return symbols[0] if len(symbols) == 1 else None

    def get_enum(self, name):
        # get list of enum values from the enum name
        return self.enums.get(name, None)


class TreeNode:
    def __init__(self, table, parent=None):
        self.table = table
        self.parent = parent
        self.children = []


class SymbolTableTree:
    def __init__(self):
        self.root = TreeNode(SymbolTable())
        self.current_node = self.root
        self.locked_scopes = False
        self.locked_stack = -1

    def open_scope(self):
        if self.locked_scopes:
            self.locked_stack = 0
            self.locked_scopes = False
            return
        if self.locked_stack != -1:
            self.locked_stack += 1
        new_node = TreeNode(SymbolTable(), self.current_node)
        self.current_node.children.append(new_node)
        self.current_node = new_node

    def close_scope(self):
        if self.locked_stack == -1:
            if self.current_node == self.root:
                raise Exception("Cannot close root scope")
            self.current_node = self.current_node.parent
        else:
            self.locked_stack = -1

    def lock_scope(self):
        self.locked_scopes = True

    def is_global(self):
        return self.current_node == self.root

    def add_symbol(self, symbol: Symbol):
        return self.current_node.table.add_symbol(symbol)

    def get_symbol(self, name) -> list | Symbol | None:
        node = self.current_node
        symbols = node.table.get_symbol(name)
        return symbols

    def remove_symbol(self, symbol):
        self.current_node.table.remove_symbol(symbol)

    def get_all_symbols(self):
        symbols = []
        node = self.current_node
        while node:
            for symbol in node.table.symbols:
                symbols.append(symbol)
            node = node.parent
        return symbols

    def lookup(self, name):
        node = self.current_node
        while node:
            symbols = node.table.get_symbol(name)
            if symbols:
                return symbols
            node = node.parent
        return None

    def add_enum(self, name, enum_list):
        self.current_node.table.add_enum(name, enum_list)

    def get_all_enums(self):
        enums = []
        node = self.current_node
        while node:
            for enum in node.table.enums:
                enums.append(enum)
            node = node.parent
        return enums

    def get_enum_values(self):
        # get all values of the enum in the current scope as a list
        enum_values = []
        for enum in self.current_node.table.enums:
            enum_values.extend(self.current_node.table.enums[enum])
        return enum_values

    def get_enum_list(self, enum_name):
        # get all values of the enum in the current scope and parent scopes
        node = self.current_node
        while node:
            enum_dict = node.table.get_enum(enum_name)
            if enum_dict:
                return enum_dict
            node = node.parent
        return None

    def get_all_enum_values(self):
        enums = []
        node = self.current_node
        while node:
            for enum in node.table.enums:
                enums.extend(node.table.enums[enum])
            node = node.parent
        return enums

    def current_scope(self):
        return self.current_node.table


    def get_enum_values_of_enum(self, enum_name):
        # get all values of the enum in the current scope or parent as a list
        enum_values = []
        node = self.current_node
        while node:
            enum_dict = node.table.get_enum(enum_name)
            if enum_dict:
                enum_values.extend(enum_dict)
                return enum_values
            node = node.parent
        return enum_values
