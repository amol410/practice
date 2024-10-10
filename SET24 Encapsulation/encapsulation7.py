# Create a class "Book" with private attributes for title, author, and publication year. Implement methods to encapsulate these attributes.

class Book:
    def __init__(self, title, author, publication_year):
        self.__title = title            # Private attribute for title
        self.__author = author          # Private attribute for author
        self.__publication_year = publication_year  # Private attribute for publication year

    # Getter method for title
    def get_title(self):
        return self.__title

    # Setter method for title
    def set_title(self, title):
        self.__title = title

    # Getter method for author
    def get_author(self):
        return self.__author

    # Setter method for author
    def set_author(self, author):
        self.__author = author

    # Getter method for publication year
    def get_publication_year(self):
        return self.__publication_year

    # Setter method for publication year
    def set_publication_year(self, publication_year):
        self.__publication_year = publication_year

    # Method to display book information
    def display_info(self):
        return f"Title: {self.__title}, Author: {self.__author}, Publication Year: {self.__publication_year}"

# Example usage
book = Book("1984", "George Orwell", 1949)

# Accessing attributes using getter methods
print(book.display_info())  # Output: Title: 1984, Author: George Orwell, Publication Year: 1949

# Updating attributes using setter methods
book.set_title("Animal Farm")
book.set_author("George Orwell")
book.set_publication_year(1945)

# Display updated book information
print(book.display_info())  # Output: Title: Animal Farm, Author: George Orwell, Publication Year: 1945
