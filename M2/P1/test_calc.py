import subprocess
import sys

# Test commands
test_commands = [
    "add 5 3",
    "sub 10 2",
    "mul 4 5",
    "div 20 4",
    "help",
    "history",
    "exit"
]

# Create input
test_input = "\n".join(test_commands)

# Run the calculator
proc = subprocess.Popen(
    [sys.executable, "calc.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    cwd=r"C:\Users\ashis\Desktop\python\M2\P1"
)

stdout, stderr = proc.communicate(input=test_input)

print("=== CALCULATOR OUTPUT ===")
print(stdout)
if stderr:
    print("=== ERRORS ===")
    print(stderr)
