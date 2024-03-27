from graphviz import Digraph

from src.parser.AST import IdentifierNode, TypeNode, IntNode, FloatNode, PointerNode, DeclarationNode, AssignmentNode, DefinitionNode


class DotGenerator:
    @staticmethod
    def generateDotImage(AST_tree, output_filename):
        """
        Generate a dot image from the AST and save it to a file.
        """
        dot = Digraph()
        DotGenerator._generateDotImage(dot, AST_tree)
        dot.render(output_filename, view=True, format='png')

    @staticmethod
    def _generateDotImage(dot, node):
        if node.children:
            dot.node(str(id(node)), node.value)
            for child in node.children:
                DotGenerator._generateDotImage(dot, child)
                dot.edge(str(id(node)), str(id(child)))
        else:
            label = f"{node.value}\n"
            if isinstance(node, IdentifierNode):
                label += f"Identifier: {node.value}"
            elif isinstance(node, TypeNode):
                label += f"Type: {node.value}"
            elif isinstance(node, IntNode):
                label = f"Literal\n"
                label += f"Value: {node.value}\nType: int"
            elif isinstance(node, FloatNode):
                label = f"Literal\n"
                label += f"Value: {node.value}\nType: float"
            elif isinstance(node, DeclarationNode):
                for child in node.type:
                    if isinstance(child, PointerNode):
                        for child1 in child.type:
                            label += f" {child1.value}"
                        label += f"*" * int(child.value)
                    else:
                        label += f" {child.value}"
                label += f" {node.lvalue.value}"
            elif isinstance(node, AssignmentNode):
                label += f" {node.lvalue.value} = {node.rvalue.value}"
            elif isinstance(node, DefinitionNode):
                for child in node.type:
                    if isinstance(child, PointerNode):
                        for child1 in child.type:
                            label += f" {child1.value}"
                        label += f"*" * int(child.value)
                    else:
                        label += f" {child.value}"
                label += f" {node.lvalue.value} = {node.rvalue.value}"
            dot.node(str(id(node)), label, shape='box')
