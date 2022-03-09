import pdfplumber 
import pandas as pd
import csv
from pathlib import Path 

text = ''
for i in range(317, 325): 
    with pdfplumber.open('/Users/laurenmccarey/math308/10-11/catalog_2010-11.pdf') as temp: 
        page = temp.pages[i]
        text = page.extract_text()
    with open ('catalog_2010-11.txt', 'a') as f: 
        f.write(text)

# FACULTY 2010-2011
# *On leave 2010-2011
# **On leave first semester 
# ***On leave second semester 
# ****On leave calendar year (January-December 2010)

