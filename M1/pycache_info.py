import py_compile
import struct
import sys
import os

with open("_temp_mod.py", "w") as f:
    f.write("answer = 42\n")

pyc_path = py_compile.compile("_temp_mod.py")

with open(pyc_path, "rb") as f:
    magic = f.read(4)
    flags = struct.unpack("<I", f.read(4))[0]
    timestamp = struct.unpack("<I", f.read(4))[0]
    size = struct.unpack("<I", f.read(4))[0]

print(f"Magic number: {magic.hex()}")
print(f"Flags: {flags}")
print(f"Timestamp: {timestamp} (non-zero = source timestamp)")
print(f"Source size: {size} bytes")
print(f"Python version: {sys.version_info.major}.{sys.version_info.minor}")

os.remove("_temp_mod.py")
os.remove(pyc_path)
os.rmdir("__pycache__")

# The .pyc header contains exactly 16 bytes in 4 fields:

# 1. Magic number (4 bytes): Identifies the Python version that produced this bytecode. Each CPython release uses a different magic number. If you try to load a .pyc from the wrong Python version, the magic number mismatch causes a recompile.
# 2. Flags (4 bytes): Bit flags. Bit 0 indicates whether the file uses a hash-based invalidation check (PEP 552) instead of timestamp-based.
# 3. Timestamp (4 bytes): The modification time of the source .py file when it was compiled. Python compares this to the current source file timestamp to decide if recompilation is needed.
# 4. Source size (4 bytes): The size of the original .py file in bytes. An extra check to detect changes even if the timestamp is the same.

# Why this matters: This is how Python decides whether to use the cached .pyc or recompile. When you edit a source file, the timestamp changes, the cached .pyc becomes stale, and Python recompiles automatically on the next import.