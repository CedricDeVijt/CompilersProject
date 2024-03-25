from graphviz import Source

class SymbolValue:
    def __init__(self, value, varType, const):
        self.value = value
        self.varType = varType
        self.const = const

class SymbolTable:
    def __init__(self):
        self.table = dict()
        self.parent = None

    def insert(self, name, value):
        self.table[name] = value

    def lookup(self, name):
        if name in self.table:
            return self.table[name]
        if self.parent is not None:
            return self.parent.lookup(name)
        return None

    def set_parent(self, parent):
        self.parent = parent

class Node:
    def __init__(self, value: str, line: int, pos: int, children=None):
        self.value = value
        self.children = children if children is not None else []
        self.line = line
        self.pos = pos

    def to_dot(self):
        dot_string = f'"{id(self)}" [label="{self.value}"];\n'
        for child in self.children:
            if isinstance(child, PointerNode):
                type = ""
                for line in child.type:
                    type += line.value
                    type += " "
                pointer_label = f"{type}{'*' * int(child.value)}"
                dot_string += f'"{id(self)}" -> "{id(self)}_{pointer_label}";\n'
                dot_string += f'"{id(self)}_{pointer_label}" [label="{pointer_label}"];\n'
            elif isinstance(child, Node):
                dot_string += f'"{id(self)}" -> "{id(child)}";\n'
                dot_string += child.to_dot()
            elif isinstance(child, str):
                dot_string += f'"{id(self)}" -> "{id(self)}_{child}";\n'
                dot_string += f'"{id(self)}_{child}" [label="{child}"];\n'
        return dot_string

    def to_dot_file(self, filename):
        dot_string = "digraph AST {\n" + self.to_dot() + "}\n"
        src = Source(dot_string)
        src.format = 'png'
        src.render(filename, view=True)


    def constantFold(self):
        for node in self.children:
            if not isinstance(node, str) and not isinstance(node, list):
                node.constantFold()
        match self:
            case IntNode():
                return
            case FloatNode():
                return
            case DivNode():
                if isinstance(self.children[0], IntNode) and isinstance(self.children[1], IntNode) and str(self.children[1].value) != "0":
                    self.__class__ = IntNode
                    self.value = str(int(self.children[0].value) // int(self.children[1].value))
                    self.children = []
                if isinstance(self.children[0], FloatNode) and isinstance(self.children[1], FloatNode) and float(self.children[1].value) != 0:
                    self.__class__ = FloatNode
                    self.value = str(float(self.children[0].value) / float(self.children[1].value))
                    self.children = []
                if isinstance(self.children[0], FloatNode) and isinstance(self.children[1], IntNode) and int(self.children[1].value) != 0:
                    self.__class__ = FloatNode
                    self.value = str(float(self.children[0].value) / float(self.children[1].value))
                    self.children = []
                if isinstance(self.children[0], IntNode) and isinstance(self.children[1], FloatNode) and float(self.children[1].value) != 0:
                    self.__class__ = FloatNode
                    self.value = str(float(self.children[0].value) / float(self.children[1].value))
                    self.children = []
                return
            case ModNode():
                if isinstance(self.children[0], IntNode) and isinstance(self.children[1], IntNode):
                    self.__class__ = IntNode
                    self.value = str(int(self.children[0].value) % int(self.children[1].value))
                    self.children = []
                return
            case MultNode():
                if isinstance(self.children[0], IntNode) and isinstance(self.children[1], IntNode):
                    self.__class__ = IntNode
                    self.value = str(int(self.children[0].value) * int(self.children[1].value))
                    self.children = []
                    return
                if isinstance(self.children[0], FloatNode) or isinstance(self.children[1], FloatNode):
                    self.__class__ = FloatNode
                    self.value = str(float(self.children[0].value) * float(self.children[1].value))
                    self.children = []
                    return
                if (isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)) and self.children[0].value == 0:
                    self.__class__ = IntNode
                    self.children = []
                    self.value = "0"
                    return
                if (isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode)) and self.children[1].value == 0:
                    self.__class__ = IntNode
                    self.children = []
                    self.value = "0"
                return
            case MinusNode():
                if isinstance(self.children[0], IntNode) and isinstance(self.children[1], IntNode):
                    self.__class__ = IntNode
                    self.value = str(int(self.children[0].value) - int(self.children[1].value))
                    self.children = []
                if isinstance(self.children[0], FloatNode) or isinstance(self.children[1], FloatNode):
                    self.__class__ = FloatNode
                    self.value = str(float(self.children[0].value) - float(self.children[1].value))
                    self.children = []
                return
            case PlusNode():
                if isinstance(self.children[0], IntNode) and isinstance(self.children[1], IntNode):
                    self.__class__ = IntNode
                    self.value = str(int(self.children[0].value) + int(self.children[1].value))
                    self.children = []
                    return
                if isinstance(self.children[0], FloatNode) or isinstance(self.children[1], FloatNode):
                    self.__class__ = FloatNode
                    self.value = str(float(self.children[0].value) + float(self.children[1].value))
                    self.children = []
                    return
            case GTNode():
                self.__class__ = IntNode
                self.value = str(float(self.children[0].value) > float(self.children[1].value))
                self.children = []
                return
            case LTNode():
                self.__class__ = IntNode
                self.value = str(float(self.children[0].value) < float(self.children[1].value))
                self.children = []
            case GTEQNode():
                self.__class__ = IntNode
                self.value = str(float(self.children[0].value) >= float(self.children[1].value))
                self.children = []
                return
            case LTEQNode():
                self.__class__ = IntNode
                self.value = str(float(self.children[0].value) <= float(self.children[1].value))
                self.children = []
                return
            case NEQNode():
                self.__class__ = IntNode
                self.value = str(float(self.children[0].value) != float(self.children[1].value))
                self.children = []
                return
            case SLNode():
                if isinstance(self.children[0], IntNode) and isinstance(self.children[1], IntNode):
                    self.__class__ = IntNode
                    self.value = str(int(self.children[0].value) << int(self.children[1].value))
                    self.children = []
                return
            case SRNode():
                if isinstance(self.children[0], IntNode) and isinstance(self.children[1], IntNode):
                    self.__class__ = IntNode
                    self.value = str(int(self.children[0].value) >> int(self.children[1].value))
                    self.children = []
                return
            case BitwiseAndNode():
                self.__class__ = IntNode
                self.value = str(float(self.children[0].value) & float(self.children[1].value))
                self.children = []
                return
            case BitwiseOrNode():
                self.__class__ = IntNode
                self.value = str(float(self.children[0].value) | float(self.children[1].value))
                self.children = []
                return
            case BitwiseXorNode():
                self.__class__ = IntNode
                self.value = str(float(self.children[0].value) ^ float(self.children[1].value))
                self.children = []
                return
            case LogicalAndNode():
                self.__class__ = IntNode
                self.value = str(float(self.children[0].value) and float(self.children[1].value))
                self.children = []
                return
            case LogicalOrNode():
                self.__class__ = IntNode
                self.value = str(float(self.children[0].value) or float(self.children[1].value))
                self.children = []
                return
            case LogicalNotNode():
                self.__class__ = IntNode
                self.value = str(not float(self.children[0].value))
                self.children = []
                return
        return


class ProgramNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("Program", line, pos, children=children)


class MainNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("Main", line, pos, children=children)

class StatementNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("Statement", line, pos, children=children)

class IdentifierNode(Node):
    def __init__(self, value, line: int, pos: int, children=None):
        super().__init__(value, line, pos, children=children)

class TypeNode(Node):
    def __init__(self, value, line: int, pos: int, children=None):
        super().__init__(value, line, pos, children=children)


class LogicalNotNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("LogicalNot", line, pos, children=children)


class DivNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("Div", line, pos, children=children)


class ModNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("Mod", line, pos, children=children)


class MultNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("Mul", line, pos, children=children)


class MinusNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("Minus", line, pos, children=children)


class PlusNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("Plus", line, pos, children=children)


class GTNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("GT", line, pos, children=children)


class LTNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("LT", line, pos, children=children)


class GTEQNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("GTEQ", line, pos, children=children)


class LTEQNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("LTEQ", line, pos, children=children)


class EQNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("EQ", line, pos, children=children)


class NEQNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("NEQ", line, pos, children=children)


class SLNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("SL", line, pos, children=children)


class SRNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("SR", line, pos, children=children)


class BitwiseAndNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("BitwiseAnd", line, pos, children=children)


class BitwiseOrNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("BitwiseOr", line, pos, children=children)


class BitwiseXorNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("BitwiseXor", line, pos, children=children)


class LogicalAndNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("LogicalAnd", line, pos, children=children)


class LogicalOrNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("LogicalOr", line, pos, children=children)


class PointerNode(Node):
    def __init__(self, value: int, line: int, pos: int, children=None):
        super().__init__(str(value), line, pos, children=children)

    def setType(self, type: TypeNode):
        self.type = type


class IntNode(Node):
    def __init__(self, value, line: int, pos: int, children=None):
        super().__init__(value, line, pos, children=children)


class FloatNode(Node):
    def __init__(self, value, line: int, pos: int, children=None):
        super().__init__(value, line, pos, children=children)