# Pandas Tutorial: Importing Data with read_csv() datacamp
from flask import Flask, render_template, url_for, request, redirect, send_from_directory
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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
        return redirect(url_for('index'))
    return render_template('index.html')
    
@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('index'))

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
