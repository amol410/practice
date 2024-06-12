
# Write a program that defines a "Employee" class with attributes like name, salary, and employee ID. 
# Implement a method to give a salary raise.


class Employee:
    def __init__(self, name, salary, employee_id):
        self.name = name
        self.salary = salary
        self.employee_id = employee_id
    
    def give_raise(self, raise_amount):
        self.salary += raise_amount
        print(f"{self.name}'s salary has been increased by ${raise_amount}.")
    
    def display_info(self):
        print("Employee Information:")
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")
        print(f"Employee ID: {self.employee_id}")

# Example usage
employee1 = Employee("John Doe", 50000, "E001")
employee2 = Employee("Jane Smith", 60000, "E002")

employee1.display_info()
print()
employee2.display_info()
print()

employee1.give_raise(5000)
employee2.give_raise(7500)
print()

employee1.display_info()
print()
employee2.display_info()