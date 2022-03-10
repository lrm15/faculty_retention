import pdfplumber 
import pandas as pd
import csv
from pathlib import Path 

text = ''
for i in range(347, 357): 
    with pdfplumber.open('/Users/laurenmccarey/math308/09-10/catalog_2009-10.pdf') as temp: 
        page = temp.pages[i]
        text = page.extract_text()
    with open ('catalog_2009-10.txt', 'a') as f: 
        f.write(text)