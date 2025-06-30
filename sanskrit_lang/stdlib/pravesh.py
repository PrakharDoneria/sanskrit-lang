"""
Pravesh Module (प्रवेश)
Input/Output operations and file handling
"""

import os
import sys
from typing import Any, Optional

class PraveshModule:
    """Input/Output operations module"""
    
    def __init__(self):
        pass
    
    def paath(self, prompt=""):
        """Read input from user (पाठ)"""
        return input(prompt)
    
    def sankhya_paath(self, prompt=""):
        """Read number input (संख्या पाठ)"""
        while True:
            try:
                value = input(prompt)
                # Handle Devanagari numerals
                devanagari_digits = '०१२३४५६७८९'
                ascii_digits = '0123456789'
                for i, d in enumerate(devanagari_digits):
                    value = value.replace(d, ascii_digits[i])
                
                if '.' in value:
                    return float(value)
                else:
                    return int(value)
            except ValueError:
                print("कृपया वैध संख्या दर्ज करें")
    
    def mudran(self, *args, **kwargs):
        """Print output (मुद्रण)"""
        print(*args, **kwargs)
    
    def naya_rekha(self):
        """Print newline (नया रेखा)"""
        print()
    
    def file_padhiye(self, file_path, encoding='utf-8'):
        """Read file content (फ़ाइल पढ़िये)"""
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"फ़ाइल '{file_path}' नहीं मिली")
        except Exception as e:
            raise Exception(f"फ़ाइल पढ़ने में त्रुटि: {e}")
    
    def file_likhiye(self, file_path, content, encoding='utf-8'):
        """Write file content (फ़ाइल लिखिये)"""
        try:
            with open(file_path, 'w', encoding=encoding) as file:
                file.write(content)
            return True
        except Exception as e:
            raise Exception(f"फ़ाइल लिखने में त्रुटि: {e}")
    
    def file_jodiye(self, file_path, content, encoding='utf-8'):
        """Append to file (फ़ाइल जोड़िये)"""
        try:
            with open(file_path, 'a', encoding=encoding) as file:
                file.write(content)
            return True
        except Exception as e:
            raise Exception(f"फ़ाइल में जोड़ने में त्रुटि: {e}")
    
    def file_hai(self, file_path):
        """Check if file exists (फ़ाइल है)"""
        return os.path.exists(file_path)
    
    def file_hataye(self, file_path):
        """Delete file (फ़ाइल हटायें)"""
        try:
            os.remove(file_path)
            return True
        except FileNotFoundError:
            raise FileNotFoundError(f"फ़ाइल '{file_path}' नहीं मिली")
        except Exception as e:
            raise Exception(f"फ़ाइल हटाने में त्रुटि: {e}")
    
    def folder_banaye(self, folder_path):
        """Create directory (फ़ोल्डर बनायें)"""
        try:
            os.makedirs(folder_path, exist_ok=True)
            return True
        except Exception as e:
            raise Exception(f"फ़ोल्डर बनाने में त्रुटि: {e}")
    
    def folder_hai(self, folder_path):
        """Check if directory exists (फ़ोल्डर है)"""
        return os.path.isdir(folder_path)
    
    def folder_suchi(self, folder_path="."):
        """List directory contents (फ़ोल्डर सूची)"""
        try:
            return os.listdir(folder_path)
        except Exception as e:
            raise Exception(f"फ़ोल्डर सूची में त्रुटि: {e}")
    
    def vartmaan_path(self):
        """Get current working directory (वर्तमान पथ)"""
        return os.getcwd()
    
    def path_badliye(self, new_path):
        """Change working directory (पथ बदलिये)"""
        try:
            os.chdir(new_path)
            return True
        except Exception as e:
            raise Exception(f"पथ बदलने में त्रुटि: {e}")
    
    def file_aakaar(self, file_path):
        """Get file size (फ़ाइल आकार)"""
        try:
            return os.path.getsize(file_path)
        except Exception as e:
            raise Exception(f"फ़ाइल आकार पाने में त्रुटि: {e}")
    
    def file_samay(self, file_path):
        """Get file modification time (फ़ाइल समय)"""
        try:
            return os.path.getmtime(file_path)
        except Exception as e:
            raise Exception(f"फ़ाइल समय पाने में त्रुटि: {e}")
    
    def path_jod(self, *paths):
        """Join paths (पथ जोड़)"""
        return os.path.join(*paths)
    
    def path_naam(self, path):
        """Get basename from path (पथ नाम)"""
        return os.path.basename(path)
    
    def path_folder(self, path):
        """Get directory from path (पथ फ़ोल्डर)"""
        return os.path.dirname(path)
    
    def path_vibhaajan(self, path):
        """Split path into directory and filename (पथ विभाजन)"""
        return os.path.split(path)
    
    def path_nirpeksh(self, path):
        """Get absolute path (पथ निर्पेक्ष)"""
        return os.path.abspath(path)
    
    def env_var(self, name, default=None):
        """Get environment variable (पर्यावरण चर)"""
        return os.getenv(name, default)
    
    def program_band(self, code=0):
        """Exit program (प्रोग्राम बंद)"""
        sys.exit(code)
    
    def command_line_args(self):
        """Get command line arguments (आदेश पंक्ति तर्क)"""
        return sys.argv
    
    def platform_jaaniye(self):
        """Get platform information (प्लेटफॉर्म जानिये)"""
        return sys.platform
    
    def python_version(self):
        """Get Python version (पायथन संस्करण)"""
        return sys.version
    
    def memory_upyog(self):
        """Get memory usage info (स्मृति उपयोग)"""
        import psutil
        process = psutil.Process()
        return {
            'rss': process.memory_info().rss,
            'vms': process.memory_info().vms,
            'percent': process.memory_percent()
        }
    
    def csv_padhiye(self, file_path, delimiter=',', encoding='utf-8'):
        """Read CSV file (CSV पढ़िये)"""
        import csv
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                reader = csv.reader(file, delimiter=delimiter)
                return list(reader)
        except Exception as e:
            raise Exception(f"CSV फ़ाइल पढ़ने में त्रुटि: {e}")
    
    def csv_likhiye(self, file_path, data, delimiter=',', encoding='utf-8'):
        """Write CSV file (CSV लिखिये)"""
        import csv
        try:
            with open(file_path, 'w', newline='', encoding=encoding) as file:
                writer = csv.writer(file, delimiter=delimiter)
                writer.writerows(data)
            return True
        except Exception as e:
            raise Exception(f"CSV फ़ाइल लिखने में त्रुटि: {e}")
