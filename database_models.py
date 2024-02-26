from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String(50), unique=True, nullable=False)


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)
    grades = relationship('Grades', back_populates='student')


class Lecturer(Base):
    __tablename__ = 'lecturers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    subjects = relationship('Subject', back_populates='lecturer')


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    lecturer_id = Column(Integer, ForeignKey('lecturers.id'), nullable=False)
    grades = relationship('Grades', back_populates='subject')
    lecturer = relationship('Lecturer', back_populates='subjects')


class Grades(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    subj_id = Column(Integer, ForeignKey('subjects.id'), nullable=False)
    mark = Column(Integer, nullable=True)
    exam_date = Column(DateTime, nullable=True)

    student = relationship('Student', back_populates='grades')
    subject = relationship('Subject', back_populates='grades')
