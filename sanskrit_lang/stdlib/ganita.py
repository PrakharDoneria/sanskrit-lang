"""
Ganita Module (गणित)
Mathematics and numerical operations
"""

import math
import random

class GanitaModule:
    """Mathematical functions module"""
    
    def __init__(self):
        self.pi = math.pi
        self.e = math.e
    
    def varg(self, x):
        """Square (वर्ग)"""
        return x * x
    
    def vargmool(self, x):
        """Square root (वर्गमूल)"""
        if x < 0:
            raise ValueError("ऋणात्मक संख्या का वर्गमूल संभव नहीं")
        return math.sqrt(x)
    
    def ghaata(self, base, exponent):
        """Power (घात)"""
        return base ** exponent
    
    def mutlak(self, x):
        """Absolute value (मुत्लक)"""
        return abs(x)
    
    def purna(self, x):
        """Floor (पूर्णांक)"""
        return math.floor(x)
    
    def aadhaar(self, x):
        """Ceiling (आधार)"""
        return math.ceil(x)
    
    def yuga(self, x):
        """Round (युग्म)"""
        return round(x)
    
    def adhikam(self, *args):
        """Maximum (अधिकम्)"""
        return max(args)
    
    def nyunam(self, *args):
        """Minimum (न्यूनम्)"""
        return min(args)
    
    def yoga(self, a, b):
        """Addition (योग)"""
        return a + b
    
    def vyavakalana(self, a, b):
        """Subtraction (व्यवकलन)"""
        return a - b
    
    def guna(self, a, b):
        """Multiplication (गुणा)"""
        return a * b
    
    def bhaga(self, a, b):
        """Division (भाग)"""
        if b == 0:
            raise ZeroDivisionError("शून्य से भाग संभव नहीं")
        return a / b
    
    def shesh(self, a, b):
        """Modulo (शेष)"""
        return a % b
    
    # Trigonometric functions
    def sin(self, x):
        """Sine (ज्या)"""
        return math.sin(x)
    
    def cos(self, x):
        """Cosine (कोज्या)"""
        return math.cos(x)
    
    def tan(self, x):
        """Tangent (स्पर्शज्या)"""
        return math.tan(x)
    
    def asin(self, x):
        """Arcsine (आर्क ज्या)"""
        return math.asin(x)
    
    def acos(self, x):
        """Arccosine (आर्क कोज्या)"""
        return math.acos(x)
    
    def atan(self, x):
        """Arctangent (आर्क स्पर्शज्या)"""
        return math.atan(x)
    
    # Logarithmic functions
    def log(self, x, base=math.e):
        """Logarithm (लघुगणक)"""
        if x <= 0:
            raise ValueError("धनात्मक संख्या की ही लघुगणक संभव है")
        return math.log(x, base)
    
    def log10(self, x):
        """Base-10 logarithm (दशाधार लघुगणक)"""
        return math.log10(x)
    
    def exp(self, x):
        """Exponential (घातांक)"""
        return math.exp(x)
    
    # Random number functions
    def ydrsh(self):
        """Random float between 0 and 1 (यादृश्)"""
        return random.random()
    
    def ydrsh_anta(self, start, end):
        """Random integer in range (यादृश् अन्त)"""
        return random.randint(start, end)
    
    def ydrsh_chayan(self, sequence):
        """Random choice from sequence (यादृश् चयन)"""
        return random.choice(sequence)
    
    # Utility functions
    def factorial(self, n):
        """Factorial (क्रमगुणित)"""
        if n < 0:
            raise ValueError("ऋणात्मक संख्या का क्रमगुणित संभव नहीं")
        return math.factorial(n)
    
    def gcd(self, a, b):
        """Greatest Common Divisor (महत्तम समापवर्तक)"""
        return math.gcd(a, b)
    
    def lcm(self, a, b):
        """Least Common Multiple (लघुत्तम समापवर्त्य)"""
        return abs(a * b) // math.gcd(a, b)
    
    def is_prime(self, n):
        """Check if number is prime (अभाज्य जांच)"""
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    def primes_up_to(self, n):
        """Generate primes up to n (अभाज्य सूची)"""
        if n < 2:
            return []
        
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        
        return [i for i in range(2, n + 1) if sieve[i]]
