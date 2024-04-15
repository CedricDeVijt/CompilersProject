import os

from graphviz import Digraph

import src.parser.AST as AST


class DotGenerator:
    @staticmethod
    def generateASTDot(AST_tree, output_filename, format="dot"):
        """
        Generate a dot image from the AST and save it to a file.
        """
        dot = Digraph()
        DotGenerator._generateASTDot(dot, AST_tree)

        # remove ".dot" from the output filename if it is present
        if output_filename.endswith(".dot") or output_filename.endswith(".png"):
            output_filename = output_filename[:-4]

        dot.render(output_filename, view=True, format=format)

        # remove the temporary file created by the render method

        os.remove(f"{output_filename}")

    @staticmethod
    def _generateASTDot(dot, node):
        if isinstance(node, str):
            return
        if node.children:
            dot.node(str(id(node)), str(expandExpression(node)))
            for child in node.children:
                DotGenerator._generateASTDot(dot, child)
                dot.edge(str(id(node)), str(id(child)))
        else:
            if isinstance(node, AST.IfStatementNode) or isinstance(node, AST.WhileLoopNode) or isinstance(node, AST.FunctionNode):
                dot.node(str(id(node)), str(expandExpression(node)))
                for child in node.body:
                    DotGenerator._generateASTDot(dot, child)
                    dot.edge(str(id(node)), str(id(child)))
                return
            label = f"{str(expandExpression(node))}\n"
            dot.node(str(id(node)), label, shape='box')

    @staticmethod
    def generateSymbolTableDot(symbol_table_tree, output_filename, format="dot"):
        dot = Digraph()
        DotGenerator._generateSymbolTableDot(dot, symbol_table_tree.root)
        # remove extension from the output filename if it is present
        if output_filename.endswith(".dot") or output_filename.endswith(".png"):
            output_filename = output_filename[:-4]

        dot.render(output_filename, view=True, format=format)
        # remove the temporary file created by the render method
        os.remove(f"{output_filename}")

    @staticmethod
    def _generateSymbolTableDot(dot, node):
        # Create a rectangle node for the current symbol table
        table_node_label = DotGenerator._generateSymbolTableLabel(node.table)
        dot.node(str(id(node)), table_node_label, shape='box')

        # Recursively generate DOT representation for children
        for child in node.children:
            child_node_label = DotGenerator._generateSymbolTableLabel(child.table)
            dot.node(str(id(child)), child_node_label, shape='box')
            dot.edge(str(id(node)), str(id(child)))
            DotGenerator._generateSymbolTableDot(dot, child)

    @staticmethod
    def _generateSymbolTableLabel(symbol_table):
        # Create a label for the symbol table node
        label = ""
        for symbol in symbol_table.symbols.values():
            if symbol.typeDef:
                label += f"typedef "

            if symbol.const:
                label += "const "

            if isinstance(symbol.type, AST.PointerNode):
                varType = symbol.type.type[-1].value
                pointerCount = int(symbol.type.value)
                label += f"{varType}{'*' * pointerCount} {symbol.name}\n"
            else:
                label += f"{symbol.type} {symbol.name}\n"

        return label


