class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []  # List to store courses student is enrolled in

    def enroll(self, course):
        self.courses.append(course)  # Enroll in a course

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []  # List to store students enrolled in the course

    def add_student(self, student):
        self.students.append(student)  # Add a student to the course

# Create instances (objects) of Student and Course
student1 = Student("John Doe")
student2 = Student("minny")
course1 = Course("Mathematics 101")
course1 = Course("Mathematics 101")

# Create an association: student1 enrolls in course1
student1.enroll(course1)
student2.enroll(course1)

print(f"{student1.name} is enrolled in {student1.courses[0].course_name}")

# Establish bidirectional association
course1.add_student(student1)  # Add student1 to course1
course1.add_student(student2)  # Add student2 to course1
print(f"Students enrolled in {course1.course_name}: {[student.name for student in course1.students]}")


#one object can interact with or reference another object
#In the Student class, the method enroll(self, course) allows a Student object to "link" itself to a Course object 
#by adding that Course object to its courses list. 
#Bidirectional association
#A Student object can reference a Course object by enrolling in it
#A Course object can reference Student objects by adding them to the course 


