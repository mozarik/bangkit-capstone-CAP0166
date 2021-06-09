from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
from flask_mysqldb import MySQL,MySQLdb
from werkzeug.utils import secure_filename
import urllib.request
import os
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)


app.secret_key = "caircocoders-ednalan"
         
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'thewatcher'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app) 
 
app.config['UPLOAD_FOLDER'] = 'static/uploads'
   
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
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM uploads")
    uploads = cur.fetchall()
    cur.close()
    return render_template('showdata.html', menu='dashboard', submenu='show', data=uploads)

@app.route("/upload",methods=["POST","GET"])
def upload():
    file = request.files['uploadFile']
    filename = secure_filename(file.filename)
    
    if file and allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        filenameimage = file.filename
 
        today = datetime.today() 
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("INSERT INTO uploads (file_name,upload_time) VALUES (%s,%s)",[filenameimage,today])
        mysql.connection.commit()       
        cur.close()
        msg  = 'File successfully uploaded ' + file.filename + ' to the database!'
    else:
        msg  = 'Invalid Uplaod only png, jpg, jpeg, gif'
    return jsonify({'htmlresponse': render_template('response.html', msg=msg, filenameimage=filenameimage)})

if __name__ == "__main__":
    app.run(debug=True)