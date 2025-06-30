#!/usr/bin/env python3
from sanskrit_lang.lexer import SanskritLexer
from sanskrit_lang.parser import SanskritParser

# Test simple assignment parsing
source = 'धारणा x = १०'
print(f"Testing source: {source}")

lexer = SanskritLexer(source)
tokens = lexer.tokenize()

print("Tokens:")
for token in tokens:
    print(f"  {token.type}: {token.value}")

parser = SanskritParser(tokens)
ast = parser.parse()

print(f"\nAST statements count: {len(ast.statements)}")
for i, stmt in enumerate(ast.statements):
    print(f"Statement {i}: {type(stmt).__name__}")
    if hasattr(stmt, 'expression'):
        print(f"  Expression: {type(stmt.expression).__name__}")