import random
import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="grades"
)

cursor = db.cursor()

for _ in range(20):
    sql = "INSERT INTO student_has_courses(Student_id, Courses_id, Grade) VALUES (%s, %s, %s)"
    Student_id = random.randint(1,20)
    Courses_id = random.randint(1, 20)
    Grade = random.randint(0, 100)
    data = (Student_id, Courses_id, Grade)
    cursor.execute(sql, data)


db.commit()
