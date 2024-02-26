from sqlalchemy import create_engine, func, desc
from sqlalchemy.orm import sessionmaker, Session
from database_models import Student, Grades, Base, Subject, Group, Lecturer

engine = create_engine('postgresql://postgres:testtest@127.0.0.1:5432/univerdb')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def select_1(session: Session):
    query = (
        session.query(
            Student.id,
            Student.name,
            Student.last_name,
            func.round(func.avg(Grades.mark), 2).label('avg_mark')
        )
        .join(Grades, Grades.student_id == Student.id)
        .group_by(Student.id)
        .order_by(desc('avg_mark'))
        .limit(5)
    )

    result = query.all()

    for row in result:
        print(row)


def select_2(session: Session, subject_name: str):
    query = (
        session.query(
            Student.id,
            Student.name,
            Student.last_name,
            func.round(func.avg(Grades.mark), 2).label('avg_mark'),
            Subject.name.label('subject')
        )
        .join(Grades, Grades.student_id == Student.id)
        .join(Subject, Subject.id == Grades.subj_id)
        .filter(Subject.name == subject_name)
        .group_by(Student.id, Subject.name)
        .order_by(desc('avg_mark'))
        .limit(1)
    )

    result = query.all()

    for row in result:
        print(row)


def select_3(session: Session, subject_name: str):
    query = (
        session.query(
            Group.group_name,
            func.round(func.avg(Grades.mark), 2).label('avg_mark'),
            Subject.name.label('subj_name')
        )
        .join(Student, Student.group_id == Group.id)
        .join(Grades, Grades.student_id == Student.id)
        .join(Subject, Subject.id == Grades.subj_id)
        .filter(Subject.name == subject_name)
        .group_by(Group.id, Subject.id)
        .order_by(Group.group_name, desc('avg_mark'))
    )

    result = query.all()

    for row in result:
        print(row)


def select_4(session: Session):
    query = (
        session.query(
            Subject.name,
            func.round(func.avg(Grades.mark), 2).label('avg_mark')
        )
        .join(Grades, Grades.subj_id == Subject.id)
        .group_by(Subject.name)
    )

    result = query.all()

    for row in result:
        print(row)


def select_5(session: Session, lecturer_name: str, lecturer_last_name: str):
    query = (
        session.query(
            Lecturer.name,
            Lecturer.last_name,
            Subject.name.label('subj')
        )
        .join(Subject, Subject.lecturer_id == Lecturer.id)
        .filter(Lecturer.name == lecturer_name)
        .filter(Lecturer.last_name == lecturer_last_name)
    )

    result = query.all()

    for row in result:
        print(row)


def select_6(session: Session, group_name: str):
    query = (
        session.query(
            Group.group_name,
            Student.name,
            Student.last_name
        )
        .join(Group, Group.id == Student.group_id)
        .filter(Group.group_name == group_name)
    )

    result = query.all()

    for row in result:
        print(row)


def select_7(session: Session, group_name: str, subject_name: str):
    query = (
        session.query(
            Student.name,
            Student.last_name,
            Subject.name,
            Grades.mark
        )
        .join(Group, Group.id == Student.group_id)
        .join(Grades, Grades.student_id == Student.id)
        .join(Subject, Subject.id == Grades.subj_id)
        .filter(Group.group_name == group_name, Subject.name == subject_name)
    )

    result = query.all()

    for row in result:
        print(row)


def select_8(session: Session, lecturer_name: str, lecturer_last_name: str):
    query = (
        session.query(
            Lecturer.name,
            Lecturer.last_name,
            func.round(func.avg(Grades.mark), 2).label('average_mark')
        )
        .join(Subject, Subject.lecturer_id == Lecturer.id)
        .join(Grades, Grades.subj_id == Subject.id)
        .filter(Lecturer.name == lecturer_name, Lecturer.last_name == lecturer_last_name)
        .group_by(Lecturer.id)
    )

    result = query.all()

    for row in result:
        print(row)


def select_9(session: Session, student_name: str, student_last_name: str):
    query = (
        session.query(
            Student.name,
            Student.last_name,
            Subject.name.label('subject_name')
        )
        .join(Grades, Grades.student_id == Student.id)
        .join(Subject, Subject.id == Grades.subj_id)
        .filter(Student.name == student_name, Student.last_name == student_last_name)
        .group_by(Student.id, Subject.name)
    )

    result = query.all()

    for row in result:
        print(row)


def select_10(session: Session, student_name: str, student_last_name: str, lecturer_name: str, lecturer_last_name: str):
    query = (
        session.query(
            Subject.name.label('subj_name'),
            Student.name.label('student_name'),
            Student.last_name.label('student_last_name'),
            Lecturer.name.label('lecturer_name'),
            Lecturer.last_name.label('lecturer_last_name')
        )
        .join(Grades, Grades.student_id == Student.id)
        .join(Subject, Subject.id == Grades.subj_id)
        .join(Lecturer, Lecturer.id == Subject.lecturer_id)
        .filter(Student.name == student_name, Student.last_name == student_last_name, Lecturer.name == lecturer_name,
                Lecturer.last_name == lecturer_last_name)
        .group_by(Student.id, Subject.name, Lecturer.name, Lecturer.last_name)
    )

    result = query.all()

    for row in result:
        print(row)


select_1(session)
select_2(session, 'Computer Science')
select_3(session, 'Computer Science')
select_4(session)
select_5(session, 'Kevin', 'Peters')
select_6(session, 'Group-2')
select_7(session, 'Group-1', 'Literature')
select_8(session, 'Kevin', 'Peters')
select_9(session, 'Mary', 'Lopez')
select_10(session, 'Mary', 'Lopez', 'Kevin', 'Peters')
