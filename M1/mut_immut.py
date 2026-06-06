def classify(obj):
    immutable_types = (int, float, bool, str, bytes, tuple, frozenset, type(None))
    return "immutable" if isinstance(obj, immutable_types) else "mutable"

print(classify(42))
print(classify([1, 2]))
print(classify("hello"))
print(classify({"a": 1}))
print(classify((1, 2)))
print(classify({1, 2}))

# mutable = list, dict, set, bytearray