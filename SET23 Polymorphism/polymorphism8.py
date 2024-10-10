# Implement a base class "Animal" with a method to describe habitat. Create derived classes "Bird" and "Mammal" that provide their own habitat descriptions.

class Animal:
    def __init__(self, name):
        self.name = name

    def describe_habitat(self):
        return "Animals can live in various habitats."

class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly

    def describe_habitat(self):
        basic_description = super().describe_habitat()
        if self.can_fly:
            return f"{basic_description} {self.name} typically lives in trees or open skies."
        else:
            return f"{basic_description} {self.name}, being a flightless bird, often lives on the ground."

class Mammal(Animal):
    def __init__(self, name, is_aquatic):
        super().__init__(name)
        self.is_aquatic = is_aquatic

    def describe_habitat(self):
        if self.is_aquatic:
            return f"{self.name} lives in aquatic environments like oceans, rivers, or lakes."
        else:
            return f"{self.name} is a terrestrial mammal and can live in various land habitats like forests, grasslands, or mountains."

# Usage example
if __name__ == "__main__":
    # Create instances of different animals
    generic_animal = Animal("Generic Animal")
    eagle = Bird("Eagle", can_fly=True)
    penguin = Bird("Penguin", can_fly=False)
    lion = Mammal("Lion", is_aquatic=False)
    dolphin = Mammal("Dolphin", is_aquatic=True)

    # Demonstrate polymorphism and method overriding
    animals = [generic_animal, eagle, penguin, lion, dolphin]
    
    for animal in animals:
        print(f"{animal.__class__.__name__}: {animal.describe_habitat()}")