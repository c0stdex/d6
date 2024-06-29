from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Group, Teacher, Subject, Student, Grade
from faker import Faker
import random
from datetime import datetime, timedelta

engine = create_engine('postgresql://username:password@localhost/databasename')
Session = sessionmaker(bind=engine)
session = Session()

faker = Faker()

# Наповнення таблиці groups
groups = ['Group 1', 'Group 2', 'Group 3']
for group in groups:
    session.add(Group(name=group))
session.commit()

# Наповнення таблиці teachers
teachers = []
for _ in range(5):
    teacher = Teacher(first_name=faker.first_name(), last_name=faker.last_name())
    session.add(teacher)
    teachers.append(teacher)
session.commit()

# Наповнення таблиці subjects
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'Literature', 'Art']
for subject in subjects:
    session.add(Subject(name=subject, teacher=random.choice(teachers)))
session.commit()

# Наповнення таблиці students
students = []
for _ in range(50):
    student = Student(first_name=faker.first_name(), last_name=faker.last_name(), group_id=random.choice([1, 2, 3]))
    session.add(student)
    students.append(student)
session.commit()

# Наповнення таблиці grades
for student in students:
    for subject in session.query(Subject).all():
        for _ in range(random.randint(10, 20)):
            grade = Grade(student=student, subject=subject, grade=round(random.uniform(2, 12), 2), date=faker.date_between(start_date="-1y", end_date="today"))
            session.add(grade)
session.commit()

session.close()
