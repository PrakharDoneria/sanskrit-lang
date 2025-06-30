# Sanskrit Programming Language - Replit.md

## Overview

The Sanskrit Programming Language is a modern programming language that draws inspiration from the precision, structure, and elegance of Sanskrit grammar. It features Sanskrit-based syntax with keywords, operators, and grammar following Sanskrit terminology. The language includes a Python-based interpreter, built-in GUI editor with syntax highlighting, and an interactive REPL for live coding and experimentation.

## System Architecture

### Language Design
- **Lexical Analysis**: Custom lexer (`lexer.py`) tokenizes Sanskrit-inspired source code with Sanskrit keywords like `यदि` (if), `यावत्` (while), `कार्य` (function)
- **Parsing**: Recursive descent parser (`parser.py`) builds Abstract Syntax Trees from tokens
- **AST Representation**: Well-defined AST node hierarchy (`ast_nodes.py`) with visitor pattern support
- **Interpretation**: Tree-walking interpreter (`interpreter.py`) executes the AST directly

### Type System
- **Sanskrit-Inspired Types**: Type system based on Sanskrit word classifications (वर्ण)
- **Core Types**: 
  - `SANKHYA` (संख्या) - Numbers
  - `SHABDA` (शब्द) - Strings
  - `SATYA_ASATYA` (सत्य-असत्य) - Booleans
  - `SHUNYA` (शून्य) - Null/None
  - `SAMUHA` (समूह) - Collections
  - `KAARYA` (कार्य) - Functions
  - `VARGA` (वर्ग) - Classes

## Key Components

### Frontend Components
1. **GUI Editor** (`editor.py`):
   - Built with tkinter for cross-platform compatibility
   - Syntax highlighting for Sanskrit keywords
   - File operations (open, save, new)
   - Integrated execution environment

2. **REPL** (`repl.py`):
   - Interactive Read-Eval-Print Loop
   - Multiline input support
   - Command history
   - Built-in documentation system
   - Special commands for help and debugging

### Backend Components
1. **Interpreter Core**:
   - Environment-based variable scoping
   - Function call stack management
   - Error handling with Sanskrit error messages
   - Support for control flow (if, while, for)

2. **Standard Library** (`stdlib/`):
   - **Ganita** (गणित): Mathematical operations
   - **Shabda** (शब्द): String manipulation
   - **Pravesh** (प्रवेश): Input/output operations

### Error System
- Custom error hierarchy with Sanskrit error messages
- Location tracking (line/column numbers)
- Formatted error output in Devanagari script
- Runtime, syntax, type, and name error categories

## Data Flow

1. **Source Input**: Sanskrit source code entered via editor, REPL, or file
2. **Lexical Analysis**: Source code tokenized into Sanskrit language tokens
3. **Parsing**: Tokens parsed into Abstract Syntax Tree
4. **Type Checking**: Static type analysis (planned feature)
5. **Interpretation**: AST traversed and executed by tree-walking interpreter
6. **Output**: Results displayed in terminal or editor console

## External Dependencies

### Core Dependencies
- **Python 3.8+**: Base runtime environment
- **tkinter**: GUI framework for editor (typically bundled with Python)
- **Standard Library**: Uses Python's built-in modules (re, os, sys, math, etc.)

### Optional Dependencies
- No external pip packages required for core functionality
- All dependencies are part of Python standard library

## Deployment Strategy

### Local Development
- Direct execution via `python main.py`
- Multiple entry points: file execution, REPL mode, or editor mode
- Cross-platform compatibility through Python and tkinter

### Distribution Options
- **Source Distribution**: Git repository with Python source files
- **Standalone Executable**: Can be packaged with PyInstaller for distribution
- **Package Manager**: Could be distributed via pip in the future

### Platform Support
- **Windows**: Full support via Python + tkinter
- **macOS**: Full support via Python + tkinter  
- **Linux**: Full support via Python + tkinter
- **Unicode Support**: Full Devanagari script support across all platforms

## User Preferences

Preferred communication style: Simple, everyday language.

## Recent Changes

✅ **Bug Fix - Variable Assignment in Loops (June 30, 2025)**
- Fixed critical scoping issue where variable assignments inside loop bodies weren't persisting
- Modified Environment.assign() method to create variables in current scope if not found in any parent scope
- Changed assignment visitor to use assign() instead of define() for proper scoping behavior
- All example programs now execute correctly including hello.sans and fibonacci.sans

✅ **Complete Language Implementation (June 30, 2025)**
- Sanskrit programming language fully functional with all major features
- Working lexer, parser, AST, and interpreter components
- Built-in REPL and GUI editor operational
- Standard library modules (ganita, shabda, pravesh) implemented
- Comprehensive error handling in Sanskrit/Devanagari
- Full Unicode and Devanagari numeral support

## Changelog

- June 30, 2025: Critical bug fix - variable assignment scoping in loops resolved
- June 30, 2025: Initial setup and complete language implementation