# def add_item(item, collection=[]):
    # collection.append(item)
    # return collection
# print(add_item("apple"))
# print(add_item("banana"))
# print(add_item("cherry"))
# 
def add_item(item, collection=None):
    if collection is None:
        collection = []
    collection.append(item)
print(add_item("apple"))
print(add_item("banana"))


