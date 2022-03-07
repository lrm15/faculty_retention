import pdfplumber 
import pandas as pd
import csv
from pathlib import Path 

# text = ''
# for i in range(550, 556): 
#     with pdfplumber.open('/Users/laurenmccarey/math308/17-18/catalog_2017-18.pdf') as temp: 
#         page = temp.pages[i]
#         text = page.extract_text()
#     with open ('catalog_2017-18.txt', 'a') as f: 
#         f.write(text)

# lines = []
# with open ('catalog_2017-18.txt') as f: 
#     lines = f.readlines()

# cleaned = []
# for line in lines: 

#     line = line.lower()

#     # these phrases contains a comma - replace with abbreviation so we can split by comma reliably 
#     if ("women's, gender and sexuality studies" in line): 
#         line = line.replace("women's, gender and sexuality studies", "wggs")

#     elif ("women's, gender, and sexuality studies" in line): 
#         line = line.replace("women's, gender, and sexuality studies", "wggs")

#     elif (", jr." in line): 
#         line = line.replace(", jr.", " jr.")

#     line = line.split(':')
#     line[0] = line[0].split(',', maxsplit=1)
#     line[0] = [item.strip() for item in line[0]]
    
#     if (len(line) == 1): 
#         line.append(None)

#     elif (len(line) == 2): 
#         line[1] = line[1].strip()

#     # check for cases to be fixed 
#     if (len(line) > 2): 
#         print("more than two fields")
#         print(line)
#         break
    
#     # make sure all fields are present in all entries 
#     if (len(line) < 2):
#         print("fewer than two fields")
#         print(line) 
#         break

#     # code s if the faculty member is on leave in the spring, f if on leave in fall, y if on leave all year, and n if not on leave 
#     if (line[1] != None): 
#         if ("on leave fall 2017" in line[1]): 
#             line.append('f') 
#             # print(line)
#             line[1] = line[1].replace("on leave fall 2017", '')        
#         elif ("on leave spring 2018" in line[1]): 
#             line.append('s')        
#             # print(line)     
#             line[1] = line[1].replace("on leave spring 2018", '') 
#         elif ("on leave 2017-2018" in line[1]): 
#             line.append('y')
#             # print(line)
#             line[1] = line[1].replace("on leave 2017-2018", '') 
#         else: 
#             if ("leave" in line[1]): 
#                 print(line)
#                 break
#             line.append('n')
#     else: 
#         if ("leave" in line[0]): 
#             print(line)
#             break
#         line.append('n')

#     if (len(line) < 3): 
#         print(line)
#         break

#     # code 1 if the faculty member is visiting and 0 otherwise 
#     if ("visiting" in line[0][1]): 
#         line.append(1)
#     else: 
#         line.append(0)

#     # make sure all lines have 5 fields 
#     if (len(line) != 4): 
#         print(line)
#         break

#     # split name into first, middle, and last 
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
#     if (faculty[0][1]): 
#         title.append(faculty[0][1])
#     else: 
#         title.append(None)

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

# # print(df)

# # df.sort_values('last', inplace=True)

# filepath = Path('/Users/laurenmccarey/math308/17-18/faculty17-18.csv')  
# filepath.parent.mkdir(parents=True, exist_ok=True)  
# df.to_csv(filepath)  

