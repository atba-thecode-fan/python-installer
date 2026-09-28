# Python Installer v2.0 Beta RC-4.0
# Extension Configuration File

EXTENSION_VERSION = "2.0-Beta-RC-4.0"
RELEASE_STATUS = "Beta Release Candidate 4"

extensions = [
    {
        "name": "Python Core Extension",
        "file": "python_core.ext",
        "enabled": True,
        "priority": 1
    },
    {
        "name": "C# .NET Extension",
        "file": "csharp_dotnet.ext",
        "enabled": True,
        "priority": 2
    },
    {
        "name": "C++ Compiler Extension",
        "file": "cpp_compiler.ext",
        "enabled": True,
        "priority": 3
    },
    {
        "name": "HTML Web Extension",
        "file": "html_web.ext",
        "enabled": True,
        "priority": 4
    }
]

def load_all_extensions():
    """Load all configured extensions"""
    for ext in extensions:
        if ext["enabled"]:
            print(f"Loading {ext['name']} from {ext['file']}")
