from src.parser.SymbolTable import Symbol


class Node:
    def __init__(self, value: str, line: int, column: int, original_code: str | None, children=None):
        self.value = value
        self.line = line
        self.column = column
        self.original = original_code
        self.children = children if children is not None else []

    def constant_fold(self, errors=None, warnings=None, parent=None):
        if isinstance(self, IfStatementNode) or isinstance(self, WhileLoopNode):
            self.condition.constant_fold()
            # Remove conditionals that are never true
            if isinstance(self.condition, CharNode) or isinstance(self.condition, IntNode) or isinstance(self.condition, FloatNode):
                if float(self.condition.value) == 0:
                    return True
        if isinstance(self, IfStatementNode) or isinstance(self, WhileLoopNode) or isinstance(self, FunctionNode):
            delete = []
            for node in self.body:
                if isinstance(node, DefinitionNode) or isinstance(node, AssignmentNode):
                    node.rvalue.constant_fold(errors, warnings, self)
                elif not isinstance(node, str) and not isinstance(node, list):
                    if node is not None:
                        result = node.constant_fold(errors, warnings, self)
                        if result:
                            delete.append(node)
            for node in delete:
                self.body.remove(node)
        else:
            delete = []
            for node in self.children:
                if isinstance(node, DefinitionNode) or isinstance(node, AssignmentNode):
                    node.rvalue.constant_fold(errors, warnings, self)
                elif not isinstance(node, str) and not isinstance(node, list):
                    if node is not None:
                        result = node.constant_fold(errors, warnings, self)
                        if result:
                            delete.append(node)
            for node in delete:
                self.children.remove(node)
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
                        errors.append(f"line {self.line}:{self.column} Division by zero!")
                    return
                if isinstance(self.children[0], CharNode) and isinstance(self.children[1], CharNode):
                    self.__class__ = CharNode
                    self.value = str(int(self.children[0].value) // int(self.children[1].value))
                    self.children = []
                elif isinstance(self.children[0], IntNode) and isinstance(self.children[1], IntNode):
                    self.__class__ = IntNode
                    self.value = str(int(self.children[0].value) // int(self.children[1].value))
                    self.children = []
                elif isinstance(self.children[0], FloatNode) or isinstance(self.children[1], FloatNode):
                    self.__class__ = FloatNode
                    self.value = str(float(self.children[0].value) / float(self.children[1].value))
                    self.children = []
                else:
                    self.__class__ = IntNode
                    self.value = str(int(self.children[0].value) // int(self.children[1].value))
                    self.children = []
            case ModNode():
                if isinstance(self.children[0], FloatNode) or isinstance(self.children[1], FloatNode):
                    if errors is not None:
                        errors.append(f"line {self.line}:{self.column} Modulus of float!")
                    return
                elif (isinstance(self.children[0], IntNode) or isinstance(self.children[0], CharNode)) and (isinstance(self.children[1], IntNode) or isinstance(self.children[1], CharNode)):
                    if int(self.children[1].value) == 0:
                        if errors is not None:
                            errors.append(f"line {self.line}:{self.column} Division by zero!")
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
                if isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode):
                    if float(self.children[0].value) == 0:
                        self.__class__ = IntNode
                        self.value = int(0)
                        self.children = []
                        return
                if isinstance(self.children[1], CharNode) or isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode):
                    if float(self.children[1].value) == 0:
                        self.__class__ = IntNode
                        self.value = int(0)
                        self.children = []
                        return
                if not (isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)):
                    return
                if not (isinstance(self.children[1], CharNode) or isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode)):
                    return
                self.__class__ = IntNode
                if float(self.children[0].value) == 0 or float(self.children[1].value) == 0:
                    self.value = 0
                else:
                    self.value = 1
                self.children = []
            case LogicalOrNode():
                if isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode):
                    if float(self.children[0].value) == 1:
                        self.__class__ = IntNode
                        self.value = int(1)
                        self.children = []
                        return
                if isinstance(self.children[1], CharNode) or isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode):
                    if float(self.children[1].value) == 1:
                        self.__class__ = IntNode
                        self.value = int(1)
                        self.children = []
                        return
                if not (isinstance(self.children[0], CharNode) or isinstance(self.children[0], IntNode) or isinstance(self.children[0], FloatNode)):
                    return
                if not (isinstance(self.children[1], CharNode) or isinstance(self.children[1], IntNode) or isinstance(self.children[1], FloatNode)):
                    return
                self.__class__ = IntNode
                self.value = int(float(self.children[0].value) != 0 or float(self.children[1].value) != 0)
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

    def remove_forward_declarations(self):
        # Find forward declarations
        forward_declarations = []
        for node in self.children:
            if isinstance(node, FunctionNode):
                if len(node.body) == 0:
                    forward_declarations.append(node)

        # replace forward declaration with definition
        for forward_declaration in forward_declarations:
            definition = None
            function_name = forward_declaration.value
            for node in self.children:
                if isinstance(node, FunctionNode) and node is not forward_declaration:
                    if node.value == function_name:
                        definition = node
                        break
            if definition is not None:
                index = self.children.index(forward_declaration)
                self.children[index] = definition

    def replace_enum(self, symbolTable):
        # Remove enum nodes
        self._remove_enum_nodes()

        # Replace enum with int
        for node in self.children:
            self._replace_enum_with_int(node, symbolTable.get_all_enums())

    def _remove_enum_nodes(self):
        remove = []
        for node in self.children:
            if isinstance(node, EnumNode):
                remove.append(node)

        for node in remove:
            self.children.remove(node)

    def _replace_enum_with_int(self, node, enums):
        if isinstance(node, DeclarationNode):
            if node.type[-1].value in enums:
                node.type[-1].value = "int"
        elif isinstance(node, DefinitionNode):
            if node.type[-1].value in enums:
                node.type[-1].value = "int"
        elif isinstance(node, FunctionNode):
            for child in node.body:
                self._replace_enum_with_int(child, enums)




class ProgramNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="Program", line=line, column=column, original_code=original, children=children)


class FunctionNode(Node):
    def __init__(self, value: str, line: int, column: int, original: str | None, return_type: Node | str, params: list, body: list, children=None):
        super().__init__(value=value, line=line, column=column, original_code=original, children=children)
        self.type = return_type
        self.params = params
        self.body = body


class FunctionCallNode(Node):
    def __init__(self, value: str, line: int, column: int, original: str | None, arguments, children=None):
        super().__init__(value=value, line=line, column=column, original_code=original, children=children)
        self.arguments = arguments


class IdentifierNode(Node):
    def __init__(self, value, line: int, column: int, original: str | None, children=None):
        super().__init__(value, line, column, original, children=children)


class TypeNode(Node):
    def __init__(self, value, line: int, column: int, original: str | None, children=None):
        super().__init__(value, line, column, original, children=children)


class LogicalNotNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="LogicalNot", line=line, column=column, original_code=original, children=children)


class BitwiseNotNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="BitwiseNot", line=line, column=column, original_code=original, children=children)


class DivNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="Div", line=line, column=column, original_code=original, children=children)


class ModNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="Mod", line=line, column=column, original_code=original, children=children)


class MultNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="Mul", line=line, column=column, original_code=original, children=children)


class MinusNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="Minus", line=line, column=column, original_code=original, children=children)


class PlusNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="Plus", line=line, column=column, original_code=original, children=children)


class GTNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="GT", line=line, column=column, original_code=original, children=children)


class LTNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="LT", line=line, column=column, original_code=original, children=children)


class GTEQNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="GTEQ", line=line, column=column, original_code=original, children=children)


class LTEQNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="LTEQ", line=line, column=column, original_code=original, children=children)


class EQNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="EQ", line=line, column=column, original_code=original, children=children)


class NEQNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="NEQ", line=line, column=column, original_code=original, children=children)


class SLNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="SL", line=line, column=column, original_code=original, children=children)


class SRNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="SR", line=line, column=column, original_code=original, children=children)


class BitwiseAndNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="BitwiseAnd", line=line, column=column, original_code=original, children=children)


class BitwiseOrNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="BitwiseOr", line=line, column=column, original_code=original, children=children)


class BitwiseXorNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="BitwiseXor", line=line, column=column, original_code=original, children=children)


class LogicalAndNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="LogicalAnd", line=line, column=column, original_code=original, children=children)


class LogicalOrNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="LogicalOr", line=line, column=column, original_code=original, children=children)


class PointerNode(Node):
    def __init__(self, value: int, line: int, column: int, original: str | None, type: TypeNode, children=None):
        super().__init__(str(value), line, column, original, children=children)
        self.type = type


class DerefNode(Node):
    def __init__(self, value: int, line: int, column: int, original: str | None, identifier: IdentifierNode, children=None):
        super().__init__(str(value), line, column, original, children=children)
        self.identifier = identifier


class AddrNode(Node):
    def __init__(self, value, line: int, column: int, original: str | None, children=None):
        super().__init__(value, line, column, original, children=children)


