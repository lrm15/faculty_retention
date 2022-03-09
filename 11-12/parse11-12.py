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

lines = []
with open ('catalog_2011-12.txt') as f: 
    lines = f.readlines()

cleaned = []
for line in lines: 

    # this phrase contains a comma - replace with abbreviation so we can split by comma reliably 
    if (", Jr." in line): 
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

    cleaned.append(line)

last = []
first = []
middle = []
title = []
degrees = []
leave = []
visiting = []
for faculty in cleaned: 
    if (len(faculty) < 4): 
        print(faculty)
        print(len(faculty))
        print("\n")
        break
    
    # deal with first, middle, and last name 
    if (len(faculty[0][0]) == 2): 
        last.append(faculty[0][0][1])
        middle.append(None)
        first.append(faculty[0][0][0])

    elif (len(faculty[0][0]) == 3): 
        last.append(faculty[0][0][2])
        middle.append(faculty[0][0][1])
        first.append(faculty[0][0][0])

    # populate list of dept names 
    title.append(faculty[0][1])

    degrees.append(faculty[1])

    # populate list of leave info 
    leave.append(faculty[2])

    # populate list of visiting info 
    visiting.append(faculty[3])
    
df = pd.DataFrame()
df['last'] = last
df['first'] = first
df['middle'] = middle 
df['title'] = title
df['degrees'] = degrees
df['leave'] = leave
df['visiting'] = visiting

# # # df.sort_values('last', inplace=True)

filepath = Path('/Users/laurenmccarey/math308/11-12/faculty11-12.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
df.to_csv(filepath)  