import pdfplumber 
import pandas as pd
import csv
from pathlib import Path 

# text = ''
# for i in range(471, 476): 
#     with pdfplumber.open('/Users/laurenmccarey/math308/14-15/catalog_2014-15.pdf') as temp: 
#         page = temp.pages[i]
#         text = page.extract_text()
#     with open ('catalog_2014-15.txt', 'a') as f: 
#         f.write(text)

# * On leave 2014-2015
# ** On leave first semester 
# ***On leave second semester 
# + Visitor first semester 
# ++ Visitor second semester

# lines = []
# with open ('catalog_2014-15.txt') as f: 
#     lines = f.readlines()

# cleaned = []
# for line in lines: 

#     # this phrase contains a comma - replace with abbreviation so we can split by comma reliably 
#     if ("Women’s, Gender and Sexuality Studies" in line): 
#         line = line.replace("Women’s, Gender and Sexuality Studies" , "WGGS")
#     elif("Women’s Gender and Sexuality Studies" in line): 
#         line = line.replace("Women’s Gender and Sexuality Studies" , "WGGS")
#     elif("Women’s, Gender, and Sexuality Studies" in line): 
#         line = line.replace("Women’s, Gender, and Sexuality Studies" , "WGGS")


#     line = line.split(',', maxsplit=1)
#     line = [item.strip() for item in line]
    
#     # make sure all fields are present in all entries 
#     if (len(line) < 2):
#         print(line) 
#         break

#         # code s if the faculty member is on leave in the spring, f if on leave in fall, y if on leave all year, and n if not on leave 
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

#     # make sure all lines have 4 fields 
#     if (len(line) != 4): 
#         print(line)
#         break

#     # split name into first, middle, and last
#     line[0] = line[0].split(" ")

#     if (len(line[0]) < 2): 
#         print(line)
#         break

#     cleaned.append(line)

# last = []
# first = []
# middle = []
# title = []
# leave = []
# visiting = []
# for faculty in cleaned: 

#     if(len(faculty[0]) == 2): 
#         last.append(faculty[0][1])
#         middle.append(None)
#         first.append(faculty[0][0])

#     elif(len(faculty[0]) == 3): 
#         last.append(faculty[0][2])
#         middle.append(faculty[0][1])
#         first.append(faculty[0][0])

#     elif(len(faculty[0]) > 3): 
#         print(faculty[0])

#     title.append(faculty[1])
#     leave.append(faculty[2])
#     visiting.append(faculty[3])

# df = pd.DataFrame()
# df['last'] = last
# df['first'] = first
# df['middle'] = middle 
# df['title'] = title
# df['leave'] = leave
# df['visiting'] = visiting

# df.sort_values('last', inplace=True)

# filepath = Path('/Users/laurenmccarey/math308/14-15/faculty14-15.csv')  
# filepath.parent.mkdir(parents=True, exist_ok=True)  
# df.to_csv(filepath)  

    