class DeclarationNode(Node):
    def __init__(self, line: int, column: int, original: str | None, type: Node | list, lvalue: IdentifierNode, children=None):
            super().__init__(value="Declaration", line=line, column=column, original_code=original, children=children)
            self.type = type
            self.lvalue = lvalue


class CommentNode(Node):
    def __init__(self, value, line: int, column: int, original: str | None, children=None):
        super().__init__(value, line, column, original, children=children)


class PostFixNode(Node):
    def __init__(self, value: str, line: int, column: int, original: str | None, op: str, children=None):
        super().__init__(value, line, column, original, children=children)
        self.op = op


class PreFixNode(Node):
    def __init__(self, value: str, line: int, column: int, original: str | None, op: str, children=None):
        super().__init__(value, line, column, original, children=children)
        self.op = op


class AssignmentNode(Node):
    def __init__(self, line: int, column: int, original: str | None, lvalue: IdentifierNode, rvalue: Node, children=None):
        super().__init__(value="Assignment", line=line, column=column, original_code=original, children=children)
        self.lvalue = lvalue
        self.rvalue = rvalue


class DefinitionNode(Node):
    def __init__(self, line: int, column: int, original: str | None, type: Node | list, lvalue: IdentifierNode, rvalue: Node, children=None):
        super().__init__(value="Definition", line=line, column=column, original_code=original, children=children)
        self.type = type
        self.lvalue = lvalue
        self.rvalue = rvalue


class CharNode(Node):
    def __init__(self, value, line: int, column: int, original: str | None, children=None):
        super().__init__(value, line, column, original, children=children)


class IntNode(Node):
    def __init__(self, value, line: int, column: int, original: str | None, children=None):
        super().__init__(value, line, column, original, children=children)


class FloatNode(Node):
    def __init__(self, value, line: int, column: int, original: str | None, children=None):
        super().__init__(value, line, column, original, children=children)


class StringNode(Node):
    def __init__(self, value, line: int, column: int, original: str | None, children=None):
        super().__init__(value, line, column, original, children=children)


class ExplicitConversionNode(Node):
    def __init__(self, line: int, column: int, original: str | None, type: str, rvalue, children=None):
        super().__init__(value="ExplicitConversion", line=line, column=column, original_code=original, children=children)
        self.type = type
        self.rvalue = rvalue


class PrintfNode(Node):
    def __init__(self, line: int, column: int, original: str | None, specifier, children=None):
        super().__init__(value="Printf", line=line, column=column, original_code=original, children=children)
        self.specifier = specifier


class FormatSpecifierNode(Node):
    def __init__(self, line: int, column: int, original: str | None, specifier: str, children=None):
        super().__init__(value="FormatSpecifier", line=line, column=column, original_code=original, children=children)
        self.specifier = specifier


class TypedefNode(Node):
    def __init__(self, line: int, column: int, original: str | None, type: Node, identifier: IdentifierNode, children=None):
        super().__init__(value="Typedef", line=line, column=column, original_code=original, children=children)
        self.type = type
        self.identifier = identifier


class IfStatementNode(Node):
    def __init__(self, line: int, column: int, original: str | None, condition: Node, body: list, children=None):
        super().__init__(value="IfStatement", line=line, column=column, original_code=original, children=children)
        self.condition = condition
        self.body = body


class ElseIfStatementNode(Node):
    def __init__(self, line: int, column: int, original: str | None, condition: Node, body: list, children=None):
        super().__init__(value="ElseIfStatement", line=line, column=column, original_code=original, children=children)
        self.condition = condition
        self.body = body


class ElseStatementNode(Node):
    def __init__(self, line: int, column: int, original: str | None, body: list, children=None):
        super().__init__(value="ElseStatement", line=line, column=column, original_code=original, children=children)
        self.body = body


class WhileLoopNode(Node):
    def __init__(self, line: int, column: int, original: str | None, condition: Node, body: list, children=None):
        super().__init__(value="While", line=line, column=column, original_code=original, children=children)
        self.condition = condition
        self.body = body


class BreakNode(Node):
    def __init__(self, line: int, column: int, original: str | None, valid=False, children=None):
        super().__init__(value="Break", line=line, column=column, original_code=original, children=children)
        self.valid = valid


class ContinueNode(Node):
    def __init__(self, line: int, column: int, original: str | None, valid=False, children=None):
        super().__init__(value="Continue", line=line, column=column, original_code=original, children=children)
        self.valid = valid


class ReturnNode(Node):
    def __init__(self, line: int, column: int, original: str | None, ret_val: Node, valid=False, children=None):
        super().__init__(value="Return", line=line, column=column, original_code=original, children=children)
        self.return_value = ret_val
        self.valid = valid


