# Write a program that defines a "Student" class with attributes like name, age, and roll number. 
# Implement a method to display the student's details.

class Student:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number
    
    def display_details(self):
        print("Student Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll Number: {self.roll_number}")

# Example usage
student1 = Student("John Doe", 18, 101)
student2 = Student("Alice Smith", 19, 102)

student1.display_details()
print()
student2.display_details()