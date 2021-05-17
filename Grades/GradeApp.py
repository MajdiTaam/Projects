import mysql.connector
import pandas as pd

db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="grades"
)

def select_menu():
    print("\n MENU")
    print("1. View Students")
    print("2. Add Student")
    print("3. Update Student")
    print("4. Add Course")
    print("5. Add Grade")
    print("6. View Student's Grades")
    print("0. EXIT")
    try:
        action = int(input("> "))
        return action
    except ValueError:
        return -1



#STUDENTS CLASS

class Students:

    def __init__(self, id, fullname, major,  age, employed, native):
        self.student_id = id
        self.fullname = fullname
        self.age = age
        self.employed = employed
        self.native = native
        self.major = major

    def __str__(self):
        return '[ ID: ' + str(self.student_id)  \
              + ' Full Name: ' + str(self.fullname) \
              + ' Age: ' + str(self.age) \
              + ' Major: ' + str(self.major) \
              + ' Employed: ' + str(self.employed) \
              + ' Native: ' + str(self.native) \
              + ' ]'


#STUDENTS ACTION 1

def get_student_object(db_row):
    student = Students(db_row[0], db_row[1], db_row[2], db_row[3], db_row[4], db_row[5])
    return student

def all_students():
    cursor = db.cursor()
    students = {}
    cursor.execute("SELECT * FROM student")
    result = cursor.fetchall()
    for row in result:
        student = get_student_object(row)
        students[student.student_id] = student
    return students

def display_students(student):
    for id in student:
        print(student[id])

# STUDENTS ACTION 2

def add_student():
    fullname = input("Name: ")
    try:
        major = input("Major: ")
        age = int(input("Age: "))
        employed = int(input("Employed ( 1 = employed, 0 = Unemployed) :"))
        native =  int(input("Native ( 1 = native, 0 = non-native) :"))
    except (ValueError):
        print("Wrong value")
        return

    cursor = db.cursor()
    sql = "INSERT INTO student(fullname, major, age, employed, native) VALUES (%s, %s, %s, %s, %s)"
    data = (fullname, major, age, employed, native)
    cursor.execute(sql, data)
    db.commit()

#STUDEN ACTION 3

def update_student():
    id = int(input("ID: "))

    fullname = input("Name: ")

    try:
        major = input("Major: ")
        age = int(input("Age: "))
        employed = int(input("Employed ( 1 = employed, 0 = unemployed) :"))
        native = int(input("Native ( 1 = native, 0 = non-native) :"))
    except (ValueError):
        print("Wrong value")
        return
    cursor = db.cursor()
    sql = "UPDATE student SET fullname=%s, major=%s, age=%s, employed=%s, native=%s WHERE id=%s"
    data = (fullname, major, age, employed, native, id)
    cursor.execute(sql, data)
    db.commit()


#COURSES ACTION 4

def add_course():
    title = input("Title: ")
    try:
        liberal = input("Liberal: ")
        credits = int(input("Credits: "))
    except (ValueError):
        print("Wrong value")
        return

    cursor = db.cursor()
    sql = "INSERT INTO courses(title, liberal, credits) VALUES (%s, %s, %s)"
    data = (title, liberal, credits)
    cursor.execute(sql, data)
    db.commit()

# ADD GRADE ACTION 5

def add_grade():

    try:
        Student_id = int(input("Student ID: "))
        Courses_id = int(input("Courses ID: "))
        Grade = int(input("Grade: "))
    except (ValueError):
        print("Wrong value")
        return
    cursor = db.cursor()
    sql = "INSERT INTO student_has_courses(Student_id, Courses_id, Grade) VALUES (%s, %s, %s)"
    data = (Student_id, Courses_id, Grade)
    cursor.execute(sql, data)
    db.commit()

# VIEW A STUDENT'S GRADE ACTION 6

    def view_students_grades(Student_id):
        cursor = db.cursor()
        students_grades = {}
        cursor.execute("SELECT s.fullname, s.id, co.title, co.id, shc.grade FROM student_has_courses shc LEFT JOIN student s on s.id = shc.Student_id LEFT JOIN courses co on co.id = shc.Courses_id WHERE s.id =" + str(Student_id))
        result = cursor.fetchall()

        for row in result:
            students_grades[row[2]] = row[4]

        return students_grades

def view_students_grades():
    try:
        Student_id = int(input("Student ID"))
    except (ValueError):
        print("Wrong value")
        return
    students_grades = view_students_grades(Student_id)

    for course in students_grades:
        print(course, students_grades[course])

    response = input("Would you like to save the following data in a CSV FIle? Yes/No ")
    if response == "Yes":
        export_student_grades(Student_id)
    elif response == "No":
        pass

# DOWNLOAD AS A CSV FILE

def export_student_grades(Student_id):
    cursor = db.cursor()
    cursor.execute("SELECT s.fullname, s.id, co.title, co.id, shc.grade FROM student_has_courses shc LEFT JOIN student s on s.id = shc.Student_id LEFT JOIN courses co on co.id = shc.Courses_id WHERE s.id =" + str(Student_id))
    result = cursor.fetchall()

    df = pd.DataFrame(result)
    df.columns = ["Full Name", "Student ID", "Course Title", "Course ID", "Grade"]
    df.set_index('Student ID')
    df.to_csv(r'C:\Users\majdi\Desktop\Grades\file.csv', index=False)


if __name__ == '__main__':
    while True:
        action = select_menu()
        if action == 1:
            students = all_students()
            display_students(students)
        elif action == 2:
            add_student()
        elif action == 3:
            update_student()
        elif action == 4:
            add_course()
        elif action == 5:
            add_grade()
        elif action == 6:
            view_students_grades()
        elif action == 0:
            print("Bye!")
            break
        else:
            print("Invalid action")
        input("any key to continue ...")