# Define a class "Person" with private attributes for name and age. Implement methods to change the name and age while encapsulating these attributes.

class Person:
    def __init__(self, name, age):
        self.__name = self.__validate_name(name)
        self.__age = self.__validate_age(age)

    def __validate_name(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Name must be a non-empty string")
        return name.strip()

    def __validate_age(self, age):
        if not isinstance(age, int) or age < 0 or age > 150:
            raise ValueError("Age must be a positive integer less than or equal to 150")
        return age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = self.__validate_name(name)

    def set_age(self, age):
        self.__age = self.__validate_age(age)

    def have_birthday(self):
        self.__age += 1
        return f"Happy Birthday! {self.__name} is now {self.__age} years old."

    def get_info(self):
        return f"Person(name='{self.__name}', age={self.__age})"

# Usage example
if __name__ == "__main__":
    try:
        # Create a person
        person = Person("Alice", 30)
        print(person.get_info())

        # Change name and age
        person.set_name("Alicia")
        person.set_age(31)
        print(person.get_info())

        # Celebrate a birthday
        print(person.have_birthday())

        # Attempt to set invalid name and age
        try:
            person.set_name("")  # This will raise a ValueError
        except ValueError as e:
            print(f"Error setting name: {e}")

        try:
            person.set_age(200)  # This will raise a ValueError
        except ValueError as e:
            print(f"Error setting age: {e}")

        # Demonstrate encapsulation
        try:
            print(person.__name)  # This will raise an AttributeError
        except AttributeError as e:
            print(f"Error accessing private attribute: {e}")

        # Attempting to modify private attribute directly (creates a new attribute)
        person.__age = 25
        print(person.get_info())  # The actual age remains unchanged

    except ValueError as e:
        print(f"Error creating person: {e}")