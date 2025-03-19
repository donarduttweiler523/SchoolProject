
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def print_student_info(self):
        print("Student Name:", self.name)
        print("Grade:", self.grade)

student1 = Student("Alice", 90)
student1.print_student_info()

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def print_teacher_info(self):
        print("Teacher Name:", self.name)
        print("Subject:", self.subject)

teacher1 = Teacher("Ms. Johnson", "Math")
teacher1.print_teacher_info()

class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students

    def print_school_info(self):
        print("School Name:", self.name)
        for student in self.students:
            student.print_student_info()

school1 = School("Acme Elementary", [student1])
school1.print_school_info()

class GradeBook:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, student, grade):
        if student in self.grades:
            self.grades[student].append(grade)
        else:
            self.grades[student] = [grade]

    def print_grade_book(self):
        print("Grade Book Name:", self.name)
        for student, grades in self.grades.items():
            print("Student Name:", student)
            print("Grades:")
            for grade in grades:
                print(grade)

gradebook1 = GradeBook("Math Grade Book")
gradebook1.add_grade(student1, 90)
gradebook1.print_grade_book()