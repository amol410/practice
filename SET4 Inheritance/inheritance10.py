class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity, towing_capacity):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity
        self.towing_capacity = towing_capacity

truck1 = Truck("Ford", "F-150", 2022, 1785, 13200)
print(truck1.make)         # Output: Ford
print(truck1.model)        # Output: F-150
print(truck1.year)         # Output: 2022
print(truck1.payload_capacity) # Output: 1785
print(truck1.towing_capacity)  # Output: 13200

truck2 = Truck("Chevrolet", "Silverado", 2020, 2100, 12000)
print(truck2.make)         # Output: Chevrolet
print(truck2.model)        # Output: Silverado
print(truck2.year)         # Output: 2020
print(truck2.payload_capacity) # Output: 2100
print(truck2.towing_capacity)  # Output: 12000        