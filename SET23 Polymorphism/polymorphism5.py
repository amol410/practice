# Implement a base class "Fruit" with a method to describe taste. Create derived classes "Apple" and "Banana" that provide their own taste descriptions.

# Base class
class Fruit:
    def describe_taste(self):
        raise NotImplementedError("Subclass must implement this method.")

# Derived class for Apple
class Apple(Fruit):
    def describe_taste(self):
        return "Apples are generally sweet with a hint of tartness."

# Derived class for Banana
class Banana(Fruit):
    def describe_taste(self):
        return "Bananas have a sweet and creamy taste when ripe."

# Example usage
apple = Apple()
banana = Banana()

print(f"Apple taste: {apple.describe_taste()}")    # Output: Apples are generally sweet with a hint of tartness.
print(f"Banana taste: {banana.describe_taste()}")  # Output: Bananas have a sweet and creamy taste when ripe.
