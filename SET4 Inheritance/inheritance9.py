class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, age, salary, team_size, project):
        super().__init__(name, age, salary)
        self.team_size = team_size
        self.project = project

manager1 = Manager("John Doe", 35, 80000, 10, "Project Alpha")
print(manager1.name)     # Output: John Doe
print(manager1.age)      # Output: 35
print(manager1.salary)   # Output: 80000
print(manager1.team_size) # Output: 10
print(manager1.project)  # Output: Project Alpha

manager2 = Manager("Jane Smith", 42, 90000, 15, "Project Omega")
print(manager2.name)     # Output: Jane Smith
print(manager2.age)      # Output: 42
print(manager2.salary)   # Output: 90000
print(manager2.team_size) # Output: 15
print(manager2.project)  # Output: Project Omega       


# You can also create instances of the Employee base class if needed:

employee = Employee("Bob Johnson", 28, 50000)
print(employee.name)     # Output: Bob Johnson
print(employee.age)      # Output: 28
print(employee.salary)   # Output: 50000