from decimal import Decimal

import requests
from flask import Flask, flash, request, redirect, url_for, render_template, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import urllib.request
import os
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__, static_folder="./static", template_folder="./templates")

app.secret_key = "caircocoders-ednalan"
#
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'thewatcher'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# mysql = MySQL(app)
#
# app.config['UPLOAD_FOLDER'] = 'static/uploads'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/js/<path:path>')
def send_js(path):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static', 'js'), path)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/uploadfile")
def index():
    return render_template('uploadfile.html', menu='dashboard', submenu='upload')


@app.route("/showdata")
def index2():
    # cur = mysql.connection.cursor()
    # cur.execute("SELECT * FROM uploads")
    # uploads = cur.fetchall()
    # cur.close()

    url = "https://api-watcher-n762eur5da-et.a.run.app/postprocess/"
    r = requests.get(url)
    data = r.json()["data"]
    for i in data:
        i['percentage'] = str(round((1 - Decimal(i['percentage'])) * 100)) + "%"
    return render_template('showdata.html', menu='dashboard', submenu='show', data=data)


@app.route("/upload", methods=["POST", "GET"])
def upload():
    file = request.files['uploadFile']

    url = "https://api-watcher-n762eur5da-et.a.run.app/uploadfile/"
    files = {'file': file}
    r = requests.post(url, files=files)
    data = r.json()["data"]
    img_url = data["img_url"]

    return jsonify({'htmlresponse': render_template('response.html', msg="", filenameimage=img_url)})


if __name__ == "__main__":
    app.run(debug=True)
