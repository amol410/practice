# Create a base class "Shape" with a method to calculate perimeter. Define derived classes "Rectangle" and "Circle" that calculate perimeter differently.

import math

class Shape:
    def __init__(self):
        pass

    def calculate_perimeter(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

# Usage example
if __name__ == "__main__":
    # Create a rectangle
    rectangle = Rectangle(5, 3)
    print(f"Rectangle perimeter: {rectangle.calculate_perimeter()}")

    # Create a circle
    circle = Circle(4)
    print(f"Circle perimeter: {circle.calculate_perimeter():.2f}")

    # Demonstrate polymorphism
    shapes = [Rectangle(4, 6), Circle(5), Rectangle(3, 7)]
    for shape in shapes:
        print(f"Shape perimeter: {shape.calculate_perimeter():.2f}")