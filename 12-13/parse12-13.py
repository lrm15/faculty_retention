import pdfplumber 
import pandas as pd
import csv
from pathlib import Path 

text = ''
for i in range(329, 336): 
    with pdfplumber.open('/Users/laurenmccarey/math308/12-13/catalog_2012-13.pdf') as temp: 
        page = temp.pages[i]
        text = page.extract_text()
    with open ('catalog_2012-13.txt', 'a') as f: 
        f.write(text)

# FACULTY 2012-2013
# *On leave 2012-2013
# **On leave first semester 
# ***On leave second semester 
# ****On leave calendar year (January-December 2012)
