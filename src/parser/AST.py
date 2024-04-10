from graphviz import Source


class Node:
    def __init__(self, value: str, line: int, pos: int, children=None):
        self.value = value
        self.children = children if children is not None else []
        self.line = line
        self.pos = pos

    def constantFold(self, errors=None, warnings=None):
        if isinstance(self, IfStatementNode) or isinstance(self, ElseIfStatementNode) or isinstance(self, WhileLoopNode):
            self.condition.constantFold()
        if isinstance(self, IfStatementNode) or isinstance(self, ElseIfStatementNode) or isinstance(self, ElseStatementNode) or isinstance(self, WhileLoopNode):
            for node in self.body:
                if isinstance(node, DefinitionNode) or isinstance(node, AssignmentNode):
                    node.rvalue.constantFold(errors, warnings)
                elif not isinstance(node, str) and not isinstance(node, list):
                    if node is not None:
                        node.constantFold(errors, warnings)
        for node in self.children:
            if isinstance(node, DefinitionNode) or isinstance(node, AssignmentNode):
                node.rvalue.constantFold(errors, warnings)
            elif not isinstance(node, str) and not isinstance(node, list):
                if node is not None:
                    node.constantFold(errors, warnings)
        match self:
            case CharNode():
                return
            case IntNode():
                return
            case FloatNode():
                return
            case DivNode():
                if not (isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)):
                    return
                if not (isinstance(self.children[1], CharNode) or isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode)):
                    return
                if float(self.children[1].value) == 0:
                    if errors is not None:
                        errors.append(f"line {self.line}:{self.pos} Division by zero!")
                    return
                if isinstance(self.children[0], CharNode) and isinstance(self.children[1], CharNode):
                    self.__class__ = CharNode
                    self.value = str(int(self.children[0].value) // int(self.children[1].value))
                    self.children = []
                elif isinstance(self.children[0], IntNode) and isinstance(self.children[1], IntNode):
                    self.__class__ = IntNode
                    self.value = str(int(self.children[0].value) / int(self.children[1].value))
                    self.children = []
                elif isinstance(self.children[0], FloatNode) or isinstance(self.children[1], FloatNode):
                    self.__class__ = FloatNode
                    self.value = str(float(self.children[0].value) / float(self.children[1].value))
                    self.children = []
                else:
                    self.__class__ = IntNode
                    self.value = str(int(self.children[0].value) / int(self.children[1].value))
                    self.children = []
            case ModNode():
                if isinstance(self.children[0], FloatNode) or isinstance(self.children[1], FloatNode):
                    if errors is not None:
                        errors.append(f"line {self.line}:{self.pos} Modulus of float!")
                    return
                elif (isinstance(self.children[0], IntNode) or isinstance(self.children[0], CharNode)) and (isinstance(self.children[1], IntNode) or isinstance(self.children[1], CharNode)):
                    if int(self.children[1].value) == 0:
                        if errors is not None:
                            errors.append(f"line {self.line}:{self.pos} Division by zero!")
                        return
                    self.__class__ = IntNode
                    self.value = str(int(self.children[0].value) % int(self.children[1].value))
                    self.children = []
            case MultNode():
                if not (isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)):
                    return
                if not (isinstance(self.children[1], CharNode) or isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode)):
                    return
                if isinstance(self.children[0], CharNode) and isinstance(self.children[1], CharNode):
                    self.__class__ = CharNode
                    self.value = str(int(self.children[0].value) * int(self.children[1].value))
                    self.children = []
                elif isinstance(self.children[0], IntNode) and isinstance(self.children[1], IntNode):
                    self.__class__ = IntNode
                    self.value = str(int(self.children[0].value) * int(self.children[1].value))
                    self.children = []
                elif isinstance(self.children[0], FloatNode) or isinstance(self.children[1], FloatNode):
                    self.__class__ = FloatNode
                    self.value = str(float(self.children[0].value) * float(self.children[1].value))
                    self.children = []
                else:
                    self.__class__ = IntNode
                    self.value = str(int(self.children[0].value) * int(self.children[1].value))
                    self.children = []
            case MinusNode():
                if not (isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)):
                    return
                if not (isinstance(self.children[1], CharNode) or isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode)):
                    return
                if isinstance(self.children[0], CharNode) and isinstance(self.children[1], CharNode):
                    self.__class__ = CharNode
                    self.value = str(int(self.children[0].value) - int(self.children[1].value))
                    self.children = []
                elif isinstance(self.children[0], IntNode) and isinstance(self.children[1], IntNode):
                    self.__class__ = IntNode
                    self.value = str(int(self.children[0].value) - int(self.children[1].value))
                    self.children = []
                elif isinstance(self.children[0], FloatNode) or isinstance(self.children[1], FloatNode):
                    self.__class__ = FloatNode
                    self.value = str(float(self.children[0].value) - float(self.children[1].value))
                    self.children = []
                else:
                    self.__class__ = IntNode
                    self.value = str(int(self.children[0].value) - int(self.children[1].value))
                    self.children = []
            case PlusNode():
                if not (isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)):
                    return
                if not (isinstance(self.children[1], CharNode) or isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode)):
                    return
                if isinstance(self.children[0], CharNode) and isinstance(self.children[1], CharNode):
                    self.__class__ = CharNode
                    self.value = str(int(self.children[0].value) + int(self.children[1].value))
                    self.children = []
                elif isinstance(self.children[0], IntNode) and isinstance(self.children[1], IntNode):
                    self.__class__ = IntNode
                    self.value = str(int(self.children[0].value) + int(self.children[1].value))
                    self.children = []
                elif isinstance(self.children[0], FloatNode) or isinstance(self.children[1], FloatNode):
                    self.__class__ = FloatNode
                    self.value = str(float(self.children[0].value) + float(self.children[1].value))
                    self.children = []
                else:
                    self.__class__ = IntNode
                    self.value = str(int(self.children[0].value) + int(self.children[1].value))
                    self.children = []
            case EQNode():
                if not (isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)):
                    return
                if not (isinstance(self.children[1], CharNode) or isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode)):
                    return
                self.__class__ = IntNode
                self.value = int(float(self.children[0].value) == float(self.children[1].value))
                self.children = []
            case GTNode():
                if not (isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)):
                    return
                if not (isinstance(self.children[1], CharNode) or isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode)):
                    return
                self.__class__ = IntNode
                self.value = int(float(self.children[0].value) > float(self.children[1].value))
                self.children = []
            case LTNode():
                if not (isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)):
                    return
                if not (isinstance(self.children[1], CharNode) or isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode)):
                    return
                self.__class__ = IntNode
                self.value = int(float(self.children[0].value) < float(self.children[1].value))
                self.children = []
            case GTEQNode():
                if not (isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)):
                    return
                if not (isinstance(self.children[1], CharNode) or isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode)):
                    return
                self.__class__ = IntNode
                self.value = int(float(self.children[0].value) >= float(self.children[1].value))
                self.children = []
            case LTEQNode():
                if not (isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)):
                    return
                if not (isinstance(self.children[1], CharNode) or isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode)):
                    return
                self.__class__ = IntNode
                self.value = int(float(self.children[0].value) <= float(self.children[1].value))
                self.children = []
            case NEQNode():
                if not (isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)):
                    return
                if not (isinstance(self.children[1], CharNode) or isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode)):
                    return
                self.__class__ = IntNode
                self.value = int(float(self.children[0].value) != float(self.children[1].value))
                self.children = []
            case SLNode():
                if not (isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)):
                    return
                if not (isinstance(self.children[1], CharNode) or isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode)):
                    return
                if isinstance(self.children[0], FloatNode) or isinstance(self.children[1], FloatNode):
                    if errors is not None:
                        errors.append()
                    return
                self.__class__ = IntNode
                # Undefined behaviour
                if int(self.children[1].value) < 0:
                    self.value = None
                else:
                    self.value = int(self.children[0].value) << int(self.children[1].value)
                self.children = []
            case SRNode():
                if not (isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)):
                    return
                if not (isinstance(self.children[1], CharNode) or isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode)):
                    return
                if isinstance(self.children[0], FloatNode) or isinstance(self.children[1], FloatNode):
                    if errors is not None:
                        errors.append()
                    return
                self.__class__ = IntNode
                # Undefined behaviour
                if int(self.children[1].value) < 0:
                    self.value = None
                else:
                    self.value = int(self.children[0].value) >> int(self.children[1].value)
                self.children = []
            case BitwiseAndNode():
                if not (isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)):
                    return
                if not (isinstance(self.children[1], CharNode) or isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode)):
                    return
                self.__class__ = IntNode
                self.value = int(int(self.children[0].value) & int(self.children[1].value))
                self.children = []
            case BitwiseOrNode():
                if not (isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)):
                    return
                if not (isinstance(self.children[1], CharNode) or isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode)):
                    return
                self.__class__ = IntNode
                self.value = int(int(self.children[0].value) | int(self.children[1].value))
                self.children = []
            case BitwiseXorNode():
                if not (isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)):
                    return
                if not (isinstance(self.children[1], CharNode) or isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode)):
                    return
                self.__class__ = IntNode
                self.value = int(int(self.children[0].value) ^ int(self.children[1].value))
                self.children = []
            case LogicalAndNode():
                if not (isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)):
                    return
                if not (isinstance(self.children[1], CharNode) or isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode)):
                    return
                self.__class__ = IntNode
                self.value = int(float(self.children[0].value) and float(self.children[1].value))
                self.children = []
            case LogicalOrNode():
                if not (isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)):
                    return
                if not (isinstance(self.children[1], CharNode) or isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode)):
                    return
                self.__class__ = IntNode
                self.value = int(float(self.children[0].value) or float(self.children[1].value))
                self.children = []
            case LogicalNotNode():
                if not (isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)):
                    return
                self.__class__ = IntNode
                self.value = int(not float(self.children[0].value))
                self.children = []
            case BitwiseNotNode():
                if not (isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)):
                    return
                self.__class__ = IntNode
                self.value = int(~int(self.children[0].value))
                self.children = []


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


class BitwiseNotNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("BitwiseNot", line, pos, children=children)


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
    def __init__(self, line: int, pos: int, type: str, rval, children=None):
        super().__init__("ExplicitConversion", line, pos, children=children)
        self.type = type
        self.rval = rval


class PrintfNode(Node):
    def __init__(self, line: int, pos: int, specifier, node, children=None):
        super().__init__("Printf", line, pos, children=children)
        self.specifier = specifier
        self.node = node


class FormatSpecifierNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("FormatSpecifier", line, pos, children=children)


class TypedefNode(Node):
    def __init__(self, line: int, pos: int, type: Node, identifier: IdentifierNode, children=None):
        super().__init__("Typedef", line, pos, children=children)
        self.type = type
        self.identifier = identifier


class IfStatementNode(Node):
    def __init__(self, line: int, pos: int, condition: Node, body: list, children=None):
        super().__init__("IfStatement", line, pos, children=children)
        self.condition = condition
        self.body = body


class ElseIfStatementNode(Node):
    def __init__(self, line: int, pos: int, condition: Node, body: list, children=None):
        super().__init__("ElseIfStatement", line, pos, children=children)
        self.condition = condition
        self.body = body


class ElseStatementNode(Node):
    def __init__(self, line: int, pos: int, body: list, children=None):
        super().__init__("ElseStatement", line, pos, children=children)
        self.body = body


class WhileLoopNode(Node):
    def __init__(self, line: int, pos: int, condition: Node, body: list, children=None):
        super().__init__("While", line, pos, children=children)
        self.condition = condition
        self.body = body


class BreakNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("Break", line, pos, children=children)


class ContinueNode(Node):
    def __init__(self, line: int, pos: int, children=None):
        super().__init__("Continue", line, pos, children=children)
