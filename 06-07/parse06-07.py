import pdfplumber 
import pandas as pd
import csv
from pathlib import Path 

# text = ''
# for i in range(395, 409): 
#     with pdfplumber.open('/Users/laurenmccarey/math308/06-07/catalog_2006-07.pdf') as temp: 
#         page = temp.pages[i]
#         text = page.extract_text()
#     with open ('catalog_2006-07.txt', 'a') as f: 
#         f.write(text)

lines = []
with open ('catalog_2006-07.txt') as f: 
    lines = f.readlines()


for line in lines: 
    line = line.lower()

    if ("b.a." in line): 
        line = line.replace("b.a.", "; b.a.")
    
    elif ("b.s." in line): 
        line = line.replace("b.s.", "; b.s.")
        line = line.strip()

    elif("associate" in line): 
        line = line.replace("associate", ", associate")


    with open ('catalog_temp.txt', 'a') as f: 
        f.write(line)
