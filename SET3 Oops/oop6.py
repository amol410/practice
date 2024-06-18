# Implement a "Circle" class with attributes for radius 
# and a method to calculate and return the area of the circle.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        area = math.pi * self.radius ** 2
        return area

# Example usage
circle1 = Circle(5)
circle2 = Circle(3.7)

area1 = circle1.calculate_area()
area2 = circle2.calculate_area()

print(f"Area of circle1 (radius={circle1.radius}): {area1:.2f}")
print(f"Area of circle2 (radius={circle2.radius}): {area2:.2f}")