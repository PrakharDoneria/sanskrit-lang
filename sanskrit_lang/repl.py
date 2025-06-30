"""
Sanskrit Language REPL
Read-Eval-Print Loop for interactive coding
"""

import sys
import traceback
from typing import List, Optional
from .interpreter import SanskritInterpreter
from .errors import SanskritError
from .docs import DocumentationSystem

class SanskritREPL:
    """Interactive Read-Eval-Print Loop"""
    
    def __init__(self):
        self.interpreter = SanskritInterpreter()
        self.history: List[str] = []
        self.docs = DocumentationSystem()
        self.multiline_buffer = ""
        self.in_multiline = False
        
    def run(self):
        """Start the REPL"""
        self.print_welcome()
        
        while True:
            try:
                line = self.read_input()
                
                if line is None:  # EOF
                    break
                
                if line.strip() == "":
                    continue
                
                # Handle special commands
                if self.handle_command(line):
                    continue
                
                # Handle multiline input
                if self.is_multiline_start(line) or self.in_multiline:
                    self.handle_multiline(line)
                    continue
                
                # Execute single line
                self.execute_line(line)
                
            except KeyboardInterrupt:
                print("\n(KeyboardInterrupt)")
                self.reset_multiline()
                continue
            except EOFError:
                break
            except Exception as e:
                print(f"REPL त्रुटि: {e}")
                self.reset_multiline()
        
        print("विदाई!")
    
    def print_welcome(self):
        """Print welcome message"""
        print("संस्कृत प्रोग्रामिंग भाषा v1.0.0")
        print("सहायता के लिए 'सहायता' टाइप करें, बाहर निकलने के लिए 'बाहर' टाइप करें")
        print()
    
    def read_input(self) -> Optional[str]:
        """Read input from user"""
        try:
            if self.in_multiline:
                prompt = "... "
            else:
                prompt = ">>> "
            
            return input(prompt)
        except EOFError:
            return None
    
    def handle_command(self, line: str) -> bool:
        """Handle special REPL commands"""
        line = line.strip()
        
        if line == "बाहर" or line == "exit":
            sys.exit(0)
        
        elif line == "सहायता" or line == "help":
            self.show_help()
            return True
        
        elif line == "इतिहास" or line == "history":
            self.show_history()
            return True
        
        elif line == "साफ" or line == "clear":
            self.clear_screen()
            return True
        
        elif line.startswith("दस्तावेज़") or line.startswith("doc"):
            # Documentation command
            parts = line.split()
            if len(parts) > 1:
                self.show_documentation(parts[1])
            else:
                self.show_documentation()
            return True
        
        elif line.startswith("उदाहरण") or line.startswith("example"):
            parts = line.split()
            if len(parts) > 1:
                self.show_example(parts[1])
            else:
                self.show_examples()
            return True
        
        elif line == "चर" or line == "vars":
            self.show_variables()
            return True
        
        return False
    
    def is_multiline_start(self, line: str) -> bool:
        """Check if line starts a multiline block"""
        stripped = line.strip()
        multiline_keywords = [
            'यदि', 'कार्य', 'वर्ग', 'यावत्', 'प्रति'
        ]
        
        for keyword in multiline_keywords:
            if stripped.startswith(keyword):
                return True
        
        return stripped.endswith('{') or stripped.endswith(':')
    
    def handle_multiline(self, line: str):
        """Handle multiline input"""
        if not self.in_multiline:
            self.in_multiline = True
            self.multiline_buffer = line + "\n"
        else:
            self.multiline_buffer += line + "\n"
        
        # Check if multiline is complete
        if line.strip() == "" or self.is_multiline_complete():
            self.execute_multiline()
    
    def is_multiline_complete(self) -> bool:
        """Check if multiline input is complete"""
        # Simple brace counting
        open_braces = self.multiline_buffer.count('{')
        close_braces = self.multiline_buffer.count('}')
        
        return open_braces <= close_braces
    
    def execute_multiline(self):
        """Execute multiline code"""
        if self.multiline_buffer.strip():
            self.execute_line(self.multiline_buffer)
        self.reset_multiline()
    
    def reset_multiline(self):
        """Reset multiline state"""
        self.in_multiline = False
        self.multiline_buffer = ""
    
    def execute_line(self, line: str):
        """Execute a line of code"""
        try:
            # Add to history
            self.history.append(line)
            
            # Execute
            self.interpreter.execute(line)
            
        except SanskritError as e:
            print(f"त्रुटि: {e}")
        except Exception as e:
            print(f"अज्ञात त्रुटि: {e}")
            if "--debug" in sys.argv:
                traceback.print_exc()
    
    def show_help(self):
        """Show help information"""
        help_text = """
संस्कृत प्रोग्रामिंग भाषा - सहायता

विशेष आदेश:
  सहायता / help     - यह सहायता दिखाएं
  बाहर / exit        - REPL से बाहर निकलें  
  इतिहास / history   - आदेश इतिहास दिखाएं
  साफ / clear        - स्क्रीन साफ करें
  चर / vars          - परिभाषित चर दिखाएं
  दस्तावेज़ [नाम]     - दस्तावेज़ दिखाएं
  उदाहरण [विषय]      - उदाहरण दिखाएं

मूल सिंटैक्स:
  चर परिभाषा:       धारणा नाम = मान
  फ़ंक्शन:          कार्य नाम(पैरामीटर) { ... }
  शर्त:            यदि शर्त { ... } अथवा { ... }
  लूप:             यावत् शर्त { ... }
  प्रिंट:           मुद्रण(संदेश)

अधिक जानकारी के लिए 'दस्तावेज़' का उपयोग करें।
        """
        print(help_text)
    
    def show_history(self):
        """Show command history"""
        if not self.history:
            print("कोई इतिहास उपलब्ध नहीं है")
            return
        
        print("आदेश इतिहास:")
        for i, command in enumerate(self.history[-10:], 1):  # Show last 10
            print(f"{i:2d}: {command}")
    
    def clear_screen(self):
        """Clear screen"""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_documentation(self, topic: str = None):
        """Show documentation"""
        if topic:
            doc = self.docs.get_documentation(topic)
            if doc:
                print(doc)
            else:
                print(f"'{topic}' के लिए दस्तावेज़ नहीं मिला")
        else:
            print("उपलब्ध दस्तावेज़ विषय:")
            for topic in self.docs.get_topics():
                print(f"  - {topic}")
    
    def show_example(self, topic: str = None):
        """Show examples"""
        examples = {
            'चर': '''
# चर परिभाषा
धारणा नाम = "राम"
धारणा उम्र = २५
मुद्रण(नाम, उम्र)
            ''',
            
            'फ़ंक्शन': '''
# फ़ंक्शन परिभाषा
कार्य योग(क, ख) {
    वापसी क + ख
}

परिणाम = योग(५, ३)
मुद्रण(परिणाम)
            ''',
            
            'शर्त': '''
# शर्त का उदाहरण
उम्र = २०

यदि उम्र >= १८ {
    मुद्रण("वयस्क")
} अथवा {
    मुद्रण("नाबालिग")
}
            ''',
            
            'लूप': '''
# लूप का उदाहरण
गिनती = १

यावत् गिनती <= ५ {
    मुद्रण(गिनती)
    गिनती = गिनती + १
}
            '''
        }
        
        if topic and topic in examples:
            print(f"उदाहरण - {topic}:")
            print(examples[topic])
        else:
            print("उपलब्ध उदाहरण:")
            for example_topic in examples.keys():
                print(f"  - {example_topic}")
    
    def show_examples(self):
        """Show all available examples"""
        self.show_example()
    
    def show_variables(self):
        """Show defined variables"""
        vars_dict = self.interpreter.environment.values
        if not vars_dict:
            print("कोई चर परिभाषित नहीं है")
            return
        
        print("परिभाषित चर:")
        for name, value in vars_dict.items():
            # Don't show built-in functions
            if not callable(value):
                print(f"  {name} = {value} ({type(value).__name__})")
