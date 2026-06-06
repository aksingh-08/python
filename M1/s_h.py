# Reassignment - moves the name to a different object:
a=5
b=a
b=6
print(a)
print(id(a))
print(b)
print(id(b))
print(a==b)


# Mutaion - changes the object itself (all names see the change):
x=[1, 2, 3]
y=x
y.append(4)
print(x)
print(id(x))
print(y)
print(id(y))
print(x==y)

