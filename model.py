from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Create the database engine
engine = create_engine("sqlite:///instance/unireq.db")

# Create a base class for declarative models
Base = declarative_base()


# Define the Country model
class Country(Base):
    __tablename__ = "countries"
    country_id = Column(Integer, primary_key=True)
    name = Column(String)


# Define the University model
class University(Base):
    __tablename__ = "universities"
    university_id = Column(Integer, primary_key=True)
    name = Column(String)
    country_id = Column(Integer, ForeignKey("countries.country_id"))
    country = relationship("Country")


# Define the Course model
class Course(Base):
    __tablename__ = "courses"
    course_id = Column(Integer, primary_key=True)
    name = Column(String)
    university_id = Column(Integer, ForeignKey("universities.university_id"))
    university = relationship("University")


# Define the AdmissionCriteria model
class AdmissionCriteria(Base):
    __tablename__ = "admission_criteria"
    admission_criteria_id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.course_id"))
    IB_score = Column(String)
    subject_requirements = Column(String)
    language_proficiency = Column(String)
    course = relationship("Course")


# Define the User model
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)


# Define the Score model
class Score(Base):
    __tablename__ = "scores"
    score_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    course_id = Column(Integer, ForeignKey("courses.course_id"))
    score = Column(Integer)
    user = relationship("User")
    course = relationship("Course")


# Define the Feedback model
class Feedback(Base):
    __tablename__ = "feedback"
    feedback_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    admission_criteria_id = Column(
        Integer, ForeignKey("admission_criteria.admission_criteria_id")
    )
    comment = Column(String)
    user = relationship("User")
    admission_criteria = relationship("AdmissionCriteria")


# Create the tables in the database
Base.metadata.create_all(engine)
