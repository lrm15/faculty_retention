import pdfplumber 
import pandas as pd
import csv
from pathlib import Path 

# text = ''
# for i in range(86, 87): 
#     with pdfplumber.open('/Users/laurenmccarey/math308/21-22/catalog_2021-22.pdf') as temp: 
#         page = temp.pages[i]
#         text = page.extract_text()
#     with open ('temp.txt', 'a') as f: 
#         f.write(text)

# text = ''
# for i in range(87, 112): 
#     with pdfplumber.open('/Users/laurenmccarey/math308/21-22/catalog_2021-22.pdf') as temp: 
#         page = temp.pages[i]
#         text = page.extract_text()
#     with open ('catalog_2021-22.txt', 'a') as f: 
#         f.write(text)
#     print(i)

lines = []
with open ('catalog_2021-22.txt') as f: 
    lines = f.readlines()

cleaned = []
for line in lines: 

    line = line.lower()

    if ("women, gender & sexuality stdy" in line): 
        line = line.replace("women, gender & sexuality stdy", "WGGS")

    elif ("women's, gender and sexuality studies" in line): 
        line = line.replace("women's, gender and sexuality studies", "WGGS")

    elif ("women's, gender, and sexuality studies" in line): 
        line = line.replace("women's, gender, and sexuality studies", "WGGS")

    elif (", jr." in line): 
        line = line.replace(", jr.", " jr.")
    
    line = line.split(";", maxsplit=1)

    if (len(line) > 1): 
        line[1] = line[1].strip()
    else: 
        line.append(None)

    line[0] = line[0].split(",", maxsplit=1)
    line[0] = [item.strip() for item in line[0]]

    line[0][0] = line[0][0].split(" ", maxsplit=2)
    line[0][0] = [item.strip() for item in line[0][0]]

    if (line[1]): 
        if ("on leave fall 2021" in line[1]): 
            line.append("f")
            line[1] = line[1].replace("; on leave fall 2021", "")
        elif ("on leave spring 2022" in line[1]): 
            line.append("s")
            line[1] = line[1].replace("; on leave spring 2022", "")
        elif ("on leave 2021-2022" in line[1]): 
            line.append("y")
            line[1] = line[1].replace("on leave 2021-2022", "")
        else:
            line.append("n")

    else: 
        line.append("n") 
    
    if (len(line) < 3): 
        print(line)
        break

    if ("visiting" in line[0][1]): 
        line.append(1)
    else: 
        line.append(0)

        
    cleaned.append(line)

last = []
first = []
middle = []
title = []
degrees = []
leave = []
visiting = []

for faculty in cleaned: 
    
    if (len(faculty) < 3): 
        print(faculty)
        break 

    if (len(faculty[0][0]) == 3): 
        last.append(faculty[0][0][0])
        middle.append(faculty[0][0][1])
        first.append(faculty[0][0][2])
    elif (len(faculty[0][0]) == 2): 
        last.append(faculty[0][0][0])
        middle.append(None)
        first.append(faculty[0][0][1])
    
    title.append(faculty[0][1])

    degrees.append(faculty[1])

    leave.append(faculty[2])

    visiting.append(faculty[3])

# print(len(first))
# print(len(last))
# print(len(middle))
# print(len(title))
# print(len(degrees))
# print(len(leave))
# print(len(visiting))

df = pd.DataFrame()
df['last'] = last 
df['first'] = first
df['middle'] = middle 
df['title'] = title
df['degrees'] = degrees 
df['leave'] = leave
df['visiting'] = visiting 

# print(df)

filepath = Path('/Users/laurenmccarey/math308/21-22/faculty21-22.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
df.to_csv(filepath)  


