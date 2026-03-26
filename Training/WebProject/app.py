import sqlite3, os, PyPDF2
from sqlite3 import IntegrityError
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, flash, jsonify

app = Flask(__name__)
app.secret_key = "secret123"

BOOK_FOLDER = "books"
ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}
app.config["BOOK_FOLDER"] = BOOK_FOLDER


def db():
    conn = sqlite3.connect("Library.db")
    conn.row_factory = sqlite3.Row
    return conn


def allowedFile(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/adduser", methods=["POST"])
def adduser():

    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    role = request.form.get("role")
    sendToLogin = False

    if role == None:
        sendToLogin = True
        role = "user"

    DB = db()

    # Optional but smart: prevent duplicates
    existing = DB.execute("SELECT id FROM users WHERE username=? OR email=?", (username, email)).fetchone()

    if existing:
        flash("User already exists.")
        DB.close()
        if sendToLogin:
            return redirect("/login")
        return redirect("/admin")

    DB.execute("INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)", (username, email, password, role))

    DB.commit()
    DB.close()

    flash("User added successfully.")
    if sendToLogin:
        return redirect("/login")
    return redirect("/admin")


@app.route("/demoteuser/<username>")
def demote(username):
    if username == session.get("user") or not session.get("user"):
        return redirect("/admin")
    DB = db()
    cur_role = DB.execute("Select role from users where username=?", (username,)).fetchone()[0]
    if cur_role == "librarian":
        DB.execute("update users set role = 'user' where username=?", (username,))
    elif cur_role == "admin":
        admin_count = DB.execute("SELECT COUNT(*) FROM users WHERE role = 'admin'").fetchone()[0]
        if admin_count > 1:
            DB.execute("update users set role = 'librarian' where username=?", (username,))
    else:
        DB.execute("delete from users where username=?", (username,))
    DB.commit()
    DB.close()
    return redirect("/admin")


@app.route("/promoteuser/<username>")
def promote(username):
    if username == session:
        return redirect("/admin")
    DB = db()
    cur_role = DB.execute("Select role from users where username=?", (username,)).fetchone()[0]
    if cur_role == "librarian":
        DB.execute("update users set role = 'admin' where username=?", (username,))
    elif cur_role == "user":
        DB.execute("update users set role = 'librarian' where username=?", (username,))
    DB.commit()
    DB.close()
    return redirect("/admin")


# ==========================
# LIBRARIAN PANEL
# ==========================


@app.route("/librarian", methods=["GET", "POST"])
def librarian():
    if not session.get("role") or session.get("role") == "user":
        return redirect("/login")

    conn = db()
    cursor = conn.cursor()

    # ======================
    # ADD BOOK
    # ======================
    if request.method == "POST":

        title = request.form.get("title")
        author = request.form.get("author")
        file = request.files.get("file")

        if title and author and file and file.filename != "" and allowedFile(file.filename):

            filename = secure_filename(file.filename)
            filepath = os.path.join(BOOK_FOLDER, filename)
            file.save(filepath)

            pdf = PyPDF2.PdfReader(filepath)
            pages = len(pdf.pages)

            size_kb = round(os.path.getsize(filepath) / 1024, 2)
            size = f"{size_kb} KB"

            cursor.execute(
                """
                INSERT INTO books (title, author, pages, size, loc)
                VALUES (?, ?, ?, ?, ?)
            """,
                (title, author, pages, size, filename),
            )

            conn.commit()
            flash("✅ Book added successfully!")

        conn.close()
        return redirect(url_for("librarian"))

    # ======================
    # SEARCH + DEFAULT 10
    # ======================
    search = request.args.get("search")

    if search:
        cursor.execute(
            """
            SELECT * FROM books
            WHERE title LIKE ? OR author LIKE ?
        """,
            (f"%{search}%", f"%{search}%"),
        )
    else:
        search = ""
        cursor.execute(
            """
            SELECT * FROM books
            ORDER BY id DESC
            LIMIT 10
        """
        )

    books = cursor.fetchall()
    conn.close()

    return render_template("librarian.html", books=books, search=search)


# ==========================
# SEARCH SUGGESTION
# ==========================
@app.route("/suggest")
def suggest():

    query = request.args.get("q")

    if not query:
        return jsonify([])
    
    conn = db()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT title, author FROM books
        WHERE title LIKE ? OR author LIKE ?
        LIMIT 5
    """,
        (f"%{query}%", f"%{query}%"),
    )

    results = cursor.fetchall()
    conn.close()

    suggestions = [{"title": row["title"], "author": row["author"]} for row in results]
    return jsonify(suggestions)


# ==========================
# DELETE BOOK
# ==========================
@app.route("/delete/<int:id>")
def delete_book(id):

    conn = db()
    cursor = conn.cursor()

    cursor.execute("SELECT loc FROM books WHERE id=?", (id,))
    book = cursor.fetchone()

    if book:
        filepath = os.path.join(BOOK_FOLDER, book["loc"])

        if os.path.exists(filepath):
            os.remove(filepath)

        cursor.execute("DELETE FROM books WHERE id=?", (id,))
        conn.commit()
        flash("❌ Book deleted successfully!")

    conn.close()
    return redirect(url_for("librarian"))


@app.route("/")
def home():
    DB = db()
    exampleData = DB.execute("Select * from books").fetchmany(3)
    return render_template("home.html", data=exampleData)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    error = None
    if request.method == "POST":
        data = (request.form["username"], request.form["email"], request.form["password"], "user")
        DB = db()

        try:
            DB.execute("INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)", data)
            DB.commit()
            print(data)
            return redirect("/login")

        except IntegrityError as e:
            DB.rollback()
            if "username" in str(e):
                error = "Username already exists."
            elif "email" in str(e):
                error = "Email already exists."
            else:
                error = "Something went wrong."
            print(error)
        finally:
            DB.close()
        return render_template("signup.html", error=error)
    return render_template("signup.html", error=error)


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        pwd = request.form["password"]

        DB = db()
        user = DB.execute("select * from users where username=? and password=?", (username, pwd)).fetchone()
        DB.close()

        if user:
            session["user"] = user["username"]
            session["role"] = user["role"]
            return redirect("/library")
        else:
            DB = db()
            user = DB.execute("select * from users where username=?", (username,)).fetchone()
            DB.close()
            print(user)
            if user:
                error = "Incorrect Password."
            else:
                error = "You don't have an account."

    return render_template("login.html", error=error)


@app.route("/librarianlogin", methods=["GET", "POST"])
def librarianlogin():
    error = None
    if request.method == "POST":
        # print("METHOD:", request.method)
        # print("FORM:", request.form)
        # return "OK"
        print(request.form)
        username = request.form["username"]
        pwd = request.form["password"]

        DB = db()
        user = DB.execute("select * from users where username=? and password=?", (username, pwd)).fetchone()
        DB.close()

        if user:
            if user["role"] != "user":
                session["user"] = user["username"]
                session["role"] = user["role"]
                return redirect("/librarian")
            else:
                error = "You don't have permission."
        else:
            DB = db()
            user = DB.execute("select * from users where username=?", (username,)).fetchone()
            DB.close()
            if user:
                error = "Incorrect Password."
            else:
                error = "You don't have an account."

    return render_template("librarianlogin.html", error=error)


@app.route("/adminlogin", methods=["GET", "POST"])
def adminlogin():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        pwd = request.form["password"]

        DB = db()
        user = DB.execute("select * from users where username=? and password=?", (username, pwd)).fetchone()
        DB.close()

        if user:
            if user["role"] == "admin":
                session["user"] = user["username"]
                session["role"] = user["role"]
                return redirect("/admin")
            else:
                error = "You don't have permission."
        else:
            DB = db()
            user = DB.execute("select * from users where username=?", (username,)).fetchone()
            DB.close()
            if user:
                error = "Incorrect Password."
            else:
                error = "You don't have an account."

    return render_template("adminlogin.html", error=error)


@app.route("/library")
def library():
    if not session.get("role"):
        return redirect("/login")

    DB = db()
    cursor = DB.cursor()
    
    search = request.args.get("search")

    if search:
        cursor.execute(
            """
            SELECT * FROM books
            WHERE title LIKE ? OR author LIKE ?
        """,
            (f"%{search}%", f"%{search}%"),
        )
    else:
        search = ""
        cursor.execute(
            """
            SELECT * FROM books
            ORDER BY id DESC
            LIMIT 10
        """
        )

    books = cursor.fetchall()
    DB.close()

    return render_template("library.html", books=books, search=search)


@app.route("/admin")
def admin():
    if session.get("role") != "admin":
        return redirect("/adminlogin")

    DB = db()
    users = DB.execute("select * from users where role='user'").fetchall()
    librarians = DB.execute("select * from users where role = 'librarian'").fetchall()
    admins = DB.execute("SELECT * FROM users WHERE role = 'admin' AND username != ?", (session["user"],)).fetchall()
    DB.close()

    return render_template("admin.html", users=users, librarians=librarians, admins=admins)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/books/<filename>")
def books(filename):
    return send_from_directory(app.config["BOOK_FOLDER"], filename)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
