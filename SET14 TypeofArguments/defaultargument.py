# Create a program that defines a function with default arguments to calculate the area of a rectangle.

def calculate_rectangle_area(length=1, width=1):
    """
    Calculate the area of a rectangle with default length and width.
    Default values are 1 for both length and width.

    Parameters:
    length (float or int): The length of the rectangle. Default is 1.
    width (float or int): The width of the rectangle. Default is 1.

    Returns:
    float: The area of the rectangle.
    """
    return length * width

# Example usage
area1 = calculate_rectangle_area()  # Using default values (1, 1)
area2 = calculate_rectangle_area(5)  # Using length=5, default width=1
area3 = calculate_rectangle_area(4, 3)  # Using length=4 and width=3

print(f"Area with default values: {area1}")  # Output: 1
print(f"Area with length=5, default width=1: {area2}")  # Output: 5
print(f"Area with length=4, width=3: {area3}")  # Output: 12
