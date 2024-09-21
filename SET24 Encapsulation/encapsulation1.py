# Create a class "Student" with private attributes for name, age, and roll number. Implement methods to set and get these attributes.

class Student:
    def __init__(self, name=None, age=None, roll_number=None):
        self.__name = name          # Private attribute
        self.__age = age            # Private attribute
        self.__roll_number = roll_number  # Private attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age > 0:  # Simple validation for age
            self.__age = age
        else:
            raise ValueError("Age must be a positive number.")

    # Getter for roll number
    def get_roll_number(self):
        return self.__roll_number

    # Setter for roll number
    def set_roll_number(self, roll_number):
        self.__roll_number = roll_number


# Example usage:
student = Student()
student.set_name("John Doe")
student.set_age(20)
student.set_roll_number("12345")

print(f"Name: {student.get_name()}")
print(f"Age: {student.get_age()}")
print(f"Roll Number: {student.get_roll_number()}")
