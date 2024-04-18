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
        for symbol in symbol_table.symbols:
            if symbol.symbol_type == 'typedef':
                label += f"typedef "
            if symbol.const:
                label += "const "

            if isinstance(symbol.type, AST.PointerNode):
                varType = symbol.type.type[-1].value
                pointerCount = int(symbol.type.value)
                label += f"{varType}{'*' * pointerCount} {symbol.name}\n"
            elif isinstance(symbol.type, list):
                varType = symbol.type[-1].value
                label += f"{varType} {symbol.name}\n"
            else:
                label += f"{symbol.type} {symbol.name}\n"

        return label


def expandExpression(node):
    expr = ""
    if node is None:
        return expr
    if isinstance(node, list):
        for item in node:
            expr += f"{expandExpression(item)} "
    elif isinstance(node, AST.ProgramNode):
        expr += "Program"
    elif isinstance(node, AST.Node):
        expr += f"{node.original}"
    return expr
