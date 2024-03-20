class Symbol:
    def __init__(self, name, varType, const, value=0):
        self.name = name
        self.const = const
        self.type = varType
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

        raise Exception(f"Symbol {name} not found in the table")

    def __str__(self):
        return "\n".join(
            [f"{symbol.name}: {symbol.type} - Scope: {symbol.scope} - Accessibility: {symbol.accessibility}" for symbol
             in self.symbols.values()])


class SymbolTableBuilder:
    def __init__(self):
        self.symbol_stack = [SymbolTable()]

    def open_scope(self):
        self.symbol_stack.append(SymbolTable())

    def close_scope(self):
        return self.symbol_stack.pop()

    def add_symbol(self, symbol):
        self.symbol_stack[-1].add_symbol(symbol)

    def get_symbol(self, name):
        for table in reversed(self.symbol_stack):
            symbol = table.get_symbol(name)
            if symbol:
                return symbol
        return None

    def current_scope(self):
        return self.symbol_stack[-1]
