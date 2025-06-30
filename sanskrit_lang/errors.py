"""
Sanskrit Language Error System
Error definitions and Sanskrit-style error messages
"""

class SanskritError(Exception):
    """Base class for all Sanskrit language errors"""
    
    def __init__(self, message: str, line: int = 0, column: int = 0):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(self.get_formatted_message())
    
    def get_formatted_message(self) -> str:
        """Get formatted error message"""
        if self.line > 0:
            return f"पंक्ति {self.line}, स्तम्भ {self.column}: {self.message}"
        return self.message

class SanskritSyntaxError(SanskritError):
    """Syntax error in Sanskrit code"""
    
    def __init__(self, message: str, line: int = 0, column: int = 0):
        formatted_message = f"व्याकरण त्रुटि: {message}"
        super().__init__(formatted_message, line, column)

class SanskritRuntimeError(SanskritError):
    """Runtime error during execution"""
    
    def __init__(self, message: str, line: int = 0, column: int = 0):
        formatted_message = f"रनटाइम त्रुटि: {message}"
        super().__init__(formatted_message, line, column)

class SanskritTypeError(SanskritError):
    """Type mismatch error"""
    
    def __init__(self, message: str, line: int = 0, column: int = 0):
        formatted_message = f"प्रकार त्रुटि: {message}"
        super().__init__(formatted_message, line, column)

class SanskritNameError(SanskritError):
    """Name not found error"""
    
    def __init__(self, name: str, line: int = 0, column: int = 0):
        message = f"नाम त्रुटि: '{name}' परिभाषित नहीं है"
        super().__init__(message, line, column)

class SanskritAttributeError(SanskritError):
    """Attribute access error"""
    
    def __init__(self, obj_type: str, attr: str, line: int = 0, column: int = 0):
        message = f"गुण त्रुटि: '{obj_type}' में '{attr}' गुण नहीं है"
        super().__init__(message, line, column)

class SanskritIndexError(SanskritError):
    """Index out of bounds error"""
    
    def __init__(self, index: int, size: int, line: int = 0, column: int = 0):
        message = f"सूचकांक त्रुटि: सूचकांक {index} सीमा से बाहर (आकार: {size})"
        super().__init__(message, line, column)

class SanskritKeyError(SanskritError):
    """Key not found error"""
    
    def __init__(self, key: str, line: int = 0, column: int = 0):
        message = f"कुंजी त्रुटि: कुंजी '{key}' नहीं मिली"
        super().__init__(message, line, column)

class SanskritValueError(SanskritError):
    """Invalid value error"""
    
    def __init__(self, message: str, line: int = 0, column: int = 0):
        formatted_message = f"मान त्रुटि: {message}"
        super().__init__(formatted_message, line, column)

class SanskritZeroDivisionError(SanskritError):
    """Division by zero error"""
    
    def __init__(self, line: int = 0, column: int = 0):
        message = "गणित त्रुटि: शून्य से भाग संभव नहीं"
        super().__init__(message, line, column)

class SanskritImportError(SanskritError):
    """Module import error"""
    
    def __init__(self, module: str, line: int = 0, column: int = 0):
        message = f"आयात त्रुटि: मॉड्यूल '{module}' नहीं मिला"
        super().__init__(message, line, column)

class SanskritReturnException(Exception):
    """Exception used for return statements (not a real error)"""
    
    def __init__(self, value):
        self.value = value
        super().__init__()

class SanskritBreakException(Exception):
    """Exception used for break statements"""
    
    def __init__(self):
        super().__init__()

class SanskritContinueException(Exception):
    """Exception used for continue statements"""
    
    def __init__(self):
        super().__init__()

