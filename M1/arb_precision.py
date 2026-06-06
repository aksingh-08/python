# Python: no overflow, ever
x = 2**63
print(x)
print(x+1)

# Very large integers work without any special handling
big = 2**332
print(big)

# sys.getsizeof shows that Python int objects grow in memory as needed
import sys
print(sys.getsizeof(1))             
print(sys.getsizeof(2**30))         
print(sys.getsizeof(2**60))         
print(sys.getsizeof(2**90))         
print(sys.getsizeof(10**100))       