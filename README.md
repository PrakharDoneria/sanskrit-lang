# संस्कृत प्रोग्रामिंग भाषा (Sanskrit Programming Language)

A Sanskrit-inspired programming language with Python-based interpreter, built-in editor, and REPL.

## Overview

Sanskrit Programming Language is a modern programming language that draws inspiration from the precision, structure, and elegance of Sanskrit grammar. It features Sanskrit-based syntax, strong type inference, and a comprehensive standard library with Sanskrit naming conventions.

## Features

### Core Language Features
- **Sanskrit-based Syntax**: Keywords, operators, and grammar follow Sanskrit terminology
- **Strong Type System**: Elegant type inference inspired by Sanskrit word classification (वर्ण)
- **Python-based Interpreter**: Written in pure Python for portability and ease of use
- **Built-in Editor**: GUI editor with syntax highlighting using tkinter
- **Interactive REPL**: Read-Eval-Print Loop for live coding and experimentation
- **Sanskrit Error Messages**: Clear, informative error messages in Sanskrit/Devanagari

### Standard Library (मानक पुस्तकालय)
- **गणित (Ganita)**: Mathematics and numerical operations
- **शब्द (Shabda)**: String manipulation and text processing  
- **प्रवेश (Pravesh)**: Input/output operations and file handling

### Advanced Features
- **Documentation System**: Built-in `doc` command for help and documentation
- **Example Programs**: Comprehensive examples demonstrating language features
- **Type Safety**: Compile-time type checking with Sanskrit-inspired type names
- **Unicode Support**: Full support for Devanagari script and Sanskrit text

## Installation

### Requirements
- Python 3.8 or higher
- tkinter (usually included with Python)
- No external dependencies required for core functionality

### Quick Install
```bash
git clone https://github.com/prakhardoneria/sanskrit-lang.git
cd sanskrit-lang
python main.py --help
```

## Usage

### Running the REPL (Interactive Mode)
```bash
python main.py --repl
# or simply
python main.py
```

### Using the Built-in Editor
```bash
python main.py --editor
```

### Running Sanskrit Programs
```bash
python main.py examples/hello.sans
python main.py examples/fibonacci.sans
python main.py examples/types.sans
```

## Language Syntax

### Basic Syntax
```sanskrit
# Variables (चर)
धारणा नाम = "राम"        # Variable declaration
धारणा उम्र = २५          # Using Devanagari numerals
स्थिर पाई = ३.१४१५९      # Constant declaration

# Output (आउटपुट)  
मुद्रण("नमस्ते संसार!")    # Print statement
मुद्रण("नाम:", नाम)       # Print with variables

# Functions (कार्य)
कार्य अभिवादन(व्यक्ति) {
    मुद्रण("नमस्कार", व्यक्ति)
    वापसी सत्य            # Return statement
}

# Conditionals (शर्त)
यदि उम्र >= १८ {
    मुद्रण("वयस्क")
} अथवा {
    मुद्रण("नाबालिग")
}

# Loops (लूप)
धारणा i = १
यावत् i <= ५ {           # While loop
    मुद्रण(i)
    i = i + १
}

प्रति संख्या में सूची {     # For loop
    मुद्रण(संख्या)
}
```

### Data Types
- **संख्या (Numbers)**: १२३, ३.१४, -५
- **शब्द (Strings)**: "नमस्ते", 'Hello'  
- **सत्य/असत्य (Booleans)**: सत्य, असत्य
- **शून्य (Null)**: शून्य

### Operators
- **Arithmetic**: + (yoga), - (vyavakalana), * (guna), / (bhaga), % (shesh)
- **Comparison**: == (sama), != (asama), < (laghu), > (mahan), <= (laghu_sama), >= (mahan_sama)
- **Logical**: च (and), वा (or), न (not)

### Built-in Functions
- **मुद्रण()** - Print output
- **प्रकार()** - Get type of variable
- **लम्बाई()** - Get length
- **संख्या()** - Convert to number
- **सुन्दर()** - Convert to string

### Standard Library Modules

#### गणित (Ganita) - Mathematics
```sanskrit
आयात गणित
गणित.वर्गमूल(१६)        # Square root: 4
गणित.sin(गणित.pi/२)    # Sine: 1
गणित.factorial(५)      # Factorial: 120
```

#### शब्द (Shabda) - String Operations  
```sanskrit
आयात शब्द
शब्द.uchcha("नमस्ते")    # Uppercase
शब्द.lambai("संस्कृत")   # Length: 7
शब्द.vibhajan("क,ख,ग", ",")  # Split
```

#### प्रवेश (Pravesh) - Input/Output
```sanskrit
आयात प्रवेश
नाम = प्रवेश.paath("नाम दर्ज करें: ")      # Input
प्रवेश.file_padhiye("test.txt")           # Read file
प्रवेश.file_likhiye("output.txt", "data") # Write file
```

## Example Programs

The `examples/` directory contains sample programs:

- **hello.sans** - Basic syntax demonstration with variables, functions, and loops
- **fibonacci.sans** - Fibonacci sequence using both recursive and iterative approaches
- **types.sans** - Type system examples and type conversions

## REPL Commands

When using the interactive REPL, you can use these special commands:

- `सहायता` / `help` - Show help information
- `बाहर` / `exit` - Exit the REPL
- `इतिहास` / `history` - Show command history  
- `साफ` / `clear` - Clear screen
- `चर` / `vars` - Show defined variables
- `दस्तावेज़ [topic]` - Show documentation for a topic
- `उदाहरण [topic]` - Show examples

## Error Messages

All error messages are displayed in Sanskrit/Devanagari script:

- **व्याकरण त्रुटि** - Syntax Error
- **रनटाइम त्रुटि** - Runtime Error  
- **प्रकार त्रुटि** - Type Error
- **नाम त्रुटि** - Name Error

## Features

✅ **Complete Implementation**
- Sanskrit-based lexer with Devanagari support
- Recursive descent parser with proper AST generation
- Tree-walking interpreter with environment-based scoping
- Variable declarations and assignments  
- Control flow (if/else, while loops, for loops)
- Function definitions and calls with parameters
- Built-in functions and standard library modules
- Interactive REPL with command history and help
- GUI editor with syntax highlighting
- Comprehensive error handling in Sanskrit

✅ **Unicode Support**
- Full Devanagari script support for keywords and identifiers
- Devanagari numeral support (०१२३४५६७८९)
- Mixed Sanskrit/English identifier support
- Unicode string handling

✅ **Development Tools**
- Built-in syntax highlighting editor
- Interactive REPL with special commands
- Example programs demonstrating language features
- Built-in documentation system

## Contributing

The Sanskrit Programming Language is designed to showcase Sanskrit-inspired programming concepts. The implementation demonstrates:

1. **Sanskrit Grammar Influence**: Keywords and operators follow Sanskrit terminology
2. **Type System**: Inspired by Sanskrit word classification (वर्ण)
3. **Cultural Programming**: Bridging ancient wisdom with modern technology
4. **Educational Value**: Teaching programming through Sanskrit linguistic concepts

## License

This project is open source and available for educational and research purposes
