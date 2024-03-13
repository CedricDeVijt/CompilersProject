class Node:
    def __init__(self, value: str, line: int, pos: int, children=None):
        self.value = value
        self.children = children if children is not None else []
        self.line = line
        self.pos = pos

    def to_dot(self):
        dot = f'"{id(self)}" [label="{self.value}"];\n'
        for child in self.children:
            dot += f'"{id(self)}" -> "{id(child)}";\n'
            dot += child.to_dot()
        return dot

    def to_dot_file(self, filename):
        dot_representation = "digraph AST {\n" + self.to_dot() + "}\n"
        with open(filename, "w") as dot_file:
            dot_file.write(dot_representation)
        print(f"DOT file generated successfully at {filename}")

    def constantFold(self):
        for node in self.children:
            node.constantFold()
        match self:
            case LiteralNode():
                return
            case DivNode():
                if isinstance(self.children[0], LiteralNode) and isinstance(self.children[1], LiteralNode) and str(self.children[1].value) != "0":
                    self.__class__ = LiteralNode
                    self.value = str(int(self.children[0].value) // int(self.children[1].value))
                    self.children = []
                return
            case ModNode():
                if isinstance(self.children[0], LiteralNode) and isinstance(self.children[1], LiteralNode):
                    self.__class__ = LiteralNode
                    self.value = str(int(self.children[0].value) % int(self.children[1].value))
                    self.children = []
                return
            case MultNode():
                if isinstance(self.children[0], LiteralNode) and isinstance(self.children[1], LiteralNode):
                    self.__class__ = LiteralNode
                    self.value = str(int(self.children[0].value) * int(self.children[1].value))
                    self.children = []
                    return
                if isinstance(self.children[0], LiteralNode) and self.children[0].value == 0:
                    self.__class__ = LiteralNode
                    self.children = []
                    self.value = "0"
                    return
                if isinstance(self.children[1], LiteralNode) and self.children[1].value == 0:
                    self.__class__ = LiteralNode
                    self.children = []
                    self.value = "0"
                return
            case MinusNode():
                if isinstance(self.children[0], LiteralNode) and isinstance(self.children[1], LiteralNode):
                    self.__class__ = LiteralNode
                    self.value = str(int(self.children[0].value) - int(self.children[1].value))
                    self.children = []
                return
            case PlusNode():
                if isinstance(self.children[0], LiteralNode) and isinstance(self.children[1], LiteralNode):
                    self.__class__ = LiteralNode
                    self.value = str(int(self.children[0].value) + int(self.children[1].value))
                    self.children = []
                return
            case GTNode():
                if isinstance(self.children[0], LiteralNode) and isinstance(self.children[1], LiteralNode):
                    self.__class__ = LiteralNode
                    self.value = str(int(self.children[0].value) > int(self.children[1].value))
                    self.children = []
                return
            case LTNode():
                if isinstance(self.children[0], LiteralNode) and isinstance(self.children[1], LiteralNode):
                    self.__class__ = LiteralNode
                    self.value = str(int(self.children[0].value) < int(self.children[1].value))
                    self.children = []
            case GTEQNode():
                if isinstance(self.children[0], LiteralNode) and isinstance(self.children[1], LiteralNode):
                    self.__class__ = LiteralNode
                    self.value = str(int(self.children[0].value) >= int(self.children[1].value))
                    self.children = []
                return
            case LTEQNode():
                if isinstance(self.children[0], LiteralNode) and isinstance(self.children[1], LiteralNode):
                    self.__class__ = LiteralNode
                    self.value = str(int(self.children[0].value) <= int(self.children[1].value))
                    self.children = []
                return
            case NEQNode():
                if isinstance(self.children[0], LiteralNode) and isinstance(self.children[1], LiteralNode):
                    self.__class__ = LiteralNode
                    self.value = str(int(self.children[0].value) != int(self.children[1].value))
                    self.children = []
                return
            case SLNode():
                if isinstance(self.children[0], LiteralNode) and isinstance(self.children[1], LiteralNode):
                    self.__class__ = LiteralNode
                    self.value = str(int(self.children[0].value) << int(self.children[1].value))
                    self.children = []
                return
            case SRNode():
                if isinstance(self.children[0], LiteralNode) and isinstance(self.children[1], LiteralNode):
                    self.__class__ = LiteralNode
                    self.value = str(int(self.children[0].value) >> int(self.children[1].value))
                    self.children = []
                return
            case BitwiseAndNode():
                if isinstance(self.children[0], LiteralNode) and isinstance(self.children[1], LiteralNode):
                    self.__class__ = LiteralNode
                    self.value = str(int(self.children[0].value) & int(self.children[1].value))
                    self.children = []
                return
            case BitwiseOrNode():
                if isinstance(self.children[0], LiteralNode) and isinstance(self.children[1], LiteralNode):
                    self.__class__ = LiteralNode
                    self.value = str(int(self.children[0].value) | int(self.children[1].value))
                    self.children = []
                return
            case BitwiseXorNode():
                if isinstance(self.children[0], LiteralNode) and isinstance(self.children[1], LiteralNode):
                    self.__class__ = LiteralNode
                    self.value = str(int(self.children[0].value) ^ int(self.children[1].value))
                    self.children = []
                return
            case LogicalAndNode():
                if isinstance(self.children[0], LiteralNode) and isinstance(self.children[1], LiteralNode):
                    self.__class__ = LiteralNode
                    self.value = str(int(self.children[0].value) and int(self.children[1].value))
                    self.children = []
                return
            case LogicalOrNode():
                if isinstance(self.children[0], LiteralNode) and isinstance(self.children[1], LiteralNode):
                    self.__class__ = LiteralNode
                    self.value = str(int(self.children[0].value) or int(self.children[1].value))
                    self.children = []
                return
            case LogicalNotNode():
                if isinstance(self.children[0], LiteralNode):
                    self.__class__ = LiteralNode
                    self.value = str(not int(self.children[0].value))
                    self.children = []
                return
        return


class ProgramNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("Program", line, pos, children=children)


class MainNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("Main", line, pos, children=children)


class IdentifierNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("Identifier", line, pos, children=children)


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


class LiteralNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("Literal", line, pos, children=children)
