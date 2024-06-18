# Implement a base class "Animal" with attributes for name and species. 
# Create a derived class "Bird" that inherits from "Animal" 
# and adds attributes for wingspan and habitat.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Bird(Animal):
    def __init__(self, name, species, wingspan, habitat):
        super().__init__(name, species)
        self.wingspan = wingspan
        self.habitat = habitat


eagle = Bird("Rocky", "Bald Eagle", 2.3, "Forest")
print(eagle.name)     # Output: Rocky
print(eagle.species)  # Output: Bald Eagle
print(eagle.wingspan) # Output: 2.3
print(eagle.habitat)  # Output: Forest

parrot = Bird("Polly", "Macaw", 1.2, "Rainforest")
print(parrot.name)    # Output: Polly
print(parrot.species) # Output: Macaw
print(parrot.wingspan) # Output: 1.2
print(parrot.habitat) # Output: Rainforest      

# can also create animal base class if required

dog = Animal("Buddy", "Golden Retriever")
print(dog.name)     # Output: Buddy
print(dog.species)  # Output: Golden Retriever