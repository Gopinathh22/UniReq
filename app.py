from flask import Flask, g, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect


app = Flask(__name__)
app.secret_key = "somesecretkeythatonlyishouldknow"


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
