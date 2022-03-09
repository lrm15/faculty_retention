import pdfplumber 
import pandas as pd
import csv
from pathlib import Path 

# text = ''
# for i in range(329, 336): 
#     with pdfplumber.open('/Users/laurenmccarey/math308/12-13/catalog_2012-13.pdf') as temp: 
#         page = temp.pages[i]
#         text = page.extract_text()
#     with open ('catalog_2012-13.txt', 'a') as f: 
#         f.write(text)

# FACULTY 2012-2013
# *On leave 2012-2013
# **On leave first semester 
# ***On leave second semester 
# ****On leave calendar year (January-December 2012)

lines = []
with open ('catalog_2012-13.txt') as f: 
    lines = f.readlines()

cleaned = []
for line in lines: 

    # this phrase contains a comma - replace with abbreviation so we can split by comma reliably 
    if ("Women’s, Gender, and Sexuality Studies" in line): 
        line = line.replace("Women’s, Gender, and Sexuality Studies", "WGGS")
    elif (", Jr." in line): 
        line = line.replace(", Jr.", "Jr.")

    line = line.lower()

    line = line.split("—", maxsplit=1)
    line[0] = line[0].split(",", maxsplit=1)
    line[0] = [item.strip() for item in line[0]]

    if (len(line) == 2): 
        line[1] = line[1].strip()

    if (len(line) == 1): 
        line.append(None)

    # make sure all fields are present in all entries 
    if (len(line) < 2):
        print(line) 
        break

    # code s if the faculty member is on leave in the spring, f if on leave in fall, y if on leave all year, and n if not on leave 
    if (line[0][0][0:3] == "***"): 
        line.append('s') 
        line[0][0] = line[0][0].replace("***", '')     
    elif (line[0][0][0:2] == "**"): 
        line.append('f')             
        line[0][0] = line[0][0].replace("**", '')
    elif (line[0][0][0:1] == "*"): 
        line.append('y')
        line[0][0] = line[0][0].replace("*", '')
    elif (line[0][0][0:4] == "****"):
        line.append('y')
        line[0][0] = line[0][0].replace("****", '')
    else: 
        line.append('n')

    # code 1 if the faculty member is visiting and 0 otherwise 
    if ("visiting" in line[0][1]): 
        line.append(1)
        line[0][1] = line[0][1].replace("visiting", '')
    else: 
        line.append(0)

    # make sure all lines have 5 fields 
    if (len(line) != 4): 
        print(line)
        break

    # deal with middle name / initial problem 
    line[0][0] = line[0][0].split(" ", maxsplit=2)
    print(line)

    # cleaned.append(line)