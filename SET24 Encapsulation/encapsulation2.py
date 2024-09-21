# # Define a class "Employee" with private attributes for name, salary, and employee ID. Implement methods to encapsulate these attributes.

# class Employee:
#     def __init__(self, name=None, salary=None, employee_id=None):
#         self.__name = name            # Private attribute for name
#         self.__salary = salary        # Private attribute for salary
#         self.__employee_id = employee_id  # Private attribute for employee ID

#     # Getter for name
#     def get_name(self):
#         return self.__name

#     # Setter for name
#     def set_name(self, name):
#         self.__name = name

#     # Getter for salary
#     def get_salary(self):
#         return self.__salary

#     # Setter for salary
#     def set_salary(self, salary):
#         if salary >= 0:  # Simple validation for salary
#             self.__salary = salary
#         else:
#             raise ValueError("Salary must be a non-negative value.")

#     # Getter for employee ID
#     def get_employee_id(self):
#         return self.__employee_id

#     # Setter for employee ID
#     def set_employee_id(self, employee_id):
#         self.__employee_id = employee_id


# # Example usage:
# employee = Employee()
# employee.set_name("Alice Smith")
# employee.set_salary(50000)
# employee.set_employee_id("EMP001")

# print(f"Name: {employee.get_name()}")
# print(f"Salary: {employee.get_salary()}")
# print(f"Employee ID: {employee.get_employee_id()}")




class employee:
    def __init__(self, name=None, salary=None, employee_id=None):
        self.__name = name
        self.__salary = salary
        self.__employee_id = employee_id

    def get_name(self):
        return self.__name 
    
    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.employee_id = employee_id        


employee = employee()

employee.set_name("amol")
employee.set_employee_id("emp211")
employee.set_salary(90000)

print (f"name{employee.get_name()}")
print (f"salary{employee.get_salary()}")
print (f"employee_id {employee.get_employee_id()}")
