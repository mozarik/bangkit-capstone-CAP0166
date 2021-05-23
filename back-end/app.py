from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = [
    {
        "id": 1,
        "title": u"Buy groceries",
        "description": u"Milk, Cheese, Pizza, Fruit, Tylenol",
        "done": False,
    },
    {
        "id": 2,
        "title": u"Learn Python",
        "description": u"Need to find a good Python tutorial on the web",
        "done": False,
    },
]


@app.route("/check")
def hello():
    return "Hello, world"


@app.route("/json", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tasks})
