import pdfplumber 
import pandas as pd
import csv
from pathlib import Path 

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

    if ("Women, Gender & Sexuality Stdy" in line): 
        line = line.replace("Women, Gender & Sexuality Stdy", "WGGS")

    elif ("Women's, Gender and Sexuality Studies" in line): 
        line = line.replace("Women's, Gender and Sexuality Studies", "WGGS")

    elif ("Women's, Gender, and Sexuality Studies" in line): 
        line = line.replace("Women's, Gender, and Sexuality Studies", "WGGS")

    elif (", Jr." in line): 
        line = line.replace(", Jr.", " Jr.")
    
    line = line.split(";", maxsplit=1)

    if (len(line) > 1): 
        line[1] = line[1].strip()
    else: 
        line.append(None)

    line[0] = line[0].split(",", maxsplit=1)
    line[0] = [item.strip() for item in line[0]]

    print(line)

    # line = line.split(',', maxsplit=2)
    # line = [item.strip(' \n') for item in line]


#     if (len(line) == 3): 
#         if ("on leave" in line[2]): 
#             if ("on leave Fall 2020" in line[2]): 
#                 line.append('f') 
#                 line[2] = line[2].replace(", on leave Fall 2020", '')
#             if ("on leave Spring 2021" in line[2]): 
#                 line.append('s')
#                 line[2] = line[2].replace(";, on leave Spring 2021", '')
#             if ("on leave 2020-2021" in line[2]): 
#                 line.append('y')
#                 line[2] = line[2].replace(", on leave 2020-2021", '') 
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
