import pdfplumber 
import pandas as pd
import csv
from pathlib import Path 

# text = ''
# for i in range(77, 105): 
#     with pdfplumber.open('/Users/laurenmccarey/math308/20-21/catalog_2020-21.pdf') as temp: 
#         page = temp.pages[i]
#         text = page.extract_text()
#     with open ('catalog_2020-21.txt', 'a') as f: 
#         f.write(text)

lines = []
with open ('catalog_2020-21.txt') as f: 
    lines = f.readlines()

for line in lines: 
    print(line)
    for c in line: 
        if (c == ";"):
            c = ","
    print(line)
    break 

# cleaned = []
# for line in lines: 
#     # print('\n')
#     line = line.split(',', maxsplit=2)
#     line = [item.strip(' \n') for item in line]

#     if (len(line) == 3): 
#         if ("on leave" in line[2]): 
#             if ("on leave Fall 2019" in line[2]): 
#                 line.append('f') 
#                 line[2] = line[2].replace(", on leave Fall 2019", '')
#             if ("on leave Spring 2020" in line[2]): 
#                 line.append('s')
#                 line[2] = line[2].replace(";, on leave Spring 2020", '')
#             if ("on leave 2019-2020" in line[2]): 
#                 line.append('y')
#                 line[2] = line[2].replace(", on leave 2019-2020", '') 
#             # print(line)
#         else: 
#             line.append('n')
#     if (len(line) == 2): 
#         line.append('none')
#         line.append('n')
#     if (len(line) == 1): 
#         line.append("none")
#         line.append("none")
#         line.append('n')
#     cleaned.append(line)

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
# filepath = Path('/Users/laurenmccarey/math308/19-20/faculty19-20.csv')  
# filepath.parent.mkdir(parents=True, exist_ok=True)  
# df.to_csv(filepath)  
