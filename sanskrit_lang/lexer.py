"""
Sanskrit Language Lexer
Tokenizes Sanskrit-inspired source code
"""

import re
from enum import Enum
from dataclasses import dataclass
from typing import List, Iterator, Optional

class TokenType(Enum):
    # Literals
    SANKHYA = "SANKHYA"  # Number
    SHABDA = "SHABDA"    # String
    SATYA = "SATYA"      # True
    ASATYA = "ASATYA"    # False
    SHUNYA = "SHUNYA"    # None/Null
    
    # Identifiers
    NAAM = "NAAM"        # Identifier/Name
    
    # Keywords - using Sanskrit terms
    YADI = "YADI"        # if
    ATHAVA = "ATHAVA"    # else
    YAVAT = "YAVAT"      # while  
    PRATHI = "PRATHI"    # for
    KAARYA = "KAARYA"    # function/def
    VRATYAA = "VRATYAA"  # return
    VARGA = "VARGA"      # class
    DHARANA = "DHARANA"  # var/let
    STHIRA = "STHIRA"    # const
    AAYAT = "AAYAT"      # import
    SE = "SE"            # from
    
    # Operators
    YOGA = "YOGA"        # + (addition)
    VYAVAKALANA = "VYAVAKALANA"  # - (subtraction)
    GUNA = "GUNA"        # * (multiplication)
    BHAGA = "BHAGA"      # / (division)
    SHESH = "SHESH"      # % (modulo)
    SAMA = "SAMA"        # == (equal)
    ASAMA = "ASAMA"      # != (not equal)
    LAGHU = "LAGHU"      # < (less than)
    MAHAN = "MAHAN"      # > (greater than)
    LAGHU_SAMA = "LAGHU_SAMA"  # <= (less equal)
    MAHAN_SAMA = "MAHAN_SAMA"  # >= (greater equal)
    NIRDESH = "NIRDESH"  # = (assignment)
    
    # Logical operators
    CHA = "CHA"          # and
    VA = "VA"            # or
    NA = "NA"            # not
    
    # Punctuation
    VIRAM = "VIRAM"      # . (dot)
    ALPA_VIRAM = "ALPA_VIRAM"  # , (comma)
    ARDHA_VIRAM = "ARDHA_VIRAM"  # ; (semicolon)
    UTKARSH = "UTKARSH"  # : (colon)
    
    # Brackets
    VAAM_VRTTA = "VAAM_VRTTA"    # ( 
    DAKSH_VRTTA = "DAKSH_VRTTA"  # )
    VAAM_KONA = "VAAM_KONA"      # [
    DAKSH_KONA = "DAKSH_KONA"    # ]
    VAAM_KURLY = "VAAM_KURLY"    # {
    DAKSH_KURLY = "DAKSH_KURLY"  # }
    
    # Special
    NAVAPANKTI = "NAVAPANKTI"    # Newline
    EOF = "EOF"
    WHITESPACE = "WHITESPACE"

@dataclass
class Token:
    type: TokenType
    value: str
    line: int
    column: int

