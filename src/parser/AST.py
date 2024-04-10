from graphviz import Source


class Node:
    def __init__(self, value: str, line: int, pos: int, original_code: str | None, children=None):
        self.value = value
        self.line = line
        self.pos = pos
        self.original = original_code
        self.children = children if children is not None else []

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
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="Program", line=line, pos=pos, original_code=original, children=children)


class MainNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="Main", line=line, pos=pos, original_code=original, children=children)


class StatementNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="Statement", line=line, pos=pos, original_code=original, children=children)


class IdentifierNode(Node):
    def __init__(self, value, line: int, pos: int, original: str | None, children=None):
        super().__init__(value, line, pos, original, children=children)


class TypeNode(Node):
    def __init__(self, value, line: int, pos: int, original: str | None, children=None):
        super().__init__(value, line, pos, original, children=children)


class LogicalNotNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="LogicalNot", line=line, pos=pos, original_code=original, children=children)


class BitwiseNotNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="BitwiseNot", line=line, pos=pos, original_code=original, children=children)


class DivNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="Div", line=line, pos=pos, original_code=original, children=children)


class ModNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="Mod", line=line, pos=pos, original_code=original, children=children)


class MultNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="Mul", line=line, pos=pos, original_code=original, children=children)


class MinusNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="Minus", line=line, pos=pos, original_code=original, children=children)


class PlusNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="Plus", line=line, pos=pos, original_code=original, children=children)


class GTNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="GT", line=line, pos=pos, original_code=original, children=children)


class LTNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="LT", line=line, pos=pos, original_code=original, children=children)


class GTEQNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="GTEQ", line=line, pos=pos, original_code=original, children=children)


class LTEQNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="LTEQ", line=line, pos=pos, original_code=original, children=children)


class EQNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="EQ", line=line, pos=pos, original_code=original, children=children)


class NEQNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="NEQ", line=line, pos=pos, original_code=original, children=children)


class SLNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="SL", line=line, pos=pos, original_code=original, children=children)


class SRNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="SR", line=line, pos=pos, original_code=original, children=children)


class BitwiseAndNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="BitwiseAnd", line=line, pos=pos, original_code=original, children=children)


class BitwiseOrNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="BitwiseOr", line=line, pos=pos, original_code=original, children=children)


class BitwiseXorNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="BitwiseXor", line=line, pos=pos, original_code=original, children=children)


class LogicalAndNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="LogicalAnd", line=line, pos=pos, original_code=original, children=children)


class LogicalOrNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="LogicalOr", line=line, pos=pos, original_code=original, children=children)


class PointerNode(Node):
    def __init__(self, value: int, line: int, pos: int, original: str | None, type: TypeNode, children=None):
        super().__init__(str(value), line, pos, original, children=children)
        self.type = type


class DerefNode(Node):
    def __init__(self, value: int, line: int, pos: int, original: str | None, identifier: str, children=None):
        super().__init__(str(value), line, pos, original, children=children)
        self.identifier=identifier


class AddrNode(Node):
    def __init__(self, value, line: int, pos: int, original: str | None, children=None):
        super().__init__(value, line, pos, original, children=children)


class DeclarationNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, type: Node | list, lvalue: IdentifierNode, children=None):
            super().__init__(value="Declaration", line=line, pos=pos, original_code=original, children=children)
            self.type = type
            self.lvalue = lvalue


class CommentNode(Node):
    def __init__(self, value, line: int, pos: int, original: str | None, children=None):
        super().__init__(value, line, pos, original, children=children)


class PostFixNode(Node):
    def __init__(self, value: str, line: int, pos: int, original: str | None, op: str, children=None):
        super().__init__(value, line, pos, original, children=children)
        self.op = op


class PreFixNode(Node):
    def __init__(self, value: str, line: int, pos: int, original: str | None, op: str, children=None):
        super().__init__(value, line, pos, original, children=children)
        self.op = op


class AssignmentNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, lvalue: IdentifierNode, rvalue: Node, children=None):
        super().__init__(value="Assignment", line=line, pos=pos, original_code=original, children=children)
        self.lvalue = lvalue
        self.rvalue = rvalue


class DefinitionNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, type: Node | list, lvalue: IdentifierNode, rvalue: Node, children=None):
        super().__init__(value="Definition", line=line, pos=pos, original_code=original, children=children)
        self.type = type
        self.lvalue = lvalue
        self.rvalue = rvalue


class CharNode(Node):
    def __init__(self, value, line: int, pos: int, original: str | None, children=None):
        super().__init__(value, line, pos, original, children=children)


class IntNode(Node):
    def __init__(self, value, line: int, pos: int, original: str | None, children=None):
        super().__init__(value, line, pos, original, children=children)


class FloatNode(Node):
    def __init__(self, value, line: int, pos: int, original: str | None, children=None):
        super().__init__(value, line, pos, original, children=children)


class ExplicitConversionNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, type: str, rval, children=None):
        super().__init__(value="ExplicitConversion", line=line, pos=pos, original_code=original, children=children)
        self.type = type
        self.rval = rval


class PrintfNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, specifier, node, children=None):
        super().__init__(value="Printf", line=line, pos=pos, original_code=original, children=children)
        self.specifier = specifier
        self.node = node


class FormatSpecifierNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, specifier: str, children=None):
        super().__init__(value="FormatSpecifier", line=line, pos=pos, original_code=original, children=children)
        self.specifier = specifier


class TypedefNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, type: Node, identifier: IdentifierNode, children=None):
        super().__init__(value="Typedef", line=line, pos=pos, original_code=original, children=children)
        self.type = type
        self.identifier = identifier


class IfStatementNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, condition: Node, body: list, children=None):
        super().__init__(value="IfStatement", line=line, pos=pos, original_code=original, children=children)
        self.condition = condition
        self.body = body


class ElseIfStatementNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, condition: Node, body: list, children=None):
        super().__init__(value="ElseIfStatement", line=line, pos=pos, original_code=original, children=children)
        self.condition = condition
        self.body = body


class ElseStatementNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, body: list, children=None):
        super().__init__(value="ElseStatement", line=line, pos=pos, original_code=original, children=children)
        self.body = body


class WhileLoopNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, condition: Node, body: list, children=None):
        super().__init__(value="While", line=line, pos=pos, original_code=original, children=children)
        self.condition = condition
        self.body = body


class BreakNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="Break", line=line, pos=pos, original_code=original, children=children)


class ContinueNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, children=None):
        super().__init__(value="Continue", line=line, pos=pos, original_code=original, children=children)


class CaseNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, condition, children=None):
        super().__init__(value="Case", line=line, pos=pos, original_code=original, children=children)
        self.condition = condition
