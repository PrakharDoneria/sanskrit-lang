#!/usr/bin/env python3
"""
Sanskrit Programming Language
A Sanskrit-inspired programming language with Python-based interpreter
"""

import sys
import argparse
from sanskrit_lang.repl import SanskritREPL
from sanskrit_lang.interpreter import SanskritInterpreter
from sanskrit_lang.editor import SanskritEditor

def main():
    parser = argparse.ArgumentParser(description='Sanskrit Programming Language')
    parser.add_argument('file', nargs='?', help='Sanskrit source file to execute')
    parser.add_argument('--repl', '-r', action='store_true', help='Start interactive REPL')
    parser.add_argument('--editor', '-e', action='store_true', help='Open built-in editor')
    parser.add_argument('--version', '-v', action='version', version='Sanskrit 1.0.0')
    
    args = parser.parse_args()
    
    if args.editor:
        # Start GUI editor
        editor = SanskritEditor()
        editor.run()
    elif args.repl or not args.file:
        # Start REPL
        repl = SanskritREPL()
        repl.run()
    else:
        # Execute file
        interpreter = SanskritInterpreter()
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                source = f.read()
            interpreter.execute(source)
        except FileNotFoundError:
            print(f"त्रुटि: फ़ाइल '{args.file}' नहीं मिली")
            sys.exit(1)
        except Exception as e:
            print(f"त्रुटि: {e}")
            sys.exit(1)

if __name__ == '__main__':
    main()
