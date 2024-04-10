class Symbol:
    def __init__(self, name, varType, const, typeDef=False, returnType=None):
        self.name = name
        self.const = const
        self.type = varType
        self.typeDef = typeDef
        self.returnType = returnType


class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.enums = {}

    def add_symbol(self, symbol):
        if symbol.name in self.symbols:
            # Symbol already exists in the table, handle error or update entry
            raise Exception(f"Symbol {symbol.name} already exists in the table")
        else:
            self.symbols[symbol.name] = symbol

    def add_enum(self, name, enum_dict):
        if name in self.enums:
            raise Exception(f"Enum {name} already exists in the table")
        else:
            self.enums[name] = enum_dict

    def get_symbol(self, name) -> Symbol:
        symbol = self.symbols.get(name, None)
        return symbol

    def get_enum(self, name):
        enum_dict = self.enums.get(name, None)
        return enum_dict


class TreeNode:
    def __init__(self, table, parent=None):
        self.table = table
        self.parent = parent
        self.children = []


class SymbolTableTree:
    def __init__(self):
        self.root = TreeNode(SymbolTable())
        self.current_node = self.root

    def open_scope(self):
        new_node = TreeNode(SymbolTable(), self.current_node)
        self.current_node.children.append(new_node)
        self.current_node = new_node

    def close_scope(self):
        if self.current_node == self.root:
            raise Exception("Cannot close root scope")
        self.current_node = self.current_node.parent

    def add_symbol(self, symbol):
        self.current_node.table.add_symbol(symbol)

    def get_symbol(self, name) -> Symbol:
        node = self.current_node
        symbol = node.table.get_symbol(name)
        return symbol

    def get_all_symbols(self):
        return self.current_node.table.symbols

    def lookup(self, name):
        node = self.current_node
        while node:
            symbol = node.table.get_symbol(name)
            if symbol:
                return symbol
            node = node.parent
        return None

    def current_scope(self):
        return self.current_node.table
