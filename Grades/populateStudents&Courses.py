import random
import mysql.connector
from faker import *



db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="grades"
)

majors = ['Education', 'Engineering']
courses = {
    'Education': ['English', 'Math', 'History'],
    'Engineering': ['Programming', 'Calculus', 'Thesis']
}
cursor = db.cursor()
dummy_data = Faker()

y = 0

for y in range(20):


    sql = "INSERT INTO student(fullname, major, age, employed, native) VALUES (%s, %s, %s, %s, %s)"
    employed = random.randint(0,1)
    native = random.randint(0,1)
    x = random.randint(0,1)
    age = random.randint(17, 30)
    major = majors[x]
    data = (dummy_data.name(), major, age, employed, native)
    cursor.execute(sql, data)

    sq = "INSERT INTO courses(title, liberal, credits) VALUES (%s, %s, %s)"
    liberal = random.randint(0, 1)
    credits = random.randint(1, 4)
    number = random.randint(0, 2)
    title = courses[major][number]
    dat = (title, liberal, credits)
    cursor.execute(sq, dat)

db.commit()