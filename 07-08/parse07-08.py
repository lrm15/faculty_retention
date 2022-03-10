import pdfplumber 
import pandas as pd
import csv
from pathlib import Path 

text = ''
for i in range(394, 408): 
    with pdfplumber.open('/Users/laurenmccarey/math308/07-08/catalog_2007-08.pdf') as temp: 
        page = temp.pages[i]
        text = page.extract_text()
    with open ('catalog_2007-08.txt', 'a') as f: 
        f.write(text)