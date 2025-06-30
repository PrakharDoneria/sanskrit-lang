"""
Sanskrit Language Type System
Type definitions inspired by Sanskrit word classifications
"""

from enum import Enum
from typing import Any, Optional, Union
from abc import ABC, abstractmethod

class VarnaType(Enum):
    """
    Varna (वर्ण) - Basic type categories inspired by Sanskrit grammar
    """
    SANKHYA = "SANKHYA"      # Numbers (संख्या)
    SHABDA = "SHABDA"        # Strings/Words (शब्द)  
    SATYA_ASATYA = "SATYA_ASATYA"  # Boolean (सत्य-असत्य)
    SHUNYA = "SHUNYA"        # Null/Empty (शून्य)
    SAMUHA = "SAMUHA"        # Collections/Arrays (समूह)
    KAARYA = "KAARYA"        # Functions (कार्य)
    VARGA = "VARGA"          # Classes/Objects (वर्ग)

class SanskritType(ABC):
    """Base class for Sanskrit language types"""
    
    def __init__(self, varna: VarnaType, name: str):
        self.varna = varna
        self.name = name
    
    @abstractmethod
    def is_compatible(self, other: 'SanskritType') -> bool:
        """Check if this type is compatible with another"""
        pass
    
    @abstractmethod
    def can_cast_to(self, other: 'SanskritType') -> bool:
        """Check if this type can be cast to another"""
        pass
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f"SanskritType({self.varna}, {self.name})"

class SankhyaType(SanskritType):
    """Number type (संख्या)"""
    
    def __init__(self, is_decimal: bool = False):
        name = "दशमलव_संख्या" if is_decimal else "पूर्ण_संख्या"
        super().__init__(VarnaType.SANKHYA, name)
        self.is_decimal = is_decimal
    
    def is_compatible(self, other: SanskritType) -> bool:
        """Numbers are compatible with other numbers"""
        return isinstance(other, SankhyaType)
    
    def can_cast_to(self, other: SanskritType) -> bool:
        """Numbers can be cast to strings and booleans"""
        return isinstance(other, (SankhyaType, ShabdaType, SatyaAsatyaType))

class ShabdaType(SanskritType):
    """String type (शब्द)"""
    
    def __init__(self):
        super().__init__(VarnaType.SHABDA, "शब्द")
    
    def is_compatible(self, other: SanskritType) -> bool:
        """Strings are only compatible with other strings"""
        return isinstance(other, ShabdaType)
    
    def can_cast_to(self, other: SanskritType) -> bool:
        """Strings can be cast to numbers and booleans"""
        return isinstance(other, (ShabdaType, SankhyaType, SatyaAsatyaType))

class SatyaAsatyaType(SanskritType):
    """Boolean type (सत्य-असत्य)"""
    
    def __init__(self):
        super().__init__(VarnaType.SATYA_ASATYA, "सत्य_असत्य")
    
    def is_compatible(self, other: SanskritType) -> bool:
        """Booleans are compatible with other booleans"""
        return isinstance(other, SatyaAsatyaType)
    
    def can_cast_to(self, other: SanskritType) -> bool:
        """Booleans can be cast to numbers and strings"""
        return isinstance(other, (SatyaAsatyaType, SankhyaType, ShabdaType))

class ShunyaType(SanskritType):
    """Null/None type (शून्य)"""
    
    def __init__(self):
        super().__init__(VarnaType.SHUNYA, "शून्य")
    
    def is_compatible(self, other: SanskritType) -> bool:
        """Null is compatible with any type"""
        return True
    
    def can_cast_to(self, other: SanskritType) -> bool:
        """Null can be cast to boolean and string"""
        return isinstance(other, (SatyaAsatyaType, ShabdaType))

class SamuhaType(SanskritType):
    """Collection type (समूह)"""
    
    def __init__(self, element_type: Optional[SanskritType] = None):
        super().__init__(VarnaType.SAMUHA, "समूह")
        self.element_type = element_type
    
    def is_compatible(self, other: SanskritType) -> bool:
        """Collections are compatible with other collections of same element type"""
        if not isinstance(other, SamuhaType):
            return False
        
        if self.element_type is None or other.element_type is None:
            return True  # Untyped collections are compatible
        
        return self.element_type.is_compatible(other.element_type)
    
    def can_cast_to(self, other: SanskritType) -> bool:
        """Collections can be cast to strings and booleans"""
        return isinstance(other, (ShabdaType, SatyaAsatyaType))

