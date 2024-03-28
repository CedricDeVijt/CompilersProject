from graphviz import Digraph

import src.parser.AST as AST


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
            if isinstance(node, AST.IdentifierNode):
                label += f"Identifier: {node.value}"
            elif isinstance(node, AST.TypeNode):
                label += f"Type: {node.value}"
            elif isinstance(node, AST.IntNode):
                label = f"Literal\nValue: {node.value}\nType: int"
            elif isinstance(node, AST.FloatNode):
                label = f"Literal\n"
                label += f"Value: {node.value}\nType: float"
            elif isinstance(node, AST.CommentNode):
                label = f"Comment\n{node.value}"
            elif isinstance(node, AST.PostFixNode):
                label = f"PostFix"
                if node.op == 'inc':
                    label += f"Increment\n{node.value}++"
                else:
                    label += f"Increment\n{node.value}--"
            elif isinstance(node, AST.PreFixNode):
                label = f"PreFix"
                if node.op == 'inc':
                    label += f"Increment\n++{node.value}"
                else:
                    label += f"Increment\n--{node.value}"
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
                label += f" {node.lvalue.value} = "
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
