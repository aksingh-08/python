def demonstrate(st, num):
    print(f"    id(st) inside: {id(st)}")
    print(f"    id(num) inside: {id(num)}")
my_list = [1, 2, 3]
my_num = 42

print(f"id(my_list): {id(my_list)}")
print(f"id(my_num): {id(my_num)}")
demonstrate(my_list, my_num)

print("*****************************************************************")

def mutate(lst):
    lst.append(99) # Mutates shared object - VISIBLE to caller

def rebind(lst):
    lst = [100, 200] # Rebinds local name - NOT visible to caller

original = [1, 2, 3]

mutate(original)
print(original)

rebind(original)
print(original)
