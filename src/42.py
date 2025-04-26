class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Course:
    def __init__(self, title, teacher, subjects):
        self.title = title
        self.teacher = teacher
        self.subjects = subjects

def register_student(student):
    student.set_age(20)  # Register a new student with default age of 20

students = [Student("Tom", 15), Student("Jerry", 16)]
courses = [
    Course("Math", "Mr. Smith", ["Algebra", "Geometry"]),
    Course("Science", "Ms. Jones", ["Physics", "Chemistry"]),
    Course("English", "Dr. Johnson", ["Reading", "Writing"])
]

for course in courses:
    for student in students:
        if student.age == 20 and (course.title, course.teacher) in course.subjects:
            print(f"{student.name} registered for {course.title} with Mr. Smith.")
