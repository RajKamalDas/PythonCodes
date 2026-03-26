from flask import Flask, render_template, abort

app = Flask("__name__")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects/<subproject>")
def projects(subproject):
    allowed = ["web", "desktop", "fun"]
    if subproject not in allowed:
        abort(404)
    return render_template(f"projects/{subproject}.html")


if __name__ == "__main__":
    app.run(debug=True)
