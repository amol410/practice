# Create a base class "Animal" with attributes for name and species. 
# Define a derived class "Dog" that inherits from "Animal" and 
# adds attributes for breed and age.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name, species="Dog")
        self.breed = breed
        self.age = age
    
    def display_info(self):
        super().display_info()
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age}")

# Example usage
animal = Animal("Buddy", "Cat")
animal.display_info()

dog = Dog("Max", "Labrador", 3)
dog.display_info()