"""
Sanskrit Language Editor
Built-in GUI editor with syntax highlighting
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import re
from typing import Dict, List, Tuple
from .interpreter import SanskritInterpreter
from .errors import SanskritError

class SyntaxHighlighter:
    """Syntax highlighter for Sanskrit code"""
    
    def __init__(self, text_widget: tk.Text):
        self.text_widget = text_widget
        self.setup_tags()
        
        # Sanskrit keyword patterns
        self.patterns = {
            'keyword': [
                r'\b(यदि|अथवा|यावत्|प्रति|कार्य|वापसी|वर्ग|धारणा|स्थिर|आयात|से)\b',
                r'\b(सत्य|असत्य|शून्य|च|वा|न)\b'
            ],
            'number': [
                r'\b\d+(\.\d+)?\b',
                r'\b[०१२३४५६७८९]+(\.[०१२३४५६७८९]+)?\b'
            ],
            'string': [
                r'"[^"]*"',
                r"'[^']*'"
            ],
            'comment': [
                r'#.*$'
            ],
            'operator': [
                r'[+\-*/%=<>!]=?',
                r'[+\-*/%=<>!]'
            ],
            'function': [
                r'\b[a-zA-Z_][a-zA-Z0-9_]*(?=\s*\()',
                r'\b[ा-ॿ][ा-ॿ]*(?=\s*\()'
            ]
        }
    
    def setup_tags(self):
        """Setup text tags for syntax highlighting"""
        self.text_widget.tag_configure('keyword', foreground='#0066cc', font=('Consolas', 11, 'bold'))
        self.text_widget.tag_configure('string', foreground='#009900')
        self.text_widget.tag_configure('comment', foreground='#666666', font=('Consolas', 11, 'italic'))
        self.text_widget.tag_configure('number', foreground='#cc6600')
        self.text_widget.tag_configure('operator', foreground='#cc0066')
        self.text_widget.tag_configure('function', foreground='#6600cc')
        self.text_widget.tag_configure('error', background='#ffcccc')
    
    def highlight(self):
        """Apply syntax highlighting to entire text"""
        # Clear existing tags
        for tag in ['keyword', 'string', 'comment', 'number', 'operator', 'function', 'error']:
            self.text_widget.tag_remove(tag, '1.0', tk.END)
        
        content = self.text_widget.get('1.0', tk.END)
        lines = content.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            for tag, patterns in self.patterns.items():
                for pattern in patterns:
                    for match in re.finditer(pattern, line, re.MULTILINE):
                        start = f"{line_num}.{match.start()}"
                        end = f"{line_num}.{match.end()}"
                        self.text_widget.tag_add(tag, start, end)

class SanskritEditor:
    """Main editor application"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("संस्कृत प्रोग्रामिंग भाषा - संपादक")
        self.root.geometry("1000x700")
        
        # Editor state
        self.current_file = None
        self.modified = False
        self.interpreter = SanskritInterpreter()
        
        self.setup_ui()
        self.setup_bindings()
        
        # Auto-highlight timer
        self.highlight_timer = None
    
    def setup_ui(self):
        """Setup the user interface"""
        # Create main menu
        self.create_menu()
        
        # Create toolbar
        self.create_toolbar()
        
        # Create main content area
        self.create_content_area()
        
        # Create status bar
        self.create_status_bar()
        
        # Update UI state
        self.update_title()
    
    def create_menu(self):
        """Create menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="फ़ाइल", menu=file_menu)
        file_menu.add_command(label="नया (Ctrl+N)", command=self.new_file)
        file_menu.add_command(label="खोलें (Ctrl+O)", command=self.open_file)
        file_menu.add_command(label="सेव करें (Ctrl+S)", command=self.save_file)
        file_menu.add_command(label="इस रूप में सेव करें", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="बाहर निकलें", command=self.quit_app)
        
        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="संपादन", menu=edit_menu)
        edit_menu.add_command(label="पूर्ववत करें (Ctrl+Z)", command=self.undo)
        edit_menu.add_command(label="दोहराएं (Ctrl+Y)", command=self.redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="कॉपी (Ctrl+C)", command=self.copy)
        edit_menu.add_command(label="कट (Ctrl+X)", command=self.cut)
        edit_menu.add_command(label="पेस्ट (Ctrl+V)", command=self.paste)
        edit_menu.add_separator()
        edit_menu.add_command(label="सभी चुनें (Ctrl+A)", command=self.select_all)
        edit_menu.add_command(label="खोजें (Ctrl+F)", command=self.find)
        
        # Run menu
        run_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="चलाएं", menu=run_menu)
        run_menu.add_command(label="प्रोग्राम चलाएं (F5)", command=self.run_program)
        run_menu.add_command(label="REPL खोलें", command=self.open_repl)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="सहायता", menu=help_menu)
        help_menu.add_command(label="सिंटैक्स गाइड", command=self.show_syntax_guide)
        help_menu.add_command(label="उदाहरण", command=self.show_examples)
        help_menu.add_command(label="के बारे में", command=self.show_about)
    
    def create_toolbar(self):
        """Create toolbar"""
        toolbar = ttk.Frame(self.root)
        toolbar.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)
        
        # File operations
        ttk.Button(toolbar, text="नया", command=self.new_file).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="खोलें", command=self.open_file).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="सेव", command=self.save_file).pack(side=tk.LEFT, padx=2)
        
        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, padx=5, fill=tk.Y)
        
        # Run operations
        ttk.Button(toolbar, text="▶ चलाएं", command=self.run_program).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="REPL", command=self.open_repl).pack(side=tk.LEFT, padx=2)
        
        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, padx=5, fill=tk.Y)
        
        # Syntax highlighting toggle
        self.highlight_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(toolbar, text="सिंटैक्स हाइलाइट", 
                       variable=self.highlight_var,
                       command=self.toggle_highlighting).pack(side=tk.LEFT, padx=2)
    
    def create_content_area(self):
        """Create main content area with editor and output"""
        # Create paned window
        paned = ttk.PanedWindow(self.root, orient=tk.VERTICAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Editor frame
        editor_frame = ttk.LabelFrame(paned, text="संपादक")
        paned.add(editor_frame, weight=3)
        
        # Line numbers
        self.line_numbers = tk.Text(editor_frame, width=4, padx=3, takefocus=0,
                                   border=0, state='disabled', wrap='none')
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)
        
        # Text editor
        self.text_editor = scrolledtext.ScrolledText(
            editor_frame,
            wrap=tk.NONE,
            font=('Consolas', 12),
            undo=True,
            maxundo=50
        )
        self.text_editor.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Syntax highlighter
        self.highlighter = SyntaxHighlighter(self.text_editor)
        
        # Output frame
        output_frame = ttk.LabelFrame(paned, text="आउटपुट")
        paned.add(output_frame, weight=1)
        
        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            height=10,
            font=('Consolas', 10),
            state='disabled'
        )
        self.output_text.pack(fill=tk.BOTH, expand=True)
    
    def create_status_bar(self):
        """Create status bar"""
        self.status_bar = ttk.Frame(self.root)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.status_label = ttk.Label(self.status_bar, text="तैयार")
        self.status_label.pack(side=tk.LEFT, padx=5)
        
        # Line/column indicator
        self.position_label = ttk.Label(self.status_bar, text="पंक्ति: 1, स्तम्भ: 1")
        self.position_label.pack(side=tk.RIGHT, padx=5)
    
    def setup_bindings(self):
        """Setup keyboard bindings"""
        # File operations
        self.root.bind('<Control-n>', lambda e: self.new_file())
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-s>', lambda e: self.save_file())
        
        # Run program
        self.root.bind('<F5>', lambda e: self.run_program())
        
        # Text editor events
        self.text_editor.bind('<KeyRelease>', self.on_text_change)
        self.text_editor.bind('<Button-1>', self.on_cursor_move)
        self.text_editor.bind('<KeyPress>', self.on_cursor_move)
        
        # Window close event
        self.root.protocol("WM_DELETE_WINDOW", self.quit_app)
    
    def on_text_change(self, event=None):
        """Handle text change events"""
        self.modified = True
        self.update_title()
        self.update_line_numbers()
        self.schedule_highlight()
        self.update_position()
    
    def on_cursor_move(self, event=None):
        """Handle cursor movement"""
        self.root.after(10, self.update_position)
    
    def schedule_highlight(self):
        """Schedule syntax highlighting"""
        if self.highlight_timer:
            self.root.after_cancel(self.highlight_timer)
        
        if self.highlight_var.get():
            self.highlight_timer = self.root.after(500, self.apply_highlighting)
    
    def apply_highlighting(self):
        """Apply syntax highlighting"""
        if self.highlight_var.get():
            self.highlighter.highlight()
    
    def update_line_numbers(self):
        """Update line numbers"""
        self.line_numbers.config(state='normal')
        self.line_numbers.delete('1.0', tk.END)
        
        content = self.text_editor.get('1.0', tk.END)
        line_count = content.count('\n')
        
        line_numbers_text = '\n'.join(str(i) for i in range(1, line_count + 1))
        self.line_numbers.insert('1.0', line_numbers_text)
        self.line_numbers.config(state='disabled')
    
    def update_position(self):
        """Update cursor position in status bar"""
        cursor_pos = self.text_editor.index(tk.INSERT)
        line, column = cursor_pos.split('.')
        self.position_label.config(text=f"पंक्ति: {line}, स्तम्भ: {int(column) + 1}")
    
    def update_title(self):
        """Update window title"""
        title = "संस्कृत प्रोग्रामिंग भाषा - संपादक"
        if self.current_file:
            title += f" - {self.current_file}"
        if self.modified:
            title += " *"
        self.root.title(title)
    
    def new_file(self):
        """Create new file"""
        if self.check_unsaved_changes():
            self.text_editor.delete('1.0', tk.END)
            self.current_file = None
            self.modified = False
            self.update_title()
            self.clear_output()
            self.status_label.config(text="नई फ़ाइल बनाई गई")
    
    def open_file(self):
        """Open existing file"""
        if self.check_unsaved_changes():
            file_path = filedialog.askopenfilename(
                title="फ़ाइल खोलें",
                filetypes=[
                    ("Sanskrit files", "*.sans"),
                    ("Text files", "*.txt"),
                    ("All files", "*.*")
                ]
            )
            
            if file_path:
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                    
                    self.text_editor.delete('1.0', tk.END)
                    self.text_editor.insert('1.0', content)
                    
                    self.current_file = file_path
                    self.modified = False
                    self.update_title()
                    self.apply_highlighting()
                    self.status_label.config(text=f"फ़ाइल खोली गई: {file_path}")
                    
                except Exception as e:
                    messagebox.showerror("त्रुटि", f"फ़ाइल खोलने में त्रुटि: {e}")
    
    def save_file(self):
        """Save current file"""
        if self.current_file:
            self.save_to_file(self.current_file)
        else:
            self.save_as_file()
    
    def save_as_file(self):
        """Save file with new name"""
        file_path = filedialog.asksaveasfilename(
            title="फ़ाइल सेव करें",
            defaultextension=".sans",
            filetypes=[
                ("Sanskrit files", "*.sans"),
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            self.save_to_file(file_path)
    
    def save_to_file(self, file_path):
        """Save content to file"""
        try:
            content = self.text_editor.get('1.0', tk.END + '-1c')
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            
            self.current_file = file_path
            self.modified = False
            self.update_title()
            self.status_label.config(text=f"फ़ाइल सेव की गई: {file_path}")
            
        except Exception as e:
            messagebox.showerror("त्रुटि", f"फ़ाइल सेव करने में त्रुटि: {e}")
    
    def check_unsaved_changes(self):
        """Check for unsaved changes"""
        if self.modified:
            result = messagebox.askyesnocancel(
                "असेव परिवर्तन",
                "फ़ाइल में असेव परिवर्तन हैं। क्या आप सेव करना चाहते हैं?"
            )
            
            if result is True:  # Yes
                self.save_file()
                return not self.modified
            elif result is False:  # No
                return True
            else:  # Cancel
                return False
        
        return True
    
    def run_program(self):
        """Run the current program"""
        content = self.text_editor.get('1.0', tk.END + '-1c')
        
        if not content.strip():
            messagebox.showwarning("चेतावनी", "कोई कोड नहीं मिला")
            return
        
        # Clear output
        self.clear_output()
        
        # Redirect output
        import sys
        from io import StringIO
        
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        
        sys.stdout = StringIO()
        sys.stderr = StringIO()
        
        try:
            self.interpreter.execute(content)
            output = sys.stdout.getvalue()
            error = sys.stderr.getvalue()
            
            if output:
                self.append_output(output, 'output')
            if error:
                self.append_output(error, 'error')
            
            if not output and not error:
                self.append_output("प्रोग्राम सफलतापूर्वक चला", 'success')
            
            self.status_label.config(text="प्रोग्राम चलाया गया")
            
        except SanskritError as e:
            self.append_output(f"संस्कृत त्रुटि: {e}", 'error')
            self.status_label.config(text="प्रोग्राम में त्रुटि")
            
        except Exception as e:
            self.append_output(f"त्रुटि: {e}", 'error')
            self.status_label.config(text="प्रोग्राम में त्रुटि")
            
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr
    
    def clear_output(self):
        """Clear output text"""
        self.output_text.config(state='normal')
        self.output_text.delete('1.0', tk.END)
        self.output_text.config(state='disabled')
    
    def append_output(self, text, text_type='normal'):
        """Append text to output"""
        self.output_text.config(state='normal')
        
        # Configure tags for different text types
        if text_type == 'error':
            self.output_text.tag_configure('error', foreground='red')
            self.output_text.insert(tk.END, text, 'error')
        elif text_type == 'success':
            self.output_text.tag_configure('success', foreground='green')
            self.output_text.insert(tk.END, text, 'success')
        else:
            self.output_text.insert(tk.END, text)
        
        self.output_text.insert(tk.END, '\n')
        self.output_text.see(tk.END)
        self.output_text.config(state='disabled')
    
    def open_repl(self):
        """Open REPL in new window"""
        repl_window = tk.Toplevel(self.root)
        repl_window.title("संस्कृत REPL")
        repl_window.geometry("600x400")
        
        # REPL text area
        repl_text = scrolledtext.ScrolledText(
            repl_window,
            font=('Consolas', 11),
            bg='black',
            fg='white'
        )
        repl_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Input frame
        input_frame = ttk.Frame(repl_window)
        input_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(input_frame, text=">>> ").pack(side=tk.LEFT)
        
        input_entry = ttk.Entry(input_frame)
        input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        def execute_repl_command(event=None):
            command = input_entry.get()
            if command.strip():
                repl_text.insert(tk.END, f">>> {command}\n")
                
                try:
                    # Redirect output for REPL
                    import sys
                    from io import StringIO
                    
                    old_stdout = sys.stdout
                    sys.stdout = StringIO()
                    
                    self.interpreter.execute(command)
                    output = sys.stdout.getvalue()
                    
                    if output:
                        repl_text.insert(tk.END, output)
                    
                    sys.stdout = old_stdout
                    
                except Exception as e:
                    repl_text.insert(tk.END, f"त्रुटि: {e}\n")
                
                input_entry.delete(0, tk.END)
                repl_text.see(tk.END)
        
        input_entry.bind('<Return>', execute_repl_command)
        ttk.Button(input_frame, text="चलाएं", command=execute_repl_command).pack(side=tk.RIGHT)
        
        # Initial message
        repl_text.insert(tk.END, "संस्कृत REPL v1.0.0\nकमांड टाइप करें और Enter दबाएं\n\n")
        input_entry.focus()
    
    def toggle_highlighting(self):
        """Toggle syntax highlighting"""
        if self.highlight_var.get():
            self.apply_highlighting()
            self.status_label.config(text="सिंटैक्स हाइलाइटिंग चालू")
        else:
            # Clear all highlighting
            for tag in ['keyword', 'string', 'comment', 'number', 'operator', 'function']:
                self.text_editor.tag_remove(tag, '1.0', tk.END)
            self.status_label.config(text="सिंटैक्स हाइलाइटिंग बंद")
    
    def undo(self):
        """Undo last action"""
        try:
            self.text_editor.edit_undo()
        except tk.TclError:
            pass
    
    def redo(self):
        """Redo last action"""
        try:
            self.text_editor.edit_redo()
        except tk.TclError:
            pass
    
    def copy(self):
        """Copy selected text"""
        try:
            self.text_editor.clipboard_clear()
            self.text_editor.clipboard_append(self.text_editor.selection_get())
        except tk.TclError:
            pass
    
    def cut(self):
        """Cut selected text"""
        try:
            self.copy()
            self.text_editor.delete(tk.SEL_FIRST, tk.SEL_LAST)
        except tk.TclError:
            pass
    
    def paste(self):
        """Paste text from clipboard"""
        try:
            self.text_editor.insert(tk.INSERT, self.text_editor.clipboard_get())
        except tk.TclError:
            pass
    
    def select_all(self):
        """Select all text"""
        self.text_editor.tag_add(tk.SEL, '1.0', tk.END)
        self.text_editor.mark_set(tk.INSERT, '1.0')
        self.text_editor.see(tk.INSERT)
    
    def find(self):
        """Open find dialog"""
        find_window = tk.Toplevel(self.root)
        find_window.title("खोजें")
        find_window.geometry("300x100")
        
        ttk.Label(find_window, text="खोजें:").pack(pady=5)
        
        search_entry = ttk.Entry(find_window, width=30)
        search_entry.pack(pady=5)
        search_entry.focus()
        
        def find_text():
            search_term = search_entry.get()
            if search_term:
                # Remove previous search highlights
                self.text_editor.tag_remove('search', '1.0', tk.END)
                
                # Find and highlight all occurrences
                start = '1.0'
                while True:
                    pos = self.text_editor.search(search_term, start, tk.END)
                    if not pos:
                        break
                    
                    end = f"{pos}+{len(search_term)}c"
                    self.text_editor.tag_add('search', pos, end)
                    start = end
                
                # Configure search highlight
                self.text_editor.tag_configure('search', background='yellow')
        
        ttk.Button(find_window, text="खोजें", command=find_text).pack(pady=5)
    
    def show_syntax_guide(self):
        """Show syntax guide"""
        guide_text = """
