from flask import Flask, g, redirect, render_template, request, session, url_for
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
migrate = Migrate(app, db)


with app.app_context():
    db.create_all()


# class Country(db.Model):
#     __tablename__ = "countries"
#     country_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)


# class University(db.Model):
#     __tablename__ = "universities"
#     university_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     country_id = db.Column(db.Integer, db.ForeignKey("countries.country_id"))
#     country = db.relationship("Country")


# class User(db.Model):
#     __tablename__ = "users"
#     user_id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String)
#     password = db.Column(db.String)


# class Course(db.Model):
#     __tablename__ = "courses"
#     course_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     university_id = db.Column(db.Integer, db.ForeignKey("universities.university_id"))
#     university = db.relationship("University")


# class AdmissionCriteria(db.Model):
#     __tablename__ = "admission_criteria"  # look at the table structure
#     admission_criteria_id = db.Column(db.Integer, primary_key=True)
#     course_id = db.Column(db.Integer, db.ForeignKey("courses.course_id"))
#     IB_Score = db.Column(db.Integer)
#     subject_requirements = db.Column(db.String)
#     language_proficiency = db.Column(db.String)
#     course = db.relationship("Course")


# class Feedback(db.Model):
#     __tablename__ = "feedback"
#     feedback_id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
#     admission_criteria_id = db.Column(
#         db.Integer, db.ForeignKey("admission_criteria.admission_criteria_id")
#     )
#     feedback = db.Column(db.String)
#     user = db.relationship("User")


# with app.app_context():
#     db.create_all()
# session = db.session


@app.route("/")
def home():
    return render_template("home.html")


@app.before_request
def before_request():
    g.user = None

    if "user_id" in session:
        user = [x for x in users if x.id == session["user_id"]][0]
        g.user = user


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.pop("user_id", None)

        username = request.form["username"]
        password = request.form["password"]

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session["user_id"] = user.id
            return redirect(url_for("profile"))

        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile")
def profile():
    if not g.user:
        return redirect(url_for("login"))

    return render_template("profile2.html")


# @app.route("/index")
# def index():
#     countries = Country.query.all()
#     university = University.query.all()
#     user = User.query.all()
#     course = Course.query.all()
#     admission_criteria = AdmissionCriteria.query.all()
#     feedback = Feedback.query.all()
#     return render_template(
#         "index.html",
#         countries=countries,
#         university=university,
#         user=user,
#         course=course,
#         admission_criteria=admission_criteria,
#         feedback=feedback,
#     )


#####################################################################################


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User: {self.username}>"


users = []
users.append(User(id=1, username="admin", password="admin"))


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

if __name__ == "__main__":
    app.run(debug=True)

# STRUCTURE OF THE DATABASE
# **Table: Countries**

# - country_id (Primary Key)
# - name

# | Country ID | Country Name |
# | --- | --- |
# |  |  |
# |  |  |

# **Table: Universities**

# - university_id (Primary Key)
# - name
# - country_id (Foreign Key referencing Countries.country_id)

# | Universities ID | University Name | Country ID |
# | --- | --- | --- |
# |  |  |  |
# |  |  |  |

# **Table: Courses**

# - course_id (Primary Key)
# - name
# - university_id (Foreign Key referencing Universities.university_id)

# | Course ID | Course Name | University ID |
# | --- | --- | --- |
# |  |  |  |
# |  |  |  |

# **Table: AdmissionCriteria**

# - admission_criteria_id (Primary Key)
# - course_id (Foreign Key referencing Courses.course_id)
# - IB_Score
# - subject_requirements
# - language_proficiency

# | Admission Criteria ID | Course ID | IB_Score | Subject Requirements | Language Proficiency |
# | --- | --- | --- | --- | --- |
# |  |  |  |  |  |
# |  |  |  |  |  |

# **Table: Users**

# - user_id (Primary Key)
# - username
# - password

# | User ID | Username | Password |
# | --- | --- | --- |
# |  |  |  |
# |  |  |  |

# **Table: Scores**

# - score_id (Primary Key)
# - user_id (Foreign Key referencing Users.user_id)
# - course_id (Foreign Key referencing Courses.course_id)
# - score

# | Score ID | User ID | Course ID | Score |
# | --- | --- | --- | --- |
# |  |  |  |  |
# |  |  |  |  |

# **Table: Feedback**

# - feedback_id (Primary Key)
# - user_id (Foreign Key referencing Users.user_id)
# - admission_criteria_id (Foreign Key referencing AdmissionCriteria.admission_criteria_id)
# - comment

# | Feedback ID | User ID | Admission Criteria ID | Feedback |
# | --- | --- | --- | --- |
# |  |  |  |  |
# |  |  |  |  |
