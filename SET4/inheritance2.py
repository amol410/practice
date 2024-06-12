# Implement a base class "Shape" with attributes for color and area. 
# Create derived classes "Rectangle" and "Circle" that inherit from "Shape" and calculate their respective areas.

import math

class Shape:
    def __init__(self, color):
        self.color = color
        self.area = 0

    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def calculate_area(self):
        self.area = self.width * self.height

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        self.area = math.pi * self.radius ** 2

# Example usage
rectangle = Rectangle("Red", 5, 3)
circle = Circle("Blue", 4)

rectangle.calculate_area()
circle.calculate_area()

print("Rectangle:")
print(f"Color: {rectangle.color}")
print(f"Area: {rectangle.area}")

print("\nCircle:")
print(f"Color: {circle.color}")
print(f"Area: {circle.area:.2f}")