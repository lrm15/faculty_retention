import pdfplumber 
import pandas as pd
import csv
from pathlib import Path 

# text = ''
# for i in range(87, 112): 
#     with pdfplumber.open('/Users/laurenmccarey/math308/21-22/catalog_2021-22.pdf') as temp: 
#         page = temp.pages[i]
#         text = page.extract_text()
#     with open ('catalog_2021-22.txt', 'a') as f: 
#         f.write(text)
#     print(i)

lines = []
with open ('catalog_2021-22.txt') as f: 
    lines = f.readlines()

print(lines)