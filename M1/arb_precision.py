# Python: no overflow, ever
x = 2**63
print(x)
print(x+1)

# Very large integers work without any special handling
big = 2**332
print(big)

# sys.getsizeof shows that Python int objects grow in memory as needed
import sys
print(sys.getsizeof(1))             # 28 bytes - minimal int
print(sys.getsizeof(2**30))         # 28 bytes - still fits in one 30-bit digit
print(sys.getsizeof(2**60))         # 32 bytes - needs a second digit
print(sys.getsizeof(2**90))         # 36 bytes - three digits
print(sys.getsizeof(10**100))       # 72 bytes - a googol