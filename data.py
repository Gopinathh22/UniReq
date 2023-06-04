from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Country, University, Course, AdmissionCriteria, User, Score, Feedback

# Create the database engine
engine = create_engine("sqlite:///instance/unireq.db")

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

# Create and add countries
country1 = Country(name="Austria")
country2 = Country(name="Germany")
session.add_all([country1, country2])
session.commit()

# Create and add 5 universities of each country
university1 = University(name="IMC Krems", country_id=country1.country_id)
university2 = University(name="University of Vienna", country_id=country1.country_id)
university3 = University(name="University of Salzburg", country_id=country1.country_id)
university4 = University(name="University of Graz", country_id=country1.country_id)
university5 = University(name="University of Innsbruck", country_id=country1.country_id)
university6 = University(name="University of Munich", country_id=country2.country_id)
university7 = University(
    name="University of Heidelberg", country_id=country2.country_id
)
university8 = University(name="University of Freiburg", country_id=country2.country_id)
university9 = University(name="University of Tübingen", country_id=country2.country_id)
university10 = University(
    name="University of Göttingen", country_id=country2.country_id
)

session.add_all(
    [
        university1,
        university2,
        university3,
        university4,
        university5,
        university6,
        university7,
        university8,
        university9,
        university10,
    ]
)
session.commit()

# Create and add courses
course1 = Course(name="Informatics", university_id=university1.university_id)
course2 = Course(name="Informatics", university_id=university2.university_id)
course3 = Course(name="Informatics", university_id=university3.university_id)
course4 = Course(name="Informatics", university_id=university4.university_id)
course5 = Course(name="Informatics", university_id=university5.university_id)
course6 = Course(name="Informatics", university_id=university6.university_id)
course7 = Course(name="Informatics", university_id=university7.university_id)
course8 = Course(name="Informatics", university_id=university8.university_id)
course9 = Course(name="Informatics", university_id=university9.university_id)
course10 = Course(name="Informatics", university_id=university10.university_id)
course11 = Course(name="Chemistry", university_id=university1.university_id)
course12 = Course(name="Chemistry", university_id=university2.university_id)
course13 = Course(name="Chemistry", university_id=university3.university_id)
course14 = Course(name="Chemistry", university_id=university4.university_id)
course15 = Course(name="Chemistry", university_id=university5.university_id)
course16 = Course(name="Chemistry", university_id=university6.university_id)
course17 = Course(name="Chemistry", university_id=university7.university_id)
course18 = Course(name="Chemistry", university_id=university8.university_id)
course19 = Course(name="Chemistry", university_id=university9.university_id)
course20 = Course(name="Chemistry", university_id=university10.university_id)

session.add_all(
    [
        course1,
        course2,
        course3,
        course4,
        course5,
        course6,
        course7,
        course8,
        course9,
        course10,
        course11,
        course12,
        course13,
        course14,
        course15,
        course16,
        course17,
        course18,
        course19,
        course20,
    ]
)
session.commit()

# Create and add admission criteria for IB students and their grades


admission_criteria1 = AdmissionCriteria(
    course_id=course1.course_id,
    IB_score=0,
    subject_requirements=None,
    language_proficiency="English",
)

admission_criteria2 = AdmissionCriteria(
    course_id=course2.course_id,
    IB_score=28,
    subject_requirements="Mathematics, German",
    language_proficiency="German",
)

admission_criteria3 = AdmissionCriteria(
    course_id=course3.course_id,
    IB_score=30,
    subject_requirements="Mathematics, English",
    language_proficiency="English",
)

admission_criteria4 = AdmissionCriteria(
    course_id=course4.course_id,
    IB_score=32,
    subject_requirements="Mathematics, English",
    language_proficiency="German",
)

admission_criteria5 = AdmissionCriteria(
    course_id=course5.course_id,
    IB_score=34,
    subject_requirements="Mathematics, English",
    language_proficiency="German",
)

admission_criteria6 = AdmissionCriteria(
    course_id=course6.course_id,
    IB_score=36,
    subject_requirements="Mathematics, English",
    language_proficiency="English",
)

