from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
    jsonify,
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_migrate import Migrate


app = Flask(__name__)
app.secret_key = "somesecretkeythatonlyishouldknow"
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "sqlite:////Users/gopinath.h03/Library/CloudStorage/OneDrive-IMC/1st Year/UniReq/unireq.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Not sure if this is needed


with app.app_context():
    db.create_all()


class Country(db.Model):  # This is the table for countries
    __tablename__ = "countries"
    country_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class University(db.Model):  # This is the table for universities
    __tablename__ = "universities"
    university_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    country_id = db.Column(db.Integer, db.ForeignKey("countries.country_id"))
    country = db.relationship("Country")


class Course(db.Model):  # This is the table for courses
    __tablename__ = "courses"
    course_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    university_id = db.Column(db.Integer, db.ForeignKey("universities.university_id"))
    university = db.relationship("University")


class AdmissionCriteria(db.Model):  # This is the table for admission criteria
    __tablename__ = "admission_criteria"
    admission_criteria_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.course_id"))
    IB_Score = db.Column(db.Integer)
    subject_requirements = db.Column(db.String)
    language_proficiency = db.Column(db.String)
    course = db.relationship("Course")


class Feedback(db.Model):  # This is the table for feedback
    id = db.Column(db.Integer, primary_key=True)
    feedback_text = db.Column(db.String(200), nullable=False)


with app.app_context():  # This is to create the tables
    db.create_all()


# Add countries
austria = Country(name="Austria")
germany = Country(name="Germany")

with app.app_context():
    db.session.add(austria)
    db.session.add(germany)
    db.session.commit()

# Add universities
university1 = University(name="University of Vienna", country=austria)
university2 = University(name="University of Salzburg", country=austria)
university3 = University(name="University of Innsbruck", country=austria)
university4 = University(name="University of Graz", country=austria)
university5 = University(name="University of Linz", country=austria)
university6 = University(name="University of Munich", country=germany)
university7 = University(name="University of Heidelberg", country=germany)
university8 = University(name="University of Freiburg", country=germany)
university9 = University(name="University of Tuebingen", country=germany)
university10 = University(name="University of Goettingen", country=germany)

with app.app_context():
    db.session.add(university1)
    db.session.add(university2)
    db.session.add(university3)
    db.session.add(university4)
    db.session.add(university5)
    db.session.add(university6)
    db.session.add(university7)
    db.session.add(university8)
    db.session.add(university9)
    db.session.add(university10)
    db.session.commit()

# Add courses
course1 = Course(name="Informatics", university=university1)
course2 = Course(name="Informatics", university=university2)
course3 = Course(name="Informatics", university=university3)
course4 = Course(name="Informatics", university=university4)
course5 = Course(name="Informatics", university=university5)
course6 = Course(name="Informatics", university=university6)
course7 = Course(name="Informatics", university=university7)
course8 = Course(name="Informatics", university=university8)
course9 = Course(name="Informatics", university=university9)
course10 = Course(name="Informatics", university=university10)
course11 = Course(name="Chemistry", university=university1)
course12 = Course(name="Chemistry", university=university2)
course13 = Course(name="Chemistry", university=university3)
course14 = Course(name="Chemistry", university=university4)
course15 = Course(name="Chemistry", university=university5)
course16 = Course(name="Chemistry", university=university6)
course17 = Course(name="Chemistry", university=university7)
course18 = Course(name="Chemistry", university=university8)
course19 = Course(name="Chemistry", university=university9)
course20 = Course(name="Chemistry", university=university10)

with app.app_context():
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.add(course5)
    db.session.add(course6)
    db.session.add(course7)
    db.session.add(course8)
    db.session.add(course9)
    db.session.add(course10)
    db.session.add(course11)
    db.session.add(course12)
    db.session.add(course13)
    db.session.add(course14)
    db.session.add(course15)
    db.session.add(course16)
    db.session.add(course17)
    db.session.add(course18)
    db.session.add(course19)
    db.session.add(course20)
    db.session.commit()