class ErrorMessages:
    """Sanskrit error message constants"""
    
    # Syntax errors
    UNEXPECTED_TOKEN = "अप्रत्याशित टोकन"
    EXPECTED_TOKEN = "अपेक्षित टोकन"
    UNTERMINATED_STRING = "अपूर्ण स्ट्रिंग"
    INVALID_NUMBER = "अवैध संख्या"
    MISSING_CLOSING_BRACE = "समापन कोष्ठक गुम"
    MISSING_OPENING_BRACE = "प्रारंभिक कोष्ठक गुम"
    
    # Runtime errors
    UNDEFINED_VARIABLE = "अपरिभाषित चर"
    FUNCTION_NOT_CALLABLE = "फ़ंक्शन कॉल योग्य नहीं"
    WRONG_ARGUMENT_COUNT = "गलत तर्क संख्या"
    CANNOT_ASSIGN = "असाइनमेंट संभव नहीं"
    
    # Type errors
    INCOMPATIBLE_TYPES = "असंगत प्रकार"
    CANNOT_CONVERT = "परिवर्तन संभव नहीं"
    INVALID_OPERATION = "अवैध ऑपरेशन"
    
    # Math errors
    DIVISION_BY_ZERO = "शून्य से भाग"
    NEGATIVE_SQRT = "ऋणात्मक संख्या का वर्गमूल"
    INVALID_LOGARITHM = "अवैध लघुगणक"
    
    # Collection errors
    INDEX_OUT_OF_BOUNDS = "सूचकांक सीमा से बाहर"
    EMPTY_COLLECTION = "खाली संग्रह"
    KEY_NOT_FOUND = "कुंजी नहीं मिली"
    
    # File errors
    FILE_NOT_FOUND = "फ़ाइल नहीं मिली"
    PERMISSION_DENIED = "अनुमति नकारी"
    FILE_READ_ERROR = "फ़ाइल पढ़ने में त्रुटि"
    FILE_WRITE_ERROR = "फ़ाइल लिखने में त्रुटि"

def format_error_context(source_line: str, column: int, length: int = 1) -> str:
    """Format error context with pointer"""
    if not source_line.strip():
        return ""
    
    pointer = " " * (column - 1) + "^" * length
    return f"\n{source_line}\n{pointer}"

def create_syntax_error(message: str, line: int, column: int, 
                       source_line: str = "") -> SanskritSyntaxError:
    """Create a formatted syntax error"""
    error = SanskritSyntaxError(message, line, column)
    if source_line:
        context = format_error_context(source_line, column)
        error.message += context
    return error

def create_runtime_error(message: str, line: int = 0, column: int = 0) -> SanskritRuntimeError:
    """Create a runtime error"""
    return SanskritRuntimeError(message, line, column)

def create_type_error(expected: str, got: str, line: int = 0, column: int = 0) -> SanskritTypeError:
    """Create a type error"""
    message = f"अपेक्षित प्रकार '{expected}', प्राप्त '{got}'"
    return SanskritTypeError(message, line, column)

def create_name_error(name: str, line: int = 0, column: int = 0) -> SanskritNameError:
    """Create a name error"""
    return SanskritNameError(name, line, column)

# Common error patterns and their Sanskrit equivalents
ERROR_TRANSLATIONS = {
    "SyntaxError": "व्याकरण त्रुटि",
    "RuntimeError": "रनटाइम त्रुटि",
    "TypeError": "प्रकार त्रुटि",
    "NameError": "नाम त्रुटि",
    "AttributeError": "गुण त्रुटि",
    "IndexError": "सूचकांक त्रुटि",
    "KeyError": "कुंजी त्रुटि",
    "ValueError": "मान त्रुटि",
    "ZeroDivisionError": "शून्य भाग त्रुटि",
    "ImportError": "आयात त्रुटि",
    "FileNotFoundError": "फ़ाइल अनुपस्थित त्रुटि",
    "PermissionError": "अनुमति त्रुटि",
}

def translate_python_error(python_error: Exception) -> str:
    """Translate Python error to Sanskrit"""
    error_type = type(python_error).__name__
    
    if error_type in ERROR_TRANSLATIONS:
        sanskrit_type = ERROR_TRANSLATIONS[error_type]
        return f"{sanskrit_type}: {str(python_error)}"
    
    return f"अज्ञात त्रुटि: {str(python_error)}"

class ErrorReporter:
    """Error reporting and formatting utility"""
    
    def __init__(self):
        self.errors: list[SanskritError] = []
    
    def report_error(self, error: SanskritError):
        """Report an error"""
        self.errors.append(error)
        print(f"त्रुटि: {error}")
    
    def has_errors(self) -> bool:
        """Check if there are errors"""
        return len(self.errors) > 0
    
    def clear_errors(self):
        """Clear all errors"""
        self.errors.clear()
    
    def get_error_summary(self) -> str:
        """Get summary of all errors"""
        if not self.errors:
            return "कोई त्रुटि नहीं"
        
        summary = f"कुल त्रुटियां: {len(self.errors)}\n"
        for i, error in enumerate(self.errors, 1):
            summary += f"{i}. {error.get_formatted_message()}\n"
        
        return summary

# Global error reporter instance
error_reporter = ErrorReporter()
