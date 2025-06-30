"""
Sanskrit Language Interpreter
Tree-walking interpreter for Sanskrit programming language
"""

from typing import Any, Dict, List, Optional, Callable
from .ast_nodes import *
from .types import SanskritType, SanskritValue
from .errors import SanskritRuntimeError, SanskritReturnException
from .stdlib import get_builtin_functions

class Environment:
    """Environment for variable scoping"""
    
    def __init__(self, enclosing: Optional['Environment'] = None):
        self.enclosing = enclosing
        self.values: Dict[str, Any] = {}
    
    def define(self, name: str, value: Any) -> None:
        """Define a variable"""
        self.values[name] = value
    
    def get(self, name: str) -> Any:
        """Get a variable value"""
        if name in self.values:
            return self.values[name]
        
        if self.enclosing:
            return self.enclosing.get(name)
        
        raise SanskritRuntimeError(f"अपरिभाषित चर '{name}'")
    
    def assign(self, name: str, value: Any) -> None:
        """Assign to a variable"""
        if name in self.values:
            self.values[name] = value
            return
        
        if self.enclosing:
            self.enclosing.assign(name, value)
            return
        
        # If variable doesn't exist anywhere, create it in current scope
        self.values[name] = value

class SanskritFunction:
    """Callable function object"""
    
    def __init__(self, declaration: FunctionDef, closure: Environment):
        self.declaration = declaration
        self.closure = closure
    
    def call(self, interpreter: 'SanskritInterpreter', arguments: List[Any]) -> Any:
        """Call the function"""
        environment = Environment(self.closure)
        
        # Bind parameters
        for i, param in enumerate(self.declaration.parameters):
            if i < len(arguments):
                environment.define(param.name, arguments[i])
            else:
                environment.define(param.name, None)
        
        try:
            interpreter.execute_block(self.declaration.body.statements, environment)
        except SanskritReturnException as ret:
            return ret.value
        
        return None
    
    def arity(self) -> int:
        """Return number of parameters"""
        return len(self.declaration.parameters)

class SanskritClass:
    """Class object"""
    
    def __init__(self, name: str, methods: Dict[str, SanskritFunction]):
        self.name = name
        self.methods = methods
    
    def call(self, interpreter: 'SanskritInterpreter', arguments: List[Any]) -> Any:
        """Create instance of class"""
        instance = SanskritInstance(self)
        return instance

class SanskritInstance:
    """Instance of a class"""
    
    def __init__(self, klass: SanskritClass):
        self.klass = klass
        self.fields: Dict[str, Any] = {}
    
    def get(self, name: str) -> Any:
        """Get field or method"""
        if name in self.fields:
            return self.fields[name]
        
        if name in self.klass.methods:
            return self.klass.methods[name]
        
        raise SanskritRuntimeError(f"अपरिभाषित गुण '{name}'")
    
    def set(self, name: str, value: Any) -> None:
        """Set field"""
        self.fields[name] = value

