#!/usr/bin/env python3
"""
Sanskrit Programming Language CLI
Command-line interface for the Sanskrit programming language
"""

import sys
import os
import argparse
from pathlib import Path

# Add the Sanskrit language modules to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sanskrit_lang.interpreter import SanskritInterpreter
from sanskrit_lang.repl import SanskritREPL
from sanskrit_lang.errors import SanskritError

def get_version():
    """Get the current version of Sanskrit language"""
    return "1.0.0"

def show_help():
    """Show detailed help information"""
    help_text = """
संस्कृत प्रोग्रामिंग भाषा (Sanskrit Programming Language) v{version}

Usage:
  sans [file.sans]           # Run a Sanskrit program file
  sans --repl               # Start interactive REPL
  sans --editor             # Launch GUI editor  
  sans --help/-h            # Show this help
  sans --version/-v         # Show version

Examples:
  sans hello.sans           # Run hello.sans program
  sans examples/fibonacci.sans  # Run fibonacci example
  sans --repl               # Start interactive mode
  
File Extensions:
  .sans                     # Sanskrit program files

Language Features:
  - Sanskrit-based keywords (यदि, यावत्, कार्य, etc.)
  - Devanagari script support
  - Variables, functions, loops, conditionals
  - Built-in standard library modules
  - Interactive REPL with command history
  - GUI editor with syntax highlighting

Standard Library:
  गणित (ganita)             # Mathematics functions
  शब्द (shabda)             # String operations  
  प्रवेश (pravesh)           # Input/output operations

Example Program:
  # hello.sans
  मुद्रण("नमस्ते संसार!")
  
  धारणा नाम = "राम"
  मुद्रण("नमस्कार", नाम)
  
  धारणा i = १
  यावत् i <= ५ {{
      मुद्रण(i)
      i = i + १
  }}

For more information and examples, visit:
https://github.com/PrakharDoneria/sanskrit-lang

""".format(version=get_version())
    print(help_text)

def run_file(file_path):
    """Run a Sanskrit program file"""
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"त्रुटि: फाइल '{file_path}' नहीं मिली")
            print(f"Error: File '{file_path}' not found")
            sys.exit(1)
        
        # Check file extension
        if not file_path.endswith('.sans'):
            print("चेतावनी: फाइल एक्सटेंशन '.sans' नहीं है")
            print("Warning: File extension is not '.sans'")
        
        # Read and execute the file
        with open(file_path, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        # Create interpreter and execute
        interpreter = SanskritInterpreter()
        interpreter.execute(source_code)
        
    except SanskritError as e:
        print(f"संस्कृत त्रुटि: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"त्रुटि: फाइल '{file_path}' नहीं मिली")
        print(f"Error: File '{file_path}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"अज्ञात त्रुटि: {e}")
        print(f"Unknown error: {e}")
        sys.exit(1)

def start_repl():
    """Start the interactive REPL"""
    try:
        repl = SanskritREPL()
        repl.run()
    except KeyboardInterrupt:
        print("\nREPL बंद किया गया")
        print("REPL closed")
    except Exception as e:
        print(f"REPL त्रुटि: {e}")
        print(f"REPL error: {e}")
        sys.exit(1)

def start_editor():
    """Start the GUI editor"""
    try:
        from sanskrit_lang.editor import SanskritEditor
        editor = SanskritEditor()
        editor.run()
    except ImportError as e:
        print("GUI editor के लिए tkinter आवश्यक है")
        print("tkinter is required for GUI editor")
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Editor त्रुटि: {e}")
        print(f"Editor error: {e}")
        sys.exit(1)

def main():
    """Main CLI entry point"""
    # Handle special cases for help and version without argparse
    if len(sys.argv) == 1:
        # No arguments - start REPL
        start_repl()
        return
    
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        
        # Handle help
        if arg in ['--help', '-h', 'help', 'सहायता']:
            show_help()
            return
        
        # Handle version
        if arg in ['--version', '-v', 'version']:
            print(f"Sanskrit Programming Language v{get_version()}")
            return
        
        # Handle REPL
        if arg in ['--repl', 'repl']:
            start_repl()
            return
        
        # Handle editor
        if arg in ['--editor', 'editor']:
            start_editor()
            return
        
        # Otherwise treat as file to run
        if arg.startswith('-'):
            print(f"अज्ञात विकल्प: {arg}")
            print(f"Unknown option: {arg}")
            print("Use 'sans --help' for usage information")
            sys.exit(1)
        else:
            run_file(arg)
            return
    
    # Multiple arguments - show error
    print("त्रुटि: अधिक तर्क दिए गए")
    print("Error: Too many arguments")
    print("Use 'sans --help' for usage information")
    sys.exit(1)

if __name__ == '__main__':
    main()