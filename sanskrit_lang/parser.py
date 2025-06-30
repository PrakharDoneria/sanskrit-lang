"""
Sanskrit Language Parser
Recursive descent parser for Sanskrit programming language
"""

from typing import List, Optional, Union
from .lexer import Token, TokenType, SanskritLexer
from .ast_nodes import *
from .errors import SanskritSyntaxError

class SanskritParser:
    """Recursive descent parser for Sanskrit language"""
    
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0
    
    def parse(self) -> Program:
        """Parse tokens into an AST"""
        statements = []
        
        while not self.is_at_end():
            # Skip newlines at top level
            if self.check(TokenType.NAVAPANKTI):
                self.advance()
                continue
            
            stmt = self.statement()
            if stmt:
                statements.append(stmt)
        
        return Program(statements)
    
    def statement(self) -> Optional[Statement]:
        """Parse a statement"""
        try:
            if self.match(TokenType.YADI):
                return self.if_statement()
            
            if self.match(TokenType.YAVAT):
                return self.while_statement()
            
            if self.match(TokenType.PRATHI):
                return self.for_statement()
            
            if self.match(TokenType.KAARYA):
                return self.function_statement()
            
            if self.match(TokenType.VARGA):
                return self.class_statement()
            
            if self.match(TokenType.VRATYAA):
                return self.return_statement()
            
            if self.match(TokenType.AAYAT):
                return self.import_statement()
            
            if self.check(TokenType.DHARANA) or self.check(TokenType.STHIRA):
                return self.variable_declaration()
            
            if self.match(TokenType.VAAM_KURLY):
                return self.block_statement()
            
            return self.expression_statement()
            
        except SanskritSyntaxError:
            self.synchronize()
            return None
    
    def if_statement(self) -> IfStatement:
        """Parse if statement: यदि condition { statements } अथवा { statements }"""
        line, col = self.previous().line, self.previous().column
        
        condition = self.expression()
        self.consume(TokenType.VAAM_KURLY, "'{' की अपेक्षा 'यदि' के बाद")
        
        then_branch = self.block_statement()
        else_branch = None
        
        if self.match(TokenType.ATHAVA):
            self.consume(TokenType.VAAM_KURLY, "'{' की अपेक्षा 'अथवा' के बाद")
            else_branch = self.block_statement()
        
        return IfStatement(condition, then_branch, else_branch, line, col)
    
    def while_statement(self) -> WhileLoop:
        """Parse while loop: यावत् condition { statements }"""
        line, col = self.previous().line, self.previous().column
        
        condition = self.expression()
        self.consume(TokenType.VAAM_KURLY, "'{' की अपेक्षा 'यावत्' के बाद")
        
        body = self.block_statement()
        return WhileLoop(condition, body, line, col)
    
    def for_statement(self) -> ForLoop:
        """Parse for loop: प्रति variable in iterable { statements }"""
        line, col = self.previous().line, self.previous().column
        
        variable_token = self.consume(TokenType.NAAM, "चर नाम की अपेक्षा")
        variable = Identifier(variable_token.value, variable_token.line, variable_token.column)
        
        # TODO: Add 'in' keyword to lexer
        self.consume(TokenType.NAAM, "'में' की अपेक्षा")  # Temporary
        
        iterable = self.expression()
        self.consume(TokenType.VAAM_KURLY, "'{' की अपेक्षा")
        
        body = self.block_statement()
        return ForLoop(variable, iterable, body, line, col)
    
    def function_statement(self) -> FunctionDef:
        """Parse function definition: कार्य name(params) { statements }"""
        line, col = self.previous().line, self.previous().column
        
        name_token = self.consume(TokenType.NAAM, "फ़ंक्शन नाम की अपेक्षा")
        name = Identifier(name_token.value, name_token.line, name_token.column)
        
        self.consume(TokenType.VAAM_VRTTA, "'(' की अपेक्षा")
        
        parameters = []
        if not self.check(TokenType.DAKSH_VRTTA):
            parameters.append(Identifier(
                self.consume(TokenType.NAAM, "पैरामीटर नाम की अपेक्षा").value
            ))
            
            while self.match(TokenType.ALPA_VIRAM):
                param_token = self.consume(TokenType.NAAM, "पैरामीटर नाम की अपेक्षा")
                parameters.append(Identifier(param_token.value))
        
        self.consume(TokenType.DAKSH_VRTTA, "')' की अपेक्षा")
        self.consume(TokenType.VAAM_KURLY, "'{' की अपेक्षा")
        
        body = self.block_statement()
        return FunctionDef(name, parameters, body, None, line, col)
    
    def class_statement(self) -> ClassDef:
        """Parse class definition: वर्ग name { methods }"""
        line, col = self.previous().line, self.previous().column
        
        name_token = self.consume(TokenType.NAAM, "वर्ग नाम की अपेक्षा")
        name = Identifier(name_token.value, name_token.line, name_token.column)
        
        superclass = None
        # TODO: Add inheritance syntax
        
        self.consume(TokenType.VAAM_KURLY, "'{' की अपेक्षा")
        
        methods = []
        while not self.check(TokenType.DAKSH_KURLY) and not self.is_at_end():
            if self.match(TokenType.NAVAPANKTI):
                continue
            if self.match(TokenType.KAARYA):
                methods.append(self.function_statement())
            else:
                self.advance()  # Skip unknown tokens
        
        self.consume(TokenType.DAKSH_KURLY, "'}' की अपेक्षा")
        return ClassDef(name, superclass, methods, line, col)
    
    def return_statement(self) -> ReturnStatement:
        """Parse return statement: वापसी [expression]"""
        line, col = self.previous().line, self.previous().column
        
        value = None
        if not self.check(TokenType.NAVAPANKTI) and not self.is_at_end():
            value = self.expression()
        
        return ReturnStatement(value, line, col)
    
    def import_statement(self) -> ImportStatement:
        """Parse import statement: आयात module"""
        line, col = self.previous().line, self.previous().column
        
        module_token = self.consume(TokenType.NAAM, "मॉड्यूल नाम की अपेक्षा")
        module = module_token.value
        
        alias = None
        from_list = None
        
        return ImportStatement(module, alias, from_list, line, col)
    
    def variable_declaration(self) -> Assignment:
        """Parse variable declaration: धारणा name = value or स्थिर name = value"""
        # Advance past the DHARANA/STHIRA token
        keyword_token = self.advance()
        line, col = keyword_token.line, keyword_token.column
        
        name_token = self.consume(TokenType.NAAM, "चर नाम की अपेक्षा")
        name = Identifier(name_token.value, name_token.line, name_token.column)
        
        self.consume(TokenType.NIRDESH, "'=' की अपेक्षा")
        value = self.expression()
        
        return Assignment(name, value, line, col)
    
    def block_statement(self) -> Block:
        """Parse block statement: { statements }"""
        line, col = self.peek().line, self.peek().column
        statements = []
        
        while not self.check(TokenType.DAKSH_KURLY) and not self.is_at_end():
            if self.match(TokenType.NAVAPANKTI):
                continue
            
            stmt = self.statement()
            if stmt:
                statements.append(stmt)
        
        self.consume(TokenType.DAKSH_KURLY, "'}' की अपेक्षा")
        return Block(statements, line, col)
    
    def expression_statement(self) -> ExpressionStatement:
        """Parse expression statement"""
        expr = self.expression()
        return ExpressionStatement(expr)
    
    def expression(self) -> Expression:
        """Parse expression"""
        return self.assignment()
    
    def assignment(self) -> Expression:
        """Parse assignment expression"""
        expr = self.logical_or()
        
        if self.match(TokenType.NIRDESH):
            value = self.assignment()
            if isinstance(expr, Identifier):
                return Assignment(expr, value)
            else:
                raise SanskritSyntaxError("अवैध असाइनमेंट लक्ष्य", 
                                        self.previous().line, self.previous().column)
        
        return expr
    
    def logical_or(self) -> Expression:
        """Parse logical OR expression"""
        expr = self.logical_and()
        
        while self.match(TokenType.VA):
            operator = self.previous().value
            right = self.logical_and()
            expr = BinaryOperation(expr, operator, right)
        
        return expr
    
    def logical_and(self) -> Expression:
        """Parse logical AND expression"""
        expr = self.equality()
        
        while self.match(TokenType.CHA):
            operator = self.previous().value
            right = self.equality()
            expr = BinaryOperation(expr, operator, right)
        
        return expr
    
    def equality(self) -> Expression:
        """Parse equality expression"""
        expr = self.comparison()
        
        while self.match(TokenType.SAMA, TokenType.ASAMA):
            operator = self.previous().value
            right = self.comparison()
            expr = BinaryOperation(expr, operator, right)
        
        return expr
    
    def comparison(self) -> Expression:
        """Parse comparison expression"""
        expr = self.term()
        
        while self.match(TokenType.MAHAN, TokenType.MAHAN_SAMA, 
                          TokenType.LAGHU, TokenType.LAGHU_SAMA):
            operator = self.previous().value
            right = self.term()
            expr = BinaryOperation(expr, operator, right)
        
        return expr
    
    def term(self) -> Expression:
        """Parse term (addition/subtraction)"""
        expr = self.factor()
        
        while self.match(TokenType.VYAVAKALANA, TokenType.YOGA):
            operator = self.previous().value
            right = self.factor()
            expr = BinaryOperation(expr, operator, right)
        
        return expr
    
    def factor(self) -> Expression:
        """Parse factor (multiplication/division)"""
        expr = self.unary()
        
        while self.match(TokenType.BHAGA, TokenType.GUNA, TokenType.SHESH):
            operator = self.previous().value
            right = self.unary()
            expr = BinaryOperation(expr, operator, right)
        
        return expr
    
    def unary(self) -> Expression:
        """Parse unary expression"""
        if self.match(TokenType.NA, TokenType.VYAVAKALANA):
            operator = self.previous().value
            right = self.unary()
            return UnaryOperation(operator, right)
        
        return self.call()
    
    def call(self) -> Expression:
        """Parse function call"""
        expr = self.primary()
        
        while True:
            if self.match(TokenType.VAAM_VRTTA):
                expr = self.finish_call(expr)
            else:
                break
        
        return expr
    
    def finish_call(self, callee: Expression) -> FunctionCall:
        """Parse function call arguments"""
        arguments = []
        
        if not self.check(TokenType.DAKSH_VRTTA):
            arguments.append(self.expression())
            while self.match(TokenType.ALPA_VIRAM):
                arguments.append(self.expression())
        
        self.consume(TokenType.DAKSH_VRTTA, "')' की अपेक्षा")
        return FunctionCall(callee, arguments)
    
    def primary(self) -> Expression:
        """Parse primary expression"""
        if self.match(TokenType.SATYA):
            return Literal(True, self.previous().line, self.previous().column)
        
        if self.match(TokenType.ASATYA):
            return Literal(False, self.previous().line, self.previous().column)
        
        if self.match(TokenType.SHUNYA):
            return Literal(None, self.previous().line, self.previous().column)
        
        if self.match(TokenType.SANKHYA):
            value = self.previous().value
            # Convert Devanagari numerals to ASCII
            devanagari_digits = '०१२३४५६७८९'
            ascii_digits = '0123456789'
            for i, d in enumerate(devanagari_digits):
                value = value.replace(d, ascii_digits[i])
            
            if '.' in value:
                return Literal(float(value), self.previous().line, self.previous().column)
            else:
                return Literal(int(value), self.previous().line, self.previous().column)
        
        if self.match(TokenType.SHABDA):
            return Literal(self.previous().value, self.previous().line, self.previous().column)
        
        if self.match(TokenType.NAAM):
            return Identifier(self.previous().value, self.previous().line, self.previous().column)
        
        if self.match(TokenType.VAAM_VRTTA):
            expr = self.expression()
            self.consume(TokenType.DAKSH_VRTTA, "')' की अपेक्षा")
            return expr
        
        raise SanskritSyntaxError("अप्रत्याशित टोकन", 
                                self.peek().line, self.peek().column)
    
    def match(self, *types: TokenType) -> bool:
        """Check if current token matches any of the given types"""
        for token_type in types:
            if self.check(token_type):
                self.advance()
                return True
        return False
    
    def check(self, token_type: TokenType) -> bool:
        """Check if current token is of given type"""
        if self.is_at_end():
            return False
        return self.peek().type == token_type
    
    def advance(self) -> Token:
        """Consume current token and return it"""
        if not self.is_at_end():
            self.current += 1
        return self.previous()
    
    def is_at_end(self) -> bool:
        """Check if we're at end of tokens"""
        return self.peek().type == TokenType.EOF
    
    def peek(self) -> Token:
        """Return current token without advancing"""
        return self.tokens[self.current]
    
    def previous(self) -> Token:
        """Return previous token"""
        return self.tokens[self.current - 1]
    
    def consume(self, token_type: TokenType, message: str) -> Token:
        """Consume token of expected type or raise error"""
        if self.check(token_type):
            return self.advance()
        
        current_token = self.peek()
        raise SanskritSyntaxError(message, current_token.line, current_token.column)
    
    def synchronize(self) -> None:
        """Synchronize after a parse error"""
        self.advance()
        
        while not self.is_at_end():
            if self.previous().type == TokenType.NAVAPANKTI:
                return
            
            if self.peek().type in [TokenType.VARGA, TokenType.KAARYA, 
                                  TokenType.DHARANA, TokenType.PRATHI,
                                  TokenType.YADI, TokenType.YAVAT, 
                                  TokenType.VRATYAA]:
                return
            
            self.advance()
