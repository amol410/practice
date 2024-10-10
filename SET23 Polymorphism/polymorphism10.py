# Create a base class "Vehicle" with a method to start the engine. Define derived classes "Car" and "Bicycle" that start the engine differently.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_running = False

    def start_engine(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def stop_engine(self):
        if self.is_running:
            self.is_running = False
            return f"{self.brand} {self.model} engine stopped."
        else:
            return f"{self.brand} {self.model} is already stopped."

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            return f"{self.brand} {self.model} car engine started. Ready to drive using {self.fuel_type}."
        else:
            return f"{self.brand} {self.model} car engine is already running."

class Bicycle(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model)
        self.type = type

    def start_engine(self):
        return f"{self.brand} {self.model} bicycle doesn't have an engine. Start pedaling your {self.type} bike!"

# Usage example
if __name__ == "__main__":
    # Create instances of Car and Bicycle
    car = Car("Toyota", "Corolla", "gasoline")
    bicycle = Bicycle("Trek", "FX 3", "hybrid")

    # Demonstrate starting vehicles
    print(car.start_engine())
    print(car.start_engine())  # Try starting again
    print(car.stop_engine())
    print(car.stop_engine())  # Try stopping again

    print("\n" + bicycle.start_engine())

    # Demonstrate polymorphism
    vehicles = [
        Car("Tesla", "Model 3", "electricity"),
        Bicycle("Schwinn", "Cruiser", "city"),
        Car("Ford", "Mustang", "gasoline")
    ]

    print("\nStarting different vehicles:")
    for vehicle in vehicles:
        print(vehicle.start_engine())