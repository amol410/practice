# Define a base class "Employee" with a method to calculate the annual salary. Create derived classes "Manager" and "Worker" that calculate the annual salary differently.

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def calculate_annual_salary(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Manager(Employee):
    def __init__(self, name, employee_id, base_salary, bonus_percentage):
        super().__init__(name, employee_id)
        self.base_salary = base_salary
        self.bonus_percentage = bonus_percentage

    def calculate_annual_salary(self):
        bonus = self.base_salary * (self.bonus_percentage / 100)
        return self.base_salary + bonus

class Worker(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_per_week):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_per_week = hours_per_week

    def calculate_annual_salary(self):
        return self.hourly_rate * self.hours_per_week * 52  # Assuming 52 weeks in a year

# Usage example
if __name__ == "__main__":
    # Create instances of Manager and Worker
    manager = Manager("Alice Smith", "M001", 80000, 20)  # 20% bonus
    worker = Worker("Bob Johnson", "W001", 25, 40)  # $25/hour, 40 hours/week

    # Calculate and display annual salaries
    print(f"{manager.name} (Manager) - Annual Salary: ${manager.calculate_annual_salary():,.2f}")
    print(f"{worker.name} (Worker) - Annual Salary: ${worker.calculate_annual_salary():,.2f}")

    # Demonstrate polymorphism
    employees = [
        Manager("Charlie Brown", "M002", 90000, 15),  # 15% bonus
        Worker("Diana Prince", "W002", 30, 35),  # $30/hour, 35 hours/week
        Manager("Eve Davis", "M003", 75000, 25)  # 25% bonus
    ]

    for employee in employees:
        print(f"{employee.name} ({employee.__class__.__name__}) - Annual Salary: ${employee.calculate_annual_salary():,.2f}")