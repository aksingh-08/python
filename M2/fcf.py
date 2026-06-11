def greet(name):
    return f"Hello, {name}"
# srore in a varibale
f = greet
print(f("lancer"))
# store in a list
funcs = [greet, len, str.upper]
# pass as an argument
def apply(func, value):
    return func(value)
print(apply(greet, "lan"))
print(apply(len, "lancer"))
print(apply(str.upper, "lancer"))
# return from a function
def make_multiplier(n):
    def multiplier(x):
        return x*n
    return multiplier
double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))
print(triple(5))