class SanskritInterpreter:
    """Tree-walking interpreter"""
    
    def __init__(self):
        self.globals = Environment()
        self.environment = self.globals
        
        # Add built-in functions
        for name, func in get_builtin_functions().items():
            self.globals.define(name, func)
    
    def execute(self, source: str) -> None:
        """Execute source code"""
        from .lexer import SanskritLexer
        from .parser import SanskritParser
        
        lexer = SanskritLexer(source)
        tokens = lexer.tokenize()
        
        parser = SanskritParser(tokens)
        ast = parser.parse()
        
        self.interpret(ast)
    
    def interpret(self, program: Program) -> None:
        """Interpret AST"""
        try:
            for statement in program.statements:
                self.execute_statement(statement)
        except SanskritRuntimeError as error:
            print(f"रनटाइम त्रुटि: {error}")
    
    def execute_statement(self, stmt: Statement) -> None:
        """Execute a statement"""
        stmt.accept(self)
    
    def evaluate(self, expr: Expression) -> Any:
        """Evaluate an expression"""
        return expr.accept(self)
    
    def execute_block(self, statements: List[Statement], environment: Environment) -> None:
        """Execute a block of statements"""
        previous = self.environment
        try:
            self.environment = environment
            for statement in statements:
                self.execute_statement(statement)
        finally:
            self.environment = previous
    
    def visit_program(self, node: Program) -> None:
        """Visit program node"""
        for statement in node.statements:
            self.execute_statement(statement)
    
    def visit_literal(self, node: Literal) -> Any:
        """Visit literal node"""
        return node.value
    
    def visit_identifier(self, node: Identifier) -> Any:
        """Visit identifier node"""
        return self.environment.get(node.name)
    
    def visit_binary_operation(self, node: BinaryOperation) -> Any:
        """Visit binary operation node"""
        left = self.evaluate(node.left)
        right = self.evaluate(node.right)
        
        # Arithmetic operators
        if node.operator == '+':
            if isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
            return left + right
        elif node.operator == '-':
            return left - right
        elif node.operator == '*':
            return left * right
        elif node.operator == '/':
            if right == 0:
                raise SanskritRuntimeError("शून्य से भाग")
            return left / right
        elif node.operator == '%':
            return left % right
        
        # Comparison operators
        elif node.operator == '==':
            return left == right
        elif node.operator == '!=':
            return left != right
        elif node.operator == '<':
            return left < right
        elif node.operator == '>':
            return left > right
        elif node.operator == '<=':
            return left <= right
        elif node.operator == '>=':
            return left >= right
        
        # Logical operators
        elif node.operator == 'च':  # and
            return self.is_truthy(left) and self.is_truthy(right)
        elif node.operator == 'वा':  # or
            return self.is_truthy(left) or self.is_truthy(right)
        
        raise SanskritRuntimeError(f"अज्ञात ऑपरेटर '{node.operator}'")
    
    def visit_unary_operation(self, node: UnaryOperation) -> Any:
        """Visit unary operation node"""
        operand = self.evaluate(node.operand)
        
        if node.operator == '-':
            return -operand
        elif node.operator == 'न':  # not
            return not self.is_truthy(operand)
        
        raise SanskritRuntimeError(f"अज्ञात यूनरी ऑपरेटर '{node.operator}'")
    
    def visit_assignment(self, node: Assignment) -> None:
        """Visit assignment node"""
        value = self.evaluate(node.value)
        self.environment.assign(node.target.name, value)
    
    def visit_if_statement(self, node: IfStatement) -> None:
        """Visit if statement node"""
        condition = self.evaluate(node.condition)
        
        if self.is_truthy(condition):
            self.execute_statement(node.then_branch)
        elif node.else_branch:
            self.execute_statement(node.else_branch)
    
    def visit_while_loop(self, node: WhileLoop) -> None:
        """Visit while loop node"""
        while self.is_truthy(self.evaluate(node.condition)):
            self.execute_statement(node.body)
    
    def visit_for_loop(self, node: ForLoop) -> None:
        """Visit for loop node"""
        iterable = self.evaluate(node.iterable)
        
        if not hasattr(iterable, '__iter__'):
            raise SanskritRuntimeError("ऑब्जेक्ट iterable नहीं है")
        
        for item in iterable:
            self.environment.define(node.variable.name, item)
            self.execute_statement(node.body)
    
    def visit_function_def(self, node: FunctionDef) -> None:
        """Visit function definition node"""
        function = SanskritFunction(node, self.environment)
        self.environment.define(node.name.name, function)
    
    def visit_function_call(self, node: FunctionCall) -> Any:
        """Visit function call node"""
        callee = self.evaluate(node.function)
        
        arguments = []
        for arg in node.arguments:
            arguments.append(self.evaluate(arg))
        
        if isinstance(callee, SanskritFunction):
            if len(arguments) != callee.arity():
                raise SanskritRuntimeError(
                    f"अपेक्षित {callee.arity()} तर्क, प्राप्त {len(arguments)}")
            return callee.call(self, arguments)
        elif callable(callee):
            # Built-in function
            return callee(*arguments)
        else:
            raise SanskritRuntimeError("केवल फ़ंक्शन को कॉल किया जा सकता है")
    
    def visit_return_statement(self, node: ReturnStatement) -> None:
        """Visit return statement node"""
        value = None
        if node.value:
            value = self.evaluate(node.value)
        
        raise SanskritReturnException(value)
    
    def visit_class_def(self, node: ClassDef) -> None:
        """Visit class definition node"""
        methods = {}
        for method in node.methods:
            function = SanskritFunction(method, self.environment)
            methods[method.name.name] = function
        
        klass = SanskritClass(node.name.name, methods)
        self.environment.define(node.name.name, klass)
    
    def visit_import_statement(self, node: ImportStatement) -> None:
        """Visit import statement node"""
        # Simple import implementation
        from .stdlib import load_module
        module = load_module(node.module)
        self.environment.define(node.module, module)
    
    def visit_block(self, node: Block) -> None:
        """Visit block node"""
        self.execute_block(node.statements, Environment(self.environment))
    
    def visit_expression_statement(self, node: ExpressionStatement) -> None:
        """Visit expression statement node"""
        # Handle assignment expressions specially
        if isinstance(node.expression, Assignment):
            self.visit_assignment(node.expression)
        else:
            self.evaluate(node.expression)
    
    def is_truthy(self, value: Any) -> bool:
        """Determine truthiness of a value"""
        if value is None:
            return False
        if isinstance(value, bool):
            return value
        return True
