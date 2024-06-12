# Define a base class "Person" with attributes for name, age, and address. 
# Create a derived class "Employee" that inherits from "Person" and adds attributes like employee ID and salary.

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print("Person Information:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

class Employee(Person):
    def __init__(self, name, age, address, employee_id, salary):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")

# Example usage
person = Person("John Doe", 30, "123 Main St")
employee = Employee("Jane Smith", 35, "456 Elm St", "E001", 50000)

person.display_info()
print()
employee.display_info()