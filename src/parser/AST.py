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
        node = self
        if isinstance(node, DefinitionNode) or isinstance(node, AssignmentNode):
            node = self.rvalue
        match node:
            case IntNode():
                return
            case FloatNode():
                return
            case DivNode():
                if isinstance(node.children[0], IntNode) and isinstance(node.children[1], IntNode):
                    node.__class__ = IntNode
                    node.value = str(int(node.children[0].value) // int(node.children[1].value))
                    node.children = []
                elif isinstance(node.children[0], FloatNode) and isinstance(node.children[1], FloatNode):
                    node.__class__ = FloatNode
                    node.value = str(float(node.children[0].value) / float(node.children[1].value))
                    node.children = []
                elif isinstance(node.children[0], FloatNode) and isinstance(node.children[1], IntNode):
                    node.__class__ = FloatNode
                    node.value = str(float(node.children[0].value) / float(node.children[1].value))
                    node.children = []
                elif isinstance(node.children[0], IntNode) and isinstance(node.children[1], FloatNode):
                    node.__class__ = FloatNode
                    node.value = str(float(node.children[0].value) / float(node.children[1].value))
                    node.children = []
                return
            case ModNode():
                if isinstance(node.children[0], IntNode) and isinstance(node.children[1], IntNode):
                    node.__class__ = IntNode
                    node.value = str(int(node.children[0].value) % int(node.children[1].value))
                    node.children = []
                return
            case MultNode():
                if isinstance(node.children[0], IntNode) and isinstance(node.children[1], IntNode):
                    node.__class__ = IntNode
                    node.value = str(int(node.children[0].value) * int(node.children[1].value))
                    node.children = []
                    return
                elif isinstance(node.children[0], FloatNode) or isinstance(node.children[1], FloatNode):
                    node.__class__ = FloatNode
                    node.value = str(float(node.children[0].value) * float(node.children[1].value))
                    node.children = []
                    return
                elif (isinstance(node.children[0], IntNode) or isinstance(node.children[0], FloatNode)) and \
                        node.children[0].value == 0:
                    node.__class__ = IntNode
                    node.children = []
                    node.value = "0"
                    return
                elif (isinstance(node.children[1], IntNode) or isinstance(node.children[1], FloatNode)) and \
                        node.children[1].value == 0:
                    node.__class__ = IntNode
                    node.children = []
                    node.value = "0"
                return
            case MinusNode():
                if isinstance(node.children[0], IntNode) and isinstance(node.children[1], IntNode):
                    node.__class__ = IntNode
                    node.value = str(int(node.children[0].value) - int(node.children[1].value))
                    node.children = []
                elif isinstance(node.children[0], FloatNode) or isinstance(node.children[1], FloatNode):
                    node.__class__ = FloatNode
                    node.value = str(float(node.children[0].value) - float(node.children[1].value))
                    node.children = []
                return
            case PlusNode():
                if isinstance(node.children[0], IntNode) and isinstance(node.children[1], IntNode):
                    node.__class__ = IntNode
                    node.value = str(int(node.children[0].value) + int(node.children[1].value))
                    node.children = []
                    return
                elif isinstance(node.children[0], FloatNode) or isinstance(node.children[1], FloatNode):
                    node.__class__ = FloatNode
                    node.value = str(float(node.children[0].value) + float(node.children[1].value))
                    node.children = []
                    return
            case EQNode():
                node.__class__ = IntNode
                node.value = int(float(node.children[0].value) == float(node.children[1].value))
                node.children = []
                return
            case GTNode():
                node.__class__ = IntNode
                node.value = int(float(node.children[0].value) > float(node.children[1].value))
                node.children = []
                return
            case LTNode():
                node.__class__ = IntNode
                node.value = int(float(node.children[0].value) < float(node.children[1].value))
                node.children = []
            case GTEQNode():
                node.__class__ = IntNode
                node.value = int(float(node.children[0].value) >= float(node.children[1].value))
                node.children = []
                return
            case LTEQNode():
                node.__class__ = IntNode
                node.value = int(float(node.children[0].value) <= float(node.children[1].value))
                node.children = []
                return
            case NEQNode():
                node.__class__ = IntNode
                node.value = int(float(node.children[0].value) != float(node.children[1].value))
                node.children = []
                return
            case SLNode():
                if isinstance(node.children[0], IntNode) and isinstance(node.children[1], IntNode):
                    node.__class__ = IntNode
                    node.value = int(node.children[0].value) << int(node.children[1].value)
                    node.children = []
                return
            case SRNode():
                if isinstance(node.children[0], IntNode) and isinstance(node.children[1], IntNode):
                    node.__class__ = IntNode
                    node.value = str(int(node.children[0].value) >> int(node.children[1].value))
                    node.children = []
                return
            case BitwiseAndNode():
                node.__class__ = IntNode
                node.value = int(int(node.children[0].value) & int(node.children[1].value))
                node.children = []
                return
            case BitwiseOrNode():
                node.__class__ = IntNode
                node.value = int(int(node.children[0].value) | int(node.children[1].value))
                node.children = []
                return
            case BitwiseXorNode():
                node.__class__ = IntNode
                node.value = int(int(node.children[0].value) ^ int(node.children[1].value))
                node.children = []
                return
            case LogicalAndNode():
                node.__class__ = IntNode
                node.value = int(float(node.children[0].value) and float(node.children[1].value))
                node.children = []
                return
            case LogicalOrNode():
                node.__class__ = IntNode
                node.value = int(float(node.children[0].value) or float(node.children[1].value))
                node.children = []
                return
            case LogicalNotNode():
                node.__class__ = IntNode
                node.value = int(not float(node.children[0].value))
                node.children = []
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
    def __init__(self, value: int, line: int, pos: int, type: TypeNode, children=None):
        super().__init__(str(value), line, pos, children=children)
        self.type = type


class DerefNode(Node):
    def __init__(self, value: int, line: int, pos: int, identifier: str, children=None):
        super().__init__(str(value), line, pos, children=children)
        self.identifier=identifier


class AddrNode(Node):
    def __init__(self, value, line: int, pos: int, children=None):
        super().__init__(value, line, pos, children=children)


class DeclarationNode(Node):
    def __init__(self, line: int, pos: int, type: Node, lvalue: IdentifierNode, children=None):
            super().__init__("Declaration", line, pos, children=children)
            self.type = type
            self.lvalue = lvalue


class CommentNode(Node):
    def __init__(self, value, line: int, pos: int, children=None):
        super().__init__(value, line, pos, children=children)


class PostFixNode(Node):
    def __init__(self, value: str, line: int, pos: int, op: str, children=None):
        super().__init__(value, line, pos, children=children)
        self.op = op


class PreFixNode(Node):
    def __init__(self, value: str, line: int, pos: int, op: str, children=None):
        super().__init__(value, line, pos, children=children)
        self.op = op


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


class CharNode(Node):
    def __init__(self, value, line: int, pos: int, children=None):
        super().__init__(value, line, pos, children=children)


class IntNode(Node):
    def __init__(self, value, line: int, pos: int, children=None):
        super().__init__(value, line, pos, children=children)


class FloatNode(Node):
    def __init__(self, value, line: int, pos: int, children=None):
        super().__init__(value, line, pos, children=children)


class ExplicitConversionNode(Node):
    def __init__(self, line: int, pos: int, type: str):
        super().__init__("ExplicitConversion", line, pos, children=None)
        self.type = type

