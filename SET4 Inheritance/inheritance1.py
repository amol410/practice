# Define a base class "Vehicle" with attributes like make, model, and year. 
# Create a derived class "Car" that inherits from "Vehicle" and adds a method to display car details.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def display_details(self):
        print("Car Details:")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

# Example usage
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2021)

car1.display_details()
print()
car2.display_details()