# Write a program that defines a "Person" class with attributes like name, age, and address. 
# Implement a method to change the person's address.

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def change_address(self, new_address):
        self.address = new_address
        print(f"{self.name}'s address has been updated to: {self.address}")
    
    def display_info(self):
        print("Person Information:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

# Example usage
person1 = Person("John Doe", 30, "123 Main St, Anytown, USA")
person2 = Person("Jane Smith", 25, "456 Elm St, Somewhere, USA")

person1.display_info()
print()
person2.display_info()
print()

person1.change_address("789 Oak Ave, Newplace, USA")
person2.change_address("321 Pine Rd, Othertown, USA")
print()

person1.display_info()
print()
person2.display_info()