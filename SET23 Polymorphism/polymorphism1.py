# Create a base class "Shape" with a method to calculate area. Define derived classes "Rectangle" and "Circle" that implement the area calculation differently.

import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement this method.")

# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Example usage
rectangle = Rectangle(4, 5)
circle = Circle(3)

print(f"Rectangle area: {rectangle.area()}")  # Output: 20
print(f"Circle area: {circle.area():.2f}")    # Output: 28.27
