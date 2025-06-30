"""
Abstract Syntax Tree Node Definitions
Defines AST nodes for the Sanskrit programming language
"""

from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict
from enum import Enum

class NodeType(Enum):
    PROGRAM = "PROGRAM"
    LITERAL = "LITERAL"
    IDENTIFIER = "IDENTIFIER"
    BINARY_OP = "BINARY_OP"
    UNARY_OP = "UNARY_OP"
    ASSIGNMENT = "ASSIGNMENT"
    IF_STATEMENT = "IF_STATEMENT"
    WHILE_LOOP = "WHILE_LOOP"
    FOR_LOOP = "FOR_LOOP"
    FUNCTION_DEF = "FUNCTION_DEF"
    FUNCTION_CALL = "FUNCTION_CALL"
    RETURN_STATEMENT = "RETURN_STATEMENT"
    CLASS_DEF = "CLASS_DEF"
    IMPORT_STATEMENT = "IMPORT_STATEMENT"
    BLOCK = "BLOCK"
    EXPRESSION_STATEMENT = "EXPRESSION_STATEMENT"

class ASTNode(ABC):
    """Base class for all AST nodes"""
    
    def __init__(self, node_type: NodeType, line: int = 0, column: int = 0):
        self.node_type = node_type
        self.line = line
        self.column = column
    
    @abstractmethod
    def accept(self, visitor):
        """Accept a visitor for the visitor pattern"""
        pass

class Expression(ASTNode):
    """Base class for all expressions"""
    pass

class Statement(ASTNode):
    """Base class for all statements"""
    pass

class Program(ASTNode):
    """Root node representing the entire program"""
    
    def __init__(self, statements: List[Statement]):
        super().__init__(NodeType.PROGRAM)
        self.statements = statements
    
    def accept(self, visitor):
        return visitor.visit_program(self)

class Literal(Expression):
    """Literal values (numbers, strings, booleans, null)"""
    
    def __init__(self, value: Any, line: int = 0, column: int = 0):
        super().__init__(NodeType.LITERAL, line, column)
        self.value = value
    
    def accept(self, visitor):
        return visitor.visit_literal(self)

class Identifier(Expression):
    """Variable or function names"""
    
    def __init__(self, name: str, line: int = 0, column: int = 0):
        super().__init__(NodeType.IDENTIFIER, line, column)
        self.name = name
    
    def accept(self, visitor):
        return visitor.visit_identifier(self)

class BinaryOperation(Expression):
    """Binary operations like +, -, *, /, ==, etc."""
    
    def __init__(self, left: Expression, operator: str, right: Expression, line: int = 0, column: int = 0):
        super().__init__(NodeType.BINARY_OP, line, column)
        self.left = left
        self.operator = operator
        self.right = right
    
    def accept(self, visitor):
        return visitor.visit_binary_operation(self)

class UnaryOperation(Expression):
    """Unary operations like -, not"""
    
    def __init__(self, operator: str, operand: Expression, line: int = 0, column: int = 0):
        super().__init__(NodeType.UNARY_OP, line, column)
        self.operator = operator
        self.operand = operand
    
    def accept(self, visitor):
        return visitor.visit_unary_operation(self)

class Assignment(Statement):
    """Variable assignment"""
    
    def __init__(self, target: Identifier, value: Expression, line: int = 0, column: int = 0):
        super().__init__(NodeType.ASSIGNMENT, line, column)
        self.target = target
        self.value = value
    
    def accept(self, visitor):
        return visitor.visit_assignment(self)

class IfStatement(Statement):
    """If-else conditional statement"""
    
    def __init__(self, condition: Expression, then_branch: Statement, 
                 else_branch: Optional[Statement] = None, line: int = 0, column: int = 0):
        super().__init__(NodeType.IF_STATEMENT, line, column)
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch
    
    def accept(self, visitor):
        return visitor.visit_if_statement(self)

class WhileLoop(Statement):
    """While loop statement"""
    
    def __init__(self, condition: Expression, body: Statement, line: int = 0, column: int = 0):
        super().__init__(NodeType.WHILE_LOOP, line, column)
        self.condition = condition
        self.body = body
    
    def accept(self, visitor):
        return visitor.visit_while_loop(self)

class ForLoop(Statement):
    """For loop statement"""
    
    def __init__(self, variable: Identifier, iterable: Expression, body: Statement, 
                 line: int = 0, column: int = 0):
        super().__init__(NodeType.FOR_LOOP, line, column)
        self.variable = variable
        self.iterable = iterable
        self.body = body
    
    def accept(self, visitor):
        return visitor.visit_for_loop(self)

class FunctionDef(Statement):
    """Function definition"""
    
    def __init__(self, name: Identifier, parameters: List[Identifier], body: Statement,
                 return_type: Optional[str] = None, line: int = 0, column: int = 0):
        super().__init__(NodeType.FUNCTION_DEF, line, column)
        self.name = name
        self.parameters = parameters
        self.body = body
        self.return_type = return_type
    
    def accept(self, visitor):
        return visitor.visit_function_def(self)

class FunctionCall(Expression):
    """Function call expression"""
    
    def __init__(self, function: Expression, arguments: List[Expression], 
                 line: int = 0, column: int = 0):
        super().__init__(NodeType.FUNCTION_CALL, line, column)
        self.function = function
        self.arguments = arguments
    
    def accept(self, visitor):
        return visitor.visit_function_call(self)

class ReturnStatement(Statement):
    """Return statement"""
    
    def __init__(self, value: Optional[Expression] = None, line: int = 0, column: int = 0):
        super().__init__(NodeType.RETURN_STATEMENT, line, column)
        self.value = value
    
    def accept(self, visitor):
        return visitor.visit_return_statement(self)

class ClassDef(Statement):
    """Class definition"""
    
    def __init__(self, name: Identifier, superclass: Optional[Identifier], 
                 methods: List[FunctionDef], line: int = 0, column: int = 0):
        super().__init__(NodeType.CLASS_DEF, line, column)
        self.name = name
        self.superclass = superclass
        self.methods = methods
    
    def accept(self, visitor):
        return visitor.visit_class_def(self)

class ImportStatement(Statement):
    """Import statement"""
    
    def __init__(self, module: str, alias: Optional[str] = None, 
                 from_list: Optional[List[str]] = None, line: int = 0, column: int = 0):
        super().__init__(NodeType.IMPORT_STATEMENT, line, column)
        self.module = module
        self.alias = alias
        self.from_list = from_list
    
    def accept(self, visitor):
        return visitor.visit_import_statement(self)

class Block(Statement):
    """Block of statements"""
    
    def __init__(self, statements: List[Statement], line: int = 0, column: int = 0):
        super().__init__(NodeType.BLOCK, line, column)
        self.statements = statements
    
    def accept(self, visitor):
        return visitor.visit_block(self)

class ExpressionStatement(Statement):
    """Statement that wraps an expression"""
    
    def __init__(self, expression: Expression, line: int = 0, column: int = 0):
        super().__init__(NodeType.EXPRESSION_STATEMENT, line, column)
        self.expression = expression
    
    def accept(self, visitor):
        return visitor.visit_expression_statement(self)
