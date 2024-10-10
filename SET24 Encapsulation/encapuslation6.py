# Implement a class "Circle" with a private attribute for radius. Provide methods to calculate and return the area while encapsulating the radius.

import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius  # Private attribute for radius

    # Getter method for radius
    def get_radius(self):
        return self.__radius

    # Setter method for radius
    def set_radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        self.__radius = radius

    # Method to calculate the area of the circle
    def calculate_area(self):
        return math.pi * (self.__radius ** 2)

# Example usage
circle = Circle(5)

# Accessing the radius using the getter method
print(f"Circle radius: {circle.get_radius()}")  # Output: Circle radius: 5

# Calculating and displaying the area
print(f"Circle area: {circle.calculate_area():.2f}")  # Output: Circle area: 78.54

# Updating the radius using the setter method
circle.set_radius(10)

# Display updated radius and area
print(f"Updated circle radius: {circle.get_radius()}")  # Output: Updated circle radius: 10
print(f"Updated circle area: {circle.calculate_area():.2f}")  # Output: Updated circle area: 314.16
