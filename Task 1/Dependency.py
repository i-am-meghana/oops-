class Library:
    def __init__(self):
        # A list of books available in the library
        self.books = ["Python Programming", "Data Science 101", "Machine Learning Basics"]

    def lend_book(self, book_name):
        if book_name in self.books:
            print(f"Lending the book '{book_name}'...")
            self.books.remove(book_name)
        else:
            print(f"Sorry, '{book_name}' is not available in the library.")

    def return_book(self, book_name):
        print(f"Returning the book '{book_name}' to the library...")
        self.books.append(book_name)


class Student:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, library: Library, book_name):
        print(f"{self.name} is trying to borrow the book '{book_name}'")
        library.lend_book(book_name)
        self.borrowed_books.append(book_name)

#the Student class depends on the Library class to perform certain actions,to borrow and return books
    def return_book(self, library: Library, book_name):
        print(f"{self.name} is returning the book '{book_name}'")
        library.return_book(book_name)
        self.borrowed_books.remove(book_name)


# Create an instance of the Library
library = Library()

# Create an instance of the Student
student = Student("John")

# The student borrows and returns books, interacting with the library 
student.borrow_book(library, "Python Programming")
student.borrow_book(library, "Machine Learning Basics")

# Print the list of borrowed books
print(f"{student.name} borrowed books: {student.borrowed_books}")

# Now, the student returns a book
student.return_book(library, "Python Programming")

# Print the list of borrowed books after returning a book
print(f"{student.name} borrowed books after returning: {student.borrowed_books}")

#If the Library class is modified (e.g., if the lend_book method is changed to check for overdue books), 
#the Student class might need to be updated accordingly to handle the new behavior.