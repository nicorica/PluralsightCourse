students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    print(students_titlecase)

def add_student(name):
    students.append(name)

add_student("Nico")

student_list = get_students_titlecase()