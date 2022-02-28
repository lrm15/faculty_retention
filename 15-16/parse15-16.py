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

# lines = []
# with open ('catalog_2015-16.txt') as f: 
#     lines = f.readlines()

# cleaned = []
# for line in lines: 

#     # this phrase contains a comma - replace with abbreviation so we can split by comma reliably 
#     if ("Women, Gender & Sexuality Stdy" in line): 
#         line = line.replace("Women, Gender & Sexuality Stdy", "WGGS")

#     line = line.split(',')
#     line = [item.strip() for item in line]
    
#     # make sure all fields are present in all entries 
#     if (len(line) < 3):
#         print(line) 
#         break

#     # code s if the faculty member is on leave in the spring, f if on leave in fall, y if on leave all year, and n if not on leave 
#     if (line[0][0:3] == "***"): 
#         line.append('s') 
#         line[0] = line[0].replace("***", '')        
#     elif (line[0][0:2] == "**"): 
#         line.append('f')             
#         line[0] = line[0].replace("**", '')
#     elif (line[0][0:1] == "*"): 
#         line.append('y')
#         line[0] = line[0].replace("*", '')
#     else: 
#         line.append('n')

#     # code 1 if the faculty member is visiting and 0 otherwise 
#     if ("+" in line[0]): 
#         line.append(1)
#         line[0] = line[0].strip('+')
#     else: 
#         line.append(0)

#     # make sure all lines have 5 fields 
#     if (len(line) != 5): 
#         print(line)
#         break

#     # deal with middle name / initial problem 
#     line[1] = line[1].split(" ")

#     # # have a middle name / initial 
#     # if (len(line[1]) > 1): 
#     #     line.append(line[1][1])
#     #     # line[1] = line[1][0]
#     #     print(line)
#     # # no middle name / initial 
#     # else: 
#     #     line.append("")

#     # # make sure all lines have 5 fields 
#     # if (len(line) != 6): 
#     #     print("line length not equal to 6")
#     #     print(line)
#     #     break

#     cleaned.append(line)

# last = []
# first = []
# middle = []
# dept = []
# leave = []
# visiting = []
# for faculty in cleaned: 
#     # check that each individual faculty member has 4 fields of data
#     if (len(faculty) < 5): 
#         print("error: the following faculty member does not have 5 fields")
#         print(faculty)
#         break 

#     # populate list of last names 
#     last.append(faculty[0])

#     # populate list of first and middle names 
#     if (len(faculty[1]) == 1): 
#         first.append(''.join(faculty[1]))
#         middle.append(None)
#     else: 
#         first.append(faculty[1][0])
#         middle.append(faculty[1][1])

#     # populate list of dept names 
#     dept.append(faculty[2])

#     # populate list of leave info 
#     leave.append(faculty[3])

#     # populate list of visiting info 
#     visiting.append(faculty[4])
    
# df = pd.DataFrame()
# df['last'] = last
# df['first'] = first
# df['middle'] = middle 
# df['dept'] = dept
# df['leave'] = leave
# df['visiting'] = visiting

# df.sort_values('last', inplace=True)

# filepath = Path('/Users/laurenmccarey/math308/15-16/faculty15-16.csv')  
# filepath.parent.mkdir(parents=True, exist_ok=True)  
# df.to_csv(filepath)  