class SanskritLexer:
    """Lexical analyzer for Sanskrit programming language"""
    
    def __init__(self, source: str):
        self.source = source
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens = []
        
        # Sanskrit keyword mapping
        self.keywords = {
            'यदि': TokenType.YADI,
            'अथवा': TokenType.ATHAVA,
            'यावत्': TokenType.YAVAT,
            'प्रति': TokenType.PRATHI,
            'कार्य': TokenType.KAARYA,
            'वापसी': TokenType.VRATYAA,
            'वर्ग': TokenType.VARGA,
            'धारणा': TokenType.DHARANA,
            'स्थिर': TokenType.STHIRA,
            'आयात': TokenType.AAYAT,
            'से': TokenType.SE,
            'सत्य': TokenType.SATYA,
            'असत्य': TokenType.ASATYA,
            'शून्य': TokenType.SHUNYA,
            'च': TokenType.CHA,
            'वा': TokenType.VA,
            'न': TokenType.NA,
        }
        
        # Operator mapping
        self.operators = {
            '+': TokenType.YOGA,
            '-': TokenType.VYAVAKALANA,
            '*': TokenType.GUNA,
            '/': TokenType.BHAGA,
            '%': TokenType.SHESH,
            '==': TokenType.SAMA,
            '!=': TokenType.ASAMA,
            '<': TokenType.LAGHU,
            '>': TokenType.MAHAN,
            '<=': TokenType.LAGHU_SAMA,
            '>=': TokenType.MAHAN_SAMA,
            '=': TokenType.NIRDESH,
        }
        
        # Punctuation mapping
        self.punctuation = {
            '.': TokenType.VIRAM,
            ',': TokenType.ALPA_VIRAM,
            ';': TokenType.ARDHA_VIRAM,
            ':': TokenType.UTKARSH,
            '(': TokenType.VAAM_VRTTA,
            ')': TokenType.DAKSH_VRTTA,
            '[': TokenType.VAAM_KONA,
            ']': TokenType.DAKSH_KONA,
            '{': TokenType.VAAM_KURLY,
            '}': TokenType.DAKSH_KURLY,
        }
    
    def current_char(self) -> Optional[str]:
        """Get current character"""
        if self.position >= len(self.source):
            return None
        return self.source[self.position]
    
    def peek_char(self, offset: int = 1) -> Optional[str]:
        """Peek at character ahead"""
        pos = self.position + offset
        if pos >= len(self.source):
            return None
        return self.source[pos]
    
    def advance(self) -> None:
        """Move to next character"""
        if self.position < len(self.source):
            if self.source[self.position] == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.position += 1
    
    def skip_whitespace(self) -> None:
        """Skip whitespace characters (except newlines)"""
        while self.current_char() and self.current_char() in ' \t\r':
            self.advance()
    
    def read_number(self) -> Token:
        """Read numeric literal"""
        start_pos = self.position
        start_col = self.column
        
        # Handle Devanagari numerals and ASCII numerals
        while self.current_char() and (self.current_char().isdigit() or 
                                     self.current_char() in '०१२३४५६७८९'):
            self.advance()
        
        # Handle decimal point
        if self.current_char() == '.' and self.peek_char() and self.peek_char().isdigit():
            self.advance()  # consume '.'
            while self.current_char() and self.current_char().isdigit():
                self.advance()
        
        value = self.source[start_pos:self.position]
        return Token(TokenType.SANKHYA, value, self.line, start_col)
    
    def read_string(self, quote_char: str) -> Token:
        """Read string literal"""
        start_col = self.column
        self.advance()  # consume opening quote
        value = ""
        
        while self.current_char() and self.current_char() != quote_char:
            if self.current_char() == '\\':
                self.advance()
                if self.current_char() in 'nrtbf"\'\\':
                    escape_chars = {'n': '\n', 'r': '\r', 't': '\t', 
                                  'b': '\b', 'f': '\f', '"': '"', 
                                  "'": "'", '\\': '\\'}
                    value += escape_chars.get(self.current_char(), self.current_char())
                    self.advance()
                else:
                    value += self.current_char()
                    self.advance()
            else:
                value += self.current_char()
                self.advance()
        
        if self.current_char() == quote_char:
            self.advance()  # consume closing quote
        
        return Token(TokenType.SHABDA, value, self.line, start_col)
    
    def read_identifier(self) -> Token:
        """Read identifier or keyword"""
        start_pos = self.position
        start_col = self.column
        
        # Support both ASCII and Devanagari identifiers
        while (self.current_char() and 
               (self.current_char().isalnum() or 
                self.current_char() == '_' or
                ord(self.current_char()) >= 0x0900)):  # Devanagari range
            self.advance()
        
        value = self.source[start_pos:self.position]
        token_type = self.keywords.get(value, TokenType.NAAM)
        return Token(token_type, value, self.line, start_col)
    
    def read_operator(self) -> Token:
        """Read operator"""
        start_col = self.column
        char = self.current_char()
        
        # Check for two-character operators first
        if char in '<>!=':
            next_char = self.peek_char()
            if next_char == '=':
                op = char + next_char
                self.advance()
                self.advance()
                return Token(self.operators[op], op, self.line, start_col)
        
        # Single character operators
        self.advance()
        token_type = self.operators.get(char, TokenType.NAAM)
        return Token(token_type, char, self.line, start_col)
    
    def tokenize(self) -> List[Token]:
        """Tokenize the source code"""
        tokens = []
        
        while self.position < len(self.source):
            char = self.current_char()
            
            if char is None:
                break
            
            # Skip whitespace (except newlines)
            if char in ' \t\r':
                self.skip_whitespace()
                continue
            
            # Handle newlines
            if char == '\n':
                tokens.append(Token(TokenType.NAVAPANKTI, char, self.line, self.column))
                self.advance()
                continue
            
            # Handle comments (# style)
            if char == '#':
                while self.current_char() and self.current_char() != '\n':
                    self.advance()
                continue
            
            # Handle numbers
            if char.isdigit() or char in '०१२३४५६७८९':
                tokens.append(self.read_number())
                continue
            
            # Handle strings
            if char in '"\'':
                tokens.append(self.read_string(char))
                continue
            
            # Handle identifiers and keywords
            if (char.isalpha() or char == '_' or ord(char) >= 0x0900):
                tokens.append(self.read_identifier())
                continue
            
            # Handle operators
            if char in '+-*/%=<>!':
                tokens.append(self.read_operator())
                continue
            
            # Handle punctuation
            if char in self.punctuation:
                tokens.append(Token(self.punctuation[char], char, self.line, self.column))
                self.advance()
                continue
            
            # Unknown character
            self.advance()
        
        tokens.append(Token(TokenType.EOF, '', self.line, self.column))
        return tokens
