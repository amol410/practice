# Create a base class "Vehicle" with a method to display information. Define derived classes "Car" and "Truck" that override the display method.

# Base class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        raise NotImplementedError("Subclass must implement this method.")

# Derived class for Car
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display_info(self):
        return f"Car: {self.year} {self.make} {self.model}, {self.doors} doors"

# Derived class for Truck
class Truck(Vehicle):
    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year)
        self.capacity = capacity

    def display_info(self):
        return f"Truck: {self.year} {self.make} {self.model}, {self.capacity} ton capacity"

# Example usage
car = Car("Toyota", "Corolla", 2021, 4)
truck = Truck("Ford", "F-150", 2019, 1.5)

print(car.display_info())  # Output: Car: 2021 Toyota Corolla, 4 doors
print(truck.display_info())  # Output: Truck: 2019 Ford F-150, 1.5 ton capacity