संस्कृत प्रोग्रामिंग भाषा - सिंटैक्स गाइड

चर परिभाषा:
    धारणा नाम = मान

संख्याएं:
    धारणा संख्या = १२३
    धारणा दशमलव = ३.१४

स्ट्रिंग:
    धारणा शब्द = "नमस्ते"

बूलियन:
    धारणा सत्य_मान = सत्य
    धारणा असत्य_मान = असत्य

फ़ंक्शन:
    कार्य नाम(पैरामीटर) {
        # कोड यहाँ
        वापसी परिणाम
    }

शर्त:
    यदि शर्त {
        # कोड यहाँ
    } अथवा {
        # अन्य कोड
    }

लूप:
    यावत् शर्त {
        # कोड यहाँ
    }

प्रिंट:
    मुद्रण("संदेश")

टिप्पणी:
    # यह एक टिप्पणी है
        """
        
        messagebox.showinfo("सिंटैक्स गाइड", guide_text)
    
    def show_examples(self):
        """Show examples"""
        messagebox.showinfo("उदाहरण", "उदाहरण फ़ाइलें examples/ फ़ोल्डर में देखें")
    
    def show_about(self):
        """Show about dialog"""
        about_text = """
संस्कृत प्रोग्रामिंग भाषा
संस्करण 1.0.0

संस्कृत व्याकरण से प्रेरित प्रोग्रामिंग भाषा

विशेषताएं:
• संस्कृत-आधारित सिंटैक्स
• मजबूत प्रकार अनुमान
• अंतर्निहित संपादक और REPL
• संस्कृत-नामित मानक पुस्तकालय

Python में निर्मित
        """
        
        messagebox.showinfo("के बारे में", about_text)
    
    def quit_app(self):
        """Quit application"""
        if self.check_unsaved_changes():
            self.root.quit()
    
    def run(self):
        """Start the editor"""
        self.root.mainloop()
