import pdfplumber 
import pandas as pd
import csv
from pathlib import Path 

# text = ''
# for i in range(404, 409): 
#     with pdfplumber.open('/Users/laurenmccarey/math308/08-09/catalog_2008-09.pdf') as temp: 
#         page = temp.pages[i]
#         text = page.extract_text()
#     with open ('catalog_2008-09.txt', 'a') as f: 
#         f.write(text)

text = ''
for i in range(395, 404): 
    with pdfplumber.open('/Users/laurenmccarey/math308/08-09/catalog_2008-09.pdf') as temp: 
        page = temp.pages[i]
        text = page.extract_text()
    with open ('temp.txt', 'a') as f: 
        f.write(text)