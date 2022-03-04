import pdfplumber 
import pandas as pd
import csv
from pathlib import Path 

# text = ''
# for i in range(576, 577): 
#     with pdfplumber.open('/Users/laurenmccarey/math308/16-17/catalog_2016-17.pdf') as temp: 
#         page = temp.pages[i]
#         text = page.extract_text()
#     with open ('catalog_2016-17.txt', 'a') as f: 
#         f.write(text)

#      *  On leave 2016-2017 
#    * *  On leave first semester  
#    * * * On leave second semester  
#      + Visitor first semester  
#    + + Visitor second semester  

lines = []
with open ('catalog_2016-17.txt') as f: 
    lines = f.readlines()


cleaned = []
for line in lines: 

    # this phrase contains a comma - replace with abbreviation so we can split by comma reliably 
    if ("Women's, Gender and Sexuality Studies" in line): 
        line = line.replace("Women's, Gender and Sexuality Studies", "WGGS")

    line = line.split('--')
    line[0] = line[0].split(',', maxsplit=1)
    line[0] = [item.strip() for item in line[0]]
    
    if (len(line) == 1):
        line.append(None) 
    elif (len(line) == 2): 
        line[1] = line[1].strip()

    print("\n")
    print(len(line))
    print(line)

    if (len(line[0]) < 2): 
        print(line[0])
        break
    
    
        
