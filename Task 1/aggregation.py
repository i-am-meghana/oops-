class Student:
    def __init__(self, name):
        self.name = name

class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.students = []  # List of students who use this library
    
    def add_student(self, student):
        self.students.append(student)  # Add a student to the library
    
    def list_students(self):
        print(f"Students who visit {self.library_name}:")
        for student in self.students:
            print(student.name)

# Create instances (objects)
student1 = Student("John Doe")
student2 = Student("Jane Smith")
library = Library("Central Library")

# Aggregation: Library has students
library.add_student(student1)
library.add_student(student2)

# Print out the students in the library
library.list_students()

# If the library is destroyed, students still exist
print(f"{student1.name} and {student2.name} still exist, even without the library.")

#In the code:
#library.add_student(student1) and library.add_student(student2) add students to the library.
# Even if the library object is removed, the student1 and student2 objects still exist.