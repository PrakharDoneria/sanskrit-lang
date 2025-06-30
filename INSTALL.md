# Sanskrit Programming Language Installation Guide

## Download and Installation

### Windows

#### Option 1: Automated Installation (Recommended)
1. Download `sans-windows.exe` and `windows-install.bat` from the [latest release](https://github.com/yourusername/sanskrit-lang/releases)
2. Place both files in the same folder
3. Right-click on `windows-install.bat` and select "Run as administrator"
4. The installer will:
   - Copy `sans.exe` to `C:\Program Files\SanskritLang\`
   - Add the installation directory to your system PATH
   - Make the `sans` command available globally

#### Option 2: Manual Installation
1. Download `sans-windows.exe` from releases
2. Rename it to `sans.exe`
3. Create a folder like `C:\SanskritLang\` and place `sans.exe` inside
4. Add `C:\SanskritLang\` to your system PATH:
   - Open "Environment Variables" in System Properties
   - Edit the "Path" variable in System Variables
   - Add the path to your installation directory
   - Click OK and restart Command Prompt

#### Verification
Open Command Prompt or PowerShell and run:
```cmd
sans --version
```

### macOS

#### Installation
1. Download `sans-macos` and `macos-install.sh` from releases
2. Open Terminal and navigate to the download folder
3. Make the files executable:
   ```bash
   chmod +x sans-macos macos-install.sh
   ```
4. Run the installer:
   ```bash
   sudo ./macos-install.sh
   ```

#### Manual Installation
1. Download `sans-macos` and rename it to `sans`
2. Make it executable: `chmod +x sans`
3. Move to system path: `sudo mv sans /usr/local/bin/`

#### Verification
```bash
sans --version
```

### Linux

#### Option 1: Using Install Script
1. Download `sans-linux` and `linux-install.sh` from releases
2. Make them executable:
   ```bash
   chmod +x sans-linux linux-install.sh
   ```
3. Run installer:
   ```bash
   sudo ./linux-install.sh
   ```

#### Option 2: Manual Installation
1. Download `sans-linux` and rename to `sans`
2. Make executable: `chmod +x sans`
3. Move to system path: `sudo mv sans /usr/local/bin/`

#### Verification
```bash
sans --version
```

## Usage After Installation

Once installed, you can use the `sans` command from anywhere:

### Run a Sanskrit Program
```bash
sans myprogram.sans
```

### Start Interactive REPL
```bash
sans --repl
# or simply
sans
```

### Launch GUI Editor
```bash
sans --editor
```

### Get Help
```bash
sans --help
```

## VS Code Integration

After installing Sanskrit language, you can run programs directly in VS Code:

### Setup
1. Install VS Code if not already installed
2. Create or open a folder for your Sanskrit projects
3. Create a new file with `.sans` extension
4. Write your Sanskrit code

### Running Programs
1. Open the integrated terminal (Ctrl+` or Cmd+`)
2. Run your program:
   ```bash
   sans yourfile.sans
   ```

### Optional: Configure Tasks
Copy the provided `.vscode/tasks.json` to your project for integrated tasks:
- **Ctrl+Shift+P** → "Tasks: Run Task" → "Run Sanskrit Program"
- **Ctrl+Shift+P** → "Tasks: Run Task" → "Start Sanskrit REPL" 
- **Ctrl+Shift+P** → "Tasks: Run Task" → "Open Sanskrit Editor"

### Font Recommendation
For better Devanagari script display, install "Noto Sans Devanagari" font:
- Windows: Download from Google Fonts
- macOS: Available in Font Book
- Linux: `sudo apt install fonts-noto-devanagari` (Ubuntu/Debian)

## Example Programs

Create a file `hello.sans`:

```sanskrit
# नमस्ते संसार!
मुद्रण("नमस्ते संसार!")

धारणा नाम = "राम"
मुद्रण("नमस्कार", नाम)

# गिनती 1 से 5 तक
धारणा i = १
यावत् i <= ५ {
    मुद्रण("संख्या:", i)
    i = i + १
}

मुद्रण("प्रोग्राम समाप्त!")
```

Run with:
```bash
sans hello.sans
```

## Troubleshooting

### Command Not Found
If you get "sans: command not found":

**Windows:**
- Restart Command Prompt/PowerShell after installation
- Verify PATH environment variable includes installation directory

**macOS/Linux:**
- Restart terminal after installation
- Check if `/usr/local/bin` is in your PATH: `echo $PATH`
- Try running with full path: `/usr/local/bin/sans --version`

### Permission Denied
**macOS/Linux:**
- Ensure the `sans` binary is executable: `chmod +x /usr/local/bin/sans`
- Run installer with sudo: `sudo ./install.sh`

### Unicode Display Issues
- Install Devanagari fonts (Noto Sans Devanagari recommended)
- Set terminal encoding to UTF-8
- Use a terminal that supports Unicode properly

### GUI Editor Not Working
- Ensure Python tkinter is installed (usually comes with Python)
- On Linux, install tkinter: `sudo apt install python3-tk`

## Uninstallation

### Windows
1. Remove installation directory (e.g., `C:\Program Files\SanskritLang\`)
2. Remove directory from PATH environment variable

### macOS/Linux
1. Delete binary: `sudo rm /usr/local/bin/sans`
2. For Linux with install script: run `sudo ./linux-uninstall.sh`

## Building from Source

If you want to build from source instead of using releases:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sanskrit-lang.git
   cd sanskrit-lang
   ```

2. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

3. Build executable:
   ```bash
   pyinstaller --onefile --name sans cli.py
   ```

4. The executable will be in `dist/sans` (or `dist/sans.exe` on Windows)

## Getting Help

- Use `sans --help` for command-line help
- Start REPL and type `सहायता` for interactive help
- Check the [GitHub repository](https://github.com/yourusername/sanskrit-lang) for documentation and examples
- Report issues on the GitHub issue tracker