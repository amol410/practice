# Create a base class "GeometricShape" with attributes for color and dimensions. 
# Define a derived class "Rectangle" that inherits from "GeometricShape" 
# and calculates its area.

class GeometricShape:
    def __init__(self, color, dimensions):
        self.color = color
        self.dimensions = dimensions

class Rectangle(GeometricShape):
    def __init__(self, color, length, width):
        self.length = length
        self.width = width
        dimensions = [length, width]
        super().__init__(color, dimensions)

    def area(self):
        return self.length * self.width
    
rectangle = Rectangle("red", 5, 3)
print(rectangle.color)    # Output: red
print(rectangle.dimensions)  # Output: [5, 3]
print(rectangle.area())   # Output: 15    