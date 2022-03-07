import pdfplumber 
import pandas as pd
import csv
from pathlib import Path 

text = ''
for i in range(548, 556): 
    with pdfplumber.open('/Users/laurenmccarey/math308/17-18/catalog_2017-18.pdf') as temp: 
        page = temp.pages[i]
        text = page.extract_text()
    with open ('catalog_2017-18.txt', 'a') as f: 
        f.write(text)