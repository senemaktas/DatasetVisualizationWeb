# Pandas Tutorial: Importing Data with read_csv() datacamp
from flask import Flask,render_template,url_for,request,redirect,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import matplotlib.pyplot as pyplot # for visualization
from bs4 import BeautifulSoup 
import numpy as np
import pandas as pd
import json
import csv
import xml.etree.ElementTree as ET
import xml
import pathlib # for get file extension
import os
from uuid import uuid4

app = Flask(__name__)  #  create instance

# herşey test.db'de depolanacak.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Webdocs.db'
db = SQLAlchemy(app) # database'i başlatmak için.

# db iceriginin nasil olacagini tanimladik.
class DBdepo(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # id degeri verildi.
    content = db.Column(db.String(200), nullable=False) # dosyanin ismini almali
    date_created = db.Column(db.DateTime, default=datetime.utcnow) # zamani alir.

    def __repr__(self):
        return '<Document name %r>' % self.id  # task ve idsini dondurur

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) # default path is working directory

@app.route('/', methods=['POST', 'GET']) # db ye veri göndermek için post-get
def index():
    # taski alip dbye yazar.
    if request.method == 'POST':  
        # forma input idsi olan content gecildi,index.html deki input text idsi
        task_content = request.form['file-picker']
        #yeni nesne (task) icin model cagrildi, content databasedeki content sutunudur.
        new_task = DBdepo(content=task_content)

        # yeni task db ye eklenir,commit edilir ve anasayda kalinir
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')  # task eklenir ve anasayfada kalinir.
        except:
            return 'There was an issue adding your task' # eklenemez ise mesaji yazar.

    else:
        # taskleri date 2 gore siraliyor
        tasks = DBdepo.query.order_by(DBdepo.date_created).all()
        return render_template('index.html', tasks=tasks)

# silme islemi id degerine gore yapiliyor, indexte tanimlandi
@app.route('/delete/<int:id>')
def delete(id):
    # task id sini alir varsa ya da 404 doner
    task_to_delete = DBdepo.query.get_or_404(id)

    # id sini aldigi task in db den silinmesinin saglar
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/') # home page de kalir
    except:
        return 'There was a problem deleting that task'


@app.route("/", methods=["POST"])
def upload():
    folder_name = request.form['file-picker']
    '''
    # this is to verify that folder to upload to exists.
    if os.path.isdir(os.path.join(APP_ROOT, 'files/{}'.format(folder_name))):
        print("folder exist")
    '''
    target = os.path.join(APP_ROOT, 'files/{}'.format(folder_name))
    print(target)

    # if target folder does not exist create that
    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"): # multiple secenegi oldugu icin
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        # This is to verify files are supported
        ext = os.path.splitext(filename)[1]
        if (ext == ".jpg") or (ext == ".png"):
            print("File supported moving on...")
        else:
            render_template("Error.html", message="Files uploaded are not supported...")
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)

    # return send_from_directory("images", filename, as_attachment=True)
    return redirect("/", image_name=filename)

@app.route('/index/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)
    
# i wrote below part
# verisetini uzantısını bulacak fonksiyon
def findextension():
    file_extension=pathlib.Path("/home/sidney/Downloads/bio.jpg").suffix
    print(file_extension)
    return file_extension

FileExtens=findextension()

# upload and take file extension on
def uploadDataset(FileExtens):
    try:
        if(FileExtens==json):
            # Loading JSON formatted data
            with open('dict.json', 'r') as formatJSON:
                df=json.load(formatJSON)

        elif(FileExtens==csv):
            # Loading CSV formatted data
            df = pd.read_csv("x.csv")

        else:
            # Loading CSV formatted data
            with open('dict.xml', 'r') as formatXML: 
                df = formatXML.read() 
    except:
        print('Could not open file')
    finally:
        df.close() 
    return df

if __name__ == "__main__":
    app.run(debug=True)
