# Generated from grammars/Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#program.
    def enterProgram(self, ctx:GrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by GrammarParser#program.
    def exitProgram(self, ctx:GrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by GrammarParser#declaration.
    def enterDeclaration(self, ctx:GrammarParser.DeclarationContext):
        pass

    # Exit a parse tree produced by GrammarParser#declaration.
    def exitDeclaration(self, ctx:GrammarParser.DeclarationContext):
        pass


    # Enter a parse tree produced by GrammarParser#scope.
    def enterScope(self, ctx:GrammarParser.ScopeContext):
        pass

    # Exit a parse tree produced by GrammarParser#scope.
    def exitScope(self, ctx:GrammarParser.ScopeContext):
        pass


    # Enter a parse tree produced by GrammarParser#statement.
    def enterStatement(self, ctx:GrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#statement.
    def exitStatement(self, ctx:GrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#function.
    def enterFunction(self, ctx:GrammarParser.FunctionContext):
        pass

    # Exit a parse tree produced by GrammarParser#function.
    def exitFunction(self, ctx:GrammarParser.FunctionContext):
        pass


    # Enter a parse tree produced by GrammarParser#structDefinition.
    def enterStructDefinition(self, ctx:GrammarParser.StructDefinitionContext):
        pass

    # Exit a parse tree produced by GrammarParser#structDefinition.
    def exitStructDefinition(self, ctx:GrammarParser.StructDefinitionContext):
        pass


    # Enter a parse tree produced by GrammarParser#structStatement.
    def enterStructStatement(self, ctx:GrammarParser.StructStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#structStatement.
    def exitStructStatement(self, ctx:GrammarParser.StructStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#structVariable.
    def enterStructVariable(self, ctx:GrammarParser.StructVariableContext):
        pass

    # Exit a parse tree produced by GrammarParser#structVariable.
    def exitStructVariable(self, ctx:GrammarParser.StructVariableContext):
        pass


    # Enter a parse tree produced by GrammarParser#structVariableDefinition.
    def enterStructVariableDefinition(self, ctx:GrammarParser.StructVariableDefinitionContext):
        pass

    # Exit a parse tree produced by GrammarParser#structVariableDefinition.
    def exitStructVariableDefinition(self, ctx:GrammarParser.StructVariableDefinitionContext):
        pass


    # Enter a parse tree produced by GrammarParser#structMember.
    def enterStructMember(self, ctx:GrammarParser.StructMemberContext):
        pass

    # Exit a parse tree produced by GrammarParser#structMember.
    def exitStructMember(self, ctx:GrammarParser.StructMemberContext):
        pass


    # Enter a parse tree produced by GrammarParser#structAssignment.
    def enterStructAssignment(self, ctx:GrammarParser.StructAssignmentContext):
        pass

    # Exit a parse tree produced by GrammarParser#structAssignment.
    def exitStructAssignment(self, ctx:GrammarParser.StructAssignmentContext):
        pass


    # Enter a parse tree produced by GrammarParser#structPostFixIncrement.
    def enterStructPostFixIncrement(self, ctx:GrammarParser.StructPostFixIncrementContext):
        pass

    # Exit a parse tree produced by GrammarParser#structPostFixIncrement.
    def exitStructPostFixIncrement(self, ctx:GrammarParser.StructPostFixIncrementContext):
        pass


    # Enter a parse tree produced by GrammarParser#structPostFixDecrement.
    def enterStructPostFixDecrement(self, ctx:GrammarParser.StructPostFixDecrementContext):
        pass

    # Exit a parse tree produced by GrammarParser#structPostFixDecrement.
    def exitStructPostFixDecrement(self, ctx:GrammarParser.StructPostFixDecrementContext):
        pass


    # Enter a parse tree produced by GrammarParser#structPreFixIncrement.
    def enterStructPreFixIncrement(self, ctx:GrammarParser.StructPreFixIncrementContext):
        pass

    # Exit a parse tree produced by GrammarParser#structPreFixIncrement.
    def exitStructPreFixIncrement(self, ctx:GrammarParser.StructPreFixIncrementContext):
        pass


    # Enter a parse tree produced by GrammarParser#structPreFixDecrement.
    def enterStructPreFixDecrement(self, ctx:GrammarParser.StructPreFixDecrementContext):
        pass

    # Exit a parse tree produced by GrammarParser#structPreFixDecrement.
    def exitStructPreFixDecrement(self, ctx:GrammarParser.StructPreFixDecrementContext):
        pass


    # Enter a parse tree produced by GrammarParser#functionParams.
    def enterFunctionParams(self, ctx:GrammarParser.FunctionParamsContext):
        pass

    # Exit a parse tree produced by GrammarParser#functionParams.
    def exitFunctionParams(self, ctx:GrammarParser.FunctionParamsContext):
        pass


    # Enter a parse tree produced by GrammarParser#functionCall.
    def enterFunctionCall(self, ctx:GrammarParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by GrammarParser#functionCall.
    def exitFunctionCall(self, ctx:GrammarParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by GrammarParser#callParams.
    def enterCallParams(self, ctx:GrammarParser.CallParamsContext):
        pass

    # Exit a parse tree produced by GrammarParser#callParams.
    def exitCallParams(self, ctx:GrammarParser.CallParamsContext):
        pass


    # Enter a parse tree produced by GrammarParser#switchStatement.
    def enterSwitchStatement(self, ctx:GrammarParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#switchStatement.
    def exitSwitchStatement(self, ctx:GrammarParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#switchCase.
    def enterSwitchCase(self, ctx:GrammarParser.SwitchCaseContext):
        pass

    # Exit a parse tree produced by GrammarParser#switchCase.
    def exitSwitchCase(self, ctx:GrammarParser.SwitchCaseContext):
        pass


    # Enter a parse tree produced by GrammarParser#conditional.
    def enterConditional(self, ctx:GrammarParser.ConditionalContext):
        pass

    # Exit a parse tree produced by GrammarParser#conditional.
    def exitConditional(self, ctx:GrammarParser.ConditionalContext):
        pass


    # Enter a parse tree produced by GrammarParser#ifStatement.
    def enterIfStatement(self, ctx:GrammarParser.IfStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#ifStatement.
    def exitIfStatement(self, ctx:GrammarParser.IfStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#elseIfStatement.
    def enterElseIfStatement(self, ctx:GrammarParser.ElseIfStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#elseIfStatement.
    def exitElseIfStatement(self, ctx:GrammarParser.ElseIfStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#elseStatement.
    def enterElseStatement(self, ctx:GrammarParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#elseStatement.
    def exitElseStatement(self, ctx:GrammarParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#whileLoop.
    def enterWhileLoop(self, ctx:GrammarParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by GrammarParser#whileLoop.
    def exitWhileLoop(self, ctx:GrammarParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by GrammarParser#forLoop.
    def enterForLoop(self, ctx:GrammarParser.ForLoopContext):
        pass

    # Exit a parse tree produced by GrammarParser#forLoop.
    def exitForLoop(self, ctx:GrammarParser.ForLoopContext):
        pass


    # Enter a parse tree produced by GrammarParser#forCondition.
    def enterForCondition(self, ctx:GrammarParser.ForConditionContext):
        pass

    # Exit a parse tree produced by GrammarParser#forCondition.
    def exitForCondition(self, ctx:GrammarParser.ForConditionContext):
        pass


    # Enter a parse tree produced by GrammarParser#printfStatement.
    def enterPrintfStatement(self, ctx:GrammarParser.PrintfStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#printfStatement.
    def exitPrintfStatement(self, ctx:GrammarParser.PrintfStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#scanfStatement.
    def enterScanfStatement(self, ctx:GrammarParser.ScanfStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#scanfStatement.
    def exitScanfStatement(self, ctx:GrammarParser.ScanfStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#formatSpecifier.
    def enterFormatSpecifier(self, ctx:GrammarParser.FormatSpecifierContext):
        pass

    # Exit a parse tree produced by GrammarParser#formatSpecifier.
    def exitFormatSpecifier(self, ctx:GrammarParser.FormatSpecifierContext):
        pass


    # Enter a parse tree produced by GrammarParser#char.
    def enterChar(self, ctx:GrammarParser.CharContext):
        pass

    # Exit a parse tree produced by GrammarParser#char.
    def exitChar(self, ctx:GrammarParser.CharContext):
        pass


    # Enter a parse tree produced by GrammarParser#string.
    def enterString(self, ctx:GrammarParser.StringContext):
        pass

    # Exit a parse tree produced by GrammarParser#string.
    def exitString(self, ctx:GrammarParser.StringContext):
        pass


    # Enter a parse tree produced by GrammarParser#variable.
    def enterVariable(self, ctx:GrammarParser.VariableContext):
        pass

    # Exit a parse tree produced by GrammarParser#variable.
    def exitVariable(self, ctx:GrammarParser.VariableContext):
        pass


    # Enter a parse tree produced by GrammarParser#lvalue.
    def enterLvalue(self, ctx:GrammarParser.LvalueContext):
        pass

    # Exit a parse tree produced by GrammarParser#lvalue.
    def exitLvalue(self, ctx:GrammarParser.LvalueContext):
        pass


    # Enter a parse tree produced by GrammarParser#rvalue.
    def enterRvalue(self, ctx:GrammarParser.RvalueContext):
        pass

    # Exit a parse tree produced by GrammarParser#rvalue.
    def exitRvalue(self, ctx:GrammarParser.RvalueContext):
        pass


    # Enter a parse tree produced by GrammarParser#jumpStatement.
    def enterJumpStatement(self, ctx:GrammarParser.JumpStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#jumpStatement.
    def exitJumpStatement(self, ctx:GrammarParser.JumpStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#unaryExpression.
    def enterUnaryExpression(self, ctx:GrammarParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#unaryExpression.
    def exitUnaryExpression(self, ctx:GrammarParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#literal.
    def enterLiteral(self, ctx:GrammarParser.LiteralContext):
        pass

    # Exit a parse tree produced by GrammarParser#literal.
    def exitLiteral(self, ctx:GrammarParser.LiteralContext):
        pass


    # Enter a parse tree produced by GrammarParser#explicitConversion.
    def enterExplicitConversion(self, ctx:GrammarParser.ExplicitConversionContext):
        pass

    # Exit a parse tree produced by GrammarParser#explicitConversion.
    def exitExplicitConversion(self, ctx:GrammarParser.ExplicitConversionContext):
        pass


    # Enter a parse tree produced by GrammarParser#pointer.
    def enterPointer(self, ctx:GrammarParser.PointerContext):
        pass

    # Exit a parse tree produced by GrammarParser#pointer.
    def exitPointer(self, ctx:GrammarParser.PointerContext):
        pass


    # Enter a parse tree produced by GrammarParser#deref.
    def enterDeref(self, ctx:GrammarParser.DerefContext):
        pass

    # Exit a parse tree produced by GrammarParser#deref.
    def exitDeref(self, ctx:GrammarParser.DerefContext):
        pass


    # Enter a parse tree produced by GrammarParser#addr.
    def enterAddr(self, ctx:GrammarParser.AddrContext):
        pass

    # Exit a parse tree produced by GrammarParser#addr.
    def exitAddr(self, ctx:GrammarParser.AddrContext):
        pass


    # Enter a parse tree produced by GrammarParser#enumDeclaration.
    def enterEnumDeclaration(self, ctx:GrammarParser.EnumDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarParser#enumDeclaration.
    def exitEnumDeclaration(self, ctx:GrammarParser.EnumDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarParser#enumStatement.
    def enterEnumStatement(self, ctx:GrammarParser.EnumStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#enumStatement.
    def exitEnumStatement(self, ctx:GrammarParser.EnumStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#enumVariableDefinition.
    def enterEnumVariableDefinition(self, ctx:GrammarParser.EnumVariableDefinitionContext):
        pass

    # Exit a parse tree produced by GrammarParser#enumVariableDefinition.
    def exitEnumVariableDefinition(self, ctx:GrammarParser.EnumVariableDefinitionContext):
        pass


    # Enter a parse tree produced by GrammarParser#enumVariableDeclaration.
    def enterEnumVariableDeclaration(self, ctx:GrammarParser.EnumVariableDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarParser#enumVariableDeclaration.
    def exitEnumVariableDeclaration(self, ctx:GrammarParser.EnumVariableDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarParser#postFixIncrement.
    def enterPostFixIncrement(self, ctx:GrammarParser.PostFixIncrementContext):
        pass

    # Exit a parse tree produced by GrammarParser#postFixIncrement.
    def exitPostFixIncrement(self, ctx:GrammarParser.PostFixIncrementContext):
        pass


    # Enter a parse tree produced by GrammarParser#postFixDecrement.
    def enterPostFixDecrement(self, ctx:GrammarParser.PostFixDecrementContext):
        pass

    # Exit a parse tree produced by GrammarParser#postFixDecrement.
    def exitPostFixDecrement(self, ctx:GrammarParser.PostFixDecrementContext):
        pass


    # Enter a parse tree produced by GrammarParser#preFixIncrement.
    def enterPreFixIncrement(self, ctx:GrammarParser.PreFixIncrementContext):
        pass

    # Exit a parse tree produced by GrammarParser#preFixIncrement.
    def exitPreFixIncrement(self, ctx:GrammarParser.PreFixIncrementContext):
        pass


    # Enter a parse tree produced by GrammarParser#preFixDecrement.
    def enterPreFixDecrement(self, ctx:GrammarParser.PreFixDecrementContext):
        pass

    # Exit a parse tree produced by GrammarParser#preFixDecrement.
    def exitPreFixDecrement(self, ctx:GrammarParser.PreFixDecrementContext):
        pass


    # Enter a parse tree produced by GrammarParser#arrayStatement.
    def enterArrayStatement(self, ctx:GrammarParser.ArrayStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#arrayStatement.
    def exitArrayStatement(self, ctx:GrammarParser.ArrayStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#arrayDeclaration.
    def enterArrayDeclaration(self, ctx:GrammarParser.ArrayDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarParser#arrayDeclaration.
    def exitArrayDeclaration(self, ctx:GrammarParser.ArrayDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarParser#arrayAssignment.
    def enterArrayAssignment(self, ctx:GrammarParser.ArrayAssignmentContext):
        pass

    # Exit a parse tree produced by GrammarParser#arrayAssignment.
    def exitArrayAssignment(self, ctx:GrammarParser.ArrayAssignmentContext):
        pass


    # Enter a parse tree produced by GrammarParser#arrayDefinition.
    def enterArrayDefinition(self, ctx:GrammarParser.ArrayDefinitionContext):
        pass

    # Exit a parse tree produced by GrammarParser#arrayDefinition.
    def exitArrayDefinition(self, ctx:GrammarParser.ArrayDefinitionContext):
        pass


    # Enter a parse tree produced by GrammarParser#array.
    def enterArray(self, ctx:GrammarParser.ArrayContext):
        pass

    # Exit a parse tree produced by GrammarParser#array.
    def exitArray(self, ctx:GrammarParser.ArrayContext):
        pass


    # Enter a parse tree produced by GrammarParser#arrayElement.
    def enterArrayElement(self, ctx:GrammarParser.ArrayElementContext):
        pass

    # Exit a parse tree produced by GrammarParser#arrayElement.
    def exitArrayElement(self, ctx:GrammarParser.ArrayElementContext):
        pass


    # Enter a parse tree produced by GrammarParser#typedef.
    def enterTypedef(self, ctx:GrammarParser.TypedefContext):
        pass

    # Exit a parse tree produced by GrammarParser#typedef.
    def exitTypedef(self, ctx:GrammarParser.TypedefContext):
        pass


    # Enter a parse tree produced by GrammarParser#type.
    def enterType(self, ctx:GrammarParser.TypeContext):
        pass

    # Exit a parse tree produced by GrammarParser#type.
    def exitType(self, ctx:GrammarParser.TypeContext):
        pass


    # Enter a parse tree produced by GrammarParser#identifier.
    def enterIdentifier(self, ctx:GrammarParser.IdentifierContext):
        pass

    # Exit a parse tree produced by GrammarParser#identifier.
    def exitIdentifier(self, ctx:GrammarParser.IdentifierContext):
        pass


    # Enter a parse tree produced by GrammarParser#comment.
    def enterComment(self, ctx:GrammarParser.CommentContext):
        pass

    # Exit a parse tree produced by GrammarParser#comment.
    def exitComment(self, ctx:GrammarParser.CommentContext):
        pass



del GrammarParser