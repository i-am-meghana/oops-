class Library:
    def __init__(self):
        # Initialize the list of books in the library
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

    def show_books(self):
        print("Books available in the library:", self.books)


class Student:
    def __init__(self, name):
        self.name = name
        # A Student *owns* their Library, which is created here
        self.library = Library()  # Composition: the student has a library

    def borrow_book(self, book_name):
        print(f"{self.name} is trying to borrow the book '{book_name}'")
        self.library.lend_book(book_name)

    def return_book(self, book_name):
        print(f"{self.name} is returning the book '{book_name}'")
        self.library.return_book(book_name)

    def show_library_books(self):
        self.library.show_books()


# Creating an instance of Student
student = Student("John")

# The student borrows and returns books from their own library
student.show_library_books()  # Show available books in the student's library
student.borrow_book("Python Programming")
student.show_library_books()  # Show available books after borrowing
student.return_book("Python Programming")
student.show_library_books()  # Show available books after returning

#The Student class contains a Library object, meaning that every Student has their own Library