def expandExpression(node):
    expr = ""
    if isinstance(node, list):
        for item in node:
            expr += expandExpression(item)
        return expr
    if isinstance(node, AST.ProgramNode):
        return f"{node.value}"
    if len(node.children) == 0:
        match node:
            case AST.BreakNode():
                return "break"
            case AST.ContinueNode():
                return "continue"
            case AST.CommentNode():
                return f"{node.value}"
            case AST.CharNode():
                return f"'{chr(int(node.value))}'"
            case AST.IntNode():
                return node.value
            case AST.FloatNode():
                return node.value
            case AST.IdentifierNode():
                return node.value
            case AST.TypeNode():
                return node.value
            case AST.PointerNode():
                if isinstance(node.type, list):
                    for node_type in node.type:
                        expr += expandExpression(node_type)
                else:
                    expr += expandExpression(node.type)
                expr += "*" * int(node.value)
            case AST.DerefNode():
                if expandExpression(node.identifier).startswith('-'):
                    expr += '-' + "*" * int(node.value) + expandExpression(node.identifier).removeprefix('-')
                else:
                    expr += "*" * int(node.value)
                    expr += expandExpression(node.identifier)
            case AST.AddrNode():
                expr += f"&{expandExpression(node.value)}"
            case AST.ExplicitConversionNode():
                expr += f"({node.type}) {expandExpression(node.rval)}"
                pass
            case AST.DeclarationNode():
                expr += f"Declaration\n{expandExpression(node.type)} {expandExpression(node.lvalue)}"
            case AST.AssignmentNode():
                expr += f"Assignment\n{expandExpression(node.lvalue)} = {expandExpression(node.rvalue)}"
            case AST.DefinitionNode():
                expr += f"Definition\n{expandExpression(node.type)} {expandExpression(node.lvalue)} = {expandExpression(node.rvalue)}"
            case AST.PostFixNode():
                expr += f"({node.value}{'++' if node.op == 'inc' else '--'})"
            case AST.PreFixNode():
                expr += f"({'++' if node.op == 'inc' else '--'}{node.value})"
            case AST.PrintfNode():
                expr += f"Printf({node.specifier}, {expandExpression(node.node)})"
            case AST.IfStatementNode():
                expr += f"if({expandExpression(node.condition)})"
                if len(node.body) == 0:
                    expr += "{}"
            case AST.ElseIfStatementNode():
                expr += f"else if({expandExpression(node.condition)})"
                if len(node.body) == 0:
                    expr += "{}"
            case AST.ElseStatementNode():
                expr += f"else"
                if len(node.body) == 0:
                    expr += "{}"
            case AST.WhileLoopNode():
                expr += f"while({expandExpression(node.condition)})"
                if len(node.body) == 0:
                    expr += "{}"
            case AST.FunctionNode():
                params_str = ''
                params = node.params
                pointer = 0
                for param in params:
                    param_name = param[1]
                    param_type = param[0]
                    const = False
                    # Get param_name
                    if isinstance(param_name, AST.IdentifierNode):
                        param_name = param_name.value
                    elif isinstance(param_name, AST.AddrNode):
                        param_name = f"&{param_name.value.value}"
                    # Get param type
                    if isinstance(param_type, AST.PointerNode):
                        pointer = int(param_type.value)
                        param_type = param_type.type
                    if isinstance(param_type, list):
                        const = True
                        pointer = 0
                        param_type = param_type[len(param_type) - 1]
                    param_type = param_type.value
                    params_str = f"{'const ' if const else ''}{param_type} {'*' * pointer}{param_name}{', ' + params_str if params_str != '' else ''}"
                expr += f"{expandType(node.type)}{node.value}({params_str})"
                if len(node.body) == 0:
                    expr += "{}"
            case AST.FunctionCall():
                expr += f"{node.value}({expandArguments(node.arguments)})"
            case AST.TypedefNode():
                expr += f"Typedef {node.type} {node.identifier}"
            case _:
                expr += node.value
        return expr
    elif len(node.children) == 1:
        expr += "("
        match node:
            case AST.LogicalNotNode():
                expr += f"!{expandExpression(node.children[0])}"
            case AST.BitwiseNotNode():
                expr += f"~{expandExpression(node.children[0])}"
            case _:
                expr += node.value
        expr += ")"
    elif len(node.children) == 2:
        expr += f"({expandExpression(node.children[0])}"
        match node:
            case AST.DivNode():
                expr += "/"
            case AST.ModNode():
                expr += "%"
            case AST.MultNode():
                expr += "*"
            case AST.MinusNode():
                expr += "-"
            case AST.PlusNode():
                expr += "+"
            case AST.LTNode():
                expr += "<"
            case AST.GTNode():
                expr += ">"
            case AST.GTEQNode():
                expr += ">="
            case AST.LTEQNode():
                expr += "<="
            case AST.EQNode():
                expr += "=="
            case AST.NEQNode():
                expr += "!="
            case AST.SLNode():
                expr += "<<"
            case AST.SRNode():
                expr += ">>"
            case AST.BitwiseAndNode():
                expr += "&"
            case AST.BitwiseOrNode():
                expr += "|"
            case AST.BitwiseXorNode():
                expr += "^"
            case AST.LogicalAndNode():
                expr += "&&"
            case AST.LogicalOrNode():
                expr += "||"
            case _:
                expr += node.value
        expr += f"{expandExpression(node.children[1])})"
    return expr

def expandType(node):
    str = ""
    if isinstance(node, AST.PointerNode):
        if isinstance(node.type, list):
            for nodetype in node.type:
                str += expandType(nodetype)
        else:
            str += expandType(node.type)
        str += "*" * int(node.value)
    elif isinstance(node, list):
        for nodetype in node:
            str += expandType(nodetype)
    else:
        str += f"{node.value} "
    return str


def expandArguments(arguments):
    str = ""
    for arg in arguments:
        str += f"{expandExpression(arg)}, "
    return str[:-2]