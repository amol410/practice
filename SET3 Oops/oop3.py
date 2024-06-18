# Implement a "Rectangle" class with attributes for length and width. 
# Write a method to calculate and return the area of the rectangle.


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        area = self.length * self.width
        return area

# Example usage
rectangle1 = Rectangle(5, 3)
rectangle2 = Rectangle(8, 4)

area1 = rectangle1.calculate_area()
area2 = rectangle2.calculate_area()

print(f"Area of rectangle1: {area1}")
print(f"Area of rectangle2: {area2}")