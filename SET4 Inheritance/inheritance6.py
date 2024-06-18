class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Apple(Fruit):
    def __init__(self, name, color, taste, vitamin_c):
        super().__init__(name, color)
        self.taste = taste
        self.vitamin_c = vitamin_c

class Banana(Fruit):
    def __init__(self, name, color, taste, vitamin_b6):
        super().__init__(name, color)
        self.taste = taste
        self.vitamin_b6 = vitamin_b6


apple = Apple("Gala", "red", "sweet", 10)
print(apple.name)     # Output: Gala
print(apple.color)    # Output: red
print(apple.taste)    # Output: sweet
print(apple.vitamin_c)  # Output: 10

banana = Banana("Cavendish", "yellow", "sweet", 0.5)
print(banana.name)     # Output: Cavendish
print(banana.color)    # Output: yellow
print(banana.taste)    # Output: sweet
print(banana.vitamin_b6)  # Output: 0.5        