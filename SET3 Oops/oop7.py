# Create a Python class for a "Book" with attributes for title, author, and publication year. 
# Implement a method to display the book's details.

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
    
    def display_details(self):
        print("Book Details:")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")

# Example usage
book1 = Book("Pride and Prejudice", "Jane Austen", 1813)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

book1.display_details()
print()
book2.display_details()