import pdfplumber 
import pandas as pd
import csv
from pathlib import Path 

# text = ''
# for i in range(393, 398): 
#     with pdfplumber.open('/Users/laurenmccarey/math308/15-16/catalog_2015-16.pdf') as temp: 
#         page = temp.pages[i]
#         text = page.extract_text()
#     with open ('catalog_2015-16.txt', 'a') as f: 
#         f.write(text)

# *  On leave 2015-2016  
# * *  On leave first semester   
# * * * On leave second semester   
# + Visitor first semester 
# + + Visitor second semester 

lines = []
with open ('catalog_2015-16.txt') as f: 
    lines = f.readlines()

cleaned = []
for line in lines: 

    # this phrase contains a comma - replace with abbreviation so we can split by comma reliably 
    if ("Women, Gender & Sexuality Stdy" in line): 
        line = line.replace("Women, Gender & Sexuality Stdy", "WGGS")

    line = line.split(',')
    line = [item.strip() for item in line]
    
    # make sure all fields are present in all entries 
    if (len(line) < 3):
        print(line) 
        break

    # code s if the faculty member is on leave in the spring, f if on leave in fall, y if on leave all year, and n if not on leave 
    if (line[0][0:3] == "***"): 
        line.append('s') 
        line[0] = line[0].replace("***", '')        
    elif (line[0][0:2] == "**"): 
        line.append('f')             
        line[0] = line[0].replace("**", '')
    elif (line[0][0:1] == "*"): 
        line.append('y')
        line[0] = line[0].replace("*", '')
    else: 
        line.append('n')

    # code 1 if the faculty member is visiting and 0 otherwise 
    if ("+" in line[0]): 
        line.append(1)
        line[0] = line[0].strip('+')
    else: 
        line.append(0)

    # make sure all lines have 5 fields 
    if (len(line) != 5): 
        print(line)
        break

    cleaned.append(line)

print(cleaned)

# names = []
# titles = []
# degrees = []
# leave = []
# for faculty in cleaned: 
#     # check that each individual faculty member has 4 fields of data
#     if (len(faculty) < 4): 
#         print("error: the following faculty member does not have 4 fields")
#         print(faculty)
#         break 
    
#     names.append(faculty[0])
#     titles.append(faculty[1])
#     degrees.append(faculty[2])
#     leave.append(faculty[3])

# df = pd.DataFrame()
# df['name'] = names
# df['title'] = titles 
# df['degrees'] = degrees 
# df['leave'] = leave

# # print(df)
# filepath = Path('/Users/laurenmccarey/math308/20-21/faculty20-21.csv')  
# filepath.parent.mkdir(parents=True, exist_ok=True)  
# df.to_csv(filepath)  