"""
Sanskrit Standard Library
Sanskrit-named modules for core functionality
"""

from typing import Dict, Any, Callable
from .ganita import GanitaModule
from .shabda import ShabdaModule  
from .pravesh import PraveshModule

def get_builtin_functions() -> Dict[str, Callable]:
    """Get all built-in functions"""
    builtins = {}
    
    # Add basic print function
    def mudran(*args):
        """Print function (मुद्रण)"""
        print(*[str(arg) for arg in args])
    
    def prakar(obj):
        """Type function (प्रकार)"""
        if isinstance(obj, int):
            return "पूर्ण_संख्या"
        elif isinstance(obj, float):
            return "दशमलव_संख्या"
        elif isinstance(obj, str):
            return "शब्द"
        elif isinstance(obj, bool):
            return "सत्य_असत्य"
        elif obj is None:
            return "शून्य"
        elif isinstance(obj, list):
            return "सूची"
        elif isinstance(obj, dict):
            return "शब्दकोश"
        else:
            return "अज्ञात"
    
    def lambai(obj):
        """Length function (लम्बाई)"""
        return len(obj)
    
    def sundar(obj):
        """String conversion (सुन्दर)"""
        return str(obj)
    
    def sankhya(obj):
        """Number conversion (संख्या)"""
        if isinstance(obj, str):
            try:
                if '.' in obj:
                    return float(obj)
                else:
                    return int(obj)
            except ValueError:
                raise ValueError(f"'{obj}' को संख्या में परिवर्तित नहीं किया जा सकता")
        return float(obj) if isinstance(obj, int) else obj
    
    builtins.update({
        'मुद्रण': mudran,      # print
        'प्रकार': prakar,       # type
        'लम्बाई': lambai,       # len
        'सुन्दर': sundar,       # str
        'संख्या': sankhya,      # number conversion
    })
    
    return builtins

def load_module(name: str) -> Any:
    """Load a standard library module"""
    modules = {
        'गणित': GanitaModule(),
        'शब्द': ShabdaModule(),
        'प्रवेश': PraveshModule(),
    }
    
    if name in modules:
        return modules[name]
    
    raise ImportError(f"मॉड्यूल '{name}' नहीं मिला")
