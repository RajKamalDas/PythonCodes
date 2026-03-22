import sqlite3, os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory

app = Flask(__name__)
app.secret_key = "secret123"

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def db():
    return sqlite3.connect("Applicatons.db")


def allowedFile(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/apply", methods=["GET", "POST"])
def apply():
    if request.method == "POST":
        resume = request.files[resume]
        filename = None

        if resume and allowedFile(resume.filename):
            filename = secure_filename(resume.filename)
            resume.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        data = (
            request.form["name"],
            request.form["email"],
            request.form["phone"],
            request.form["position"],
            request.form["message"],
            filename,
        )

        DB = db()
        DB.execute("insert into Applications values (NULL, ?, ?, ?, ?, ?, ?)", data)
        DB.commit()
        DB.close()

        return render_template(
            "success.html",
            name=request.form["name"],
            mail=request.form["email"],
            phone=request.form["phone"],
            position=request.form["position"],
            message=request.form["message"],
        )

    return render_template("application.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        user = request.form["usernames"]
        pwd = request.form["password"]

        DB = db()
        admin = DB.execute("select * from admin where username=? and password=?", (user, pwd)).fetchone()
        DB.close()

        if admin:
            session["admin"] = True
            return redirect("/admin")
        else:
            error = "You don't have permission."

    return render_template("login.html", error=error)


@app.route("/admin")
def admin():
    if not session.get("admin"):
        return redirect("/login")

    DB = db()
    data = DB.execute("select * from Applications").fetchall()
    DB.close()

    return render_template("admin.html", data=data)


@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect("/login")


@app.route("/uploads/<filename>")
def upload(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
