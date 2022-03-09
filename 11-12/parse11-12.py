import pdfplumber 
import pandas as pd
import csv
from pathlib import Path 

# text = ''
# for i in range(346, 355): 
#     with pdfplumber.open('/Users/laurenmccarey/math308/11-12/catalog_2011-12.pdf') as temp: 
#         page = temp.pages[i]
#         text = page.extract_text()
#     with open ('catalog_2011-12.txt', 'a') as f: 
#         f.write(text)

# FACULTY 2011-2012
# *On leave 2011-2012
# **On leave first semester 
# ***On leave second semester 
# ****On leave calendar year (January-December 2011)