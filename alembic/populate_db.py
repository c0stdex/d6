import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="your_db_name", 
    user="your_db_user", 
    password="your_db_password", 
    host="your_db_host", 
    port="your_db_port"
)
cur = conn.cursor()

faker = Faker()

# Генерація даних для таблиці 
groups = ['Group 1', 'Group 2', 'Group 3']
for group in groups:
    cur.execute("INSERT INTO groups (name) VALUES (%s)", (group,))

# Генерація даних для таблиці teachers
teachers = []
for _ in range(5):
    first_name = faker.first_name()
    last_name = faker.last_name()
    cur.execute("INSERT INTO teachers (first_name, last_name) VALUES (%s, %s)", (first_name, last_name))
    teachers.append(cur.fetchone()[0])

# Генерація даних для таблиці subjects
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'Literature', 'Art']
for subject in subjects:
    teacher_id = random.choice(teachers)
    cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)", (subject, teacher_id))

# Генерація даних для таблиці students
for _ in range(50):
    first_name = faker.first_name()
    last_name = faker.last_name()
    group_id = random.choice([1, 2, 3])
    cur.execute("INSERT INTO students (first_name, last_name, group_id) VALUES (%s, %s, %s)", (first_name, last_name, group_id))

# Генерація даних для таблиці grades
cur.execute("SELECT id FROM students")
student_ids = [row[0] for row in cur.fetchall()]

cur.execute("SELECT id FROM subjects")
subject_ids = [row[0] for row in cur.fetchall()]

for student_id in student_ids:
    for subject_id in subject_ids:
        for _ in range(random.randint(10, 20)):
            grade = round(random.uniform(2, 12), 2)
            date = faker.date_between(start_date="-1y", end_date="today")
            cur.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (%s, %s, %s, %s)", (student_id, subject_id, grade, date))

# Фіксація змін
conn.commit()
cur.close()
conn.close()
