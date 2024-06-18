# Implement a "Dog" class with attributes for name and breed. 
# Write a method to display the dog's name and breed.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")

# Example usage
dog1 = Dog("Buddy", "Labrador Retriever")
dog2 = Dog("Max", "German Shepherd")

dog1.display_info()
print()
dog2.display_info()