# Add admission criteria
admission_criteria1 = AdmissionCriteria(
    course=course1,
    IB_Score=38,
    subject_requirements="Programming and English",
    language_proficiency="English",
)
admission_criteria2 = AdmissionCriteria(
    course=course2,
    IB_Score=41,
    subject_requirements="Mathematics and English",
    language_proficiency="English",
)
admission_criteria3 = AdmissionCriteria(
    course=course3,
    IB_Score=42,
    subject_requirements="German",
    language_proficiency="German",
)
admission_criteria4 = AdmissionCriteria(
    course=course4,
    IB_Score=43,
    subject_requirements="Mathematics and English",
    language_proficiency="English",
)
admission_criteria5 = AdmissionCriteria(
    course=course5,
    IB_Score=39,
    subject_requirements="German",
    language_proficiency="German",
)
admission_criteria6 = AdmissionCriteria(
    course=course6,
    IB_Score=38,
    subject_requirements="Programming and English",
    language_proficiency="English",
)
admission_criteria7 = AdmissionCriteria(
    course=course7,
    IB_Score=41,
    subject_requirements="Mathematics and English",
    language_proficiency="English",
)
admission_criteria8 = AdmissionCriteria(
    course=course8,
    IB_Score=42,
    subject_requirements="German",
    language_proficiency="German",
)
admission_criteria9 = AdmissionCriteria(
    course=course9,
    IB_Score=43,
    subject_requirements="Mathematics and English",
    language_proficiency="English",
)
admission_criteria10 = AdmissionCriteria(
    course=course10,
    IB_Score=39,
    subject_requirements="German",
    language_proficiency="German",
)
admission_criteria11 = AdmissionCriteria(
    course=course11,
    IB_Score=38,
    subject_requirements="Programming and English",
    language_proficiency="English",
)
admission_criteria12 = AdmissionCriteria(
    course=course12,
    IB_Score=41,
    subject_requirements="Mathematics and English",
    language_proficiency="English",
)
admission_criteria13 = AdmissionCriteria(
    course=course13,
    IB_Score=42,
    subject_requirements="German",
    language_proficiency="German",
)
admission_criteria14 = AdmissionCriteria(
    course=course14,
    IB_Score=43,
    subject_requirements="Mathematics and English",
    language_proficiency="English",
)
admission_criteria15 = AdmissionCriteria(
    course=course15,
    IB_Score=39,
    subject_requirements="German",
    language_proficiency="German",
)
admission_criteria16 = AdmissionCriteria(
    course=course16,
    IB_Score=38,
    subject_requirements="Programming and English",
    language_proficiency="English",
)
admission_criteria17 = AdmissionCriteria(
    course=course17,
    IB_Score=41,
    subject_requirements="Mathematics and English",
    language_proficiency="English",
)
admission_criteria18 = AdmissionCriteria(
    course=course18,
    IB_Score=42,
    subject_requirements="German",
    language_proficiency="German",
)
admission_criteria19 = AdmissionCriteria(
    course=course19,
    IB_Score=43,
    subject_requirements="Mathematics and English",
    language_proficiency="English",
)
admission_criteria20 = AdmissionCriteria(
    course=course20,
    IB_Score=39,
    subject_requirements="German",
    language_proficiency="German",
)

with app.app_context():
    db.session.add(admission_criteria1)
    db.session.add(admission_criteria2)
    db.session.add(admission_criteria3)
    db.session.add(admission_criteria4)
    db.session.add(admission_criteria5)
    db.session.add(admission_criteria6)
    db.session.add(admission_criteria7)
    db.session.add(admission_criteria8)
    db.session.add(admission_criteria9)
    db.session.add(admission_criteria10)
    db.session.add(admission_criteria11)
    db.session.add(admission_criteria12)
    db.session.add(admission_criteria13)
    db.session.add(admission_criteria14)
    db.session.add(admission_criteria15)
    db.session.add(admission_criteria16)
    db.session.add(admission_criteria17)
    db.session.add(admission_criteria18)
    db.session.add(admission_criteria19)
    db.session.add(admission_criteria20)
    db.session.commit()


