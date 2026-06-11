class Dog:
    species = "Canis lupus familiaris"
    def bark(self):
        return "Woof!"
print(type(Dog))
print(isinstance(Dog, type))
print(Dog.species)
