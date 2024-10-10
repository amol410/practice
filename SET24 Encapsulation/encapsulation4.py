# Create a class "Rectangle" with private attributes for length and width. Implement methods to calculate and return the area while encapsulating these attributes.

class Rectangle:
    def __init__(self, length, width):
        self.__length = self.__validate_dimension(length)
        self.__width = self.__validate_dimension(width)

    def __validate_dimension(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Dimensions must be positive numbers")
        return value

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def set_length(self, length):
        self.__length = self.__validate_dimension(length)

    def set_width(self, width):
        self.__width = self.__validate_dimension(width)

    def calculate_area(self):
        return self.__length * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__length + self.__width)

    def get_info(self):
        return f"Rectangle(length={self.__length}, width={self.__width})"

# Usage example
if __name__ == "__main__":
    try:
        # Create a rectangle
        rect = Rectangle(5, 3)
        print(rect.get_info())

        # Calculate and display area and perimeter
        print(f"Area: {rect.calculate_area()}")
        print(f"Perimeter: {rect.calculate_perimeter()}")

        # Modify dimensions
        rect.set_length(7)
        rect.set_width(4)
        print(rect.get_info())
        print(f"New Area: {rect.calculate_area()}")

        # Attempt to set invalid dimensions
        rect.set_length(-2)  # This will raise a ValueError
    except ValueError as e:
        print(f"Error: {e}")

    # Demonstrate encapsulation
    try:
        print(rect.__length)  # This will raise an AttributeError
    except AttributeError as e:
        print(f"Error: {e}")

    # Attempting to modify private attribute directly (creates a new attribute)
    rect.__length = 100
    print(rect.get_info())  # The actual length remains unchanged