@app.route("/")  # Home page
def home():
    return render_template("home.html")


@app.before_request  # Before request to check if user is logged in
def before_request():
    g.user = None

    if "user_id" in session:  # If user is logged in, set g.user to user
        user = [x for x in users if x.id == session["user_id"]][0]
        g.user = user


@app.route("/login", methods=["GET", "POST"])  # Login page
def login():
    if request.method == "POST":  # If user submits login form
        session.pop("user_id", None)

        username = request.form["username"]
        password = request.form["password"]

        user = [x for x in users if x.username == username][
            0
        ]  # Check if user exists and password is correct
        if user and user.password == password:
            session["user_id"] = user.id
            return redirect(url_for("profile"))

        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile")  # Profile page
def profile():
    if not g.user:
        return redirect(
            url_for("login")
        )  # If user is not logged in, redirect to login page

    filter_options = [
        {"name": "Country", "options": ["Austria", "Germany"]},
        {"name": "Course", "options": ["Informatics", "Chemistry"]},
        {"name": "Language", "options": ["English", "German"]},
        {
            "name": "IB Score",
            "options": ["36", "37", "38", "39", "40", "41", "42", "43", "44"],
        },
    ]  # Filter options

    country = {"name": "Country", "options": ["Austria", "Germany"]}
    course = {"name": "Course", "options": ["Informatics", "Chemistry"]}
    language = {"name": "Language", "options": ["English", "German"]}
    ib_score = {
        "name": "IB Score",
        "options": ["36", "37", "38", "39", "40", "41", "42", "43", "44"],
    }  # Filter options

    return render_template(
        "profile.html",
        filter_options=filter_options,
        country=country,
        course=course,
        language=language,
        ib_score=ib_score,
    )


@app.route("/profile/results", methods=["GET"])  # Profile results page
def profile_results():
    country = request.args.get("country")  # Get filter options from request
    course = request.args.get("course")
    language = request.args.get("language")
    ib_score = request.args.get("ib_score")

    #  Query database for universities matching filter options
    universities = (
        db.session.query(University)
        .join(Country)
        .join(Course)
        .join(AdmissionCriteria)
        .filter(Country.name == country)
        .filter(Course.name == course)
        .filter(AdmissionCriteria.IB_Score >= ib_score)
        .filter(AdmissionCriteria.language_proficiency == language)
        .all()
    )

    return render_template(
        "profile_results.html",
        universities=universities,
        country=country,
        course=course,
        language=language,
        ib_score=ib_score,
    )


@app.route("/submit-feedback", methods=["POST"])  # Submit feedback page
def submit_feedback():
    feedback_text = request.form["feedback"]
    feedback = Feedback(feedback_text=feedback_text)
    db.session.add(feedback)
    db.session.commit()
    return "Feedback submitted successfully"


class User:  # User class
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User: {self.username}>"


users = []
users.append(User(id=1, username="admin", password="admin"))  # i am admin MUHHAHHAHAH


#####################################################################################
# Test
#####################################################################################

# def check_tables_exist():
#     inspector = inspect(db.engine)
#     tables = inspector.get_table_names()
#     return (
#         "university" in tables and "course" in tables and "admission_criteria" in tables
#     )


# # Call the function to check if the tables exist
# with app.app_context():
#     tables_exist = check_tables_exist()

# if tables_exist:
#     print("Tables exist in the database.")
# else:
#     print("Tables do not exist in the database.")


#####################################################################################
# how clear all the data in the database after each run
#####################################################################################
def clear_data():
    with app.app_context():
        meta = db.metadata
        for table in reversed(meta.sorted_tables):
            print("Clear table %s" % table)
            db.session.execute(table.delete())
        db.session.commit()


# clear_data() #run this to clear the data in the database

if __name__ == "__main__":
    app.run(debug=True)