class KaaryaType(SanskritType):
    """Function type (कार्य)"""
    
    def __init__(self, param_types: list[SanskritType], return_type: Optional[SanskritType] = None):
        super().__init__(VarnaType.KAARYA, "कार्य")
        self.param_types = param_types
        self.return_type = return_type
    
    def is_compatible(self, other: SanskritType) -> bool:
        """Functions are compatible if they have same signature"""
        if not isinstance(other, KaaryaType):
            return False
        
        if len(self.param_types) != len(other.param_types):
            return False
        
        for p1, p2 in zip(self.param_types, other.param_types):
            if not p1.is_compatible(p2):
                return False
        
        if self.return_type and other.return_type:
            return self.return_type.is_compatible(other.return_type)
        
        return True
    
    def can_cast_to(self, other: SanskritType) -> bool:
        """Functions can only be cast to strings and booleans"""
        return isinstance(other, (ShabdaType, SatyaAsatyaType))

class VargaType(SanskritType):
    """Class type (वर्ग)"""
    
    def __init__(self, class_name: str, fields: dict[str, SanskritType] = None):
        super().__init__(VarnaType.VARGA, class_name)
        self.class_name = class_name
        self.fields = fields or {}
    
    def is_compatible(self, other: SanskritType) -> bool:
        """Classes are compatible with same class or parent classes"""
        if not isinstance(other, VargaType):
            return False
        return self.class_name == other.class_name
    
    def can_cast_to(self, other: SanskritType) -> bool:
        """Classes can be cast to strings and booleans"""
        return isinstance(other, (ShabdaType, SatyaAsatyaType))

class SanskritValue:
    """Wrapper for values with type information"""
    
    def __init__(self, value: Any, type_info: SanskritType):
        self.value = value
        self.type_info = type_info
    
    def __str__(self) -> str:
        return str(self.value)
    
    def __repr__(self) -> str:
        return f"SanskritValue({self.value}, {self.type_info})"

class TypeInferrer:
    """Type inference engine for Sanskrit language"""
    
    @staticmethod
    def infer_type(value: Any) -> SanskritType:
        """Infer type from a Python value"""
        if isinstance(value, int):
            return SankhyaType(is_decimal=False)
        elif isinstance(value, float):
            return SankhyaType(is_decimal=True)
        elif isinstance(value, str):
            return ShabdaType()
        elif isinstance(value, bool):
            return SatyaAsatyaType()
        elif value is None:
            return ShunyaType()
        elif isinstance(value, (list, tuple)):
            element_type = None
            if value:
                element_type = TypeInferrer.infer_type(value[0])
            return SamuhaType(element_type)
        else:
            return VargaType("अज्ञात")
    
    @staticmethod
    def check_compatibility(left_type: SanskritType, right_type: SanskritType, 
                          operation: str) -> bool:
        """Check if types are compatible for given operation"""
        
        # Arithmetic operations
        if operation in ['+', '-', '*', '/', '%']:
            if operation == '+':
                # Addition allows numbers + numbers or strings + anything
                return (isinstance(left_type, SankhyaType) and isinstance(right_type, SankhyaType)) or \
                       isinstance(left_type, ShabdaType) or isinstance(right_type, ShabdaType)
            else:
                # Other arithmetic requires numbers
                return isinstance(left_type, SankhyaType) and isinstance(right_type, SankhyaType)
        
        # Comparison operations
        elif operation in ['==', '!=']:
            return True  # Any types can be compared for equality
        
        elif operation in ['<', '>', '<=', '>=']:
            # Ordering requires compatible types
            return left_type.is_compatible(right_type)
        
        # Logical operations
        elif operation in ['च', 'वा']:  # and, or
            return True  # Any type can be used in logical context
        
        return False

def create_typed_value(value: Any) -> SanskritValue:
    """Create a typed value from a Python value"""
    return SanskritValue(value, TypeInferrer.infer_type(value))
