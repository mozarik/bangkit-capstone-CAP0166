from decimal import Decimal

from flask import Flask, request, render_template, jsonify
import requests

import json

app = Flask(__name__)

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
        i['percentage'] = str(round((1 - Decimal(i['percentage'])) *100)) + "%"
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
