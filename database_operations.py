from sqlalchemy.orm import sessionmaker
from database_models import Base, Group, Student, Lecturer, Subject, Grades
from connect_database import create_database_engine

engine = create_database_engine()
DBSession = sessionmaker(bind=engine)
session = DBSession()


def create_group(group_name):
    new_group = Group(group_name=group_name)
    session.add(new_group)
    session.commit()


def list_groups():
    groups = session.query(Group).all()
    for group in groups:
        print(f"Group ID: {group.id}, Group Name: {group.group_name}")


def update_group(group_id, new_group_name):
    group = session.query(Group).filter_by(id=group_id).first()
    if group:
        group.group_name = new_group_name
        session.commit()
    else:
        print(f"Group with ID {group_id} not found.")


def remove_group(group_id):
    group = session.query(Group).filter_by(id=group_id).first()
    if group:
        session.delete(group)
        session.commit()
    else:
        print(f"Group with ID {group_id} not found.")


def create_student(name, last_name, group_id):
    new_student = Student(name=name, last_name=last_name, group_id=group_id)
    session.add(new_student)
    session.commit()


def list_students():
    students = session.query(Student).all()
    for student in students:
        print(f"Student ID: {student.id}, Name: {student.name}, Last Name: {student.last_name}, Group ID: {student.group_id}")


def update_student(student_id, new_name, new_last_name, new_group_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        student.name = new_name
        student.last_name = new_last_name
        student.group_id = new_group_id
        session.commit()
    else:
        print(f"Student with ID {student_id} not found.")


def remove_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
    else:
        print(f"Student with ID {student_id} not found.")


def create_lecturer(name, last_name):
    new_lecturer = Lecturer(name=name, last_name=last_name)
    session.add(new_lecturer)
    session.commit()


def list_lecturers():
    lecturers = session.query(Lecturer).all()
    for lecturer in lecturers:
        print(f"Lecturer ID: {lecturer.id}, Name: {lecturer.name}, Last Name: {lecturer.last_name}")


def update_lecturer(lecturer_id, new_name, new_last_name):
    lecturer = session.query(Lecturer).filter_by(id=lecturer_id).first()
    if lecturer:
        lecturer.name = new_name
        lecturer.last_name = new_last_name
        session.commit()
    else:
        print(f"Lecturer with ID {lecturer_id} not found.")


def remove_lecturer(lecturer_id):
    lecturer = session.query(Lecturer).filter_by(id=lecturer_id).first()
    if lecturer:
        session.delete(lecturer)
        session.commit()
    else:
        print(f"Lecturer with ID {lecturer_id} not found.")


def create_subject(name, lecturer_id):
    new_subject = Subject(name=name, lecturer_id=lecturer_id)
    session.add(new_subject)
    session.commit()


def list_subjects():
    subjects = session.query(Subject).all()
    for subject in subjects:
        print(f"Subject ID: {subject.id}, Name: {subject.name}, Lecturer ID: {subject.lecturer_id}")


def update_subject(subject_id, new_name, new_lecturer_id):
    subject = session.query(Subject).filter_by(id=subject_id).first()
    if subject:
        subject.name = new_name
        subject.lecturer_id = new_lecturer_id
        session.commit()
    else:
        print(f"Subject with ID {subject_id} not found.")


def remove_subject(subject_id):
    subject = session.query(Subject).filter_by(id=subject_id).first()
    if subject:
        session.delete(subject)
        session.commit()
    else:
        print(f"Subject with ID {subject_id} not found.")


def create_grade(student_id, subject_id, mark, exam_date):
    new_grade = Grades(student_id=student_id, subj_id=subject_id, mark=mark, exam_date=exam_date)
    session.add(new_grade)
    session.commit()
    print("Grade created successfully.")


def list_grades():
    grades = session.query(Grades).all()
    for grade in grades:
        print(f"Grade ID: {grade.id}, Student ID: {grade.student_id}, Subject ID: {grade.subj_id}, Mark: {grade.mark}, Exam Date: {grade.exam_date}")


def update_grade(grade_id, new_student_id, new_subject_id, new_mark, new_exam_date):
    grade = session.query(Grades).filter_by(id=grade_id).first()
    if grade:
        grade.student_id = new_student_id
        grade.subj_id = new_subject_id
        grade.mark = new_mark
        grade.exam_date = new_exam_date
        session.commit()
        print("Grade updated successfully.")
    else:
        print(f"Grade with ID {grade_id} not found.")


def remove_grade(grade_id):
    grade = session.query(Grades).filter_by(id=grade_id).first()
    if grade:
        session.delete(grade)
        session.commit()
    else:
        print(f"Grade with ID {grade_id} not found.")


def close_session():
    session.close()
    print("Database session closed.")