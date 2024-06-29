from sqlalchemy import create_engine, func, desc
from sqlalchemy.orm import sessionmaker
from models import Group, Teacher, Subject, Student, Grade

engine = create_engine('postgresql://username:password@localhost/databasename')
Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    return session.query(
        Student.first_name, Student.last_name, func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

def select_2(subject_name):
    return session.query(
        Student.first_name, Student.last_name, func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade).join(Subject).filter(Subject.name == subject_name).group_by(Student.id).order_by(desc('avg_grade')).limit(1).all()

def select_3(subject_name):
    return session.query(
        Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Student).join(Grade).join(Subject).filter(Subject.name == subject_name).group_by(Group.id).all()

def select_4():
    return session.query(func.round(func.avg(Grade.grade), 2)).scalar()

def select_5(teacher_id):
    return session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()

def select_6(group_id):
    return session.query(Student.first_name, Student.last_name).filter(Student.group_id == group_id).all()

def select_7(group_id, subject_name):
    return session.query(
        Student.first_name, Student.last_name, Grade.grade
    ).join(Student).join(Subject).filter(Student.group_id == group_id, Subject.name == subject_name).all()

def select_8(teacher_id):
    return session.query(
        func.round(func.avg(Grade.grade), 2)
    ).join(Subject).filter(Subject.teacher_id == teacher_id).scalar()

def select_9(student_id):
    return session.query(Subject.name).join(Grade).filter(Grade.student_id == student_id).group_by(Subject.id).all()

def select_10(student_id, teacher_id):
    return session.query(Subject.name).join(Grade).filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id).group_by(Subject.id).all()

def select_11(student_id, teacher_id):
    return session.query(
        func.round(func.avg(Grade.grade), 2)
    ).join(Subject).filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id).scalar()

def select_12(group_id, subject_name):
    subquery = session.query(
        func.max(Grade.date).label('last_date')
    ).join(Student).filter(Student.group_id == group_id).join(Subject).filter(Subject.name == subject_name).scalar_subquery()
    
    return session.query(
        Student.first_name, Student.last_name, Grade.grade
    ).join(Student).join(Subject).filter(Student.group_id == group_id, Subject.name == subject_name, Grade.date == subquery).all()

session.close()
