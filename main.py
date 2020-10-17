# https://stackabuse.com/reading-and-writing-xml-files-in-python/
# https://www.geeksforgeeks.org/reading-and-writing-xml-files-in-python/
# Pandas Tutorial: Importing Data with read_csv() datacamp

import matplotlib.pyplot as pyplot # for visualization
from bs4 import BeautifulSoup 
import numpy as np
import pandas as pd
import json
import csv
import xml.etree.ElementTree as ET
import xml
import pathlib # for get file extension

def chooseDataset():

    return my_dataset


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


