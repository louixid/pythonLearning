#!env/bin/active ipython

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:@localhost/shiyanlou')

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    email = Column(String(64))
    def __repr__(self):
        return 'User<name=%s>' % self.name

class Course(Base):
    __tablename__='course'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    teacher_id = Column(Integer,ForeignKey('user.id')) #
    teacher = relationship('User')
    def __repr__(self):
        return '<Course(name=%s)>' % self.name

class Lab(Base):
    __tablename__='lab'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    course = relationship('Course', backref='labs')
    course_id = Column(Integer, ForeignKey('course.id'))
    def __repr__(self):
        return '<Lab(name=%s)>' % self.name

class Path(Base):
    __tablename__ = 'path'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    config = Column(String(128))
    def __repr__(self):
        return '<Path(name=%s)>' % self.name

Base.metadata.create_all(engine)

course = session.query(Course).first()

lab1 = Lab(name='ORM jichu', course_id=course.id)
lab2 = Lab(name='guanxi database', course=course)

session.add(lab1)
session.add(lab2)
session.commit()

course.labs

