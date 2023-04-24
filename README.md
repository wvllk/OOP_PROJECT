# OOP_PROJECT
The program is built using two classes, Book and Library, that work together to represent a digital library system.

The Book class represents a book object with attributes like title, author, isbn, year, and available. It also has two methods: borrow() and return_book(). These methods allow users to borrow and return books from the library by changing the value of the available attribute. The __repr__() method is also defined, which returns a string representation of the book object.

The Library class represents the collection of books in the library. It has an attribute books that is a list of Book objects. It also has methods like add_book(), remove_book(), and search_books(). These methods allow users to add and remove books from the library, and search for books by title or author.

The program follows the fundamental principles of object-oriented programming. Each class has a clear responsibility and encapsulates its own data and behavior. The Book class is responsible for representing a book object and managing its state, while the Library class is responsible for managing the collection of books and providing search functionality. The program also uses inheritance, as the Library class inherits from the Book class.
