#Use this for any flask implementation
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from FirebaseHelper import pushStudent, getStudents, removeStudent


app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=2)

@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        #session.permanent = True
        user = request.form["nm"]
        email = request.form["email"]
        session["user"] = user
        session["email"] = email
        pushStudent("LoggedIn", user, email)
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        return render_template("Locations.html")
    else:
        return redirect(url_for("login"))
@app.route("/Zachary")
def Zachary():

    return render_template("Zachary.html")

@app.route("/MSC")
def MSC():

    return render_template("MSC.html")

@app.route('/Zachary-link/')
def Zachary_link():
  q = " "
  counter = 0
  for student in getStudents("Zachry"):
      counter += 1
      q = q + "<br>" + str(counter)+". Name: " + student.name + "<br>" + "Email: " + student.email + "</br>"
  return q

@app.route('/MSC-link/')
def MSC_link():
    q = " "
    counter = 0
    for student in getStudents("MSC"):
        counter += 1
        q = q + "<br>" + str(counter) + ". Name: " + student.name + "<br>" + "Email: " + student.email + "</br>"
    return q

@app.route("/logout")
def logout():
    user = session["user"]
    session.pop("user", None)
    removeStudent("LoggedIn", user)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
