# Define a base class "Employee" with a method to calculate the bonus. Create derived classes "Manager" and "Worker" that calculate the bonus differently.


# Base class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        raise NotImplementedError("Subclass must implement this method.")

# Derived class for Manager
class Manager(Employee):
    def calculate_bonus(self):
        # Managers get 20% of their salary as a bonus
        return self.salary * 0.20

# Derived class for Worker
class Worker(Employee):
    def calculate_bonus(self):
        # Workers get 10% of their salary as a bonus
        return self.salary * 0.10

# Example usage
manager = Manager("Alice", 80000)
worker = Worker("Bob", 40000)

print(f"{manager.name}'s bonus: ${manager.calculate_bonus():.2f}")  # Output: 16000.00
print(f"{worker.name}'s bonus: ${worker.calculate_bonus():.2f}")    # Output: 4000.00
