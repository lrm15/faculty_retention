import pdfplumber 
import pandas as pd
import csv
from pathlib import Path 

text = ''
for i in range(576, 577): 
    with pdfplumber.open('/Users/laurenmccarey/math308/16-17/catalog_2016-17.pdf') as temp: 
        page = temp.pages[i]
        text = page.extract_text()
    with open ('catalog_2016-17.txt', 'a') as f: 
        f.write(text)

#      *  On leave 2016-2017 
#    * *  On leave first semester  
#    * * * On leave second semester  
#      + Visitor first semester  
#    + + Visitor second semester  