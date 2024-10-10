# Implement a base class "Animal" with a method to make a sound. Create derived classes "Dog" and "Cat" that override the sound method.


# Base class
class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclass must implement this method.")

# Derived class for Dog
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

# Derived class for Cat
class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"

# Example usage
dog = Dog()
cat = Cat()

print(f"Dog sound: {dog.make_sound()}")  # Output: Woof! Woof!
print(f"Cat sound: {cat.make_sound()}")  # Output: Meow! Meow!
