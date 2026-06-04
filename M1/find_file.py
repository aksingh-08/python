import py_compile
import os
import sys
with open("example.py", "w") as f:
    f.write("x = 42\nprint(x)\n")
    
pyc_path = py_compile.compile("example.py")
print(f"Compiled! .pyc file exists at: {pyc_path}")
print(f"File exists: {os.path.exists(pyc_path)}")
print(f"Python version tag: cpython-{sys.version_info.major}{sys.version_info.minor}")

os.remove("example.py")
if os.path.exists(pyc_path):
    os.remove(pyc_path)
    os.rmdir("__pycache__")
