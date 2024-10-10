# Define a class "Dog" with private attributes for name and breed. Implement methods to encapsulate these attributes and display the dog's details.

class Dog:
    def __init__(self, name, breed):
        self.__name = name  # Private attribute for name
        self.__breed = breed  # Private attribute for breed

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, name):
        self.__name = name

    # Getter method for breed
    def get_breed(self):
        return self.__breed

    # Setter method for breed
    def set_breed(self, breed):
        self.__breed = breed

    # Method to display dog's details
    def display_details(self):
        return f"Dog's Name: {self.__name}, Breed: {self.__breed}"

# Example usage
dog = Dog("Buddy", "Golden Retriever")

# Accessing attributes using getter methods
print(dog.display_details())  # Output: Dog's Name: Buddy, Breed: Golden Retriever

# Updating attributes using setter methods
dog.set_name("Max")
dog.set_breed("Labrador")

# Display updated dog's details
print(dog.display_details())  # Output: Dog's Name: Max, Breed: Labrador
