students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase

def add_student(name):
    students.append(name)

student_list = get_students_titlecase()

add_student("nico")