# Create a class "Student" with private attributes for name, age, and roll number. Implement a method to display the student's details while encapsulating the attributes.

class Student:
    def __init__(self, name, age, roll_number):
        self.__name = name            # Private attribute for name
        self.__age = age              # Private attribute for age
        self.__roll_number = roll_number  # Private attribute for roll number

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, name):
        self.__name = name

    # Getter method for age
    def get_age(self):
        return self.__age

    # Setter method for age
    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self.__age = age

    # Getter method for roll number
    def get_roll_number(self):
        return self.__roll_number

    # Setter method for roll number
    def set_roll_number(self, roll_number):
        self.__roll_number = roll_number

    # Method to display student's details
    def display_details(self):
        return f"Student Name: {self.__name}, Age: {self.__age}, Roll Number: {self.__roll_number}"

# Example usage
student = Student("Alice", 20, "A123")

# Accessing attributes using getter methods
print(student.display_details())  # Output: Student Name: Alice, Age: 20, Roll Number: A123

# Updating attributes using setter methods
student.set_name("Bob")
student.set_age(21)
student.set_roll_number("B456")

# Display updated student's details
print(student.display_details())  # Output: Student Name: Bob, Age: 21, Roll Number: B456
