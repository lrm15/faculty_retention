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

# lines = []
# with open ('catalog_2016-17.txt') as f: 
#     lines = f.readlines()


# cleaned = []
# for line in lines: 

#     # this phrase contains a comma - replace with abbreviation so we can split by comma reliably 
#     if ("Women's, Gender and Sexuality Studies" in line): 
#         line = line.replace("Women's, Gender and Sexuality Studies", "WGGS")

#     line = line.split('--')
#     line[0] = line[0].split(',', maxsplit=1)
#     line[0] = [item.strip() for item in line[0]]
    
#     if (len(line) == 1):
#         line.append(None) 
#     elif (len(line) == 2): 
#         line[1] = line[1].strip()   

#     if (len(line[0]) < 2): 
#         print(line[0])
#         break

#     # code s if the faculty member is on leave in the spring, f if on leave in fall, y if on leave all year, and n if not on leave 
#     if (line[0][0][0:3] == "***"): 
#         line.append('s') 
#         line[0][0] = line[0][0].replace("***", '')        
#     elif (line[0][0][0:2] == "**"): 
#         line.append('f')             
#         line[0][0] = line[0][0].replace("**", '')
#     elif (line[0][0][0:1] == "*"): 
#         line.append('y')
#         line[0][0] = line[0][0].replace("*", '')
#     else: 
#         line.append('n')

#     # code 1 if the faculty member is visiting and 0 otherwise 
#     if ("+" in line[0][0]): 
#         line.append(1)
#         line[0][0] = line[0][0].strip('+')
#     else: 
#         line.append(0)

#     # make sure all lines have 4 fields 
#     if (len(line) != 4): 
#         print(line)
#         break
    
#     # deal with middle name / initial problem 
#     line[0][0] = line[0][0].split(" ", maxsplit=2)

#     cleaned.append(line)


# last = []
# first = []
# middle = []
# title = []
# degrees = []
# leave = []
# visiting = []

# for faculty in cleaned: 
    
#     # check that each individual faculty member has 4 fields of data
#     if (len(faculty) < 4): 
#         print("error: the following faculty member does not have 4 fields")
#         print(faculty)
#         break 

#     # deal with first, middle, and last name 
#     if (len(faculty[0][0]) == 2): 
#         last.append(faculty[0][0][1])
#         middle.append(None)
#         first.append(faculty[0][0][0])

#     elif (len(faculty[0][0]) == 3): 
#         last.append(faculty[0][0][2])
#         middle.append(faculty[0][0][1])
#         first.append(faculty[0][0][0])

#     # populate list of titles 
#     title.append(faculty[0][1])

#     # populate list of degree info 
#     degrees.append(faculty[1])

#     # populate list of leave info 
#     leave.append(faculty[2])

#     # populate list of faculty visiting status
#     visiting.append(faculty[3])

    
# df = pd.DataFrame()
# df['last'] = last
# df['first'] = first
# df['middle'] = middle 
# df['title'] = title
# df['degrees'] = degrees
# df['leave'] = leave
# df['visiting'] = visiting

# # df.sort_values('last', inplace=True)

# filepath = Path('/Users/laurenmccarey/math308/16-17/faculty16-17.csv')  
# filepath.parent.mkdir(parents=True, exist_ok=True)  
# df.to_csv(filepath)  
