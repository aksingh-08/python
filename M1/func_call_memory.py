def mutate(lst):
    lst.append(99) # Mutates shared object - VISIBLE to caller

def rebind(lst):
    lst = [100, 200] # Rebinds local name - NOT visible to caller

original = [1, 2, 3]

mutate(original)
print(original)

rebind(original)
print(original)
