class Book:
    def __init__(self, title, author, isbn, year, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.available = available

    def __repr__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def borrow(self):
        if not self.available:
            print("Sorry, this book is already borrowed.")
        else:
            self.available = False
            print(f"{self.title} has been borrowed.")

    def return_book(self):
        self.available = True
        print(f"Thank you for returning {self.title}.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_books(self, search_term):
        results = []
        for book in self.books:
            if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower():
                results.append(book)
        return results
      
"""
Here we create a book objects and add them to the library object. 
You can also search for books by title or author and borrow or return books that are in the library. 
Here's an example usage:
"""
# create some book objects
book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "978-0747532743", 1997)
book2 = Book("The Hobbit", "J.R.R. Tolkien", "978-0261102217", 1937)
book3 = Book("1984", "George Orwell", "978-0141036144", 1949)

# create a library object
library = Library()

# add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# search for books by title or author
results = library.search_books("harry potter")
print(results)

# borrow a book
book1.borrow()

# try to borrow a book that's already borrowed
book2.borrow()

# return a book
book1.return_book()