class CaseNode(Node):
    def __init__(self, line: int, column: int, original: str | None, condition, children=None):
        super().__init__(value="Case", line=line, column=column, original_code=original, children=children)
        self.condition = condition


class EnumNode(Node):
    def __init__(self, line: int, pos: int, original: str | None, enum_name: str, enum_list: list, children=None):
        super().__init__(value="Enum", line=line, column=pos, original_code=original, children=children)
        self.enum_name = enum_name
        self.enum_list = enum_list


class ArrayNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None, array=None):
        super().__init__(value="Array", line=line, column=column, original_code=original, children=children)
        self.array = array


class ArrayIdentifierNode(Node):
    def __init__(self, line: int, column: int, original: str | None, identifier: Symbol, indices: list, children=None):
        super().__init__(value=identifier.name, line=line, column=column, original_code=original, children=children)
        self.indices = indices


class ScopeNode(Node):
    def __init__(self, line: int, column: int, original: str | None, children=None):
        super().__init__(value="Scope", line=line, column=column, original_code=original, children=children)


class StructNode(Node):
    def __init__(self, line: int, column: int, original: str | None, struct_name: str, struct_members: list, children=None):
        super().__init__(value="Struct", line=line, column=column, original_code=original, children=children)
        self.struct_name = struct_name
        self.struct_members = struct_members


class StructMemberNode(Node):
    def __init__(self, line: int, column: int, original: str | None, type: TypeNode, struct_var_name: str, struct_member_name: str, array_size= None, children=None):
        super().__init__(value="StructMember", line=line, column=column, original_code=original, children=children)
        self.type = type
        self.struct_var_name = struct_var_name
        self.struct_member_name = struct_member_name
        self.array_size = array_size


class StructAssignmentNode(Node):
    def __init__(self, line: int, column: int, original: str | None, lvalue: Node, rvalue: Node, children=None):
        super().__init__(value="StructAssignment", line=line, column=column, original_code=original, children=children)
        self.lvalue = lvalue
        self.rvalue = rvalue


class ArrayDeclarationNode(Node):
    def __init__(self, line: int, column: int, original: str | None, type: TypeNode, lvalue: IdentifierNode, size: list, children=None):
        super().__init__(value="ArrayDeclaration", line=line, column=column, original_code=original, children=children)
        self.type = type
        self.lvalue = lvalue
        self.size = size


class ArrayDefinitionNode(Node):
    def __init__(self, line: int, column: int, original: str | None, type: TypeNode, lvalue: IdentifierNode, size: list, rvalue: Node, children=None):
        super().__init__(value="ArrayDefinition", line=line, column=column, original_code=original, children=children)
        self.type = type
        self.lvalue = lvalue
        self.size = size
        self.rvalue = rvalue


class ArrayAssignmentNode(Node):
    def __init__(self, line: int, column: int, original: str | None, lvalue: Node, rvalue: Node, children=None):
        super().__init__(value="ArrayAssignment", line=line, column=column, original_code=original, children=children)
        self.lvalue = lvalue
        self.rvalue = rvalue


class ScanfNode(Node):
    def __init__(self, line: int, column: int, original: str | None, specifier, children=None):
        super().__init__(value="scanf", line=line, column=column, original_code=original, children=children)
        self.specifier = specifier


class StructDeclarationNode(Node):
    def __init__(self, line: int, column: int, original: str | None, type: TypeNode, lvalue: IdentifierNode, children=None):
        super().__init__(value="StructDeclaration", line=line, column=column, original_code=original, children=children)
        self.type = type
        self.lvalue = lvalue


class StructDefinitionNode(Node):
    def __init__(self, line: int, column: int, original: str | None, type: TypeNode, lvalue: IdentifierNode, rvalue: Node, children=None):
        super().__init__(value="StructDefinition", line=line, column=column, original_code=original, children=children)
        self.type = type
        self.lvalue = lvalue
        self.rvalue = rvalue


class StructPostFixNode(Node):
    def __init__(self, line: int, column: int, original: str | None, struct_member: StructMemberNode, op: str, children=None):
        super().__init__(value="StructMember", line=line, column=column, original_code=original, children=children)
        self.struct_member = struct_member
        self.op = op


class StructPreFixNode(Node):
    def __init__(self, line: int, column: int, original: str | None, struct_member: StructMemberNode, op: str, children=None):
        super().__init__(value="StructMember", line=line, column=column, original_code=original, children=children)
        self.struct_member = struct_member
        self.op = op
