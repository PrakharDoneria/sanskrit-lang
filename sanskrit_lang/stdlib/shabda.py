"""
Shabda Module (शब्द)
String manipulation and text processing functions
"""

import re

class ShabdaModule:
    """String manipulation module"""
    
    def __init__(self):
        pass
    
    def lambai(self, text):
        """Length of string (लम्बाई)"""
        return len(text)
    
    def uchcha(self, text):
        """Convert to uppercase (उच्च)"""
        return text.upper()
    
    def laghu(self, text):
        """Convert to lowercase (लघु)"""
        return text.lower()
    
    def pratham_uchcha(self, text):
        """Capitalize first letter (प्रथम उच्च)"""
        return text.capitalize()
    
    def shabad_uchcha(self, text):
        """Title case (शब्द उच्च)"""
        return text.title()
    
    def safai(self, text):
        """Remove leading/trailing whitespace (सफाई)"""
        return text.strip()
    
    def vaam_safai(self, text):
        """Remove leading whitespace (वाम सफाई)"""
        return text.lstrip()
    
    def daksh_safai(self, text):
        """Remove trailing whitespace (दक्ष सफाई)"""
        return text.rstrip()
    
    def vibhajan(self, text, separator=" "):
        """Split string (विभाजन)"""
        return text.split(separator)
    
    def sandharan(self, sequence, separator=""):
        """Join strings (संधारण)"""
        return separator.join(str(item) for item in sequence)
    
    def sthaan_badal(self, text, old, new, count=-1):
        """Replace text (स्थान बदल)"""
        if count == -1:
            return text.replace(old, new)
        return text.replace(old, new, count)
    
    def khoj(self, text, substring):
        """Find substring (खोज)"""
        return text.find(substring)
    
    def ant_khoj(self, text, substring):
        """Find last occurrence (अन्त खोज)"""
        return text.rfind(substring)
    
    def sankhya_ginti(self, text, substring):
        """Count occurrences (संख्या गिनती)"""
        return text.count(substring)
    
    def aarambh_jaanch(self, text, prefix):
        """Check if starts with (आरम्भ जांच)"""
        return text.startswith(prefix)
    
    def ant_jaanch(self, text, suffix):
        """Check if ends with (अन्त जांच)"""
        return text.endswith(suffix)
    
    def samelan(self, text, substring):
        """Check if contains (समेलन)"""
        return substring in text
    
    def akshar_jaanch(self, text):
        """Check if all characters are alphabetic (अक्षर जांच)"""
        return text.isalpha()
    
    def anka_jaanch(self, text):
        """Check if all characters are digits (अंक जांच)"""
        return text.isdigit()
    
    def akshar_anka_jaanch(self, text):
        """Check if all characters are alphanumeric (अक्षर अंक जांच)"""
        return text.isalnum()
    
    def khali_sthaan_jaanch(self, text):
        """Check if all characters are whitespace (खाली स्थान जांच)"""
        return text.isspace()
    
    def khand(self, text, start, end=None):
        """Slice string (खण्ड)"""
        if end is None:
            return text[start:]
        return text[start:end]
    
    def poorti(self, text, width, fill_char=" ", align="left"):
        """Pad string (पूर्ति)"""
        if align == "left":
            return text.ljust(width, fill_char)
        elif align == "right":
            return text.rjust(width, fill_char)
        else:
            return text.center(width, fill_char)
    
    def ulta(self, text):
        """Reverse string (उल्टा)"""
        return text[::-1]
    
    def krami_sthaan(self, text, index):
        """Get character at position (क्रमी स्थान)"""
        if 0 <= index < len(text):
            return text[index]
        raise IndexError("स्थान सीमा से बाहर")
    
    # Regular expression functions
    def niyam_khoj(self, pattern, text):
        """Find pattern using regex (नियम खोज)"""
        match = re.search(pattern, text)
        return match.group() if match else None
    
    def niyam_sabhi_khoj(self, pattern, text):
        """Find all pattern matches (नियम सभी खोज)"""
        return re.findall(pattern, text)
    
    def niyam_badal(self, pattern, replacement, text):
        """Replace using regex (नियम बदल)"""
        return re.sub(pattern, replacement, text)
    
    def niyam_vibhajan(self, pattern, text):
        """Split using regex (नियम विभाजन)"""
        return re.split(pattern, text)
    
    # Text analysis functions
    def shabd_ginti(self, text):
        """Count words (शब्द गिनती)"""
        return len(text.split())
    
    def vakya_ginti(self, text):
        """Count sentences (वाक्य गिनती)"""
        sentences = re.split(r'[.!?]+', text)
        return len([s for s in sentences if s.strip()])
    
    def pankti_ginti(self, text):
        """Count lines (पंक्ति गिनती)"""
        return len(text.splitlines())
    
    def swar_ginti(self, text):
        """Count vowels (स्वर गिनती)"""
        vowels = "aeiouAEIOU"
        return sum(1 for char in text if char in vowels)
    
    def vyanjan_ginti(self, text):
        """Count consonants (व्यञ्जन गिनती)"""
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        return sum(1 for char in text if char in consonants)
    
    def vishesh_akshar_ginti(self, text):
        """Count special characters (विशेष अक्षर गिनती)"""
        return sum(1 for char in text if not char.isalnum() and not char.isspace())
    
    def sadharan_banayen(self, text):
        """Normalize text (साधारण बनायें)"""
        # Remove extra whitespace and normalize
        return ' '.join(text.split())
    
    def ascii_maan(self, char):
        """Get ASCII value (ASCII मान)"""
        return ord(char)
    
    def char_se_ascii(self, ascii_val):
        """Get character from ASCII (अक्षर से ASCII)"""
        return chr(ascii_val)
