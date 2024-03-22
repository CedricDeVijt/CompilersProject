class Symbol:
    def __init__(self, name, varType, const, value=0, returnType=None):
        self.name = name
        self.const = const
        self.type = varType
        self.returnType = returnType
        self.value = value


class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, symbol):
        if symbol.name in self.symbols:
            # Symbol already exists in the table, handle error or update entry
            raise Exception(f"Symbol {symbol.name} already exists in the table")
        else:
            self.symbols[symbol.name] = symbol

    def get_symbol(self, name):
        symbol = self.symbols.get(name, None)
        if symbol:
            return symbol
        return None


class TreeNode:
    def __init__(self, table, parent=None):
        self.table = table
        self.parent = parent
        self.children = []


class SymbolTableBuilder:
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

    def get_symbol(self, name):
        node = self.current_node
        symbol = node.table.get_symbol(name)
        if symbol:
            return symbol
        raise Exception(f"Symbol {name} not found in the current scope")

    def lookup(self, name):
        node = self.current_node
        while node:
            symbol = node.table.get_symbol(name)
            if symbol:
                return symbol
            node = node.parent

        raise Exception(f"Symbol {name} not found in tree")

    def current_scope(self):
        return self.current_node.table
