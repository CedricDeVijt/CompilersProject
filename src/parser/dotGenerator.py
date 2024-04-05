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
            dot.node(str(id(node)), str(node.value))
            for child in node.children:
                DotGenerator._generateASTDot(dot, child)
                dot.edge(str(id(node)), str(id(child)))
        else:
            label = f"{str(node.value)}\n"
            if isinstance(node, AST.IdentifierNode):
                label += f"Identifier: {str(node.value)}"
            elif isinstance(node, AST.TypeNode):
                label += f"Type: {str(node.value)}"
            elif isinstance(node, AST.CharNode):
                label = f"Literal\nValue: \'{chr(str(node.value))}\'\nType: char"
            elif isinstance(node, AST.IntNode):
                label = f"Literal\nValue: {str(node.value)}\nType: int"
            elif isinstance(node, AST.FloatNode):
                label = f"Literal\n"
                label += f"Value: {str(node.value)}\nType: float"
            elif isinstance(node, AST.PrintfNode):
                label = f"Printf({node.specifier}, {str(node.value)})"
                pass
            elif isinstance(node, AST.CommentNode):
                label = f"Comment\n" + str(node.value).replace('\n', '\\\\n')
            elif isinstance(node, AST.PostFixNode):
                label = f"PostFix"
                if node.op == 'inc':
                    label += f"Increment\n{str(node.value)}++"
                else:
                    label += f"Increment\n{str(node.value)}--"
            elif isinstance(node, AST.TypedefNode):
                label = f"{str(node.value)} {node.type} {node.identifier}"
            elif isinstance(node, AST.PreFixNode):
                label = f"PreFix"
                if node.op == 'inc':
                    label += f"Increment\n++{str(node.value)}"
                else:
                    label += f"Increment\n--{str(node.value)}"
            elif isinstance(node, AST.DeclarationNode):
                for child in node.type:
                    if isinstance(child, AST.PointerNode):
                        for child1 in child.type:
                            label += f" {child1.value}"
                        label += f"*" * int(child.value)
                    else:
                        label += f" {child.value}"
                label += f" {node.lvalue.value}"
            elif isinstance(node, AST.AssignmentNode):
                label = f"Assignment\n"
                if isinstance(node.lvalue, AST.DerefNode):
                    label += f"*" * int(node.lvalue.value)
                    label += f"{node.lvalue.identifier.value}"
                    label += " = "
                else:
                    label += f"{node.lvalue.value} = "
                if isinstance(node.rvalue, AST.DerefNode):
                    label += f"*" * int(node.rvalue.value)
                    label += f"{node.rvalue.identifier.value}"
                else:
                    label += f"{node.rvalue.value}"
            elif isinstance(node, AST.DefinitionNode):
                for child in node.type:
                    if isinstance(child, AST.PointerNode):
                        for child1 in child.type:
                            label += f" {child1.value}"
                        label += f"*" * int(child.value)
                    else:
                        label += f" {child.value}"
                label += f" {node.lvalue.value} = "
                if isinstance(node.rvalue, AST.DerefNode):
                    label += f"*" * int(node.rvalue.value)
                    label += f"{node.rvalue.identifier.value}"
                else:
                    label += f"{node.rvalue.value}"
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

