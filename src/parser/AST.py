from graphviz import Source

class Node:
    def __init__(self, value: str, line: int, pos: int, children=None):
        self.value = value
        self.children = children if children is not None else []
        self.line = line
        self.pos = pos

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
                if isinstance(self.children[0], IntNode) and isinstance(self.children[1], IntNode):
                    self.__class__ = IntNode
                    self.value = str(int(self.children[0].value) // int(self.children[1].value))
                    self.children = []
                elif isinstance(self.children[0], FloatNode) and isinstance(self.children[1], FloatNode):
                    self.__class__ = FloatNode
                    self.value = str(float(self.children[0].value) / float(self.children[1].value))
                    self.children = []
                elif isinstance(self.children[0], FloatNode) and isinstance(self.children[1], IntNode):
                    self.__class__ = FloatNode
                    self.value = str(float(self.children[0].value) / float(self.children[1].value))
                    self.children = []
                elif isinstance(self.children[0], IntNode) and isinstance(self.children[1], FloatNode):
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
                elif isinstance(self.children[0], FloatNode) or isinstance(self.children[1], FloatNode):
                    self.__class__ = FloatNode
                    self.value = str(float(self.children[0].value) * float(self.children[1].value))
                    self.children = []
                    return
                elif (isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)) and \
                        self.children[0].value == 0:
                    self.__class__ = IntNode
                    self.children = []
                    self.value = "0"
                    return
                elif (isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode)) and \
                        self.children[1].value == 0:
                    self.__class__ = IntNode
                    self.children = []
                    self.value = "0"
                return
            case MinusNode():
                if isinstance(self.children[0], IntNode) and isinstance(self.children[1], IntNode):
                    self.__class__ = IntNode
                    self.value = str(int(self.children[0].value) - int(self.children[1].value))
                    self.children = []
                elif isinstance(self.children[0], FloatNode) or isinstance(self.children[1], FloatNode):
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
                elif isinstance(self.children[0], FloatNode) or isinstance(self.children[1], FloatNode):
                    self.__class__ = FloatNode
                    self.value = str(float(self.children[0].value) + float(self.children[1].value))
                    self.children = []
                    return
            case EQNode():
                self.__class__ = IntNode
                self.value = int(float(self.children[0].value) == float(self.children[1].value))
                self.children = []
                return
            case GTNode():
                self.__class__ = IntNode
                self.value = int(float(self.children[0].value) > float(self.children[1].value))
                self.children = []
                return
            case LTNode():
                self.__class__ = IntNode
                self.value = int(float(self.children[0].value) < float(self.children[1].value))
                self.children = []
            case GTEQNode():
                self.__class__ = IntNode
                self.value = int(float(self.children[0].value) >= float(self.children[1].value))
                self.children = []
                return
            case LTEQNode():
                self.__class__ = IntNode
                self.value = int(float(self.children[0].value) <= float(self.children[1].value))
                self.children = []
                return
            case NEQNode():
                self.__class__ = IntNode
                self.value = int(float(self.children[0].value) != float(self.children[1].value))
                self.children = []
                return
            case SLNode():
                if isinstance(self.children[0], IntNode) and isinstance(self.children[1], IntNode):
                    self.__class__ = IntNode
                    self.value = int(self.children[0].value) << int(self.children[1].value)
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
                self.value = int(int(self.children[0].value) & int(self.children[1].value))
                self.children = []
                return
            case BitwiseOrNode():
                self.__class__ = IntNode
                self.value = int(int(self.children[0].value) | int(self.children[1].value))
                self.children = []
                return
            case BitwiseXorNode():
                self.__class__ = IntNode
                self.value = int(int(self.children[0].value) ^ int(self.children[1].value))
                self.children = []
                return
            case LogicalAndNode():
                self.__class__ = IntNode
                self.value = int(float(self.children[0].value) and float(self.children[1].value))
                self.children = []
                return
            case LogicalOrNode():
                self.__class__ = IntNode
                self.value = int(float(self.children[0].value) or float(self.children[1].value))
                self.children = []
                return
            case LogicalNotNode():
                self.__class__ = IntNode
                self.value = int(not float(self.children[0].value))
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


class AddrNode(Node):
    def __init__(self, value, line: int, pos: int, children=None):
        super().__init__(value, line, pos, children=children)


class DeclarationNode(Node):
        def __init__(self, line: int, pos: int, type: Node, lvalue: IdentifierNode, children=None):
            super().__init__("Declaration", line, pos, children=children)
            self.type = type
            self.lvalue = lvalue

class AssignmentNode(Node):
    def __init__(self, line: int, pos: int, lvalue: IdentifierNode, rvalue: Node, children=None):
        super().__init__("Assignment", line, pos, children=children)
        self.lvalue = lvalue
        self.rvalue = rvalue


class DefinitionNode(Node):
    def __init__(self, line: int, pos: int, type: Node, lvalue: IdentifierNode, rvalue: Node, children=None):
        super().__init__("Definition", line, pos, children=children)
        self.type = type
        self.lvalue = lvalue
        self.rvalue = rvalue


class IntNode(Node):
    def __init__(self, value, line: int, pos: int, children=None):
        super().__init__(value, line, pos, children=children)


class FloatNode(Node):
    def __init__(self, value, line: int, pos: int, children=None):
        super().__init__(value, line, pos, children=children)
