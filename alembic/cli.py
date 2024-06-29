import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic.models import Base, Group, Teacher, Subject, Student, Grade

engine = create_engine('postgresql://username:password@localhost/databasename')
Session = sessionmaker(bind=engine)
session = Session()

def create_teacher(name):
    first_name, last_name = name.split(' ')
    teacher = Teacher(first_name=first_name, last_name=last_name)
    session.add(teacher)
    session.commit()

def list_teachers():
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        print(f'{teacher.id}: {teacher.first_name} {teacher.last_name}')

def update_teacher(id, name):
    teacher = session.query(Teacher).get(id)
    if teacher:
        first_name, last_name = name.split(' ')
        teacher.first_name = first_name
        teacher.last_name = last_name
        session.commit()

def remove_teacher(id):
    teacher = session.query(Teacher).get(id)
    if teacher:
        session.delete(teacher)
        session.commit()

# Add similar functions for Group, Subject, Student, Grade

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', '-a', required=True, choices=['create', 'list', 'update', 'remove'])
    parser.add_argument('--model', '-m', required=True, choices=['Teacher', 'Group', 'Subject', 'Student', 'Grade'])
    parser.add_argument('--id', type=int)
    parser.add_argument('--name', type=str)

    args = parser.parse_args()

    if args.model == 'Teacher':
        if args.action == 'create' and args.name:
            create_teacher(args.name)
        elif args.action == 'list':
            list_teachers()
        elif args.action == 'update' and args.id and args.name:
            update_teacher(args.id, args.name)
        elif args.action == 'remove' and args.id:
            remove_teacher(args.id)

    # Add similar conditionals for Group, Subject, Student, Grade

    session.close()
