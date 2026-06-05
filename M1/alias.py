def are_aliases(a, b):
    return a is b
x=[1, 2, 3]
y=x
z=[1, 2, 3]
print(are_aliases(x, y))
print(are_aliases(x, z))
