# Create a Python class to represent a "Car" with attributes like make, model, and year. 
# Implement a method to display the car's information.


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

# Example usage
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2021)

car1.display_info()
print()
car2.display_info()