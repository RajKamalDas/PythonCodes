import mysql.connector as MC

db = MC.connect(host="localhost", database="API", user="root", passwd="r.3.a.j.")

cursor = db.cursor(dictionary=True)

print("DB connected")

from flask import Flask, request, jsonify
import threading

app = Flask(__name__)

app.route("/posts", method=["GET"])


def get_posts():
    cursor.execute("select * from posts")
    result = cursor.fetchall()
    return jsonify(result)
