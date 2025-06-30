"""
Sanskrit Programming Language
A Sanskrit-inspired programming language implementation
"""

__version__ = "1.0.0"
__author__ = "Sanskrit Language Team"

from .lexer import SanskritLexer
from .parser import SanskritParser
from .interpreter import SanskritInterpreter
from .repl import SanskritREPL
from .editor import SanskritEditor

__all__ = [
    'SanskritLexer',
    'SanskritParser', 
    'SanskritInterpreter',
    'SanskritREPL',
    'SanskritEditor'
]