admission_criteria7 = AdmissionCriteria(
    course_id=course7.course_id,
    IB_score=38,
    subject_requirements="Mathematics, English",
    language_proficiency="German",
)

admission_criteria8 = AdmissionCriteria(
    course_id=course8.course_id,
    IB_score=40,
    subject_requirements="Mathematics, German",
    language_proficiency="German",
)

admission_criteria9 = AdmissionCriteria(
    course_id=course9.course_id,
    IB_score=42,
    subject_requirements="German",
    language_proficiency="German",
)

admission_criteria10 = AdmissionCriteria(
    course_id=course10.course_id,
    IB_score=44,
    subject_requirements="German, English",
    language_proficiency="English",
)

admission_criteria11 = AdmissionCriteria(
    course_id=course11.course_id,
    IB_score=0,
    subject_requirements=None,
    language_proficiency="English",
)

admission_criteria12 = AdmissionCriteria(
    course_id=course12.course_id,
    IB_score=28,
    subject_requirements="Mathematics, German",
    language_proficiency="German",
)

admission_criteria13 = AdmissionCriteria(
    course_id=course13.course_id,
    IB_score=30,
    subject_requirements="Mathematics, English",
    language_proficiency="English",
)

admission_criteria14 = AdmissionCriteria(
    course_id=course14.course_id,
    IB_score=32,
    subject_requirements="Mathematics, English",
    language_proficiency="English",
)
# give random requirements

admission_criteria15 = AdmissionCriteria(
    course_id=course15.course_id,
    IB_score=34,
    subject_requirements="Mathematics, English",
    language_proficiency="English",
)

admission_criteria16 = AdmissionCriteria(
    course_id=course16.course_id,
    IB_score=36,
    subject_requirements="Mathematics, English",
    language_proficiency="English",
)

admission_criteria17 = AdmissionCriteria(
    course_id=course17.course_id,
    IB_score=38,
    subject_requirements="Mathematics, English",
    language_proficiency="English",
)

admission_criteria18 = AdmissionCriteria(
    course_id=course18.course_id,
    IB_score=40,
    subject_requirements="Mathematics, English",
    language_proficiency="English",
)

admission_criteria19 = AdmissionCriteria(
    course_id=course19.course_id,
    IB_score=42,
    subject_requirements="Mathematics, English",
    language_proficiency="English",
)

admission_criteria20 = AdmissionCriteria(
    course_id=course20.course_id,
    IB_score=44,
    subject_requirements="Mathematics, English",
    language_proficiency="English",
)

session.add_all(
    [
        admission_criteria1,
        admission_criteria2,
        admission_criteria3,
        admission_criteria4,
        admission_criteria5,
        admission_criteria6,
        admission_criteria7,
        admission_criteria8,
        admission_criteria9,
        admission_criteria10,
        admission_criteria11,
        admission_criteria12,
        admission_criteria13,
        admission_criteria14,
        admission_criteria15,
        admission_criteria16,
        admission_criteria17,
        admission_criteria18,
        admission_criteria19,
        admission_criteria20,
    ]
)
session.commit()

# Create and add users
user1 = User(username="Max", password="ihopeiget")
user2 = User(username="Lia", password="liaisbest")
session.add_all([user1, user2])
session.commit()

# Create and add scores
score1 = Score(user_id=user1.user_id, course_id=course1.course_id, score=33)
score2 = Score(user_id=user2.user_id, course_id=course2.course_id, score=44)
session.add_all([score1, score2])
session.commit()

# Create and add feedback
feedback1 = Feedback(
    user_id=user1.user_id,
    admission_criteria_id=admission_criteria1.admission_criteria_id,
    comment="This course is great!",
)
feedback2 = Feedback(
    user_id=user2.user_id,
    admission_criteria_id=admission_criteria2.admission_criteria_id,
    comment="I had a wonderful experience.",
)
session.add_all([feedback1, feedback2])
session.commit()
