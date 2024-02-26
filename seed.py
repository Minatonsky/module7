from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_models import Base, Group, Student, Lecturer, Subject, Grades
from faker import Faker
from random import randint, choice

num_students = 50
num_lecturers = 5
num_groups = 3
num_subjects = 7
num_grades = 20 * num_students
subjects_name = ['Computer Science', 'Physics', 'History', 'Mathematics', 'Chemistry', 'Biology', 'Literature']

fake = Faker()

engine = create_engine('postgresql://postgres:testtest@127.0.0.1:5432/univerdb')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

groups = [Group(group_name=f"Group-{i + 1}") for i in range(num_groups)]
session.add_all(groups)
session.commit()

students = [Student(name=fake.first_name(), last_name=fake.last_name(), group_id=randint(1, 3)) for _ in range(num_students)]
session.add_all(students)
session.commit()

lecturers = [Lecturer(name=fake.first_name(), last_name=fake.last_name()) for _ in range(num_lecturers)]
session.add_all(lecturers)
session.commit()

subjects = [Subject(name=choice(subjects_name), lecturer_id=randint(1, num_lecturers)) for _ in range(num_subjects)]
session.add_all(subjects)
session.commit()

grades = [Grades(student_id=randint(1, num_students), subj_id=randint(1, num_subjects), mark=randint(1, 12), exam_date=fake.date_time()) for _ in range(num_grades)]
session.add_all(grades)
session.commit()
